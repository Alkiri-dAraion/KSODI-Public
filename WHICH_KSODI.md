# Which KSODI Variant Do I Need?

Status: public orientation guide for new readers and external agents; not an
implementation specification.

KSODI exposes three named variants, but they are not three interchangeable or
independent products:

- **KSODI-Light** is an independently usable reflective working method.
- **KSODI Standard-Eval** is the complete monadic numeric Observer line.
- **KSODI-Full** is a relational extension of that Observer line and cannot be
  used without distinguishable monadic source trajectories.
- A future **Controller** is not a fourth KSODI variant. It may act on Observer
  findings only through separately declared governance corridors.

Choose the lowest abstraction level that answers the question. Do not infer a
formal measurement merely because Light is used inside a conversation, and do
not begin relational calculation before the monadic source states are
distinguishable.

For the complete Layer 0-8 topology, branch point after `Z` and current
publication boundary, see the root
[KSODI v350 Architecture Sketch](./KSODI_V350_ARCHITECTURE_ASCII.md).

## Quick Choice

| Question / purpose | Start with | Abstraction level | Dependency and infrastructure | What it provides |
| --- | --- | --- | --- | --- |
| “How can I formulate, reflect or improve this interaction?” | [KSODI-Light](./KSODI-Light/README.md) | Layer 0: reflective language and local guidance | Independently usable. No external Observer is required; it can be used in one chat, an account prompt or a suitable developer/system prompt. | Prompt improvement, reflective self-alignment, lightweight local steering and a shared K/S/O/D/I vocabulary. No formal state or relational calculation. |
| “What is observably happening in this one identified source trajectory?” | [KSODI Standard-Eval](./KSODI-Eval-Variants/KSODI-Standard-Eval/README.md) | Layers 1-3: monadic numeric observation | Requires a separate Observer architecture, source attribution, event and trajectory records, declared bases and profiles. | Per-source `K/S/O/D/I -> Z_A(k_A) -> IK_A(k_A)`, including optional typed drift, window and Hangar views. |
| “Are two or more distinguishable trajectories eligible for relational comparison, and what can then be observed?” | [KSODI-Full](./KSODI-Eval-Variants/KSODI-Full/Full_v350/README.md) | Layers 4-8: relational Observer extension; currently public through Layer 5 | Not standalone. It consumes distinguishable Layer-1/2 trajectories, an explicit pairing or constellation, reference spaces, windows and policy/profile declarations. | The `R0` comparability gate, then public `IK_rel` and separately staged parallel R-family branches. Passing `R0` does not itself prove coupling, meaning or causality. |

## The Four Responsibility Levels

### 1. KSODI-Light: work within an interaction

Light is a reflective working agreement on the prompt/agent side. It can help a
human, chatbot or other suitable agent inspect visible context, structure,
grounding, clarity and information impulse. It may be used reciprocally or
asymmetrically inside a dyadic setting, but it does not calculate formal
monadic or relational Observer values.

### 2. Standard-Eval: observe one source at a time

Standard-Eval reconstructs source-attributed events and trajectories. Entity or
source `A` remains distinguishable from `B`; sender and receiver are
exchange-relative roles and may reverse without changing those identities.

The fixed coordinate order is

```text
(K, S, O, D, I)
```

It is a reporting convention, not a causal sequence. Sender-side formation may
often be described by `K -> S -> O -> D -> I`; investigation of an unknown
incoming signal may use `I -> D -> O -> S -> K` as a preferred iterative
reconstruction direction. These are retained process hypotheses where the
entity, convention, channel and use case support them, not universal laws.

For a source-local position `k_A`, the Observer builds one monadic state
`Z_A(k_A)` and may project it to monadic coherence `IK_A(k_A)`.
Standard-Eval ends with `IK`.

### 3. KSODI-Full: compare only after distinction

KSODI-Full begins methodically at Layer 4, but it depends on distinguishable
`Z` trajectories produced through Layers 1 and 2. After `Z`, the
architecture branches: monadic `IK` is Layer 3, while relational `R0` is
evaluated in parallel as Layer 4. `R0` is not calculated from `IK`.

For relational evaluation index `j`, the pairing map
`pi(j) = (k_A(j), k_B(j))` declares which source-local positions are compared.
An n-adic setting requires an explicit constellation rather than an implied
shared trajectory.

After stable `R0`, `IK_rel`, staged `R_geom` and staged optional
`R_pace` are parallel branches with their own bases, profiles, applicability
rules and weights. One branch does not validate or consume another unless a
later method definition states so explicitly.

### 4. Future Controller: act under governance

