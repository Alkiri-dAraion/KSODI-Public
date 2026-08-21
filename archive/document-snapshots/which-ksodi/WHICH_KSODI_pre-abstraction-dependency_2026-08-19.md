# Which KSODI Variant Do I Need?

Status: public orientation guide for new readers; not an implementation
specification.

KSODI has three practical entry points. You do not need all of them for every
use case. Choose the smallest variant that fits the observable interaction you
want to work with.

For the complete Layer 0-8 topology, branch point after `Z(t)` and current
publication boundary, see the root
[KSODI v350 Architecture Sketch](./KSODI_V350_ARCHITECTURE_ASCII.md).

## Quick Choice

| If you want to... | Start with | Canonical layers | Required infrastructure | Effect / function |
| --- | --- | --- | --- | --- |
| Learn the method, improve prompting or create a shared reflection language | [KSODI-Light](./KSODI-Light/README.md) | Layer 0 | No special infrastructure. It can be used in one chat, through an account prompt or embedded in a developer / system prompt on any suitable model or platform. | Prompt improvement, reflective self-alignment, lightweight local steering and agent guidance. |
| Observe one interaction trajectory numerically | [KSODI Standard-Eval](./KSODI-Eval-Variants/KSODI-Standard-Eval/README.md) | Layers 1-3 | A separate Observer architecture that reconstructs and evaluates observable states and trajectories. | Pure observability across the monadic line `K/S/O/D/I -> Z -> IK`, including drift, stability and monadic coherence. |
| Compare distinguishable trajectories in a relational setting | [KSODI-Full](./KSODI-Eval-Variants/KSODI-Full/Full_v350/README.md) | Layers 4-8; currently public through Layer 5 | An Observer architecture with distinguishable `Z`-trajectories, declared reference spaces and observation windows. | Pure relational observability beginning with the `R0` Handshake gate, followed by `IK_rel` and the further R-family. |

## Architecture Boundary

KSODI-Full begins methodically at Layer 4, but it consumes distinguishable
`Z`-trajectories produced through Layers 1 and 2. After `Z(t)`, the architecture
branches: monadic `IK` is Layer 3, while relational `R0` is evaluated in
parallel as Layer 4. `R0` is not calculated from `IK`.

KSODI Standard-Eval and KSODI-Full are observability architectures. They do not
decide, intervene or steer by themselves. Automated alignment, feedback routing
or intervention requires a separate Controller architecture with declared
governance corridors. This Controller architecture remains a Future-Work
publication line.

Prompt-level self-alignment and lightweight local steering in KSODI-Light must
not be confused with system-level Controller steering.

## What The Words Mean

`Observable interaction` means that KSODI works only with what can be seen,
logged, reconstructed, measured, compared or otherwise grounded. It does not
evaluate a person's mind, character, intention or hidden inner state.

`Monadic` means that one interaction trajectory is observed on its own. In
Standard-Eval, the five operators become a state vector `Z(t)`, and `IK`
projects that state onto a monadic interaction-coherence axis. Standard-Eval
ends with `IK`.

`Dyadic` means that two distinguishable trajectories are compared, for example
human and chatbot, agent A and agent B, or user side and system side.

KSODI-Light may be used within a dyadic interaction and may support
reciprocal or asymmetric lightweight self-steering. At the Light level,
"dyadic" describes the interaction setting and the placement of reflection; it
does not mean that KSODI-Light performs formal dyadic measurement. Formal
numerical comparison of distinguishable trajectories belongs to KSODI-Full and
begins at the R0 gate.

`N-adic` means that more than two distinguishable trajectories are involved,
for example a multi-agent system, a human team with AI support, or a larger
agentic workflow.

`Relational` means that KSODI no longer asks only whether one trajectory is
internally coherent. It asks whether distinguishable trajectories are
comparable, relatable or coupled in a defined way. In v3.5, `R0` is the
relational gate: it checks comparability before later relational layers such as
`IK_rel` or `R_geom` are considered.

## Typical Starting Points

Use **KSODI-Light** if you are learning KSODI, teaching AI literacy, improving
prompts, setting up a reflective working agreement, or giving an assistant a
simple way to notice context, structure, grounding, clarity and information
impulse.

Use **KSODI Standard-Eval** if you are building or reviewing an Observer for a
single observable trajectory. This is the public v3.5 numeric release line:
Layer 1 operators, Layer 2 `Z(t)` and Layer 3 `IK`.

Use **KSODI-Full** if your system has distinguishable interaction sides and you
need to decide whether relational comparison is methodically meaningful. The
public v3.5 Full release currently includes `R0` as Layer 4 and `IK_rel` as
Layer 5. `R_geom`, `R_pace` and later R-family work remain staged unless their
own release status states otherwise.

## Implementation Status

This repository documents the KSODI method and gives implementation
orientation. It is not itself the full executable implementation.

Before storing operator values, constructing trajectories or evaluating
relational layers, read the root
[KSODI Implementation Guardrails](./IMPLEMENTATION_GUARDRAILS.md). They define
the minimum source-attribution, evaluation-unit, pairing and partial-operator
conditions required across the variants.

Public implementation-transfer examples are kept under
[implementation-examples](./KSODI-Eval-Variants/implementation-examples/README.md),
including a
[human-chatbot Observer setting](./KSODI-Eval-Variants/implementation-examples/chatbot-human-observer_v350/README.md).
These examples explain transfer logic but are not production systems.

A separately published implementation is expected from
[Patrick Barthelmäs's GitHub account](https://github.com/blackbaddl13) when it
is ready. Its own repository and licence file will be authoritative for
executable code.

## Minimal Reading Path

1. Read this guide.
2. Read the root [architecture sketch](./KSODI_V350_ARCHITECTURE_ASCII.md) for
   the canonical Layer 0-8 map, branch point and publication boundary.
3. Read the [implementation guardrails](./IMPLEMENTATION_GUARDRAILS.md) before
   storing evaluations or translating the method into code.
4. Choose one branch:
   - [KSODI-Light](./KSODI-Light/README.md) for learning, training and prompt
     guidance.
   - [KSODI Standard-Eval](./KSODI-Eval-Variants/KSODI-Standard-Eval/README.md)
     for monadic numeric observation.
   - [KSODI-Full](./KSODI-Eval-Variants/KSODI-Full/Full_v350/README.md) for
     relational gates, `IK_rel` and later staged R-family layers.
5. Treat historical archives as provenance, not current implementation
   guidance.
