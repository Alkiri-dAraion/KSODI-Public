#!/usr/bin/env python3
"""Generate and verify Phase-F ordinal monadic trajectories."""

from __future__ import annotations

import csv
import math
from fractions import Fraction
from pathlib import Path


COORDINATES = ("K", "S", "O", "D", "I")
DIMENSION = len(COORDINATES)
PROFILE_ID = "ik_equal_reference_v350"
ABS_TOLERANCE = 1e-12
POSITIONS_PATH = Path(__file__).with_name("phase_f_trajectory_positions.csv")
SUMMARIES_PATH = Path(__file__).with_name("phase_f_trajectory_summaries.csv")


def vector(*values: str) -> tuple[Fraction, ...]:
    return tuple(Fraction(value) for value in values)


BALANCED = vector("1/2", "1/2", "1/2", "1/2", "1/2")
CONCENTRATED = vector("4/5", "4/5", "1/2", "1/5", "1/5")
CONTRACTED_END = vector("7/10", "4/5", "1/2", "1/5", "3/10")

TRAJECTORIES = (
    {
        "trajectory_id": "F01_STAY_BALANCED",
        "role": "stationary_baseline",
        "states": (BALANCED, BALANCED, BALANCED),
    },
    {
        "trajectory_id": "F02_OUT_BACK_KI",
        "role": "zero_net_nonzero_path_KI",
        "states": (
            BALANCED,
            vector("7/10", "1/2", "1/2", "1/2", "3/10"),
            BALANCED,
        ),
    },
    {
        "trajectory_id": "F03_OUT_BACK_SO",
        "role": "scalar_history_match_different_coordinates",
        "states": (
            BALANCED,
            vector("1/2", "7/10", "3/10", "1/2", "1/2"),
            BALANCED,
        ),
    },
    {
        "trajectory_id": "F04_DIRECT_CONTRACTION",
        "role": "same_endpoint_direct_path",
        "states": (
            CONCENTRATED,
            vector("3/4", "4/5", "1/2", "1/5", "1/4"),
            CONTRACTED_END,
        ),
    },
    {
        "trajectory_id": "F05_DETOUR_SAME_ENDPOINT",
        "role": "same_endpoint_detour_path",
        "states": (
            CONCENTRATED,
            vector("7/10", "9/10", "1/2", "1/5", "1/5"),
            CONTRACTED_END,
        ),
    },
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


def subtract(
    right: tuple[Fraction, ...], left: tuple[Fraction, ...]
) -> tuple[Fraction, ...]:
    return tuple(r_value - l_value for r_value, l_value in zip(right, left))


def l2(values: tuple[Fraction, ...]) -> float:
    return math.sqrt(float(sum((value * value for value in values), Fraction(0))))


def normalized_l2(values: tuple[Fraction, ...]) -> float:
    return l2(values) / math.sqrt(DIMENSION)


def metrics(values: tuple[Fraction, ...]) -> tuple[float, float, float]:
    exact_mean = sum(values, Fraction(0)) / DIMENSION
    mean = float(exact_mean)
    mean_square = float(
        sum((value * value for value in values), Fraction(0)) / DIMENSION
    )
    magnitude = math.sqrt(mean_square)
    deviation = math.sqrt(max(0.0, mean_square - mean * mean))
    assert close(magnitude * magnitude, mean * mean + deviation * deviation)
    return mean, magnitude, deviation


def calculate() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    position_rows: list[dict[str, str]] = []
    summary_rows: list[dict[str, str]] = []

    for trajectory in TRAJECTORIES:
        trajectory_id = str(trajectory["trajectory_id"])
        role = str(trajectory["role"])
        states = trajectory["states"]
        assert len(states) == 3

        deltas = (subtract(states[1], states[0]), subtract(states[2], states[1]))
        second_difference = subtract(deltas[1], deltas[0])
        net_delta = subtract(states[-1], states[0])
        raw_step_lengths = tuple(map(l2, deltas))
        normalized_step_lengths = tuple(map(normalized_l2, deltas))
        raw_path_length = sum(raw_step_lengths)
        normalized_path_length = sum(normalized_step_lengths)
        raw_net_displacement = l2(net_delta)
        normalized_net_displacement = normalized_l2(net_delta)
        state_metrics = tuple(map(metrics, states))

        for step_index, state in enumerate(states):
            mean, magnitude, deviation = state_metrics[step_index]
            if step_index == 0:
                delta_exact = "NA"
                raw_step = "NA"
                normalized_step = "NA"
            else:
                delta_exact = vector_exact(deltas[step_index - 1])
                raw_step = decimal_text(raw_step_lengths[step_index - 1])
                normalized_step = decimal_text(
                    normalized_step_lengths[step_index - 1]
                )

            position_rows.append(
                {
                    "trajectory_id": trajectory_id,
                    "trajectory_role": role,
                    "step_index": str(step_index),
                    **{
                        coordinate: fraction_text(value)
                        for coordinate, value in zip(COORDINATES, state)
                    },
                    "z_exact": vector_exact(state),
                    "delta_z_from_previous_exact": delta_exact,
                    "raw_step_l2": raw_step,
                    "normalized_step_l2": normalized_step,
                    "ik_equal": decimal_text(mean),
                    "ik_m2": decimal_text(magnitude),
                    "axis_dev_eq": decimal_text(deviation),
                    "profile_id": PROFILE_ID,
                }
            )

        ik_values = [entry[0] for entry in state_metrics]
        magnitude_values = [entry[1] for entry in state_metrics]
        deviation_values = [entry[2] for entry in state_metrics]

        summary_rows.append(
            {
                "trajectory_id": trajectory_id,
                "trajectory_role": role,
                "start_z_exact": vector_exact(states[0]),
                "middle_z_exact": vector_exact(states[1]),
                "end_z_exact": vector_exact(states[2]),
                "delta_z_01_exact": vector_exact(deltas[0]),
                "delta_z_12_exact": vector_exact(deltas[1]),
                "delta2_z_exact": vector_exact(second_difference),
                "net_delta_z_exact": vector_exact(net_delta),
                "raw_net_displacement": decimal_text(raw_net_displacement),
                "normalized_net_displacement": decimal_text(
                    normalized_net_displacement
                ),
                "raw_path_length": decimal_text(raw_path_length),
                "normalized_path_length": decimal_text(normalized_path_length),
                "raw_delta2_z_l2": decimal_text(l2(second_difference)),
                "normalized_delta2_z_l2": decimal_text(
                    normalized_l2(second_difference)
                ),
                "net_delta_ik_equal": decimal_text(ik_values[-1] - ik_values[0]),
                "net_delta_ik_m2": decimal_text(
                    magnitude_values[-1] - magnitude_values[0]
                ),
                "net_delta_axis_dev": decimal_text(
                    deviation_values[-1] - deviation_values[0]
                ),
                "ik_equal_range": decimal_text(max(ik_values) - min(ik_values)),
                "ik_m2_range": decimal_text(
                    max(magnitude_values) - min(magnitude_values)
                ),
                "axis_dev_range": decimal_text(
                    max(deviation_values) - min(deviation_values)
                ),
                "profile_id": PROFILE_ID,
            }
        )

    return position_rows, summary_rows


def summary_by(
    rows: list[dict[str, str]], trajectory_id: str
) -> dict[str, str]:
    matches = [row for row in rows if row["trajectory_id"] == trajectory_id]
    assert len(matches) == 1
    return matches[0]


def position_sequence(
    rows: list[dict[str, str]], trajectory_id: str, field: str
) -> tuple[str, ...]:
    matches = [row for row in rows if row["trajectory_id"] == trajectory_id]
    matches.sort(key=lambda row: int(row["step_index"]))
    assert len(matches) == 3
    return tuple(row[field] for row in matches)


def verify(
    position_rows: list[dict[str, str]], summary_rows: list[dict[str, str]]
) -> None:
    assert len(position_rows) == 15
    assert len(summary_rows) == 5
    assert {row["ik_equal"] for row in position_rows} == {"0.500000000000"}

    stay = summary_by(summary_rows, "F01_STAY_BALANCED")
    out_back_ki = summary_by(summary_rows, "F02_OUT_BACK_KI")
    out_back_so = summary_by(summary_rows, "F03_OUT_BACK_SO")
    direct = summary_by(summary_rows, "F04_DIRECT_CONTRACTION")
    detour = summary_by(summary_rows, "F05_DETOUR_SAME_ENDPOINT")

    assert float(stay["raw_net_displacement"]) == 0.0
    assert float(stay["raw_path_length"]) == 0.0

    for out_back in (out_back_ki, out_back_so):
        assert float(out_back["raw_net_displacement"]) == 0.0
        assert float(out_back["raw_path_length"]) > 0.0
        assert float(out_back["ik_m2_range"]) > 0.0
        assert float(out_back["axis_dev_range"]) > 0.0

    for field in ("ik_equal", "ik_m2", "axis_dev_eq"):
        assert position_sequence(position_rows, "F02_OUT_BACK_KI", field) == (
            position_sequence(position_rows, "F03_OUT_BACK_SO", field)
        )
    assert position_sequence(position_rows, "F02_OUT_BACK_KI", "z_exact") != (
        position_sequence(position_rows, "F03_OUT_BACK_SO", "z_exact")
    )

    assert direct["start_z_exact"] == detour["start_z_exact"]
    assert direct["end_z_exact"] == detour["end_z_exact"]
    assert close(
        float(direct["raw_path_length"]), float(direct["raw_net_displacement"])
    )
    assert float(detour["raw_path_length"]) > float(detour["raw_net_displacement"])
    assert float(direct["raw_delta2_z_l2"]) == 0.0
    assert float(detour["raw_delta2_z_l2"]) > 0.0

    direct_magnitude = tuple(
        map(float, position_sequence(position_rows, "F04_DIRECT_CONTRACTION", "ik_m2"))
    )
    detour_magnitude = tuple(
        map(float, position_sequence(position_rows, "F05_DETOUR_SAME_ENDPOINT", "ik_m2"))
    )
    assert direct_magnitude[0] > direct_magnitude[1] > direct_magnitude[2]
    assert detour_magnitude[1] > detour_magnitude[0] > detour_magnitude[2]


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file, fieldnames=list(rows[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    position_rows, summary_rows = calculate()
    verify(position_rows, summary_rows)
    write_csv(POSITIONS_PATH, position_rows)
    write_csv(SUMMARIES_PATH, summary_rows)
    print(f"verified_position_rows={len(position_rows)}")
    print(f"verified_trajectory_rows={len(summary_rows)}")
    print("flat_ik_equal_all_positions=true")
    print("zero_net_nonzero_path=true")
    print("scalar_history_coordinate_collapse=true")
    print("same_endpoints_different_path_and_delta2=true")
    print(f"absolute_tolerance={ABS_TOLERANCE}")
    print(f"positions_output={POSITIONS_PATH.name}")
    print(f"summaries_output={SUMMARIES_PATH.name}")


if __name__ == "__main__":
    main()
