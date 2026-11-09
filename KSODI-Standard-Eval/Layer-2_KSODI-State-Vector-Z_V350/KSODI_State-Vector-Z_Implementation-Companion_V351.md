# KSODI State Vector Z v3.51 - Implementation Companion

This cumulative successor preserves the v3.50 implementation boundary and
adds the identity, basis-instance, representation, window-object and migration
precision required by the v3.51 method. It is reference guidance, not evidence
that any particular runtime conforms.

This conditional implementation companion is subordinate to the carrier-neutral
[`KSODI_State-Vector-Z_V351.md`](./KSODI_State-Vector-Z_V351.md) method.

Scope: storage schema, validation, typed-status mapping, partial projections,
dynamics, migration, pseudocode and conformance tests. This file is not the
canonical definition of Z and does not prescribe one database, framework or
Observer architecture.

Read together with:

- [`KSODI_State-Vector-Z_V351.md`](./KSODI_State-Vector-Z_V351.md), the controlling method;
- the [v3.51 Layer-1 measurement-basis discipline](../Layer-1_KSODI-Operators_V350/LAYER_1_MEASUREMENT_BASIS_AND_REFERENCE_DISCIPLINE_V351.md).

## 0. Authority boundary

The method file controls:

- source-attributed target and trajectory identity;
- canonical coordinate order `(K,S,O,D,I)`;
- mandatory typed status vector `T_Z`;
- derived binary mask `A_Z`;
- complete-Z and partial-projection boundaries;
- comparability, dynamics, norms and coverage semantics;
- IK, R0, Hangar and publication boundaries.

This companion may choose concrete record fields, validation code, indexes,
serialization, migration and display behavior. It must not:

- create a numeric coordinate from a non-numeric status;
- use zero as a missing-value placeholder;
- label a reduced projection as complete Z;
- merge A and B into `Z_AB`;
- infer relational pairing from timestamps or conversation membership;
- define IK, R0 or a relational formula.

Any comparison with an external implementation requires its own declared
baseline and scope and must preserve the method/implementation boundary.

## 1. Canonical identity mapping

Minimum identity fields:

```text
target_event_id
source_entity_id
source_attribution_status
emitting_entity_id, if established
trajectory_id
global_event_index n
local_trajectory_index k_A
```

Optional environment fields:

```text
conversation_id
thread_id
exchange_id
reply_to_event_id
timestamp
sender_role
receiver_role
```

Optional fields do not replace canonical identity. Sender and receiver are
exchange-relative roles. `timestamp` or legacy `turn_index` must map to the
source-local index rather than becoming a shared trajectory key.

## 2. Coordinate-result schema

Recommended record for each Layer-1 coordinate:

```yaml
coordinate_record_id: immutable-id
operator_id: K | S | O | D | I
method_version: "3.51"

target_event_id: event-id
source_entity_id: stable-or-provisional-source-id
source_attribution_status: confirmed-or-controlled-provisional-status
emitting_entity_id: entity-id-or-null
trajectory_id: trajectory-id
global_event_index: integer
local_trajectory_index: integer

result_status: numeric | not_selected | not_observable | not_applicable
result_value: number-or-null
status_reason: controlled-reason-or-null

profile_id: profile-id
profile_version: version
basis_profile_id: basis-profile-id
basis_profile_version: version
basis_type: operator-specific-type
basis_id: basis-id-or-null
basis_instance_id: concrete-basis-instance-id-or-null
candidate_member_refs: governed-reference-list
admitted_member_refs: governed-reference-list
excluded_members:
  - member_ref: governed-reference
    exclusion_reason: controlled-reason
component_mask: operator-specific-or-null
gate_record_id: gate-id-or-null
native_observation_refs: governed-reference-list
transformation_id: transformation-id-or-null
transformation_version: version-or-null
transformation_parameters_ref: governed-reference-or-null
known_information_loss: declared-loss-list
raw_method_result: typed-raw-result-or-null
display_policy_id: display-policy-id-or-null
display_policy_version: version-or-null
display_value: rounded-or-formatted-value-or-null
display_rounding_rule: declared-rule-or-null
evidence_refs: governed-reference-list

created_at: timestamp
evaluator_id: evaluator-id
evaluator_version: version
provenance_record_id: provenance-id
```

Validation rules:

- `result_status = numeric` requires a finite `result_value in [0,1]`;
- a non-numeric status requires `result_value = null`;
- `status_reason` does not replace the common result status;
- one stable or explicitly provisional `source_entity_id` is resolvable;
- `source_attribution_status` records whether attribution is confirmed or
  provisional under a controlled status vocabulary;
