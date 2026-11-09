#!/usr/bin/env python3
"""Generate and verify Phase-D equal-axis boundary/interior families."""

from __future__ import annotations

import csv
import math
from fractions import Fraction
from pathlib import Path


COORDINATES = ("K", "S", "O", "D", "I")
DIMENSION = len(COORDINATES)
PROFILE_ID = "ik_equal_reference_v350"
ABS_TOLERANCE = 1e-12
OUTPUT_PATH = Path(__file__).with_name("phase_d_equal_axis_families.csv")

CASES = (
    ("D01", "MU_1_5", "balanced_minimum", ("1/5",) * 5, "1/5", "0"),
    (
        "D02",
        "MU_1_5",
        "graduated_interior",
        ("2/5", "3/10", "1/5", "1/10", "0"),
        "sqrt(6)/10",
        "sqrt(2)/10",
    ),
    (
        "D03",
        "MU_1_5",
        "boundary_maximum",
        ("1", "0", "0", "0", "0"),
        "sqrt(5)/5",
        "2/5",
    ),
    ("D04", "MU_2_5", "balanced_minimum", ("2/5",) * 5, "2/5", "0"),
    (
        "D05",
        "MU_2_5",
        "graduated_interior",
        ("4/5", "3/5", "2/5", "1/5", "0"),
        "sqrt(6)/5",
        "sqrt(2)/5",
    ),
    (
        "D06",
        "MU_2_5",
        "boundary_maximum",
        ("1", "1", "0", "0", "0"),
        "sqrt(10)/5",
        "sqrt(6)/5",
    ),
    ("D07", "MU_4_5", "balanced_minimum", ("4/5",) * 5, "4/5", "0"),
    (
        "D08",
        "MU_4_5",
        "graduated_interior",
        ("3/5", "7/10", "4/5", "9/10", "1"),
        "sqrt(66)/10",
        "sqrt(2)/10",
    ),
    (
        "D09",
        "MU_4_5",
        "boundary_maximum",
        ("1", "1", "1", "1", "0"),
        "2*sqrt(5)/5",
        "2/5",
    ),
)


def parse_fraction(text: str) -> Fraction:
    return Fraction(text)


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else str(value)


def calculate_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    for case_id, family_id, role, vector_text, m2_exact, dev_exact in CASES:
        vector = tuple(map(parse_fraction, vector_text))
        vector_float = tuple(map(float, vector))
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
                "case_id": case_id,
                "family_id": family_id,
                "case_role": role,
                **{
                    coordinate: fraction_text(value)
                    for coordinate, value in zip(COORDINATES, vector)
                },
                "z_tuple": "(" + ",".join(map(fraction_text, vector)) + ")",
                "coordinate_sum_exact": fraction_text(exact_sum),
                "ik_equal_exact": fraction_text(exact_mean),
                "ik_equal": f"{ik_equal:.12f}",
                "mean_square_exact": fraction_text(exact_mean_square),
                "ik_m2_exact": m2_exact,
                "ik_m2": f"{ik_m2:.12f}",
                "axis_dev_eq_exact": dev_exact,
                "axis_dev_eq": f"{axis_dev_direct:.12f}",
                "profile_id": PROFILE_ID,
            }
        )

    return rows


def verify_families(rows: list[dict[str, str]]) -> None:
    assert len(rows) == 9
    expected_means = {
        "MU_1_5": Fraction(1, 5),
        "MU_2_5": Fraction(2, 5),
        "MU_4_5": Fraction(4, 5),
    }

    for family_id, expected_mean in expected_means.items():
        family = [row for row in rows if row["family_id"] == family_id]
        assert len(family) == 3
        assert {row["ik_equal_exact"] for row in family} == {
            fraction_text(expected_mean)
        }
        magnitudes = [float(row["ik_m2"]) for row in family]
        deviations = [float(row["axis_dev_eq"]) for row in family]
        assert magnitudes[0] < magnitudes[1] < magnitudes[2]
        assert deviations[0] < deviations[1] < deviations[2]

    # Complementary graduated families have the same deviation but different
    # axial positions and total magnitudes.
    assert math.isclose(
        float(rows[1]["axis_dev_eq"]),
        float(rows[7]["axis_dev_eq"]),
        rel_tol=0.0,
        abs_tol=ABS_TOLERANCE,
    )
    assert not math.isclose(
        float(rows[1]["ik_m2"]),
        float(rows[7]["ik_m2"]),
        rel_tol=0.0,
        abs_tol=ABS_TOLERANCE,
    )

def write_csv(rows: list[dict[str, str]]) -> None:
    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file, fieldnames=list(rows[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows = calculate_rows()
    verify_families(rows)
    write_csv(rows)
    print(f"verified_rows={len(rows)}")
    print("equal_axis_families=3")
    print("strict_magnitude_order_per_family=min<interior<max")
    print("strict_axis_deviation_order_per_family=min<interior<max")
    print("endpoint_uniqueness=proved_in_results_note")
    print(f"absolute_tolerance={ABS_TOLERANCE}")
    print(f"output={OUTPUT_PATH.name}")


if __name__ == "__main__":
    main()
