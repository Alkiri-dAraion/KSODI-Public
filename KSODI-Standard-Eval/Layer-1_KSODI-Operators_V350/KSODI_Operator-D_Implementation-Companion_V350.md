# KSODI Operator D0 v3.50 - Implementation Companion

This file provides conditional implementation guidance. It is not the
canonical method definition and not an executable production implementation.

Canonical method source:
[Operator D v3.50](./KSODI_Operator-D_Observable-Clarity_V350.md)

This companion translates the canonical D definition into an implementation
contract. It does not introduce another operator or formula.

The mappings below describe a profile-oriented implementation contract. They
do not make one carrier, detector, segmenter, storage schema or application
domain canonical. Other implementations may use different technical mappings
while preserving the same D semantics, identities, applicability states,
comparability gates and provenance discipline.

## 1. Implementation Boundary

The implementation receives one already declared observable target event and
estimates profile-bound signal discernibility/reconstruction support. It must
not:

- discover communication existence on behalf of I;
- infer a numeric I value as a hidden D input;
- claim completed decoding, meaning or receiver understanding;
- merge events or trajectories from different entities;
- use another entity's event as a source-local predecessor;
- fill non-numeric states with zero;
- replace a failed L/V profile silently with L-only;
- calculate relational D before a separately declared R0 gate;
- route scores back into the observed agent without a separate Controller and
  approved governance corridor.

## 2. Required Evaluation Record

For every attempted D evaluation, store or recoverably reference:

```text
evaluation_id
target_event_id
source_entity_id
emitting_entity_id, if established
source_attribution_status
trajectory_id
trajectory_index = k_A
global_event_index = n
observed_at
physical_time, if separately retained
exchange_id, if applicable
reply_to_event_id, if applicable
context_event_ids, if admitted for metadata only
carrier_type

d_profile_id and version
l_profile_id and version
v_profile_id and version
detector_profile_id and version
carrier_profile_id and version
segmenter_profile_id and version
normalizer_profile_id and version
weight_profile_id and version
applicability_profile_id and version
active_component_mask

support_unit_definition
support_ceiling_or_normalizer
local_unit_definition
distance_function_id and version
expected_variation_threshold
w_L
w_V

l_component_status
l_value, only when l_component_status = applicable
v_component_status
v_raw_value, only when v_component_status = applicable
v_value, only when v_component_status = applicable
operator_result_status
d_value, only when operator_result_status = numeric
status_reason
processing_status, if validation or calculation fails

comparability_status, if evaluated
comparability_reason
predecessor_event_id, if used
window_id, if aggregated
aggregation_profile_id, if aggregated
retention_policy_id
access_policy_id
```

`source_entity_id`, `trajectory_id` and `target_event_id` are distinct fields.
`context_event_ids` must not replace the target event or enter canonical D
numerically unless a future method version explicitly changes the definition.

## 3. Typed Status Model

Keep internal component applicability separate from the common external
Layer-1 result handed to Z.

Internal component statuses may use:

```text
applicable
not_observable
not_applicable
insufficient_valid_units
```

The final operator result uses exactly:

```text
numeric
not_selected
not_observable
not_applicable
```

Processing failures remain separate, for example:

```text
profile_missing
profile_incompatible
calculation_error
```

Each component carries its own status. The final `operator_result_status` is
derived through the declared component mask and fallback policy; it is not
inferred from a null database field. A successfully applicable finite D value
maps to `numeric`. Internal `applicable` is not an additional external result
status.

Recommended representation:

```text
ComponentResult<T> = {
  status: ComponentStatus,
  value: T only when status == applicable,
  reason_code: versioned reason,
  evidence_refs: declared provenance
}

OperatorResult<T> = {
  status: OperatorResultStatus,
  value: T only when status == numeric,
  reason_code: versioned reason,
  evidence_refs: declared provenance
}
```

An empty value field is not itself a semantic state. Serialization must retain
the explicit status and reason.

