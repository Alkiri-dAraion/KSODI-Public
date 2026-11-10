#!/usr/bin/env python3
"""Generate dependency-free IK_rel Phase-B component fixtures."""

from __future__ import annotations

import csv
from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parent
GRID_OUTPUT = ROOT / "phase_b_component_grids.csv"
COLLISION_OUTPUT = ROOT / "phase_b_trajectory_collisions.csv"

POSITION_VALUES = tuple(Fraction(value, 4) for value in range(5))
MOVE_VALUES = tuple(Fraction(value, 2) for value in (-2, -1, 0, 1, 2))
ACCEL_VALUES = tuple(Fraction(value, 1) for value in (-2, -1, 0, 1, 2))
TRAJECTORY_VALUES = (Fraction(0), Fraction(1, 2), Fraction(1))


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def decimal_text(value: Fraction) -> str:
    return f"{float(value):.12f}"


def sequence_text(values: tuple[Fraction, ...]) -> str:
    return "(" + ",".join(fraction_text(value) for value in values) + ")"


def component_value(kind: str, value_a: Fraction, value_b: Fraction) -> Fraction:
    divisor = {"gap": 1, "move": 2, "accel": 4}[kind]
    return 1 - abs(value_a - value_b) / divisor


def write_grids() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    domains = {
        "gap": POSITION_VALUES,
        "move": MOVE_VALUES,
        "accel": ACCEL_VALUES,
    }
    for kind, values in domains.items():
        for row_index, value_a in enumerate(values, start=1):
            for column_index, value_b in enumerate(values, start=1):
                value = component_value(kind, value_a, value_b)
                swapped = component_value(kind, value_b, value_a)
                assert Fraction(0) <= value <= 1
                assert value == swapped
                rows.append(
                    {
                        "case_id": f"B-{kind.upper()}-{row_index:02d}-{column_index:02d}",
                        "component_kind": kind,
                        "input_a_exact": fraction_text(value_a),
                        "input_b_exact": fraction_text(value_b),
                        "absolute_gap_exact": fraction_text(abs(value_a - value_b)),
                        "component_value_exact": fraction_text(value),
                        "component_value_decimal": decimal_text(value),
                        "swapped_value_exact": fraction_text(swapped),
                        "component_status_scope": "raw_formula_only_phase_c_applies_zero_policy",
                    }
                )

    with GRID_OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows


def trajectory_record(
    trajectory_a: tuple[Fraction, Fraction, Fraction],
    trajectory_b: tuple[Fraction, Fraction, Fraction],
) -> dict[str, object]:
    a0, a1, a2 = trajectory_a
    b0, b1, b2 = trajectory_b
    delta_a = a2 - a1
    delta_b = b2 - b1
    delta2_a = a2 - 2 * a1 + a0
    delta2_b = b2 - 2 * b1 + b0
    return {
        "trajectory_a": trajectory_a,
        "trajectory_b": trajectory_b,
        "ik_a": a2,
        "ik_b": b2,
        "delta_a": delta_a,
        "delta_b": delta_b,
        "delta2_a": delta2_a,
        "delta2_b": delta2_b,
        "c_gap": component_value("gap", a2, b2),
        "c_move": component_value("move", delta_a, delta_b),
        "c_accel": component_value("accel", delta2_a, delta2_b),
    }


def find_collision_pair(
    records: list[dict[str, object]],
    fixed_component: str,
) -> tuple[dict[str, object], dict[str, object]]:
    other_components = tuple(
        component for component in ("c_gap", "c_move", "c_accel")
        if component != fixed_component
    )
    groups: dict[Fraction, list[dict[str, object]]] = defaultdict(list)
    for record in records:
        groups[record[fixed_component]].append(record)  # type: ignore[index]

    for fixed_value in sorted(groups, reverse=True):
        group = groups[fixed_value]
        for left_index, left in enumerate(group):
            for right in group[left_index + 1:]:
                if (
                    component_is_numeric_at_epsilon_zero(left, fixed_component)
                    and component_is_numeric_at_epsilon_zero(right, fixed_component)
                    and any(left[name] != right[name] for name in other_components)
                ):
                    return left, right
    raise AssertionError(f"no collision found for {fixed_component}")


