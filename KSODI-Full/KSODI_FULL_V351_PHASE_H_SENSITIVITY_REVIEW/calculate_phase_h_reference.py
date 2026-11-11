#!/usr/bin/env python3
"""Generate the joint R0/IK_rel v3.51 Phase-H sensitivity fixtures.

Standard library only. This is runtime-independent reference evidence over the
frozen v3.51 contracts. It checks declared fixture expectations; it is not an
independent method-to-fixture reconciliation. Alternative metrics, coordinate
weights, IK weights and positive epsilons are named test controls; the
generator does not create a new method profile or empirical calibration claim.
"""

from __future__ import annotations

import csv
from decimal import Decimal, getcontext
from pathlib import Path


getcontext().prec = 50
HERE = Path(__file__).resolve().parent
D = Decimal
ZERO = D("0")
ONE = D("1")
TWO = D("2")
FIVE = D("5")
COORDINATES = ("K", "S", "O", "D", "I")
EQUAL_WEIGHTS = (D("0.2"),) * 5
K_FOCUS_WEIGHTS = (D("0.6"), D("0.1"), D("0.1"), D("0.1"), D("0.1"))
S_FOCUS_WEIGHTS = (D("0.1"), D("0.6"), D("0.1"), D("0.1"), D("0.1"))

METHOD_STATUS_DOMAIN = {"numeric", "not_selected", "not_observable", "not_applicable"}
PROCESSING_STATUS_DOMAIN = {"processing_error"}
FIXTURE_STATUS_TO_METHOD_STATUS = {
    "numeric": "numeric",
    "not_observable": "not_observable",
    "not_applicable": "not_applicable",
    "not_applicable_joint_projected_zero": "not_applicable",
    "not_applicable_joint_move_epsilon_band": "not_applicable",
    "processing_error": "processing_error",
}

OUTPUTS = {
    "H-A": HERE / "phase_h_r0_profile_sensitivity.csv",
    "H-B": HERE / "phase_h_coordinate_extrema.csv",
    "H-C": HERE / "phase_h_ikrel_projection_collisions.csv",
    "H-D": HERE / "phase_h_epsilon_profiles.csv",
    "H-E": HERE / "phase_h_joint_pipeline.csv",
}


def decimal_text(value: Decimal) -> str:
    text = format(value, ".15f").rstrip("0").rstrip(".")
    return text if text else "0"


def vector(values: tuple[str, ...]) -> tuple[Decimal, ...]:
    result = tuple(D(value) for value in values)
    assert len(result) == 5
    assert all(-ONE <= value <= ONE for value in result)
    return result


def vector_text(values: tuple[Decimal, ...]) -> str:
    return "[" + ",".join(decimal_text(value) for value in values) + "]"


def ids_text(values: tuple[str, ...]) -> str:
    return "|".join(values)


def weighted_l1(values: tuple[Decimal, ...], weights: tuple[Decimal, ...]) -> Decimal:
    assert len(values) == len(weights) == 5
    assert all(weight >= ZERO for weight in weights)
    assert sum(weights, ZERO) == ONE
    return sum((weight * abs(value) for weight, value in zip(weights, values)), ZERO)


def normalized_l2(values: tuple[Decimal, ...]) -> Decimal:
    return (sum((value * value for value in values), ZERO) / FIVE).sqrt()


def drift(
    values: tuple[Decimal, ...],
    metric_profile_id: str,
) -> Decimal:
    if metric_profile_id == "equal_coordinate_normalized_l1_v351":
        return weighted_l1(values, EQUAL_WEIGHTS)
    if metric_profile_id == "equal_coordinate_normalized_l2_test_control":
        return normalized_l2(values)
    if metric_profile_id == "g_k_focus_normalized_l1_test_control":
        return weighted_l1(values, K_FOCUS_WEIGHTS)
    if metric_profile_id == "g_s_focus_normalized_l1_test_control":
        return weighted_l1(values, S_FOCUS_WEIGHTS)
    raise AssertionError(f"unknown metric profile: {metric_profile_id}")


def metric_kind(metric_profile_id: str) -> str:
    return "normalized_L2" if "l2" in metric_profile_id else "normalized_L1"


def metric_status(metric_profile_id: str) -> str:
    return (
        "canonical_v351_reference"
        if metric_profile_id == "equal_coordinate_normalized_l1_v351"
        else "named_test_control_not_method_default"
    )