- `emitting_entity_id` is populated only when emission is established;
- the concrete admitted basis and every exclusion remain reconstructible under
  the declared basis profile;
- a transformation never overwrites its native observation or raw result;
- `display_value` is derived from the raw method result and never enters Z
  assembly as an operand;
- every coordinate record is immutable or versioned after use in a Z record.

## 3. Z assembly record

Recommended record:

```yaml
z_record_id: immutable-id
z_method_version: "3.51"

target_event_id: event-id
source_entity_id: stable-or-provisional-source-id
source_attribution_status: confirmed-or-controlled-provisional-status
emitting_entity_id: entity-id-or-null
trajectory_id: trajectory-id
global_event_index: integer
local_trajectory_index: integer

coordinate_order: [K, S, O, D, I]
coordinate_record_ids:
  K: id
  S: id
  O: id
  D: id
  I: id

status_vector: [status_K, status_S, status_O, status_D, status_I]
numeric_availability_mask: [0-or-1, 0-or-1, 0-or-1, 0-or-1, 0-or-1]

identity_gate: true-or-false
identity_gate_reason: controlled-reason-or-null
complete_gate: true-or-false

complete_z_value: [K, S, O, D, I]-or-null
z_state: complete | not_complete | assembly_error

machine_object_ref: governed-reference
assistive_interpretation_ref: governed-reference-or-null
governance_display_ref: governed-reference-or-null

created_at: timestamp
assembler_id: evaluator-id
assembler_version: version
provenance_record_id: provenance-id
```

`assembly_error` is not a Layer-1 coordinate status. It means the proposed
coordinate set did not satisfy the Z identity contract.
An assembly-error audit record is not a valid method-level `R_Z` record and
must not enter complete, partial, dynamic, window or Hangar calculations.

The three presentation channels remain distinct:

```text
recoverable machine-readable typed Z object
assistive-model interpretation over governed inputs
human/governance display
```

The machine object is primary. An assistive interpretation and a display each
require their own identity, policy/version and reverse links. Neither may
change a coordinate status, impute a value, certify meaning or create action
authority. A rounded display value must never be read back as a calculation
operand.

## 4. Status mapping and reasons

Common statuses:

```text
numeric
not_selected
not_observable
not_applicable
```

Examples of retained reasons:

```text
reference_space_not_exposed
expected_requirement_set_empty
availability_relation_unobservable
mandatory_component_unavailable
insufficient_structural_basis
static_baseline_missing
detector_unavailable
profile_not_selected
```

Implementation failures are not automatically operator statuses:

```text
profile_missing
profile_incompatible
record_corrupt
identity_mismatch
calculation_error
```

Resolve them under a declared error policy. Do not convert an error into zero,
`not_applicable` or `not_observable` merely to complete a vector.

## 5. Assembly data flow

```text
1. Resolve one target-event identity.
2. Fetch exactly one final static result record for each operator.
3. Validate coordinate-record schemas and value/status consistency.
4. Validate same target, source, trajectory and local index.
5. Order records as K, S, O, D, I.
6. Construct T_Z from common statuses.
7. Derive A_Z from T_Z.
8. Open complete gate only when identity passes and A_Z = (1,1,1,1,1).
9. Store complete numeric Z only when the gate is open.
10. Store the typed Z record in every valid assembly case.
11. Construct a partial projection only under an explicit projection profile.
12. Evaluate comparability before Delta, norms, windows or Hangar derivation.
```

Reference pseudocode:

```python
COORDINATE_ORDER = ("K", "S", "O", "D", "I")
COMMON_STATUSES = {
    "numeric",
    "not_selected",
    "not_observable",
    "not_applicable",
}


def assemble_z(target_identity, coordinate_records, assembler_profile):
    ordered = []
    for operator_id in COORDINATE_ORDER:
        record = require_exactly_one_final_result_record(
            coordinate_records,
            operator_id,
        )
        validate_coordinate_record(record)
        ordered.append(record)

    identity_result = validate_common_identity(target_identity, ordered)
    if not identity_result.ok:
        return ZAssemblyError(
            reason=identity_result.reason,
            coordinate_record_ids=[r.id for r in ordered],
        )

    status_vector = tuple(record.result_status for record in ordered)
    if any(status not in COMMON_STATUSES for status in status_vector):
        return ZAssemblyError(reason="invalid_common_status")

    numeric_mask = tuple(
        1 if status == "numeric" else 0
        for status in status_vector
    )

    complete = numeric_mask == (1, 1, 1, 1, 1)
    complete_value = None
    if complete:
        complete_value = tuple(record.result_value for record in ordered)
        validate_unit_vector(complete_value, dimension=5)

    return ZRecord(
        identity=target_identity,
        coordinate_record_ids=[r.id for r in ordered],
        status_vector=status_vector,
        numeric_availability_mask=numeric_mask,
        identity_gate=True,
        complete_gate=complete,
        complete_z_value=complete_value,
        z_state="complete" if complete else "not_complete",
        assembler_profile=assembler_profile,
    )
```

