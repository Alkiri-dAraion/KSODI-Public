# KSODI IK v3.51 - Implementation Companion

Authority: conditional implementation guidance only. The mathematical source
of truth is
[`KSODI_Monadic-Interaction-Coherence-IK_V351.md`](./KSODI_Monadic-Interaction-Coherence-IK_V351.md).
Its input is the complete typed-Z contract in
[`../Layer-2_KSODI-State-Vector-Z_V350/KSODI_State-Vector-Z_V351.md`](../Layer-2_KSODI-State-Vector-Z_V350/KSODI_State-Vector-Z_V351.md).

## 1. Purpose and non-authority

This companion maps the v3.51 IK result family into implementable records,
gates, pseudocode, windows, migration classes and tests. It carries forward
the v3.50 weighted projection and reduced profile while adding the accepted
fixed-reference geometry and `IK-Gesamtbild` contract.

It does not select empirical weights, set universal thresholds, authorize a
retention policy, define a user interface, validate a runtime or redefine
missingness. External implementation material may supply design evidence; it
does not override the method.

A conforming implementation keeps these objects distinct:

```text
complete typed Z input
weighted-axis profile
fixed-reference geometry profile
individual typed IK component result
IK-Gesamtbild / ik_joint_evaluation_view
processing failure
derived window object and aggregate
human display and assistive interpretation
```

## 2. Logical records

### 2.1 Weighted-axis profile

```text
IKWeightProfile {
  ik_profile_id
  ik_profile_version
  profile_status                 # reference | domain | research
  coordinate_order              # exactly [K,S,O,D,I]
  weights                       # map coordinate -> finite number
  purpose
  validation_note
}
```

Validation:

```text
keys(weights) = {K,S,O,D,I}
all weights finite and >= 0
abs(sum(weights) - 1) <= epsilon_weight
```

Transparent reference:

```text
ik_profile_id = ik_equal_reference_v351
weights = {K:0.2, S:0.2, O:0.2, D:0.2, I:0.2}
profile_status = reference
```

Do not label the reference profile calibrated, learned or optimal.

### 2.2 Fixed-reference geometry profile

```text
IKReferenceGeometryProfile {
  reference_geometry_id         # z_equal_coordinate_diagonal
  reference_geometry_version
  coordinate_order              # exactly [K,S,O,D,I]
  reference_unit_vector         # (1,1,1,1,1)/sqrt(5)
  metric_id                     # euclidean_l2
  normalization_id              # l2_by_sqrt_dimension
  dimension                     # 5
  formula_versions
}
```

This profile is independent of the active `IK_w` weights. Learned axes,
weight rays and question-specific corridors require different profile IDs and
are not v3.51 defaults.

### 2.3 Typed component result

```text
IKComponentResult {
  ik_result_id
  eval_unit_id
  target_event_id
  source_entity_id
  source_attribution_status
  emitting_entity_id             # only if established
  trajectory_id
  global_event_index             # n
  source_local_index             # k_A or k_B, never relational j
  observation_granularity_id
  context_scope_id
  z_record_id
  t_z_snapshot
  result_kind                    # ik_w | ik_m2 | ik_ref | axisdev_ref
  formula_id
  formula_version
  projection_kind                # canonical | reduced; only for ik_w
  active_coordinate_set          # complete set or explicit M for reduced ik_w
  ik_profile_id                  # for ik_w
  ik_profile_version
  reference_geometry_id          # for fixed-reference components
  reference_geometry_version
  metric_id
  normalization_id
  numeric_policy_id
  numeric_policy_version
  status                         # numeric | not_selected | not_observable | not_applicable
  raw_value                      # present only when numeric
  reason_codes
  created_at
}
```

Never use `raw_value = 0` for a non-numeric status. A rounded display value is
not stored in `raw_value`.

### 2.4 Joint evaluation view

```text
IKJointEvaluationView {
  view_id
  view_kind                      # ik_joint_evaluation_view
  z_record_id
  complete_labelled_z_reference
  component_result_ids           # selected ik_w, ik_m2, ik_ref, axisdev_ref
  display_policy_id
  access_policy_id
  evidence_drilldown_reference
  provenance
}
```

