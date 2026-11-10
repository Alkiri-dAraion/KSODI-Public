#!/usr/bin/env python3
"""Generate dependency-free IK_rel Phase-A formula and collision fixtures."""

from __future__ import annotations

import csv
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent
GRID_OUTPUT = ROOT / "phase_a_primary_grid.csv"
COLLISION_OUTPUT = ROOT / "phase_a_projection_collisions.csv"

GRID_VALUES = tuple(Fraction(value, 2) for value in (-2, -1, 0, 1, 2))
COORDINATES = ("K", "S", "O", "D", "I")
SYNTHETIC_R0_THRESHOLD = Fraction(1, 2)


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def decimal_text(value: Fraction) -> str:
    return f"{float(value):.12f}"


def vector_text(values: tuple[Fraction, ...]) -> str:
    return "(" + ",".join(fraction_text(value) for value in values) + ")"


def subtract(
    target: tuple[Fraction, ...], start: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    return tuple(target[index] - start[index] for index in range(5))


def ik_delta(delta_z: tuple[Fraction, ...]) -> Fraction:
    return sum(delta_z, Fraction(0)) / 5


def l1_drift(delta_z: tuple[Fraction, ...]) -> Fraction:
    return sum((abs(value) for value in delta_z), Fraction(0)) / 5


def c_move(delta_a: Fraction, delta_b: Fraction) -> Fraction:
    return 1 - abs(delta_a - delta_b) / 2


def primary_status_epsilon_zero(
    delta_a: Fraction, delta_b: Fraction
) -> str:
    if delta_a == 0 and delta_b == 0:
        return "not_applicable_joint_projected_zero"
    return "numeric"


def write_grid() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for row_index, delta_a in enumerate(GRID_VALUES, start=1):
        for column_index, delta_b in enumerate(GRID_VALUES, start=1):
            gap = abs(delta_a - delta_b)
            value = c_move(delta_a, delta_b)
            swapped = c_move(delta_b, delta_a)
            assert Fraction(0) <= gap <= 2
            assert Fraction(0) <= value <= 1
            assert value == swapped
            rows.append(
                {
                    "case_id": f"A-GRID-{row_index:02d}-{column_index:02d}",
                    "delta_ik_a_exact": fraction_text(delta_a),
                    "delta_ik_b_exact": fraction_text(delta_b),
                    "movement_gap_exact": fraction_text(gap),
                    "c_move_exact": fraction_text(value),
                    "c_move_decimal": decimal_text(value),
                    "swapped_c_move_exact": fraction_text(swapped),
                    "phase_a_epsilon_move": "0",
                    "method_status_epsilon_0": primary_status_epsilon_zero(
                        delta_a, delta_b
                    ),
                    "joint_r0_feasibility": "not_tested_until_phase_d",
                }
            )

    with GRID_OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows


ZERO = Fraction(0)
ONE = Fraction(1)
Z0 = (ZERO, ZERO, ZERO, ZERO, ZERO)
EK = (ONE, ZERO, ZERO, ZERO, ZERO)
ES = (ZERO, ONE, ZERO, ZERO, ZERO)
EO = (ZERO, ZERO, ONE, ZERO, ZERO)
ED = (ZERO, ZERO, ZERO, ONE, ZERO)

COLLISION_CASES = (
    (
        "A-COLL-01",
        "equal_positive_projection_different_coordinates",
        Z0,
        EK,
        Z0,
        ES,
    ),
    (
        "A-COLL-02",
        "equal_negative_projection_different_coordinates",
        EK,
        Z0,
        ES,
        Z0,
    ),
    (
        "A-COLL-03",
        "disjoint_zero_sum_transfers",
        EK,
        ES,
        EO,
        ED,
    ),
    (
        "A-COLL-04",
        "projected_stillness_vs_full_coordinate_transfer",
        Z0,
        Z0,
        EK,
        ES,
    ),
    (
        "A-COLL-05",
        "positive_shift_against_projected_stillness",
        Z0,
        EK,
        Z0,
        Z0,
    ),
    (
        "A-COLL-06",
        "projected_stillness_against_negative_shift",
        Z0,
        Z0,
        ES,
        Z0,
    ),
)


def write_collisions() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for case_id, description, start_a, target_a, start_b, target_b in COLLISION_CASES:
        delta_z_a = subtract(target_a, start_a)
        delta_z_b = subtract(target_b, start_b)
        delta_a = ik_delta(delta_z_a)
        delta_b = ik_delta(delta_z_b)
        drift_a = l1_drift(delta_z_a)
        drift_b = l1_drift(delta_z_b)
        r0_value = 1 - (drift_a + drift_b) / 2
        value = c_move(delta_a, delta_b)
        delta_z_distance = math.sqrt(
            sum(float(a - b) ** 2 for a, b in zip(delta_z_a, delta_z_b)) / 5
        )

        assert all(ZERO <= value_part <= ONE for value_part in start_a + target_a)
        assert all(ZERO <= value_part <= ONE for value_part in start_b + target_b)
        assert r0_value >= SYNTHETIC_R0_THRESHOLD
        assert Fraction(0) <= value <= 1

        rows.append(
            {
                "case_id": case_id,
                "description": description,
                "coordinate_order": "K,S,O,D,I",
                "z_a_start": vector_text(start_a),
                "z_a_target": vector_text(target_a),
                "delta_z_a": vector_text(delta_z_a),
                "delta_ik_a_exact": fraction_text(delta_a),
                "z_b_start": vector_text(start_b),
                "z_b_target": vector_text(target_b),
                "delta_z_b": vector_text(delta_z_b),
                "delta_ik_b_exact": fraction_text(delta_b),
                "delta_z_vectors_equal": str(delta_z_a == delta_z_b).lower(),
                "normalized_delta_z_distance_decimal": f"{delta_z_distance:.12f}",
                "c_move_exact": fraction_text(value),
                "c_move_decimal": decimal_text(value),
                "method_status_epsilon_0": primary_status_epsilon_zero(
                    delta_a, delta_b
                ),
                "r0_l1_drift_a_exact": fraction_text(drift_a),
                "r0_l1_drift_b_exact": fraction_text(drift_b),
                "synthetic_r0_value_exact": fraction_text(r0_value),
                "synthetic_r0_threshold_exact": fraction_text(
                    SYNTHETIC_R0_THRESHOLD
                ),
                "synthetic_r0_gate_state": "open",
            }
        )

    assert rows[0]["c_move_exact"] == "1"
    assert rows[2]["method_status_epsilon_0"] == (
        "not_applicable_joint_projected_zero"
    )
    assert rows[3]["delta_z_vectors_equal"] == "false"
    assert rows[4]["c_move_exact"] == rows[5]["c_move_exact"] == "9/10"

    with COLLISION_OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows


def main() -> None:
    grid_rows = write_grid()
    collision_rows = write_collisions()
    raw_scores = sorted({row["c_move_exact"] for row in grid_rows})
    score_counts = Counter(row["c_move_exact"] for row in grid_rows)
    assert score_counts == {
        "1": 5,
        "3/4": 8,
        "1/2": 6,
        "1/4": 4,
        "0": 2,
    }
    numeric_rows = sum(
        row["method_status_epsilon_0"] == "numeric" for row in grid_rows
    )
    print(f"verified_formula_grid_rows={len(grid_rows)}")
    print(f"numeric_rows_under_epsilon_0={numeric_rows}")
    print("joint_projected_zero_rows=1")
    print(f"unique_formula_scores={len(raw_scores)}")
    print(f"verified_open_r0_collision_rows={len(collision_rows)}")
    print(f"synthetic_r0_threshold={fraction_text(SYNTHETIC_R0_THRESHOLD)}")
    print(f"grid_output={GRID_OUTPUT.name}")
    print(f"collision_output={COLLISION_OUTPUT.name}")


if __name__ == "__main__":
    main()
