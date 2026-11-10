# KSODI-Full v3.51 — Phase-H Sensitivity Review

Status: `PUBLIC_V351_SYNTHETIC_REFERENCE_REVIEW /
REPRODUCIBLE_SYNTHETIC_EVIDENCE / NO_NEW_METHOD_PROFILE`

Phase H tests how the frozen v3.51 `R_0` and `IK_rel` contracts respond to
declared metric, weighting and epsilon choices. It is a protection and
diagnostic package, not a new method profile, empirical calibration study or
runtime-conformance claim.

## Reading order

1. [Public review and collaboration questions](PHASE_H_SENSITIVITY_AND_PROJECTION_LOSS_PUBLIC_REVIEW_V351.md)
2. [Frozen basis](PHASE_0_FROZEN_BASIS.md)
3. [Detailed sensitivity results](PHASE_H_SENSITIVITY_RESULTS.md)
4. [Generator](calculate_phase_h_reference.py)
5. the five exact CSV fixture families
6. [SHA-256 manifest](PHASE_H_SHA256SUMS.txt)

## Five blocks

| Block | Question | Fixture |
| --- | --- | --- |
| H-A | How do declared R₀ norm and coordinate-metric profiles affect drift, value and gate state? | `phase_h_r0_profile_sensitivity.csv` |
| H-B | What does the optional coordinate-extreme diagnostic retain or compress, including ties? | `phase_h_coordinate_extrema.csv` |
| H-C | Which distinct complete movements collide under the scalar `IK_w`/`C_move` projection? | `phase_h_ikrel_projection_collisions.csv` |
| H-D | How do epsilon boundaries and calibration-provenance requirements affect status? | `phase_h_epsilon_profiles.csv` |
| H-E | Does the complete R₀ → IK_rel route preserve identity, gate and profile effects? | `phase_h_joint_pipeline.csv` |

## Reproduce

From this directory:

```bash
python3 calculate_phase_h_reference.py
shasum -a 256 -c PHASE_H_SHA256SUMS.txt
```

The generator uses only the Python standard library. It rewrites the five CSV
files deterministically with LF line endings and asserts the expected boundary
relations. A green run confirms these fixtures against the bound formulas; it
does not validate an empirical threshold, epsilon, semantic interpretation or
production implementation.

## Reader and machine guards

- Canonical equal-coordinate normalized L1 remains distinct from all named
  test controls.
- L2, coordinate-weight vector `g` and alternative `IK_w` weights are never
  promoted by appearing in a test row.
- `max_abs_coordinate_delta_E` never replaces the complete signed `Delta Z_E`.
- A scalar projection collision is an observable information loss, not proof
  that the formula is incorrect.
- Positive epsilon fixtures identify their origin and calibration status.
- The four finding classes remain distinguishable even when one class has
  zero observed rows.

Presence on Public `main` makes this package inspectable reference evidence;
it does not by itself create a tagged release, runtime-conformance result or
v3.52 record-schema decision. Those remain separately governed.
