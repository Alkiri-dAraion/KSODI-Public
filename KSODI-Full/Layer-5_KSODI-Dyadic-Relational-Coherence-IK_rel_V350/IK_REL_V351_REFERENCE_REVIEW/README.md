# `IK_rel` v3.51 public reference package

## Purpose

This package makes the retained `IK_rel` formula and the v3.51 identity,
epsilon, status, component and window contracts independently reproducible.
It does not use an implementation runtime as method authority.

## Reading and reproduction order

```text
Phase 0 frozen basis
-> A primary formula and collisions
-> B component separation
-> C epsilon and derivative order
-> D exact R_0 handoff
-> D+ complete-Z gate exclusion
-> E fixed component profiles
-> F windows, coverage, overlap and dynamics
```

Run from this directory with Python 3:

```text
python3 calculate_phase_a_primary_reference.py
python3 calculate_phase_b_component_reference.py
python3 calculate_phase_c_epsilon_reference.py
python3 calculate_phase_d_r0_handoff_reference.py
python3 calculate_phase_d_plus_gate_exclusion_reference.py
python3 calculate_phase_e_fixed_n_reference.py
python3 calculate_phase_f_window_reference.py
```

The generators use only the Python standard library and assertion-check their
outputs. Successful generation does not validate a production threshold,
epsilon, semantic interpretation or third-party runtime.

## Checked inventory

| Phase | Assertion-checked scope |
| --- | --- |
| A | 25 primary grid rows; six open-gate projection collisions |
| B | 75 component rows; 729 trajectory pairs; four selected collisions |
| C | 22 epsilon-boundary rows; two derivative-order cases |
| D | 25 projected-feasibility rows; 25 handoff-precedence rows |
| D+ | five complete-Z cases; two closed and three open gates |
| E | seven nonempty sets; 45 status rows; nine invalid profiles |
| F | five window scenarios; five overlap windows; six dynamic steps |

## Interpretation guards

- Phase-D projected feasibility is not the actual Layer-4 handoff.
- Fixture thresholds and positive epsilon bands are test controls, not
  production recommendations.
- A high projected value can collide with different complete trajectories.
- A closed gate preserves `R_0`, monadic trajectories and exclusion evidence;
  it does not emit current primary `IK_rel`.
- `C_gap`, `C_move` and `C_accel` answer separate questions.
- Window means depend on exact membership, partitions and coverage.
- The package is reference evidence, not runtime-conformance evidence.

## Integrity

[`IK_REL_V351_REFERENCE_SHA256SUMS.txt`](./IK_REL_V351_REFERENCE_SHA256SUMS.txt)
binds the published Layer-5 method, implementation companion and this complete
reference package. Regenerate every fixture before comparing the manifest.
