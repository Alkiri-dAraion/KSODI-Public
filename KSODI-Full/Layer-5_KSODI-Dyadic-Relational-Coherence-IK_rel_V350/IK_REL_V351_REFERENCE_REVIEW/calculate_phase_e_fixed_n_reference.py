#!/usr/bin/env python3
"""Generate dependency-free IK_rel Phase-E fixed-component fixtures."""

from __future__ import annotations

import csv
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SETS_OUTPUT = ROOT / "phase_e_fixed_component_sets.csv"
STATUS_OUTPUT = ROOT / "phase_e_status_propagation.csv"
INVALID_OUTPUT = ROOT / "phase_e_invalid_profiles.csv"

COMPONENTS = ("gap", "move", "accel")
COMPONENT_VALUES = {
    "gap": Fraction(1, 4),
    "move": Fraction(1, 2),
    "accel": Fraction(3, 4),
}
BASE_WEIGHT = {"gap": 1, "move": 2, "accel": 3}


def fraction_text(value: Fraction | None) -> str:
    if value is None:
        return ""
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def set_text(component_set: tuple[str, ...]) -> str:
    return "{" + ",".join(component_set) + "}"


def weights_for(component_set: tuple[str, ...]) -> dict[str, Fraction]:
    denominator = sum(BASE_WEIGHT[name] for name in component_set)
    return {
        name: Fraction(BASE_WEIGHT[name], denominator)
        for name in component_set
    }


def weights_text(weights: dict[str, Fraction]) -> str:
    return ";".join(
        f"{name}:{fraction_text(weights[name])}"
        for name in COMPONENTS if name in weights
    )


def weighted_value(
    component_set: tuple[str, ...], weights: dict[str, Fraction]
) -> Fraction:
    return sum(
        (weights[name] * COMPONENT_VALUES[name] for name in component_set),
        Fraction(0),
    )


def all_component_sets() -> tuple[tuple[str, ...], ...]:
    return tuple(
        combination
        for size in range(1, len(COMPONENTS) + 1)
        for combination in combinations(COMPONENTS, size)
    )


def write_sets() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for index, component_set in enumerate(all_component_sets(), start=1):
        weights = weights_for(component_set)
        result = weighted_value(component_set, weights)
        reversed_set = tuple(reversed(component_set))
        reordered_named_result = weighted_value(reversed_set, weights)
        positional_weights = tuple(weights[name] for name in component_set)
        wrongly_rebound = sum(
            (
                positional_weights[position] * COMPONENT_VALUES[name]
                for position, name in enumerate(reversed_set)
            ),
            Fraction(0),
        )
        assert sum(weights.values(), Fraction(0)) == 1
        assert result == reordered_named_result
        rows.append(
            {
                "case_id": f"E-SET-{index:02d}",
                "component_set_N": set_text(component_set),
                "component_count": str(len(component_set)),
                "representative_named_weights": weights_text(weights),
                "sample_component_values": "gap:1/4;move:1/2;accel:3/4",
                "weighted_result_exact": fraction_text(result),
                "reversed_serialization": set_text(reversed_set),
                "named_weight_reordered_result_exact": fraction_text(reordered_named_result),
                "wrong_positional_rebinding_result_exact": fraction_text(wrongly_rebound),
                "positional_rebinding_detectably_wrong": str(
                    len(component_set) > 1 and wrongly_rebound != result
                ).lower(),
                "profile_kind": "test_only_not_canonical_weight_choice",
            }
        )

    assert len(rows) == 7
    assert sum(row["positional_rebinding_detectably_wrong"] == "true" for row in rows) == 4
    with SETS_OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows


def projected_status(
    component_set: tuple[str, ...], statuses: dict[str, str]
) -> str:
    required = tuple(statuses[name] for name in component_set)
    if "processing" in required:
        return "processing_block"
    if "not_observable" in required:
        return "not_observable"
    if any(status != "numeric" for status in required):
        return "not_applicable"
    return "numeric"


