# KSODI Implementation Guardrails

Status: public cross-layer implementation contract for the current KSODI v3.50
method line; method guidance, not an executable production implementation.

These guardrails apply to KSODI Standard-Eval and KSODI-Full. They also apply
when outputs from a KSODI-Light-guided interaction are stored, compared over
time or evaluated by an external Observer.

Read this document together with:

- [KSODI Architecture V350](./KSODI-Architecture_V350.md)
- [Which KSODI Variant Do I Need?](./WHICH_KSODI.md)
- [KSODI Conceptual Note](./Conceptual-Note.md)
- [Agent Instructions](./AGENTS.md)

## 1. Core Invariants

A KSODI implementation must preserve the following distinctions:

1. Contributions from distinguishable entities remain source-attributed before
   operator evaluation.
2. Entity identity remains stable; sender and receiver are exchange-relative
   roles stored on the relevant transmission or pairing edge.
3. Context may be shared, but the evaluation target remains explicit.
4. Monadic state and movement are calculated along one declared trajectory and
   its source-local index.
5. Relational pairing and relational index are declared separately; neither is
   inferred by silently aggregating adjacent contributions.
6. Individual operators remain operator-specific diagnostics until a valid
   state-vector profile has been constructed.
7. After stable `R0`, `IK_rel`, staged `R_geom` and staged optional `R_pace`
   remain parallel calculations with separate bases and profiles.
8. Graph, vector, Hangar and visualization layers remain typed derived views
   whose outputs can be traced back to original events, evaluations, windows
   and model versions.
9. Coordinate order `(K,S,O,D,I)` is not a causal execution pipeline. Sender-side
   formation and receiver-side preferred reconstruction are explanatory,
   role-relative process topologies and must not be hard-coded as universal
   internal processing order.

These are method invariants, not preferences of one database product or
implementation stack.

### Monadic Default, Relational Only After Explicit Pairing

