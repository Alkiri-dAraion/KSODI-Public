# KSODI Operator K0 v3.50 - Implementation Companion

This conditional implementation companion is subordinate to the carrier-neutral
[`KSODI_Operator-K_Observable-Context-Completeness_V350.md`](./KSODI_Operator-K_Observable-Context-Completeness_V350.md) method.

Scope: implementation-oriented identity, scope construction, access-relation
evidence, context taxonomies, typed results, profile validation, pseudocode,
partial diagnostics and tests. This file is not the canonical definition of K
and not a mandatory production architecture.

## 0. Authority and Alignment Boundary

The method file controls K's observable question, target and source identity,
admissible scope, availability relation, expected requirements, applicability,
static formula, source-local movement and layer boundaries.

This companion may map those semantics to prompts, retrieval, files, tools,
session state, logs or other concrete carriers. It must not make one LLM stack,
prompt taxonomy, storage field or detector family part of universal K.

A repository-visible object must not be treated as model-visible context
without evidence from the implementation being evaluated. Any comparison with
an external implementation requires its own declared baseline and scope.

## 1. Identity, Index and Context-Object Mapping

```text
n   = global observable event index
k_A = local position inside trajectory A
k_B = local position inside trajectory B
j   = declared relational exchange or paired-evaluation index

pi(j) = (k_A(j), k_B(j))
```

One K result belongs to one `target_event_id`, one stable or explicitly
provisional `source_entity_id`, one `source_attribution_status`, one
`trajectory_id`, one local index and one K profile version.
`emitting_entity_id` is stored separately only when established. Every
admitted context object retains:

```text
context_object_id
originating_entity_id or system_id
origin_event_id, if applicable
object_type and version or content hash
admission_evidence
availability_relation_evidence
visibility_boundary
retention state
```

A conversation, workspace, shared folder or timestamp is a container
reference, not proof that every contained object was available for the target
event.

## 2. Required Evaluation Record

An implementation should store or recoverably reference:

