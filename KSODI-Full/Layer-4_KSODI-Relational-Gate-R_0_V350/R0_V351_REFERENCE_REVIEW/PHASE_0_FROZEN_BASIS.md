# R₀ v3.51 reference review — Phase 0 frozen basis

Date: `2026-11-10`

## Purpose

This file binds the first Layer-4 v3.51 reference calculation to the exact
method, companion and upstream monadic sources used to construct it. It does not make the method universal, empirically calibrated or independent of its declared profile.

## Governed source identities

| Source | SHA-256 |
| --- | --- |
| `KSODI_State-Vector-Z_V351.md` | `f3ad6674ad8c5a97c3b49f30ee44f9b8b0eb87ce50cdccdc011d0f057d71c846` |
| `KSODI_Monadic-Interaction-Coherence-IK_V351.md` | `517219d50ac00ddf41836c94af2a66d2d78df4bff250f268a6a82eef5e613d7e` |
| `KSODI_Relational-Gate-R_0_V351.md` | `6a67e7d27396aa12a6dce7fcef7f27b0bafebc93b015d4535019f79dd7ba5715` |
| `KSODI_Relational-Gate-R_0_Implementation-Companion_V351.md` | `c5bb0d8ed9ce2e12904635950d403e509e4c50fc26a7c14043c7e9eaaffa5a6d` |

Any byte change to these sources reopens this basis and requires a complete
generator rerun plus renewed interpretation review.

## Formula basis

```text
canonical complete equal-coordinate normalized L1 drift:
d_E = (1/5) sum_X |Delta X_E|

canonical dyadic arithmetic-mean gate:
R0_raw = 1 - (d_A + d_B)/2
R0 = clip(R0_raw, 0, 1)

gate_state = open   if numeric R0 >= theta_R0_gate_open_min
gate_state = closed if numeric R0 < theta_R0_gate_open_min
gate_state = not_evaluable if result is non-numeric

aggregate_drift_max = 1 - theta_R0_gate_open_min
```

The suite also calculates the separately identified equal-coordinate L2 norm
and one fixed reduced-M comparison. It does not calculate alternative
coordinate weights `g`, learned metrics, n-adic gates, empirical calibration
or IK_rel.

## Fixture parameter boundary

The `theta_R0_gate_open_min` values `0.8` and `0.5` are transparent synthetic
fixture parameters. Their equivalent `aggregate_drift_max` values are `0.2`
and `0.5`. These values are recorded
with `threshold_calibration_status=set_not_empirically_calibrated`. They are
not recommended defaults and establish no empirical corridor.

## Completion boundary

Phase 0 is complete only for the bounded numeric/status fixture set in this
directory. Layer-4 method acceptance, Public selection, runtime conformance,
the joint later R₀/IK_rel sensitivity package and release verification remain
open.