def r0_record(
    delta_a: tuple[Decimal, ...],
    delta_b: tuple[Decimal, ...],
    metric_profile_id: str,
    theta: Decimal,
) -> dict[str, str]:
    d_a = drift(delta_a, metric_profile_id)
    d_b = drift(delta_b, metric_profile_id)
    raw = ONE - (d_a + d_b) / TWO
    value = min(ONE, max(ZERO, raw))
    return {
        "metric_profile_id": metric_profile_id,
        "metric_profile_status": metric_status(metric_profile_id),
        "norm_family": metric_kind(metric_profile_id),
        "d_a": decimal_text(d_a),
        "d_b": decimal_text(d_b),
        "r0_raw": decimal_text(raw),
        "r0_value": decimal_text(value),
        "theta_r0_gate_open_min": decimal_text(theta),
        "gate_state": "open" if value >= theta else "closed",
    }


def ik_weights(profile_id: str) -> tuple[Decimal, ...]:
    if profile_id == "ik_w_equal_coordinate_reference":
        return EQUAL_WEIGHTS
    if profile_id == "ik_w_k_focus_test_control":
        return K_FOCUS_WEIGHTS
    raise AssertionError(f"unknown IK weight profile: {profile_id}")


def delta_ik(values: tuple[Decimal, ...], profile_id: str) -> Decimal:
    return sum(
        (weight * value for weight, value in zip(ik_weights(profile_id), values)),
        ZERO,
    )


def c_move(value_a: Decimal, value_b: Decimal) -> Decimal:
    return min(ONE, max(ZERO, ONE - abs(value_a - value_b) / TWO))


def normalized_vector_distance(
    values_a: tuple[Decimal, ...], values_b: tuple[Decimal, ...]
) -> Decimal:
    return (
        sum(((a - b) * (a - b) for a, b in zip(values_a, values_b)), ZERO)
        / FIVE
    ).sqrt()


def coordinate_extrema(
    values: tuple[Decimal, ...],
) -> tuple[Decimal, tuple[str, ...]]:
    magnitude = max((abs(value) for value in values), default=ZERO)
    if magnitude == ZERO:
        return ZERO, ()
    return magnitude, tuple(
        coordinate
        for coordinate, value in zip(COORDINATES, values)
        if abs(value) == magnitude
    )


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    assert rows
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def phase_h_a() -> list[dict[str, str]]:
    cases = (
        ("H-A-01", "both_static", ("0",) * 5, ("0",) * 5, "equal_coordinate_normalized_l1_v351", "0.8", "contract_confirmed"),
        ("H-A-02", "uniform_just_below_drift_limit", ("0.19",) * 5, ("0.19",) * 5, "equal_coordinate_normalized_l1_v351", "0.8", "contract_confirmed"),
        ("H-A-03", "uniform_exactly_at_drift_limit", ("0.2",) * 5, ("0.2",) * 5, "equal_coordinate_normalized_l1_v351", "0.8", "contract_confirmed"),
        ("H-A-04", "uniform_just_above_drift_limit", ("0.21",) * 5, ("0.21",) * 5, "equal_coordinate_normalized_l1_v351", "0.8", "contract_confirmed"),
        ("H-A-05", "single_axis_under_canonical_l1", ("1", "0", "0", "0", "0"), ("1", "0", "0", "0", "0"), "equal_coordinate_normalized_l1_v351", "0.8", "profile_sensitive_expected"),
        ("H-A-06", "single_axis_under_l2_control", ("1", "0", "0", "0", "0"), ("1", "0", "0", "0", "0"), "equal_coordinate_normalized_l2_test_control", "0.8", "profile_sensitive_expected"),
        ("H-A-07", "equal_l1_different_concentration_l1", ("1", "0", "0", "0", "0"), ("0.2",) * 5, "equal_coordinate_normalized_l1_v351", "0.8", "profile_sensitive_expected"),
        ("H-A-08", "equal_l1_different_concentration_l2", ("1", "0", "0", "0", "0"), ("0.2",) * 5, "equal_coordinate_normalized_l2_test_control", "0.8", "profile_sensitive_expected"),
        ("H-A-09", "equal_l2_different_l1_geometry_l1", ("0.6", "0.8", "0", "0", "0"), ("1", "0", "0", "0", "0"), "equal_coordinate_normalized_l1_v351", "0.8", "profile_sensitive_expected"),
        ("H-A-10", "equal_l2_different_l1_geometry_l2", ("0.6", "0.8", "0", "0", "0"), ("1", "0", "0", "0", "0"), "equal_coordinate_normalized_l2_test_control", "0.8", "profile_sensitive_expected"),
        ("H-A-11", "k_axis_under_k_focus_control", ("0.5", "0", "0", "0", "0"), ("0.5", "0", "0", "0", "0"), "g_k_focus_normalized_l1_test_control", "0.8", "profile_sensitive_expected"),
        ("H-A-12", "s_axis_under_k_focus_control", ("0", "0.5", "0", "0", "0"), ("0", "0.5", "0", "0", "0"), "g_k_focus_normalized_l1_test_control", "0.8", "profile_sensitive_expected"),
    )
    rows: list[dict[str, str]] = []
    for case_id, description, a_raw, b_raw, profile_id, theta_raw, finding in cases:
        delta_a = vector(a_raw)
        delta_b = vector(b_raw)
        row = {
            "case_id": case_id,
            "description": description,
            "delta_z_a": vector_text(delta_a),
            "delta_z_b": vector_text(delta_b),
            **r0_record(delta_a, delta_b, profile_id, D(theta_raw)),
            "finding_class": finding,
        }
        rows.append(row)

    by_id = {row["case_id"]: row for row in rows}
    assert by_id["H-A-03"]["r0_value"] == "0.8"
    assert by_id["H-A-03"]["gate_state"] == "open"
    assert by_id["H-A-04"]["gate_state"] == "closed"
    assert by_id["H-A-05"]["gate_state"] == "open"
    assert by_id["H-A-06"]["gate_state"] == "closed"
    assert by_id["H-A-07"]["r0_value"] == "0.8"
    assert by_id["H-A-11"]["r0_value"] != by_id["H-A-12"]["r0_value"]
    write_rows(OUTPUTS["H-A"], rows)
    return rows


