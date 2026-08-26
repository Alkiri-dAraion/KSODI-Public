# KSODI Operator S0 v3.50 - Implementation Companion

This conditional implementation companion is subordinate to the carrier-neutral
[`KSODI_Operator-S_Observable-Structural-Coherence_V350.md`](./KSODI_Operator-S_Observable-Structural-Coherence_V350.md) method.

Scope: implementation-oriented identity, typed results, profile validation,
detector mappings, normalization examples, candidate profiles, pseudocode and
tests. This file is not the canonical definition of S and not a mandatory
production architecture.

## 0. Authority and Alignment Boundary

The method file controls:

- S's narrow observable question;
- source-attributed target identity and monadic arity;
- measurement-basis and applicability discipline;
- component semantics and static formula contract;
- comparability, source-local movement and typed aggregation;
- relational and publication boundaries.

This companion may select concrete carriers, detectors, component masks,
weights and storage mappings. It must not make marker count, document length,
one software stack or one language profile part of the universal S definition.

Implementation alignment with Patrick's current Observer / KSODI-Light stack
is pending. Any mismatch remains visible until that implementation has been
reviewed separately.

## 1. Identity and Index Mapping

Minimum index discipline:

```text
n   = global observable event index
k_A = local position inside trajectory A
k_B = local position inside trajectory B
j   = declared relational exchange or paired-evaluation index

pi(j) = (k_A(j), k_B(j))
```

One S result belongs to one `target_event_id`, one stable or explicitly
provisional `source_entity_id`, one `source_attribution_status`, one
`trajectory_id`, one local trajectory index and one S profile version.
`emitting_entity_id` is retained separately only when established. A
conversation ID, reply edge or shared timestamp does not replace these fields.

Sender and receiver are exchange-relative roles. Role reversal must not change
stable entity identity or splice two source trajectories together.

## 2. Required Evaluation Record

An implementation should store or recoverably reference:

```text
evaluation_id
operator = "S"
method_version = "3.50"

target_event_id
source_entity_id
source_attribution_status
emitting_entity_id, if established
trajectory_id
global_event_index
local_trajectory_index

conversation_id or environment_id, if applicable
exchange_id, if applicable
reply_to_event_id, if applicable
sender_role and receiver_role, if applicable
visible_context_event_ids

carrier_type
target_unit_type
evaluation_scope
payload_reference or governed payload

s_profile_id and version
segmenter_profile_id and version
requirement_profile_id and version
boundary_detector_profile_id and version
order_reference_profile_id and version
normalizer_profile_id and version
weight_profile_id and version
disruption_profile_id and version, if selected
applicability_profile_id and version

mandatory_component_mask
optional_component_mask
active_component_mask
component_attribution_policy_id and version
component_values
component_statuses
active_weights
renormalization_applied

operator_result_status
result_value, only when operator_result_status = numeric
formula_variant
status_reason

comparability_status and reason
predecessor_target_event_id, if applicable
window_profile_id, if applicable
hangar_derivation_id, if applicable

created_at
evaluator_id and version
provenance_record
```

`renormalization_applied` records only a profile-declared normalization over
the applicable selected components inside one static event evaluation. It must
not be reused to authorize or encode event-wise active-set intersection or
renormalization across dynamics, windows, projections or relational
constructions.

Raw payloads and derived feature records may have different retention rules.
References must remain resolvable for the declared audit horizon or explicitly
record that the governed payload was deleted.

## 3. Typed Status Model

Common external Layer-1 statuses:

```text
numeric
not_selected
not_observable
not_applicable
```

Valid retained operator-result reasons may include:

```text
carrier_incompatible
target_unit_incompatible
segmenter_unavailable
required_parts_not_observable
mandatory_component_unavailable
mandatory_component_not_applicable
insufficient_structural_basis
disruption_detector_unavailable
profile_incompatible_for_comparison
same_trajectory_predecessor_missing
window_subset_empty
```

The concrete reason determines the common status. Required evidence or a
selected detector that exists or is expected but cannot be inspected maps to
`not_observable`. A carrier, target unit, component or structural relation for
which no valid basis applies maps to `not_applicable`. Elective omission alone
maps to `not_selected`. Every successful applicable finite calculation maps to
`numeric`.

Implementation failures remain outside the operator-result status domain:

```text
target_identity_missing
source_identity_missing
profile_missing
profile_invalid
invalid_weight_sum
identity_mismatch
calculation_error
```

