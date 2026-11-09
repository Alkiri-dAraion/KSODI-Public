# KSODI Operator O v3.50 - Implementation Companion

This conditional implementation companion is subordinate to the carrier-neutral
[`KSODI_Operator-O_Observable-Grounded-Objectivity_V350.md`](./KSODI_Operator-O_Observable-Grounded-Objectivity_V350.md) method and the semantic
[`KSODI_Operator-O_Source-Need-Gate_V350.md`](./KSODI_Operator-O_Source-Need-Gate_V350.md).

Scope: one conditional Conversation-/Retrieval-/RAG-oriented implementation
profile plus storage, data-flow, validation and separate diagnostic mappings.
This file is not a sixth operator, not the universal definition of O and not a
mandatory production stack.

## 0. Authority and Alignment Boundary

The method file controls:

- O's observable question;
- target-event and source identity;
- Source-Need applicability;
- carrier-neutral profile contract;
- static output range and typed non-numeric states;
- comparability and source-local movement;
- Sigma/Hangar and relational boundaries.

This companion may operationalize those rules. It may not redefine them.

If method, gate and implementation appear to differ:

1. retain the mismatch visibly;
2. do not silently change a formula or status mapping;
3. record the implementation and method versions;
4. request Anne's semantic decision before alignment or public transfer.

## 1. Required Evaluation and Gate Record

Every attempted O evaluation should preserve or recoverably reference:

```text
evaluation_id
operator_id = O
operator_version
implementation_version

target_event_id
source_entity_id
source_attribution_status
emitting_entity_id, if established
trajectory_id
trajectory_index = k_A
global_event_index = n
context_event_ids

conversation_id
thread_id

exchange_id
reply_to_event_id
receiver_entity_id
role_in_exchange

source_need_policy_id
source_need_reason
reference_space_need
reference_space_id
reference_space_version
reference_space_available
reference_space_visible_to_evaluator
reference_space_admissible_for_evaluation
reference_space_nonempty
o_applicability_state
missing_reason
operator_result_status
status_reason
result_value
processing_status
processing_reason

o_profile_id
o_profile_version
active_component_mask
component_values
component_applicability
o_value, only when operator_result_status = numeric

observer_id
created_at
provenance_record_ids
retention_and_access_policy_id
```

Entity, target event, visible context, trajectory, exchange, reply edge and
reference elements remain distinguishable. Sender and receiver are
exchange-relative roles, not stable entity types.

## 2. Typed Status Handling

Use the semantic gate states exactly:

```text
reference_space_need
  in {not_expected, optional, required}

reference_space_available
  in {true, false, undetermined}

reference_space_visible_to_evaluator
  in {true, false, undetermined}

reference_space_admissible_for_evaluation
  in {true, false, undetermined}

reference_space_nonempty
  in {true, false, undetermined}

o_applicability_state
  in {
    numeric_may_open,
    not_applicable,
    required_basis_unavailable,
    not_visible_to_evaluator,
    gate_condition_undetermined
  }

operator_result_status
  in {numeric, not_selected, not_observable, not_applicable}
```

Map the O-specific gate state to the common Layer-1 result:

```text
numeric_may_open          -> numeric, after successful O calculation
required_basis_unavailable -> not_observable
not_visible_to_evaluator  -> not_observable
gate_condition_undetermined -> not_observable
not_applicable            -> not_applicable
```

`not_selected` is emitted only when the declared Layer-1 view omits O; it is
not a Source-Need Gate outcome. Do not coerce gate states, result states or
implementation failures into numeric O. Malformed identity,
`invalid_source_need_policy`, `inconsistent_gate_state`, `profile_missing`,
`profile_incompatible` and calculation errors are processing failures and
produce no valid common operator status. All remain distinct from `0`.

A completed retrieval that returned no candidates, an unavailable retrieval,
a non-empty raw result whose candidates were all inadmissible and a reference
space hidden from the evaluator are different implementation states. Retain
each gate state and controlled reason beside the mapped common result without
collapsing provenance.

