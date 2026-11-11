# Phase B — gap, movement and acceleration-component separation

Basis:

- [Phase 0 frozen basis](./PHASE_0_FROZEN_BASIS.md);
- [Phase-A primary result](./PHASE_A_PRIMARY_FORMULA_RESULTS.md).

## 1. Question

Do the three retained v3.50 components remain mathematically bounded and
distinguishable, or can one component or derivative order be interpreted as a
substitute for another?

```text
C_gap   = 1 - |IK_w,A - IK_w,B|
C_move  = 1 - |Delta IK_w,A - Delta IK_w,B| / 2
C_accel = 1 - |Delta2 IK_w,A - Delta2 IK_w,B| / 4
```

Phase B checks raw formula behavior. Component-local zero/epsilon status rules
are reserved for Phase C.

## 2. Reproducible artifacts

- [`calculate_phase_b_component_reference.py`](./calculate_phase_b_component_reference.py)
- [`phase_b_component_grids.csv`](./phase_b_component_grids.csv)
- [`phase_b_trajectory_collisions.csv`](./phase_b_trajectory_collisions.csv)

Reference execution:

```text
verified_component_grid_rows=75
gap_value_classes=5
move_value_classes=5
accel_value_classes=5
verified_trajectory_pairs=729
selected_collision_fixtures=4
```

SHA-256:

```text
phase_b_component_grids.csv
da04911088875d2d7fe3898420c301a5ded8406639ec7999b68802391ef95ea2

phase_b_trajectory_collisions.csv
1103a4c0c12ccebc15038d11a85b7ab853729eb5057f46b2c07b9c092ad9d430
```

The grids use five evenly spaced exact inputs over each component's complete
input interval. The five observed score classes are sample-grid classes, not a
claim that the continuous formulas admit only five values.

## 3. Range and endpoint check

| Component | Operand range | Maximum operand gap | Result range | Value 1 means |
| --- | --- | --- | --- | --- |
| `C_gap` | `IK_w in [0,1]` | `1` | `[0,1]` | equal current projected positions |
| `C_move` | `Delta IK_w in [-1,1]` | `2` | `[0,1]` | equal first projected differences |
| `C_accel` | `Delta2 IK_w in [-2,2]` | `4` | `[0,1]` | equal second projected differences |

For every component, exchanging A and B leaves the scalar unchanged. The
ordered dyad, operand direction and trajectory identities remain distinct.

## 4. Three-step trajectory check

All 729 ordered pairs of three-position trajectories over
`{0, 1/2, 1}` were evaluated exactly. Four retained fixtures demonstrate:

1. equal `C_gap` does not determine `C_move` or `C_accel`;
2. equal `C_move` does not determine `C_gap` or `C_accel`;
3. equal `C_accel` does not determine `C_gap` or `C_move`;
4. even the complete scalar triple `(C_gap,C_move,C_accel)` does not identify
   the underlying paired trajectories.

The movement- and acceleration-collision fixtures were selected so that their
fixed component remains numeric at `epsilon = 0`; joint-zero cases are not
used to obtain the Phase-B conclusion.

One especially compact collision is:

```text
A = B = (0,0,1/2)  -> (C_gap,C_move,C_accel) = (1,1,1)
A = B = (0,0,1)    -> (C_gap,C_move,C_accel) = (1,1,1)
```

The two dyadic trajectory pairs have different movement and acceleration
magnitudes, yet all three compatibility components equal one because each
component compares A with B at its own derivative order. The triple therefore
describes paired compatibility, not absolute activity, path identity or event
identity.

## 5. Bounded finding

The normalizations are mathematically consistent and each component answers a
different question:

```text
C_gap   -> compatibility of current projected position
C_move  -> compatibility of first projected movement
C_accel -> compatibility of change in projected movement
```

No component implies another. No component value, and not even the complete
three-component scalar tuple, reconstructs the paired trajectories. A
conforming result therefore retains the raw operands, derivative order,
source-local predecessors, ordered dyad, pairing map, profile and provenance.

High compatibility at one or all derivative orders is not evidence of low
activity, equal full `Delta Z`, agreement, target direction, coupling,
resonance or successful communication. Those require their own observable
basis and question-led diagnostic bundle.

## 6. Contract conclusions

- Position, movement and change of movement remain separate questions.
- The complete component tuple is a compatibility description, not a
  trajectory identity or activity measure.
- Raw operands and derivative-order identity remain beside every selected
  component.
- The 75 grid rows, 729 trajectory-pair enumeration and four retained
  collisions form the Phase-B reference basis.