KSODI v3.50 keeps monadic and relational / potentially n-adic layers methodologically separate.

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
Delta Z_A(k_A) = Z_A(k_A) - Z_A(k_A - 1)
Delta Z_B(k_B) = Z_B(k_B) - Z_B(k_B - 1)
```

A response from `B` after `A` is not automatically a monadic state transition
for `A` or `B`. It is only a relational exchange when a pairing map is
explicitly declared.

This rule matters for `R0` and every separately defined relational branch.
The same distinction must remain visible in stored records, projections,
vector and Hangar views, analytical queries and later Controller inputs.

## 2. Evaluation Unit and Identity Contract

Each externally observable contribution must be retained as its own event
before the five operators are evaluated.

A minimal implementation distinguishes:

| Field | Function |
| --- | --- |
| `conversation_id` | overall interaction container; not a shared state |
| `thread_id` | one linear or branching path inside the container |
| `event_id` | unique identifier of one contribution or observable event |
| `entity_id` | stable distinguishable emitting entity or system side |
| `trajectory_id` | monadic trajectory to which the event belongs |
| `trajectory_index` / `k_entity` | local order within that trajectory |
| `observed_at` / timestamp | recorded clock time where available; separate from event and trajectory order |
| `global_event_index` / `n` | declared global order across ingested observable events; not automatically a timestamp |
| `exchange_id` | declared exchange container or edge identity |
| `relational_index` / `j` | order of comparable paired or n-adic evaluations |
| `pairing_map` / `pi(j)` | explicit mapping to local trajectory positions |
| `role_in_exchange` | sender, receiver or another declared edge-relative role |
| `reply_to_event_id` | explicit response relation to another event |
| `target_event_id` | event whose operators are being evaluated |
| `context_event_ids` | visible events used as context for that evaluation |
| `observation_object_type` | event, state, trajectory, window, aggregate or relational feature object |
| `profile_id` / `profile_version` | declared evaluation or branch profile |

In a simple linear chat, `conversation_id` and `thread_id` may coincide. In
branched, multi-agent or tool-using interactions they must not be assumed to be
the same object.

Example:

| Contribution | Entity | Event | Trajectory | Local index | Exchange | Relational index | Role | Replies to |
| --- | --- | --- | --- | ---: | --- | ---: | --- | --- |
| contribution from A | `A` | `A-17` | `T-A` | 17 | `X-09` | 9 | sender | — |
| response from B | `B` | `B-09` | `T-B` | 9 | `X-09` | 9 | receiver | `A-17` |

The response may be evaluated with the preceding contribution as visible
context:

```text
target_event_id: B-09
context_event_ids: [A-17, ...]
```

This does not merge the two sources. Shared context, entity identity,
trajectory identity and exchange-relative role are different properties.

### Unknown Morse-like carrier

An implementation that detects an unfamiliar recurring pulse pattern stores
each attributable signal event before it knows the convention or meaning. It
also versions carrier, segmentation and feature-extraction profiles. Repeated
events may support an anomaly or contact-attempt hypothesis, but the record must
not silently label them as acknowledgement, successful decoding, hostile
intent or attack.

If a second source replies, the reply remains a separate trajectory. A declared
`exchange_id`, `relational_index` and `pairing_map` may later permit `R0`
evaluation. Similar signs or timing do not themselves establish semantic
agreement, coupling or causality.

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

Here, `j` indexes a paired evaluation, while `k_A` and `k_B` remain local
trajectory indices. A versioned `pairing_map` materializes
`pi(j)=(k_A(j),k_B(j))`. `R0` and every relational branch must preserve this
distinction.

`R0` receives distinguishable trajectories, explicit pairing or constellation
metadata, compatible profiles, applicability and the selected stability policy.
It is not calculated from monadic `IK` and is not a technical handshake
detector. An open gate does not prove receipt, acknowledgement, contact,
semantic agreement, coupling or causality.

After stable `R0`, implementations keep the branches separate:

```text
IK_rel(j | p_IK_rel)
R_geom(j | p_geom)   [staged]
R_pace(j | p_pace)   [staged, optional]
```

Each branch stores its own basis, feature schema, weights, applicability and
version. None automatically inherits the equal five-axis `IK` baseline or the
output of another relational branch.

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
| distinguishable trajectories plus explicit pairing / constellation and compatible gate policy | possible input for `R0`; only stable applicable `R0` may open separately based relational branches |

A single operator or electively selected subset must not be represented as:

- a complete `Z` state;
- canonical `IK`;
- a relational gate;
- coupling or resonance measurement;
- the complete KSODI method.

Missing or omitted operators must never be silently encoded as zero.

## 5. Applicability Is Not Elective Omission

An applicability mask such as `A_Z,A(k_A | p_Z)` records whether an operator
component is methodically evaluable for one source-local target under the
declared profile. A relational mask uses its declared relational index and
branch profile, for example `A_IK_rel(j | p_IK_rel)`. A generic `t` must not
silently stand for both index types. Applicability is not a shortcut for
selecting only convenient operators.

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
shared Light interaction frame into one aggregated entity-independent
state.

KSODI-Light itself does not calculate `R0`, `IK_rel` or the R-family.

## 7. Storage, Graph and Vector Views

The canonical record must preserve raw observable events and versioned
evaluations. A graph database, vector database or visualization layer may
project that record for particular queries, but it must not become the only
place where event identity, source attribution or evaluation provenance exists.

A versioned evaluation should retain at least:

- `evaluation_id`, observation-object type and layer or branch;
- `target_event_id`, `context_event_ids`, entity and trajectory identity;
- global, local or relational index type and value as applicable;
- exchange, reply and pairing / constellation metadata where relational;
- evaluator model and version;
- operator or branch profile and version;
- declared reference-space identifier;
- operator, state, projection, gate or branch values plus applicability mask;
- window and aggregation policy for Sigma or Hangar views;
- weighting, normalization and threshold policy where relevant;
- evaluation configuration hash or equivalent reproducibility metadata.

Embedding vectors are auxiliary representations. They are not the KSODI state
vector `Z`. Store the embedding model, version, dimensionality, normalization,
purpose and source-content hash. Vectors created in different embedding spaces
must not be compared directly unless an explicit cross-space calibration has
been defined.

Graph, vector, dashboard and Hangar views must declare their input object type,
index/window policy, profile, applicability and provenance. They must not become
untyped stores that merge raw events, monadic states, relational evaluations
and window aggregates.

## 8. Observer, Controller and Data-Governance Boundary

KSODI Standard-Eval and KSODI-Full specify Observer-oriented calculations. The
Observer reconstructs and reports observable states, trajectories and typed
relational views. It does not decide, intervene or steer by itself.

A future Controller is not a standalone KSODI variant. It may consume only
declared Observer findings inside governance corridors approved for the
application case. Controller policy, action, authorization and audit events
remain separate from observed events and Observer evaluations. Feedback must
not allow the Observer to redefine its own evidence, thresholds or profiles.

Reduced state vectors, projections, embeddings, trajectories and Hangar objects
may remain sensitive or personally identifiable even when raw text is absent.
Implementations therefore require purpose limitation, access controls,
retention rules, deletion policies and documented legal / governance review.
Pseudonymization does not automatically create anonymity.
## 9. Legacy and Aggregated Data

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

## 10. Minimal Implementation Check

Before treating an implementation as v3.50-compatible, verify:

1. Are evaluation targets and visible context separately identifiable?
2. Are stable entity identity and exchange-relative roles stored separately?
3. Can every operator value be traced to one target event and one versioned
   evaluation?
4. Are `n`, source-local `k_entity` and relational `j` distinguishable?
5. Are state changes calculated only along one comparable typed sequence?
6. Is relational pairing explicit, versioned and reproducible?
7. Does `R0` use trajectories and pairing metadata rather than monadic `IK`?
8. Are `IK_rel`, staged `R_geom` and staged optional `R_pace` implemented as
   separate branches with their own bases?
9. Are partial profiles, non-applicability, non-observability and numeric zero
   distinguishable?
10. Do graph, vector, Hangar and dashboard outputs preserve object type and
    links to canonical events and evaluations?
11. Are model, prompt, reference-space, retrieval, window, weighting and
    embedding changes versioned?
12. Are Observer findings, Controller actions and governance approvals stored
    as separate event types?
13. Are legacy aggregates prevented from entering relational calculations as
    if they were separated trajectories?
14. Are sensitive reduced vectors and trajectory data governed rather than
    assumed anonymous?

Public transfer examples are available under
[implementation-examples](./implementation-examples/README.md).
They are orientation aids, not production systems.

---

© 2026 Anne Steinacker-Folkerts & Heiko Folkerts  
Licensed under CC BY 4.0
