# KSODI `IK_rel` v3.51 — Conditional Implementation Companion

Status: `PUBLIC_V3.51_SUBORDINATE_IMPLEMENTATION_GUIDANCE /
NOT_RUNTIME_CONFORMANCE`

Authority: implementation guidance only. The method source is
[`KSODI_Dyadic-Relational-Coherence-IK_rel_V351.md`](./KSODI_Dyadic-Relational-Coherence-IK_rel_V351.md).

## 1. Required object separation

Keep distinct:

```text
monadic trajectory A
monadic trajectory B
pairing record pi(j)
exact Layer-4 R_0 handoff
primary IK_rel result
typed component record
fixed-N projection
window opportunity ledger and aggregate
assistive interpretation and human display
processing failure
```

## 2. Logical records

Physical schemas may differ, but a conforming implementation can reconstruct:

```text
IKRelProfile {
  profile_id, version, profile_kind
  required_component_set_N
  component_name_bound_weights
  required_monadic_ik_w_profile_id
  required_r0_profile_id
  required_r0_projection_kind = canonical_complete
  theta_r0_gate_open_min
  epsilon_policies[] {
    component_name, epsilon_kind, epsilon_value
    domain_and_scale, inclusive_boundary_policy
    evidence_or_rationale, policy_id, version
    status_consequence, raw_operand_retention
  }
}

IKRelAttempt {
  result_id, relational_eval_id_j, ordered_dyad_id, directionality
  pairing_map_id, observation_question_id, comparison_scope
  members[2] {
    target_event_id, source_entity_id, source_attribution_status
    trajectory_id, source_local_position_k
    predecessor_event_id, predecessor_source_local_position_k
  }
  r0_result_id
  ik_w_result_ids[2], delta_ik_w_result_ids[2]
  delta_z_result_ids[2]
  profile_id, component_set_N, component_status_map
  raw_operands, raw_component_gaps
  result_status, raw_value, reason_codes
  numeric_policy_id, calculation_realization
  display_value, display_policy_id
  provenance
}
```

Processing failures remain separate from method statuses. `static_step` and
`theta_r0_stable` are accepted only as explicitly mapped legacy aliases.

## 3. Atomic decision procedure

```text
function compute_primary_ik_rel(attempt, r0, operands, profile):
    if profile is absent:
        return method_status(not_selected)

    validate_profile_identity(profile)
    require profile.profile_kind == primary_move
    require profile.required_component_set_N == {move}
    require profile.component_name_bound_weights == {move: 1}
    validate_pairing_and_predecessor_identity(attempt)

    if r0 has no valid result because of failure or incomparability:
        return processing_block(upstream_r0_invalid, preserve=r0)

    require exact_same_dyad_members_pairing_and_step(attempt, r0)
    require r0.profile_id == profile.required_r0_profile_id
    require r0.projection_kind == canonical_complete
    require r0.active_coordinate_set_M == {K,S,O,D,I}
    require r0.threshold == profile.theta_r0_gate_open_min
    require r0.gate_state == derive_gate_state(r0.value, r0.threshold)

    if r0.status == not_observable:
        return method_status(not_observable, preserve=r0)
    if r0.status != numeric or r0.gate_state != open:
        return method_status(not_applicable, reason=gate_not_open,
                             preserve=r0)

    if required operands have failure or invalid identity:
        return processing_block(upstream_monadic_operand_invalid)
    if required operands are not observable:
        return method_status(not_observable, preserve=operands)
    require all required operands are numeric
    require same_exact_canonical_ik_w_profile(operands)
    require source_local_predecessors_are_distinctly_valid(operands)

    epsilon_decision = evaluate_move_epsilon(operands, profile)
    if epsilon_decision is nonnumeric:
        return epsilon_decision with raw operands retained

    gap = abs(delta_ik_w_A - delta_ik_w_B)
    require 0 <= gap <= 2 within numeric tolerance
    raw_value = 1 - gap / 2
    require 0 <= raw_value <= 1 within numeric tolerance

    return numeric(raw_value, component_set_N={move},
                   raw_operands=operands, reverse_links=delta_z_records)
```

The implementation must not synthesize a shared predecessor or infer the
handoff from an `R_0` number alone.

## 4. Epsilon evaluator

```text
function evaluate_move_epsilon(operands, policy):
    switch policy.kind:
      epsilon_numeric_tolerance:
        if both canonical_zero_under_policy:
          return not_applicable(
            joint_projected_zero_under_numeric_policy)
      epsilon_observation_resolution:
        if either required movement is unresolved at resolution:
          return not_observable(
            projected_movement_unresolved_at_observation_resolution)
      epsilon_question_relevance:
        if both observed operands are inside declared joint band:
          return not_applicable(
            joint_projected_movement_below_question_relevance)
      otherwise:
        return processing_block(unknown_or_ambiguous_epsilon_kind)
    return eligible
```

One operand inside and one outside a question-relevance band remains numeric
when both are observable. One unresolved operand never becomes zero. Movement
and acceleration use distinct policies. Learned/adaptive policies require a
separate validated profile and may not self-confirm against the desired result.

## 5. Typed components and fixed-N projection

```text
C_gap   = 1 - abs(IK_w_A - IK_w_B)
C_move  = 1 - abs(Delta IK_w_A - Delta IK_w_B) / 2
C_accel = 1 - abs(Delta2 IK_w_A - Delta2 IK_w_B) / 4
```

Each evaluator first validates the same exact handoff, then its component-local
operands and policy. Build a status/value record for every component; do not
construct an unlabeled vector by deleting nonnumeric entries.