def renormalized_drop_value(
    component_set: tuple[str, ...], missing: str
) -> Fraction | None:
    remaining = tuple(name for name in component_set if name != missing)
    if not remaining:
        return None
    original_weights = weights_for(component_set)
    denominator = sum((original_weights[name] for name in remaining), Fraction(0))
    return sum(
        (
            original_weights[name] / denominator * COMPONENT_VALUES[name]
            for name in remaining
        ),
        Fraction(0),
    )


def write_statuses() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for set_index, component_set in enumerate(all_component_sets(), start=1):
        required = component_set[0]
        nonrequired = next(
            (name for name in COMPONENTS if name not in component_set), None
        )
        scenarios: list[tuple[str, dict[str, str]]] = [
            ("all_required_numeric", {}),
            ("required_processing", {required: "processing"}),
            ("required_not_observable", {required: "not_observable"}),
            ("required_not_applicable", {required: "not_applicable"}),
            ("required_not_selected", {required: "not_selected"}),
        ]
        if len(component_set) > 1:
            scenarios.append(
                (
                    "required_processing_precedes_not_observable",
                    {
                        component_set[0]: "processing",
                        component_set[1]: "not_observable",
                    },
                )
            )
        if nonrequired is not None:
            scenarios.append(("nonrequired_processing_does_not_block", {nonrequired: "processing"}))

        for scenario_index, (scenario, changes) in enumerate(scenarios, start=1):
            statuses = {name: "numeric" for name in COMPONENTS}
            statuses.update(changes)
            result_status = projected_status(component_set, statuses)
            missing_required = required if scenario == "required_not_applicable" else None
            forbidden_drop = (
                renormalized_drop_value(component_set, missing_required)
                if missing_required is not None else None
            )
            rows.append(
                {
                    "case_id": f"E-STATUS-{set_index:02d}-{scenario_index:02d}",
                    "component_set_N": set_text(component_set),
                    "scenario": scenario,
                    "status_gap": statuses["gap"],
                    "status_move": statuses["move"],
                    "status_accel": statuses["accel"],
                    "expected_projection_status": result_status,
                    "forbidden_drop_and_renormalize_value_exact": fraction_text(forbidden_drop),
                    "drop_and_renormalize_allowed": "false",
                    "full_T_G_retained": "true",
                }
            )

    assert all(row["drop_and_renormalize_allowed"] == "false" for row in rows)
    with STATUS_OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows


INVALID_CASES = (
    ("E-INVALID-01", "empty_component_set", "N is empty"),
    ("E-INVALID-02", "unknown_or_reserved_component", "N contains shared"),
    ("E-INVALID-03", "duplicate_component_identity", "N contains move twice"),
    ("E-INVALID-04", "missing_named_weight", "one selected component has no weight"),
    ("E-INVALID-05", "extra_named_weight", "weight supplied for component outside N"),
    ("E-INVALID-06", "negative_weight", "one named weight is negative"),
    ("E-INVALID-07", "nonfinite_weight", "one named weight is nonfinite"),
    ("E-INVALID-08", "weight_sum_not_one", "finite nonnegative weights do not sum to one"),
    ("E-INVALID-09", "unnamed_positional_weights", "weights are not bound to component identities"),
)


def write_invalid_profiles() -> list[dict[str, str]]:
    rows = [
        {
            "case_id": case_id,
            "description": description,
            "violated_contract": violated_contract,
            "expected_outcome": "processing_error_invalid_profile",
            "numeric_result_permitted": "false",
        }
        for case_id, description, violated_contract in INVALID_CASES
    ]
    with INVALID_OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows


def main() -> None:
    sets = write_sets()
    statuses = write_statuses()
    invalid = write_invalid_profiles()
    print(f"verified_nonempty_component_sets={len(sets)}")
    print(f"verified_status_rows={len(statuses)}")
    print(f"verified_invalid_profile_rows={len(invalid)}")
    print(f"sets_output={SETS_OUTPUT.name}")
    print(f"status_output={STATUS_OUTPUT.name}")
    print(f"invalid_output={INVALID_OUTPUT.name}")


if __name__ == "__main__":
    main()