def phase_h_b() -> list[dict[str, str]]:
    cases = (
        ("H-B-01", "zero_vector_has_no_extreme_identity", ("0",) * 5, "contract_confirmed"),
        ("H-B-02", "single_positive_k", ("0.7", "0", "0", "0", "0"), "contract_confirmed"),
        ("H-B-03", "single_negative_s", ("0", "-0.7", "0", "0", "0"), "contract_confirmed"),
        ("H-B-04", "two_way_equal_positive_tie", ("0.7", "0.7", "0", "0", "0"), "diagnostic_information_loss"),
        ("H-B-05", "mixed_sign_equal_tie", ("0.7", "-0.7", "0", "0", "0"), "diagnostic_information_loss"),
        ("H-B-06", "all_coordinate_tie", ("0.3", "-0.3", "0.3", "-0.3", "0.3"), "diagnostic_information_loss"),
        ("H-B-07", "one_unique_maximum_with_secondary_motion", ("0.8", "0.7", "-0.2", "0", "0"), "diagnostic_information_loss"),
    )
    rows: list[dict[str, str]] = []
    for case_id, description, raw, finding in cases:
        values = vector(raw)
        magnitude, coordinate_ids = coordinate_extrema(values)
        rows.append(
            {
                "case_id": case_id,
                "description": description,
                "delta_z_e": vector_text(values),
                "max_abs_coordinate_delta_e": decimal_text(magnitude),
                "max_abs_coordinate_ids_e": ids_text(coordinate_ids),
                "tied_maximum_count": str(len(coordinate_ids)),
                "canonical_equal_l1_drift": decimal_text(drift(values, "equal_coordinate_normalized_l1_v351")),
                "l2_test_control_drift": decimal_text(drift(values, "equal_coordinate_normalized_l2_test_control")),
                "k_focus_test_control_drift": decimal_text(drift(values, "g_k_focus_normalized_l1_test_control")),
                "complete_signed_delta_z_authoritative": "true",
                "diagnostic_changes_r0_or_gate": "false",
                "finding_class": finding,
            }
        )

    by_id = {row["case_id"]: row for row in rows}
    assert by_id["H-B-01"]["max_abs_coordinate_ids_e"] == ""
    assert by_id["H-B-04"]["max_abs_coordinate_ids_e"] == "K|S"
    assert by_id["H-B-05"]["max_abs_coordinate_ids_e"] == "K|S"
    assert by_id["H-B-06"]["tied_maximum_count"] == "5"
    write_rows(OUTPUTS["H-B"], rows)
    return rows


