#!/usr/bin/env python3
"""Generate exact complete-Z Phase-D+ R0 gate-exclusion fixtures."""

from __future__ import annotations

import csv
import hashlib
from fractions import Fraction
from pathlib import Path
from typing import NamedTuple


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "phase_d_plus_gate_exclusion_complete_z.csv"

ZERO = Fraction(0)
ONE = Fraction(1)
VECTOR_SIZE = 5
EPSILON_MOVE = ZERO

Z = tuple[Fraction, Fraction, Fraction, Fraction, Fraction]


class Fixture(NamedTuple):
    case_id: str
    description: str
    z_a_before: Z
    z_a_after: Z
    z_b_before: Z
    z_b_after: Z
    threshold: Fraction
    expected_r0: Fraction
    expected_gate: str
    expected_result_status: str
    expected_result_reason: str


def z(*values: Fraction | int) -> Z:
    assert len(values) == VECTOR_SIZE
    return tuple(Fraction(value) for value in values)  # type: ignore[return-value]


FIXTURES: tuple[Fixture, ...] = (
    Fixture(
        "D+01",
        "strong_equal_projected_movement_behind_closed_gate",
        z(0, 0, 0, 0, 0),
        z(Fraction(3, 4), Fraction(3, 4), Fraction(3, 4), Fraction(3, 4), Fraction(3, 4)),
        z(0, 0, 0, 0, 0),
        z(Fraction(3, 4), Fraction(3, 4), Fraction(3, 4), Fraction(3, 4), Fraction(3, 4)),
        Fraction(1, 2),
        Fraction(1, 4),
        "closed",
        "not_applicable",
        "gate_closed",
    ),
    Fixture(
        "D+02",
        "threshold_equality_opens",
        z(0, 0, 0, 0, 0),
        z(Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2)),
        z(0, 0, 0, 0, 0),
        z(Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2)),
        Fraction(1, 2),
        Fraction(1, 2),
        "open",
        "numeric",
        "exact_primary_move_result",
    ),
    Fixture(
        "D+03",
        "equal_projection_off_axis_drift_closes_gate",
        z(0, 0, 0, 0, 0),
        z(Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2), Fraction(1, 2)),
        z(0, 0, 0, 0, Fraction(1, 10)),
        z(Fraction(13, 20), Fraction(13, 20), Fraction(13, 20), Fraction(13, 20), 0),
        Fraction(1, 2),
        Fraction(12, 25),
        "closed",
        "not_applicable",
        "gate_closed",
    ),
    Fixture(
        "D+04",
        "changed_threshold_profile_opens_same_movement",
        z(0, 0, 0, 0, 0),
        z(Fraction(3, 4), Fraction(3, 4), Fraction(3, 4), Fraction(3, 4), Fraction(3, 4)),
        z(0, 0, 0, 0, 0),
        z(Fraction(3, 4), Fraction(3, 4), Fraction(3, 4), Fraction(3, 4), Fraction(3, 4)),
        Fraction(1, 5),
        Fraction(1, 4),
        "open",
        "numeric",
        "exact_primary_move_result",
    ),
    Fixture(
        "D+05",
        "open_gate_but_joint_projected_zero",
        z(0, Fraction(1, 5), 0, 0, 0),
        z(Fraction(1, 5), 0, 0, 0, 0),
        z(0, Fraction(1, 5), 0, 0, 0),
        z(Fraction(1, 5), 0, 0, 0, 0),
        Fraction(1, 2),
        Fraction(23, 25),
        "open",
        "not_applicable",
        "joint_projected_zero_under_numeric_policy",
    ),
)


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def decimal_text(value: Fraction) -> str:
    return f"{float(value):.12f}"


def vector_text(vector: Z) -> str:
    return "(" + ",".join(fraction_text(value) for value in vector) + ")"


def subtract(left: Z, right: Z) -> Z:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def mean(vector: Z) -> Fraction:
    return sum(vector, ZERO) / VECTOR_SIZE


def normalized_l1(vector: Z) -> Fraction:
    return sum((abs(value) for value in vector), ZERO) / VECTOR_SIZE


def clip_unit(value: Fraction) -> Fraction:
    return min(ONE, max(ZERO, value))