```text
evaluation_id, operator, method_version
target_event_id, source_entity_id, source_attribution_status
emitting_entity_id, if established
trajectory_id
global_event_index, local_trajectory_index
conversation_id or environment_id, if applicable
exchange_id and reply_to_event_id, if applicable
sender_role and receiver_role, if applicable

scope_id
scope_construction_policy_id and version
context_object_ids and admission records
availability_relation_id and version
availability_relation_evidence
observer_vantage_id and version

k_profile_id and version
expected_requirement_profile_id and version
detector_profile_id and version
fulfillment_profile_id and version
binary_or_graded_profile_id and version
component_attribution_policy_id and version
weight_profile_id and version
applicability_profile_id and version

expected_requirement_ids
requirement_states and values
requirement_evidence_refs
active_weights and overlap decisions

gate_status, operator_result_status, status_reason
result_value only when operator_result_status = numeric
formula_variant
comparability_status and reason
predecessor_target_event_id, if applicable
window_profile_id and hangar_derivation_id, if applicable
partial_diagnostic_refs, if any
evaluator_id and version
provenance_record
```

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
declared_scope_unobservable
scope_not_applicable
expected_requirement_set_empty
context_object_unresolved
availability_relation_unobservable
requirement_detector_unavailable
requirement_observably_absent
profile_incompatible_for_comparison
same_trajectory_predecessor_missing
window_subset_empty
```

`requirement_observably_absent` supports numeric zero at component level. It
does not close the gate. Required access or context that exists or is expected
but cannot be inspected maps to `not_observable`. Absence of a valid context
basis maps to `not_applicable`; elective omission maps to `not_selected`.
Every successful applicable finite K calculation maps to `numeric`.

Implementation failures remain outside the operator-result status domain:

```text
target_identity_missing
source_identity_missing
profile_missing
profile_invalid
scope_policy_missing_or_invalid
availability_relation_undeclared
observer_vantage_undeclared
invalid_weight_sum
overlapping_requirement_evidence
calculation_error
```

They produce no valid `operator_result_status` or K value and must not be
coerced into zero or a common non-numeric status merely to complete Z.

## 4. Profile Schema and Validation

```yaml
profile_id: p_K_example_v1
method_version: "3.50"
target_unit_profile: one-source-attributed-event
scope_construction_policy: versioned-policy
context_object_admission_policy: versioned-policy
expected_requirements: []
availability_relation_profile: target_access
observer_vantage_profile: versioned-vantage
detector_profile: versioned-detector
fulfillment_profile: binary
component_attribution_policy: versioned-policy
formula_variant: unweighted
weights: null
applicability_policy: complete-required
interpretation_profile: versioned-policy
```

Stop with a processing failure before calculation when:

- target, source or trajectory identity is unresolved;
- scope construction or object admission is undeclared;
- availability relation or observer vantage is missing;
- one availability fact is reused contrary to the attribution policy;
- active weights are non-positive or have zero sum;
- a fallback, partial calculation or substitution was not predeclared.

Return the reason-mapped common non-numeric status when a valid selected
profile encounters an operator-domain condition:

- the declared scope exists or is expected but cannot be observed;
- no valid scope applies to the target class;
- the expected requirement set is empty;
- any expected requirement cannot be observed under a complete profile;
- a valid required detector cannot inspect the required evidence.

Evidence unavailability maps to `not_observable`; an absent valid basis maps to
`not_applicable`. Invalid scope construction, detector configuration or
calculation remains a processing failure.

Target-access, evaluator-access and receiver-access profiles answer different
questions. Give them different IDs and never compare them silently.

## 5. Suggested Static Data Flow

```text
1. Resolve target-event, source and trajectory identity.
2. Resolve the versioned K profile.
3. Build the admissible scope from identified context objects.
4. Resolve availability relation and evaluator vantage.
5. Verify availability evidence for each admitted object.
6. Resolve the non-empty expected requirement set.
7. Decide observability and applicability before numeric fulfillment.
8. Evaluate every expected requirement.
9. Enforce attribution and overlap rules.
10. Validate the complete numeric set and denominator.
11. Calculate exactly one selected K profile.
12. Store result, gate state, evidence and provenance.
13. Establish comparability before Delta, window or Hangar construction.
```

Reference pseudocode:

```python
def evaluate_k(event, profile, observed_context):
    validate_identity(event)
    validate_profile(profile)

    if not profile.selects_k:
        return TypedResult(status="not_selected")

    scope_result = build_admissible_scope(observed_context, profile)
    if scope_result.status != "applicable":
        return map_scope_failure_to_operator_result(scope_result)
    scope = scope_result.value

    requirements = resolve_expected_requirements(event, profile)
    if not requirements:
        return TypedResult(
            status="not_applicable",
            reason="expected_requirement_set_empty",
        )

    results = []
    for requirement in requirements:
        relation = observe_availability_relation(
            requirement,
            scope,
            profile.availability_relation_profile,
            profile.observer_vantage_profile,
        )
        if relation.status != "applicable":
            return map_requirement_failure_to_operator_result(relation)
        fulfillment = evaluate_requirement_fulfillment(
            requirement, relation, profile
        )
        if fulfillment.status != "applicable":
            return map_requirement_failure_to_operator_result(fulfillment)
        results.append(fulfillment)

    validate_component_attribution(results, profile)

    if profile.formula_variant == "unweighted":
        value = arithmetic_mean([result.value for result in results])
    else:
        weights = resolve_positive_weights(requirements, profile)
        value = weighted_mean([result.value for result in results], weights)

    return numeric_k_result(value, event, scope, profile, results)
