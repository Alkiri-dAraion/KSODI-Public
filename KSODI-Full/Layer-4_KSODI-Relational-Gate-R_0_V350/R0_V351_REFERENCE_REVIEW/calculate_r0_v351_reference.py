#!/usr/bin/env python3
"""Generate the bounded R0 v3.51 reference fixtures.

Standard library only. The script implements the formulas printed in the
v3.51 method; it is reference evidence, not an independent method
authority or runtime-conformance test.
"""

from __future__ import annotations

import csv
import hashlib
from decimal import Decimal, getcontext
from pathlib import Path


getcontext().prec = 50
HERE = Path(__file__).resolve().parent
NUMERIC_OUT = HERE / "r0_v351_numeric_reference.csv"
STATUS_OUT = HERE / "r0_v351_status_precedence.csv"

D = Decimal
ZERO = D("0")
ONE = D("1")
FIVE = D("5")


def decimal_text(value: Decimal) -> str:
    text = format(value, ".15f").rstrip("0").rstrip(".")
    return text if text else "0"


def vector_text(values: tuple[Decimal, ...]) -> str:
    return "[" + ",".join(decimal_text(value) for value in values) + "]"


def normalized_drift(
    values: tuple[Decimal, ...], indices: tuple[int, ...], norm: str
) -> Decimal:
    selected = tuple(values[index] for index in indices)
    assert selected
    if norm == "normalized_L1":
        return sum((abs(value) for value in selected), ZERO) / D(len(selected))
    if norm == "normalized_L2":
        return sum((value * value for value in selected), ZERO).sqrt() / D(
            len(selected)
        ).sqrt()
    raise AssertionError(f"unknown norm: {norm}")


def numeric_case(
    case_id: str,
    description: str,
    delta_a: tuple[str, ...],
    delta_b: tuple[str, ...],
    norm: str,
    theta: str,
    indices: tuple[int, ...] = (0, 1, 2, 3, 4),
) -> dict[str, str]:
    a = tuple(D(value) for value in delta_a)
    b = tuple(D(value) for value in delta_b)
    assert len(a) == len(b) == 5
    assert all(-ONE <= value <= ONE for value in a + b)

    d_a = normalized_drift(a, indices, norm)
    d_b = normalized_drift(b, indices, norm)
    raw = ONE - (d_a + d_b) / D(2)
    value = min(ONE, max(ZERO, raw))
    threshold = D(theta)
    gate = "open" if value >= threshold else "closed"

    return {
        "case_id": case_id,
        "description": description,
        "delta_z_a": vector_text(a),
        "delta_z_b": vector_text(b),
        "projection_kind": "complete" if len(indices) == 5 else "reduced",
        "active_coordinate_set_m": "K,S,O,D,I"
        if len(indices) == 5
        else ",".join("KSODI"[index] for index in indices),
        "coordinate_metric_profile_id": "equal_coordinate_reference",
        "norm_profile_id": norm,
        "trajectory_aggregation_profile_id": "arithmetic_mean",
        "theta_r0_gate_open_min": decimal_text(threshold),
        "aggregate_drift_max": decimal_text(ONE - threshold),
        "threshold_calibration_status": "set_not_empirically_calibrated",
        "d_a": decimal_text(d_a),
        "d_b": decimal_text(d_b),
        "r0_raw": decimal_text(raw),
        "r0_value": decimal_text(value),
        "r0_status": "numeric",
        "gate_state": gate,
        "asymmetry": decimal_text(abs(d_a - d_b)),
    }


def numeric_rows() -> list[dict[str, str]]:
    z = ("0", "0", "0", "0", "0")
    rows = [
        numeric_case("R0-01", "both static", z, z, "normalized_L1", "0.8"),
        numeric_case(
            "R0-02",
            "low uniform movement",
            ("0.1",) * 5,
            ("0.2",) * 5,
            "normalized_L1",
            "0.8",
        ),
        numeric_case(
            "R0-03",
            "concentrated movement under L1 reference",
            ("1", "0", "0", "0", "0"),
            z,
            "normalized_L1",
            "0.8",
        ),
        numeric_case(
            "R0-04",
            "same concentrated movement under separate L2 profile",
            ("1", "0", "0", "0", "0"),
            z,
            "normalized_L2",
            "0.8",
        ),
        numeric_case(
            "R0-05",
            "high equal uniform movement",
            ("0.75",) * 5,
            ("0.75",) * 5,
            "normalized_L1",
            "0.5",
        ),
        numeric_case(
            "R0-06",
            "one-sided movement exposes asymmetry",
            z,
            ("0.8",) * 5,
            "normalized_L1",
            "0.5",
        ),
        numeric_case(
            "R0-07",
            "fixed reduced K-only question",
            ("1", "0", "0", "0", "0"),
            z,
            "normalized_L1",
            "0.5",
            (0,),
        ),
        numeric_case(
            "R0-08",
            "same movement under complete reference question",
            ("1", "0", "0", "0", "0"),
            z,
            "normalized_L1",
            "0.5",
        ),
        numeric_case(
            "R0-09",
            "inclusive equality at threshold",
            ("0.5",) * 5,
            ("0.5",) * 5,
            "normalized_L1",
            "0.5",
        ),
    ]

    by_id = {row["case_id"]: row for row in rows}
    assert by_id["R0-01"]["r0_value"] == "1"
    assert by_id["R0-02"]["r0_value"] == "0.85"
    assert by_id["R0-03"]["r0_value"] == "0.9"
    assert by_id["R0-03"]["gate_state"] == "open"
    assert by_id["R0-04"]["gate_state"] == "closed"
    assert by_id["R0-05"]["r0_value"] == "0.25"
    assert by_id["R0-06"]["asymmetry"] == "0.8"
    assert by_id["R0-07"]["r0_value"] == "0.5"
    assert by_id["R0-08"]["r0_value"] == "0.9"
    assert by_id["R0-09"]["gate_state"] == "open"
    return rows


