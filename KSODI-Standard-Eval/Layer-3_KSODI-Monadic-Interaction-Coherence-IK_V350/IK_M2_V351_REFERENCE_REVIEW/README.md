# IK v3.51 mathematical reference package

## What this package is

This directory provides the reproducible mathematical reference evidence for
the v3.51 joint monadic IK view:

```text
complete typed Z
├── IK_w          active weighted projection
├── IK_M2         normalized complete-vector L2 magnitude
├── IK_ref        position on the fixed equal-coordinate diagonal
├── AxisDev_ref   normalized deviation from that fixed diagonal
└── identities, profiles, typed statuses, evidence and provenance
```

The readings answer different questions. They are inspected jointly but are
not added into one total score. Complete labelled and typed `Z` remains the
recoverable primary object.

The package contains exact synthetic fixtures, dependency-free Python
generators, machine-readable CSV outputs and human-readable result reports. It
supports inspection, criticism and implementation-conformance preparation. It
does not establish empirical validity, semantic adequacy, domain thresholds,
runtime conformance or action authority.

## Quick reading routes

For a human method reader:

1. start with the [frozen basis](./PHASE_0_FROZEN_BASIS.md);
2. read the [result contract](./IK_M2_V351_RESULT_CONTRACT_V01.md);
3. use the [question–measurement–view matrix](./IK_QUESTION_MEASUREMENT_VIEW_MATRIX_V351.md);
4. follow Phase A through G and then the window-order report;
5. return to the complete typed-Z and IK method files linked from Phase 0.

For a developer or machine reader:

1. verify [`REFERENCE_PACKAGE_SHA256SUMS_V351.txt`](./REFERENCE_PACKAGE_SHA256SUMS_V351.txt);
2. run all eight `calculate_*.py` generators with Python 3;
3. confirm that no tracked CSV changes;
4. retain full labelled Z, identities, profiles and typed statuses beside every
   derived scalar;
5. treat the scripts as reference arithmetic, not as a production schema or
   accepted runtime implementation.

## Review sequence and bounded questions

| Stage | Main question | Report |
| --- | --- | --- |
| Phase 0 | Which sources, formulas, fixtures and numeric rules are frozen? | [`PHASE_0_FROZEN_BASIS.md`](./PHASE_0_FROZEN_BASIS.md) |
| A | What collapses on all 32 binary vertices under the equal reference? | [`PHASE_A_BINARY_GRID_RESULTS.md`](./PHASE_A_BINARY_GRID_RESULTS.md) |
| B | Can equal mean hide different concentration and magnitude? | [`PHASE_B_EQUAL_MEAN_CONCENTRATION_RESULTS.md`](./PHASE_B_EQUAL_MEAN_CONCENTRATION_RESULTS.md) |
| C | Can equal magnitude occur at different reference-axis positions? | [`PHASE_C_EQUAL_MAGNITUDE_DIFFERENT_AXIS_RESULTS.md`](./PHASE_C_EQUAL_MAGNITUDE_DIFFERENT_AXIS_RESULTS.md) |
| D | What ranges remain possible at one fixed reference-axis position? | [`PHASE_D_EQUAL_AXIS_FAMILIES_RESULTS.md`](./PHASE_D_EQUAL_AXIS_FAMILIES_RESULTS.md) |
| E | Do equal-sized changes remain distinguishable by direction and start state? | [`PHASE_E_EQUAL_SIZE_PERTURBATION_RESULTS.md`](./PHASE_E_EQUAL_SIZE_PERTURBATION_RESULTS.md) |
| F | Which path, net and ordinal second-difference distinctions survive over trajectories? | [`PHASE_F_MONADIC_TRAJECTORY_RESULTS.md`](./PHASE_F_MONADIC_TRAJECTORY_RESULTS.md) |
| G | How do weighted functionals, weight-ray geometry and fixed-reference geometry differ? | [`PHASE_G_GENERAL_AXIS_GEOMETRY_RESULTS.md`](./PHASE_G_GENERAL_AXIS_GEOMETRY_RESULTS.md) |
| Window | What changes when derivation and arithmetic-mean aggregation exchange order? | [`WINDOW_AGGREGATION_ORDER_REFERENCE_RESULTS.md`](./WINDOW_AGGREGATION_ORDER_REFERENCE_RESULTS.md) |

## Contracts and navigation

- [`IK_M2_V351_RESULT_CONTRACT_V01.md`](./IK_M2_V351_RESULT_CONTRACT_V01.md)
  defines result kinds, formulas, identities, statuses, provenance and
  conformance boundaries;
- [`IK_QUESTION_MEASUREMENT_VIEW_MATRIX_V351.md`](./IK_QUESTION_MEASUREMENT_VIEW_MATRIX_V351.md)
  routes current questions to the required retained objects, calculations and
  bounded views;
- [`IK_V351_WINDOW_AGGREGATION_ORDER_CONTRACT_V01.md`](./IK_V351_WINDOW_AGGREGATION_ORDER_CONTRACT_V01.md)
  distinguishes window identities, eligibility, coverage, status and the two
  aggregation orders.

## Exact artifact inventory

### Phase A

- [`calculate_phase_a_reference.py`](./calculate_phase_a_reference.py)
- [`phase_a_binary_grid.csv`](./phase_a_binary_grid.csv)
- [`PHASE_A_BINARY_GRID_RESULTS.md`](./PHASE_A_BINARY_GRID_RESULTS.md)