They produce no valid `operator_result_status` or S value and must not be
coerced into numeric zero or a common non-numeric status merely to complete Z.
A numeric zero is stored only when S applies and the declared structural
relations fail completely.

## 4. Profile Schema and Validation

A machine-readable S profile should define:

```yaml
profile_id: p_S_example_v1
method_version: "3.50"
carrier_profile: declared-carrier
target_unit_profile: one-source-attributed-event
evaluation_scope: declared-scope
segmenter_profile: versioned-segmenter
requirement_profile: optional-versioned-requirements
boundary_detector_profile: optional-versioned-boundary-detector
order_reference_profile: optional-versioned-order-rules
normalizer_profile: versioned-normalizer
mandatory_components: []
optional_components: []
component_attribution_policy: versioned-policy
weights: {}
allow_optional_renormalization: false
marker_only_basis_allowed: false
disruption_profile: null
applicability_policy: versioned-policy
interpretation_profile: versioned-policy
```

Stop with a processing failure before calculation when:

- target or source identity is unresolved;
- profile or constitutive version is missing;
- the profile is internally inconsistent or invalid;
- active weights are negative or sum to zero;
- structural evidence is assigned to several components without a declared
  overlap policy;
- a fallback or renormalization was not predeclared.

Return the reason-mapped common non-numeric status when a valid selected
profile encounters an operator-domain condition:

- the valid profile's carrier or target-unit basis does not apply to the event;
- the selected segmenter cannot expose the required parts;
- a mandatory component cannot be calculated;
- marker-only evidence is active while `marker_only_basis_allowed = false`;
- the active component set fails the profile's structural-sufficiency rule;
- an extended profile selects `P_disrupt` without an applicable disruption
  basis.

An unavailable but required segmenter, component or disruption detector maps
to `not_observable` when its evidence is expected but inaccessible; absence of
an applicable structural basis maps to `not_applicable`. An invalid detector,
overlap configuration or calculation remains a processing failure.

## 5. Suggested Static Data Flow

```text
1. Resolve target-event, source and trajectory identity.
2. Resolve the versioned S profile.
3. Confirm target-unit and carrier compatibility.
4. Determine observability under the selected segmenter.
5. Evaluate component applicability before component values.
6. Enforce the mandatory-component and structural-sufficiency rules.
7. Calculate applicable selected base components.
8. Validate active weights and any declared optional renormalization.
9. Calculate S_base.
10. Apply P_disrupt only under a named extended profile.
11. Store typed result, component mask, profile and provenance.
12. Evaluate comparability before any Delta, window or Hangar operation.
```

Reference pseudocode:

```python
def evaluate_s(event, profile):
    validate_identity(event)
    validate_profile(profile)

    if not profile.selects_s:
        return TypedResult(status="not_selected")

    basis = evaluate_carrier_and_target_unit_basis(event, profile)
    if not basis.is_applicable:
        return map_component_failure_to_operator_result(basis)

    if not target_is_observable(event, profile):
        return TypedResult(status="not_observable")

    component_results = evaluate_selected_components(event, profile)

    mandatory_failure = first_mandatory_component_failure(
        component_results, profile
    )
    if mandatory_failure:
        return map_component_failure_to_operator_result(mandatory_failure)

    optional_failure = first_blocking_optional_component_failure(
        component_results, profile
    )
    if optional_failure and not profile.allow_optional_renormalization:
        return map_component_failure_to_operator_result(optional_failure)

    if marker_only(component_results) and not profile.marker_only_basis_allowed:
        return TypedResult(
            status="not_applicable",
            reason="insufficient_structural_basis",
        )

    if not structural_basis_is_sufficient(component_results, profile):
        return TypedResult(
            status="not_applicable",
            reason="insufficient_structural_basis",
        )

    active = select_active_components(component_results, profile)
    weights = resolve_active_weights(active, profile)
    validate_positive_weight_sum(weights)
    s_base = clipped_weighted_mean(active, weights)

    if profile.formula_variant == "minimal":
        return numeric_s_result(s_base, event, profile, component_results)

    disruption = evaluate_disruption(event, profile)
    if not disruption.is_numeric:
        return map_component_failure_to_operator_result(disruption)

    value = clip(s_base - profile.gamma_s * disruption.value, 0.0, 1.0)
    return numeric_s_result(value, event, profile, component_results, disruption)
```