def resolve_status_case(
    case_id: str,
    condition: str,
    *,
    profile_selected: bool = True,
    required_statuses: tuple[str, ...] = ("numeric",),
    incomparable_present: bool = False,
    processing_error_present: bool = False,
    numeric_value: str = "",
    threshold: str = "",
) -> dict[str, str]:
    """Resolve one synthetic status case using the printed v3.51 precedence."""

    allowed = {"numeric", "not_selected", "not_observable", "not_applicable"}
    assert required_statuses
    assert set(required_statuses) <= allowed

    if not profile_selected:
        result_status = "not_selected"
        gate_state = "not_evaluable"
        processing_state = "none"
    elif processing_error_present:
        result_status = "no_valid_result"
        gate_state = "absent"
        processing_state = "processing_error"
    elif incomparable_present:
        result_status = "no_valid_result"
        gate_state = "absent"
        processing_state = "incomparable"
    elif "not_observable" in required_statuses:
        result_status = "not_observable"
        gate_state = "not_evaluable"
        processing_state = "none"
    elif any(status != "numeric" for status in required_statuses):
        assert set(required_statuses) <= {"numeric", "not_selected", "not_applicable"}
        result_status = "not_applicable"
        gate_state = "not_evaluable"
        processing_state = "none"
    else:
        value = D(numeric_value)
        gate_threshold = D(threshold)
        assert ZERO <= value <= ONE
        assert ZERO <= gate_threshold <= ONE
        result_status = "numeric"
        gate_state = "open" if value >= gate_threshold else "closed"
        processing_state = "none"

    return {
        "case_id": case_id,
        "condition": condition,
        "profile_selected": str(profile_selected).lower(),
        "required_statuses": "|".join(required_statuses),
        "incomparable_present": str(incomparable_present).lower(),
        "processing_error_present": str(processing_error_present).lower(),
        "numeric_value": numeric_value,
        "threshold": threshold,
        "result_status": result_status,
        "gate_state": gate_state,
        "processing_state": processing_state,
        "numeric_value_present": str(result_status == "numeric").lower(),
    }


def status_rows() -> list[dict[str, str]]:
    rows = [
        resolve_status_case("S-01", "no R0 profile selected", profile_selected=False),
        resolve_status_case(
            "S-02",
            "required movement not observable",
            required_statuses=("not_observable",),
        ),
        resolve_status_case(
            "S-03",
            "declared pairing or fixed-M contract not applicable",
            required_statuses=("not_applicable",),
        ),
        resolve_status_case(
            "S-04",
            "identity or profile incomparable",
            incomparable_present=True,
        ),
        resolve_status_case(
            "S-05",
            "malformed threshold or arithmetic",
            processing_error_present=True,
        ),
        resolve_status_case(
            "S-06",
            "valid numeric result below threshold",
            numeric_value="0.4",
            threshold="0.5",
        ),
        resolve_status_case(
            "S-07",
            "valid numeric result at threshold",
            numeric_value="0.5",
            threshold="0.5",
        ),
        resolve_status_case(
            "S-08",
            "not observable takes precedence over inapplicable",
            required_statuses=("not_observable", "not_applicable"),
        ),
        resolve_status_case(
            "S-09",
            "selected profile with not-selected and inapplicable inputs",
            required_statuses=("not_selected", "not_applicable"),
        ),
        resolve_status_case(
            "S-10",
            "incomparability blocks otherwise unobservable inputs",
            required_statuses=("not_observable",),
            incomparable_present=True,
        ),
        resolve_status_case(
            "S-11",
            "absent R0 profile short-circuits input-status resolution",
            profile_selected=False,
            required_statuses=("not_observable",),
        ),
    ]

    by_id = {row["case_id"]: row for row in rows}
    assert by_id["S-08"]["result_status"] == "not_observable"
    assert by_id["S-09"]["result_status"] == "not_applicable"
    assert by_id["S-10"]["processing_state"] == "incomparable"
    assert by_id["S-11"]["result_status"] == "not_selected"
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(rows[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    numeric = numeric_rows()
    statuses = status_rows()
    write_csv(NUMERIC_OUT, numeric)
    write_csv(STATUS_OUT, statuses)
    print(f"verified_numeric_cases={len(numeric)}")
    print(f"verified_status_cases={len(statuses)}")
    print(f"numeric_sha256={sha256(NUMERIC_OUT)}")
    print(f"status_sha256={sha256(STATUS_OUT)}")


if __name__ == "__main__":
    main()
