# Phase 0 — frozen `R_0` / `IK_rel` v3.51 reference basis

This file freezes the formulas, identities and interpretation guards used by
the adjacent assertion-checked Phases A–F. The package manifest binds the
published method, companion, generators, fixtures and reports to exact bytes.
The 2026-11-12 source reconciliation adds the cross-layer evidence-object
guard and changes no formula, component or status rule.

## 1. Atomic observation object

```text
rho_AB(j | pi(j))
pi(j) = (k_A(j), k_B(j))
```

The two monadic trajectories remain distinguishable. Each side retains its
own target event, source entity, source-attribution status, trajectory,
source-local position and source-local predecessor. `j` is the relational
evaluation index, not a substitute for either source-local position.

The reference dataflow is:

```text
complete comparable Delta Z_A and Delta Z_B
  -> independently calculated canonical R_0,AB(j)

canonical IK_w trajectories A and B
  -> source-local Delta IK_w,A and Delta IK_w,B

exact compatible open numeric canonical-complete dyadic R_0,AB(j)
+ paired comparable Delta IK_w under one shared profile
  -> current primary IK_rel may be numeric
```

`R_0` is independent of `IK`. `IK_rel` does not discover the pair, repair a
missing predecessor or turn two parallel monadic curves into relational
evidence.

## 2. Frozen `R_0` reference and handoff

For complete five-coordinate movement under the equal-coordinate L1 reference
profile:

```text
d_E,L1(j) = ||Delta Z_E(j)||_1 / 5

R_0,raw,AB(j) = 1 - (d_A,L1(j) + d_B,L1(j)) / 2
R_0,AB(j) = clip(R_0,raw,AB(j), 0, 1)
```

The valid numeric gate decision is separate from result status:

```text
numeric R_0 >= theta_R0_gate_open_min -> open
numeric R_0 <  theta_R0_gate_open_min -> closed
nonnumeric R_0                         -> not_evaluable
```

The threshold is a finite versioned policy parameter in `[0,1]`, not an
empirical fact. `theta_R0_stable` is a legacy alias and carries no stability
claim. A closed numeric gate remains a valid `R_0` observation. Reduced or
n-adic `R_0` profiles do not open current primary dyadic `IK_rel`.

## 3. Frozen `IK_rel` formulas

For canonical `IK_w in [0,1]`:

```text
Delta IK_w in [-1,1]
Delta2 IK_w in [-2,2]

C_gap   = 1 - |IK_w,A - IK_w,B|
C_move  = 1 - |Delta IK_w,A - Delta IK_w,B| / 2
C_accel = 1 - |Delta2 IK_w,A - Delta2 IK_w,B| / 4
```

Each numeric component lies in `[0,1]` when its own eligibility and
comparability requirements pass. The current primary profile is:

```text
N = {move}
IK_rel = C_move
```

One-sided observable zero remains numeric. Exact method zero, numerical
tolerance, observation resolution and question-relevance bands remain
distinguishable; a projected null/band result never establishes complete-Z
stillness.

For one fixed nonempty component set
`N subset_of {gap,move,accel}` with finite nonnegative name-bound weights
summing to one:

```text
IK_rel^[N] = sum_(c in N) v_c C_c
```

Every required component must be numeric. Event-wise component removal and
automatic weight renormalization are forbidden.

## 4. Layer-3 connection boundary

Only the explicitly identified shared `IK_w` profile enters current primary
`IK_rel`. `IK_M2`, `IK_ref`, `AxisDev_ref`, the `IK-Gesamtbild` and complete
`Delta Z` / `Delta2 Z` are parallel evidence and diagnostic views; they do not
become implicit primary operands.

An aggregate monadic window object is not an event-bound canonical `Z` and not
a dyadic participant state. It cannot silently satisfy a gate or `IK_rel`
contract that requires event-level canonical movement.

## 5. Gate-exclusion boundary

If current `R_0` is closed, not evaluable or invalid, current `IK_rel` is not
numerically manufactured. This does not erase:

- otherwise qualifying monadic `IK` and complete-Z trajectories;
- a valid numeric closed `R_0` result;
- the gate/status reason and excluded relational opportunity;
- separately named experimental diagnostics under their own contracts.

The current branch must not be bypassed merely because another observation
question remains meaningful.

## 6. Numeric and reproducibility rules

- retain exact expressions where practical and full-precision inputs;
- use dependency-free reference calculations;
- state assertion tolerances and never use clipping to conceal invalid input;
- preserve raw operands, statuses, identities, profiles and gate records;
- distinguish mathematical equality from profile comparability;
- do not use a third-party runtime to define expected method results.

## 7. Reopening rule

Re-freeze and regenerate the package if a governed formula, shared monadic
axis, exact Layer-4 handoff, atomic identity, status precedence, component
profile, window basis or source byte changes. Runtime conformance, threshold
adequacy, empirical calibration and real-world semantic validity remain
separate questions.
