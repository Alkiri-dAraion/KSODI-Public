# KSODI-Full v3.51 — Phase-H Sensitivity Review

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
files deterministically with LF line endings and asserts its declared boundary
expectations and status vocabulary. A green run confirms that the generated
rows match those declared expectations. It does not independently reconcile
the fixtures against the method files, prove the absence of a contract
contradiction, or validate an empirical threshold, epsilon, semantic
interpretation or production implementation.

## Fixture vocabulary mapping

Some retained fixture labels predate the fully typed v3.51 result vocabulary.
They are searchable test shorthand, not additional method statuses:

| Fixture label | Method status | Typed interpretation |
| --- | --- | --- |
| `numeric` | `numeric` | value is present |
| `not_applicable_joint_projected_zero` | `not_applicable` | exact joint projected zero under the declared exact-zero policy |
| `not_applicable_joint_move_epsilon_band` | `not_applicable` | interpret through `epsilon_kind`: numeric-policy zero/band or question-relevance band |
| `not_observable` | `not_observable` | required projected movement unresolved at observation resolution |
| `not_applicable` | `not_applicable` | for example `gate_not_open` in the present primary branch |
| `processing_error` | processing state | invalid or incomplete processing record; not a method result |

The generator checks every emitted IK_rel fixture status against this mapping.
Full vocabulary harmonization, if desired, remains a later migration task; the
published fixture history is not silently rewritten.

## Reader and machine guards

- Canonical equal-coordinate normalized L1 remains distinct from all named
  test controls.
- L2, coordinate-weight vector `g` and alternative `IK_w` weights are never
  promoted by appearing in a test row.
- `max_abs_coordinate_delta_E` never replaces the complete signed `Delta Z_E`.
- A scalar projection collision is an observable information loss, not proof
  that the formula is incorrect.
- Positive epsilon fixtures identify their origin and calibration status.
- The review vocabulary reserves `contract_contradiction` for an independent
  method-to-fixture reconciliation. The self-expecting generator emits and
  checks the other finding classes but does not claim that the reserved class
  has been independently excluded.

Presence on Public `main` makes this package inspectable reference evidence;
it does not by itself create a tagged release, runtime-conformance result or
v3.52 record-schema decision. Those remain separately governed.