## 4. Profile Validation Before Calculation

Reject or return a typed non-numeric state before calculation when:

- the target event or trajectory identity is missing;
- carrier/detector/segmenter/normalizer versions are unresolved;
- the active component mask is absent;
- L is selected but its support-unit definition or normalizer is invalid;
- V is selected but its distance function, expected threshold or local-unit
  definition is invalid;
- weights are negative or do not sum to one within the declared numeric
  tolerance;
- `tau_expected_p_V` is outside `[0,1)`;
- the requested fallback was not predeclared by the profile.

Profile validation failure produces no valid operator result unless the
declared policy maps the concrete reason to one of the common non-numeric
operator statuses. It must not emit `D = 0` or introduce another Z status.

## 5. Static Calculation Order

Reference pseudocode:

```text
function evaluate_D(event_record, p_D):
    validate_identity(event_record)
    validate_profile(p_D)

    if D not selected:
        return OperatorResult(status=not_selected)

    L = evaluate_local_support(event_record, p_D.p_L)

    if L.status != applicable:
        return map_component_failure_to_operator_result(L)

    if p_D.component_mask == L_only:
        return OperatorResult(status=numeric, value=L.value)

    if p_D.component_mask != L_plus_V:
        return ProcessingFailure(status=profile_incompatible)

    V = evaluate_local_dispersion(event_record, p_D.p_V)

    if V.status != applicable:
        if p_D.predeclared_fallback_profile == L_only:
            return evaluate_D(event_record, p_D.predeclared_L_only_profile)
        return map_component_failure_to_operator_result(V)

    D = p_D.w_L * L.value + p_D.w_V * (1 - V.value)
    return OperatorResult(status=numeric, value=clip(D, 0, 1))
```

The explicit second call under a predeclared fallback creates a separately
profiled L-only result. It must retain the fallback provenance and must not be
stored as though the original L/V profile succeeded.

`map_component_failure_to_operator_result` retains the component reason and
maps it only to `not_observable` or `not_applicable` under the declared D
policy. `not_selected` arises only from operator/profile selection, not from a
failed selected component. Invalid profiles and calculation errors remain
processing failures rather than additional operator-result states.

## 6. Component Implementation Notes

### 6.1 Local support L

The implementation must expose:

- how effective support units are selected;
- which repeated units count as reinforcement;
- the saturation/ceiling policy;
- why the denominator is valid for the carrier;
- which status is returned when units cannot be observed.

Tests must confirm that unlimited duplication cannot raise L without bound.
Where the event was admitted by I but the units required by D cannot be
exposed, return a D-specific `not_observable` result. Do not reinterpret that
status as a claim that the event itself was never observed.

### 6.2 Local dispersion V

The implementation must expose:

- the local-unit segmenter;
- the exact unordered-pair construction;
- the normalized distance range;
- the expected-variation threshold;
- behavior for fewer than two valid units;
- numeric tolerance and clipping behavior.

For `m` valid units, exactly `m(m-1)/2` unordered pairs are expected. A failure
to generate that set is an implementation error, not a low V result.

### 6.3 Detector overlap

If S, D or another coordinate uses shared embeddings, segmenters, markers or
corpora, record the shared dependency. Validation must examine whether the
common detector creates artificial correlation or double counting. Shared
features do not make the operator meanings identical, but hidden shared
instrumentation can make their results appear less distinct than they are.

## 7. Source-Local Comparability and Dynamics

`G_cmp_D` must verify at least:

```text
same source_entity_id or same preserved provisional source identity
same trajectory_id
correct local predecessor relation k_A-1
compatible target-event granularity
compatible active component mask
compatible detector/carrier/segmenter/normalizer versions
compatible support and dispersion profiles
compatible weights and applicability policy
applicable static D values
```

The global predecessor `n-1` is not a valid substitute unless it is explicitly
also A's comparable local predecessor.

