# KSODI O Source-Need Gate v3.50

Status: public v3.50 semantic applicability companion, reviewed and released
with the reader-first Operator-O package on 2026-08-25.

Role: operator-specific semantic applicability companion to
[`KSODI_Operator-O_Observable-Grounded-Objectivity_V350.md`](./KSODI_Operator-O_Observable-Grounded-Objectivity_V350.md). The gate is not a sixth
operator, not an O score and not an implementation profile.

Implementation companion:
[`KSODI_Operator-O_Implementation-Companion_V350.md`](./KSODI_Operator-O_Implementation-Companion_V350.md)
(public conditional guidance).

## 0. What the Source-Need Gate Does

The O Source-Need Gate asks one question before Operator O may calculate:

> Is a numeric grounding and traceability evaluation methodologically open for
> this one target event under the declared source-need policy?

The gate separates two different questions:

1. **Applicability:** Is an admitted reference space needed and validly
   available to the evaluator?
2. **Grounding:** If so, how strongly is the target event observably supported
   by and traceable to that reference space?

The gate answers only the first. Operator O answers the second.

Actual use of visible reference material belongs to the O calculation. Do not
invent a gate state such as `source_present_and_used`; presence/admission and
observable use are different questions.

A required source that is missing, invisible or inadmissible must therefore not
be encoded as low O. Likewise, an event for which reference material is not
expected must not receive a neutral invented score such as O=0.5. Both remain
typed non-numeric states.

### 0.1 Minimal Practical Reading

> Before asking “How well grounded is this event?”, first establish whether
> there is a declared, visible, admissible and non-empty reference space against
> which that question can validly be asked.

### 0.2 How to Read This File

- Sections 0-2 explain the gate through two bounded examples and define its
  event identity.
- Sections 3-5 define the policy, state model and ordered decisions.
- Section 6 records downstream Z/IK consequences without making those later
  layers inputs to the gate.
- Sections 7-8 close privacy, formal and implementation boundaries.

## 1. Bounded Application Examples

### 1.1 Human-Chatbot Interaction

```text
entity_A = human or chatbot
target_event = one source-attributed contribution e_A(k_A)
interaction_scope = one declared conversation or exchange
trajectory_A and trajectory_B remain distinguishable
```

One conversation can contain several event-level source-need states:

```text
creative exploration
  -> reference_space_need = not_expected

current factual claim
  -> reference_space_need = required
  -> source_need_reason = reference_required_for_temporal_validity

synthesis from provided documents
  -> reference_space_need = required
  -> source_need_reason = reference_required_for_traceability

fictional writing under declared canon
  -> reference_space_need in {optional, required}, according to policy
```

The phase or task may help select the policy, but each target event receives
its own gate record. A conversation label never replaces target-event,
source-entity or trajectory identity.

If a chatbot used hidden tools or references that are not exposed to the
external evaluator, the external evaluator cannot claim direct grounding.
That condition is `not_visible_to_evaluator`, not O=0.

### 1.2 Unknown Morse-Like Signal

```text
observed_source = provisional source U
target_event = one sign group e_U(k_U)
reference_candidates = codebooks, known signal patterns or documented
                       transmission conventions
trajectory_U remains distinct from any receiver or replying entity
```

Initial signal detection may not expect a reference space. The gate then
returns `not_applicable`; I and D may still evaluate the impulse and its
discernibility.

If a declared reconstruction task requires a codebook but none is available,
the gate returns `not_observable` with
`required_reference_space_missing`. If codebook material exists but the
evaluator cannot inspect it, the result is
`not_visible_to_evaluator`. Only a non-empty, visible and admissible reference
space opens numeric O.

Opening the gate does not prove successful decoding, source identity,
acknowledgement, intent or coupling.

## 2. Canonical Boundary, Event Identity and Indices

For entity or provisionally attributed source A:

```text
entity/source A
  -> emits or is attributed target event e_A(k_A)
  -> Source-Need Gate G_O_sem,A(k_A) evaluates under p_G_O
  -> numeric O may open or a typed non-numeric state follows
  -> if open: O0_A(k_A | Ref_A(k_A), p_O)
```

Entity B is not required for this decision. B may later be an interaction
partner, receiver, sender or source of visible reference material without
becoming part of A's target identity.

The gate belongs to one event:

```text
G_O_sem,A(k_A) = {
  target_event_id,
  source_entity_id,
  source_attribution_status,
  emitting_entity_id, if established,
  trajectory_id,
  trajectory_index,
  global_event_index,
  source_need_policy_id,
  source_need_reason,
  reference_space_need,
  reference_space_id,
  reference_space_available,
  reference_space_visible_to_evaluator,
  reference_space_admissible_for_evaluation,
  reference_space_nonempty,
  o_applicability_state,
  missing_reason,
  operator_result_status,
  status_reason,
  gate_processing_status,
  gate_processing_reason
}
```

