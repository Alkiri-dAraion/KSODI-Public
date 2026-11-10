# Phase E — fixed component sets, weights and typed projection status

Status: `PUBLIC_V3.51_ASSERTION_CHECKED_REFERENCE_RESULTS /
NOT_RUNTIME_CONFORMANCE`

Basis:

- [Phase 0 frozen basis](./PHASE_0_FROZEN_BASIS.md);
- [Phase-B component separation](./PHASE_B_COMPONENT_SEPARATION_RESULTS.md);
- [Phase-C typed epsilon direction](./PHASE_C_EPSILON_BOUNDARY_RESULTS.md);
- [Phase-D handoff decision](./PHASE_D_R0_HANDOFF_IDENTITY_RESULTS.md).

## 1. Question

Does every declared extended profile retain one fixed nonempty component basis,
named weights and typed-status behavior, or can the basis drift when a
component is unavailable or serialization order changes?

```text
N subset_of {gap,move,accel}, N nonempty
IK_rel^[N] = sum_(c in N) v_c C_c
```

Every selected weight is finite, nonnegative, bound to a component name and
sums to one over the fixed N.

## 2. Reproducible artifacts

- [`calculate_phase_e_fixed_n_reference.py`](./calculate_phase_e_fixed_n_reference.py)
- [`phase_e_fixed_component_sets.csv`](./phase_e_fixed_component_sets.csv)
- [`phase_e_status_propagation.csv`](./phase_e_status_propagation.csv)
- [`phase_e_invalid_profiles.csv`](./phase_e_invalid_profiles.csv)

Reference execution:

```text
verified_nonempty_component_sets=7
verified_status_rows=45
verified_invalid_profile_rows=9
```

SHA-256:

```text
phase_e_fixed_component_sets.csv
00d4882a35c96b921dd5a12f781364af9aa19cf4b7a0b9b69da13dc5d2a6c74b

phase_e_status_propagation.csv
97d1c13af76724952d4e666591f19a0c9b1f24b98bd7902de6eac3d57f1d0431

phase_e_invalid_profiles.csv
393df2bce122a465345503a718b6c84ebc71234883373d9d76b3e4eb33605b32
```

All fixture weights are test-only named weights chosen to make binding errors
visible. They are not canonical extended-profile choices.

## 3. Seven fixed nonempty sets

The complete structural family is:

```text
{gap}
{move}
{accel}
{gap,move}
{gap,accel}
{move,accel}
{gap,move,accel}
```

Current primary IK_rel remains the one-component `{move}` profile. Structural
validity of the other six sets does not make them selected defaults or prove
their semantic usefulness.

Weights are bound by component identity, not list position. Reversing the
serialization order preserves all seven correct results. Rebinding the same
positional weights to the reversed component order changes every multi-
component fixture result and is therefore a detectable profile error.

## 4. Typed status precedence

For one fixed selected N:

```text
required processing failure -> processing block
else required not_observable -> not_observable
else any required nonnumeric -> not_applicable
else                         -> numeric weighted result
```

A nonrequired component does not change the selected projection's status, but
its typed result or processing record remains visible in the complete `T_G`
snapshot. This preserves both the fixed question and the wider diagnostic
basis.

If one required component becomes nonnumeric, the method does not remove it,
renormalize the remaining weights or emit a value from a smaller implicit N.
The fixture table records the tempting renormalized value only as a forbidden
counterexample. Such a value answers a different profile question.

## 5. Invalid profile boundary

The following produce no valid numeric result:

- empty N;
- unknown/reserved or duplicate component identity;
- missing or extra named weight;
- negative or nonfinite weight;
- finite weights not summing to one;
- unnamed positional weights.

These are profile/configuration errors, not valid `not_applicable` results.

## 6. Scalar and point-cloud boundary

Even a valid extended scalar does not replace its component vector. Preserve:

```text
T_G = (typed C_gap, typed C_move, typed C_accel, reserved shared status)
selected N
named weights
scalar result/status
gate, pairing, operands, profiles and provenance
```

The same fixed-basis rule applies analogously to point-cloud analysis:

- one scalar `IK_rel^[N]` cloud contains only results under the same N,
  named weights, component definitions, gate/profile and status policy;
- clouds with different N or weights remain different typed clouds rather than
  being pooled into one unlabeled distribution;
- a component-feature cloud may retain the full typed `T_G`, but axes and
  nonnumeric partitions stay explicit;
- excluded or nonnumeric opportunities remain in coverage/status partitions
  and are not dropped to make the cloud appear complete;
- centroids, distances and clusters are derived views, not dyads, events or
  replacements for their member records.

Thus the calculation path can be reused for compatible point sets without
turning point-cloud convenience into a moving component basis.

## 7. Bounded finding

The fixed-N mathematics is internally consistent. The main implementation and
governance risk is not the weighted sum but silent question change:

- positional weight rebinding;
- event-wise component removal;
- automatic renormalization;
- pooling different profile identities;
- dropping nonnumeric points from coverage.

The complete typed component record and fixed profile identity are therefore
part of the result, not optional debug material.

## 8. Contract conclusions

- All seven sets remain structurally possible; `{move}` is the current primary
  profile and no other set is a default without separate evidence.
- Weights bind permanently to component names rather than positions.
- Required-component status precedence is fixed and reconstructible.
- A nonrequired component may be nonnumeric without blocking the selected
  fixed-N projection when the full diagnostic record remains visible.
- Required components are never removed or followed by renormalization.
- Scalar distributions and point clouds remain partitioned by fixed profile.
- The seven-set, 45-status and nine-invalid-profile fixtures form the Phase-E
  reference basis.