def phase_h_c() -> list[dict[str, str]]:
    cases = (
        ("H-C-01", "equal_projection_different_coordinates", ("0.5", "0", "0", "0", "0"), ("0", "0.5", "0", "0", "0")),
        ("H-C-02", "projected_zero_full_transfer_vs_rest", ("0.5", "-0.5", "0", "0", "0"), ("0", "0", "0", "0", "0")),
        ("H-C-03", "equal_projection_concentrated_vs_distributed", ("1", "0", "0", "0", "0"), ("0.2", "0.2", "0.2", "0.2", "0.2")),
        ("H-C-04", "equal_projected_zero_disjoint_transfers", ("0.5", "-0.5", "0", "0", "0"), ("0", "0", "0.5", "-0.5", "0")),
        ("H-C-05", "identical_full_movement", ("0.4", "0.1", "0", "0", "0"), ("0.4", "0.1", "0", "0", "0")),
        ("H-C-06", "opposite_projection_same_canonical_drift", ("0.5", "0", "0", "0", "0"), ("-0.5", "0", "0", "0", "0")),
        ("H-C-07", "equal_projection_mixed_sign_vs_small_uniform", ("0.6", "-0.2", "0", "0", "0"), ("0.08", "0.08", "0.08", "0.08", "0.08")),
    )
    rows: list[dict[str, str]] = []
    for case_id, description, a_raw, b_raw in cases:
        delta_a = vector(a_raw)
        delta_b = vector(b_raw)
        delta_ik_a = delta_ik(delta_a, "ik_w_equal_coordinate_reference")
        delta_ik_b = delta_ik(delta_b, "ik_w_equal_coordinate_reference")
        component = c_move(delta_ik_a, delta_ik_b)
        method_status = (
            "not_applicable_joint_projected_zero"
            if delta_ik_a == ZERO and delta_ik_b == ZERO
            else "numeric"
        )
        r0 = r0_record(
            delta_a,
            delta_b,
            "equal_coordinate_normalized_l1_v351",
            D("0.8"),
        )
        raw_collision = component == ONE and delta_a != delta_b
        numeric_collision = method_status == "numeric" and raw_collision
        rows.append(
            {
                "case_id": case_id,
                "description": description,
                "delta_z_a": vector_text(delta_a),
                "delta_z_b": vector_text(delta_b),
                "delta_ik_w_a": decimal_text(delta_ik_a),
                "delta_ik_w_b": decimal_text(delta_ik_b),
                "c_move_raw": decimal_text(component),
                "method_status_epsilon_0": method_status,
                "method_value": decimal_text(component) if method_status == "numeric" else "",
                "delta_z_vectors_equal": str(delta_a == delta_b).lower(),
                "normalized_delta_z_distance": decimal_text(normalized_vector_distance(delta_a, delta_b)),
                "canonical_r0_value": r0["r0_value"],
                "canonical_r0_gate_state": r0["gate_state"],
                "raw_projection_collision": str(raw_collision).lower(),
                "numeric_projection_collision": str(numeric_collision).lower(),
                "full_delta_z_required_for_distinction": str(delta_a != delta_b).lower(),
                "finding_class": "diagnostic_information_loss" if raw_collision else "contract_confirmed",
            }
        )

    by_id = {row["case_id"]: row for row in rows}
    assert by_id["H-C-01"]["numeric_projection_collision"] == "true"
    assert by_id["H-C-02"]["raw_projection_collision"] == "true"
    assert by_id["H-C-02"]["numeric_projection_collision"] == "false"
    assert by_id["H-C-02"]["method_status_epsilon_0"] == "not_applicable_joint_projected_zero"
    assert by_id["H-C-03"]["numeric_projection_collision"] == "true"
    assert by_id["H-C-05"]["delta_z_vectors_equal"] == "true"
    assert by_id["H-C-06"]["c_move_raw"] == "0.9"
    assert all(row["canonical_r0_gate_state"] == "open" for row in rows)
    for row in rows:
        assert_fixture_status_domain(row["method_status_epsilon_0"])
    write_rows(OUTPUTS["H-C"], rows)
    return rows