Canonical indices:

```text
n    = global event index
k_A  = local position in trajectory A
k_B  = local position in trajectory B
j    = later relational pairing index

pi(j) = (k_A(j), k_B(j))
```

The gate uses `k_A`; it does not infer a shared index from a timestamp,
conversation turn or exchange. `j` and `pi(j)` belong to later relational
work and are included here only to prevent identity collapse.

## 3. Declared Policy and Controlled Reasons

### 3.1 Reference-Space Need

```text
reference_space_need
  in {not_expected, optional, required}
```

The three states answer:

- `not_expected`: the selected policy does not make reference material part
  of this event's O evaluation;
- `optional`: numeric O may open if a valid reference space is available;
- `required`: numeric O can open only if the required reference basis is
  validly present.

This explicit state replaces two ambiguous booleans. A legacy mapping is valid
only as follows:

```text
expected = false, required = false -> not_expected
expected = true,  required = false -> optional
expected = true,  required = true  -> required
expected = false, required = true  -> invalid_gate_state
```

`invalid_gate_state` is a processing reason. It produces no valid common
operator result.

### 3.2 Source-Need Reason

`source_need_reason` explains why the selected need state applies. It does
not explain why numeric O is missing.

Canonical reasons include:

```text
reference_not_required
reference_optional
reference_required_by_task
reference_required_by_policy
reference_required_for_temporal_validity
reference_required_for_traceability
reference_requirement_uncertain
```

Application profiles may add narrower reasons but must map them to a canonical
need state and preserve the versioned policy ID.

### 3.3 Missing Reason

`missing_reason` separately explains why the gate did not produce a numeric
O path:

```text
reference_space_not_expected
reference_space_optional_absent
required_reference_space_missing
reference_space_not_exposed
visible_reference_space_unsuitable
reference_space_empty_after_admission
reference_space_gate_undetermined
```

Never assign:

```text
missing_reason = source_need_reason  [invalid conflation]
```

The first field explains the policy need; the second explains the failed
numeric path.

Invalid source-need policy, inconsistent gate-state combinations, malformed
identity, invalid profile and calculation failure belong to a separate
`gate_processing_reason`; they do not become `missing_reason` values or valid O
results.

## 4. Typed State Model and Consistency

Required state domains:

```text
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
  in {
    numeric,
    not_selected,
    not_observable,
    not_applicable
  }
```

`o_applicability_state` is the O-specific gate result.
`operator_result_status` is the common Layer-1 result type. The mapping is:

```text
numeric_may_open          -> numeric, after successful O calculation
required_basis_unavailable -> not_observable
not_visible_to_evaluator  -> not_observable
gate_condition_undetermined -> not_observable
not_applicable            -> not_applicable
```

The gate-specific state and `missing_reason` remain stored; the common result
type does not erase them.

`not_selected` is not produced by the Source-Need Gate. It is emitted only
when the declared Layer-1 view does not select O. Invalid identity, an invalid
or unresolved source-need policy, an inconsistent gate record, an invalid O
profile or a calculation failure is a processing failure and produces no valid
operator result.

Consistency requirements:

- visibility `true` requires availability `true`;
- admissibility `true` requires available and evaluator-visible material;
- non-empty `true` refers to the admitted `Ref_A(k_A)`, not merely a raw
  retrieval result;
- unavailable, invisible, inadmissible, empty or undetermined reference
  material cannot open numeric O;
- an evidence-dependent `undetermined` gate condition maps to
  `not_observable` and is never coerced to false, zero or a low score;
- an invalid or internally inconsistent state is a processing failure rather
  than an O result;
- `missing_reason = none` when `o_applicability_state = numeric_may_open` or
  when a processing failure prevents any valid gate result; the latter must
  carry a non-empty `gate_processing_reason`.

A raw source or retrieval collection may be non-empty while the admitted
reference space is empty because every candidate is inadmissible. Availability,
admission and non-emptiness must therefore remain distinguishable.

## 5. Ordered Gate Decision

Evaluate in this order:

```text
need
  -> availability
  -> evaluator visibility
  -> admissibility
  -> admitted-space non-emptiness
  -> numeric O may open
```

Once a specific terminal case is reached, downstream fields may remain
`undetermined`; they must not overwrite the specific missing reason.

### 5.1 Invalid or Unresolved Need Policy

```text
if reference_space_need is invalid or undetermined:
  gate_processing_status = failed
  gate_processing_reason = invalid_source_need_policy
  operator_result_status is not emitted
  O0_A(k_A) = no valid operator result
  missing_reason = none
```

The policy must first resolve whether the O question is not expected, optional
or required. An invalid or unresolved policy is not evidence about the target
event and must not be disguised as `not_applicable`.

