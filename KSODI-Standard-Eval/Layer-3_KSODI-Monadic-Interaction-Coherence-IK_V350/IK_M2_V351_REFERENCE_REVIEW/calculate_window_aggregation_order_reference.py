#!/usr/bin/env python3
"""Generate and verify the v3.51 IK window aggregation-order fixtures."""

from __future__ import annotations

import csv
import math
from fractions import Fraction
from pathlib import Path


DIMENSION = 5
ABS_TOLERANCE = 1e-12
OUTPUT_PATH = Path(__file__).with_name("window_aggregation_order_reference.csv")


def vector(*values: str) -> tuple[Fraction, ...]:
    return tuple(Fraction(value) for value in values)


WINDOWS = (
    (
        "W_CONSTANT",
        "constant_complete_z",
        (vector("1/2", "1/2", "1/2", "1/2", "1/2"),) * 2,
    ),
    (
        "W_COORDINATE_SWAP",
        "different_coordinate_identity_and_positive_order_gaps",
        (vector("1", "0", "0", "0", "0"), vector("0", "1", "0", "0", "0")),
    ),
    (
        "W_SAME_REFERENCE_RAY",
        "different_states_with_zero_order_gaps",
        (vector("1/5", "1/5", "1/5", "1/5", "1/5"), vector("4/5", "4/5", "4/5", "4/5", "4/5")),
    ),
    (
        "W_CENTERED_CANCELLATION",
        "opposite_off_axis_shapes_with_balanced_aggregate",
        (vector("1", "0", "0", "0", "0"), vector("0", "1", "1", "1", "1")),
    ),
)


def mean(values: tuple[Fraction, ...]) -> Fraction:
    return sum(values, Fraction(0)) / len(values)


def mean_vector(states: tuple[tuple[Fraction, ...], ...]) -> tuple[Fraction, ...]:
    return tuple(mean(tuple(state[index] for state in states)) for index in range(DIMENSION))


def ik_ref(state: tuple[Fraction, ...]) -> float:
    return float(mean(state))


def ik_m2(state: tuple[Fraction, ...]) -> float:
    return math.sqrt(sum(float(value * value) for value in state) / DIMENSION)


def axis_dev_ref(state: tuple[Fraction, ...]) -> float:
    center = mean(state)
    return math.sqrt(sum(float((value - center) ** 2) for value in state) / DIMENSION)


def exact_vector_text(state: tuple[Fraction, ...]) -> str:
    return "(" + ",".join(str(value) for value in state) + ")"


def decimal_text(value: float) -> str:
    if abs(value) <= ABS_TOLERANCE:
        value = 0.0
    return f"{value:.12f}"


def calculate_row(
    window_id: str,
    role: str,
    states: tuple[tuple[Fraction, ...], ...],
) -> dict[str, str]:
    aggregate_state = mean_vector(states)
    state_ik_ref = tuple(ik_ref(state) for state in states)
    state_ik_m2 = tuple(ik_m2(state) for state in states)
    state_axis_dev = tuple(axis_dev_ref(state) for state in states)

    derive_ik_ref = sum(state_ik_ref) / len(states)
    derive_ik_m2 = sum(state_ik_m2) / len(states)
    derive_axis_dev = sum(state_axis_dev) / len(states)
    aggregate_ik_ref = ik_ref(aggregate_state)
    aggregate_ik_m2 = ik_m2(aggregate_state)
    aggregate_axis_dev = axis_dev_ref(aggregate_state)

    return {
        "window_id": window_id,
        "role": role,
        "member_count": str(len(states)),
        "member_z_exact": ";".join(exact_vector_text(state) for state in states),
        "aggregate_z_exact": exact_vector_text(aggregate_state),
        "derive_then_aggregate_ik_ref": decimal_text(derive_ik_ref),
        "aggregate_then_derive_ik_ref": decimal_text(aggregate_ik_ref),
        "derive_then_aggregate_ik_m2": decimal_text(derive_ik_m2),
        "aggregate_then_derive_ik_m2": decimal_text(aggregate_ik_m2),
        "gap_m2": decimal_text(derive_ik_m2 - aggregate_ik_m2),
        "derive_then_aggregate_axis_dev_ref": decimal_text(derive_axis_dev),
        "aggregate_then_derive_axis_dev_ref": decimal_text(aggregate_axis_dev),
        "gap_axis_dev_ref": decimal_text(derive_axis_dev - aggregate_axis_dev),
    }


def calculate() -> list[dict[str, str]]:
    return [calculate_row(window_id, role, states) for window_id, role, states in WINDOWS]


def verify(rows: list[dict[str, str]]) -> None:
    assert len(rows) == len(WINDOWS)

    for row in rows:
        assert math.isclose(
            float(row["derive_then_aggregate_ik_ref"]),
            float(row["aggregate_then_derive_ik_ref"]),
            rel_tol=0.0,
            abs_tol=ABS_TOLERANCE,
        )
        assert float(row["gap_m2"]) >= -ABS_TOLERANCE
        assert float(row["gap_axis_dev_ref"]) >= -ABS_TOLERANCE

    indexed = {row["window_id"]: row for row in rows}
    constant = indexed["W_CONSTANT"]
    same_ray = indexed["W_SAME_REFERENCE_RAY"]
    swap = indexed["W_COORDINATE_SWAP"]
    cancellation = indexed["W_CENTERED_CANCELLATION"]

    assert float(constant["gap_m2"]) == 0.0
    assert float(constant["gap_axis_dev_ref"]) == 0.0
    assert float(same_ray["gap_m2"]) == 0.0
    assert float(same_ray["gap_axis_dev_ref"]) == 0.0
    assert float(swap["gap_m2"]) > 0.0
    assert float(swap["gap_axis_dev_ref"]) > 0.0
    assert float(cancellation["aggregate_then_derive_axis_dev_ref"]) == 0.0
    assert float(cancellation["derive_then_aggregate_axis_dev_ref"]) > 0.0


def write_csv(rows: list[dict[str, str]]) -> None:
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows = calculate()
    verify(rows)
    write_csv(rows)
    print(f"wrote {len(rows)} verified rows to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
