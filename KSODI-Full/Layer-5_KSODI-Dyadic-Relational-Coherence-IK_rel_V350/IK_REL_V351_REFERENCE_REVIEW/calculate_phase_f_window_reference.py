#!/usr/bin/env python3
"""Generate dependency-free IK_rel Phase-F window and dynamics fixtures."""

from __future__ import annotations

import csv
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent
WINDOW_OUTPUT = ROOT / "phase_f_window_coverage.csv"
OVERLAP_OUTPUT = ROOT / "phase_f_window_overlap.csv"
DYNAMICS_OUTPUT = ROOT / "phase_f_relational_dynamics.csv"

MIN_AGGREGATE_COUNT = 3
MIN_COVERAGE = Fraction(1, 2)


def fraction_text(value: Fraction | None) -> str:
    if value is None:
        return ""
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def decimal_text(value: Fraction | None) -> str:
    if value is None:
        return ""
    return f"{float(value):.12f}"


def event(gate: str, movement: str, value: Fraction | None = None) -> dict[str, object]:
    return {"gate": gate, "movement": movement, "value": value}


SCENARIOS: tuple[tuple[str, str, tuple[dict[str, object], ...]], ...] = (
    (
        "F-WIN-01",
        "sustained_numeric",
        tuple(
            event("open", "numeric", value)
            for value in (
                Fraction(4, 5), Fraction(41, 50), Fraction(21, 25), Fraction(43, 50),
                Fraction(22, 25), Fraction(9, 10), Fraction(23, 25), Fraction(47, 50),
            )
        ),
    ),
    (
        "F-WIN-02",
        "sparse_high_values",
        (
            event("open", "numeric", Fraction(99, 100)),
            event("closed", "not_reached"),
            event("closed", "not_reached"),
            event("closed", "not_reached"),
            event("open", "numeric", Fraction(1)),
            event("closed", "not_reached"),
            event("closed", "not_reached"),
            event("closed", "not_reached"),
        ),
    ),
    (
        "F-WIN-03",
        "no_numeric_gate_denominator",
        (
            event("not_observable", "not_reached"),
            event("not_observable", "not_reached"),
            event("not_applicable", "not_reached"),
            event("processing", "not_reached"),
        ),
    ),
    (
        "F-WIN-04",
        "all_open_inside_movement_epsilon_band",
        tuple(event("open", "epsilon_band") for _ in range(4)),
    ),
    (
        "F-WIN-05",
        "mixed_gate_and_component_statuses",
        (
            event("open", "numeric", Fraction(4, 5)),
            event("open", "numeric", Fraction(3, 5)),
            event("open", "numeric", Fraction(9, 10)),
            event("open", "epsilon_band"),
            event("open", "epsilon_band"),
            event("open", "not_observable"),
            event("closed", "not_reached"),
            event("closed", "not_reached"),
            event("not_observable", "not_reached"),
            event("not_applicable", "not_reached"),
        ),
    ),
)


def mean(values: list[Fraction]) -> Fraction | None:
    if not values:
        return None
    return sum(values, Fraction(0)) / len(values)


def write_windows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for case_id, description, events in SCENARIOS:
        total = len(events)
        gate_numeric = sum(item["gate"] in ("open", "closed") for item in events)
        gate_open = sum(item["gate"] == "open" for item in events)
        movement_opportunities = sum(
            item["gate"] == "open" and item["movement"] in ("numeric", "epsilon_band")
            for item in events
        )
        epsilon_band = sum(
            item["gate"] == "open" and item["movement"] == "epsilon_band"
            for item in events
        )
        numeric_values = [
            item["value"] for item in events
            if item["gate"] == "open" and item["movement"] == "numeric"
        ]
        assert all(isinstance(value, Fraction) for value in numeric_values)
        numeric_values = list(numeric_values)  # type: ignore[assignment]
        coverage = Fraction(len(numeric_values), total)
        gate_open_rate = (
            Fraction(gate_open, gate_numeric) if gate_numeric > 0 else None
        )
        epsilon_band_rate = (
            Fraction(epsilon_band, movement_opportunities)
            if movement_opportunities > 0 else None
        )
        eligible_mean = mean(numeric_values)  # type: ignore[arg-type]
        aggregate_numeric = (
            len(numeric_values) >= MIN_AGGREGATE_COUNT
            and coverage >= MIN_COVERAGE
        )
        rows.append(
            {
                "case_id": case_id,
                "description": description,
                "total_opportunities": str(total),
                "gate_numeric_count": str(gate_numeric),
                "gate_open_count": str(gate_open),
                "movement_policy_opportunity_count": str(movement_opportunities),
                "movement_epsilon_band_count": str(epsilon_band),
                "eligible_numeric_ik_rel_count": str(len(numeric_values)),
                "coverage_rel_exact": fraction_text(coverage),
                "gate_open_rate_exact": fraction_text(gate_open_rate),
                "gate_open_rate_status": "numeric" if gate_open_rate is not None else "not_evaluable_empty_denominator",
                "movement_epsilon_band_rate_exact": fraction_text(epsilon_band_rate),
                "movement_epsilon_band_rate_status": "numeric" if epsilon_band_rate is not None else "not_evaluable_empty_denominator",
                "eligible_subset_mean_exact": fraction_text(eligible_mean),
                "eligible_subset_mean_decimal": decimal_text(eligible_mean),
                "test_minimum_count": str(MIN_AGGREGATE_COUNT),
                "test_minimum_coverage_exact": fraction_text(MIN_COVERAGE),
                "aggregate_emission": "numeric_emitted" if aggregate_numeric else "not_emitted_minimum_or_coverage",
                "aggregate_method_status": "numeric" if aggregate_numeric else "open_contract_not_inferred",
                "aggregate_value_exact": fraction_text(eligible_mean if aggregate_numeric else None),
                "excluded_partitions_retained": "true",
            }
        )

    by_id = {row["case_id"]: row for row in rows}
    assert by_id["F-WIN-01"]["aggregate_emission"] == "numeric_emitted"
    assert by_id["F-WIN-02"]["eligible_subset_mean_exact"] == "199/200"
    assert by_id["F-WIN-02"]["aggregate_emission"].startswith("not_emitted")
    assert by_id["F-WIN-03"]["gate_open_rate_status"].startswith("not_evaluable")
    assert by_id["F-WIN-04"]["movement_epsilon_band_rate_exact"] == "1"
    assert by_id["F-WIN-05"]["coverage_rel_exact"] == "3/10"
    assert by_id["F-WIN-05"]["gate_open_rate_exact"] == "3/4"
    assert by_id["F-WIN-05"]["movement_epsilon_band_rate_exact"] == "2/5"
    with WINDOW_OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows


SERIES = {
    "j1": Fraction(1, 5),
    "j2": Fraction(2, 5),
    "j3": Fraction(3, 5),
    "j4": Fraction(4, 5),
    "j5": Fraction(1),
    "j6": Fraction(9, 10),
}

WINDOWS = (
    ("F-OVER-01", "sliding_left", ("j1", "j2", "j3", "j4"), "profile-A"),
    ("F-OVER-02", "sliding_right", ("j3", "j4", "j5", "j6"), "profile-A"),
    ("F-OVER-03", "tumbling_left", ("j1", "j2", "j3"), "profile-A"),
    ("F-OVER-04", "tumbling_right", ("j4", "j5", "j6"), "profile-A"),
    ("F-OVER-05", "profile_mismatch_control", ("j3", "j4", "j5", "j6"), "profile-B"),
)


def write_overlap() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for case_id, description, members, profile in WINDOWS:
        value = mean([SERIES[member] for member in members])
        rows.append(
            {
                "case_id": case_id,
                "description": description,
                "member_ids": ";".join(members),
                "member_count": str(len(members)),
                "profile_id": profile,
                "aggregate_exact": fraction_text(value),
                "aggregate_decimal": decimal_text(value),
                "membership_and_overlap_retained": "true",
            }
        )

    by_id = {row["case_id"]: row for row in rows}
    left = Fraction(by_id["F-OVER-01"]["aggregate_exact"])
    right = Fraction(by_id["F-OVER-02"]["aggregate_exact"])
    assert left == Fraction(1, 2)
    assert right == Fraction(33, 40)
    assert right - left == Fraction(13, 40)
    with OVERLAP_OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows


DYNAMIC_STEPS = (
    ("j1", "numeric", Fraction(4, 5)),
    ("j2", "numeric", Fraction(9, 10)),
    ("j3", "gate_closed", None),
    ("j4", "numeric", Fraction(7, 10)),
    ("j5", "numeric", Fraction(3, 5)),
    ("j6", "numeric", Fraction(4, 5)),
)


def write_dynamics() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    previous_numeric: Fraction | None = None
    previous_step_was_numeric = False
    previous_delta: Fraction | None = None
    for step_id, status, value in DYNAMIC_STEPS:
        delta: Fraction | None = None
        delta2: Fraction | None = None
        if status == "numeric" and previous_step_was_numeric:
            assert value is not None and previous_numeric is not None
            delta = value - previous_numeric
            if previous_delta is not None:
                delta2 = delta - previous_delta
        rows.append(
            {
                "relational_step_id": step_id,
                "status_or_gate_transition": status,
                "ik_rel_value_exact": fraction_text(value),
                "delta_ik_rel_exact": fraction_text(delta),
                "delta2_ik_rel_exact": fraction_text(delta2),
                "categorical_transition_encoded_as_numeric_delta": "false",
            }
        )
        if status == "numeric":
            previous_numeric = value
            previous_delta = delta
            previous_step_was_numeric = True
        else:
            previous_numeric = None
            previous_delta = None
            previous_step_was_numeric = False

    assert rows[1]["delta_ik_rel_exact"] == "1/10"
    assert rows[2]["delta_ik_rel_exact"] == ""
    assert rows[3]["delta_ik_rel_exact"] == ""
    assert rows[4]["delta_ik_rel_exact"] == "-1/10"
    assert rows[5]["delta_ik_rel_exact"] == "1/5"
    assert rows[5]["delta2_ik_rel_exact"] == "3/10"
    with DYNAMICS_OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows


def main() -> None:
    windows = write_windows()
    overlap = write_overlap()
    dynamics = write_dynamics()
    print(f"verified_window_scenarios={len(windows)}")
    print(f"verified_overlap_windows={len(overlap)}")
    print(f"verified_dynamic_steps={len(dynamics)}")
    print(f"test_minimum_count={MIN_AGGREGATE_COUNT}")
    print(f"test_minimum_coverage={fraction_text(MIN_COVERAGE)}")
    print(f"window_output={WINDOW_OUTPUT.name}")
    print(f"overlap_output={OVERLAP_OUTPUT.name}")
    print(f"dynamics_output={DYNAMICS_OUTPUT.name}")


if __name__ == "__main__":
    main()
