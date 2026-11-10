#!/usr/bin/env python3
"""Generate dependency-free IK_rel Phase-D R0 handoff fixtures."""

from __future__ import annotations

import csv
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent
FEASIBILITY_OUTPUT = ROOT / "phase_d_projected_r0_feasibility.csv"
PRECEDENCE_OUTPUT = ROOT / "phase_d_handoff_precedence.csv"

GRID_VALUES = tuple(Fraction(value, 2) for value in (-2, -1, 0, 1, 2))
THRESHOLD = Fraction(1, 2)


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def decimal_text(value: Fraction) -> str:
    return f"{float(value):.12f}"


def write_projected_feasibility() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for row_index, delta_a in enumerate(GRID_VALUES, start=1):
        for column_index, delta_b in enumerate(GRID_VALUES, start=1):
            minimum_l1_a = abs(delta_a)
            minimum_l1_b = abs(delta_b)
            maximum_r0 = 1 - (minimum_l1_a + minimum_l1_b) / 2
            existential_open = maximum_r0 >= THRESHOLD
            rows.append(
                {
                    "case_id": f"D-FEAS-{row_index:02d}-{column_index:02d}",
                    "delta_ik_a_exact": fraction_text(delta_a),
                    "delta_ik_b_exact": fraction_text(delta_b),
                    "minimum_possible_l1_drift_a_exact": fraction_text(minimum_l1_a),
                    "minimum_possible_l1_drift_b_exact": fraction_text(minimum_l1_b),
                    "maximum_possible_r0_exact": fraction_text(maximum_r0),
                    "maximum_possible_r0_decimal": decimal_text(maximum_r0),
                    "synthetic_threshold_exact": fraction_text(THRESHOLD),
                    "some_complete_z_realization_can_open": str(existential_open).lower(),
                    "every_complete_z_realization_opens": "false",
                    "actual_gate_requires_complete_delta_z": "true",
                }
            )

    assert sum(row["some_complete_z_realization_can_open"] == "true" for row in rows) == 13
    assert sum(row["some_complete_z_realization_can_open"] == "false" for row in rows) == 12
    with FEASIBILITY_OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows


DEFAULTS: dict[str, object] = {
    "profile_selected": True,
    "profile_valid": True,
    "pairing_valid": True,
    "r0_record": "valid",
    "r0_status": "numeric",
    "r0_kind": "dyad",
    "r0_projection": "complete",
    "r0_identity_match": True,
    "r0_profile_match": True,
    "r0_threshold_match": True,
    "r0_gate_consistent": True,
    "r0_gate_state": "open",
    "monadic_inputs": "numeric",
    "predecessor_contract": "valid_separate",
    "ik_profile_match": True,
}


def outcome(case: dict[str, object]) -> tuple[str, str]:
    if not case["profile_selected"]:
        return "not_selected", "ik_rel_profile_absent"
    if not case["profile_valid"]:
        return "processing_error", "invalid_ik_rel_profile"
    if not case["pairing_valid"]:
        return "processing_error", "invalid_pairing_identity"
    if case["r0_record"] == "processing":
        return "processing_block", "upstream_r0_has_no_valid_result"
    if case["r0_record"] == "absent":
        return "not_applicable", "qualifying_r0_absent"
    if not case["r0_identity_match"]:
        return "processing_error", "r0_pairing_or_member_identity_mismatch"
    if case["r0_status"] == "not_observable":
        return "not_observable", "upstream_r0_not_observable"
    if case["r0_status"] != "numeric":
        return "not_applicable", "upstream_r0_nonnumeric"
    if case["r0_kind"] != "dyad":
        return "not_applicable", "non_dyadic_r0_does_not_open_primary"
    if case["r0_projection"] != "complete":
        return "not_applicable", "reduced_r0_does_not_open_primary"
    if not case["r0_profile_match"]:
        return "processing_error", "required_r0_profile_mismatch"
    if not case["r0_threshold_match"]:
        return "processing_error", "r0_threshold_mismatch"
    if not case["r0_gate_consistent"]:
        return "processing_error", "r0_gate_value_inconsistent"
    if case["r0_gate_state"] != "open":
        return "not_applicable", "gate_closed"
    if case["monadic_inputs"] == "processing":
        return "processing_block", "upstream_monadic_input_invalid"
    if case["monadic_inputs"] == "not_observable":
        return "not_observable", "upstream_monadic_input_not_observable"
    if case["monadic_inputs"] != "numeric":
        return "not_applicable", "upstream_monadic_input_nonnumeric"
    if case["predecessor_contract"] == "synthetic_shared":
        return "processing_error", "shared_predecessor_synthesized"
    if case["predecessor_contract"] != "valid_separate":
        return "not_applicable", "source_local_predecessor_absent"
    if not case["ik_profile_match"]:
        return "processing_error", "monadic_ik_profile_mismatch"
    return "eligible_for_component_policy", "exact_handoff_valid"


