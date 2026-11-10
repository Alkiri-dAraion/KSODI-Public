# Phase D+ — Complete-Z gate-exclusion regression results

Status: `PUBLIC_V3.51_ASSERTION_CHECKED_REFERENCE_REGRESSION /
NOT_RUNTIME_CONFORMANCE`

Basis:

- [Phase 0 frozen basis](./PHASE_0_FROZEN_BASIS.md);
- [Phase-D R0 handoff results](./PHASE_D_R0_HANDOFF_IDENTITY_RESULTS.md).

## 1. Bounded purpose

This narrow regression checks the exact seam between complete paired monadic
movement, the independently calculated canonical-complete dyadic R0 gate, raw
axial movement compatibility and the actual current primary IK_rel result.

It tests five complete-Z cases requested by the semantic review. It does not
start another A–G series, select a production threshold, validate a domain,
change R0 or IK_rel, or authorize an ungated relational result.

## 2. Reproducible artifacts

- [`calculate_phase_d_plus_gate_exclusion_reference.py`](./calculate_phase_d_plus_gate_exclusion_reference.py)
- [`phase_d_plus_gate_exclusion_complete_z.csv`](./phase_d_plus_gate_exclusion_complete_z.csv)

Reference execution:

```text
verified_complete_z_cases=5
closed_gate_cases=2
open_gate_cases=3
numeric_ik_rel_cases=2
nonnumeric_ik_rel_cases=3
output=phase_d_plus_gate_exclusion_complete_z.csv
sha256=55a2d960782d23c6a7c6a6f9aec9d1d97148ed86b5a08a7b3b9fce9af8b9577c
```

The generator uses only Python's standard library and exact `Fraction`
arithmetic for all method calculations. Decimal columns are display aids and
do not feed any assertion.

## 3. Tested subcontracts

Every row retains and assertion-checks:

1. complete five-coordinate before/after Z for A and B;
2. complete signed `Delta Z_A` and `Delta Z_B`;
3. source-local `IK_w` before/after and `Delta IK_w`;
4. normalized complete L1 drift for each side;
5. raw and clipped R0, the exact threshold profile and inclusive gate state;
6. raw `C_move` separately from the emitted IK_rel result;
7. source, ordered-dyad, pairing, relational-evaluation, target-event and
   separate predecessor identities;
8. native basis, normalization, IK, R0 and IK_rel fixture-profile identities;
9. typed IK_rel status/reason and the retained excluded opportunity.

The fixtures declare valid synthetic source attribution and pairing. They do
not claim that their profiles are empirical defaults.

## 4. Exact cases and findings

| Case | Distinguishing condition | `Delta IK_w,A/B` | `d_A/d_B` | R0 / threshold | Gate | raw `C_move` | current primary IK_rel |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `D+01` | strong equal uniform movement | `3/4`, `3/4` | `3/4`, `3/4` | `1/4` / `1/2` | closed | `1` | `not_applicable / gate_closed` |
| `D+02` | equality at the gate threshold | `1/2`, `1/2` | `1/2`, `1/2` | `1/2` / `1/2` | open | `1` | `numeric(1)` |
| `D+03` | equal projection, additional off-axis drift for B | `1/2`, `1/2` | `1/2`, `27/50` | `12/25` / `1/2` | closed | `1` | `not_applicable / gate_closed` |
| `D+04` | D+01 movement under another test threshold | `3/4`, `3/4` | `3/4`, `3/4` | `1/4` / `1/5` | open | `1` | `numeric(1)` |
| `D+05` | complete movement with joint zero axial projection | `0`, `0` | `2/25`, `2/25` | `23/25` / `1/2` | open | `1` | `not_applicable / joint_projected_zero_under_numeric_policy` |

The result reproduces the bounded semantic claim through a separate checked-in
calculation path. In particular:

- perfect raw projected compatibility does not override a closed R0 gate;
- equal `Delta IK_w` does not determine the actual complete-Z gate;
- threshold equality opens only because the current test contract uses
  `R0 >= theta`;
- changing the threshold changes the comparison profile and can change the
  gate result without changing the movements;
- an open gate does not bypass later component applicability checks.

## 5. Reconstructibility and claim boundary

The regression supports this bounded v3.51 statement:

> Current primary IK_rel describes compatibility of explicitly paired,
> comparable movement along one shared declared IK_w axis only inside its
> exact open canonical-complete dyadic R0 stability corridor and after the
> selected component's own applicability checks.

A valid closed numeric R0 keeps its value, threshold/profile, pairing,
complete movements, raw diagnostic operand and excluded opportunity. It makes
current primary IK_rel `not_applicable`; it does not prove absence of relation,
joint movement, coupling, agreement, a common cause or domain relevance.

`C_move_raw=1` behind the gate must not be emitted as `IK_rel=1`, pooled into
an IK_rel aggregate or inserted into the valid relational point cloud. A later
`ungated_move_diagnostic` remains a separately named research direction with
its own purpose, eligibility, validation and partition.

## 6. Limits and next use

- The thresholds `1/2` and `1/5` are transparent fixture settings only.
- The coordinates and identities are synthetic and establish no empirical
  frequency, semantic meaning, clinical result or causal relation.
- All five rows use one equal-weight monadic reference axis and exact-zero
  movement applicability. Other accepted profiles require their own fixtures.
- This is reference arithmetic and contract regression, not runtime-
  conformance evidence.
- The bounded claim is integrated into the v3.51 `R_0` / `IK_rel` contract.
  The ungated research direction is not current method behavior.

## 7. Contract conclusion

All five reference cases belong to the public v3.51 regression basis. Their
acceptance as fixtures does not establish empirical frequency, semantic
validity or runtime conformance.
