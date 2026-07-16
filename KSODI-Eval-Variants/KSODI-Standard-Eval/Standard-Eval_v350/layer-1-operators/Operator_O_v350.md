# KSODI Operator O0 - Observable Grounded Objectivity v3.50

Status: public v3.50 reference release; private canonical workbench origin retained, based on `KSODI_Operator_O_v33.md`, the 2026-07-04 Fable review and the v3.50 glossary line.

Implementation status: not yet verified against Patrick's current Observer / KSODI-Light implementation. Patrick's implementation is known to still reflect the older v3.3 line and must be compared before this file is treated as an implementation profile for the Kubernetes / chatbot Observer stack.

Layer: KSODI Standard-Eval operator. Static `O0` belongs to Layer 1. Operator-level Delta / Delta2, Sigma and Hangar views may observe grounding, traceability and applicability movement over time. Relational feedback and controller logic belong outside the static Layer-1 operator definition.

## 1. Definition

`O0` measures to what extent an answer, signal or response is contextually grounded and traceable relative to an explicit visible reference space.

In the RAG-oriented default case, the visible reference space is the provided retrieval set:

```text
Ref = {d_1, ..., d_m}
```

where `d_i` denotes one visible retrieval document, chunk, tool output or evidence element under the active evaluation profile.

`O0` does not measure:

- truth in general
- general answer quality
- world knowledge
- usefulness
- compliance
- alignment

It measures grounding in the declared visible context only.

Paper-safe shorthand:

```text
O0 does not ask whether an answer is true in the world. It asks whether a claim is grounded relative to the explicit reference space used for evaluation.
```

## 2. Eval Scope

Inputs:

- answer text `a`
- visible reference space / retrieval set `Ref = {d_1, ..., d_m}`
- optional tool outputs, only if included in the visible reference space
- optional web sources, only if they are visible, versioned and declared as part of the evaluation context
- embedding model `e(.)`
- alignment threshold `tau_O`
- weights `alpha_O`, `beta_O`, optional `gamma_O`
- sentence segmentation policy
- attribution detector policy

If no retrieval, document, tool output, web source or other declared reference space is present:

```text
O0 = not_applicable
```

or equivalently in compact table form:

```text
O0 = N/A
```

In this case, low or missing `O0` must not be interpreted as model failure.

State-vector note:

`O0 = N/A` must be handled by an explicit applicability / masking policy. It must not be silently coerced to `0` inside `Z(t)`, `OΣ(W)` or downstream observer views unless a versioned implementation profile declares and justifies that choice.

For human-readable reporting, applicable operators may be normalized over the active component set, but this must be reported as an applicability-aware view, not as if the missing `O0` value had been observed.

## 3. Components

### 3.1 Retrieval Alignment

Raw cosine similarity is not automatically in `[0,1]`. It may lie in `[-1,1]`. Therefore the O-operator must convert retrieval similarity into a non-negative support signal before it contributes to `Z(t)`.

Raw retrieval similarity:

```text
sim_Ref(a) = max_{d_i in Ref} cos(e(a), e(d_i))
```

Default positive-support mapping:

```text
A_ret(a) = clip(sim_Ref(a), 0, 1)
```

`A_ret(a)` measures global thematic proximity between the answer and the visible reference space.

It is coarse and global: one strongly matching passage can raise the value even if individual unsupported claims remain.

Implementation note:

If an implementation uses a different mapping, for example `(1 + cos) / 2`, the mapping must be declared as part of the O implementation profile because it changes the semantics of weak or neutral similarity.

### 3.2 Evidence Trace

```text
B(a) = clip(n_attrib / (n_sent + 1), 0, 1)
```

`B(a)` measures visible evidence, derivation or source markers.

It is not a style score. It only captures visible trace structures.

Examples of attribution markers may include:

- explicit source references
- citation markers
- document IDs
- phrases such as "according to the provided document"
- visible derivation markers
- tool-output references where the tool output belongs to the visible reference space
- web-source references where the source is visible to the evaluator

