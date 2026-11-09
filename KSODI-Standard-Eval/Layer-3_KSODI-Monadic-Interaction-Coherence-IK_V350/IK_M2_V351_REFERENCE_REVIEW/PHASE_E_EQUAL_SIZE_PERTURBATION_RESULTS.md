# Phase E — equal-size perturbations and start-state sensitivity

Date: 2026-11-05

Basis: frozen Phase-0 reference profile. Its final Public basis record is
added after all reference blocks and source hashes are fixed.

Machine-readable cases:
[`phase_e_equal_size_perturbations.csv`](./phase_e_equal_size_perturbations.csv)

Reproducer:
[`calculate_phase_e_reference.py`](./calculate_phase_e_reference.py)

CSV SHA-256:

```text
3f8d0d78ca8b2354ec13dc6bfd4693a4cb9638a1f8569f7223b4819758695946
```

## 1. Question and design

How do equally large complete signed perturbations behave around a balanced
and a concentrated state?

Starting states share `IK_equal=1/2`:

```text
BALANCED     = (1/2,1/2,1/2,1/2,1/2)
CONCENTRATED = (4/5,4/5,1/2,1/5,1/5)
```

Three perturbations each have the same raw Euclidean length:

```text
||Delta Z||_2 = 1/10
||Delta Z||_2/sqrt(5) = sqrt(5)/50 = 0.044721359550
```

They are:

```text
AXIAL_PLUS      = equal positive movement on all five coordinates
SPREAD_K_TO_I   = positive K and equally negative I movement
CONTRACT_K_TO_I = the exact signed reverse of SPREAD_K_TO_I
```

The names `SPREAD` and `CONTRACT` describe their relation to the chosen
concentrated start. Around the balanced start the two transfer directions are
symmetrical and both create deviation.

## 2. Verified result

| Start | Perturbation | `Delta IK_equal` | `Delta IK_M2` | `Delta AxisDev_eq` |
| --- | --- | ---: | ---: | ---: |
| balanced | axial plus | `+0.044721359550` | `+0.044721359550` | `0` |
| balanced | K/I transfer | `0` | `+0.001996015920` | `+0.044721359550` |
| balanced | reverse K/I transfer | `0` | `+0.001996015920` | `+0.044721359550` |
| concentrated | axial plus | `+0.044721359550` | `+0.039773869079` | `0` |
| concentrated | spreading K/I transfer | `0` | `+0.016476408722` | `+0.033285109564` |
| concentrated | contracting K/I transfer | `0` | `-0.013348067632` | `-0.029519787992` |

Every target remains inside `[0,1]^5`. Every row retains start Z, signed
`Delta Z`, target Z, profile and before/after metrics.

## 3. Exact sensitivity mechanism

For any complete transition under the frozen metric:

```text
IK_M2(Z + Delta Z)^2 - IK_M2(Z)^2
  = (2 * Z dot Delta Z + ||Delta Z||_2^2) / 5

Delta IK_equal
  = sum(Delta Z) / 5
```

Thus equal perturbation length does not imply equal magnitude response. The
inner product `Z dot Delta Z` retains how the signed direction meets the
starting state.

The two transfer perturbations have coordinate sum zero, so the fixed
equal-coordinate reference projection does not move. Around the balanced
state, their inner products are equal and they are scalar-symmetrical. Around
the concentrated state, one direction reinforces the existing K-to-I spread
while the reverse direction reduces it.

Even exact reverse steps need not produce equal and opposite changes in
`IK_M2` or `AxisDev_eq`, because norms are curved functions of state. The
complete signed transition remains necessary for reconstruction.

## 4. Consequences for observation and alerts

Phase E distinguishes at least four objects that must not be collapsed:

```text
starting state Z_t
signed movement Delta Z
movement size ||Delta Z||
resulting state Z_(t+1)
```

The same movement size can be axial, spreading or contracting. The same
`Delta IK_equal=0` can hide increasing or decreasing magnitude and deviation.
An alert based only on axis movement or unsigned movement size would therefore
lose the diagnosis-opening distinction.

A conforming diagnostic bundle needs the declared start and target identities,
signed complete `Delta Z`, axis/profile, movement of the applicable axial
projection, magnitude movement, axis-deviation movement and provenance. In
this fixture the applicable axial projection is `IK_ref`; no general
`Delta IK_w` claim is inferred for undeclared weighted profiles. No sign is
intrinsically good, bad, coherent or erroneous.

## 5. Bounded Phase-E finding

Equal-size monadic perturbations produce different `IK_M2` and
`AxisDev_eq` responses according to their signed direction and starting Z.
A zero axial change can accompany increased or decreased concentration.
Movement magnitude, signed `Delta Z`, start/target state and profile must
therefore remain distinct and reconstructible.

## 6. Boundary and next phase

These are paired monadic states, not yet a time series, pace measurement,
interaction relation or R-family result. Phase E establishes local
sensitivity only.

No production implementation, learned axis, empirical corpus or external
numeric package was used. Phase F next composes multiple comparable monadic
states into trajectories and compares net displacement, path length, direction
and compensating movement without entering Pace, Voice or R-family semantics.

Compatibility note: the historical fixture labels `IK_equal` and
`AxisDev_eq` correspond to `IK_ref` and `AxisDev_ref` under the fixed
equal-coordinate reference geometry selected for v3.51. The generated labels
remain unchanged for exact reproducibility.