def epsilon_decision(
    value_a: Decimal,
    value_b: Decimal,
    epsilon: Decimal,
    epsilon_kind: str,
    parameter_origin: str,
    calibration_status: str,
    calibration_evidence_reference: str,
) -> tuple[str, str]:
    if not parameter_origin:
        return "processing_error", "missing_epsilon_parameter_origin"
    if not calibration_status:
        return "processing_error", "missing_epsilon_calibration_status"
    if calibration_status == "empirically_calibrated" and not calibration_evidence_reference:
        return "processing_error", "calibration_claim_without_evidence_reference"
    if epsilon < ZERO:
        return "processing_error", "negative_epsilon"
    if epsilon_kind == "epsilon_method_exact_zero":
        if epsilon != ZERO:
            return "processing_error", "exact_zero_kind_requires_zero_epsilon"
        if value_a == ZERO and value_b == ZERO:
            return "not_applicable_joint_projected_zero", "exact_joint_projected_zero"
        return "numeric", "outside_exact_joint_projected_zero"
    if epsilon_kind == "epsilon_numeric_tolerance":
        if abs(value_a) <= epsilon and abs(value_b) <= epsilon:
            return "not_applicable_joint_move_epsilon_band", "joint_projected_band"
        return "numeric", "outside_joint_projected_band"
    if epsilon_kind == "epsilon_observation_resolution":
        if abs(value_a) <= epsilon or abs(value_b) <= epsilon:
            return (
                "not_observable",
                "projected_movement_unresolved_at_observation_resolution",
            )
        return "numeric", "both_projected_movements_resolved"
    if epsilon_kind == "epsilon_question_relevance":
        if abs(value_a) <= epsilon and abs(value_b) <= epsilon:
            return "not_applicable_joint_move_epsilon_band", "joint_projected_band"
        return "numeric", "outside_joint_projected_band"
    return "processing_error", "unknown_or_ambiguous_epsilon_kind"


def assert_fixture_status_domain(status: str) -> None:
    assert status in FIXTURE_STATUS_TO_METHOD_STATUS, f"unknown fixture status: {status}"
    normalized = FIXTURE_STATUS_TO_METHOD_STATUS[status]
    assert normalized in METHOD_STATUS_DOMAIN | PROCESSING_STATUS_DOMAIN


