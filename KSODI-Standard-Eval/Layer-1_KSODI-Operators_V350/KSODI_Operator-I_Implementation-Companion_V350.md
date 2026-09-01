# KSODI Operator I0 v3.50 - Implementation Companion

This file provides conditional implementation guidance; it is not the
canonical method definition or an executable production implementation.

Canonical method: [`KSODI_Operator-I_Observable-Information-Impulse_V350.md`](./KSODI_Operator-I_Observable-Information-Impulse_V350.md).

## 0. Authority and Alignment Boundary

This file operationalizes the adjacent canonical method. It may define storage mappings, retrieval proxies, data flow, pseudocode, configuration and tests. It must not redefine Operator I's semantic question, measurement basis, applicability, static formula, source identity or layer boundary.

The mappings below illustrate a conversation- and retrieval-oriented profile.
They do not make Human–Chatbot interaction, text, embeddings or retrieval the
canonical observation object. Other carriers and application profiles may use
different implementations while preserving the same method invariants,
identities, applicability states and provenance discipline.

If this companion and the canonical operator disagree, the disagreement must remain visible and the canonical method controls until joint review resolves it.

## 1. Index and Record Discipline

```text
n   = global observable event-stream index
k_A = local position inside trajectory A
k_B = local position inside trajectory B
j   = declared relational pairing index
```

Implementation records may also store timestamps, but a timestamp must not replace these identities or create an implicit cross-entity predecessor. Every predecessor used for `C_seq,I`, `Delta I` or `Delta2 I` is source-local and recoverably referenced.

## 2. Storage Invariant

For every computed I value, store or recoverably reference:

- `conversation_id`;
- `event_id`;
- `source_entity_id`;
- `source_attribution_status`;
- `emitting_entity_id`, if established;
- `trajectory_id`;
- `trajectory_index`;
- `global_event_index`;
- `target_event_id`;
- `context_event_ids`;
- `exchange_id` and `reply_to_event_id`, when applicable;
- `operator_profile_id`;
- `reference_space_id` for the static I value;
- predecessor `event_id` where `C_seq,I` is computed;
- predecessor evaluation IDs and both reference-space provenance records where
  `Delta I` or `Delta2 I` is computed;
- embedding, retrieval, preprocessing and Observer versions;
- component values and applicability flags;
- `operator_result_status` in
  `{numeric, not_selected, not_observable, not_applicable}`;
- final static I value only when `operator_result_status = numeric`;
- controlled status reason and processing status;
- where computed, separately named diagnostic values;
- timestamps and temporal visibility boundary.

Binding rule:

> Every static I value is attributed to one explicitly identified target event
> and one monadic trajectory. `C_seq,I`, `Delta I` and `Delta2 I` remain
> anchored at the current target event while recoverably referencing every
> required comparable predecessor. A later relational comparison remains a
> separately defined construct and does not become an I mutation.

A later separation is not reliable. Once distinguishable events or trajectories are aggregated before operator formation, the original monadic I states cannot be mathematically reconstructed from the aggregate alone.

## 3. Conditional Identity and Reference Mapping

A conversation-oriented implementation may map the canonical identities to:

| Field | Function |
| --- | --- |
| `conversation_id` / `thread_id` | declared interaction scope |
| `event_id` / `target_event_id` | unique contribution and evaluation target |
| `source_entity_id` | stable or explicitly provisional source identity used for attribution |
| `source_attribution_status` | provenance state of the current attribution |
| `emitting_entity_id` | confirmed emitting entity, only when established |
| `trajectory_id` | monadic trajectory of the attributed source |
| `trajectory_index` | local position within that trajectory |
| `context_event_ids` | visible context considered during evaluation |
| `exchange_id` / `reply_to_event_id` | optional pairing metadata; not a monadic merge |
| `global_event_index` | chronological order across all visible events |
| `operator_profile_id` | versioned I profile and parameters |
| `reference_space_id` | versioned I-baseline construction |
| `embedding_profile_id` | vector-profile model, version and preprocessing |

Under a Human–Chatbot or retrieval-oriented implementation, visible candidate
material `V_A(k_A)` may include declared system, developer, application or task
instructions, retrieved elements, files, memory or visible context. Symbols
such as `SP`, `DP`, `AP`, `TP`, `RET`, `FILES` and `MEMORY` are implementation
mappings only. Every element still requires selection, admissibility and
evaluator visibility under `p_I` before it enters `Ref_A(k_A)`.

## 4. Conditional Retrieval Implementation Profile

An implementation may use an auditable retrieval proxy when a non-empty,
visible and admissible retrieval subset exists and the target representation
is itself applicable under the vector profile:

```text
RET_adm,A(k_A)
= {d in RET_r |
   d is visible to the evaluator
   and d is admitted by p_I
   and emb(d) is finite
   and norm(emb(d)) > 0}

G_proxy_ret,A(k_A)
= clip(
    (1 - max_{d in RET_adm,A(k_A)} cos(emb(e_A(k_A)), emb(d))) / 2,
    0,
    1
  )
```

**Set semantics.** `RET_adm,A(k_A)` contains only retrieval elements that are
simultaneously visible, admitted and vector-applicable. Membership in the raw
retrieval result does not make an element admissible.

The retrieval state must distinguish at least:

```text
retrieval_proxy_status in {
  retrieval_missing,
  retrieval_not_requested,
  retrieval_unavailable,
  retrieval_empty,
  retrieval_inadmissible,
  retrieval_admissible_available
}
```

| State | Minimum implementation meaning |
| --- | --- |
| `retrieval_missing` | the operation record or provenance needed to reconstruct its state is absent |
| `retrieval_not_requested` | the declared retrieval operation was not invoked |
| `retrieval_unavailable` | retrieval was required or requested, but the operation, channel or result was unavailable |
| `retrieval_empty` | a completed retrieval operation returned no candidate elements |
| `retrieval_inadmissible` | candidates were returned, but none survives visibility, admissibility and vector-applicability checks |
| `retrieval_admissible_available` | at least one candidate enters `RET_adm,A(k_A)` |

For the selected retrieval-backed I profile, map those states to the common
Layer-1 result family without discarding the retrieval reason:

```text
retrieval_missing              -> not_observable
retrieval_not_requested        -> not_applicable
retrieval_unavailable          -> not_observable
retrieval_empty                -> not_applicable
retrieval_inadmissible         -> not_applicable
retrieval_admissible_available -> numeric may open after remaining gates
```

`retrieval_not_requested` does not block a separately selected non-retrieval
profile. The mapping above applies when retrieval is constitutive for the
selected implementation profile.

`RET_r = ∅` (the `retrieval_empty` state) is reserved for a completed
operation with no candidate elements. It must not be used as an
umbrella encoding for missing, not-requested, unavailable or inadmissible
states. A non-empty `RET_r` can still produce
`RET_adm,A(k_A) = empty` under `retrieval_inadmissible`.

When a required retrieval state is missing or unavailable:

```text
G_proxy_ret,A(k_A) = not_observable
```

When required retrieval was not requested, completed empty or produced only
inadmissible candidates:

```text
G_proxy_ret,A(k_A) = not_applicable
```

**Implementation semantics.** `G_proxy_ret` uses the maximum visible admitted retrieval similarity to construct a bounded distance proxy. It is an operational proxy for the conceptual content component, not proof of novelty and not the canonical carrier-neutral definition. The typed retrieval outcome describes a reference operation, not whether communication or an observable signal occurred.

The retrieval-backed formula is:

```text
I_ref,A(k_A)
= eta_ref * G_proxy_ret,A(k_A)
  + (1 - eta_ref) * J_ref,A(k_A)
```

**Formula semantics.** The weighted retrieval profile uses the same convex structure as canonical `I_ref`, substituting an explicitly named proxy for `G_ref`. The proxy profile must remain separately versioned and cannot be compared silently with the conceptual profile.

No missing, not-requested, unavailable, empty or inadmissible retrieval state
activates a direction-only fallback under the canonical retrieval-backed
profile. The reference-dependent `I_ref,A(k_A)` retains the mapped
`not_observable` or `not_applicable` result and its specific retrieval reason;
neither result is numeric zero. If the required admissible basis cannot later
be reconstructed, the value remains non-reconstructable for that event.

An implementation may define a separately named and versioned direction-only
diagnostic, but it must not call that diagnostic `I_ref`, substitute it into
canonical `Z` or imply that missing retrieval information equals directional
information.
## 5. Suggested Data-flow Order

1. Resolve target-event, stable or provisional source attribution and
   trajectory identity; retain an emitting entity separately only when
   established.
2. Resolve the versioned I profile and visible candidate material.
3. Apply selection, admissibility and visibility rules.
4. Evaluate applicability and map the exact reason to the common Layer-1
   result before any numeric component.
5. Compute component values and typed states.
6. Compute canonical static I only under the selected profile.
7. Store optional sequence, drift, mask, Sigma or Hangar diagnostics separately.
8. Preserve all versions, baselines and predecessor references required for comparison.

## 6. Minimum Conformance Tests

- reject an empty or inadmissible baseline as numeric zero;
- reject zero-norm or non-finite vector inputs;
- keep entity A and B records distinguishable inside one interaction;
- select the predecessor by `trajectory_id` and local index, not global adjacency;
- prevent `C_seq,I` from filling the I coordinate of Z;
- prevent missing, not-requested, unavailable, empty, inadmissible and admissible-available retrieval outcomes from collapsing into one state;
- map required missing/unavailable retrieval to `not_observable` and required
  not-requested/empty/inadmissible retrieval to `not_applicable`;
- reject every retrieval-dependent non-numeric state as numeric zero or as evidence that no communication occurred;
- ensure every successful finite static I result emits
  `operator_result_status = numeric`;
- keep profile and calculation failures outside the common operator-result
  family;
- reject a direction-only diagnostic as canonical `I_ref` or as a canonical `Z` coordinate;
- prevent conceptual and proxy profiles from being compared without an explicit compatibility mapping;
- retain repeated low-I events for source-local recurrence and anomaly views;
- keep static, Delta and Delta2 window records typed separately;
- block any relational claim before explicit pairing, compatible profiles and
  an open numeric canonical complete `R0` gate under the exact required
  profile.

## 7. Release and Reuse Boundary

This companion is publicly released beside the canonical Operator-I method
and remains subordinate to that method and to the public KSODI Implementation
Guardrails. Neither publication nor this erratum makes the conditional
Conversation-/Retrieval profile mandatory, validated for every application or
a required production stack. If this companion and the canonical method
appear to differ, the method controls and the mismatch must be reported rather
than silently normalized.
