#!/usr/bin/env python3
"""Generate and verify Phase-G stable non-equal-axis reference geometry."""

from __future__ import annotations

import csv
import itertools
import math
from fractions import Fraction
from pathlib import Path


COORDINATES = ("K", "S", "O", "D", "I")
DIMENSION = len(COORDINATES)
ABS_TOLERANCE = 1e-12
GRID_PATH = Path(__file__).with_name("phase_g_general_axis_binary_grid.csv")
CASES_PATH = Path(__file__).with_name("phase_g_general_axis_cases.csv")


def vector(*values: str) -> tuple[Fraction, ...]:
    return tuple(Fraction(value) for value in values)


PROFILES = (
    ("ik_equal_reference_v350", vector("1/5", "1/5", "1/5", "1/5", "1/5")),
    ("ik_grad_control_v351", vector("3/10", "1/4", "1/5", "3/20", "1/10")),
    ("ik_grad_rev_control_v351", vector("1/10", "3/20", "1/5", "1/4", "3/10")),
    ("ik_K_peak_control_v351", vector("3/5", "1/10", "1/10", "1/10", "1/10")),
    ("ik_I_peak_control_v351", vector("1/10", "1/10", "1/10", "1/10", "3/5")),
)


CASES = (
    ("G_ZERO", "zero_boundary", vector("0", "0", "0", "0", "0")),
    ("G_ALL_ONE", "upper_cube_corner", vector("1", "1", "1", "1", "1")),
    ("G_BALANCED_HALF", "equal_coordinate_interior", vector("1/2", "1/2", "1/2", "1/2", "1/2")),
    ("G_K_ONLY", "coordinate_identity_K", vector("1", "0", "0", "0", "0")),
    ("G_I_ONLY", "coordinate_identity_I", vector("0", "0", "0", "0", "1")),
    ("G_GRAD_ALIGNED", "aligned_with_grad_weight_ray", vector("3/5", "1/2", "2/5", "3/10", "1/5")),
    ("G_GRAD_REV_ALIGNED", "aligned_with_reversed_grad_weight_ray", vector("1/5", "3/10", "2/5", "1/2", "3/5")),
    ("G_K_PEAK_ALIGNED", "aligned_with_K_peak_weight_ray", vector("1", "1/6", "1/6", "1/6", "1/6")),
    ("G_I_PEAK_ALIGNED", "aligned_with_I_peak_weight_ray", vector("1/6", "1/6", "1/6", "1/6", "1")),
    ("G_FIXED_ASYMMETRIC", "fixed_state_axis_change_control", vector("4/5", "3/5", "2/5", "1/5", "1/10")),
)


def close(left: float, right: float) -> bool:
    return math.isclose(left, right, rel_tol=0.0, abs_tol=ABS_TOLERANCE)


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def vector_exact(values: tuple[Fraction, ...]) -> str:
    return "(" + ",".join(map(fraction_text, values)) + ")"


def decimal_text(value: float) -> str:
    if abs(value) < ABS_TOLERANCE:
        value = 0.0
    return f"{value:.12f}"


def dot(left: tuple[Fraction, ...], right: tuple[Fraction, ...]) -> Fraction:
    return sum((a * b for a, b in zip(left, right)), Fraction(0))


def squared_norm_exact(values: tuple[Fraction, ...]) -> Fraction:
    return dot(values, values)


def metrics(
    state: tuple[Fraction, ...], weights: tuple[Fraction, ...]
) -> dict[str, float | Fraction]:
    ik_w_exact = dot(weights, state)
    weight_norm = math.sqrt(float(squared_norm_exact(weights)))
    state_norm = math.sqrt(float(squared_norm_exact(state)))
    ik_m2 = state_norm / math.sqrt(DIMENSION)
    axis_coordinate_raw = float(ik_w_exact) / weight_norm
    axis_component_normalized = axis_coordinate_raw / math.sqrt(DIMENSION)

    unit_axis = tuple(float(weight) / weight_norm for weight in weights)
    residual = tuple(
        float(value) - axis_coordinate_raw * unit_component
        for value, unit_component in zip(state, unit_axis)
    )
    axis_dev = math.sqrt(sum(value * value for value in residual)) / math.sqrt(
        DIMENSION
    )
    pythagorean_error = ik_m2 * ik_m2 - (
        axis_component_normalized * axis_component_normalized + axis_dev * axis_dev
    )
    raw_ik_substitution_error = ik_m2 * ik_m2 - (
        float(ik_w_exact) * float(ik_w_exact) + axis_dev * axis_dev
    )

    return {
        "ik_w_exact": ik_w_exact,
        "weight_norm": weight_norm,
        "axis_coordinate_raw": axis_coordinate_raw,
        "axis_component_normalized": axis_component_normalized,
        "ik_m2": ik_m2,
        "axis_dev_w": axis_dev,
        "pythagorean_error": pythagorean_error,
        "raw_ik_substitution_error": raw_ik_substitution_error,
    }