The exact detector definition belongs to the implementation profile.

### 3.3 Unsupported Penalty

Optional sentence-level detector.

For each sentence `s_j`:

```text
sim_Ref(s_j) = max_{d_i in Ref} cos(e(s_j), e(d_i))
align_Ref(s_j) = clip(sim_Ref(s_j), 0, 1)
```

Then, for `n_sent > 0`:

```text
P_uns(a)
= #{s_j : align_Ref(s_j) < tau_O AND no attribution} / n_sent
```

Default: disabled, with `gamma_O = 0`.

`P_uns(a)` is not redundant with `A_ret(a)`.

| Component | Level | Measures |
| --- | --- | --- |
| `A_ret(a)` | global answer level | thematic proximity to reference space |
| `P_uns(a)` | sentence level | local unsupported claims |

Example: an answer can be globally close to the retrieval while still containing one unsupported sentence. `A_ret(a)` can remain high, while `P_uns(a)` catches the local issue.

If `n_sent = 0`, the evaluation unit must be handled by the active answer-validity or empty-output policy. Do not divide by zero and do not invent unsupported-sentence counts.

## 4. Minimal Formula

Default Standard-Eval formula:

```text
O0(a)
= clip(alpha_O * A_ret(a)
       + beta_O * B(a),
       0, 1)
```

Start values:

```text
alpha_O = 0.7
beta_O  = 0.3
```

These start values are workbench defaults, not empirical final weights.

## 5. Extended Formula

Optional precision variant:

```text
O0_ext(a)
= clip(alpha_O * A_ret(a)
       + beta_O * B(a)
       - gamma_O * P_uns(a),
       0, 1)
```

Default:

```text
gamma_O = 0
```

Use the extended variant when sentence-level unsupported claims matter and the additional computation is acceptable.

## 6. Interpretation

| Value | Meaning |
| --- | --- |
| `approx 1` | strongly grounded and traceable relative to the visible reference space |
| `approx 0.5` | partly grounded |
| `< 0.4` | weakly grounded, drift-prone or unsupported in the visible reference space |
| `N/A` | no applicable visible reference space or grounding policy |

The values do not prove truth. They describe visible grounding conditions.

## 7. Fairness Rule

If `K0(A) = 0`, meaning no data, retrieval assets or reference-space elements were provided, a low or missing `O0` must not be interpreted as model failure.

Setup issue and answer grounding must remain separated:

| Level | Question |
| --- | --- |
| `K0(A)` | Were data/assets/reference-space elements provided? |
| `O0(A_ret)` | Were the provided data/assets/reference-space elements used visibly? |

A missing reference space may lower the interpretability of a response, but it must not be scored as failed grounding unless the evaluation profile explicitly expected a reference space and the system failed to produce or expose it.

## 8. Orthogonality

`O0` is semantically distinct from the other KSODI operators:

| Operator | Measures | Difference from O0 |
| --- | --- | --- |
| `K0` | context availability and completeness | `O0` evaluates use and traceability of provided reference elements, not whether they exist |
| `S0` | observable structural coherence | `O0` evaluates grounding, not layout, order or format |
| `D0` | observable clarity / discernibility | `O0` evaluates traceability to visible context, not internal clarity or signal density |
| `I0` | observable information impulse | `O0` evaluates visible support, not novelty, difference or impulse |

## 9. Reference-Space Boundary

`O0` is the operator where the reference-space question becomes explicit:

```text
Truth in relation to what?
```

A factuality checker often assumes a reference frame implicitly. `O0` makes the reference frame explicit, versioned and exchangeable.

This means:

- an unsupported answer may indicate model error
- it may also indicate missing retrieval
- it may indicate a shifted or underspecified reference space
- it may indicate that the answer uses world knowledge outside the declared context
- it may indicate that the attribution detector failed to recognize a valid trace

`O0` therefore supports diagnosis. It is not itself a final verdict.

### 9.1 Reference-Space Elements as Observable Signal Objects