`Delta D` and `Delta2 D` are calculated only after the required gates succeed.
Failed gates return typed `not_applicable` with reasons. Physical-time
interpretation requires a separate sampling/time mapping.

Window profiles must also name the aggregation functions and the variance
convention. Sample variance with fewer than two applicable records is typed as
inapplicable; it is not silently replaced by zero or population variance.

## 8. Window and Hangar Construction

Static D, `Delta D` and `Delta2 D` use separate applicable subsets and separate
aggregation functions. Implementations must retain:

- the original typed records;
- the window membership rule;
- per-field applicable counts and rates;
- aggregation-profile versions;
- source and trajectory provenance;
- distribution reconstruction parameters.

Do not average non-applicable positions as zero. Do not combine the three
object types into one scalar. A Hangar view is a derived Observer view; it is
not another architecture or a shared relational entity.

`P_D_A(W_A)` is reserved and must not be numerically implemented until a
separate definition supplies inputs, formula, range, profile and applicability.

## 9. Validation Tests

Minimum test groups:

### 9.1 Identity and monadic isolation

- removing entity B does not make `D_A` undefined;
- A's predecessor selection never chooses B's event;
- provisional observed-source identity remains stable until an attributed
  provenance update occurs;
- exchange and reply edges do not merge trajectories.

### 9.2 Applicability

- missing L basis produces a typed non-numeric result;
- fewer than two V units produce `insufficient_valid_units` or
  `not_applicable`, never numeric zero;
- L-only output occurs only under a named L-only profile or declared fallback;
- profile change blocks naive deltas.
- every successful finite D calculation emits `operator_result_status = numeric`;
- internal `applicable` never enters the Layer-1-to-Z result-status field;
- processing failures never become extra Z statuses.

### 9.3 Numeric properties

- L, V and applicable D remain in `[0,1]`;
- mean-pairwise V uses the correct number of unordered pairs;
- `tau_expected_p_V` boundary behavior is tested near `0` and `1`;
- non-negative weights sum to one within tolerance;
- the v3.50 default reproduces `0.6 L + 0.4(1-V)`;
- clipping does not hide invalid upstream values.

### 9.4 Semantic boundaries

- an observable but noisy impulse can yield observable I and low D;
- a crisp unknown Morse-like signal can yield high D without resolved O/S/K;
- structural regularity does not automatically raise D unless it contributes
  to the declared D detector;
- high D does not produce a “decoded” or “understood” flag;
- repetition does not infer intent, attack or acknowledgement.

### 9.5 Window/Hangar

- typed subsets preserve their own denominators;
- all-empty fields produce typed non-applicable results;
- applicability rates do not alter D values;
- distributions retain source, trajectory, profile and window provenance.

## 10. Privacy, Retention and Governance

Raw carriers, text, audio, embeddings, bit sequences, local units, scores and
derived distributions may contain sensitive or personal information. Apply:

- data minimization;
- declared purpose and lawful/governance basis;
- role-based access;
- retention and deletion schedules;
- provenance-preserving correction;
- separation of raw and derived-data permissions;
- audit logging for profile and model changes.

Removing the raw carrier does not make derived vectors or distributions
anonymous automatically.

## 11. Observer and Controller Separation

This implementation observes. It does not decide, punish, rank persons,
intervene or steer by itself. Any feedback routing requires a separate
Controller architecture, explicitly approved governance corridors and a rule
preventing the Observer from changing its own measurement basis through
uncontrolled feedback.

## 12. Release and Reuse Boundary

This companion is publicly released beside the canonical Operator-D method
file. It remains subordinate to that method and to the public KSODI
Implementation Guardrails. Publication does not make its conditional profile
mandatory, validate it for every carrier or application or establish a required
production stack. Software translation or transfer into another repository
still requires the corresponding implementation-side review and licence
decision. If this companion and the canonical method appear to differ, the
method controls and the mismatch must be reported rather than silently
normalized.