The pseudocode is illustrative. It does not prescribe Python or an object
store.

## 6. Partial projection profile

A partial profile should declare:

```yaml
partial_profile_id: p_Z_partial_example_v1
z_method_version: "3.51"
active_coordinate_set: [D, I]
coordinate_order: [D, I]
selection_reason: unknown-signal-observation
require_numeric_for_every_active_coordinate: true
allow_imputation: false
comparability_policy_id: policy-id
norm_policy_id: policy-id
display_label: "partial Z[D,I] diagnostic"
```

Validation:

- `active_coordinate_set` is non-empty and contains only K/S/O/D/I;
- order is explicit and stable;
- every active coordinate is numeric for the evaluated point;
- omitted-coordinate statuses remain attached;
- imputation is disabled for observed v3.51 partial Z;
- downstream consumers must opt into the exact partial-profile ID.

Reference pseudocode:

```python
def project_partial_z(z_record, partial_profile):
    validate_partial_profile(partial_profile)

    values = []
    for operator_id in partial_profile.coordinate_order:
        record = z_record.coordinate_record(operator_id)
        if record.result_status != "numeric":
            return TypedDiagnostic(
                status="not_applicable",
                reason="active_partial_coordinate_not_numeric",
            )
        values.append(record.result_value)

    return PartialZDiagnostic(
        values=tuple(values),
        active_coordinate_set=partial_profile.active_coordinate_set,
        full_status_vector=z_record.status_vector,
        full_numeric_mask=z_record.numeric_availability_mask,
        profile_id=partial_profile.id,
    )
```

## 7. Dynamics and comparability

Recommended comparability record:

```yaml
comparison_id: id
view_type: complete_z | partial_z
partial_profile_id: id-or-null
current_z_record_id: id
predecessor_z_record_id: id
same_source: true-or-false
same_trajectory: true-or-false
local_index_relation: declared-relation
coordinate_profile_compatibility: per-coordinate-map
basis_instance_relation: exact | declared-compatible | incompatible
transformation_compatibility: per-coordinate-map
status_compatibility: per-coordinate-map
scale_compatibility: true-or-false
comparability_status: comparable | incomparable
comparability_reason: controlled-reason
```

Reference pseudocode:

```python
def delta_complete_z(current, predecessor, comparison_profile):
    cmp = compare_z_records(current, predecessor, comparison_profile)
    if not cmp.comparable:
        return TypedDiagnostic(
            status="not_applicable",
            reason=cmp.reason,
        )
    if not current.complete_gate or not predecessor.complete_gate:
        return TypedDiagnostic(
            status="not_applicable",
            reason="complete_z_required",
        )
    return vector_subtract(
        current.complete_z_value,
        predecessor.complete_z_value,
    )
```

For partial dynamics, require the same partial profile and coordinate set at
every compared position. Never take the intersection after seeing the data
unless that intersection policy was declared before evaluation and the result
is labeled as a separate diagnostic profile.

## 8. Norm implementation

For a finite difference vector `delta` of declared dimension `d > 0`:

```python
def normalized_l1(delta):
    require_nonempty_finite_vector(delta)
    return sum(abs(x) for x in delta) / len(delta)


def normalized_l2(delta):
    require_nonempty_finite_vector(delta)
    return sqrt(sum(x * x for x in delta)) / sqrt(len(delta))
```

For complete Z, `d = 5`. For partial Z, `d = |M|` and the result stores M.
Do not compare norms produced under different dimensions or masks without a
separately justified comparison profile.

Raw and normalized values should be stored separately:

```text
drift_l1_raw
drift_l1_normalized
drift_l2_raw
drift_l2_normalized
dimension
active_coordinate_set
comparison_profile_id
```

## 9. Status-transition record

Recommended categorical record:

```yaml
status_transition_id: id
trajectory_id: trajectory-id
current_z_record_id: id
predecessor_z_record_id: id
transitions:
  K: [previous-status, current-status]
  S: [previous-status, current-status]
  O: [previous-status, current-status]
  D: [previous-status, current-status]
  I: [previous-status, current-status]
```

