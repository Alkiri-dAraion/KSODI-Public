#!/usr/bin/env python3
"""Generate and verify equal-size Phase-E perturbations."""

from __future__ import annotations

import csv
import math
from pathlib import Path


COORDINATES = ("K", "S", "O", "D", "I")
DIMENSION = len(COORDINATES)
PROFILE_ID = "ik_equal_reference_v350"
ABS_TOLERANCE = 1e-12
RAW_STEP_L2 = 0.1
OUTPUT_PATH = Path(__file__).with_name("phase_e_equal_size_perturbations.csv")

AXIAL_COMPONENT = RAW_STEP_L2 / math.sqrt(DIMENSION)
TRANSFER_COMPONENT = RAW_STEP_L2 / math.sqrt(2.0)

STARTS = (
    {
        "start_id": "BALANCED",
        "start_z_exact": "(1/2,1/2,1/2,1/2,1/2)",
        "vector": (0.5, 0.5, 0.5, 0.5, 0.5),
    },
    {
        "start_id": "CONCENTRATED",
        "start_z_exact": "(4/5,4/5,1/2,1/5,1/5)",
        "vector": (0.8, 0.8, 0.5, 0.2, 0.2),
    },
)

PERTURBATIONS = (
    {
        "perturbation_id": "AXIAL_PLUS",
        "delta_z_exact": "(sqrt(5)/50,sqrt(5)/50,sqrt(5)/50,sqrt(5)/50,sqrt(5)/50)",
        "delta": (AXIAL_COMPONENT,) * DIMENSION,
    },
    {
        "perturbation_id": "SPREAD_K_TO_I",
        "delta_z_exact": "(sqrt(2)/20,0,0,0,-sqrt(2)/20)",
        "delta": (TRANSFER_COMPONENT, 0.0, 0.0, 0.0, -TRANSFER_COMPONENT),
    },
    {
        "perturbation_id": "CONTRACT_K_TO_I",
        "delta_z_exact": "(-sqrt(2)/20,0,0,0,sqrt(2)/20)",
        "delta": (-TRANSFER_COMPONENT, 0.0, 0.0, 0.0, TRANSFER_COMPONENT),
    },
)


def close(left: float, right: float) -> bool:
    return math.isclose(left, right, rel_tol=0.0, abs_tol=ABS_TOLERANCE)


def decimal_text(value: float) -> str:
    if abs(value) < ABS_TOLERANCE:
        value = 0.0
    return f"{value:.12f}"


def tuple_text(values: tuple[float, ...]) -> str:
    return "(" + ",".join(decimal_text(value) for value in values) + ")"


def metrics(vector: tuple[float, ...]) -> tuple[float, float, float]:
    ik_equal = sum(vector) / DIMENSION
    ik_m2 = math.sqrt(sum(value * value for value in vector) / DIMENSION)
    axis_dev = math.sqrt(
        sum((value - ik_equal) ** 2 for value in vector) / DIMENSION
    )
    assert close(ik_m2**2, ik_equal**2 + axis_dev**2)
    return ik_equal, ik_m2, axis_dev


