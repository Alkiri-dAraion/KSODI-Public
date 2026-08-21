# KSODI O Source-Need Gate v3.50

Status: public v3.50 companion note for `KSODI_Operator-O_Observable-Grounded-Objectivity_V350.md`; private workbench origin retained.

Implementation status: method note only. This file is not an implementation profile and does not define a production detector by itself.

## 1. Purpose

The O-operator needs a semantic gate before answer-level grounding is interpreted.

The gate decides whether a declared reference space is expected, optional or not required for the current evaluation unit.

Without this gate, the Observer cannot distinguish between:

- no source needed
- source optional
- source required but missing
- source present but not visible to the Observer
- source present but unsuitable
- source present and used

This distinction is necessary because a conversation may move through phases where sources are unnecessary, and later through phases where sources are required for traceability, auditability or current factual accuracy.

## 2. Minimal Gate Variables

Recommended semantic gate state per evaluation unit:

```text
G_O_sem(t) = {
    reference_space_expected,
    reference_space_required,
    reference_space_available,
    reference_space_visible_to_observer,
    source_need_reason,
    source_need_policy_id
}
```

Possible values:

```text
reference_space_expected in {true, false}
reference_space_required in {true, false}
reference_space_available in {true, false}
reference_space_visible_to_observer in {true, false}
```

`source_need_reason` should be a short controlled label where possible.

Example labels:

```text
none_expected
creative_or_fictional_mode
brainstorming_mode
user_requested_sources
current_factual_claim
legal_or_regulatory_claim
medical_or_safety_claim
financial_or_risk_claim
document_grounded_task
tool_required_by_policy
web_verification_required
auditability_required
uncertain_or_contested_claim
```

## 3. Gate Output and O Applicability

The semantic gate precedes `O0`.

Case 1: no reference space expected

```text
reference_space_expected = false
reference_space_required = false
O0 = not_applicable
missing_reason = no_reference_space_expected
```

Interpretation: neutral grey in heatmaps or dashboards. Do not treat as poor grounding.

Case 2: reference space optional but absent

```text
reference_space_expected = false or optional
reference_space_available = false
O0 = not_applicable
missing_reason = reference_space_optional_absent
```

Interpretation: no O-score. Other operators may be projected with an applicability mask.

Case 3: reference space required but absent

```text
reference_space_expected = true
reference_space_required = true
reference_space_available = false
O0 = not_applicable
missing_reason = required_reference_space_missing
```

Interpretation: do not coerce O to `0`. The failure belongs first to setup, tool use, retrieval, workflow or exposure policy. It may be reported as a process / observability issue.

Case 4: reference space available but not visible to the external Observer

```text
reference_space_available = true
reference_space_visible_to_observer = false
O0 = not_applicable_for_external_observer
missing_reason = reference_space_not_exposed
```

Interpretation: the local Agent-Light may have grounded its answer internally, but the external Observer cannot claim direct source-grounding unless source traces, metadata, citations or an approved audit path are exposed.

Case 5: reference space available and visible

```text
reference_space_available = true
reference_space_visible_to_observer = true
O0 may be evaluated
```

Interpretation: answer-level grounding can be evaluated relative to the declared reference space.

## 4. Applicability-Masked Z and IK

When O is not applicable, `Z(t)` remains logically five-dimensional, but the active projection uses an applicability mask.

```text
Z(t)    = [K, S, O, D, I]
mask(t) = [1, 1, 0, 1, 1]
O(t)    = not_applicable
```

Applicability-aware projection:

```text
IK_applicable(t)
= sum_i(mask_i * w_i * Z_i(t)) / sum_i(mask_i * w_i)
```

Required metadata:

```text
applicability_rate(t) = sum(mask_i) / 5
missing_operator = O
missing_reason = source_need_reason
source_need_policy_id = ...
```

This prevents `O = N/A` from being read as `O = 0` or `O = 0.5`.

A dashboard may display O in a neutral grey state, but the numeric `O0` value remains `not_applicable`.

## 5. Conversation-Phase Sensitivity

The gate is evaluated per evaluation unit or conversation phase, not once for the whole conversation.

Example phase pattern:

```text
Phase 1: brainstorming / creative exploration
G_O_sem = no_reference_space_expected
O0 = not_applicable

Phase 2: factual verification requested
G_O_sem = web_verification_required
O0 requires visible reference space

Phase 3: synthesis from provided sources
G_O_sem = document_grounded_task
O0 evaluated against declared source set

Phase 4: fictional writing inside a constructed world
G_O_sem = creative_or_fictional_mode
O0 evaluated only if an internal fictional reference space is declared and relevant
```

The same conversation can therefore contain both O-neutral segments and O-required segments.

## 6. Signals That a Source or Tool Is Needed

A source or tool may be needed when the evaluation unit contains or responds to signals such as:

- explicit request for sources, citations, links or verification
- request for current or recent information
- legal, regulatory, medical, financial, safety or compliance claims
- claim that depends on a named external document, policy, repository, ticket, dataset or web page
- comparison of current products, prices, schedules, roles, standards or regulations
- request to check whether something is true, updated, changed or still valid
- internal policy requiring a tool or source for auditability
- uncertainty or contestability that cannot be resolved from the visible local context

A source may not be needed when the task is clearly:

- creative writing
- fictional worldbuilding
- brainstorming
- translation
- rewriting user-provided text
- summarizing text already fully provided in context
- personal reflection without factual verification need
- explicitly marked as speculative or conceptual

These rules are policy hooks. They must be versioned per implementation profile.

## 7. Agent-Light and External Observer Boundary

Inside a local Agent-Light workflow, the agent may act as a first semantic gate:

```text
Should I answer from current context?
Should I retrieve?
Should I search the web?
Should I ask for a source?
Should I mark O as not_applicable?
```

The external Observer cannot automatically see that internal gate unless the implementation exposes gate metadata, tool logs, source lists, citations or derived traces.

Therefore:

- Agent-Light may decide source need operationally.
- The external Observer may evaluate only visible traces.
- A later audit path may reconstruct more, if explicitly approved.
- Hidden tool traces or raw source contents must not be assumed by the Observer.

## 8. Privacy and Retention Boundary

Because source-need gating may involve web pages, user queries, tool outputs, snippets or internal source-selection traces, retention must be explicit.

Prefer retaining:

- gate status
- source_need_reason
- source_need_policy_id
- source IDs or hashes where appropriate
- visibility flags
- applicability masks
- derived vectors or scores
- timestamps and configuration IDs

Avoid retaining long-term unless explicitly justified:

- full user queries
- full raw source text
- full web pages
- unnecessary snippets
- hidden intermediate reasoning
- sensitive source-selection traces

## 9. Canonical Boundary

This note does not replace `KSODI_Operator-O_Observable-Grounded-Objectivity_V350.md`.

It clarifies the semantic gate that decides when `O0` is applicable and how O-missingness should be interpreted.

Implementation profiles must define their own source-need policy IDs,
visibility rules, retention rules and detector behavior before using this note
operationally.