Examples:

```text
not_observable -> numeric    newly observable basis
not_selected   -> numeric    changed selection profile
numeric        -> not_applicable changed applicability conditions
```

These are categorical changes. They are not numeric drift from or to zero.

## 10. Window and Hangar implementation

For a joint complete Z window:

1. select one source trajectory and window profile;
2. select records with complete Z and compatible constitutive profiles;
3. use the same selected positions for all five coordinate aggregates;
4. retain `complete_rate_Z` and the excluded-status distribution;
5. keep static, Delta and Delta2 sets separate;
6. record aggregation functions and minimum sample sizes.

Numeric coverage rates require `total_position_count > 0`. For an empty or
invalid window, return a typed non-numeric window result and leave numeric rate
fields null; never evaluate `0/0` or manufacture zero coverage.

Recommended derived window-object record:

```yaml
window_result_id: immutable-id
trajectory_id: trajectory-id
window_profile_id: profile-id
window_profile_version: version
window_kind: event | time | declared-other
boundary_rule: declared-rule
aggregation_order: derive_then_aggregate | aggregate_then_derive
candidate_member_ids: ordered-id-list
included_member_ids: ordered-id-list
excluded_members:
  - member_id: id
    exclusion_reason: controlled-reason
status_partitions: controlled-partition-map
total_position_count: integer
complete_z_count: integer
complete_z_rate: number
minimum_numeric_count: integer
minimum_count_decision: pass | fail | not_applicable
numeric_count_by_coordinate: {K: n, S: n, O: n, D: n, I: n}
numeric_rate_by_coordinate: {K: r, S: r, O: r, D: r, I: r}
status_distribution_by_coordinate: per-coordinate-map
aggregator_id: arithmetic_mean
aggregator_version: version
result_status: numeric | not_selected | not_observable | not_applicable
member_z_record_refs: governed-reference-list
derived_view_refs: governed-reference-list
provenance_record_id: provenance-id
```

The two v3.51 orders are not aliases:

```text
derive_then_aggregate:
  derive one result from each eligible complete Z,
  then aggregate the per-state results

aggregate_then_derive:
  aggregate one shared eligible set of complete Z vectors,
  then derive results from that aggregate Z
```

The transparent v3.51 reference profile is `strict_integrity_v351` with a
named arithmetic aggregator. Event/time, overlapping, median/quantile/robust,
distributional, semantic/episodic, change-point and
`partition_preserving_bounded_tolerance` (`PPWA-bounded`) profiles require
separate later validation. They must not be silently simulated by changing the
member set or status handling.

`Delta Z`, `Delta2 Z`, path length, per-state aggregation and window-to-window
difference remain different operations. Every result stores the operation and
operand order that produced it.

For Hangar:

- complete Z points form a five-dimensional collection;
- partial points are grouped by exact mask/status pattern and profile;
- zero-filling, mean-filling or silent projection into five dimensions is
  forbidden;
- every point links back to its canonical Z record and coordinate records;
- a distribution over window aggregates is distinct from an event-level point
  cloud.

## 11. Migration and v3.51 conformance classes

Legacy records may contain only:

```text
Z_t
A_Z(t)
turn_index t
```

Migration must not invent lost status reasons.

Recommended mapping:

```text
A_X = 1 and finite value -> tau_X = numeric
A_X = 0                  -> tau_X = legacy_non_numeric_unspecified
```

`legacy_non_numeric_unspecified` is a migration-only state outside the common
new-evaluation domain. It requires historical provenance and must not be
silently mapped to `not_applicable`, `not_observable` or `not_selected`.

For each legacy record:

- map `t` to event/source/trajectory identity where evidence exists;
- preserve unresolved identity as a migration failure;
- retain the original mask and values;
- do not label a record complete unless all five finite values and identities
  are verifiable;
- keep legacy and current profile families non-comparable unless an explicit
  bridge is validated.

Classify the resulting record or import attempt as one of:

```text
v351_conformant
legacy_reconstructible
legacy_partially_reconstructible
legacy_noncomparable
```

`reconstruction_pending` is a workflow state for unresolved evidence, not a
fifth conformance class and not permission to invent missing identity, basis,
status or provenance. `not v3.51 conformant` does not mean worthless or
invalid; it limits the comparisons and claims the record supports.

## 12. Human-chatbot record example

