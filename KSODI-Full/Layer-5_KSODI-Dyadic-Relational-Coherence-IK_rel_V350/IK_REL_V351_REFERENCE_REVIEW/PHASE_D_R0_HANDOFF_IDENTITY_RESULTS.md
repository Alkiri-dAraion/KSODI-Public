# Phase D — R0 handoff, identity and status precedence

Basis:

- [Phase 0 frozen basis](./PHASE_0_FROZEN_BASIS.md);
- [Phase-C epsilon decision](./PHASE_C_EPSILON_BOUNDARY_RESULTS.md).

## 1. Two separate questions

Phase D distinguishes:

1. **projected existential feasibility** — can any complete-Z realization of
   a given pair `(Delta IK_w,A, Delta IK_w,B)` open the declared canonical L1
   R0 threshold?;
2. **actual handoff validity** — does one concrete R0 record have the exact
   status, gate, identity, profile, pairing and source-local predecessors
   required by current primary IK_rel?

The first never replaces the second.

## 2. Reproducible artifacts

- [`calculate_phase_d_r0_handoff_reference.py`](./calculate_phase_d_r0_handoff_reference.py)
- [`phase_d_projected_r0_feasibility.csv`](./phase_d_projected_r0_feasibility.csv)
- [`phase_d_handoff_precedence.csv`](./phase_d_handoff_precedence.csv)

Reference execution:

```text
verified_projected_feasibility_rows=25
existentially_open_rows=13
existentially_closed_rows=12
verified_handoff_precedence_rows=25
synthetic_r0_threshold=1/2
```

SHA-256:

```text
phase_d_projected_r0_feasibility.csv
feba696a4404adec3e66585fd7c25c0ca16e31083e06528ead295e14e78e7283

phase_d_handoff_precedence.csv
4b7a0cf6cff959f2d7dad208b1e4de4aaa6489e6a53ee3544d51f10a7ac32f1f
```

## 3. Projected feasibility bound

For canonical equal-weight `IK_w` and complete L1 movement:

```text
Delta IK_w,E = mean(Delta Z_E)
d_E,L1       = mean(|Delta Z_E|)
```

The triangle inequality gives:

```text
d_E,L1 >= |Delta IK_w,E|
```

Equality is attainable by uniform coordinate movement, so the maximum R0 that
any complete-Z realization can attain for one projected pair is:

```text
R0_max_from_projection
= 1 - (|Delta IK_w,A| + |Delta IK_w,B|) / 2
```

An open gate at threshold `theta` is therefore existentially possible exactly
when:

```text
|Delta IK_w,A| + |Delta IK_w,B| <= 2(1-theta)
```

For the transparent test threshold `theta = 1/2`, 13 of the 25 Phase-A grid
pairs lie inside or on this diamond and 12 lie outside it. Equality at the
gate threshold opens under the current `>=` policy.

This is a necessary-and-sufficient existence statement over possible complete
Z transitions. It is not the gate result for a concrete observation. Off-axis
movement can increase actual L1 drift while leaving `Delta IK_w` unchanged;
the actual gate always requires complete `Delta Z_A` and `Delta Z_B`.

### 3.1 Consequence for the current method claim

Two sides can have perfect projected movement compatibility and still fail the
current R0 prerequisite because both move strongly:

```text
Delta IK_w,A = Delta IK_w,B = x
C_move = 1

existential R0 opening requires:
2|x| <= 2(1-theta), hence |x| <= 1-theta
```

At `theta = 1/2`, equal projected movements greater than `1/2` cannot open any
canonical complete L1 realization, despite raw `C_move = 1`. At exactly `1/2`,
only a minimum-drift realization reaches the threshold; additional off-axis
movement can close it.

Current primary IK_rel therefore does not describe projected movement
compatibility in general. It describes it only inside the selected open R0
stability corridor. High synchronized movement, clinically/domain-relevant
instability or another meaningful gate-excluded pattern remains observable in
the monadic records and exclusion evidence, but has no current primary IK_rel
value. Any later behind-gate diagnostic or alternative eligibility profile
must remain separately named and validated.

## 4. Handoff precedence

The 25-row decision table verifies these boundaries:

| Condition | Current v3.51 review outcome |
| --- | --- |
| no IK_rel profile selected | `not_selected` before downstream evaluation |
| malformed IK_rel profile or pairing identity | processing error |
| upstream R0 processing/incomparability with no valid result | downstream processing block |
| qualifying R0 absent | `not_applicable` |
| R0/member/pairing/relational identity mismatch | processing error; never compare the wrong objects |
| valid R0 `not_observable` | `not_observable` |
| selected IK_rel but R0 otherwise nonnumeric | `not_applicable` |
| n-adic or reduced R0 offered to current primary dyadic branch | `not_applicable` |
| required R0 profile/threshold mismatch or inconsistent gate declaration | processing error |
| valid numeric closed R0 | valid R0 retained; IK_rel `not_applicable` |
| open R0 plus invalid monadic input | processing block |
| open R0 plus monadic `not_observable` | `not_observable` |
| open R0 plus other valid nonnumeric monadic input | `not_applicable` |
| valid first-event/missing source-local predecessor | `not_applicable` |
| fabricated shared predecessor | processing error |
| monadic IK profile mismatch | processing error |
| exact compatible open handoff | eligible for the selected component policy |

`eligible for component policy` is not yet a numeric result. Phase C may still
produce a component-local nonnumeric status.

## 5. Identity and exclusion finding

R0 and IK_rel do not discover or repair their own observation objects. A
conforming handoff retains:

- ordered dyad and stable member identities;
- pairing map, paired event IDs and relational evaluation ID;
- exact R0 result/profile/threshold/gate record;
- two separate source-local predecessor chains;
- shared compatible canonical IK profile identity;
- every excluded opportunity and reason.

Chronological adjacency between A and B does not create a shared monadic
predecessor. A missing legitimate predecessor yields no movement comparison;
fabricating one is an identity error.

A closed, non-evaluable or mismatched gate does not erase the monadic records
or the observation opportunity. It only blocks current primary IK_rel. Any
sidecar analysis behind the gate requires its own name, purpose, status and
review; it must not masquerade as current IK_rel.

## 6. Contract conclusions

- Projected feasibility is a diagnostic bound, never a substitute for the
  complete-Z `R_0` gate.
- Threshold equality is `open` under the declared `>= theta` contract.
- Identity/profile mismatch is a processing error; a valid closed `R_0` makes
  current primary `IK_rel` `not_applicable`.
- A legitimate absent predecessor differs from a fabricated shared
  predecessor.
- Every excluded opportunity retains its gate, pairing, status and reason
  references.
- The 25 feasibility and 25 precedence cases form the Phase-D reference basis.
- Primary `IK_rel` measures axial movement compatibility only after the exact
  declared gate handoff. Gate-excluded movement requires a separately named
  diagnostic contract.

## 7. Narrow Phase-D+ follow-up

The later [complete-Z gate-exclusion regression](./PHASE_D_PLUS_GATE_EXCLUSION_RESULTS.md)
adds five assertion-checked cases for the semantic boundary identified here,
including equal projected movement with different complete-Z gate outcomes.
It is a focused follow-up, not a replacement for this 25+25-row Phase-D basis
or a new review phase.
