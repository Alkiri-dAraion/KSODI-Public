# KSODI Implementation Guardrails

Status: public cross-layer implementation contract for the current KSODI v3.50
method line; method guidance, not an executable production implementation.

These guardrails apply to KSODI Standard-Eval and KSODI-Full. They also apply
when outputs from a KSODI-Light-guided interaction are stored, compared over
time or evaluated by an external Observer.

Read this document together with:

- [KSODI Architecture](./ARCHITECTURE.md)
- [Which KSODI Variant Do I Need?](./WHICH_KSODI.md)
- [KSODI Conceptual Note](./KSODI-Eval-Variants/Conceptual-Note.md)
- [Agent Instructions](./AGENTS.md)

## 1. Core Invariants

A KSODI implementation must preserve the following distinctions:

1. Contributions from distinguishable entities remain source-attributed before
   operator evaluation.
2. Context may be shared, but the evaluation target remains explicit.
3. Monadic state and movement are calculated along one declared trajectory.
4. Relational pairing is declared separately; it is not inferred by silently
   aggregating adjacent contributions.
5. Individual operators remain operator-specific diagnostics until a valid
   state-vector profile has been constructed.
6. Graph, vector and visualization layers remain derived views whose outputs
   can be traced back to the original events, evaluations and model versions.

These are method invariants, not preferences of one database product or
implementation stack.

### Monadic default, dyadic only after explicit pairing

KSODI v3.50 keeps the monadic and dyadic layers methodologically separate.

- Operator values and state movement remain monadic unless a pairing rule is
  explicitly declared.
- A contribution from entity `A` and a contribution from entity `B` remain
  separate trajectories unless the implementation defines a relational pair,
  exchange or comparison step.
- A visible context relation does not collapse separate entities into one
  shared state.
- The predecessor for local movement must stay inside the same trajectory.

In practical terms:

```text
Delta Z_A(k) = Z_A(k) - Z_A(k - 1)
Delta Z_B(l) = Z_B(l) - Z_B(l - 1)
```

A response from `B` after `A` is not automatically a monadic state transition
for `A` or `B`. It is only a relational exchange when a pairing map is
explicitly declared.

This rule matters for implementation and for all later relational layers such
as `R0`, `IK_rel` and the R-family. The same distinction must remain visible in
stored records, projections, vector views and analytical queries.

## 2. Evaluation Unit and Identity Contract

Each externally observable contribution must be retained as its own event
before the five operators are evaluated.

A minimal implementation distinguishes:

| Field | Function |
| --- | --- |
| `conversation_id` | overall interaction container |
| `thread_id` | one linear or branching path inside the conversation |
| `event_id` | unique identifier of one contribution or observable event |
| `entity_id` | distinguishable emitting entity or system side |
| `trajectory_id` | monadic trajectory to which the event belongs |
| `trajectory_index` | local order within that trajectory |
| `global_event_index` | chronological order across all observed events |
| `exchange_id` | declared relational exchange unit |
| `reply_to_event_id` | explicit response relation to another event |
| `target_event_id` | event whose operators are being evaluated |
| `context_event_ids` | visible events used as context for that evaluation |

In a simple linear chat, `conversation_id` and `thread_id` may coincide. In
branched, multi-agent or tool-using interactions they must not be assumed to be
the same object.

Example:

| Contribution | Conversation | Event | Trajectory | Local index | Exchange | Replies to |
| --- | --- | --- | --- | ---: | --- | --- |
| contribution from A | `C-01` | `A-17` | `T-A` | 17 | `X-09` | — |
| response from B | `C-01` | `B-09` | `T-B` | 9 | `X-09` | `A-17` |

The response may be evaluated with the preceding contribution as visible
context:

```text
target_event_id: B-09
context_event_ids: [A-17, ...]
```

This does not merge the two sources. Shared context and source attribution are
different properties.

## 3. Monadic Movement Before Relational Pairing

For distinguishable trajectories `A` and `B`:

```text
Z_A(k_A)
Z_B(k_B)

Delta Z_A(k_A) = Z_A(k_A) - Z_A(k_A - 1)
Delta Z_B(k_B) = Z_B(k_B) - Z_B(k_B - 1)
```

The predecessor must belong to the same trajectory. In a simple human-chatbot
exchange, this means that the human-side sequence is compared with its own
previous contributions and the chatbot-side sequence with its own previous
contributions. A chronological transition from a contribution by `A` directly
to a response by `B` is not a monadic `Delta Z`.

Relational evaluation uses a separately declared pairing map:

```text
pi(j) = (k_A(j), k_B(j))
```

Here, `j` indexes a paired exchange step, while `k_A` and `k_B` remain
local trajectory indices. `R0`, `IK_rel` and later relational layers must not
erase this distinction.

Adjacency alone is not a universal pairing rule. Implementations must handle
multiple responses, interruptions, tool calls, asynchronous events, branches
and n-agent settings through explicit exchange, reply or graph metadata.

## 4. Individual Operators and Partial Profiles

The five KSODI operators can be inspected individually. Their standalone use
has a narrower meaning than a complete KSODI state-space evaluation.

| Available material | Defensible interpretation |
| --- | --- |
| one operator value | operator-specific diagnostic |
| one operator over time | operator-specific trajectory |
| electively selected subset | explicitly partial or KSODI-inspired profile |
| all five separately evaluated operators | possible input for a complete `Z` profile |
| valid `Z` under a declared profile | possible input for IK and monadic drift |
| distinguishable and explicitly paired trajectories | possible input for `R0`, `IK_rel` and later relational layers |

A single operator or electively selected subset must not be represented as:

- a complete `Z` state;
- canonical `IK`;
- a relational gate;
- coupling or resonance measurement;
- the complete KSODI method.

Missing or omitted operators must never be silently encoded as zero.

## 5. Applicability Is Not Elective Omission

An applicability mask such as `A_Z(t)` records whether an operator component
is methodically evaluable under the declared observation profile. It is not a
shortcut for selecting only convenient operators.

```text
not applicable != not selected
not observable  != zero
```

Applicability-aware projections must declare their active component set,
minimum-component policy and renormalization rule. An intentionally reduced
experimental profile must be named and versioned as such. It is not
automatically comparable with the canonical five-operator profile.

## 6. KSODI-Light to Observer Boundary

KSODI-Light can be used inside one chat or prompt context without formal data
infrastructure. It remains a local reflective working agreement.

The moment Light-guided contributions are stored, trended, compared or
evaluated by an external Observer, the source-attribution and trajectory rules
in this document apply. Formal observer evaluation must not turn a locally
shared Light interaction frame into one aggregated participant-independent
state.

KSODI-Light itself does not calculate `R0`, `IK_rel` or the R-family.

## 7. Storage, Graph and Vector Views

The canonical record must preserve raw observable events and versioned
evaluations. A graph database, vector database or visualization layer may
project that record for particular queries, but it must not become the only
place where event identity, source attribution or evaluation provenance exists.

A versioned evaluation should retain at least:

- `evaluation_id`;
- `target_event_id` and `context_event_ids`;
- evaluator model and version;
- operator profile and version;
- declared reference-space identifier;
- operator values and applicability mask;
- weighting, normalization and threshold policy where relevant;
- evaluation configuration hash or equivalent reproducibility metadata.

Embedding vectors are auxiliary representations. They are not the KSODI state
vector `Z`. Store the embedding model, version, dimensionality, normalization,
purpose and source-content hash. Vectors created in different embedding spaces
must not be compared directly unless an explicit cross-space calibration has
been defined.

## 8. Legacy and Aggregated Data

Historical or external data may already aggregate multiple contributions into
one evaluation unit. Such data remains useful for provenance or aggregate
interaction views, but it must not be silently treated as source-separated
trajectory data.

A legacy aggregate should declare an equivalent status such as:

```text
evaluation_unit_type: interaction_pair_aggregate
trajectory_separation: unavailable
ik_rel_eligible: false
r0_eligible: false
```

If the original events still exist, they may be re-ingested and evaluated
under the current contract. If only the aggregate remains, the original
monadic trajectories cannot be reconstructed reliably from the aggregate
alone.

## 9. Minimal Implementation Check

Before treating an implementation as v3.50-compatible, verify:

1. Are evaluation targets and visible context separately identifiable?
2. Can every operator value be traced to one target event and one versioned
   evaluation?
3. Are state changes calculated only along the same trajectory?
4. Is relational pairing explicit and reproducible?
5. Are partial profiles and applicability masks distinguishable?
6. Do graph, vector and dashboard outputs preserve links to canonical events?
7. Are model, prompt, reference-space, retrieval and embedding changes
   versioned?
8. Are legacy aggregates prevented from entering relational calculations as if
   they were separated trajectories?

Public transfer examples are available under
[implementation-examples](./KSODI-Eval-Variants/implementation-examples/README.md).
They are orientation aids, not production systems.

---

© 2026 Anne Steinacker-Folkerts & Heiko Folkerts  
Licensed under CC BY 4.0
