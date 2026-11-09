# Phase D — equal-axis families across interior and boundary shapes

Date: 2026-11-05

Basis: frozen Phase-0 reference profile. Its final Public basis record is
added after all reference blocks and source hashes are fixed.

Machine-readable cases:
[`phase_d_equal_axis_families.csv`](./phase_d_equal_axis_families.csv)

Reproducer:
[`calculate_phase_d_reference.py`](./calculate_phase_d_reference.py)

CSV SHA-256:

```text
a661090efbd4816ab53925f0587fdbbcee7634aa7f422558a10c5ae2ec12d492
```

## 1. Question

Does the equal-axis separation found at `IK_equal = 1/2` in Phase B persist at
other axial positions and across balanced, interior and coordinate-boundary
shapes?

Three families fix `IK_equal` at `1/5`, `2/5` and `4/5`. Each contains:

1. the balanced minimum-magnitude state;
2. a graduated interior or mixed interior/boundary state;
3. the maximally concentrated state permitted by `[0,1]^5`.

## 2. Verified result

| `IK_equal` | Shape | Complete `Z=(K,S,O,D,I)` | `IK_M2` | `AxisDev_eq` |
| ---: | --- | --- | ---: | ---: |
| `1/5` | balanced minimum | `(1/5,1/5,1/5,1/5,1/5)` | `1/5 = 0.200000000000` | `0` |
| `1/5` | graduated | `(2/5,3/10,1/5,1/10,0)` | `sqrt(6)/10 = 0.244948974278` | `sqrt(2)/10 = 0.141421356237` |
| `1/5` | boundary maximum | `(1,0,0,0,0)` | `sqrt(5)/5 = 0.447213595500` | `2/5 = 0.400000000000` |
| `2/5` | balanced minimum | `(2/5,2/5,2/5,2/5,2/5)` | `2/5 = 0.400000000000` | `0` |
| `2/5` | graduated | `(4/5,3/5,2/5,1/5,0)` | `sqrt(6)/5 = 0.489897948557` | `sqrt(2)/5 = 0.282842712475` |
| `2/5` | boundary maximum | `(1,1,0,0,0)` | `sqrt(10)/5 = 0.632455532034` | `sqrt(6)/5 = 0.489897948557` |
| `4/5` | balanced minimum | `(4/5,4/5,4/5,4/5,4/5)` | `4/5 = 0.800000000000` | `0` |
| `4/5` | graduated | `(3/5,7/10,4/5,9/10,1)` | `sqrt(66)/10 = 0.812403840464` | `sqrt(2)/10 = 0.141421356237` |
| `4/5` | boundary maximum | `(1,1,1,1,0)` | `2*sqrt(5)/5 = 0.894427191000` | `2/5 = 0.400000000000` |

For every family, both orders are strict:

```text
IK_M2:       balanced < graduated < boundary maximum
AxisDev_eq:  balanced < graduated < boundary maximum
```

## 3. General bounded result

For one fixed equal-axis mean `mu` in `[0,1]`, let:

```text
s = 5*mu
q = floor(s)
r = s-q
```

The minimum normalized L2 magnitude occurs at complete balance:

```text
Z_min = (mu,mu,mu,mu,mu)
IK_M2_min = mu
AxisDev_eq_min = 0
```

The maximum occurs at a permutation of `q` ones, then `r` if non-zero, then
zeros:

```text
Z_max = permutation(1,...,1,r,0,...,0)
IK_M2_max = sqrt((q+r^2)/5)
AxisDev_eq_max = sqrt(IK_M2_max^2-mu^2)
```

The maximum follows from convexity: with fixed sum, moving available mass
toward coordinate bounds increases the sum of squares. The minimum follows
from equal distribution of the fixed sum.

At the true axial endpoints, no shape interval remains:

```text
IK_equal = 0 -> Z = (0,0,0,0,0)
IK_equal = 1 -> Z = (1,1,1,1,1)
```

Because all coordinates are bounded and non-negative, no other complete Z can
have either endpoint mean. At every strict interior mean, multiple shapes and
magnitudes are possible.

## 4. Method and governance reading

Phase D generalizes Phase B: the hidden shape interval is not peculiar to the
chosen value `0.5`. Its width depends on axial position and collapses only at
the two domain endpoints.

This also prevents a misleading comparison of raw deviations across axis
positions. For example, a deviation of `0.4` is maximal at `IK_equal=0.2` and
`0.8`, while a larger maximum is possible at `IK_equal=0.4`. A future corridor
or alert must therefore declare its reference position/profile rather than
using one context-free deviation threshold.

Permutations of every maximum vector retain the same three scalar views while
changing operator identity. Full labelled Z and provenance remain mandatory.

## 5. Bounded Phase-D finding

At every strict interior equal-axis position, complete Z admits a bounded
interval from balanced minimum magnitude/deviation to maximally concentrated
magnitude/deviation. The interval and its maximum depend on axial position; it
disappears only at `IK_equal=0` and `1`. Consequently, `IK_M2` and
`AxisDev_eq` remain necessary shape views, but no context-free deviation
threshold is justified by this geometry alone.

## 6. Limits and next decision point

The result assumes complete comparable coordinates in `[0,1]`, the equal
profile and Euclidean geometry. It establishes neither cross-operator
commensurability nor empirical coherence, quality, error or intervention
thresholds.

No production implementation, learned axis, empirical corpus or external
numeric package was used. Phase E next examines equal-size perturbations around
balanced and concentrated states while retaining the complete signed
`Delta Z`; this changes the question from static shape to local sensitivity.

Compatibility note: the historical fixture labels `IK_equal` and
`AxisDev_eq` correspond to `IK_ref` and `AxisDev_ref` under the fixed
equal-coordinate reference geometry selected for v3.51. The generated labels
remain unchanged for exact reproducibility.