def row_for(
    state_id: str,
    state_role: str,
    state: tuple[Fraction, ...],
    profile_id: str,
    weights: tuple[Fraction, ...],
) -> dict[str, str]:
    values = metrics(state, weights)
    return {
        "state_id": state_id,
        "state_role": state_role,
        **{
            coordinate: fraction_text(value)
            for coordinate, value in zip(COORDINATES, state)
        },
        "z_exact": vector_exact(state),
        "profile_id": profile_id,
        "weights_exact": vector_exact(weights),
        "weight_norm_l2": decimal_text(float(values["weight_norm"])),
        "ik_w_exact": fraction_text(values["ik_w_exact"]),
        "ik_w": decimal_text(float(values["ik_w_exact"])),
        "axis_coordinate_raw": decimal_text(float(values["axis_coordinate_raw"])),
        "axis_component_normalized": decimal_text(
            float(values["axis_component_normalized"])
        ),
        "ik_m2": decimal_text(float(values["ik_m2"])),
        "axis_dev_w": decimal_text(float(values["axis_dev_w"])),
        "pythagorean_error": decimal_text(float(values["pythagorean_error"])),
        "raw_ik_substitution_error": decimal_text(
            float(values["raw_ik_substitution_error"])
        ),
    }


def calculate() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    grid_rows: list[dict[str, str]] = []
    case_rows: list[dict[str, str]] = []

    for bits in itertools.product((0, 1), repeat=DIMENSION):
        state = tuple(Fraction(bit) for bit in bits)
        state_id = "G_BIN_" + "".join(map(str, bits))
        role = f"binary_hamming_{sum(bits)}"
        for profile_id, weights in PROFILES:
            grid_rows.append(row_for(state_id, role, state, profile_id, weights))

    for state_id, role, state in CASES:
        for profile_id, weights in PROFILES:
            case_rows.append(row_for(state_id, role, state, profile_id, weights))

    return grid_rows, case_rows


def rows_for(
    rows: list[dict[str, str]], state_id: str
) -> dict[str, dict[str, str]]:
    selected = {row["profile_id"]: row for row in rows if row["state_id"] == state_id}
    assert len(selected) == len(PROFILES)
    return selected


def verify(grid_rows: list[dict[str, str]], case_rows: list[dict[str, str]]) -> None:
    assert len(grid_rows) == 32 * len(PROFILES)
    assert len(case_rows) == len(CASES) * len(PROFILES)

    for row in grid_rows + case_rows:
        assert abs(float(row["pythagorean_error"])) <= ABS_TOLERANCE

    for state_id in {row["state_id"] for row in grid_rows + case_rows}:
        selected = rows_for(grid_rows + case_rows, state_id)
        assert len({row["ik_m2"] for row in selected.values()}) == 1

    zero = rows_for(case_rows, "G_ZERO")
    for row in zero.values():
        assert float(row["ik_w"]) == 0.0
        assert float(row["ik_m2"]) == 0.0
        assert float(row["axis_dev_w"]) == 0.0

    all_one = rows_for(case_rows, "G_ALL_ONE")
    assert {row["ik_w"] for row in all_one.values()} == {"1.000000000000"}
    assert {row["ik_m2"] for row in all_one.values()} == {"1.000000000000"}
    assert float(all_one["ik_equal_reference_v350"]["axis_dev_w"]) == 0.0
    for profile_id, row in all_one.items():
        if profile_id != "ik_equal_reference_v350":
            assert float(row["axis_dev_w"]) > 0.0
            assert abs(float(row["raw_ik_substitution_error"])) > ABS_TOLERANCE

    k_only = rows_for(case_rows, "G_K_ONLY")
    i_only = rows_for(case_rows, "G_I_ONLY")
    equal_id = "ik_equal_reference_v350"
    for field in ("ik_w", "axis_component_normalized", "ik_m2", "axis_dev_w"):
        assert k_only[equal_id][field] == i_only[equal_id][field]
    assert float(k_only["ik_K_peak_control_v351"]["ik_w"]) > float(
        i_only["ik_K_peak_control_v351"]["ik_w"]
    )
    assert float(i_only["ik_I_peak_control_v351"]["ik_w"]) > float(
        k_only["ik_I_peak_control_v351"]["ik_w"]
    )

    aligned_expectations = {
        "G_GRAD_ALIGNED": "ik_grad_control_v351",
        "G_GRAD_REV_ALIGNED": "ik_grad_rev_control_v351",
        "G_K_PEAK_ALIGNED": "ik_K_peak_control_v351",
        "G_I_PEAK_ALIGNED": "ik_I_peak_control_v351",
    }
    for state_id, profile_id in aligned_expectations.items():
        selected = rows_for(case_rows, state_id)
        assert float(selected[profile_id]["axis_dev_w"]) == 0.0

    fixed = rows_for(case_rows, "G_FIXED_ASYMMETRIC")
    assert len({row["ik_w"] for row in fixed.values()}) > 1
    assert len({row["axis_dev_w"] for row in fixed.values()}) > 1
    assert len({row["ik_m2"] for row in fixed.values()}) == 1

    non_equal_rows = [
        row
        for row in grid_rows + case_rows
        if row["profile_id"] != equal_id
    ]
    assert any(
        abs(float(row["raw_ik_substitution_error"])) > ABS_TOLERANCE
        for row in non_equal_rows
    )


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    assert rows
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(rows[0]),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    grid_rows, case_rows = calculate()
    verify(grid_rows, case_rows)
    write_csv(GRID_PATH, grid_rows)
    write_csv(CASES_PATH, case_rows)
    print(f"wrote {len(grid_rows)} verified rows to {GRID_PATH}")
    print(f"wrote {len(case_rows)} verified rows to {CASES_PATH}")


if __name__ == "__main__":
    main()