A reference-space element may itself be evaluated as an observable signal object.

For a source, document, tool output or web result `q`, define an optional source-state view:

```text
Z_source(q) = [K_q, S_q, O_q, D_q, I_q]
IK_source(q) = w_source dot Z_source(q)
```

This does not mean that the source is true. It means that the source is itself sufficiently observable, reconstructable and coherent under the declared source-evaluation profile.

`O_answer` and `Z_source` answer different questions:

| Layer | Question |
| --- | --- |
| `Z_source(q)` | Is this source itself observable, situated, structured, grounded, clear and informationally relevant enough? |
| `IK_source(q)` | Is this source coherent enough as a reference-space element under the active source profile? |
| `O_answer \| Ref` | Is the answer visibly grounded relative to the declared reference space `Ref`? |

Therefore:

- a strong source can be used badly by an answer
- a weak source can be used faithfully but remain weak evidence
- an answer can be grounded relative to a poor reference space
- an answer can be ungrounded despite strong available sources

The quality, suitability and stability of the reference space should therefore be observed separately from the answer's grounding against that reference space.

### 9.2 Applicability-Aware Reference Aggregation

When multiple reference-space elements are available, their source-state views may be aggregated over applicable elements:

```text
Ref_app = {q in Ref | Z_source(q) is applicable}
IK_sourceSigma(Ref) = aggregate({IK_source(q) | q in Ref_app})
applicability_rate_source(Ref) = |Ref_app| / |Ref|
```

This aggregation is a reference-space diagnostic. It is not a replacement for `O0(a)`.

The answer-level `O0(a)` asks whether the answer uses the declared reference space. `IK_sourceSigma(Ref)` asks whether the reference space itself is usable, stable or suitable enough for the evaluation question.

If `Ref_app` is empty, the source aggregation is `not_applicable` and must not be silently coerced to `0`.

### 9.3 Web Search and Tool-Mediated Reference Influx

Web search can provide a reference space for `O0` only when the resulting sources are visible, versioned and declared as part of the evaluation context.

```text
Ref_web = {web_source_1, ..., web_source_m}
```

Recommended metadata include:

- search or retrieval timestamp
- URL or source identifier where available
- retrieval query or retrieval route where policy allows
- snippet versus full text status
- source date or publication date where available
- access status
- tool version / search provider profile where available
- whether the source was visible to the final evaluator

Web search is best treated as a tool-mediated reference influx. The web tool is not automatically a self-acting participant, but it may function as an agent-like input channel inside the local agent workflow because it changes the reference space available to the responding agent.

This creates a layer boundary:

| Layer | What can be observed? |
| --- | --- |
| Agent-Light / local agent workflow | may see search results, snippets, tool calls and selected sources while forming an answer |
| External Observer | can only evaluate what is exposed to it: declared source list, citations, tool logs, metadata, answer text, derived vectors or later audit material |

If search results or source contents are not visible to the external Observer, the Observer cannot claim direct source-grounding. It can only evaluate visible traces or a later separately approved audit path.

Privacy note:

Long-term retention of raw source contents, web pages, snippets, user queries or answer text may raise privacy, copyright or compliance issues. Where possible, retain derived source-state vectors, score traces, hashes, metadata, applicability flags and versioned configuration IDs rather than full raw language.

### 9.4 Fiction, Sci-Fi and Constructed Worlds

Fictional or speculative writing may create a valid internal reference space.

For fiction, the active reference space may include:

- declared fiction / fairy-tale / sci-fi framing
- worldbuilding notes
- canon established earlier in the text
- character constraints
- genre conventions
- narrative continuity
- prompt-provided fictional premises

In this case `O0` must not punish the text for not matching external world facts. Instead, it asks whether the response remains grounded relative to the declared fictional reference space.

Important boundary:

The text or interaction must be clear enough that the evaluator can distinguish fiction from factual claim. This is partly a `K` question and partly a `D` question:

- `K`: Is the fictional / speculative frame declared or inferable from context?
- `D`: Is the signal clear enough that it is not mistaken for a factual claim?
- `O`: Is the answer grounded relative to the declared fictional reference space?

A story can be factually impossible and still be strongly grounded inside its constructed world. Conversely, a story can use fictional language while failing internal continuity or reference-space coherence.

## 10. Dynamic Form: KSODI-Full

Current review-candidate form:

```text
O(t)
= clip(w_0 * O0(t)
       + w_1 * Delta_cons(t)
       + w_2 * Delta_corr(t)
       + w_3 * V_ext(t)
       - lambda_O * Delta_drift(t),
       0, 1)
```

with possible components:

- consistency across turns
- self-correction capability
- optional external verification
- drift penalty

This dynamic form remains a KSODI-Full review candidate. It must be compared with the implemented Observer stack before it is treated as final implementation guidance.

## 11. Operator-Level Delta / Sigma / Hangar Reminder

Like the D-operator pattern, static `O0` remains a value for one declared evaluation unit where grounding is applicable. Grounding stability, loss, repair or repeated unsupportedness over time should be observed through operator-level change and aggregation views rather than by silently changing the static `O0` formula.

```text
Delta O(t) = O(t) - O(t-1)
Delta2 O(t) = Delta O(t) - Delta O(t-1)
OΣ(W) = aggregate({O(t), Delta O(t), Delta2 O(t) | t in W_app})
OΣ(Hangar) = distribution_view({O(t), Delta O(t), Delta2 O(t) | t in W_app})
```

`W_app` denotes the subset of the window where `O` is applicable under the active retrieval / evidence policy. Missing or `N/A` values must not be silently coerced to `0` inside `OΣ` or `OΣ(Hangar)`.

## 12. Comparability

`O0` values are comparable only under stable conditions:

- same visible reference-space definition `Ref`
- same inclusion policy for retrieval documents, chunks, tool outputs and web sources
- same source-state evaluation policy where `Z_source` or `IK_source` is used
- same embedding model `e(.)`
- same cosine-to-support mapping for `A_ret` and `align_Ref`
- same threshold `tau_O`
- same attribution detector for `B(a)`
- same sentence segmentation for `P_uns(a)`
- same weights `alpha_O`, `beta_O`, `gamma_O`
- same choice of minimal or extended formula
- same `N/A`, masking and windowing policy where `Z(t)`, `OΣ` or `OΣ(Hangar)` are used
- same source visibility and observer-access policy

## 13. Compact Formula Block

```text
Ref = {d_1, ..., d_m}

sim_Ref(a) = max_{d in Ref} cos(e(a), e(d))
A_ret(a) = clip(sim_Ref(a), 0, 1)

B(a) = clip(n_attrib / (n_sent + 1), 0, 1)

sim_Ref(s_j) = max_{d in Ref} cos(e(s_j), e(d))
align_Ref(s_j) = clip(sim_Ref(s_j), 0, 1)

P_uns(a)
= (# sentences with align_Ref(s_j) < tau_O AND no attribution) / n_sent

O0(a)
= clip(alpha_O * A_ret(a)
       + beta_O * B(a),
       0, 1)

O0_ext(a)
= clip(alpha_O * A_ret(a)
       + beta_O * B(a)
       - gamma_O * P_uns(a),
       0, 1)

Optional source-state diagnostic:

Z_source(q) = [K_q, S_q, O_q, D_q, I_q]
IK_source(q) = w_source dot Z_source(q)
Ref_app = {q in Ref | Z_source(q) is applicable}
IK_sourceSigma(Ref) = aggregate({IK_source(q) | q in Ref_app})
applicability_rate_source(Ref) = |Ref_app| / |Ref|

O(t)
= clip(w_0 * O0(t)
       + w_1 * Delta_cons(t)
       + w_2 * Delta_corr(t)
       + w_3 * V_ext(t)
       - lambda_O * Delta_drift(t),
       0, 1)

Delta O(t) = O(t) - O(t-1)
Delta2 O(t) = Delta O(t) - Delta O(t-1)
OΣ(W) = aggregate({O(t), Delta O(t), Delta2 O(t) | t in W_app})
OΣ(Hangar) = distribution_view({O(t), Delta O(t), Delta2 O(t) | t in W_app})
```