```

The pseudocode is illustrative. It prescribes no framework, database,
retrieval stack or model provider. Validation helpers return a processing
failure for invalid identity, profile, scope policy, attribution, weights or
calculation. `numeric_k_result` emits `operator_result_status = numeric` and a
finite `result_value in [0,1]`. The mapping helpers preserve the specific
reason, map only valid evidence-unavailability and no-basis conditions to the
common non-numeric statuses, and return a processing failure for invalid
states.

## 6. Context Scope and Availability-Evidence Notes

### 6.1 Scope Construction

An implementation may organize identified context objects into classes such
as task or goal context, governance or policy context, carrier or environment
context, admitted prior events, external assets, capabilities and visible
session state. These are implementation classes, not additional K coordinates
and not a universal ontology.

### 6.2 Access Evidence

Possible evidence for `target_access` includes:

- an immutable request envelope bound to the target event;
- a trace showing retrieval output inserted before target generation;
- a tool or orchestration log showing context admission;
- a signed or hashed context manifest bound to `target_event_id`;
- a governed human-process record showing prior supply.

“The file existed,” “the tool was enabled,” or “the UI displayed it” is weak
evidence unless that is the availability relation explicitly selected by the
profile.

### 6.3 Context Roles and Double Counting

One object may support several genuinely distinct requirements, for example a
task document may contain both a goal and a constraint. Store separate evidence
spans or relations. Do not count one undifferentiated “document present” fact
repeatedly as though it proved every requirement.

If requirements are correlated, the profile should merge them, down-weight
them or declare the dependence. Silent independence is invalid.

## 7. Illustrative Human-Chatbot Task Profile

The former `G/P/A/X/F/L` set is retained here as one candidate profile rather
than universal K canon:

```text
Cset_task = {G, P, A, X, F, L}
```

| Feature | Candidate meaning | Observable question |
| --- | --- | --- |
| `G` | goal | Is the expected task goal available under the declared relation? |
| `P` | perspective or role | Is an expected standpoint or role declaration available? |
| `A` | assets or admitted material | Are expected data, files, examples or retrieved objects admitted? |
| `X` | constraints | Are expected rules, limits or exclusions available? |
| `F` | requested output form | Is the expected form specification available? |
| `L` | tools or capabilities | Is the applicable capability declaration available? |

```text
profile_id = p_K_task_context_candidate_v1
availability_relation = target_access
fulfillment_profile = binary_explicit_marker
formula_variant = unweighted
expected_feature_subset = declared per target-event class
```

Possible explicit markers include task statements, named roles, declared asset
references, constraints, output schemas and a non-empty capability manifest.
They establish only profile-defined observable availability. They do not prove
semantic adequacy, correctness or actual use.

Concrete container mappings may include:

| Application field | Candidate scope role |
| --- | --- |
| `system_context` | governance/policy or task context, as declared |
| `developer_or_project_context` | governance/policy or task context |
| `user_prompt` | task/goal context |
| admitted prior turns | admissible prior events |
| `retrieved_context`, files, tool output | external objects |
| `tool_availability` | available capabilities |
| visible session state | session context |

Field names do not prove admission. A tool output is separate from tool
availability. K may observe presence under its profile; O may separately use an
admitted tool output in a visible declared `Ref`.

## 8. Illustrative Unknown-Signal Profile

```text
profile_id = p_K_unknown_signal_candidate_v1
availability_relation = evaluation_access
expected_requirements = {
  sampling_calibration,
  bounded_observation_window,
  detector_configuration,
  admitted_prior_bursts_if_selected,
  codebook_if_selected
}
formula_variant = unweighted
```

The codebook is not missing unless the profile selects it. Calibration or prior
bursts may be context for K without establishing meaning, grounding or
acknowledgement. The profile makes no claim about context available to the
unknown emitter.

## 9. Separate Partial and Scope Diagnostics

### 9.1 Partial Observable Requirement View

When complete K is `not_observable`, an explicitly selected diagnostic may
summarize only numeric observable requirements:

```text
E_obs,K,A(k_A)
= {r_i in E_K,A(k_A) | a_i,A(k_A) is numeric}

K_obs,A(k_A)
= sum_{r_i in E_obs,K,A(k_A)} w_i a_i,A(k_A)
  / sum_{r_i in E_obs,K,A(k_A)} w_i