The pseudocode is illustrative. It does not prescribe a programming language,
framework, database or detector family.
`map_component_failure_to_operator_result` preserves the specific reason and
maps only a valid evidence-unavailability condition to `not_observable` or a
valid no-basis condition to `not_applicable`. Invalid identity, profile,
weights, detector configuration or calculation returns a processing failure,
not an operator result.

## 6. Component Implementation Notes

### 6.1 Structural-Requirement Conformance - `C_req`

For a finite weighted requirement set:

```text
C_req
= sum_r requirement_weight_r * fulfillment_r
  / sum_r requirement_weight_r
```

where `fulfillment_r in [0,1]`, weights are non-negative and the denominator is
positive. Store the requirement version, each fulfillment result and the
aggregation rule. Do not infer an undeclared requirement merely because a
detector can recognize one.

Example mappings may include JSON schema fields and nesting, explicitly
required document sections, protocol envelope fields or declared workflow
phases. Order relations should normally be assigned to `P_order`. If a profile
keeps an order requirement inside `C_req`, the attribution policy must prevent
the same relation from being scored again in `P_order`.

### 6.2 Segmentation and Boundary Support - `M_vis`

An implementation must normalize boundary evidence against a declared carrier
extent or opportunity set. Raw marker count is invalid.

One bounded density profile may use:

```text
rho_boundary
= effective_nonredundant_boundaries / eligible_extent_units

M_vis
= clip(rho_boundary / expected_boundary_density, 0, 1)
```

where `eligible_extent_units > 0` and `expected_boundary_density > 0` are
profile-defined. Other profiles may use boundary-opportunity recall, weighted
segmentation agreement or schema-specific boundary coverage.

The detector must reject redundant delimiters and artificial marker inflation.
For text, a heading followed by unrelated material is not automatically an
effective boundary. For a pulse carrier, gaps may support segmentation only if
the pulse/gap detector is itself applicable and versioned.

`M_vis` alone remains insufficient under the default v3.50 profile discipline.

### 6.3 Order-Relation Coherence - `P_order`

For a finite weighted transition set:

```text
P_order
= sum_u transition_weight_u * relation_satisfied_u
  / sum_u transition_weight_u
```

The order reference may be an explicit schema, task order, protocol state
machine or a predeclared pattern-hypothesis procedure. Store each evaluated
relation and its source.

If a hypothesis is inferred from repeated observations, freeze the hypothesis
and its uncertainty treatment before scoring the target to which it is applied.
Do not fit a unique order rule to one target and then score that target against
its own fitted rule.

### 6.4 Structural Disruption - `P_disrupt`

Keep duplication and fragmentation observable as separate diagnostics:

```text
P_dup  in [0,1] or not_observable or not_applicable
P_frag in [0,1] or not_observable or not_applicable

P_disrupt
= lambda_dup * P_dup + lambda_frag * P_frag

lambda_dup >= 0
lambda_frag >= 0
lambda_dup + lambda_frag = 1
```

The extended profile must declare what counts as disruptive duplication and
what counts as fragmentation for its carrier. Repeated motifs, corrective
restatement, redundancy for error tolerance and deliberate chunking must not be
penalized merely because they repeat or divide material.

If one selected mandatory disruption subdiagnostic is expected but unavailable
to the evaluator, the extended profile is `not_observable`; if no valid basis
for that subdiagnostic applies, it is `not_applicable`. A different
partial-disruption profile must be separately named rather than created by
silent renormalization.

### 6.5 Shared Detector Boundary with D

S and D may reuse a segmenter, embedding or marker extractor, but they ask
different questions. The implementation must record shared detector identity
and test for artificial correlation or double counting:

- D uses segmentation only insofar as it supports signal discernibility and
  reconstruction conditions.
- S evaluates organization and relations among the observed parts.

A shared detector result must not be copied directly into both coordinates as
though the coordinates were synonymous.

## 7. Illustrative Candidate Profiles

These profiles are workbench examples, not empirical validation and not
universal defaults.

### 7.1 Conversational Text Structure

```text
profile_id = p_S_text_conversation_candidate_v1
mandatory_components = {P_order}
optional_components = {C_req, M_vis}
marker_only_basis_allowed = false
allow_optional_renormalization = true
candidate weights:
  C_req  = 0.40
  M_vis  = 0.30
  P_order = 0.30
formula_variant = minimal
```

The target unit is one source-attributed contribution. The profile must define
what counts as an applicable order relation for short, long and atomic
contributions. A short question is not penalized for lacking headings.

### 7.2 Unknown Morse-Like Pulse Burst