## 3. Conditional Human-Chatbot / RAG Profile

This section instantiates one application profile:

```text
entity_A = human or chatbot application entity
target_event = one source-attributed contribution a_A(k_A)
Ref_A(k_A) = admitted retrieval, document, tool or web material
trajectory_A and trajectory_B remain distinguishable
```

Required profile inputs:

- open Source-Need Gate;
- non-empty admitted `Ref_A(k_A) = {d_1, ..., d_m}`;
- finite non-zero target and reference representations;
- versioned embedding and similarity mapping;
- versioned contribution and sentence segmentation;
- versioned attribution detector;
- explicit component mask, weights, thresholds and missingness rules.

A web or retrieval tool is not automatically an entity merely because it
changes A's reference material. Separate entity or trajectory assignment
requires its own declared implementation profile.

Where policy permits, reference provenance should additionally preserve:

```text
source_identifier
retrieval_timestamp
publication_or_effective_date
query_or_route_id
retrieval_channel_id
snippet_or_full_text_status
access_state
cache_state
freshness_policy_id_and_result
tool_and_connector_version
admission_decision_and_reason
```

The implementation may retain approved derived traces instead of restricted
raw contents, but it must not claim direct evaluator visibility that did not
exist.

## 4. RAG Components and Static Profiles

### 4.1 Global Retrieval Alignment - `A_ret`

For one target contribution:

```text
sim_Ref,A(k_A)
= max_{d_i in Ref_A(k_A)}
    cos(emb(a_A(k_A)), emb(d_i))

A_ret,A(k_A)
= clip(sim_Ref,A(k_A), 0, 1)
```

Semantic reading: the maximum selects the admitted reference element with the
strongest directional similarity to the complete target contribution. Positive
support clipping maps negative cosine values to zero and bounds the result.

What follows: high `A_ret` indicates coarse global thematic proximity to at
least one admitted reference element.

What does not follow: it does not prove local claim support, correct
attribution, truth, causal origin or quality of the reference space. One strong
global match may coexist with unsupported local claims.

An implementation using `(1 + cos)/2`, another similarity function or another
reference aggregation must declare a different versioned profile because the
semantics change.

### 4.2 Visible Attribution Trace - `B_trace`

Let:

```text
n_sent,A(k_A) = number of valid sentence or claim units
n_attrib,A(k_A) = number of those units with a profile-valid visible
                  attribution trace
```

Each valid unit is counted at most once even when it contains several trace
markers.

Required count bounds:

```text
0 <= n_attrib,A(k_A) <= n_sent,A(k_A)
```

For `n_sent,A(k_A) > 0`:

```text
B_trace,A(k_A)
= n_attrib,A(k_A) / n_sent,A(k_A)
```

For `n_sent,A(k_A) = 0`:

```text
B_trace,A(k_A) = not_applicable
```

Semantic reading: `B_trace` is the share of valid target units carrying a
visible attribution trace under the declared detector. When every valid unit
is attributed, `B_trace = 1`; when none is attributed, `B_trace = 0`.

This replaces the earlier denominator `n_sent + 1`. That smoothing prevented
complete visible attribution from ever reaching 1 and had no declared semantic
justification. The corrected denominator therefore restores the component's
stated proportion semantics. Any future smoothing requires a separately named,
versioned profile and an explicit reason.

Visible traces may include citations, source or document identifiers, declared
derivation markers or references to exposed tool outputs. This is not a style
or writing-quality score.

Migration note:

```text
legacy component symbol B_A(k)
  -> B_trace,A(k_A)
```

The semantic component is retained; the longer symbol prevents collision with
stable Entity B.

### 4.3 Unsupported-Claim Pressure - `P_uns`

For every valid sentence or claim unit `s_r`:

```text
sim_Ref,A(s_r, k_A)
= max_{d_i in Ref_A(k_A)}
    cos(emb(s_r), emb(d_i))

align_Ref,A(s_r, k_A)
= clip(sim_Ref,A(s_r, k_A), 0, 1)
```

For `n_sent,A(k_A) > 0`:

```text
P_uns,A(k_A)
= #{
    s_r :
      align_Ref,A(s_r, k_A) < tau_O
      and no profile-valid attribution trace
  }
  / n_sent,A(k_A)
```

For `n_sent,A(k_A) = 0`:

```text
P_uns,A(k_A) = not_applicable
```

Semantic reading: `P_uns` is the share of local units that fall below the
declared support threshold and lack a visible trace. It is a local pressure
component, not proof that the unit is false or fabricated.

The threshold `tau_O`, segmentation, representation and attribution detector
are constitutive profile choices.

### 4.4 Minimal RAG Profile

```text
p_O_RAG_min = {
  components = [A_ret, B_trace],
  alpha_O >= 0,
  beta_O >= 0,
  alpha_O + beta_O = 1,
  similarity_map = positive_support_clip,
  representation, detector and normalizer versions
}
```

If both mandatory components are applicable:

```text
O_RAG_min,A(k_A)
= clip(
    alpha_O * A_ret,A(k_A)
    + beta_O * B_trace,A(k_A),
    0,
    1
  )
```

The workbench start profile retains:

```text
alpha_O = 0.7
beta_O = 0.3
```

Semantic reading: this convex combination weighs coarse global alignment more
strongly than visible trace coverage while keeping both inspectable.

These weights are versioned workbench start values, not empirical universal
optima.

Historical interpretation aids near `1`, near `0.5` and below `0.4` may be
retained only as profile-bound exploratory labels. They are not universal O
thresholds or governance corridors.

### 4.5 Extended RAG Profile

```text
p_O_RAG_ext = {
  components = [A_ret, B_trace, P_uns],
  alpha_O >= 0,
  beta_O >= 0,
  alpha_O + beta_O = 1,
  gamma_O >= 0,
  tau_O in [0,1],
  similarity map, segmentation, detector and normalizer versions
}
```

If all selected mandatory components are applicable:

```text
O_RAG_ext,A(k_A)
= clip(
    alpha_O * A_ret,A(k_A)
    + beta_O * B_trace,A(k_A)
    - gamma_O * P_uns,A(k_A),
    0,
    1
  )
```

Semantic reading: alignment and visible trace provide positive support; local
unsupported-claim pressure subtracts a separately weighted penalty; clipping
preserves the output range.

`gamma_O = 0` disables the penalty mathematically, but a missing active
`P_uns` component is not thereby made applicable. When the penalty is not
selected, use the minimal profile rather than silently switching component
masks.

The historical workbench start value `gamma_O = 0` therefore records an
inactive penalty, not evidence that unsupported-claim pressure is universally
irrelevant.

Minimal and extended values are not naively interchangeable. Exactly one
declared profile may supply the O coordinate of one concrete Z view.

## 5. Suggested Evaluation Data Flow

```text
1. identify target event, source and trajectory
2. create event-bound Source-Need Gate record
3. evaluate need -> availability -> visibility -> admissibility -> non-empty
4. map the exact valid terminal gate reason to `not_observable` or
   `not_applicable`; stop separately with a processing failure for invalid
   identity, policy or gate state
5. select exactly one versioned O profile
6. validate target/reference representations and detector inputs
7. calculate each selected component with its own applicability
8. validate the selected component mask
9. apply the declared static profile formula
10. clip only where the profile declares clipping
11. on finite success emit `operator_result_status = numeric`, persist
    `result_value in [0,1]`, component values and complete provenance
12. apply comparability before Delta O or Delta2 O
13. construct typed window and Hangar views only from admitted records
```

Do not infer numeric O before Step 4. Do not silently fall back from the
extended to minimal profile after a component failure.

## 6. Reference-Space Movement and Stability

For one vector-compatible profile, define a versioned non-empty reference-space
representation `emb_Ref,A(k_A)`.

Only when consecutive representations are finite, non-zero and explicitly
comparable:

```text
RefDrift_O,A(k_A)
= clip(
    (1 - cos(
      emb_Ref,A(k_A - 1),
      emb_Ref,A(k_A)
    )) / 2,
    0,
    1
  )
```