```

The diagnostic profile and positive weights must be declared and the subset
non-empty. Store every omitted requirement ID and state. `K_obs` is not
complete `K0`, never fills K in a complete Z view and has no canonical v3.50
Delta or Sigma definition.

### 9.2 Context-Scope Drift

```text
Delta_scope,A(k_A)
= clip(dist_scope(scope_A(k_ref), scope_A(k_A)), 0, 1)
```

This separately profiled diagnostic describes scope movement. It is not
`Delta K`, does not evaluate context quality and does not alter static K.

### 9.3 Measurement Uncertainty

```text
u_K,A(k_A) in [0,1]
```

Uncertainty may summarize detector confidence, access-evidence ambiguity or
scope reconstruction uncertainty under its own profile. It remains separate
from K. A declared gate policy may make complete K `not_observable`;
uncertainty must not silently penalize a numeric value.

## 10. Comparability, Dynamics, Windows and Hangar

Before Delta K, require:

```text
same trajectory_id
same or explicitly compatible K profiles
compatible scope and object-admission policies
compatible expected requirement sets and fulfillment rules
compatible availability relations and observer vantages
compatible detectors and binary/graded profiles
compatible attribution policies, formulas and weights
compatible applicability and missingness policies
numeric current and predecessor values
```

The predecessor is referenced by `target_event_id`, not guessed from global
time or alternating dialogue order.

Window construction stores separate applicable subsets for static, Delta and
Delta2 values. Every field names its aggregation function, minimum sample size,
missingness policy and profile version.

Hangar distributions are derived views. They retain canonical evaluation refs
and the availability relation. A side-by-side A/B display remains two monadic
views unless a later construct has explicit pairing and an open numeric
canonical complete `R0` gate under the exact required profile.

## 11. Minimum Conformance Tests

### 11.1 Identity and Arity

- removing B leaves A's K construction available whenever A's own basis
  remains satisfied;
- removing a B-originated context object may alter A's result without creating
  a dyadic formula;
- role reversal does not alter stable entity or trajectory identity;
- context-object multiplicity never pools target-event identities;
- predecessor selection never crosses trajectory boundaries.

### 11.2 Applicability and Access

- `not_selected`, `not_observable`, `not_applicable` and numeric zero remain
  distinguishable;
- an empty expected set is `not_applicable`, not complete;
- an observable absent requirement is zero;
- unobservable target access is `not_observable`, not zero;
- repository presence, UI visibility and target admission remain distinct;
- partial diagnostics cannot fill complete K or complete Z.

### 11.3 Numeric Properties

- requirement values and numeric K remain in `[0,1]`;
- the expected set is non-empty;
- weighted profiles use positive weights and denominator;
- unweighted and weighted profiles remain separate;
- binary and graded profiles require a compatibility mapping;
- one availability fact cannot be duplicated contrary to the attribution
  policy.

### 11.4 Semantic Boundaries

- availability does not establish quality, suitability or actual use;
- K availability does not replace O grounding;
- format-instruction presence does not replace S evaluation;
- a listed tool is not an admitted tool output;
- an evaluator-access profile does not claim emitter access;
- no relational claim opens before explicit pairing and an open numeric
  canonical complete `R0` gate under the exact required profile;
- invalid identity, profile, scope policy, attribution, weights and
  calculations produce processing failures rather than extra or coerced Z
  statuses.

### 11.5 Window and Hangar

- empty typed subsets become `not_applicable`, not zero;
- static, Delta and Delta2 aggregates use separate functions and subsets;
- derived distributions retain source, event, trajectory, profile, scope,
  availability relation, window and derivation provenance;
- Hangar never replaces the canonical evaluation record.

## 12. Observer, Controller and Governance Boundary

This implementation observes context provisioning. It does not automatically
inject context, change prompts, select tools, rank persons or control a system.
Any Controller requires a separately authorized policy, audit logging, human
oversight and rollback boundary.

Context and access logs can reveal system instructions, personal data,
security controls or proprietary material. Access, consent, retention,
deletion, redaction and later auditability must be declared. A derived feature
record is not automatically anonymous.

## 13. Publication Boundary

This companion is publicly released beside the carrier-neutral method. It
remains conditional and visibly subordinate and must not be presented as the
only valid K implementation or a mandatory production stack. Publication does
not convert its context taxonomies, detector mappings, candidate profiles or
weights into universal K semantics. Software integration and any
implementation owned by another party still require a separate
implementation-side review and license decision.