```text
profile_id = p_S_pulse_burst_candidate_v1
mandatory_components = {M_vis, P_order}
optional_components = {}
marker_only_basis_allowed = false
candidate weights:
  M_vis   = 0.50
  P_order = 0.50
formula_variant = minimal
```

The target unit is one bounded pulse burst. `M_vis` uses declared pulse/gap
segmentation; `P_order` evaluates selected within-burst relations. Meaning,
sender identity, grounding and acknowledgement remain outside the profile.

### 7.3 Declared JSON Schema

```text
profile_id = p_S_json_schema_candidate_v1
mandatory_components = {C_req}
optional_components = {P_order}
marker_only_basis_allowed = false
allow_optional_renormalization = false
formula_variant = minimal
```

`C_req` may evaluate required fields, nesting and types. `P_order` is selected
only where order is semantically constitutive; ordinary JSON object member
order must not be scored merely because a serializer emits one sequence.

## 8. Comparability, Dynamics, Windows and Hangar

Before Delta S, require:

```text
same trajectory_id
same or explicitly compatible S profiles
compatible target units and carrier profiles
compatible segmenter, requirement, boundary and order profiles
compatible component masks and weights
compatible formula variants and disruption profiles
compatible applicability and missingness policies
numeric current and predecessor values
```

The predecessor is referenced by `target_event_id`, not guessed from a global
timestamp or alternating dialogue order.

Window construction stores separate applicable subsets for static, Delta and
Delta2 values. Each aggregation field names its function, minimum sample size,
missingness policy and profile version.

Hangar distributions are derived views. They retain references to canonical
evaluation records and do not become a new source of static S truth. A
side-by-side A/B visualization is still two monadic displays unless a later
relational construct has explicit pairing and an open numeric canonical
complete `R0` gate under the exact required profile.

## 9. Minimum Conformance Tests

### 9.1 Identity and Arity

- removing Entity B leaves a valid A evaluation unchanged;
- role reversal does not alter stable entity or trajectory identity;
- two entities are never pooled into one static S record;
- local predecessor selection never crosses trajectory boundaries.

### 9.2 Applicability

- `not_selected`, `not_observable`, `not_applicable` and numeric zero remain
  distinguishable;
- missing mandatory components block numeric S;
- required but unavailable observable structural evidence maps to
  `not_observable`, while absence of a valid structural basis maps to
  `not_applicable`;
- marker-only evidence is blocked unless a separately named profile explicitly
  permits and justifies it;
- undeclared fallback and renormalization are rejected;
- an unavailable selected disruption detector blocks the extended profile.
- invalid identity, profile, weights, detector configuration and calculations
  produce processing failures rather than extra or coerced Z statuses.

### 9.3 Numeric Properties

- each component and final numeric S remains in `[0,1]`;
- weights are non-negative and active weight sum is positive;
- marker duplication cannot inflate `M_vis`;
- one evidence item cannot be counted across components without the declared
  overlap policy;
- the disruption penalty cannot increase S;
- static, Delta and Delta2 values remain separate types.

### 9.4 Semantic Boundaries

- shortness and simplicity do not automatically reduce S;
- formatting density does not equal structural coherence;
- S does not claim meaning, truth, grounding, clarity or information novelty;
- a Morse-pattern score does not claim decoding or acknowledgement;
- shared S/D detectors do not collapse the two coordinates;
- no relational claim opens before explicit pairing and an open numeric
  canonical complete `R0` gate under the exact required profile.

### 9.5 Window and Hangar

- empty typed subsets become `not_applicable`, not zero;
- static, Delta and Delta2 aggregates use separate functions and subsets;
- derived distributions retain source, trajectory, event, profile, window and
  derivation provenance;
- Hangar never replaces the canonical evaluation record.

## 10. Observer, Controller and Governance Boundary

This implementation observes and records profile-bound structure. It does not
automatically rank persons, punish communication styles, choose interventions
or control a system. Any controller requires a separately authorized policy,
fairness analysis, human-oversight design and logging boundary.

Raw carriers and derived structures remain subject to access, consent,
retention and deletion rules. Model, detector and profile changes must be
auditable.

## 11. Publication Boundary

This companion is publicly released beside the carrier-neutral method. It
remains conditional and visibly subordinate and must not be presented as the
only valid S implementation or a mandatory production stack. Publication does
not convert its detector mappings, candidate profiles or workbench weights
into universal S semantics. Software integration and any implementation owned
by another party still require a separate implementation-side review and
license decision.