```text
function compute_fixed_projection(component_records, profile):
    N = profile.required_component_set_N
    require N is explicit, nonempty and subset_of {gap,move,accel}
    require exactly one finite nonnegative named weight per c in N
    require sum(weights) == 1 within tolerance

    if any required component is invalid:
        return processing_block(required_component_invalid)
    if any required component is not_observable:
        return not_observable(component_status_map)
    if any required component is nonnumeric:
        return not_applicable(component_status_map)

    value = sum(weight[c] * component[c].value for c in N)
    return numeric(value, fixed_N=N, component_status_map=all_components)
```

Never set `N` to the components numeric at one event. Never renormalize after a
component disappears. Non-required statuses remain visible.

## 6. Comparability and dynamics

Two results are comparable only when numeric and identical in dyad,
directionality, pairing semantics, member-identity policy, exact `R_0`
profile/threshold/projection, shared `IK_w` profile, `IK_rel` profile,
component set, named weights and epsilon policy.

Only consecutive comparable numeric steps permit `Delta IK_rel` and
`Delta2 IK_rel`. A gate or status transition terminates the numeric chain and
is retained as a categorical event.

## 7. Window opportunity ledger

Suggested logical record:

```text
IKRelWindow {
  window_id, window_kind, ordered_dyad_id, pairing_semantics
  exact_opportunity_member_ids[], overlap_metadata
  profile_id, component_set_N, named_weights
  opportunity_count
  valid_numeric_gate_count, gate_open_count
  post_open_movement_policy_opportunity_count
  movement_epsilon_band_count
  numeric_ik_rel_count
  status_partition_counts, processing_partition_counts
  coverage_rel {numerator, denominator, status}
  gate_open_rate {numerator, denominator, status}
  movement_epsilon_band_rate {numerator, denominator, status}
  aggregator, minimum_numeric_count, minimum_coverage_rel
  processing_error_policy, status_precedence
  aggregate_status, raw_aggregate_value
}
```

Never zero-fill an excluded member or empty denominator. Under
`strict_integrity_v351`, emit a numeric aggregate only if the complete profile
and membership are valid, required processing is contained, minimum count and
coverage pass, and all partitions remain visible.

For a later `PPWA-bounded` profile, additionally persist maximum allowed
processing count/rate and sensitivity/stopping rules. It remains inactive in
v3.51.

## 8. Machine, assistive and display projections

The raw machine result stores unrounded values, identities, policies and
reverse links. The assistive LLM receives a bounded attributable package and
produces a separate interpretation record. The human view may simplify and
round but must expose status, coverage and drill-down.

```text
raw computational result != display value != assistive interpretation
```

No downstream calculation consumes a display or LLM interpretation.

## 9. Migration

Map legacy records only with evidence:

| Legacy construct | v3.51 treatment |
| --- | --- |
| generic shared `t` | explicit `j` plus `pi(j)` |
| `theta_r0_stable` | legacy alias for recorded Layer-4 threshold identity |
| `static_step` | exact joint projected zero only if recorded epsilon is zero |
| `static_rate` | migrate only to precisely supported `movement_epsilon_band_rate` |
| automatic active component vector | reconstruct fixed `N` or classify noncomparable |
| event-wise renormalization | prohibited for v3.51 conformance |
| positional unnamed weights | reconstruct name binding or classify noncomparable |
| rounded result reused as input | prohibit; recover raw value or retain legacy display |
| incomplete window summary | retain historically; no conforming aggregate claim |

Store the migration class, reconstruction state, source identity, transform
version and all unresolved loss. Do not invent missing provenance.

## 10. Required fixtures

Implementations should reproduce the adjacent reference package:

- Phase A: 25 formula rows and six projection-collision fixtures;
- Phase B: 75 component rows and selected trajectory collisions;
- Phase C: 22 epsilon-boundary rows and two derivative-order cases;
- Phase D: 25 projected-feasibility rows, 25 handoff-precedence rows and five
  complete-Z gate-exclusion cases;
- Phase E: seven nonempty component sets, 45 status rows and nine invalid
  profiles;
- Phase F: five coverage scenarios, five overlap windows and six dynamic
  steps.

Fixture thresholds and means are test controls, not production recommendations.

## 11. Acceptance tests

1. invalid or non-opening exact handoff never emits numeric `IK_rel`;
2. reduced/n-adic `R_0` does not open the current primary branch;
3. pairing and both source-local predecessor chains are explicit;
4. unequal/reduced `IK_w` profiles block primary calculation;
5. formula endpoints and genuine numeric zero are preserved;
6. complete-Z projection collisions remain diagnosable;
7. epsilon kind changes status exactly as declared;
8. projected-null findings do not become complete-Z stillness claims;
9. gap/move/acceleration eligibility remains independent;
10. all seven fixed sets are name-bound and never dynamically reduced;
11. invalid weights/profiles yield processing failure, not method statuses;
12. non-required failures remain visible without blocking selected `N`;
13. status/gate transitions break numeric deltas;
14. empty denominators produce no numeric rate;
15. sparse high means cannot override failed count/coverage;
16. overlap and membership are reconstructible;
17. raw/display/LLM records remain separate;
18. migration retains ambiguity and loss;
19. runtime provenance identifies code/profile versions;
20. no result is labelled resonance, alignment, causation or control.

## 12. Boundary

This companion is not runtime conformance and does not establish software
adoption, production thresholds, epsilon calibration, release or action
authority. Runtime evidence must map actual outputs to the frozen fixtures and
preserve exact identities, partitions and provenance.