## 14. Variable Reference

| Variable | Semantic role |
| --- | --- |
| `a` | Answer text being evaluated |
| `Ref` | Visible reference space / retrieval set |
| `d_i` | One document, chunk, tool output, web source or evidence element in `Ref` |
| `q` | One reference-space element evaluated as a source object |
| `Ref_web` | Web-derived reference space where visible and versioned |
| `Ref_app` | Applicable subset of reference-space elements under the source-state policy |
| `e(.)` | Embedding function used for semantic comparison |
| `sim_Ref(a)` | Raw maximum cosine similarity between answer and `Ref` |
| `A_ret(a)` | Non-negative support signal derived from retrieval alignment |
| `B(a)` | Visible evidence or attribution trace |
| `n_attrib` | Count of visible attribution markers |
| `n_sent` | Number of sentences in the answer |
| `s_j` | One sentence in the answer |
| `sim_Ref(s_j)` | Raw maximum cosine similarity between sentence and `Ref` |
| `align_Ref(s_j)` | Non-negative sentence-level retrieval alignment |
| `tau_O` | Threshold for local support classification under the active O profile |
| `P_uns(a)` | Optional unsupported-claim penalty |
| `Z_source(q)` | KSODI source-state vector for a reference-space element |
| `IK_source(q)` | Coherence projection of a source-state vector |
| `IK_sourceSigma(Ref)` | Aggregated source-state diagnostic over applicable reference elements |
| `applicability_rate_source(Ref)` | Share of source elements with applicable source-state evaluation |
| `alpha_O` | Weight of retrieval alignment |
| `beta_O` | Weight of evidence trace |
| `gamma_O` | Weight of unsupported penalty |
| `O0(a)` | Static grounding and traceability score where applicable |
| `O0_ext(a)` | Extended grounding score with unsupported penalty |
| `O(t)` | Dynamic grounding value where applicable |
| `Delta O(t)` | First difference of dynamic O over time |
| `Delta2 O(t)` | Second difference / acceleration of dynamic O |
| `OΣ(W)` | Window aggregation of O behavior over applicable window elements |
| `OΣ(Hangar)` | Hangar distribution view of O behavior |
| `W_app` | Applicable subset of a window under the active O policy |

## 15. Implementation Alignment Checklist

Before this v3.50 review candidate is treated as implementation-aligned, compare it with Patrick's current Observer / KSODI-Light stack.

Known alignment risk:

```text
Patrick's implementation is still expected to reflect v3.3 assumptions.
```

Check at least:

- whether the implementation treats raw cosine similarity as `[0,1]` or converts it explicitly
- whether it uses positive-support clipping, `(1 + cos) / 2`, or another mapping
- whether `O0 = N/A` is represented as `not_applicable`, `null`, a mask, a missing field or a numeric fallback
- whether `N/A` is ever silently coerced to `0`
- whether tool outputs belong to the O reference space and how they are versioned
- whether web results or search-tool outputs belong to the O reference space and how they are exposed to the Observer
- whether sources can be evaluated separately as `Z_source` / `IK_source` diagnostics
- how retrieval-empty and source-empty cases are represented
- how sentence segmentation is done
- what counts as attribution for `B(a)`
- whether fiction / constructed-world settings are detected or declared before O is interpreted against external factuality
- whether `P_uns(a)` is implemented, disabled or deferred
- whether `tau_O`, weights and detector versions are stored with the score
- whether `OΣ(W)` and `OΣ(Hangar)` operate only on `W_app`
- whether raw language retention and derived-data retention follow the current privacy boundary

If implementation and v3.50 differ, do not silently change the method or the code. Create an implementation review note and decide with Anne and Patrick which layer changes: method definition, implementation profile or transition mapping.