### 5.2 Reference Not Expected

```text
if reference_space_need = not_expected:
  o_applicability_state = not_applicable
  operator_result_status = not_applicable
  O0_A(k_A) = not_applicable
  missing_reason = reference_space_not_expected
```

This remains non-numeric even if unrelated material happens to be visible.

### 5.3 Optional Reference Space Absent

```text
if reference_space_need = optional
   and reference_space_available = false:
  o_applicability_state = not_applicable
  operator_result_status = not_applicable
  O0_A(k_A) = not_applicable
  missing_reason = reference_space_optional_absent
```

### 5.4 Required Reference Space Missing

```text
if reference_space_need = required
   and reference_space_available = false:
  o_applicability_state = required_basis_unavailable
  operator_result_status = not_observable
  O0_A(k_A) = not_observable
  missing_reason = required_reference_space_missing
```

The finding belongs first to setup, retrieval, tool use, workflow or exposure
policy. It is not O=0.

### 5.5 Reference Space Not Visible to the Evaluator

```text
if reference_space_available = true
   and reference_space_visible_to_evaluator = false:
  o_applicability_state = not_visible_to_evaluator
  operator_result_status = not_observable
  O0_A(k_A) = not_observable
  missing_reason = reference_space_not_exposed
```

The older labels `not_visible_to_evaluator` and
`not_applicable_for_external_observer` remain gate/reason detail; neither is
a fifth common Layer-1 operator-result type.

### 5.6 Visible Reference Space Inadmissible

```text
if reference_space_available = true
   and reference_space_visible_to_evaluator = true
   and reference_space_admissible_for_evaluation = false:
  o_applicability_state = not_applicable
  operator_result_status = not_applicable
  O0_A(k_A) = not_applicable
  missing_reason = visible_reference_space_unsuitable
```

Visibility alone does not grant methodological admission.

### 5.7 Admitted Reference Space Empty

```text
if reference_space_available = true
   and reference_space_visible_to_evaluator = true
   and reference_space_admissible_for_evaluation = true
   and Ref_A(k_A) = empty:
  o_applicability_state = not_applicable
  operator_result_status = not_applicable
  O0_A(k_A) = not_applicable
  missing_reason = reference_space_empty_after_admission
```

This state is distinct from an unavailable reference operation. It also
prevents undefined maximum-similarity, aggregation or representation formulas.

### 5.8 Gate Condition Undetermined

```text
if any required availability, visibility, admissibility or non-emptiness
state is undetermined:
  o_applicability_state = gate_condition_undetermined
  operator_result_status = not_observable
  O0_A(k_A) = not_observable
  missing_reason = reference_space_gate_undetermined
```

A narrower implementation subreason must distinguish which observable gate
condition is unresolved. This rule applies only after a valid source-need
policy exists; invalid policy or inconsistent state combinations remain
processing failures.

### 5.9 Numeric O Evaluation May Open

```text
if reference_space_need in {optional, required}
   and reference_space_available = true
   and reference_space_visible_to_evaluator = true
   and reference_space_admissible_for_evaluation = true
   and Ref_A(k_A) != empty:

  o_applicability_state = numeric_may_open
  gate_processing_status = success
  gate_processing_reason = none
  missing_reason = none
  O0_A(k_A | Ref_A(k_A), p_O) may be evaluated
```

This corrects two possible category errors:

- the same availability condition is not counted twice;
- non-empty admitted `Ref_A(k_A)` is explicit rather than inferred from
  availability.

Opening the gate establishes applicability only. It does not prejudge the O
value.

## 6. Downstream Z and IK Consequence

This section records a consequence of the gate. Z and IK are not inputs to the
gate and do not alter its state.

The Z schema retains five named coordinates:

```text
Z_A(k_A)
= [K_A(k_A), S_A(k_A), O_A(k_A), D_A(k_A), I_A(k_A)]
```

If O is non-numeric, the typed Z assembly record preserves the O status and
its gate-specific reason:

```text
T_Z,A(k_A)
= (status_K, status_S, status_O, status_D, status_I)

status_O in {numeric, not_selected, not_observable, not_applicable}
A_O,A(k_A) = 1 if status_O = numeric, else 0
```

`A_Z` is derived numeric-availability information. It does not replace
`T_Z`, because `not_selected`, `not_observable` and `not_applicable` all map
to zero in the binary mask. If any required coordinate is non-numeric, the
typed Z record remains valid, but complete canonical `Z_A(k_A)` is not
constructed and canonical `IK_A(k_A)` is non-numeric under the Layer-3 result
policy.

A reduced projection may be calculated only through one separately declared,
fixed non-empty coordinate set `M` and its own versioned reduced-axis profile:

```text
Z_A^[M](k_A)       = declared partial Z projection
IK_A^[M](k_A)      = declared reduced IK projection
M                  = fixed for every directly compared position
```

The full `T_Z` and derived `A_Z`, the fixed set `M`, reduced-axis weights,
missing O status, source-need reason, missing reason and policy ID remain
attached. Event-wise active-set generation or automatic weight
renormalization is not part of the current v3.50 contract. `IK^[M]` is never
canonical full IK, complete Z, R0, IK_rel or resonance.

## 7. Edge Cases, Privacy and Governance

An interaction phase may choose a policy for several events, but each event
still receives its own `G_O_sem,A(k_A)`.

Typical Human-LLM policy signals for optional or required references may
include source requests, current claims, legal/regulatory/medical/financial or
safety claims, named documents, tool-required workflows and auditability.
Typical `not_expected` signals may include creative exploration,
brainstorming, translation, rewriting visible material or explicitly
speculative reflection. These are profile hooks, not universal truth rules.

Raw target events, queries, sources, snippets, tool outputs and selection
traces may be sensitive, personal, copyrighted or restricted. Hashes,
embeddings, identifiers, gate states, masks and trajectories may preserve
identifying relationships. Derived data is not automatically anonymous or safe
for longer retention.

Implementations require declared access, retention, deletion and provenance
policies. This gate prescribes no universal retention period.

## 8. Formal Summary and Implementation Boundary

### 8.1 Compact Gate Block

```text
G_O_sem,A(k_A)
= event-bound Source-Need Gate under p_G_O

numeric_may_open
iff reference_space_need in {optional, required}
    and reference_space_available = true
    and reference_space_visible_to_evaluator = true
    and reference_space_admissible_for_evaluation = true
    and Ref_A(k_A) != empty

if numeric_may_open:
  missing_reason = none
  O0_A(k_A | Ref_A(k_A), p_O) may be evaluated
  operator_result_status = numeric after successful calculation
else:
  required basis unavailable, not visible or evidence-undetermined
    -> O0_A(k_A) = not_observable
    -> operator_result_status = not_observable
  basis not expected, optional absent, inadmissible or admitted empty
    -> O0_A(k_A) = not_applicable
    -> operator_result_status = not_applicable
  missing_reason = the matching controlled terminal reason

invalid identity, policy, profile, gate record or calculation
  -> gate_processing_status = failed
  -> gate_processing_reason = controlled failure reason
  -> no valid operator_result_status or O0 value
```

### 8.2 Variable Reference

| Variable or field | Semantic role |
| --- | --- |
| `G_O_sem,A(k_A)` | Event-bound semantic gate record |
| `p_G_O` | Versioned source-need policy |
| `e_A(k_A)` | Source-attributed target event |
| `Ref_A(k_A)` | Admitted reference space for this event |
| `reference_space_need` | Not expected, optional or required |
| `source_need_reason` | Why the selected need state applies |
| `missing_reason` | Why no numeric O path resulted |
| `reference_space_available` | Whether candidate reference material is available |
| `reference_space_visible_to_evaluator` | Whether the evaluator can inspect the required basis |
| `reference_space_admissible_for_evaluation` | Whether visible material may enter this evaluation |
| `reference_space_nonempty` | Whether admitted `Ref_A(k_A)` contains at least one valid element |
| `o_applicability_state` | O-gate state: numeric may open, not applicable, required basis unavailable, not visible or gate condition undetermined |
| `operator_result_status` | Common Layer-1 result: numeric, not selected, not observable or not applicable |
| `gate_processing_status` / `gate_processing_reason` | Separate gate-processing record; a failure produces no valid O result |
| `T_Z,A(k_A)` | Mandatory typed Z coordinate-status vector |
| `A_Z,A(k_A)` | Derived numeric-availability mask; never a replacement for `T_Z` |
| `M` | Fixed declared coordinate set for a partial `Z^[M]` or reduced `IK^[M]` view |
| `IK_A^[M](k_A)` | Separately named reduced downstream projection under its own fixed-axis profile |
| `not_applicable` | O is not expected or no valid admissible basis exists; never numeric zero |
| `not_observable` | Required observable support cannot be inspected |
| `not_visible_to_evaluator` | Gate-specific reason retained when evaluator visibility is absent |

### 8.3 Separate Implementation Companion

Storage mappings, legacy-state conversion, pseudocode, RAG data flow, detector
configuration, test fixtures and Patrick implementation alignment belong in
[Operator O Implementation Companion](./KSODI_Operator-O_Implementation-Companion_V350.md).

The implementation companion may operationalize this gate but must not
redefine its ordered decision, need states, controlled reasons, non-empty
reference requirement or N/A-to-zero prohibition. This gate is publicly
released only as part of the jointly reviewed Operator-O package and remains
subordinate to the canonical method.