def phase_h_d() -> list[dict[str, str]]:
    cases = (
        ("H-D-01", "epsilon_zero_exact_joint_zero", "0", "0", "0", "epsilon_method_exact_zero", "method_reference", "exact_reference_no_empirical_calibration_required", ""),
        ("H-D-02", "numeric_tolerance_joint_below", "0.09", "0.09", "0.1", "epsilon_numeric_tolerance", "synthetic_reference_fixture", "set_not_empirically_calibrated", ""),
        ("H-D-03", "numeric_tolerance_joint_at_boundary", "0.1", "-0.1", "0.1", "epsilon_numeric_tolerance", "synthetic_reference_fixture", "set_not_empirically_calibrated", ""),
        ("H-D-04", "numeric_tolerance_one_outside", "0", "0.11", "0.1", "epsilon_numeric_tolerance", "synthetic_reference_fixture", "set_not_empirically_calibrated", ""),
        ("H-D-05", "numeric_tolerance_both_outside", "-0.11", "0.11", "0.1", "epsilon_numeric_tolerance", "synthetic_reference_fixture", "set_not_empirically_calibrated", ""),
        ("H-D-06", "observation_resolution_joint_below", "0.09", "0.09", "0.1", "epsilon_observation_resolution", "synthetic_reference_fixture", "set_not_empirically_calibrated", ""),
        ("H-D-07", "observation_resolution_joint_at_boundary", "0.1", "-0.1", "0.1", "epsilon_observation_resolution", "synthetic_reference_fixture", "set_not_empirically_calibrated", ""),
        ("H-D-08", "observation_resolution_one_outside", "0", "0.11", "0.1", "epsilon_observation_resolution", "synthetic_reference_fixture", "set_not_empirically_calibrated", ""),
        ("H-D-09", "question_relevance_joint_below", "0.09", "0.09", "0.1", "epsilon_question_relevance", "synthetic_reference_fixture", "set_not_empirically_calibrated", ""),
        ("H-D-10", "question_relevance_joint_at_boundary", "0.1", "-0.1", "0.1", "epsilon_question_relevance", "synthetic_reference_fixture", "set_not_empirically_calibrated", ""),
        ("H-D-11", "question_relevance_one_outside", "0", "0.11", "0.1", "epsilon_question_relevance", "synthetic_reference_fixture", "set_not_empirically_calibrated", ""),
        ("H-D-12", "missing_parameter_origin", "0", "0.11", "0.1", "epsilon_numeric_tolerance", "", "set_not_empirically_calibrated", ""),
        ("H-D-13", "missing_calibration_status", "0", "0.11", "0.1", "epsilon_numeric_tolerance", "synthetic_reference_fixture", "", ""),
        ("H-D-14", "unsupported_calibration_claim_without_evidence", "0", "0.11", "0.1", "epsilon_numeric_tolerance", "external_dataset", "empirically_calibrated", ""),
        ("H-D-15", "structurally_complete_calibration_record_not_evidence_validation", "0", "0.11", "0.1", "epsilon_numeric_tolerance", "synthetic_schema_test", "empirically_calibrated", "synthetic-evidence-reference-for-schema-test"),
        ("H-D-16", "negative_epsilon_rejected", "0", "0.11", "-0.1", "epsilon_numeric_tolerance", "synthetic_reference_fixture", "set_not_empirically_calibrated", ""),
    )
    rows: list[dict[str, str]] = []
    for case_id, description, a_raw, b_raw, epsilon_raw, epsilon_kind, origin, status, evidence in cases:
        value_a = D(a_raw)
        value_b = D(b_raw)
        epsilon = D(epsilon_raw)
        method_status, reason = epsilon_decision(
            value_a, value_b, epsilon, epsilon_kind, origin, status, evidence
        )
        raw_component = c_move(value_a, value_b)
        rows.append(
            {
                "case_id": case_id,
                "description": description,
                "delta_ik_w_a": decimal_text(value_a),
                "delta_ik_w_b": decimal_text(value_b),
                "epsilon_move": decimal_text(epsilon),
                "epsilon_kind": epsilon_kind,
                "epsilon_parameter_origin": origin,
                "epsilon_calibration_status": status,
                "calibration_evidence_reference": evidence,
                "c_move_raw": decimal_text(raw_component),
                "method_status": method_status,
                "reason": reason,
                "method_value": decimal_text(raw_component) if method_status == "numeric" else "",
                "finding_class": "contract_confirmed",
            }
        )

    by_id = {row["case_id"]: row for row in rows}
    assert by_id["H-D-02"]["method_status"].startswith("not_applicable")
    assert by_id["H-D-03"]["method_status"].startswith("not_applicable")
    assert by_id["H-D-04"]["method_status"] == "numeric"
    assert by_id["H-D-06"]["method_status"] == "not_observable"
    assert by_id["H-D-07"]["method_status"] == "not_observable"
    assert by_id["H-D-08"]["method_status"] == "not_observable"
    assert by_id["H-D-09"]["method_status"].startswith("not_applicable")
    assert by_id["H-D-11"]["method_status"] == "numeric"
    assert by_id["H-D-12"]["reason"] == "missing_epsilon_parameter_origin"
    assert by_id["H-D-14"]["reason"] == "calibration_claim_without_evidence_reference"
    assert by_id["H-D-15"]["method_status"] == "numeric"
    assert all(
        row["reason"] == "projected_movement_unresolved_at_observation_resolution"
        for row in rows
        if row["epsilon_kind"] == "epsilon_observation_resolution"
    )
    assert epsilon_decision(
        ZERO,
        ZERO,
        ZERO,
        "unknown_epsilon_kind",
        "synthetic_schema_test",
        "set_not_empirically_calibrated",
        "",
    ) == ("processing_error", "unknown_or_ambiguous_epsilon_kind")
    for row in rows:
        assert_fixture_status_domain(row["method_status"])
    write_rows(OUTPUTS["H-D"], rows)
    return rows