def component_is_numeric_at_epsilon_zero(
    record: dict[str, object], component: str
) -> bool:
    if component == "c_move":
        return record["delta_a"] != 0 or record["delta_b"] != 0
    if component == "c_accel":
        return record["delta2_a"] != 0 or record["delta2_b"] != 0
    return True


def find_full_component_collision(
    records: list[dict[str, object]],
) -> tuple[dict[str, object], dict[str, object]]:
    groups: dict[tuple[Fraction, Fraction, Fraction], list[dict[str, object]]] = defaultdict(list)
    for record in records:
        key = (record["c_gap"], record["c_move"], record["c_accel"])
        groups[key].append(record)  # type: ignore[arg-type]
    for key in sorted(groups, reverse=True):
        group = groups[key]
        for left_index, left in enumerate(group):
            for right in group[left_index + 1:]:
                if (
                    component_is_numeric_at_epsilon_zero(left, "c_move")
                    and component_is_numeric_at_epsilon_zero(right, "c_move")
                    and component_is_numeric_at_epsilon_zero(left, "c_accel")
                    and component_is_numeric_at_epsilon_zero(right, "c_accel")
                    and (
                        left["trajectory_a"] != right["trajectory_a"]
                        or left["trajectory_b"] != right["trajectory_b"]
                    )
                ):
                    return left, right
    raise AssertionError("no full component collision found")


def record_side(
    row: dict[str, str], prefix: str, record: dict[str, object]
) -> None:
    row[f"{prefix}_trajectory_a"] = sequence_text(record["trajectory_a"])  # type: ignore[arg-type]
    row[f"{prefix}_trajectory_b"] = sequence_text(record["trajectory_b"])  # type: ignore[arg-type]
    for name in (
        "ik_a", "ik_b", "delta_a", "delta_b", "delta2_a", "delta2_b",
        "c_gap", "c_move", "c_accel",
    ):
        row[f"{prefix}_{name}_exact"] = fraction_text(record[name])  # type: ignore[arg-type]


def write_collisions() -> tuple[list[dict[str, str]], int]:
    trajectories = tuple(product(TRAJECTORY_VALUES, repeat=3))
    records = [
        trajectory_record(trajectory_a, trajectory_b)
        for trajectory_a in trajectories
        for trajectory_b in trajectories
    ]
    assert len(records) == 729

    selected = (
        ("B-COLL-GAP", "same_c_gap_different_move_or_accel", "c_gap", find_collision_pair(records, "c_gap")),
        ("B-COLL-MOVE", "same_c_move_different_gap_or_accel", "c_move", find_collision_pair(records, "c_move")),
        ("B-COLL-ACCEL", "same_c_accel_different_gap_or_move", "c_accel", find_collision_pair(records, "c_accel")),
        ("B-COLL-TRIPLE", "same_component_triple_different_trajectories", "all", find_full_component_collision(records)),
    )

    rows: list[dict[str, str]] = []
    for case_id, description, fixed_component, (left, right) in selected:
        row = {
            "case_id": case_id,
            "description": description,
            "fixed_component": fixed_component,
        }
        record_side(row, "left", left)
        record_side(row, "right", right)
        row["underlying_trajectories_equal"] = str(
            left["trajectory_a"] == right["trajectory_a"]
            and left["trajectory_b"] == right["trajectory_b"]
        ).lower()
        rows.append(row)

    assert all(row["underlying_trajectories_equal"] == "false" for row in rows)
    with COLLISION_OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows, len(records)


def main() -> None:
    grids = write_grids()
    collisions, trajectory_pair_count = write_collisions()
    counts = defaultdict(set)
    for row in grids:
        counts[row["component_kind"]].add(row["component_value_exact"])
    print(f"verified_component_grid_rows={len(grids)}")
    print(f"gap_value_classes={len(counts['gap'])}")
    print(f"move_value_classes={len(counts['move'])}")
    print(f"accel_value_classes={len(counts['accel'])}")
    print(f"verified_trajectory_pairs={trajectory_pair_count}")
    print(f"selected_collision_fixtures={len(collisions)}")
    print(f"grid_output={GRID_OUTPUT.name}")
    print(f"collision_output={COLLISION_OUTPUT.name}")


if __name__ == "__main__":
    main()
