# Phase F — monadic trajectories, path and second difference

Date: 2026-11-05

Basis: frozen Phase-0 reference profile. Its final Public basis record is
added after all reference blocks and source hashes are fixed.

Machine-readable positions:
[`phase_f_trajectory_positions.csv`](./phase_f_trajectory_positions.csv)

Machine-readable summaries:
[`phase_f_trajectory_summaries.csv`](./phase_f_trajectory_summaries.csv)

Reproducer:
[`calculate_phase_f_reference.py`](./calculate_phase_f_reference.py)

CSV SHA-256:

```text
positions: 53d6fb49991777396112edee69391d00b836e40058e9fec1b751dc957e4164d0
summaries: 8dd41bcea97c9a072d5aa7fa70358488c480eedaa8fef62c30ca269168809285
```

## 1. Question and design

What is lost if a monadic development is represented only by its current
axis value, its start/end difference or its scalar history?

Five three-position sequences were calculated:

1. stationary balanced baseline;
2. balanced K/I excursion and return;
3. balanced S/O excursion and return with the same scalar history as 2;
4. direct contraction from one concentrated start to a less concentrated end;
5. a detour between the exact same start and end as 4.

All 15 positions retain:

```text
IK_equal = 1/2
```

The step indices describe order only. No elapsed time, sampling interval,
pace, rhythm or physical acceleration is assumed.

## 2. Summary result

| Trajectory | Net displacement | Path length | `\|\|Δ²Z\|\|_2` | Scalar/path reading |
| --- | ---: | ---: | ---: | --- |
| stationary | `0` | `0` | `0` | no movement |
| K/I out-and-back | `0` | `0.565685424949` | `0.565685424949` | non-zero excursion, zero net |
| S/O out-and-back | `0` | `0.565685424949` | `0.565685424949` | same scalar history, different operators |
| direct contraction | `0.141421356237` | `0.141421356237` | `0` | straight equal steps |
| detour, same endpoints | `0.141421356237` | `0.282842712475` | `0.244948974278` | longer path and direction change |

Raw Euclidean lengths are shown. The machine-readable summary also retains
their normalized-by-`sqrt(5)` counterparts.

## 3. Net displacement does not preserve path

The stationary and both out-and-back trajectories share:

```text
start Z = end Z
net ΔZ = 0
net ΔIK_equal = 0
net ΔIK_M2 = 0
net ΔAxisDev_eq = 0
```

Yet the out-and-back paths have non-zero length and non-zero intermediate
magnitude/deviation. An endpoint-only comparison would make actual movement
indistinguishable from stillness.

Similarly, the direct and detour trajectories share the exact start, exact
end, net `ΔZ` and all net scalar changes. The direct path length equals
its net displacement. The detour path is twice as long and has non-zero second
difference.

## 4. Scalar history does not preserve operator path

The K/I and S/O out-and-back trajectories have identical histories for:

```text
IK_equal
IK_M2
AxisDev_eq
step magnitude
path length
net displacement
||Δ²Z||
```

Their complete Z and signed coordinate movements differ. Even the three-view
scalar history plus unsigned movement diagnostics cannot identify which
operators moved. Full labelled states and directed `ΔZ` remain required.

## 5. Meaning and limit of `Δ²Z`

For the three ordinal positions `Z_0, Z_1, Z_2`, this review defines:

```text
ΔZ_01 = Z_1 - Z_0
ΔZ_12 = Z_2 - Z_1
Δ²Z_1 = ΔZ_12 - ΔZ_01
      = Z_2 - 2*Z_1 + Z_0
```

`Δ²Z=0` means the two index steps have identical vector change. A
non-zero value marks a change of direction and/or step vector. Without a time
contract it is an ordinal second difference, not acceleration or Pace.

Its norm alone still loses direction and coordinate identity. The complete
signed `Δ²Z` must remain available wherever the question requires
reconstruction.

## 6. Different intermediate stories at identical endpoints

The direct contraction decreases `IK_M2` and `AxisDev_eq` monotonically. The
detour first increases both, then ends at the same lower values as the direct
path. Endpoint equality therefore does not establish process equality,
monotonicity or absence of an intermediate excursion.

This is the first A–F result that directly motivates a Hangar trajectory view:
the view must be able to navigate from aggregate path/net summaries back to
the ordered complete states and signed transitions.

## 7. Bounded Phase-F finding

Equal start/end states or equal net changes do not imply equal paths.
Identical scalar histories can still hide different operator-coordinate
trajectories. Preserve ordered complete Z, signed `ΔZ`, path length, net
displacement and, where the question needs direction-change information,
signed `Δ²Z`. An ordinal second difference does not become Pace,
acceleration, relation or R-family evidence without their separate contracts.

## 8. Reopening and next decision point

This result assumes comparable ordered states, fixed coordinate identity,
fixed profile and equal step semantics only as ordinal positions. A later time
contract must distinguish irregular sampling, duration, pace and linguistic
rhythm rather than retroactively reading them into this fixture.

No production implementation, learned axis, empirical corpus or external
numeric package was used. A–F are calculated under the equal-coordinate
reference profile. The next mathematical branch tests stable non-equal axes
and their deviation geometry.

Compatibility note: the historical fixture labels `IK_equal` and
`AxisDev_eq` correspond to `IK_ref` and `AxisDev_ref` under the fixed
equal-coordinate reference geometry selected for v3.51. The generated labels
remain unchanged for exact reproducibility.
