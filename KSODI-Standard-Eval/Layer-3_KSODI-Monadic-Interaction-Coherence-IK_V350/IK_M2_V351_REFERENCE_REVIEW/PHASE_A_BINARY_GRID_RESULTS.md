# Phase A — complete binary Z grid

Date: 2026-11-05

Basis: frozen Phase-0 reference profile. Its final Public basis record is
added after all reference blocks and source hashes are fixed.

Machine-readable grid:
[`phase_a_binary_grid.csv`](./phase_a_binary_grid.csv)

Reproducer:
[`calculate_phase_a_reference.py`](./calculate_phase_a_reference.py)

CSV SHA-256:

```text
61c2a752d90c8d309483b78c8417fa7f665d106366c8d9798631b87bcf0bc10e
```

## 1. What was calculated

All 32 coordinate-labelled vertices of `{0,1}^5` were enumerated in fixed
`(K,S,O,D,I)` order. Every output row retains complete Z and calculates:

```text
IK_equal  = arithmetic mean of the five coordinates
M_1       = normalized L1 magnitude
IK_M2     = root mean square of the five coordinates
AxisDev_eq = population standard deviation across the five coordinates
```

For this non-negative equal-weight case:

```text
M_1 = IK_equal
IK_M2^2 = IK_equal^2 + AxisDev_eq^2
```

The second identity is the familiar root-mean-square decomposition into
mean position and dispersion. It is exact here; it is not a claim that five
different operators are empirically interchangeable measuring scales.

## 2. Verified group result

Let `h` be the number of coordinates equal to one.

| h | Complete-Z states | `IK_equal = M_1` | `IK_M2` | `AxisDev_eq` |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 1 | `0` | `0` | `0` |
| 1 | 5 | `1/5 = 0.2` | `sqrt(1/5) = 0.447213595500` | `2/5 = 0.4` |
| 2 | 10 | `2/5 = 0.4` | `sqrt(2/5) = 0.632455532034` | `sqrt(6)/5 = 0.489897948557` |
| 3 | 10 | `3/5 = 0.6` | `sqrt(3/5) = 0.774596669241` | `sqrt(6)/5 = 0.489897948557` |
| 4 | 5 | `4/5 = 0.8` | `sqrt(4/5) = 0.894427191000` | `2/5 = 0.4` |
| 5 | 1 | `1` | `1` | `0` |

Assertions passed with absolute tolerance `1e-12`:

- exactly 32 ordered states;
- class counts `1,5,10,10,5,1`;
- independent direct and identity calculations of `AxisDev_eq` agree;
- every derived value remains inside its proven Phase-A range;
- a second complete run produced the same CSV hash.

## 3. Distinctions retained and collapsed

The 32 complete vectors become only six scalar classes under `IK_equal`.
They also become only six classes under `IK_M2`, and only six under the pair
`(IK_equal, IK_M2)`. In this binary-only grid:

```text
IK_M2 = sqrt(IK_equal)
```

Therefore `IK_M2` adds no new class distinction in Raster A. It must not be
rejected on that basis: binary vertices force squared coordinates to equal
their original values. Phases B–D are specifically needed to expose the
continuous-state concentration difference.

Coordinate identity is completely lost inside each Hamming class. For
example, `A02 = (0,0,0,0,1)` and `A17 = (1,0,0,0,0)` receive identical
`IK_equal`, `IK_M2` and `AxisDev_eq`, although the active operator is different.
Only complete labelled Z preserves that distinction.

`AxisDev_eq` alone produces only three classes:

```text
h = 0 or 5 -> 0
h = 1 or 4 -> 0.4
h = 2 or 3 -> sqrt(6)/5
```

It describes spread around the equal axis but cannot identify the axial
position or which coordinates create that spread. Under this profile it can
be reconstructed from the pair `(IK_equal, IK_M2)`; it remains valuable as a
human-readable geometric view, not as a replacement for either scalar or Z.

Compatibility note: the historical fixture labels `IK_equal` and
`AxisDev_eq` correspond to `IK_ref` and `AxisDev_ref` under the fixed
equal-coordinate reference geometry selected for v3.51. They remain unchanged
in the generated artifacts so that the original calculation stays exactly
reproducible.

## 4. Governance-readable interpretation

For a governance-readable view, Raster A says:

- `IK_equal` answers where the state lies on the declared equal axis;
- `IK_M2` answers how large the complete state is under normalized Euclidean
  magnitude;
- `AxisDev_eq` answers how unevenly the five coordinate values are arranged
  around their common mean;
- none of the three tells us whether K, S, O, D or I produced the pattern;
- the same displayed line value can therefore still have several materially
  different complete-Z origins.

For every non-constant binary vector, `IK_M2` is strictly greater than
`IK_equal`. Equality occurs only at `(0,0,0,0,0)` and `(1,1,1,1,1)`, where all
five coordinates are equal and axis deviation is zero. A larger deviation is
not automatically an error or incoherence; it is a diagnosis-opening marker
of unequal coordinate values under the declared representation.

## 5. Bounded Phase-A finding

Complete binary Z contains 32 labelled states, while `IK_equal`, `IK_M2`, and
their pair each retain only six Hamming-weight classes. `AxisDev_eq` retains
only three. Raster A therefore confirms the need to preserve complete labelled
Z and reverse provenance. It does not yet demonstrate the incremental
distinguishing value of `IK_M2` over `IK_equal`; exact continuous
counterexamples in B–D are needed for that question.

## 6. Reopening condition and next phase

Phase A may be reopened if the coordinate order, typed-Z eligibility, equal
profile, normalization, metric or numeric rules change. The calculation uses
only synthetic complete states and the declared formulas; it is independent
of a production runtime, learned axis or empirical corpus.

Phase B constructs continuous states with equal `IK_equal` but different
`IK_M2` and `AxisDev_eq` to test the distinction that the binary grid cannot
expose.
