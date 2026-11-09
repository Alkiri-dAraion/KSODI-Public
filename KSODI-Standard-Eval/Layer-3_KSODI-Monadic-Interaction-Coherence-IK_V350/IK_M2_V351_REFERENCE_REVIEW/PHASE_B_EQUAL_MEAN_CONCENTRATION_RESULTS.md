# Phase B — equal axial position, different concentration

Date: 2026-11-05

Basis: frozen Phase-0 reference profile. Its final Public basis record is
added after all reference blocks and source hashes are fixed.

Machine-readable cases:
[`phase_b_equal_mean_concentration.csv`](./phase_b_equal_mean_concentration.csv)

Reproducer:
[`calculate_phase_b_reference.py`](./calculate_phase_b_reference.py)

CSV SHA-256:

```text
6435ca85f5011c776ef41575ed8778d30998b57ffcfb66cbb9fef565be902f60
```

## 1. Question

Can complete continuous Z states have the same equal-axis position while
their normalized L2 magnitude and equal-axis deviation distinguish balanced
from increasingly uneven coordinate patterns?

All four cases are complete typed synthetic Z states. They have the same
coordinate sum `5/2` and therefore the same:

```text
IK_equal = M_1 = 1/2
```

## 2. Exact result

| Case | Complete `Z=(K,S,O,D,I)` | Reading | `IK_equal` | `IK_M2` | `AxisDev_eq` |
| --- | --- | --- | ---: | ---: | ---: |
| B01 | `(1/2,1/2,1/2,1/2,1/2)` | balanced | `1/2` | `1/2 = 0.500000000000` | `0` |
| B02 | `(7/10,3/5,1/2,2/5,3/10)` | graduated interior | `1/2` | `3*sqrt(3)/10 = 0.519615242271` | `sqrt(2)/10 = 0.141421356237` |
| B03 | `(1,1,1/2,0,0)` | bounded maximum, K/S side | `1/2` | `3*sqrt(5)/10 = 0.670820393250` | `sqrt(5)/5 = 0.447213595500` |
| B04 | `(0,0,1/2,1,1)` | coordinate permutation, D/I side | `1/2` | `3*sqrt(5)/10 = 0.670820393250` | `sqrt(5)/5 = 0.447213595500` |

The reference calculator verified the strict orders:

```text
IK_M2(B01) < IK_M2(B02) < IK_M2(B03)
AxisDev_eq(B01) < AxisDev_eq(B02) < AxisDev_eq(B03)
```

B03 and B04 deliberately have identical scalars but different labelled Z.

## 3. Why these cases bound the question at `IK_equal = 1/2`

At a fixed arithmetic mean, the equal vector minimizes the sum of squares and
therefore normalized L2 magnitude. This follows from the mean-square identity
or, equivalently, from Cauchy/Jensen. B01 is consequently the bounded minimum.

Inside `[0,1]^5`, a fixed sum of `5/2` maximizes the sum of squares by moving
mass toward the permitted boundaries. At an extremum, no two coordinates can
both remain strictly fractional: shifting a small amount from the lower to the
higher one increases the sum of squares while preserving the sum. The bounded
maximum is therefore any permutation of:

```text
(1,1,1/2,0,0)
```

B03 and B04 are two such permutations. Thus these examples do not merely show
an arbitrary difference; they bracket the full balanced-to-maximally-
concentrated range for this fixed equal-axis position.

## 4. What `IK_M2` and `AxisDev_eq` add

Phase B supplies the distinction that Raster A structurally could not:

- `IK_equal` alone maps all four states to the same axial position;
- `IK_M2` distinguishes the balanced, moderately uneven and maximally uneven
  patterns;
- `AxisDev_eq` isolates the off-axis/dispersion component of that difference;
- complete labelled Z identifies which operator coordinates create it.

Under the equal profile:

```text
IK_M2^2 = IK_equal^2 + AxisDev_eq^2
```

Therefore, once `IK_equal` is known, `IK_M2` and `AxisDev_eq` determine one
another mathematically. They are different governance views of the same
equal-axis geometry, not three independent pieces of scalar evidence.
`IK_M2` expresses total normalized magnitude; `AxisDev_eq` expresses only the
component not explained by the equal axial position.

## 5. What the bundle still loses

B03 and B04 show that even the bundle
`(IK_equal, IK_M2, AxisDev_eq)` cannot distinguish a K/S-heavy state from a
D/I-heavy state when their coordinate values are permutations. It also does
not preserve ordering, operator evidence, uncertainty, typed-status reasons
or provenance.

This directly supports the v3.51 joint IK evaluation structure:

```text
complete typed Z
├── IK_w
├── IK_M2
├── IK_ref
├── AxisDev_ref
└── complete provenance and profiles
```

The scalars are navigable projections of Z; they are not replacement truths.

Compatibility note: the historical fixture labels `IK_equal` and
`AxisDev_eq` correspond to `IK_ref` and `AxisDev_ref` under the fixed
equal-coordinate reference geometry selected for v3.51. The generated labels
remain unchanged for exact reproducibility.

## 6. Bounded Phase-B finding

At the same equal-axis position `IK_equal = 1/2`, normalized L2 magnitude and
equal-axis deviation distinguish balanced, moderately uneven and maximally
concentrated continuous Z states. The scalar bundle still collapses coordinate
permutations, so complete labelled Z and provenance remain necessary. The
calculation establishes a geometric distinction; it does not establish
coherence, quality, error or empirical communication meaning.

## 7. Reopening condition and next phase

Phase B may be reopened if the equal profile, Euclidean metric, normalization,
coordinate domain or typed-Z eligibility changes. The calculation uses
synthetic complete states and is independent of a production runtime, learned
axis or empirical corpus.

Phase C reverses the comparison: equal `IK_M2`, different `IK_equal`.
