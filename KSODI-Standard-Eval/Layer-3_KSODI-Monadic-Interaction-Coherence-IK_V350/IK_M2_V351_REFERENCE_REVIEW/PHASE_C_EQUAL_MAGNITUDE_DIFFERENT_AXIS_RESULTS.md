# Phase C — equal magnitude, different axial position

Date: 2026-11-05

Basis: frozen Phase-0 reference profile. Its final Public basis record is
added after all reference blocks and source hashes are fixed.

Machine-readable cases:
[`phase_c_equal_magnitude_different_axis.csv`](./phase_c_equal_magnitude_different_axis.csv)

Reproducer:
[`calculate_phase_c_reference.py`](./calculate_phase_c_reference.py)

CSV SHA-256:

```text
dba16da9ea2a125e1f8d79eaeaea9d88f25e41b9a61655ee83d4167fc0aa556a
```

## 1. Question

Can complete continuous Z states have the same normalized L2 magnitude while
occupying different positions on the declared equal axis?

Two exact pairs test the question. The first contrasts a balanced state with a
concentrated state. The second contrasts two unequal states with the same
Euclidean magnitude but different coordinate sums.

## 2. Exact result

| Pair | Case | Complete `Z=(K,S,O,D,I)` | `IK_equal` | `IK_M2` | `AxisDev_eq` |
| --- | --- | --- | ---: | ---: | ---: |
| 1 | C01 | `(1/2,1/2,1/2,1/2,1/2)` | `1/2 = 0.5` | `1/2 = 0.5` | `0` |
| 1 | C02 | `(1,1/2,0,0,0)` | `3/10 = 0.3` | `1/2 = 0.5` | `2/5 = 0.4` |
| 2 | C03 | `(1,0,0,0,0)` | `1/5 = 0.2` | `sqrt(5)/5 = 0.447213595500` | `2/5 = 0.4` |
| 2 | C04 | `(4/5,3/5,0,0,0)` | `7/25 = 0.28` | `sqrt(5)/5 = 0.447213595500` | `2*sqrt(19)/25 = 0.348711915483` |

Both pairs pass:

```text
IK_M2(first state) = IK_M2(second state)
IK_equal(first state) != IK_equal(second state)
```

The complete vectors and their equal-axis deviations also differ.

## 3. Geometric reading

Under the frozen equal profile:

```text
IK_M2^2 = IK_equal^2 + AxisDev_eq^2
```

At fixed `IK_M2`, more axial position necessarily leaves less perpendicular
deviation, and less axial position leaves more. Pair 1 makes the contrast
maximally legible: the balanced state places its entire magnitude on the equal
axis, while the concentrated state has the same total magnitude split between
smaller axial position and larger deviation.

Pair 2 shows that this is not only a balanced-versus-unbalanced endpoint
effect. Two unequal states can also share magnitude while dividing it
differently between axial position and deviation.

## 4. Consequence for joint IK evaluation

Phase C establishes the reverse non-substitution result:

- `IK_M2` cannot replace the declared axial projection, because equal
  magnitude does not determine axial position;
- Phase B already showed that the fixed-reference axial projection cannot
  replace `IK_M2`, because equal axial position does not determine magnitude;
- `AxisDev_eq` makes their geometric difference readable;
- complete labelled Z is still required to identify the contributing
  operators, evidence and provenance.

In this fixture, `IK_equal` is the v3.51 fixed-reference projection
`IK_ref`; it is not a general result about every possible weighted
`IK_w` profile. The three displayed measurements are complementary views,
but under the
fixed equal-axis Euclidean contract they are not three independent scalar
information sources. Any two of `IK_equal`, `IK_M2` and `AxisDev_eq` determine
the third when their applicability conditions hold. This dependency should be
visible in implementation and governance documentation rather than presented
as three independent confirmations.

## 5. Bounded Phase-C finding

Equal normalized L2 magnitude does not imply equal position on the declared
axis. `IK_M2` therefore cannot replace the applicable axial projection; it
must be interpreted jointly with axial position, deviation and complete
labelled Z. Under the equal-axis Euclidean contract, the three scalars form one
reconstructible geometric bundle rather than three independent evidence
streams.

## 6. Limits and reopening

The result is mathematical and synthetic. It does not establish coherence,
quality, error, truth or real communication meaning. It may be reopened if the
profile, axis, metric, normalization, coordinate domain or typed-Z eligibility
changes.

No production implementation, learned axis, empirical corpus or external
numeric package was used. Phase D adds several equal-axis/different-magnitude
cases across boundary and interior positions rather than relying on the single
fixed mean used in Phase B.

Compatibility note: the historical fixture labels `IK_equal` and
`AxisDev_eq` correspond to `IK_ref` and `AxisDev_ref` under the fixed
equal-coordinate reference geometry selected for v3.51. The generated labels
remain unchanged for exact reproducibility.
