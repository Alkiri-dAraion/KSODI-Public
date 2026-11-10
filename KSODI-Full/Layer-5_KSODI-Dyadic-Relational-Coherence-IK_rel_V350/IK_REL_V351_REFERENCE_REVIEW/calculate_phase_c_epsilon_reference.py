#!/usr/bin/env python3
"""Generate dependency-free IK_rel Phase-C epsilon-boundary fixtures."""

from __future__ import annotations

import csv
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BOUNDARY_OUTPUT = ROOT / "phase_c_epsilon_boundaries.csv"
ORDER_OUTPUT = ROOT / "phase_c_derivative_order_statuses.csv"

EPSILON_MOVE = Fraction(1, 10)
EPSILON_ACCEL = Fraction(1, 5)
PROBE_STEP = Fraction(1, 100)
EPSILON_POLICY_IDS = {
    "move": "phase_c_move_test_control_v351",
    "accel": "phase_c_accel_test_control_v351",
}
EPSILON_PARAMETER_ORIGIN = "synthetic_reference_fixture"
EPSILON_CALIBRATION_STATUS = "set_not_empirically_calibrated"


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def decimal_text(value: Fraction) -> str:
    return f"{float(value):.12f}"


def component_value(kind: str, value_a: Fraction, value_b: Fraction) -> Fraction:
    divisor = {"move": 2, "accel": 4}[kind]
    return 1 - abs(value_a - value_b) / divisor


def method_status(
    kind: str,
    value_a: Fraction,
    value_b: Fraction,
    epsilon: Fraction,
) -> str:
    if abs(value_a) <= epsilon and abs(value_b) <= epsilon:
        return f"not_applicable_joint_{kind}_epsilon_band"
    return "numeric"


def boundary_cases(epsilon: Fraction) -> tuple[tuple[str, Fraction, Fraction], ...]:
    below = epsilon - PROBE_STEP
    above = epsilon + PROBE_STEP
    return (
        ("joint_exact_zero", Fraction(0), Fraction(0)),
        ("joint_equal_below_positive", below, below),
        ("joint_equal_at_positive_boundary", epsilon, epsilon),
        ("joint_equal_above_positive_boundary", above, above),
        ("opposite_at_band_edges", -epsilon, epsilon),
        ("opposite_outside_band", -above, above),
        ("one_sided_zero_other_inside", Fraction(0), below),
        ("one_sided_zero_other_at_boundary", Fraction(0), epsilon),
        ("one_sided_zero_other_outside", Fraction(0), above),
        ("one_inside_one_outside", below, above),
        ("joint_equal_at_negative_boundary", -epsilon, -epsilon),
    )


def write_boundaries() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for kind, epsilon in (("move", EPSILON_MOVE), ("accel", EPSILON_ACCEL)):
        for index, (description, value_a, value_b) in enumerate(
            boundary_cases(epsilon), start=1
        ):
            raw_value = component_value(kind, value_a, value_b)
            status = method_status(kind, value_a, value_b, epsilon)
            method_value = raw_value if status == "numeric" else None
            assert Fraction(0) <= raw_value <= 1
            rows.append(
                {
                    "case_id": f"C-{kind.upper()}-{index:02d}",
                    "component_kind": kind,
                    "description": description,
                    "epsilon_exact": fraction_text(epsilon),
                    "epsilon_policy_id": EPSILON_POLICY_IDS[kind],
                    "epsilon_parameter_origin": EPSILON_PARAMETER_ORIGIN,
                    "epsilon_calibration_status": EPSILON_CALIBRATION_STATUS,
                    "probe_step_exact": fraction_text(PROBE_STEP),
                    "input_a_exact": fraction_text(value_a),
                    "input_b_exact": fraction_text(value_b),
                    "raw_component_exact": fraction_text(raw_value),
                    "raw_component_decimal": decimal_text(raw_value),
                    "method_status": status,
                    "method_value_exact": (
                        fraction_text(method_value) if method_value is not None else ""
                    ),
                    "boundary_operator": "absolute_input_less_than_or_equal_epsilon",
                }
            )

    assert rows[2]["method_status"].startswith("not_applicable")
    assert rows[3]["method_status"] == "numeric"
    assert rows[7]["method_status"].startswith("not_applicable")
    assert rows[8]["method_status"] == "numeric"
    with BOUNDARY_OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows


def derive(sequence: tuple[Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    x0, x1, x2 = sequence
    return x2 - x1, x2 - 2 * x1 + x0


def sequence_text(values: tuple[Fraction, ...]) -> str:
    return "(" + ",".join(fraction_text(value) for value in values) + ")"


def write_derivative_order_cases() -> list[dict[str, str]]:
    cases = (
        (
            "C-ORDER-01",
            "equal_nonzero_constant_velocity_move_numeric_accel_not_applicable",
            (Fraction(0), Fraction(1, 4), Fraction(1, 2)),
            (Fraction(0), Fraction(1, 4), Fraction(1, 2)),
        ),
        (
            "C-ORDER-02",
            "joint_current_rest_move_not_applicable_accel_numeric",
            (Fraction(0), Fraction(1, 2), Fraction(1, 2)),
            (Fraction(0), Fraction(1, 4), Fraction(1, 4)),
        ),
    )
    rows: list[dict[str, str]] = []
    for case_id, description, trajectory_a, trajectory_b in cases:
        delta_a, delta2_a = derive(trajectory_a)
        delta_b, delta2_b = derive(trajectory_b)
        move_status = method_status("move", delta_a, delta_b, EPSILON_MOVE)
        accel_status = method_status("accel", delta2_a, delta2_b, EPSILON_ACCEL)
        row = {
            "case_id": case_id,
            "description": description,
            "trajectory_a": sequence_text(trajectory_a),
            "trajectory_b": sequence_text(trajectory_b),
            "delta_a_exact": fraction_text(delta_a),
            "delta_b_exact": fraction_text(delta_b),
            "delta2_a_exact": fraction_text(delta2_a),
            "delta2_b_exact": fraction_text(delta2_b),
            "c_move_raw_exact": fraction_text(component_value("move", delta_a, delta_b)),
            "c_move_status": move_status,
            "c_accel_raw_exact": fraction_text(component_value("accel", delta2_a, delta2_b)),
            "c_accel_status": accel_status,
            "epsilon_move_exact": fraction_text(EPSILON_MOVE),
            "epsilon_move_policy_id": EPSILON_POLICY_IDS["move"],
            "epsilon_move_parameter_origin": EPSILON_PARAMETER_ORIGIN,
            "epsilon_move_calibration_status": EPSILON_CALIBRATION_STATUS,
            "epsilon_accel_exact": fraction_text(EPSILON_ACCEL),
            "epsilon_accel_policy_id": EPSILON_POLICY_IDS["accel"],
            "epsilon_accel_parameter_origin": EPSILON_PARAMETER_ORIGIN,
            "epsilon_accel_calibration_status": EPSILON_CALIBRATION_STATUS,
        }
        rows.append(row)

    assert rows[0]["c_move_status"] == "numeric"
    assert rows[0]["c_accel_status"].startswith("not_applicable")
    assert rows[1]["c_move_status"].startswith("not_applicable")
    assert rows[1]["c_accel_status"] == "numeric"
    with ORDER_OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows


def main() -> None:
    boundaries = write_boundaries()
    order_cases = write_derivative_order_cases()
    numeric = sum(row["method_status"] == "numeric" for row in boundaries)
    not_applicable = len(boundaries) - numeric
    print(f"verified_boundary_rows={len(boundaries)}")
    print(f"numeric_boundary_rows={numeric}")
    print(f"not_applicable_boundary_rows={not_applicable}")
    print(f"verified_derivative_order_cases={len(order_cases)}")
    print(f"epsilon_move_test_only={fraction_text(EPSILON_MOVE)}")
    print(f"epsilon_accel_test_only={fraction_text(EPSILON_ACCEL)}")
    print(f"boundary_output={BOUNDARY_OUTPUT.name}")
    print(f"order_output={ORDER_OUTPUT.name}")


if __name__ == "__main__":
    main()