def calculate_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    case_number = 1

    for start in STARTS:
        start_vector = start["vector"]
        ik_before, m2_before, dev_before = metrics(start_vector)

        for perturbation in PERTURBATIONS:
            delta = perturbation["delta"]
            target_vector = tuple(
                value + change for value, change in zip(start_vector, delta)
            )
            raw_delta_l2 = math.sqrt(sum(change * change for change in delta))
            normalized_delta_l2 = raw_delta_l2 / math.sqrt(DIMENSION)
            ik_after, m2_after, dev_after = metrics(target_vector)

            assert close(raw_delta_l2, RAW_STEP_L2)
            assert all(0.0 <= value <= 1.0 for value in target_vector)

            rows.append(
                {
                    "case_id": f"E{case_number:02d}",
                    "start_id": str(start["start_id"]),
                    "perturbation_id": str(perturbation["perturbation_id"]),
                    "start_z_exact": str(start["start_z_exact"]),
                    "start_z": tuple_text(start_vector),
                    "delta_z_exact": str(perturbation["delta_z_exact"]),
                    "delta_z": tuple_text(delta),
                    "target_z": tuple_text(target_vector),
                    "raw_delta_l2": decimal_text(raw_delta_l2),
                    "normalized_delta_l2": decimal_text(normalized_delta_l2),
                    "ik_equal_before": decimal_text(ik_before),
                    "ik_equal_after": decimal_text(ik_after),
                    "delta_ik_equal": decimal_text(ik_after - ik_before),
                    "ik_m2_before": decimal_text(m2_before),
                    "ik_m2_after": decimal_text(m2_after),
                    "delta_ik_m2": decimal_text(m2_after - m2_before),
                    "axis_dev_before": decimal_text(dev_before),
                    "axis_dev_after": decimal_text(dev_after),
                    "delta_axis_dev": decimal_text(dev_after - dev_before),
                    "profile_id": PROFILE_ID,
                }
            )
            case_number += 1

    return rows


def row_by(rows: list[dict[str, str]], start: str, perturbation: str) -> dict[str, str]:
    matches = [
        row
        for row in rows
        if row["start_id"] == start and row["perturbation_id"] == perturbation
    ]
    assert len(matches) == 1
    return matches[0]


def verify_sensitivity(rows: list[dict[str, str]]) -> None:
    assert len(rows) == 6
    assert len({row["raw_delta_l2"] for row in rows}) == 1
    assert len({row["normalized_delta_l2"] for row in rows}) == 1

    balanced_axial = row_by(rows, "BALANCED", "AXIAL_PLUS")
    concentrated_axial = row_by(rows, "CONCENTRATED", "AXIAL_PLUS")
    balanced_spread = row_by(rows, "BALANCED", "SPREAD_K_TO_I")
    balanced_contract = row_by(rows, "BALANCED", "CONTRACT_K_TO_I")
    concentrated_spread = row_by(rows, "CONCENTRATED", "SPREAD_K_TO_I")
    concentrated_contract = row_by(rows, "CONCENTRATED", "CONTRACT_K_TO_I")

    assert close(float(balanced_axial["delta_axis_dev"]), 0.0)
    assert close(float(concentrated_axial["delta_axis_dev"]), 0.0)
    assert close(
        float(balanced_axial["delta_ik_equal"]),
        float(concentrated_axial["delta_ik_equal"]),
    )
    assert not close(
        float(balanced_axial["delta_ik_m2"]),
        float(concentrated_axial["delta_ik_m2"]),
    )

    assert close(float(balanced_spread["delta_ik_equal"]), 0.0)
    assert close(float(balanced_contract["delta_ik_equal"]), 0.0)
    assert close(
        float(balanced_spread["delta_ik_m2"]),
        float(balanced_contract["delta_ik_m2"]),
    )
    assert close(
        float(balanced_spread["delta_axis_dev"]),
        float(balanced_contract["delta_axis_dev"]),
    )

    assert close(float(concentrated_spread["delta_ik_equal"]), 0.0)
    assert close(float(concentrated_contract["delta_ik_equal"]), 0.0)
    assert float(concentrated_spread["delta_ik_m2"]) > 0.0
    assert float(concentrated_spread["delta_axis_dev"]) > 0.0
    assert float(concentrated_contract["delta_ik_m2"]) < 0.0
    assert float(concentrated_contract["delta_axis_dev"]) < 0.0


def write_csv(rows: list[dict[str, str]]) -> None:
    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file, fieldnames=list(rows[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows = calculate_rows()
    verify_sensitivity(rows)
    write_csv(rows)
    print(f"verified_rows={len(rows)}")
    print("equal_raw_delta_l2=0.100000000000")
    print("equal_normalized_delta_l2=0.044721359550")
    print("balanced_transfer_symmetry=true")
    print("concentrated_direction_sensitivity=true")
    print(f"absolute_tolerance={ABS_TOLERANCE}")
    print(f"output={OUTPUT_PATH.name}")


if __name__ == "__main__":
    main()
