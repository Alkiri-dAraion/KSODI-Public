#!/usr/bin/env python3
"""Generate and verify the Phase-A binary IK reference grid.

This calculator is deliberately independent of the KSODI runtime and uses
only the Python standard library.  It implements the frozen formulas from
PHASE_0_FROZEN_BASIS.md; it is not a production implementation.
"""

from __future__ import annotations

import csv
import itertools
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path


COORDINATES = ("K", "S", "O", "D", "I")
DIMENSION = len(COORDINATES)
PROFILE_ID = "ik_equal_reference_v350"
ABS_TOLERANCE = 1e-12
OUTPUT_PATH = Path(__file__).with_name("phase_a_binary_grid.csv")


def close(left: float, right: float) -> bool:
    return math.isclose(left, right, rel_tol=0.0, abs_tol=ABS_TOLERANCE)


def rational_text(numerator: int, denominator: int) -> str:
    value = Fraction(numerator, denominator)
    return str(value.numerator) if value.denominator == 1 else str(value)


def magnitude_exact(hamming_weight: int) -> str:
    if hamming_weight == 0:
        return "0"
    if hamming_weight == DIMENSION:
        return "1"
    return f"sqrt({rational_text(hamming_weight, DIMENSION)})"


def axis_deviation_exact(hamming_weight: int) -> str:
    radicand = hamming_weight * (DIMENSION - hamming_weight)
    if radicand == 0:
        return "0"
    root = math.isqrt(radicand)
    if root * root == radicand:
        return rational_text(root, DIMENSION)
    return f"sqrt({radicand})/{DIMENSION}"


def calculate_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []

    for ordinal, vector in enumerate(
        itertools.product((0, 1), repeat=DIMENSION), start=1
    ):
        hamming_weight = sum(vector)
        ik_equal = sum(vector) / DIMENSION
        m1 = sum(abs(value) for value in vector) / DIMENSION
        ik_m2 = math.sqrt(sum(value * value for value in vector) / DIMENSION)
        mean = ik_equal
        axis_dev_direct = math.sqrt(
            sum((value - mean) ** 2 for value in vector) / DIMENSION
        )
        axis_dev_identity = math.sqrt(max(0.0, ik_m2**2 - ik_equal**2))

        expected_ik = hamming_weight / DIMENSION
        expected_m2 = math.sqrt(hamming_weight / DIMENSION)
        expected_axis_dev = math.sqrt(
            (hamming_weight / DIMENSION)
            * (1.0 - hamming_weight / DIMENSION)
        )

        assert close(ik_equal, expected_ik)
        assert close(m1, expected_ik)
        assert close(ik_m2, expected_m2)
        assert close(axis_dev_direct, axis_dev_identity)
        assert close(axis_dev_direct, expected_axis_dev)
        assert 0.0 <= ik_equal <= 1.0
        assert 0.0 <= ik_m2 <= 1.0
        assert 0.0 <= axis_dev_direct <= 0.5

        row: dict[str, str] = {
            "case_id": f"A{ordinal:02d}",
            **dict(zip(COORDINATES, map(str, vector))),
            "z_tuple": "(" + ",".join(map(str, vector)) + ")",
            "hamming_weight": str(hamming_weight),
            "ik_equal_exact": rational_text(hamming_weight, DIMENSION),
            "ik_equal": f"{ik_equal:.12f}",
            "m1": f"{m1:.12f}",
            "ik_m2_exact": magnitude_exact(hamming_weight),
            "ik_m2": f"{ik_m2:.12f}",
            "axis_dev_eq_exact": axis_deviation_exact(hamming_weight),
            "axis_dev_eq": f"{axis_dev_direct:.12f}",
            "ik_class_id": f"H{hamming_weight}",
            "ik_m2_class_id": f"H{hamming_weight}",
            "paired_class_id": f"H{hamming_weight}",
            "profile_id": PROFILE_ID,
        }
        rows.append(row)

    return rows


def verify_grid(rows: list[dict[str, str]]) -> None:
    assert len(rows) == 2**DIMENSION
    assert rows[0]["z_tuple"] == "(0,0,0,0,0)"
    assert rows[-1]["z_tuple"] == "(1,1,1,1,1)"

    expected_counts = {
        hamming_weight: math.comb(DIMENSION, hamming_weight)
        for hamming_weight in range(DIMENSION + 1)
    }
    observed_counts = Counter(int(row["hamming_weight"]) for row in rows)
    assert dict(observed_counts) == expected_counts

    # Raster A deliberately demonstrates that all three scalar views collapse
    # the 32 coordinate-labelled vertices into Hamming-weight classes.
    assert len({row["ik_equal"] for row in rows}) == DIMENSION + 1
    assert len({row["ik_m2"] for row in rows}) == DIMENSION + 1
    assert len(
        {
            (row["ik_equal"], row["ik_m2"], row["axis_dev_eq"])
            for row in rows
        }
    ) == DIMENSION + 1
    assert len({row["axis_dev_eq"] for row in rows}) == 3


def write_csv(rows: list[dict[str, str]]) -> None:
    fieldnames = list(rows[0])
    with OUTPUT_PATH.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(
            output_file, fieldnames=fieldnames, lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows = calculate_rows()
    verify_grid(rows)
    write_csv(rows)
    print(f"verified_rows={len(rows)}")
    print("hamming_counts=1,5,10,10,5,1")
    print("unique_ik_equal=6")
    print("unique_ik_m2=6")
    print("unique_paired_scalar_states=6")
    print("unique_axis_dev_eq=3")
    print(f"absolute_tolerance={ABS_TOLERANCE}")
    print(f"output={OUTPUT_PATH.name}")


if __name__ == "__main__":
    main()