def joint_pipeline_case(
    case_id: str,
    description: str,
    a_raw: tuple[str, ...],
    b_raw: tuple[str, ...],
    metric_profile_id: str,
    ik_profile_id: str,
    epsilon_raw: str,
    epsilon_kind: str,
    origin: str,
    calibration_status: str,
    expected_finding: str,
) -> dict[str, str]:
    delta_a = vector(a_raw)
    delta_b = vector(b_raw)
    r0 = r0_record(delta_a, delta_b, metric_profile_id, D("0.8"))
    ik_a = delta_ik(delta_a, ik_profile_id)
    ik_b = delta_ik(delta_b, ik_profile_id)
    epsilon = D(epsilon_raw)
    if r0["gate_state"] != "open":
        downstream_status = "not_applicable"
        reason = "gate_not_open"
        method_value = ""
    else:
        downstream_status, reason = epsilon_decision(
            ik_a, ik_b, epsilon, epsilon_kind, origin, calibration_status, ""
        )
        method_value = (
            decimal_text(c_move(ik_a, ik_b))
            if downstream_status == "numeric"
            else ""
        )
    projection_collision = (
        downstream_status == "numeric"
        and method_value == "1"
        and delta_a != delta_b
    )
    return {
        "case_id": case_id,
        "description": description,
        "delta_z_a": vector_text(delta_a),
        "delta_z_b": vector_text(delta_b),
        "r0_metric_profile_id": metric_profile_id,
        "r0_metric_profile_status": metric_status(metric_profile_id),
        "r0_value": r0["r0_value"],
        "theta_r0_gate_open_min": r0["theta_r0_gate_open_min"],
        "r0_gate_state": r0["gate_state"],
        "ik_weight_profile_id": ik_profile_id,
        "ik_weight_profile_status": "canonical_test_basis" if ik_profile_id == "ik_w_equal_coordinate_reference" else "named_test_control_not_method_default",
        "delta_ik_w_a": decimal_text(ik_a),
        "delta_ik_w_b": decimal_text(ik_b),
        "epsilon_move": decimal_text(epsilon),
        "epsilon_kind": epsilon_kind,
        "epsilon_parameter_origin": origin,
        "epsilon_calibration_status": calibration_status,
        "ik_rel_status": downstream_status,
        "ik_rel_reason": reason,
        "ik_rel_value": method_value,
        "projection_collision": str(projection_collision).lower(),
        "expected_finding_class": expected_finding,
        "observed_finding_class": (
            "diagnostic_information_loss"
            if projection_collision
            else "profile_sensitive_expected"
            if "test_control" in metric_status(metric_profile_id)
            or "test_control" in ("named_test_control_not_method_default" if ik_profile_id != "ik_w_equal_coordinate_reference" else "")
            else "contract_confirmed"
        ),
    }