Standard-Eval and KSODI-Full are Observer architectures. They do not decide,
intervene or steer by themselves. Automated alignment, feedback routing or
intervention requires a separate Controller architecture, declared governance
corridors and responsibility for actions. The Controller remains a future-work
publication line and depends on validated Observer findings; it must not be
collapsed into Light or the Observer.

Prompt-level self-alignment and lightweight local steering in KSODI-Light are
not system-level Controller steering.

## What the Relational Terms Mean

`Monadic` means that one identified source trajectory is observed on its own.
A visible external reference space may be used where an operator profile permits
it; this does not merge sources or create a relational value.

`Dyadic` means that two distinguishable trajectories are explicitly paired
for comparison, for example a human and chatbot, robot A and robot B, or an
unknown Morse-like source and a responding receiver. Roles may reverse while
entity/source identities remain stable or explicitly provisional.

`N-adic` means that more than two distinguishable trajectories are included
through a declared constellation, for example several robots, agents or signal
sources. Their records do not become one source merely because they share an
environment or channel.

`Relational` means that KSODI asks whether distinguishable trajectories are
eligible for a declared comparison and, after the gate, which relational
projections are defined. It does not mean that `R0` proves contact,
acknowledgement, shared meaning, coupling or causality.

## Three Short Examples

### Human and chatbot

Use Light if the goal is to improve the working exchange. Use Standard-Eval if
a separate Observer should reconstruct the human and chatbot events as
distinct monadic trajectories. Use Full only when a declared pairing asks a
relational question about those already distinguishable trajectories.

### Unknown Morse-like signal

A single provisionally attributable pulse or pulse sequence can already be
examined with Standard-Eval. One identified signal event requires neither a
predecessor nor a second trajectory: the Observer can evaluate the applicable
Layer-1 coordinates and, where the complete basis is available, construct its
monadic `Z` and optional `IK`. Repeated pulses may form one source-local
trajectory and support drift, window and anomaly observation. This can be
relevant for security-oriented detection and reconstruction even while the
emitter, convention or meaning remain unknown.

KSODI-Full is not triggered merely because a second trajectory exists. It
becomes applicable only when the observation question explicitly compares two
or more distinguishable trajectories through a declared pairing or
constellation and the `R0` gate. A reply edge is not proof of acknowledgement,
successful decoding, coupling or attack.

### Robots

Each robot first needs its own source-attributed trajectory. After `R0`, two
robots may show similar pacing while moving apart geometrically, or remain
geometrically close while their pacing diverges. This is why relational
coherence, geometry and pace require separate parallel branches.

## Implementation Status

This repository documents the KSODI method and gives implementation
orientation. It is not itself the full executable implementation.

Before storing operator values, constructing trajectories or evaluating
relational layers, read the root
[KSODI Implementation Guardrails](./IMPLEMENTATION_GUARDRAILS.md). They define
the minimum source-attribution, evaluation-unit, pairing, applicability and
partial-operator conditions required across the Observer variants.

Public implementation-transfer examples are kept under
[implementation-examples](./KSODI-Eval-Variants/implementation-examples/README.md),
including a
[human-chatbot Observer setting](./KSODI-Eval-Variants/implementation-examples/chatbot-human-observer_v350/README.md).
These examples explain transfer logic but are not production systems.

The next implementation-alignment phase is planned in
[Patrick Barthelmäs's GitHub context](https://github.com/blackbaddl13). Anne
will prepare method-alignment contributions with ELKIM through a fork and
review branch; Patrick retains implementation-side merge, release and
software-licence control. The implementation repository and its licence will
be authoritative for executable code; this repository remains authoritative
for the released method.

## Minimal Reading Path

1. Read this guide and identify the actual question: reflection, monadic
   observation or relational comparison.
2. Read the root [architecture sketch](./KSODI_V350_ARCHITECTURE_ASCII.md) for
   the Layer 0-8 map, branch point, dependencies and publication boundary.
3. Choose the correct entry:
   - [KSODI-Light](./KSODI-Light/README.md) for an independently usable
     reflective working method;
   - [KSODI Standard-Eval](./KSODI-Eval-Variants/KSODI-Standard-Eval/README.md)
     for the complete monadic Observer line;
   - [KSODI-Full](./KSODI-Eval-Variants/KSODI-Full/Full_v350/README.md) only as
     a relational extension of distinguishable monadic trajectories.
4. Read the [implementation guardrails](./IMPLEMENTATION_GUARDRAILS.md) before
   storing evaluations or translating the Observer method into code.
5. Treat historical archives as provenance, not current implementation
   guidance.