The view has no `total_value`. It may be partially renderable when a selected
component is non-numeric, but it must preserve that component's typed status.

### 2.5 Processing failure

Malformed profiles, identity mismatch, duplicate coordinates, invalid geometry,
out-of-range inputs and arithmetic failure are processing errors outside the
valid result domain. Do not coerce them to `not_applicable`.

## 3. Complete-state computation

### 3.1 Common input gate

```text
function resolve_complete_z(z_record):
    validate_z_record_identity(z_record)
    require z_record.complete_Z_state == complete
    require z_record.Z exists in coordinate order [K,S,O,D,I]
    require every coordinate is finite and in [0,1]
    return z_record.Z
```

If complete Z does not exist, each selected complete-state component propagates
the method status:

```text
if any required T_Z status is not_observable:
    component_status = not_observable
else:
    component_status = not_applicable
```

An unselected component returns `not_selected`. Every result retains full
`T_Z` and all coordinate reason codes.

### 3.2 Weighted projection

```text
function compute_ik_w(z_record, weight_profile):
    if weight_profile is absent:
        return typed_result(result_kind=ik_w, status=not_selected)

    validate_weight_profile(weight_profile)
    Z = resolve_complete_z_or_propagate_status(z_record)
    if Z is not numeric:
        return propagated typed result

    raw = dot(weight_profile.weights, Z)
    require raw in [0,1] within declared tolerance
    return typed_result(result_kind=ik_w,
                        projection_kind=canonical,
                        active_coordinate_set=[K,S,O,D,I],
                        status=numeric,
                        raw_value=clip_tolerance_only(raw,0,1))
```

Clipping may absorb floating-point tolerance only. It must not hide invalid
inputs or a malformed profile.

### 3.3 Fixed-reference readings

```text
function compute_fixed_reference_readings(z_record, geometry_profile):
    validate_fixed_reference_geometry(geometry_profile)
    Z = resolve_complete_z_or_propagate_status(z_record)
    if Z is not numeric:
        return three separately typed propagated results

    ik_ref = sum(Z) / 5
    centered = [x - ik_ref for x in Z]
    axisdev_ref = sqrt(sum(d*d for d in centered) / 5)
    ik_m2 = sqrt(sum(x*x for x in Z) / 5)

    require 0 <= ik_ref <= 1 within tolerance
    require 0 <= ik_m2 <= 1 within tolerance
    require 0 <= axisdev_ref <= sqrt(6)/5 within tolerance
    require approximately_equal(ik_m2*ik_m2,
                                ik_ref*ik_ref + axisdev_ref*axisdev_ref,
                                epsilon_identity)

    return separately typed numeric results
```

Compute `AxisDev_ref` from centered coordinates. Use the squared identity as an
independent check, not as a subtraction of rounded values.

No partial `IK_M2^[M]`, `IK_ref^[M]` or `AxisDev_ref^[M]` is a v3.51 method
result.

## 4. Reduced `IK_w` computation

For a native reduced profile:

```text
function compute_reduced_ik_w(z_record, M, reduced_profile):
    require M is explicit, non-empty and subset_of {K,S,O,D,I}
    require every X in M has T_Z[X].status == numeric
    validate finite nonnegative weights exactly over M with sum == 1
    raw = sum(reduced_profile.weight[X] * z_record.value[X] for X in M)
    return typed numeric result(result_kind=ik_w,
                                projection_kind=reduced,
                                active_coordinate_set=ordered(M),
                                raw_value=raw)
```

For a profile derived from canonical weights:

```text
denom = sum(canonical_profile.weight[X] for X in M)
require denom > epsilon_weight
w_tilde[X] = canonical_profile.weight[X] / denom
```

Persist `denom`, parent profile, derived profile and `M`. Never auto-select
`M = currently numeric coordinates`; that would restore the prohibited
changing-mask behavior.

## 5. Comparability and source-local dynamics

```text
function comparable_component(a, b):
    return (
      a.status == numeric and b.status == numeric and
      a.result_kind == b.result_kind and
      a.formula_id_and_version == b.formula_id_and_version and
      a.source_entity_id == b.source_entity_id and
      a.trajectory_id == b.trajectory_id and
      comparable_source_local_positions(a,b) and
      a.observation_granularity_id == b.observation_granularity_id and
      a.context_scope_id == b.context_scope_id and
      same_z_contract(a,b) and
      same_numeric_policy(a,b) and
      same_component_profile_or_geometry(a,b)
    )
```