Otherwise:

```text
RefDrift_O,A(k_A) = not_applicable
```

Semantic reading: the affine cosine-distance map places directional
reference-space movement in `[0,1]`.

Boundary: this diagnostic may explain movement in O but does not modify,
penalize or retroactively reweight O. Another carrier may require a different
profile-defined reference movement measure.

A window-level `P_ref,A(W_A)` may be implemented only under its own versioned
stability definition. It is not inserted into every Hangar point.

## 7. Separate Reference-Element Evaluation

A reference element `d_i` may be selected as a new target object and receive
its own complete applicable KSODI evaluation:

```text
Z_source(d_i)
= [
    K_source_i,
    S_source_i,
    O_source_i,
    D_source_i,
    I_source_i
  ]

IK_source(d_i)
= w_source dot Z_source(d_i)

w_source,r >= 0
sum_r w_source,r = 1
```

The projection is valid only for a complete applicable source-element Z and a
declared source-evaluation weight profile.

This is a separate Layer-1-to-Layer-3 evaluation pipeline for `d_i`. It is not
an input component of the original target event's O calculation and does not
open its Source-Need Gate.

Consequently:

- a strong reference element may be used poorly by the target event;
- a weak reference element may be followed faithfully;
- a target can be grounded relative to a poor reference space;
- a target can remain ungrounded despite strong admitted sources.

For a non-empty reference space:

```text
Ref_A_app(k_A)
= {
    d_i in Ref_A(k_A) :
      Z_source(d_i) is complete and applicable
      and IK_source(d_i) is applicable
  }
```

Only when `|Ref_A_app(k_A)| > 0`:

```text
IK_sourceSigma,A(Ref_A(k_A))
= Agg_source({
    IK_source(d_i) :
      d_i in Ref_A_app(k_A)
  })

applicability_rate_source,A(Ref_A(k_A))
= |Ref_A_app(k_A)| / |Ref_A(k_A)|
```

Otherwise both diagnostics are `not_applicable`.

The name `IK_sourceSigma` denotes a separate aggregation over complete
source-element projections. It is not the target event's canonical IK and not
a relational value.

## 8. Window and Hangar Implementation

For every selected O window, preserve separate applicable sets for:

```text
static O0 values
Delta O values
Delta2 O values
```

Do not combine them into one untyped scalar. Each empty applicable subset
produces a field-level `not_applicable`; if all selected subsets are empty,
the complete structured view is `not_applicable`.

A Hangar view is reconstructed from canonical event/evaluation records. It does
not replace those records, merge A and B or become participant-visible context
unless a later declared architecture explicitly exposes it.

## 9. Minimum Conformance Tests

### 9.1 Identity and Monadic Isolation

- Remove Entity B; applicable `O0_A(k_A)`, `Z_A(k_A)` and
  `IK_A(k_A)` remain defined from A's own valid basis.
- Reverse sender/receiver roles in a later exchange; stable entity and
  trajectory identities remain unchanged.
- Verify that `k_A-1` never selects B or the preceding global event.
- Verify that reference material from B does not become part of A's target
  event.

### 9.2 Gate and Missingness

- `not_expected` never produces numeric O.
- optional-absent and required-missing retain different reasons.
- optional-absent maps to `not_applicable`; required-missing maps to
  `not_observable`.
- invisible material produces gate state `not_visible_to_evaluator` and
  common operator status `not_observable`.
- evidence-dependent undetermined gate conditions map to `not_observable`
  with their exact reason.
- invalid or unresolved source-need policy and inconsistent gate records are
  processing failures and produce no operator status.
- visible but inadmissible material does not open O.
- a raw non-empty retrieval with empty admitted subset remains non-numeric.
- no N/A state is stored as 0 or 0.5.

### 9.3 Numeric Components

