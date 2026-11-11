# Phase C — zero, epsilon and derivative-order status boundaries

Basis:

- [Phase 0 frozen basis](./PHASE_0_FROZEN_BASIS.md);
- [Phase-B component separation](./PHASE_B_COMPONENT_SEPARATION_RESULTS.md).

## 1. Question and test-only policies

The retained v3.50 rules are:

```text
both |Delta IK_w| <= epsilon_move   -> C_move not_applicable
both |Delta2 IK_w| <= epsilon_accel -> C_accel not_applicable
```

Phase C tests exact zero, both signs, exact boundaries, just-below/above
values, one-sided zero and derivative-order separation. It uses transparent
test-only values:

```text
epsilon_move  = 1/10
epsilon_accel = 1/5
probe step    = 1/100
```

These are fixtures, not selected v3.51 defaults or empirical thresholds.
Each fixture now carries its distinct policy ID, parameter origin
`synthetic_reference_fixture` and explicit calibration status
`set_not_empirically_calibrated`. Formula correctness never upgrades that
status.

## 2. Reproducible artifacts

- [`calculate_phase_c_epsilon_reference.py`](./calculate_phase_c_epsilon_reference.py)
- [`phase_c_epsilon_boundaries.csv`](./phase_c_epsilon_boundaries.csv)
- [`phase_c_derivative_order_statuses.csv`](./phase_c_derivative_order_statuses.csv)

Reference execution:

```text
verified_boundary_rows=22
numeric_boundary_rows=8
not_applicable_boundary_rows=14
verified_derivative_order_cases=2
```

SHA-256:

```text
phase_c_epsilon_boundaries.csv
aa396f0a58b5638a6df7cc21c05293f6e1f751126c623b5b599db2783f621908

phase_c_derivative_order_statuses.csv
79167ce0f65cc3b054fe26acebe9e6f1d7b307c342dfe5da41f6c0c6e0e4c7ac
```

## 3. Boundary findings

The comparison operator is inclusive. At exactly `|x| = epsilon`, the input
remains inside the band. Two equal inputs therefore move from a nonnumeric
status at the boundary to numeric value `1` immediately above it:

```text
(epsilon, epsilon)             -> not_applicable
(epsilon + delta, epsilon + delta) -> numeric, value 1
```

This is a typed eligibility transition, not a numerical jump between two
numeric results. A plot must show the status boundary rather than drawing a
continuous numeric line through it.

"One-sided zero remains numeric" is only conditionally true:

```text
(0, value within epsilon)  -> both inputs inside band -> not_applicable
(0, value outside epsilon) -> only one input inside   -> numeric
```

The policy also suppresses opposite signed inputs when both magnitudes remain
inside the band. With the test-only movement epsilon:

```text
(-1/10, +1/10) -> raw C_move = 9/10 -> method status not_applicable
(-11/100, +11/100) -> raw C_move = 89/100 -> method status numeric
```

The raw formula remains mathematically defined in both cases, but the current
method elects not to emit a numeric component inside the joint band.

## 4. Fehlerteufel: zero/stillness labels overclaim for positive epsilon

For `epsilon > 0`, the rule does not establish exact zero, stillness or absence
of full-vector movement. It establishes only that both projected operands fall
inside the declared tolerance band. Current implementation vocabulary such as
`static_step`, `joint_zero_movement` or `joint_zero_acceleration` is therefore
too strong as a general v3.51 semantic label.

The v3.51 reason concepts are:

```text
joint_projected_movement_within_epsilon
joint_projected_acceleration_within_epsilon
```

At `epsilon = 0`, these concepts reduce to exact joint projected zero. They do
not claim that complete `Delta Z` or `Delta2 Z` is zero.

## 5. Derivative-order status independence

Two valid three-step trajectory fixtures show that component statuses cannot
be inherited across derivative order:

```text
equal nonzero constant velocity:
  C_move  = numeric 1
  C_accel = not_applicable (joint projected acceleration inside band)

joint current projected rest after different prior movement:
  C_move  = not_applicable (joint projected movement inside band)
  C_accel = numeric 15/16
```

Transition to projected rest may therefore retain a numeric acceleration
comparison. Conversely, equal nonzero movement may coexist with non-applicable
acceleration. `C_gap` remains independently static and is not blocked by
either epsilon rule.

## 6. Bounded finding

The existing rule is arithmetically precise and reproducible, but its meaning
depends materially on the selected epsilon policy. It creates a deliberate
nonnumeric tolerance region rather than measuring compatibility everywhere.
Accordingly:

- epsilon identity/version and raw operands must remain attached;
- status transitions remain categorical, not numeric deltas;
- display and aggregation must expose excluded/subthreshold opportunities;
- no component status may be inferred from another derivative order;
- no positive epsilon should be called exact zero or stillness;
- selection of epsilon values requires empirical/question-specific evidence
  and human authority, not formula correctness alone.

## 7. Human policy questions

1. Is the inclusive boundary `<= epsilon` retained as the v3.51 policy form?
2. Is the joint tolerance region correctly `not_applicable`, rather than a
   numeric compatibility result with a separate low-activity flag?
3. Should v3.51 replace zero/stillness reason wording with
   `joint_projected_*_within_epsilon` while retaining exact raw operands?
4. Is it accepted that one-sided zero is numeric only when the other side lies
   outside the joint epsilon band?
5. Are the 22 boundary rows and two derivative-order trajectory fixtures
   accepted as the Phase-C reference basis?

Next after policy review: Phase D tests R0 gate/status precedence, ordered-dyad
identity, pairing identity, separate source-local predecessors and excluded
opportunities.

## 8. Contract conclusions

- exact joint projected zero uses the reference `epsilon_method = 0` and
  remains `not_applicable` for the current movement/acceleration question;
- positive thresholds require a separately identified, versioned basis rather
  than one untyped epsilon default;
- every positive epsilon retains parameter origin and explicit calibration
  status; a set/test value is never reported as empirically calibrated;
- numerical calculation tolerance, measurement-resolution/noise boundary and
  question-specific activity/relevance threshold remain distinct;
- a measurement-resolution route may require `not_observable`, whereas a
  selected relevance route may support `not_applicable`; the mapping belongs
  to the named profile;
- the inclusive comparison remains explicit wherever a positive profile is
  later admitted;
- reason wording uses `joint_projected_*_within_epsilon` and never claims full
  Z stillness;
- raw operands, threshold identity and categorical status boundary remain
  reconstructible.

No positive default epsilon is established. Missing cases may be added after
further evidence and a separately versioned profile decision.
