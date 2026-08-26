# KSODI IK_rel v3.50 - Implementation Companion

Authority: implementation guidance only. The mathematical source of truth is
[`KSODI_Dyadic-Relational-Coherence-IK_rel_V350.md`](./KSODI_Dyadic-Relational-Coherence-IK_rel_V350.md).

## 1. Purpose and record separation

Keep these objects distinct:

```text
monadic trajectory A
monadic trajectory B
pairing record pi(j)
R0 gate result
primary IK_rel result
typed extended component record T_G
fixed-N extended IK_rel^[N]
processing error
```

## 2. Suggested records

```text
IKRelProfile {
  ik_rel_profile_id
  version
  profile_kind                    # primary_move | extended
  required_component_set_N
  component_weights
  zero_movement_policy_id
  zero_acceleration_policy_id
  epsilon_move
  epsilon_accel
  required_monadic_ik_profile_id
  required_r0_profile_id
  required_r0_projection_kind       # complete for v3.50 primary and extended profiles
  theta_r0_stable
}

IKRelResult {
  ik_rel_result_id
  relational_eval_id              # j
  ordered_dyad_id
  pairing_map_id
  member_event_identities[]       # exactly A and B for current v3.50
    target_event_id
    source_entity_id              # stable or provisional
    source_attribution_status
    emitting_entity_id            # present only when established
    trajectory_id
    global_event_index_n
    source_local_position_k
    predecessor_event_id
    predecessor_source_local_position_k
  ik_A_result_id
  ik_B_result_id
  delta_ik_A_result_id
  delta_ik_B_result_id
  r0_result_id
  r0_ordered_dyad_id
  r0_pairing_map_id
  r0_relational_eval_id
  ik_rel_profile_id
  projection_kind                 # primary_move | extended
  component_set_N
  t_g_snapshot
  static_step                     # joint zero first-order movement
  zero_accel_step                 # joint zero second-order movement
  status                          # numeric | not_selected | not_observable | not_applicable
  value
  reason_codes
}
```

Processing errors remain separate from result statuses.

## 3. Primary computation

```text
function compute_primary_ik_rel(pairing, r0, ik_A, ik_B,
                                delta_A, delta_B, profile):
    if profile is absent:
        return status(not_selected)

    validate_primary_profile(profile)
    require profile.profile_kind == primary_move
    require profile.required_component_set_N == [move]
    require profile.component_weights == {move: 1}
    require profile.theta_r0_stable is finite and in [0,1]
    require profile.epsilon_move is finite
            and 0 <= profile.epsilon_move < 1
    validate_pairing_identity(pairing)

    if r0 has incomparable or processing record and no valid result:
        return processing_block(upstream_r0_has_no_valid_result,
                                retain upstream reasons)

    if no valid r0 result exists:
        return status(not_applicable, reason = qualifying_r0_absent)

    require r0.comparison_kind == dyad
    require r0.ordered_dyad_id == pairing.ordered_dyad_id
    require r0.pairing_or_constellation_map_id == pairing.pairing_map_id
    require r0.relational_eval_id == pairing.relational_eval_id
    require same paired member-event identities in r0 and pairing

    if r0.status == not_observable:
        return status(not_observable, reasons = r0.reasons)

    if r0.status != numeric:
        return status(not_applicable, reasons = r0.reasons)

    if r0.projection_kind != complete
       or r0.active_coordinate_set_M != [K,S,O,D,I]:
        return status(not_applicable,
                      reason = reduced_r0_does_not_open_primary)

    require r0.r0_profile_id == profile.required_r0_profile_id
    require r0.threshold == profile.theta_r0_stable
    require r0.threshold is finite and in [0,1]
    require r0.gate_state == (
        open if r0.value >= profile.theta_r0_stable else closed)

    if r0.gate_state != open:
        return status(not_applicable, reason = gate_closed)

    if any required monadic input has processing failure/no valid result:
        return processing_block(upstream_monadic_input_invalid,
                                retain all source reasons)

    if any required monadic input is not_observable:
        return status(not_observable, retain all source reasons)

    if any required monadic input is not numeric:
        return status(not_applicable, retain all source reasons)

    require ik_A and ik_B are canonical
    require delta_A and delta_B are canonical source-local differences
    require same monadic IK profile and weights on A and B
    require profile required by IK_rel matches that shared profile

    if abs(delta_A.value) <= profile.epsilon_move
       and abs(delta_B.value) <= profile.epsilon_move:
        return status(not_applicable, static_step = true)

    gap = abs(delta_A.value - delta_B.value)
    require 0 <= gap <= 2 within tolerance
    value = 1 - gap / 2

    return numeric(value,
                   projection_kind = primary_move,
                   component_set_N = [move],
                   static_step = false)
```

Do not synthesize a shared predecessor. Each delta must already have been
validated inside its own source trajectory.

## 4. Typed extended components

