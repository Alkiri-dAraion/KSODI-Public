# KSODI Standard-Eval & Full

This directory contains the evaluation-oriented variants of the KSODI framework.

These variants extend the same K/S/O/D/I operator logic that appears in
KSODI-Light, but they do so as formal observer-oriented layers. KSODI-Light can
support a reflective working agreement inside an interaction. Standard-Eval and
KSODI-Full are intended to observe trajectories, drift, coupling and structural
stability from outside the prompt.

## Operator Names in Light and Eval

KSODI-Light and KSODI Standard-Eval / Full use slightly different operator
names because they operate from different positions.

KSODI-Light uses short, human-facing labels for prompt work, training and local
reflection. They name practical working questions such as context, structure,
objectifiability, clarity and information impulse.

Standard-Eval and KSODI-Full use observer-facing names because this layer must
describe what can be reconstructed from exposed interaction states, reference
spaces, trajectories and audit material:

- **Observable Context Completeness**
- **Observable Structural Coherence**
- **Observable Grounded Objectivity**
- **Observable Clarity**
- **Observable Information Impulse**

The difference is not a competing definition. It is a layer and viewpoint
distinction. Light asks from inside the interaction whether the working frame is
usable. Eval asks from outside the prompt what can be observed, reconstructed,
compared and monitored.

For the human-facing Light terminology and prompt-level use, see
[KSODI-Light](../KSODI-Light/README.md).

These components are designed for:

- numeric interaction observation
- drift detection
- agent-system monitoring
- governance and compliance contexts
- long-term structural stability analysis

## Observer Role in the v3.5 Direction

In the current v3.5 direction, KSODI Standard-Eval and KSODI-Full are the layers where the external Observer structure is explained and developed.

KSODI-Light belongs to the local agent side: it may guide an agent through user, account, developer, system-prompt or skill-level instructions. Standard-Eval and KSODI-Full belong to the observer side: they are intended to monitor what happens from outside the prompt and across time.

The current public v350 architecture sketch is maintained at the Eval-Variants
root because it spans Standard-Eval and the R-family / KSODI-Full research
boundary:

[`KSODI_V350_ARCHITECTURE_ASCII.md`](./KSODI_V350_ARCHITECTURE_ASCII.md)

The shared v350 method note for Sigma, Sigma(Hangar), drift and distribution
views is also maintained at the Eval-Variants root because it spans
Standard-Eval and KSODI-Full:

[`Hangar_350.md`](./Hangar_350.md)

Public implementation-transfer examples are kept separate from the canonical
method folders. They are orientation aids, not customer implementations:

[`implementation-examples`](./implementation-examples/README.md)

The Observer layer may use existing observability material such as traces, threads, chunks, retrieval records, vector similarity, generation parameters, evaluation signals and tool-call logs. KSODI adds an additional interaction-oriented observation layer around K/S/O/D/I, `Z(t)`, drift, acceleration, interaction coherence and relational or resonance-family structures.

A central challenge is that developers and architects must understand how the selected input, reference space, retrieval context, tool state and operator mapping affect the five KSODI operators. These choices shape `Z(t)` and all later projections, drift metrics, relational gates and visualizations. If the input frame is wrong, the observer may not merely measure badly; it may observe a different system state than intended.

This is why the public 3.3 material should not be used as an implementation reference. The v3.5 line is intended to clarify these layer boundaries before implementation and testing.

## Variants

### KSODI Standard-Eval
Model-agnostic numeric evaluation layer for monadic observation.
Designed for operators, `Z`, `IK`, aggregation and Delta / Delta2 views.

### KSODI-Full
Extended analytical layer for relational gates, dyadic / n-adic observation and
R-family structures such as `R_geom`, `R_pace` and future signal-media work.
Explanatory and architectural – never decision-making.

## Intended Use

These variants are intended for:

- enterprise environments
- public administration
- regulated domains
- continuous, autonomous or multi-agent AI systems

## Transparency

Earlier operator drafts (e.g. v0.8) are preserved for transparency.
They reflect exploratory stages and are not representative of the current implementation architecture.

The public KSODI 3.3 materials are also not recommended as an implementation
reference. They contain known structural issues, including:

- an objectivity operator behavior where measurement can collapse to 0 / not
  measurable when no external data source or web access is connected
- ambiguous or duplicated variable handling in parts of the public draft
- unresolved public separation between Z, IK, R0, IK_rel and the R-family of relational observation variants

A revised KSODI 3.5 reference specification is currently maintained privately
and described in the current paper draft. It refines the separation between
interaction coherence, relational comparability and resonance-family observation and will only be published after final
testing and review.

Some public v3.3 files already contain placeholders or preliminary glossary
notes for Z, IK and R0. These files are not normative and should not be treated
as a complete or tested specification.

Historical Observer visualizations are preserved under
[`archive_assets_historical-observer-v342`](./archive_assets_historical-observer-v342/README.md).
They show that implementation and dashboard work already existed in the v3.3 to
v3.42 line, while also making visible why the v3.5 correction needs a clearer
separation between interaction coherence and resonance-family observation, plus
clearer reference-space and `O0` interpretation.

Until then, this directory should be used for conceptual review, discussion and
research orientation only.

## License

Commercial license only.  
All rights reserved.

No usage, distribution or modification is permitted  
without prior written agreement from the copyright holders.

For licensing inquiries, please contact:
ksodi@thevoid.email

---

© 2026 Anne Steinacker-Folkerts & Heiko Folkerts
All rights reserved
