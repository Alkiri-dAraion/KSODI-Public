# Layer 1 - Operators

Status: canonical public v3.50 Standard-Eval operator line. All five operator
files are released as public method documentation. Release status does not
turn optional views into mandatory calculations or make staged later research
operational.

## What this folder contains

Layer 1 observes one explicitly identified, source-attributed target event at a
time. Each applicable static operator produces one scalar coordinate:

```text
e_A(k_A)
  -> K_A(k_A), S_A(k_A), O_A(k_A), D_A(k_A), I_A(k_A)
  -> Z_A(k_A)
```

The five coordinates jointly form the monadic state vector `Z_A(k_A)`. A
single operator value is not itself a vector. Sequences, windows and Hangar
views may describe movement or distribution of one operator coordinate, but
they do not change the source identity or layer of the static value.

Entity `A` and Entity `B` remain distinguishable. Sender and receiver are
roles inside a declared exchange, not stable entity types. Relational
comparison begins only at the separately declared `R0` gate after complete,
distinguishable `Z` trajectories and an explicit pairing rule are available.

## Operators and companion

- [`K0`](./Operator_K_v350.md) — Observable Context Completeness
- [`S0`](./Operator_S_v350.md) — Observable Structural Coherence
- [`O0`](./Operator_O_v350.md) — Observable Grounded Objectivity
  - [`O` Source-Need Gate](./O_Source-Need-Gate_v350.md) — applicability and
    source-need companion; not a sixth operator
- [`D0`](./Operator_D_v350.md) — Observable Clarity
- [`I0`](./Operator_I_v350.md) — Observable Information Impulse

## Reader path inside each operator

Each substantive operator file should let a new reader follow the same
reasoning dependency while preserving the operator's own semantics:

1. narrow observable question and plain-language orientation;
2. one bounded Human–Chatbot example and one bounded second-domain example;
3. canonical definition, evaluation unit, source and trajectory identity;
4. declared measurement basis, profile and applicability;
5. static components, calculation and interpretation;
6. comparability before source-local `Delta` and `Delta2`;
7. typed window and Hangar views;
8. explicit boundary to `R0` and later relational layers;
9. compact formal summary and variable reference;
10. separation between the public method and implementation material.

This is a semantic reading order. It does not require identical formulas or
section numbering across the five operators.

## Coordinate order and two process topologies

The five operator coordinates can be evaluated independently. Their canonical
state-vector order is a stable reporting convention, not a causal calculation
chain:

```text
Z_A(k_A) =
  (K_A(k_A), S_A(k_A), O_A(k_A), D_A(k_A), I_A(k_A))
```

KSODI additionally uses two role-relative explanatory process topologies:

```text
sender-side formation:        K -> S -> O -> D -> I
receiver-side reconstruction: I -> D -> O -> S -> K
```

Sender-side formation describes how context-bound material may be structured,
grounded, transformed into a channel-appropriate form and emitted as an
observable information impulse.

Receiver-side reconstruction is a preferred iterative direction for an
unfamiliar signal: notice enough observable difference, establish
distinguishability, check available sources or reference spaces, examine
structure and place a reconstruction into context.

These topologies do not change entity identity, impose formula dependencies or
claim access to hidden human or machine processing. Established conventions
may abbreviate, reorder or parallelize practical reconstruction. Without a
shared convention, failed grounding may reopen segmentation, structural
analysis, source checking and contextual hypotheses.

Repeated events remain attributable. A repeated event may carry little new
static information relative to a declared baseline while its recurrence,
stagnation, burst or oscillation remains relevant in trajectory, window and
anomaly views. Static value and sequence pattern answer different questions.

## Three bounded examples

### Human and chatbot

A human `A` sends a request and a chatbot `B` answers. The contributions
remain in separate trajectories even when both are visible in one conversation.
On the next turn the roles may reverse without the entities changing identity.
A later relational comparison needs an explicit exchange and pairing rule.

### Unknown Morse-like signal

Repeated pulses may become detectable before their meaning is known. A receiver
may first observe informational movement and distinguish marks from gaps, then
test available references, inspect structure and attempt contextual
reconstruction. A shared convention accelerates decoding but is not required
to observe that a patterned carrier may exist.

Repetition may support an anomaly or contact-attempt hypothesis. It does not by
itself prove acknowledgement, meaning, intent, attack or causal coupling.

### Robots or embodied agents

Two robots may exchange well-formed signals while their spatial trajectories
diverge, or remain geometrically close while their response pace separates.
This motivates keeping staged `R_geom` and optional staged `R_pace` as
parallel later research branches after stable `R0`. Neither is a Layer-1
operator, motion controller or physical safety system.

## Indices, comparability and optional views

Keep the following orders distinct:

- `n` — global event order;
- `k_A` / `k_B` — source-local trajectory positions;
- `j` — relational evaluation position;
- `pi(j) = (k_A(j), k_B(j))` — explicit pairing map.

A predecessor for operator-level `Delta` or `Delta2` comes from the same
declared trajectory under a comparable profile. Operator-level `Sigma`,
`Sigma(Hangar)`, drift and second-order drift are not automatically required
for every application. Select them by layer, use case and declared observation
question.

## Method and implementation boundary

The operator files define what is observed, under which basis and validity
conditions, and how the value and its permitted monadic views are calculated.
Storage schemas, detector configuration, pseudocode, model integration and
test fixtures are separate implementation material and must not redefine the
method.

Read together with:

- [root architecture](../../ARCHITECTURE.md)
- [conceptual note](../../Conceptual-Note.md)
- [shared Hangar method note](../../KSODI-Hangar_V350.md)
- [implementation guardrails](../../IMPLEMENTATION_GUARDRAILS.md)
- [public implementation examples](../../implementation-examples/README.md)

## Layer boundary

Layer 1 ends with attributable operator observations. The complete monadic
Standard-Eval line continues through `Z` and monadic `IK`. `R0` is a
separate gate based on distinguishable `Z` trajectories plus an explicit
pairing or constellation rule. After stable `R0`, `IK_rel`, staged
`R_geom` and optional staged `R_pace` remain parallel branch calculations
with their own bases and profiles.

No Layer-1 operator, single repeated signal, visible shared context or
operator-specific diagnostic establishes relational coherence, resonance,
causality, desirability or authorization to intervene.