```text
function build_typed_components(inputs, component_profile):
    validate exact R0 handoff as in primary computation:
        same ordered dyad, paired members, pairing map and relational step
        numeric canonical complete dyadic R0 over [K,S,O,D,I]
        open gate, finite matching threshold and exact required R0 profile
    require finite 0 <= epsilon_move < 1
    require finite 0 <= epsilon_accel < 2
    T_G = {}
    T_G.gap   = evaluate_gap_status_and_value(inputs)
    T_G.move  = evaluate_move_status_and_value(inputs)
    T_G.accel = evaluate_accel_status_and_value(inputs)
    T_G.shared = not_selected(reason = reserved_v350)
    return T_G

function evaluate_move_status_and_value(inputs, profile):
    require comparable numeric Delta IK_A and Delta IK_B
    if abs(Delta IK_A) <= profile.epsilon_move
       and abs(Delta IK_B) <= profile.epsilon_move:
        return not_applicable(reason = joint_zero_movement,
                              static_step = true)
    return numeric(1 - abs(Delta IK_A - Delta IK_B) / 2,
                   static_step = false)

function evaluate_accel_status_and_value(inputs, profile):
    require comparable numeric Delta2 IK_A and Delta2 IK_B
    if abs(Delta2 IK_A) <= profile.epsilon_accel
       and abs(Delta2 IK_B) <= profile.epsilon_accel:
        return not_applicable(reason = joint_zero_acceleration,
                              zero_accel_step = true)
    return numeric(1 - abs(Delta2 IK_A - Delta2 IK_B) / 4,
                   zero_accel_step = false)
```

Each evaluator requires the exact compatible open canonical complete dyadic R0
gate first, then applies its own input, comparability and component-local
zero-input contract. An upstream incomparable or processing record yields a
processing block, not `T_G`. `C_gap` remains static
and is not masked by movement or acceleration stillness. Joint zero movement
at the current step must not be reused as the acceleration guard: a transition
to rest can carry nonzero and comparable second differences. Preserve every
reason and both flags.

## 5. Fixed-N extended projection

```text
function compute_extended_ik_rel(T_G, profile):
    N = profile.required_component_set_N
    require N is explicit and non-empty
    require N subset_of {gap, move, accel}
    validate one finite nonnegative weight bound to each named component in N
    require sum(weights_N) == 1 within tolerance

    if any required component has processing failure/no valid component result:
        return processing_block(required_component_invalid,
                                t_g_snapshot = T_G)

    if any T_G[c].status == not_observable for c in N:
        return status(not_observable, t_g_snapshot = T_G)

    if any T_G[c].status != numeric for c in N:
        return status(not_applicable, t_g_snapshot = T_G)

    value = sum(profile.weight[c] * T_G[c].value for c in N)
    return numeric(value,
                   projection_kind = extended,
                   component_set_N = ordered(N),
                   t_g_snapshot = T_G)
```

Never set `N = numeric components at this event`. Never renormalize after an
event-level component disappears. `shared` remains visible as `not_selected`
in `T_G`, but is not selectable in a released v3.50 N.

## 6. Component formulas and ranges

```text
C_gap   = 1 - |IK_A - IK_B|                  # gap in [0,1]
C_move  = 1 - |Delta IK_A - Delta IK_B| / 2 # gap in [0,2]
C_accel = 1 - |Delta2 IK_A - Delta2 IK_B|/4 # gap in [0,4]
```

All inputs must be comparable and all outputs must lie in `[0,1]` within
tolerance. Before the formulas are evaluated, joint zero first-order input
makes `C_move` `not_applicable`, and joint zero second-order input makes
`C_accel` `not_applicable`, under their separately versioned epsilons. A
one-sided zero remains numeric. `C_gap` is unaffected. Clipping may absorb
floating-point noise only. Validate finite `0 <= epsilon_move < 1` and finite
`0 <= epsilon_accel < 2` before applying the zero-input policies.

## 7. Comparability and dynamics

```text
function comparable_rel(a, b):
    return (
      a.status == numeric and b.status == numeric and
      a.ordered_dyad_id == b.ordered_dyad_id and
      same_pairing_semantics(a, b) and
      same_member_identity_policy(a, b) and
      same_r0_profile_and_threshold(a, b) and
      same_complete_dyadic_r0_projection_contract(a, b) and
      same_monadic_ik_profile(a, b) and
      a.ik_rel_profile_id == b.ik_rel_profile_id and
      a.projection_kind == b.projection_kind and
      a.component_set_N == b.component_set_N
    )
```

Only then compute relational-index differences over j. Gate closure, static
masking and component-status changes are categorical events, not numeric
deltas.

## 8. Windows and Hangar

Freeze ordered dyad, pairing policy, R0 contract, monadic IK profile, IK_rel
profile, projection kind, fixed N, aggregator and coverage policy.

Suggested window record:

```text
IKRelWindow {
  window_id
  total_relational_steps
  gate_numeric_eligible_count
  gate_open_count
  movement_opportunity_count
  static_step_count
  eligible_numeric_ik_rel_count
  coverage_rel
  gate_open_rate
  static_rate
  ik_rel_status_counts
  component_status_counts
  aggregate_status
  aggregate_value
}
```

