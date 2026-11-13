# R₀ v3.51 reference review — Phase 0 frozen basis

- Initial freeze: `2026-11-10`
- Evidence-object guard reconciliation: `2026-11-12` (no formula change)

## Purpose

This file binds the first Layer-4 v3.51 reference calculation to the exact
method, companion and upstream monadic sources used to construct it. It does not make the method universal, empirically calibrated or independent of its declared profile.

## Governed source identities

| Source | SHA-256 |
| --- | --- |
| `KSODI_State-Vector-Z_V351.md` | `bee6b5b63f6557a6cedbea885c8c7e9308170a7daebba156958ced7657c19887` |
| `KSODI_Monadic-Interaction-Coherence-IK_V351.md` | `5e9e5c640b493c747988fdf130182efba727091d78e8e17db4084e9edd8fc8f4` |
| `KSODI_Relational-Gate-R_0_V351.md` | `e7ee08362506a2098debbe74d191d01f0d8ad4975c3004df7c703f54143bb614` |
| `KSODI_Relational-Gate-R_0_Implementation-Companion_V351.md` | `f2f263e507fadaeb9e3e59e2798335d609862cf2948483b7960a3c158f010425` |

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