CASE_OVERRIDES: tuple[tuple[str, str, dict[str, object]], ...] = (
    ("D-HAND-01", "profile_absent_precedes_other_checks", {"profile_selected": False, "pairing_valid": False}),
    ("D-HAND-02", "invalid_ik_rel_profile", {"profile_valid": False}),
    ("D-HAND-03", "invalid_pairing_identity", {"pairing_valid": False}),
    ("D-HAND-04", "upstream_r0_processing_record", {"r0_record": "processing"}),
    ("D-HAND-05", "qualifying_r0_absent", {"r0_record": "absent"}),
    ("D-HAND-06", "ordered_dyad_mismatch", {"r0_identity_match": False}),
    ("D-HAND-07", "pairing_map_mismatch", {"r0_identity_match": False}),
    ("D-HAND-08", "relational_eval_mismatch", {"r0_identity_match": False}),
    ("D-HAND-09", "paired_member_event_mismatch", {"r0_identity_match": False}),
    ("D-HAND-10", "r0_not_observable", {"r0_status": "not_observable"}),
    ("D-HAND-11", "r0_not_selected", {"r0_status": "not_selected"}),
    ("D-HAND-12", "r0_not_applicable", {"r0_status": "not_applicable"}),
    ("D-HAND-13", "n_adic_r0_for_primary", {"r0_kind": "constellation"}),
    ("D-HAND-14", "reduced_r0_for_primary", {"r0_projection": "reduced"}),
    ("D-HAND-15", "required_r0_profile_mismatch", {"r0_profile_match": False}),
    ("D-HAND-16", "r0_threshold_mismatch", {"r0_threshold_match": False}),
    ("D-HAND-17", "declared_gate_inconsistent_with_value", {"r0_gate_consistent": False}),
    ("D-HAND-18", "valid_numeric_closed_r0", {"r0_gate_state": "closed"}),
    ("D-HAND-19", "monadic_processing_failure_after_open_gate", {"monadic_inputs": "processing"}),
    ("D-HAND-20", "monadic_not_observable_after_open_gate", {"monadic_inputs": "not_observable"}),
    ("D-HAND-21", "monadic_not_applicable_after_open_gate", {"monadic_inputs": "not_applicable"}),
    ("D-HAND-22", "missing_valid_source_local_predecessor", {"predecessor_contract": "missing"}),
    ("D-HAND-23", "synthetic_shared_predecessor", {"predecessor_contract": "synthetic_shared"}),
    ("D-HAND-24", "monadic_ik_profile_mismatch", {"ik_profile_match": False}),
    ("D-HAND-25", "exact_valid_handoff_with_separate_predecessors", {}),
)


def write_precedence() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for case_id, description, overrides in CASE_OVERRIDES:
        case = dict(DEFAULTS)
        case.update(overrides)
        result, reason = outcome(case)
        rows.append(
            {
                "case_id": case_id,
                "description": description,
                "expected_outcome": result,
                "expected_reason": reason,
                "excluded_opportunity_retained": "true",
                "r0_record_ref_retained": str(case["r0_record"] != "absent").lower(),
                "ordered_dyad_and_pairing_retained": "true",
                "source_local_predecessors_retained": "true",
            }
        )

    by_id = {row["case_id"]: row for row in rows}
    assert by_id["D-HAND-01"]["expected_outcome"] == "not_selected"
    assert by_id["D-HAND-04"]["expected_outcome"] == "processing_block"
    assert by_id["D-HAND-10"]["expected_outcome"] == "not_observable"
    assert by_id["D-HAND-18"]["expected_outcome"] == "not_applicable"
    assert by_id["D-HAND-23"]["expected_outcome"] == "processing_error"
    assert by_id["D-HAND-25"]["expected_outcome"] == "eligible_for_component_policy"
    with PRECEDENCE_OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows


def main() -> None:
    feasibility = write_projected_feasibility()
    precedence = write_precedence()
    print(f"verified_projected_feasibility_rows={len(feasibility)}")
    print(f"existentially_open_rows={sum(row['some_complete_z_realization_can_open'] == 'true' for row in feasibility)}")
    print(f"existentially_closed_rows={sum(row['some_complete_z_realization_can_open'] == 'false' for row in feasibility)}")
    print(f"verified_handoff_precedence_rows={len(precedence)}")
    print(f"synthetic_r0_threshold={fraction_text(THRESHOLD)}")
    print(f"feasibility_output={FEASIBILITY_OUTPUT.name}")
    print(f"precedence_output={PRECEDENCE_OUTPUT.name}")


if __name__ == "__main__":
    main()