Validate `total_relational_steps > 0` before computing `coverage_rel`.
Compute `gate_open_rate` only when `gate_numeric_eligible_count > 0` and
`static_rate` only when `movement_opportunity_count > 0`; otherwise the
respective rate is non-evaluable. Store all numerators and denominators.
Enforce the declared positive minimum aggregate count and coverage threshold
before emitting `aggregate_value`.

Hangar partitions retain the same keys. Do not pool changing axes or component
sets. Do not zero-fill typed failures or coerce an empty denominator to zero.

## 9. Migration from the legacy IK_rel file

| Legacy construct | Migration |
| --- | --- |
| generic `t` on both trajectories | map to `j` plus explicit `pi(j)` |
| `IK_rel := C_ik_move` | retain only after gate, identity and canonical-profile validation |
| automatic `G_rel_active(t)` | reconstruct fixed N from profile; otherwise legacy non-comparable |
| event-wise weight renormalization | remove; require fixed profile over N |
| `C_shared` active without definition | mark `not_selected` and exclude from N |
| `IK_shared = w dot mean(Z_A,Z_B)` | keep only as observer-side display derivative, not IK_rel evidence |
| binary masks without typed reasons | return to source records; otherwise retain legacy ambiguity |
| reduced monadic IK in primary calculation | exclude or migrate into a separately named future reduced profile |

Retain original IDs, transform version and exclusion reasons.

## 10. Worked fixtures

### 10.1 Numeric primary result

```text
R0 = 0.90, theta = 0.80
Delta IK_A = +0.20
Delta IK_B = +0.10
gap = 0.10
IK_rel = 1 - 0.10/2 = 0.95
```

### 10.2 Opposite maximal movement

```text
Delta IK_A = +1
Delta IK_B = -1
IK_rel = 0
```

This is a genuine numeric zero, not missingness.

### 10.3 Joint stillness

```text
Delta IK_A = 0
Delta IK_B = 0
status = not_applicable
static_step = true
value = absent
```

### 10.4 Closed gate

```text
R0 = 0.60, theta = 0.80
status = not_applicable
reason = gate_closed
```

No relational component is reported as numeric.

### 10.5 Joint zero acceleration

```text
Delta2 IK_A = 0
Delta2 IK_B = 0
C_accel.status = not_applicable
zero_accel_step = true
C_accel.value = absent
```

This remains distinct from `static_step`, which belongs to first-order
movement.

### 10.6 Transition to rest preserves acceleration information

```text
Delta IK_A(j-1) = 0.40
Delta IK_B(j-1) = 0.20
Delta IK_A(j)   = 0
Delta IK_B(j)   = 0

C_move.status = not_applicable
static_step = true

Delta2 IK_A(j) = -0.40
Delta2 IK_B(j) = -0.20
C_accel = 1 - |-0.40 - (-0.20)| / 4 = 0.95
C_accel.status = numeric
zero_accel_step = false
```

First- and second-order eligibility are therefore evaluated independently.

## 11. Acceptance tests

1. closed, non-open or valid non-numeric R0 blocks numeric IK_rel, and gate
   state, numeric value, finite threshold and profile must be mutually
   consistent;
2. reduced `R0^[M]` blocks the v3.50 primary and extended contracts;
3. n-adic R0 does not open current dyadic IK_rel;
4. the R0 record and IK_rel attempt require the same ordered dyad, paired
   member events, pairing map and relational step;
5. an upstream incomparable/processing record produces no valid IK_rel result;
6. an open canonical complete R0 gate alone does not manufacture an IK_rel
   value;
7. pairing requires distinct monadic identities and explicit `pi(j)`;
8. A and B deltas use their own source-local predecessors;
9. different or reduced monadic IK profiles block the primary calculation;
10. full movement- and acceleration-gap ranges map to `[0,1]`;
11. joint zero first-order movement makes `C_move` `not_applicable`;
12. joint zero second-order movement makes `C_accel` `not_applicable`;
13. transition to rest may make `C_move` non-numeric while `C_accel` remains
    numeric;
14. one-sided zero input remains a numeric component comparison;
15. `C_gap` remains statically evaluable under movement stillness;
16. numeric zero remains distinguishable from non-numeric status;
17. `T_G` preserves every extended component status;
18. fixed-N projection rejects implicit/changing N and reserved `shared`;
19. weights are finite, component-bound, nonnegative and sum to one over N;
20. thresholds and epsilons lie in their declared finite normalized domains;
21. categorical gate/status transitions do not become numeric deltas;
22. empty or zero-eligible windows emit no numeric rate or aggregate;
23. windows report coverage, gate-open, static and typed-status numerators and
    denominators;
24. transient shared-set display is not stored as merged state;
25. no result is labeled resonance, coupling, alignment or control.

## 12. Release and alignment boundary

This companion is released subordinate guidance for the public v3.50 IK_rel
method. It does not authorize software merge, implementation adoption,
threshold or epsilon choice, Controller action, a GitHub tag, GitHub Release,
DOI or Zenodo artifact. Patrick alignment remains a separate implementation
decision.