For comparable results of one kind `Q`:

```text
delta_q = current.raw_value - previous.raw_value
delta2_q = delta_q_current - delta_q_previous
```

Keep the complete movement object beside scalar dynamics:

```text
Z_start
Delta Z
component-wise Delta Z
norm_Delta_Z
Z_target
predecessor identity
```

Never label `Delta IK_M2` as `norm_Delta_Z`. Test
`Delta IK_w = dot(w, Delta Z)` only for complete comparable states with stable
weights.

### 5.1 Changed weighted axis

For diagnostic research only:

```text
w_k dot Z_k - w_(k-1) dot Z_(k-1)
= w_(k-1) dot (Z_k - Z_(k-1))
+ (w_k - w_(k-1)) dot Z_k
```

Store the terms as state movement under the old axis and axis-change
contribution. Do not store the sum as canonical `Delta IK_w`, because the
profile changed.

## 6. Window and aggregation contract

### 6.1 Derived window identity

```text
IKWindowObject {
  window_id
  window_kind
  boundary_policy
  start_boundary
  end_boundary
  exact_ordered_member_ids
  included_member_ids
  excluded_member_ids_with_reasons
  source_entity_id
  trajectory_id
  context_scope_id
  observation_granularity_id
  result_kind
  component_profile_or_geometry
  aggregation_order              # derive_then_aggregate | aggregate_then_derive
  aggregator_id_and_version
  minimum_count
  coverage_policy_id
  total_count
  eligible_count
  coverage
  status_counts
  processing_failure_count
  provenance
}
```

Validate `total_count > 0` before coverage. An empty/invalid window has no
numeric coverage or aggregate. Never coerce it to `0/0`, zero coverage or a
numeric zero result.

The window object has its own identity. It is not a target event, not a
participant and not a participant's Z state.

### 6.2 Derive then aggregate

```text
per_state_results = [Q(Z_k) for each eligible complete Z_k]
aggregate = Agg_Q(per_state_results)
```

### 6.3 Aggregate then derive

```text
Z_agg = Agg_Z(one shared eligible set of complete Z vectors)
aggregate = Q(Z_agg)
```

Persist `Z_agg` as a derived aggregate record with exact members, aggregator,
coverage, status and provenance. Never overwrite a source event or participant
state with it.

For the arithmetic-mean reference case, verify linear equivalence for `IK_w`
under stable weights and for `IK_ref`, using one identical complete subset.
Do not require equality for `IK_M2` or `AxisDev_ref`; test and report their two
orders separately.

The v3.51 reference family supports event/clock and tumbling/sliding windows
with arithmetic means. Median, quantiles, robust, semantic/episodic,
change-point and distribution profiles remain separately named extensions.
There is no universal v3.51 minimum count or coverage threshold.

## 7. Machine, assistive and human views

### 7.1 Purpose-required machine object

Retain, where purpose and governance permit:

```text
complete typed Z reference
all selected typed IK component records
raw operands and raw numeric results
profile/geometry/formula/numeric-policy versions
trajectory and predecessor identity
window members, partitions and coverage
transformation and evidence provenance
```

Rich representation does not authorize maximal raw-data retention. Apply data
minimization, access, legal and retention requirements.

### 7.2 Assistive LLM projection

An assistive interpreter may receive a purpose-bound projection that includes
the question, component definitions, typed statuses, values, profiles,
coverage, limitations and allowed evidence links. Its explanation is an
interpretation record, not another IK result. It must not fill missing
coordinates, infer hidden state or claim causality from the bundle.

### 7.3 Human/governance projection

A human view may simplify to labelled lines, points, rings, corridors or
rounded numbers. Store separately:

```text
raw_value
numeric_policy
display_policy
display_value
rounding precision and rule
hidden-detail disclosure
drill-down locator
```

Display equality does not imply equality of Z, profiles or raw results. An
alert opens diagnosis; it does not establish error or authorize action.