def evaluate(fixture: Fixture) -> dict[str, str]:
    all_states = (
        fixture.z_a_before,
        fixture.z_a_after,
        fixture.z_b_before,
        fixture.z_b_after,
    )
    assert all(ZERO <= coordinate <= ONE for state in all_states for coordinate in state)

    delta_z_a = subtract(fixture.z_a_after, fixture.z_a_before)
    delta_z_b = subtract(fixture.z_b_after, fixture.z_b_before)
    ik_a_before = mean(fixture.z_a_before)
    ik_a_after = mean(fixture.z_a_after)
    ik_b_before = mean(fixture.z_b_before)
    ik_b_after = mean(fixture.z_b_after)
    delta_ik_a = ik_a_after - ik_a_before
    delta_ik_b = ik_b_after - ik_b_before
    drift_a = normalized_l1(delta_z_a)
    drift_b = normalized_l1(delta_z_b)
    r0_raw = ONE - (drift_a + drift_b) / 2
    r0 = clip_unit(r0_raw)
    gate_state = "open" if r0 >= fixture.threshold else "closed"
    c_move_raw = ONE - abs(delta_ik_a - delta_ik_b) / 2

    if gate_state == "closed":
        result_status = "not_applicable"
        result_reason = "gate_closed"
        result_value = ""
    elif abs(delta_ik_a) <= EPSILON_MOVE and abs(delta_ik_b) <= EPSILON_MOVE:
        result_status = "not_applicable"
        result_reason = "joint_projected_zero_under_numeric_policy"
        result_value = ""
    else:
        result_status = "numeric"
        result_reason = "exact_primary_move_result"
        result_value = fraction_text(c_move_raw)

    assert r0 == fixture.expected_r0
    assert gate_state == fixture.expected_gate
    assert result_status == fixture.expected_result_status
    assert result_reason == fixture.expected_result_reason
    assert c_move_raw == ONE

    suffix = fixture.case_id.replace("+", "PLUS")
    threshold_profile = "r0_fixture_theta_1_5" if fixture.threshold == Fraction(1, 5) else "r0_fixture_theta_1_2"
    return {
        "case_id": fixture.case_id,
        "description": fixture.description,
        "source_a_id": "synthetic_source_A",
        "source_b_id": "synthetic_source_B",
        "ordered_dyad_id": "synthetic_source_A__synthetic_source_B",
        "pairing_map_id": f"pairing_{suffix}",
        "relational_eval_id": f"rho_{suffix}",
        "pairing_status": "valid_explicit_synthetic_pairing",
        "source_attribution_status": "synthetic_fixture_declared",
        "event_a_predecessor_id": f"A_{suffix}_prev",
        "event_a_target_id": f"A_{suffix}_target",
        "event_b_predecessor_id": f"B_{suffix}_prev",
        "event_b_target_id": f"B_{suffix}_target",
        "native_basis": "complete_typed_z_5d_exact_rational",
        "normalization_profile": "unit_interval_equal_coordinate_reference",
        "ik_profile_id": "ik_w_equal_weight_mean_v351_fixture",
        "r0_profile_id": f"r0_complete_l1_mean_{threshold_profile}",
        "ik_rel_profile_id": "ik_rel_primary_move_epsilon_exact_zero_fixture",
        "z_a_before_exact": vector_text(fixture.z_a_before),
        "z_a_after_exact": vector_text(fixture.z_a_after),
        "delta_z_a_exact": vector_text(delta_z_a),
        "z_b_before_exact": vector_text(fixture.z_b_before),
        "z_b_after_exact": vector_text(fixture.z_b_after),
        "delta_z_b_exact": vector_text(delta_z_b),
        "ik_w_a_before_exact": fraction_text(ik_a_before),
        "ik_w_a_after_exact": fraction_text(ik_a_after),
        "delta_ik_w_a_exact": fraction_text(delta_ik_a),
        "ik_w_b_before_exact": fraction_text(ik_b_before),
        "ik_w_b_after_exact": fraction_text(ik_b_after),
        "delta_ik_w_b_exact": fraction_text(delta_ik_b),
        "d_a_l1_exact": fraction_text(drift_a),
        "d_b_l1_exact": fraction_text(drift_b),
        "r0_raw_exact": fraction_text(r0_raw),
        "r0_exact": fraction_text(r0),
        "r0_decimal": decimal_text(r0),
        "r0_threshold_exact": fraction_text(fixture.threshold),
        "r0_status": "numeric",
        "r0_gate_state": gate_state,
        "epsilon_move_exact": fraction_text(EPSILON_MOVE),
        "c_move_raw_exact": fraction_text(c_move_raw),
        "c_move_raw_decimal": decimal_text(c_move_raw),
        "ik_rel_status": result_status,
        "ik_rel_reason": result_reason,
        "ik_rel_value_exact": result_value,
        "source_local_predecessor_contract": "valid_separate",
        "required_profiles_compatible": "true",
        "relational_opportunity_declared": "true",
        "excluded_opportunity_retained": str(result_status != "numeric").lower(),
        "complete_operands_retained": "true",
        "profile_and_provenance_retained": "true",
    }


def write_rows() -> list[dict[str, str]]:
    rows = [evaluate(fixture) for fixture in FIXTURES]
    assert len(rows) == 5
    assert sum(row["r0_gate_state"] == "closed" for row in rows) == 2
    assert sum(row["r0_gate_state"] == "open" for row in rows) == 3
    assert sum(row["ik_rel_status"] == "numeric" for row in rows) == 2
    assert sum(row["ik_rel_reason"] == "gate_closed" for row in rows) == 2
    assert sum(
        row["ik_rel_reason"] == "joint_projected_zero_under_numeric_policy"
        for row in rows
    ) == 1

    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    rows = write_rows()
    print(f"verified_complete_z_cases={len(rows)}")
    print(f"closed_gate_cases={sum(row['r0_gate_state'] == 'closed' for row in rows)}")
    print(f"open_gate_cases={sum(row['r0_gate_state'] == 'open' for row in rows)}")
    print(f"numeric_ik_rel_cases={sum(row['ik_rel_status'] == 'numeric' for row in rows)}")
    print(f"nonnumeric_ik_rel_cases={sum(row['ik_rel_status'] != 'numeric' for row in rows)}")
    print(f"output={OUTPUT.name}")
    print(f"sha256={sha256(OUTPUT)}")


if __name__ == "__main__":
    main()