### Phase B

- [`calculate_phase_b_reference.py`](./calculate_phase_b_reference.py)
- [`phase_b_equal_mean_concentration.csv`](./phase_b_equal_mean_concentration.csv)
- [`PHASE_B_EQUAL_MEAN_CONCENTRATION_RESULTS.md`](./PHASE_B_EQUAL_MEAN_CONCENTRATION_RESULTS.md)

### Phase C

- [`calculate_phase_c_reference.py`](./calculate_phase_c_reference.py)
- [`phase_c_equal_magnitude_different_axis.csv`](./phase_c_equal_magnitude_different_axis.csv)
- [`PHASE_C_EQUAL_MAGNITUDE_DIFFERENT_AXIS_RESULTS.md`](./PHASE_C_EQUAL_MAGNITUDE_DIFFERENT_AXIS_RESULTS.md)

### Phase D

- [`calculate_phase_d_reference.py`](./calculate_phase_d_reference.py)
- [`phase_d_equal_axis_families.csv`](./phase_d_equal_axis_families.csv)
- [`PHASE_D_EQUAL_AXIS_FAMILIES_RESULTS.md`](./PHASE_D_EQUAL_AXIS_FAMILIES_RESULTS.md)

### Phase E

- [`calculate_phase_e_reference.py`](./calculate_phase_e_reference.py)
- [`phase_e_equal_size_perturbations.csv`](./phase_e_equal_size_perturbations.csv)
- [`PHASE_E_EQUAL_SIZE_PERTURBATION_RESULTS.md`](./PHASE_E_EQUAL_SIZE_PERTURBATION_RESULTS.md)

### Phase F

- [`calculate_phase_f_reference.py`](./calculate_phase_f_reference.py)
- [`phase_f_trajectory_positions.csv`](./phase_f_trajectory_positions.csv)
- [`phase_f_trajectory_summaries.csv`](./phase_f_trajectory_summaries.csv)
- [`PHASE_F_MONADIC_TRAJECTORY_RESULTS.md`](./PHASE_F_MONADIC_TRAJECTORY_RESULTS.md)

### Phase G

- [`calculate_phase_g_general_axis_reference.py`](./calculate_phase_g_general_axis_reference.py)
- [`phase_g_general_axis_binary_grid.csv`](./phase_g_general_axis_binary_grid.csv)
- [`phase_g_general_axis_cases.csv`](./phase_g_general_axis_cases.csv)
- [`PHASE_G_GENERAL_AXIS_GEOMETRY_RESULTS.md`](./PHASE_G_GENERAL_AXIS_GEOMETRY_RESULTS.md)

### Window aggregation order

- [`calculate_window_aggregation_order_reference.py`](./calculate_window_aggregation_order_reference.py)
- [`window_aggregation_order_reference.csv`](./window_aggregation_order_reference.csv)
- [`WINDOW_AGGREGATION_ORDER_REFERENCE_RESULTS.md`](./WINDOW_AGGREGATION_ORDER_REFERENCE_RESULTS.md)

Together with Phase 0 and the three contracts, these are the 30 hashed
evidence artifacts. This README and the checksum manifest are navigation and
verification surfaces and are deliberately not self-hashed by the manifest.

## Reproduction

From this directory:

```sh
shasum -a 256 -c REFERENCE_PACKAGE_SHA256SUMS_V351.txt

for script in calculate_*.py; do
  python3 "$script"
done

git diff --exit-code -- '*.csv'
```

Expected generator totals:

```text
Phase A: 32 rows
Phase B: 4 rows
Phase C: 4 rows
Phase D: 9 rows
Phase E: 6 rows
Phase F: 15 position rows and 5 trajectory rows
Phase G: 160 binary-grid rows and 50 selected-case rows
Window order: 4 rows
```

The generators use only the Python standard library. Decimal output is
reported to twelve places where declared; comparisons use the numeric rules
frozen in Phase 0. Do not round display values and then reuse them as method
operands.

## Interpretation guards

- `IK_w`, `IK_M2`, `IK_ref` and `AxisDev_ref` are not interchangeable.
- `IK_ref` is a derived support coordinate, not an independent confirmation.
- Historical fixture field names remain evidence; Phase 0 states their current
  v3.51 mapping.
- Phase-G weight-ray `AxisDev_w` is not canonical fixed-diagonal
  `AxisDev_ref`.
- `Delta IK_M2` is not generally the normalized magnitude of `Delta Z`.
- Net displacement, path length, direction and ordinal second difference
  answer different questions.
- `derive_then_aggregate` and `aggregate_then_derive` must remain named.
- An aggregate window object is not a participant state or target event.
- A positive order gap is not automatically a semantic difference, conflict
  or coherence measure; a zero gap does not prove identical members.
- Complete typed Z, profile identities and provenance remain necessary for
  reconstruction.

## Scope and authority boundary

The reference package verifies declared synthetic mathematics and preserves
counterexamples. It does not choose universal weights, windows, thresholds,
alerts, corridors or visualizations. It does not validate a population or
domain, infer hidden state, authorize data collection or intervention, or
replace independent runtime and implementation-conformance testing.

The tagged release state, GitHub Release and DOI are separate publication
decisions. A moving Public-main package is not itself a new fixed citation
snapshot until those actions are separately authorized and completed.