## 8. Hangar partitioning

Partition derived IK views by at least:

```text
result_kind
formula/profile/geometry version
canonical or reduced ik_w and fixed M
source and trajectory scope
window kind and aggregation order
numeric/status partition
coverage policy
```

Never pool changing result kinds, `M`, weights, geometries or processing orders
into an unlabeled distribution. Retain the return path to exact operands and
admissible evidence.

## 9. Migration and compatibility

Use one declared migration class:

```text
v351_conformant
legacy_reconstructible
legacy_partially_reconstructible
legacy_noncomparable
```

`reconstruction_pending` is a workflow state, not a method result.

| Legacy field / behavior | Migration treatment |
| --- | --- |
| `A_Z` as sole applicability record | reconstruct `T_Z` only from source records; otherwise retain unknown status detail |
| `IK(t)` from five numeric fields | migrate to `IK_w` only after identity, profile and complete-Z validation |
| `IK_applicable(t)` | recover exact `M` and weights, then migrate to `IK_w^[M]`; otherwise legacy non-comparable |
| changing per-event mask | split by fixed `M` or exclude from dynamics/windows |
| generic `t` / `u` | map to source-attributed evaluation unit and source-local index |
| missing coordinate stored as zero | do not infer genuine zero; return to evidence or record ambiguity |
| rounded-only result | retain display evidence, but do not invent an exact raw operand |
| absent profile/provenance | mark the gap; never reconstruct it as fact |

Migration retains original record ID, transform version, classification and
reason for every exclusion or uncertainty. Non-conformant legacy material may
remain useful for a bounded question.

## 10. Worked reference fixture

For:

```text
Z_A(k_A) = [0.8, 0.6, 0.5, 0.7, 0.9]
w_ref     = [0.2, 0.2, 0.2, 0.2, 0.2]
```

the expected complete-state readings are approximately:

```text
IK_w        = 0.7000000000
IK_ref      = 0.7000000000
IK_M2       = 0.7141428429
AxisDev_ref = 0.1414213562
```

and:

```text
IK_M2^2 = IK_ref^2 + AxisDev_ref^2 = 0.51
```

For an incomplete typed state, canonical `IK_w` and all three fixed-reference
readings remain separately typed non-numeric; no zero fill or automatic subset
renormalization is permitted. A declared reduced `IK_w^[M]` may still exist as
a different question.

## 11. Conformance tests

1. complete Z plus valid weights produces numeric `[0,1]` `IK_w`;
2. fixed-reference readings satisfy their ranges and squared identity;
3. any non-numeric required coordinate blocks every complete-state numeric component;
4. selected typed status propagates without erasing `T_Z` detail;
5. malformed weights, geometry or identity produce processing failure;
6. reduced computation rejects empty, implicit or non-numeric `M`;
7. reduced weights retain denominator and parent profile;
8. changing `M`, weights, geometry, formula or numeric policy blocks comparison;
9. stable complete pairs satisfy `Delta IK_w = w dot Delta Z` within tolerance;
10. `Delta IK_M2` is not reported as `norm_Delta_Z`;
11. arithmetic-mean linear equivalence uses one identical complete subset;
12. nonlinear aggregation orders are calculated and labelled separately;
13. windows retain exact members, denominator, coverage and status partitions;
14. empty/invalid windows produce no numeric coverage or aggregate;
15. joint views contain no total scalar and preserve component statuses;
16. display and assistive objects do not overwrite raw method results;
17. migration does not invent missing identity, profile or provenance;
18. R0 is not computed from IK and no IK result is labelled relational;
19. current IK_rel retains its own exact R0 handoff and formula;
20. every persisted object has a reverse path to its admissible operands.

The dependency-free Phase A-G and window-order reference suite used during
method review provides reproducible mathematical evidence for these contracts.
Publication or runtime integration of that suite remains a separate selection
decision.

## 12. Release and alignment boundary

This companion is subordinate to the v3.51 method. It does not itself authorize
implementation changes, software merge, threshold choice, a GitHub tag,
GitHub Release, DOI or Zenodo artifact.

Reference method and reproducible tests may be published while an independent
runtime-conformance demonstration remains outstanding, provided that boundary
is stated explicitly.
