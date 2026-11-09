#!/usr/bin/env python3
"""Generate and verify Phase-B equal-mean concentration counterexamples."""

from __future__ import annotations

import csv
import math
from fractions import Fraction
from pathlib import Path


COORDINATES = ("K", "S", "O", "D", "I")
DIMENSION = len(COORDINATES)
PROFILE_ID = "ik_equal_reference_v350"
ABS_TOLERANCE = 1e-12
OUTPUT_PATH = Path(__file__).with_name("phase_b_equal_mean_concentration.csv")

CASES = (
    {
        "case_id": "B01",
        "case_role": "balanced_minimum",
        "vector": tuple(Fraction(1, 2) for _ in range(DIMENSION)),
        "ik_m2_exact": "1/2",
        "axis_dev_eq_exact": "0",
    },
    {
        "case_id": "B02",
        "case_role": "graduated_interior",
        "vector": (
            Fraction(7, 10),
            Fraction(3, 5),
            Fraction(1, 2),
            Fraction(2, 5),
            Fraction(3, 10),
        ),
        "ik_m2_exact": "3*sqrt(3)/10",
        "axis_dev_eq_exact": "sqrt(2)/10",
    },
    {
        "case_id": "B03",
        "case_role": "boundary_maximum_KS",
        "vector": (
            Fraction(1),
            Fraction(1),
            Fraction(1, 2),
            Fraction(0),
            Fraction(0),
        ),
        "ik_m2_exact": "3*sqrt(5)/10",
        "axis_dev_eq_exact": "sqrt(5)/5",
    },
    {
        "case_id": "B04",
        "case_role": "boundary_maximum_DI_permutation",
        "vector": (
            Fraction(0),
            Fraction(0),
            Fraction(1, 2),
            Fraction(1),
            Fraction(1),
        ),
        "ik_m2_exact": "3*sqrt(5)/10",
        "axis_dev_eq_exact": "sqrt(5)/5",
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
        m1 = sum(abs(value) for value in vector_float) / DIMENSION
        ik_m2 = math.sqrt(float(exact_mean_square))
        axis_dev_direct = math.sqrt(
            sum((value - ik_equal) ** 2 for value in vector_float) / DIMENSION
        )
        axis_dev_identity = math.sqrt(max(0.0, ik_m2**2 - ik_equal**2))

        assert exact_mean == Fraction(1, 2)
        assert math.isclose(m1, ik_equal, rel_tol=0.0, abs_tol=ABS_TOLERANCE)
        assert math.isclose(
            axis_dev_direct,
            axis_dev_identity,
            rel_tol=0.0,
            abs_tol=ABS_TOLERANCE,
        )

        rows.append(
            {
                "case_id": str(case["case_id"]),
                "case_role": str(case["case_role"]),
                **{
                    coordinate: fraction_text(value)
                    for coordinate, value in zip(COORDINATES, vector)
                },
                "z_tuple": "(" + ",".join(map(fraction_text, vector)) + ")",
                "coordinate_sum_exact": fraction_text(exact_sum),
                "ik_equal_exact": fraction_text(exact_mean),
                "ik_equal": f"{ik_equal:.12f}",
                "m1": f"{m1:.12f}",
                "mean_square_exact": fraction_text(exact_mean_square),
                "ik_m2_exact": str(case["ik_m2_exact"]),
                "ik_m2": f"{ik_m2:.12f}",
                "axis_dev_eq_exact": str(case["axis_dev_eq_exact"]),
                "axis_dev_eq": f"{axis_dev_direct:.12f}",
                "profile_id": PROFILE_ID,
            }
        )

    return rows


def verify_cases(rows: list[dict[str, str]]) -> None:
    assert len(rows) == 4
    assert len({row["ik_equal"] for row in rows}) == 1
    assert len({row["m1"] for row in rows}) == 1

    magnitudes = [float(row["ik_m2"]) for row in rows]
    deviations = [float(row["axis_dev_eq"]) for row in rows]
    assert magnitudes[0] < magnitudes[1] < magnitudes[2]
    assert deviations[0] < deviations[1] < deviations[2]
    assert math.isclose(
        magnitudes[2], magnitudes[3], rel_tol=0.0, abs_tol=ABS_TOLERANCE
    )
    assert math.isclose(
        deviations[2], deviations[3], rel_tol=0.0, abs_tol=ABS_TOLERANCE
    )
    assert rows[2]["z_tuple"] != rows[3]["z_tuple"]


def write_csv(rows: list[dict[str, str]]) -> None:
    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file, fieldnames=list(rows[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows = calculate_rows()
    verify_cases(rows)
    write_csv(rows)
    print(f"verified_rows={len(rows)}")
    print("shared_ik_equal=0.500000000000")
    print("strict_magnitude_order=B01<B02<B03")
    print("strict_axis_deviation_order=B01<B02<B03")
    print("permutation_scalar_identity=B03=B04")
    print(f"absolute_tolerance={ABS_TOLERANCE}")
    print(f"output={OUTPUT_PATH.name}")


if __name__ == "__main__":
    main()