def phase_h_e() -> list[dict[str, str]]:
    cases = (
        ("H-E-01", "static_open_r0_exact_zero_not_applicable", ("0",) * 5, ("0",) * 5, "equal_coordinate_normalized_l1_v351", "ik_w_equal_coordinate_reference", "0", "epsilon_method_exact_zero", "method_reference", "exact_reference_no_empirical_calibration_required", "contract_confirmed"),
        ("H-E-02", "same_k_movement_numeric_perfect", ("0.5", "0", "0", "0", "0"), ("0.5", "0", "0", "0", "0"), "equal_coordinate_normalized_l1_v351", "ik_w_equal_coordinate_reference", "0", "epsilon_method_exact_zero", "method_reference", "exact_reference_no_empirical_calibration_required", "contract_confirmed"),
        ("H-E-03", "different_axes_equal_projection", ("0.5", "0", "0", "0", "0"), ("0", "0.5", "0", "0", "0"), "equal_coordinate_normalized_l1_v351", "ik_w_equal_coordinate_reference", "0", "epsilon_method_exact_zero", "method_reference", "exact_reference_no_empirical_calibration_required", "diagnostic_information_loss"),
        ("H-E-04", "opposite_projection_numeric", ("0.5", "0", "0", "0", "0"), ("-0.5", "0", "0", "0", "0"), "equal_coordinate_normalized_l1_v351", "ik_w_equal_coordinate_reference", "0", "epsilon_method_exact_zero", "method_reference", "exact_reference_no_empirical_calibration_required", "contract_confirmed"),
        ("H-E-05", "single_axis_l1_gate_boundary", ("1", "0", "0", "0", "0"), ("1", "0", "0", "0", "0"), "equal_coordinate_normalized_l1_v351", "ik_w_equal_coordinate_reference", "0", "epsilon_method_exact_zero", "method_reference", "exact_reference_no_empirical_calibration_required", "contract_confirmed"),
        ("H-E-06", "single_axis_l2_gate_closed", ("1", "0", "0", "0", "0"), ("1", "0", "0", "0", "0"), "equal_coordinate_normalized_l2_test_control", "ik_w_equal_coordinate_reference", "0", "epsilon_method_exact_zero", "method_reference", "exact_reference_no_empirical_calibration_required", "profile_sensitive_expected"),
        ("H-E-07", "different_axes_equal_ik_weights_baseline_for_h_e_08", ("0.5", "0", "0", "0", "0"), ("0", "0.5", "0", "0", "0"), "equal_coordinate_normalized_l1_v351", "ik_w_equal_coordinate_reference", "0", "epsilon_method_exact_zero", "method_reference", "exact_reference_no_empirical_calibration_required", "diagnostic_information_loss"),
        ("H-E-08", "different_axes_k_focus_ik_control", ("0.5", "0", "0", "0", "0"), ("0", "0.5", "0", "0", "0"), "equal_coordinate_normalized_l1_v351", "ik_w_k_focus_test_control", "0", "epsilon_method_exact_zero", "method_reference", "exact_reference_no_empirical_calibration_required", "profile_sensitive_expected"),
        ("H-E-09", "small_equal_projection_positive_epsilon_band", ("0.2", "0", "0", "0", "0"), ("0.2", "0", "0", "0", "0"), "equal_coordinate_normalized_l1_v351", "ik_w_equal_coordinate_reference", "0.05", "epsilon_numeric_tolerance", "synthetic_reference_fixture", "set_not_empirically_calibrated", "contract_confirmed"),
        ("H-E-10", "small_equal_projection_exact_epsilon", ("0.2", "0", "0", "0", "0"), ("0.2", "0", "0", "0", "0"), "equal_coordinate_normalized_l1_v351", "ik_w_equal_coordinate_reference", "0", "epsilon_method_exact_zero", "method_reference", "exact_reference_no_empirical_calibration_required", "contract_confirmed"),
    )
    rows = [joint_pipeline_case(*case) for case in cases]
    by_id = {row["case_id"]: row for row in rows}
    assert by_id["H-E-01"]["ik_rel_status"].startswith("not_applicable")
    assert by_id["H-E-02"]["ik_rel_value"] == "1"
    assert by_id["H-E-03"]["projection_collision"] == "true"
    assert by_id["H-E-05"]["r0_gate_state"] == "open"
    assert by_id["H-E-06"]["r0_gate_state"] == "closed"
    assert by_id["H-E-06"]["ik_rel_status"] == "not_applicable"
    assert by_id["H-E-06"]["ik_rel_reason"] == "gate_not_open"
    assert by_id["H-E-07"]["ik_rel_value"] == "1"
    assert by_id["H-E-08"]["ik_rel_value"] == "0.875"
    assert by_id["H-E-09"]["ik_rel_status"].startswith("not_applicable")
    assert by_id["H-E-10"]["ik_rel_status"] == "numeric"
    assert all(
        row["expected_finding_class"] == row["observed_finding_class"]
        for row in rows
    )
    for row in rows:
        assert_fixture_status_domain(row["ik_rel_status"])
    write_rows(OUTPUTS["H-E"], rows)
    return rows


def main() -> None:
    blocks = {
        "H-A": phase_h_a(),
        "H-B": phase_h_b(),
        "H-C": phase_h_c(),
        "H-D": phase_h_d(),
        "H-E": phase_h_e(),
    }
    all_rows = [row for rows in blocks.values() for row in rows]
    for block_id, rows in blocks.items():
        print(f"verified_{block_id.lower().replace('-', '_')}_rows={len(rows)}")
    print(f"verified_total_rows={len(all_rows)}")
    print("generator_assertions_passed=true")
    print("independent_contract_reconciliation_performed=false")
    for block_id, path in OUTPUTS.items():
        print(f"{block_id.lower().replace('-', '_')}_output={path.name}")


if __name__ == "__main__":
    main()