- finite/non-zero representation guards precede cosine calculations.
- empty `Ref` never reaches a maximum-similarity expression.
- `0 <= n_attrib <= n_sent`.
- `B_trace = 1` when every valid unit is attributed.
- `B_trace = 0` when no valid unit is attributed and `n_sent>0`.
- `n_sent=0` makes `B_trace` and `P_uns` non-applicable.
- minimal weights are non-negative and sum to one.
- all applicable profile outputs remain in `[0,1]`.
- every successful finite final O result emits
  `operator_result_status = numeric` and a numeric `result_value`.

### 9.4 Profile and Comparability

- minimal and extended profiles are never silently substituted.
- component-mask changes remain visible.
- representation, detector, threshold or reference-policy change closes direct
  comparability unless an explicit compatibility mapping exists.
- Delta and Delta2 use only same-trajectory applicable comparable records.

### 9.5 Layer and Relation Boundaries

- no Layer-1 O input depends on Z, IK, R0, IK_rel or an R-family result.
- source-element Z/IK evaluation remains a separate downstream pipeline.
- side-by-side O display does not become dyadic O.
- no operator-only route is reported as complete Z, IK_rel or resonance.
- every current relational claim remains behind an open numeric canonical
  complete R0 gate under the exact required profile.

### 9.6 Template Acceptance Tests

Released package result:

- **Monadic-independence / removal test: pass.** Removing Entity B leaves
  applicable `O0_A(k_A)`, complete `Z_A(k_A)` and monadic `IK_A(k_A)` defined
  from A's own declared bases.
- **Role-reversal test: pass.** Sender/receiver reversal changes exchange
  roles, not stable entity or trajectory identity.
- **Application-substitution test: pass.** Human-Chatbot and unknown
  Morse-like signal examples use the same canonical O question while declaring
  different reference, segmentation and detector profiles.
- **Layer-dependency test: pass.** O uses no Z, IK, R0, IK_rel or R-family
  result as an input. Source-element Z/IK remains a separate downstream
  diagnostic pipeline.
- **Provenance test: pass.** Target event, source identity, context events,
  trajectory, exchange, reply edge and reference elements remain distinct.
- **Index-identity test: pass.** Global `n`, local `k_A/k_B` and relational
  `j`/`pi(j)` are distinguishable; no shared timestamp creates a predecessor.

## 10. Privacy, Retention and Observer/Controller Separation

Raw target events, reference contents, queries, web pages, tool outputs,
embeddings, identifiers, gate states, component values, deltas, windows and
Hangar distributions may remain personal, sensitive, copyrighted or
restricted.

Derived data is not automatically anonymous. Declare retention, access,
deletion, reuse, provenance and re-identification controls for raw and derived
records.

The Observer evaluates and reports. It does not authorize retrieval, alter the
target, steer the attributed source or trigger action by itself. Any future
Controller requires separate governance corridors, feedback policy, authority
and audit trail.

## 11. External Implementation Comparison Boundary

No external implementation is presumed to match this companion. Before
implementation alignment is claimed, declare and compare the selected code
baseline against:

- stable/provisional source identity;
- canonical `n`, `k_A/k_B` and `j` indices;
- event-bound Source-Need Gate state;
- distinct need and missingness reasons;
- explicit admitted-reference non-emptiness;
- corrected `B_trace = n_attrib/n_sent` formula;
- exact RAG similarity map;
- profile/component-mask handling;
- same-trajectory comparability;
- typed Sigma/Hangar views;
- separation of source-element diagnostics from O;
- mandatory `T_Z` versus derived `A_Z`, complete canonical IK versus one
  separately declared fixed-axis `IK^[M]`, and prohibition of event-wise
  active-set renormalization;
- data-governance and Observer/Controller boundaries.

Record verified software behavior, current method requirement, mismatch and
proposed change separately. Implementation behavior does not become method
canon by inference.

## 12. Publication Boundary

This companion is publicly released beside the carrier-neutral method and the
semantic Source-Need Gate. It remains conditional and visibly subordinate and
must not be presented as the only valid O implementation or a mandatory
production stack. Publication does not convert its Conversation-/Retrieval-/
RAG profile, detector choices or workbench start weights into universal O
semantics.
