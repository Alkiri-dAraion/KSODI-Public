#!/usr/bin/env python3
"""Generate and verify Phase-C equal-magnitude/different-axis pairs."""

from __future__ import annotations

import csv
import math
from fractions import Fraction
from pathlib import Path


COORDINATES = ("K", "S", "O", "D", "I")
DIMENSION = len(COORDINATES)
PROFILE_ID = "ik_equal_reference_v350"
ABS_TOLERANCE = 1e-12
OUTPUT_PATH = Path(__file__).with_name("phase_c_equal_magnitude_different_axis.csv")

CASES = (
    {
        "case_id": "C01",
        "pair_id": "C_PAIR_1",
        "case_role": "balanced_half",
        "vector": tuple(Fraction(1, 2) for _ in range(DIMENSION)),
        "ik_m2_exact": "1/2",
        "axis_dev_eq_exact": "0",
    },
    {
        "case_id": "C02",
        "pair_id": "C_PAIR_1",
        "case_role": "concentrated_same_magnitude",
        "vector": (
            Fraction(1),
            Fraction(1, 2),
            Fraction(0),
            Fraction(0),
            Fraction(0),
        ),
        "ik_m2_exact": "1/2",
        "axis_dev_eq_exact": "2/5",
    },
    {
        "case_id": "C03",
        "pair_id": "C_PAIR_2",
        "case_role": "one_hot",
        "vector": (
            Fraction(1),
            Fraction(0),
            Fraction(0),
            Fraction(0),
            Fraction(0),
        ),
        "ik_m2_exact": "sqrt(5)/5",
        "axis_dev_eq_exact": "2/5",
    },
    {
        "case_id": "C04",
        "pair_id": "C_PAIR_2",
        "case_role": "three_four_five_split",
        "vector": (
            Fraction(4, 5),
            Fraction(3, 5),
            Fraction(0),
            Fraction(0),
            Fraction(0),
        ),
        "ik_m2_exact": "sqrt(5)/5",
        "axis_dev_eq_exact": "2*sqrt(19)/25",
    },
)


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def calculate_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    for case in CASES:
        vector = case["vector"]
        vector_float = tuple(float(value) for value in vector)
        exact_sum = sum(vector, Fraction(0))
        exact_mean = exact_sum / DIMENSION
        exact_mean_square = (
            sum((value * value for value in vector), Fraction(0)) / DIMENSION
        )
        ik_equal = float(exact_mean)
        ik_m2 = math.sqrt(float(exact_mean_square))
        axis_dev_direct = math.sqrt(
            sum((value - ik_equal) ** 2 for value in vector_float) / DIMENSION
        )
        axis_dev_identity = math.sqrt(max(0.0, ik_m2**2 - ik_equal**2))

        assert math.isclose(
            axis_dev_direct,
            axis_dev_identity,
            rel_tol=0.0,
            abs_tol=ABS_TOLERANCE,
        )

        rows.append(
            {
                "case_id": str(case["case_id"]),
                "pair_id": str(case["pair_id"]),
                "case_role": str(case["case_role"]),
                **{
                    coordinate: fraction_text(value)
                    for coordinate, value in zip(COORDINATES, vector)
                },
                "z_tuple": "(" + ",".join(map(fraction_text, vector)) + ")",
                "coordinate_sum_exact": fraction_text(exact_sum),
                "ik_equal_exact": fraction_text(exact_mean),
                "ik_equal": f"{ik_equal:.12f}",
                "mean_square_exact": fraction_text(exact_mean_square),
                "ik_m2_exact": str(case["ik_m2_exact"]),
                "ik_m2": f"{ik_m2:.12f}",
                "axis_dev_eq_exact": str(case["axis_dev_eq_exact"]),
                "axis_dev_eq": f"{axis_dev_direct:.12f}",
                "profile_id": PROFILE_ID,
            }
        )

    return rows


def verify_pairs(rows: list[dict[str, str]]) -> None:
    assert len(rows) == 4
    for pair_id in ("C_PAIR_1", "C_PAIR_2"):
        pair = [row for row in rows if row["pair_id"] == pair_id]
        assert len(pair) == 2
        assert math.isclose(
            float(pair[0]["ik_m2"]),
            float(pair[1]["ik_m2"]),
            rel_tol=0.0,
            abs_tol=ABS_TOLERANCE,
        )
        assert not math.isclose(
            float(pair[0]["ik_equal"]),
            float(pair[1]["ik_equal"]),
            rel_tol=0.0,
            abs_tol=ABS_TOLERANCE,
        )
        assert pair[0]["z_tuple"] != pair[1]["z_tuple"]

    # At fixed RMS magnitude, more axial position leaves less perpendicular
    # deviation under the equal-profile Pythagorean identity.
    assert float(rows[0]["ik_equal"]) > float(rows[1]["ik_equal"])
    assert float(rows[0]["axis_dev_eq"]) < float(rows[1]["axis_dev_eq"])
    assert float(rows[3]["ik_equal"]) > float(rows[2]["ik_equal"])
    assert float(rows[3]["axis_dev_eq"]) < float(rows[2]["axis_dev_eq"])


def write_csv(rows: list[dict[str, str]]) -> None:
    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file, fieldnames=list(rows[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows = calculate_rows()
    verify_pairs(rows)
    write_csv(rows)
    print(f"verified_rows={len(rows)}")
    print("equal_magnitude_pairs=2")
    print("different_axis_position_per_pair=true")
    print("axis_position_deviation_tradeoff=true")
    print(f"absolute_tolerance={ABS_TOLERANCE}")
    print(f"output={OUTPUT_PATH.name}")


if __name__ == "__main__":
    main()
