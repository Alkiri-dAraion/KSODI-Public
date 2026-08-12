# Which KSODI Variant Do I Need?

Status: public orientation guide for new readers; not an implementation
specification.

KSODI has three practical entry points. You do not need all of them for every
use case. Choose the smallest variant that fits the observable interaction you
want to work with.

## Quick Choice

| If you want to... | Start with | Why |
| --- | --- | --- |
| Learn the method, improve prompting or create a shared reflection language | [KSODI-Light](./KSODI-Light/README.md) | Light is the human-facing entry layer for users, trainers, teams and simple agent guidance. |
| Observe one interaction trajectory numerically | [KSODI Standard-Eval](./KSODI-Eval-Variants/KSODI-Standard-Eval/README.md) | Standard-Eval observes a monadic line: one party, agent or interaction-state trajectory through `K/S/O/D/I -> Z -> IK`. |
| Compare distinguishable trajectories in a relational setting | [KSODI-Full](./KSODI-Eval-Variants/KSODI-Full/Full_v350/README.md) | Full begins where relational comparability matters: `R0` checks whether distinguishable `Z`-trajectories can be compared before later relational projections are used. |

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
2. Read the root [README](./README.md) for the public release boundary and
   layer map.
3. Choose one branch:
   - [KSODI-Light](./KSODI-Light/README.md) for learning, training and prompt
     guidance.
   - [KSODI Standard-Eval](./KSODI-Eval-Variants/KSODI-Standard-Eval/README.md)
     for monadic numeric observation.
   - [KSODI-Full](./KSODI-Eval-Variants/KSODI-Full/Full_v350/README.md) for
     relational gates, `IK_rel` and later staged R-family layers.
4. Treat historical archives as provenance, not current implementation
   guidance.