```yaml
target_event_id: chatbot-event-42
source_entity_id: chatbot-B
source_attribution_status: confirmed
emitting_entity_id: chatbot-B
trajectory_id: trajectory-B
global_event_index: 42
local_trajectory_index: 17
coordinate_order: [K, S, O, D, I]
status_vector:
  [numeric, numeric, not_observable, numeric, numeric]
numeric_availability_mask: [1, 1, 0, 1, 1]
complete_gate: false
complete_z_value: null
z_state: not_complete
coordinate_reasons:
  O: reference_space_not_exposed
```

Permitted display:

```text
typed Z record: valid, not complete
partial Z[K,S,D,I]: available under named diagnostic profile
```

Forbidden display:

```text
Z = (K,S,0,D,I)
canonical IK computed after silent renormalization
```

## 13. Unknown-signal record example

```yaml
target_event_id: signal-group-9
source_entity_id: source-U
source_attribution_status: provisional-observed-source
emitting_entity_id: null
trajectory_id: trajectory-U
global_event_index: 109
local_trajectory_index: 9
status_vector:
  [not_observable, not_observable, not_applicable, numeric, numeric]
numeric_availability_mask: [0, 0, 0, 1, 1]
complete_gate: false
complete_z_value: null
z_state: not_complete
```

A partial D/I trajectory may be valuable. It remains a declared two-coordinate
diagnostic and does not establish full state, meaning or relation.

## 14. Minimum conformance tests

### 14.1 Identity and assembly

- reject mixed target-event IDs;
- reject mixed source or trajectory IDs;
- reject duplicate or missing coordinate records;
- reject non-canonical coordinate order in canonical serialization;
- accept explicitly provisional source identity when consistently declared
  with its attribution status;
- reject a populated emitting entity when emission has not been established.

### 14.2 Status and values

- accept finite numeric values only in `[0,1]`;
- reject numeric status with null or non-finite value;
- reject non-numeric status with a stored numeric value;
- verify `A_Z` is derived exactly from `T_Z`;
- verify distinct non-numeric statuses produce the same mask bit without losing
  their typed status.

### 14.3 Complete and partial views

- open complete gate only for five numeric aligned records;
- never zero-fill a non-numeric coordinate;
- require explicit non-empty M for partial projection;
- reject partial view when one active coordinate is non-numeric;
- prevent partial Z from entering canonical IK without a separately named
  reduced projection profile.

### 14.4 Dynamics and norms

- reject cross-source predecessor comparison;
- reject incompatible operator profiles;
- require complete comparable states for complete Delta Z;
- require one fixed M for partial Delta and Delta2;
- verify L1 and L2 normalization denominators use 5 or declared `|M|`;
- return `not_applicable` for empty comparison dimension.

### 14.5 Window and Hangar

- complete joint aggregation uses one shared complete subset;
- reject a numeric coverage-rate calculation for an empty window;
- coordinate-wise differing subsets are labeled diagnostic;
- coverage and status distributions are retained;
- partial Hangar points are stratified by exact mask/status profile;
- canonical record references survive every derived view.
- a window object has an identity distinct from every member state;
- candidate, included and excluded members plus reasons are retained;
- `derive_then_aggregate` and `aggregate_then_derive` produce separately
  identified results even when a linear special case yields equal numbers;
- no window aggregate is written back as a participant's canonical Z state;

### 14.6 Layer boundaries

- removing B leaves A's typed and complete Z records unchanged;
- role reversal does not rewrite entity identity;
- Z consumes but does not redefine Layer-1 values;
- no Z routine defines IK, R0, IK_rel or R-family semantics;
- relational pairing requires explicit `j` and `pi(j)` outside Z assembly.

### 14.7 Representation and migration

- raw method results and display values remain separately stored or
  reproducible under identified policies;
- a rounded display never re-enters a calculation as the raw operand;
- assistive interpretations retain governed inputs and cannot modify Z;
- every imported record receives an explicit migration/conformance class;
- unresolved provenance remains unresolved rather than reconstructed as fact.

## 15. Privacy, retention and release boundary

Separate retention policies may apply to raw events, operator bases,
coordinate records, typed Z records, partial projections, trajectories and
Hangar views. Status patterns and profile IDs may reveal access or capability
conditions. Hashes and embeddings may remain identifying.

Store only what the declared audit purpose requires. Deletion of raw material
must not be disguised as continuing direct observability.

Publication of this companion would provide conditional reference guidance
subordinate to the released Z method. It would not approve Patrick
implementation alignment, deployment architecture, thresholds, database
choices or UI behavior. Independent runtime-conformance evidence remains
required.
