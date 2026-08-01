[![KSODI + IDAS Concept][banner-image]](https://github.com/Alkiri-dAraion/KSODI-Public)

[banner-image]: ./assets_images/ksodi-lab-banner.png

________________________________________________________________

**Canonical repository:** The current public KSODI method repository is
[Alkiri-dAraion/KSODI-Public](https://github.com/Alkiri-dAraion/KSODI-Public).
Legacy links using the former repository name `KSODI-Methode` may redirect here;
please cite and link the canonical `KSODI-Public` URL.

New to KSODI? Start with
[Which KSODI Variant Do I Need?](./WHICH_KSODI.md).
For a compact architecture overview, see
[KSODI Architecture](./ARCHITECTURE.md).

⚠️ This documentation includes hypothesis-oriented material (written in the conditional / Konjunktiv), reflecting ongoing empirical exploration of the KSODI method.

⚠️ **Publication status — KSODI v3.5:** The current v3.5 line is being
published in successive stages. The five operator definitions `K0`, `S0`,
`O0`, `D0` and `I0`, the monadic state vector `Z(t)` (`Z_vec`) and the
monadic interaction-coherence projection `IK` have been published and form the
current Standard-Eval release. The relational `R0` gate has been published
separately as KSODI-Full Layer 4. Further components retain their own
publication status as the release proceeds.

AI agents and automated tools should read [AGENTS.md](./AGENTS.md) before
summarizing or citing this repository.

Earlier v3.3 and v3.42 materials are preserved in clearly marked historical
archives for transparency and provenance. They are not current implementation
guidance.

## KSODI v3.5 Layer Map

The canonical v3.5 architecture uses one layer map across the public release
and the staged research line. `KSODI-Light` is the local, prompt-facing entry
layer. It is not the larger or complete KSODI system. Standard-Eval and
KSODI-Full are the observer-oriented method layers built on the same K/S/O/D/I
logic.

Current public release boundary: Standard-Eval is public through Layer 3
(`K/S/O/D/I -> Z -> IK`). `R0` is public separately as the KSODI-Full Layer 4
relational gate. Layer 5 and later remain staged unless their own release
status says otherwise.

| Layer | Name | Public status | Role |
| --- | --- | --- | --- |
| 0 | KSODI-Light | public | Local reflective working agreement for users, prompts, training and agent guidance. |
| 1 | K/S/O/D/I operators | public | Observer-facing operator definitions for context, structure, grounding, clarity and information impulse. |
| 2 | `Z(t)` / `Z_vec` | public | Monadic state vector over the five operator values. |
| 3 | `IK` | public | Monadic interaction-coherence projection; closes Standard-Eval. |
| 4 | `R0` / `R_0` gate | public | Relational comparability gate over distinguishable `Z`-trajectories; not a coupling or resonance score. |
| 5 | `IK_rel` | private / staged | Relational coherence projection after stable `R0`. |
| 6 | `R_geom` | private / staged | Geometric coupling in KSODI state space. |
| 7 | `R_pace` | private / staged | Optional pacing overlay where pacing dynamics are explicitly defined. |
| 8 | Future signal-media layer | future research | Voice, Takt, audio, radio, Morse-like or other signal-media work; not part of the current v3.5 release. |

Implementation shortcuts such as "agent layer" or "observer layer" may appear
in older notes, but the table above is the current public orientation map. For
the fuller architecture sketch, see
[KSODI Architecture](./ARCHITECTURE.md) and the detailed
[KSODI v350 Eval Architecture Sketch](./KSODI-Eval-Variants/KSODI_V350_ARCHITECTURE_ASCII.md).

Mini note on `Hangar`: in KSODI, a Hangar view is not the whole private mental
space of a person or agent. It is a method term for the observable or
reconstructable projection space in which stored interaction states,
trajectories, distributions, drift paths or point clouds can be compared over
time. The term emerged during the method's development and is kept because it
names a layer for which there is no exact established replacement in the
current KSODI context.

# KSODI Method

KSODI is a structured observation method for human-AI, agent-agent and n-agent
interaction structures, focussing on explainable governance and observability.
It is embedded in the IDAS framework.

→ See: [KSODI-IDAS-SIRA_Framework](./KSODI-IDAS-SIRA_Framework.md)

The name `KSODI` is intentionally retained from the German development
context. This is not meant as a value judgement between languages. The German
terms helped preserve conceptual precision during the early development of the
method, while English terminology supports international accessibility and
therefore requires explicit definitions. Multilingual discussion, including
French and Chinese perspectives, also helped sharpen the distinctions between
the dimensions.

`CSOCI` may appear only as an English translation mnemonic for the five
KSODI-Light labels. It is not an alternative method name, a separate English
version or an independent provenance line. The method remains `KSODI` in every
language. See the [KSODI English Translation Table](./KSODI-Light/KSODI-CSOCI_EN.md).

Within IDAS, KSODI separates explainability, observability and advanced
interaction analysis (with optional steering) into clearly defined layers, such
as interaction states, interaction coherence and relational R-family
observations over time.

KSODI does **not** evaluate people, personalities or intentions.  
It respects maximum privacy and operates exclusively on observable interaction states.

This repository is organized into clearly separated components with different
purposes. Published method documentation and method materials are covered by the
repository-wide CC BY 4.0 licence unless a file or subfolder explicitly states
otherwise. Separately published implementation code is a distinct work and may
use its own software licence.

## Where KSODI Fits

KSODI is a layered method for making human-AI, human-agent and agent-agent
interaction quality observable, discussable and steering-supportive without
reducing it to single-prompt quality or model accuracy.

It is intended to bridge three practical contexts:

- **AI literacy and training:** KSODI-Light gives users, trainers and
  organizations a shared language for context, structure, grounding, signal
  clarity and information impulse.
- **Prompt-level agent guidance:** KSODI-Light can be embedded into user,
  account, developer or system-prompt settings as a disclosed reflective
  working agreement with lightweight corridors and fallback behavior.
- **AI observability and governance:** KSODI Standard-Eval, KSODI Full and
  IDAS/SIRA-level implementations extend the same operator logic into numeric
  observer layers for drift, coupling, corridor exits and longer-term
  interaction monitoring.

KSODI is not presented as a complete alignment solution. It is a structured way
to reason about interaction conditions, drift, corridors and coupling in a form
that remains understandable for humans while remaining compatible with
machine-readable observation.

## KSODI as a Baseline Radar for Observed Communication

KSODI is not required as a running method for every act of communication.
People, animals, machines and technical systems can exchange signals without a
formal KSODI evaluation layer.

KSODI offers a structured baseline radar when communication is made an object
of methodical observation through these five operators.

This distinction is central. KSODI does not replace communication theory, signal
theory, AI observability, explainability, governance frameworks, safety methods
or domain-specific analysis. It provides a baseline radar for the threshold at
which an event can be reconstructed as an observable communicative signal at
all.

The minimal question is:

> Can this event be observed as a signal that is contextually situated,
> structurally recognizable, sufficiently grounded, clear and stable enough to
> be distinguished from noise, and informationally relevant enough to enter a
> feedback loop?

In KSODI terms, this means asking whether the five operators are sufficiently
visible or reconstructable:

- **Observable Context Completeness:** Is the signal situated in a meaningful or operational frame?
- **Observable Structural Coherence:** Does it show form, pattern, sequence, rhythm, protocol or rule-like organization?
- **Observable Grounded Objectivity:** Can it be stabilized, checked, logged, measured, compared or otherwise grounded beyond pure projection?
- **Observable Clarity:** Can it be distinguished from noise, remain locally stable or dense enough to be reconstructed, and stay operationally connectable?
- **Observable Information Impulse:** Does it make a difference for state, action, interpretation, relation or response?

These operator names reflect the current research-facing terminology. Shorter
KSODI-Light terms may still be used in training contexts, but Standard-Eval and
Full discussions should map them explicitly to the research-facing names.

This does not mean that KSODI explains all communication or defines its only
possible observational entry point. When the five-operator schema is selected,
KSODI can establish a structured baseline from which further methods may be
applied.
Shannon-oriented models may examine transmission, channel and noise.
Watzlawick-oriented views may examine relational and behavioral dynamics.
Schulz von Thun-oriented views may examine message layers and reception sides.
Luhmann-oriented views may examine Anschlussfähigkeit, selection and
autopoietic communication. AI observability may examine traces, logs, tool
calls, retrievals, vector movement, latency or system health. Explainability
methods may examine why a model generated, selected, routed or acted in a
certain way.

KSODI does not replace these layers. It frames the baseline question before and
around them:

> Is there still an observable communicative handshake, and is it stable enough
> to remain connectable?

The KSODI Handshake is a working hypothesis for the transition between monadic
sendability and receiver-side reconstructability. Sender-side observation is
described in the K/S/O/D/I direction, while receiver-side reconstruction is
described in the inverse I/D/O/S/K direction.

This ordering is not claimed as a universal law of communication, nor as an
established theorem from communication theory or signal theory. It is a KSODI
working convention derived from empirical interaction observation and cautiously
related to signal-reception logic: in reception, an informational difference
must first be noticed before it can be distinguished, grounded, structurally
reconstructed and situated in context.

The Handshake is therefore not a sixth operator and not a separate score. It is
the transient, session-bound coupling condition in which an event becomes
sendable, receivable and feedback-capable. In numeric evaluation, the five
operators remain separate tuple components.

This makes KSODI especially relevant for human-AI interaction, agent-agent
communication, multi-agent systems, embodied agents, therapy assistants,
organizational AI teammates and safety-sensitive or governance-sensitive
systems. In such contexts, the issue is not merely whether a system produces
output. The issue is whether communication remains contextually anchored,
structurally coherent, grounded, discernible and stable enough to be interpreted
and informationally useful for the next step.

For simple automation, such as a narrowly scoped device that only follows a
local floor map or reports a small number of fixed states, a full KSODI Observer
may be unnecessary. The communication surface is small, autonomy is limited and
conventional telemetry may be sufficient.

For systems that interact with humans, other agents, organizations, policies,
tools, memories or changing environments, the relevance increases. The more
autonomous, relational, safety-sensitive or context-dependent the system
becomes, the more important it becomes to observe whether the communicative
handshake remains intact.

In observer-supported architectures, KSODI-Light may support local agent
behavior through clarification, uncertainty visibility, corridor awareness and
fallback behavior. KSODI Standard-Eval or KSODI Full may then act as external
Observer layers that monitor trajectories, drift, acceleration, relational
coherence and corridor exits across time.

The Observer does not primarily ask whether a task was completed. It asks
whether communication remains reconstructable, stable and safely connectable. If
the handshake degrades, the system may need to clarify, slow down, correct,
escalate, pause or terminate the interaction.

In this sense, KSODI is not necessary for every communication as an active
procedure. Where its five-operator schema is selected, it can serve as a
baseline radar for signal formation, communicative stability and relational
drift.

## Why These Five Operators? A Cross-Domain Reading Matrix

The following matrix is not an implementation formula. It is a human-readable orientation aid for understanding why the five operators are observed separately.

KSODI does not claim that LLM chats, horse training, whale song and network traffic are the same kind of thing. It also does not claim to decode every signal system automatically. The generality lives in the schema; the work lives in the instantiation.

| Operator | LLM chat | Horse training | Whale song | Honeypot / network noise |
| --- | --- | --- | --- | --- |
| **K - Context** | System prompt, role, goal, format, tools and visible constraints | Environment and situation: arena or trail, position of the human, arousal state, previous lesson | Ocean region, season, group context, depth or migration / mating situation | Network segment, port or service, time-of-day baseline, protocol context |
| **S - Structure** | Formatting, turn sequence, answer organization, tool workflow | Consistent cue sequence, for example weight, leg and rein; stable order of aids | Unit, phrase, theme or song-like hierarchy; repetition patterns | Handshake conformity, packet sequence, session structure |
| **O - Grounding** | Retrieval alignment, attribution to documents, logs or tool outputs | Reaction traceable to a given aid; reference is the trained signal repertoire | Comparison with a defined corpus or observation set | Comparison with signatures, IOC databases or baseline traffic |
| **D - Clarity** | Precise semantics, operational anchors, low dispersion, reconstructable answer | Dosed, unambiguous cue rather than blurred mixed signals | Discriminable sound units against overlapping noise | Distinguishable pattern rather than random bytes; signal-to-noise separation |
| **I - Information Impulse** | New concept, direction change, useful difference versus mere repetition | New impulse or task versus confirmation of an existing lesson | New variation versus stable repetition | Novel pattern versus known scan noise or expected background traffic |
| **Reference space Ref** | System prompt + tools + documents | Training state + repertoire of this horse | Defined corpus / population / observation context | Baseline of this segment + signature or IOC database |

The reference-space row is deliberate: the operators are not filled first. The reference space, abbreviated here as `Ref`, must be defined first, and only then can the operators be interpreted responsibly. `Ref` is kept separate from the R-family of relational or resonance-oriented observations.

A similar pattern can therefore mean different things in different domains. High information impulse with weak grounding could mean unsupported novelty in an LLM answer, an unexpected reaction in horse training, a potential variation in whale-song observation or an anomaly in a honeypot trace. The structural pattern may be comparable; the interpretation remains domain-specific.

This is also why purely technical developer metrics are not enough for every audience. Latency, token use, tool-call success, retrieval time and cost are important, but organizations also need to know whether artificial team members remain understandable, grounded, reconstructable, corrigible and safely connectable over time.

## v3.5 Direction: Observer-Supported Agentic Systems

KSODI v3.5 extends the public KSODI-Light idea toward an observer-supported implementation line for agentic systems.

The current work explores how KSODI-Light can guide local agent behavior while a separate Observer layer monitors trajectories, drift, acceleration, retrieval behavior, vector movement and relational coherence. This is not presented as a finished alignment solution. It is an early research and implementation path for making agentic interaction more observable, reviewable and adjustable under human oversight.

In this architecture, KSODI-Light belongs to the agent side: it may be used as
a user, account, developer, system-prompt or skill-level layer. KSODI
Standard-Eval and KSODI Full belong to the observer side: they are intended to
define, explain and build the external Observer structure. KSODI-Light and the
Observer can each be used independently. When combined, Light provides local
reflective guidance while the Observer provides external, auditable observation
and feedback. An Observer may also evaluate interactions whose participants do
not use KSODI-Light.

A long-term hypothesis is that teams of specialized agents may benefit from observer-supported feedback loops: agents act within their normal role and skill instructions, KSODI-Light supports local reflection and corridor awareness, and the Observer helps detect drift, corridor exits or relational instability across complex traces and vector spaces.

A central implementation challenge is that developers and system architects must remain aware of all relevant layers before building or testing such systems. The choice of input, reference space, retrieval context, tool state and operator mapping directly affects the five KSODI operators and therefore the entire downstream architecture.

In other words: KSODI is not only a scoring surface. It requires careful decisions about what is observed, how input is transformed into K/S/O/D/I, how `Z(t)` is formed, and how later projections, drift metrics, relational gates and visualizations are derived from it.

Historical implementation note: earlier KSODI implementation work in the v3.3 to v3.42 period already explored a Kubernetes / microservice-oriented architecture with operator and Observer components. The v3.5 transition does not discard that carrier architecture. It reworks the method layer: `Z(t)` is made explicit, `IK` is separated from the R-family because coherence is not resonance, `R0` is introduced as a relational gate, and source / reference-space visibility is treated more carefully. Older outputs, dashboards or diagrams should therefore be read as historical implementation context rather than as current v3.5 method specifications.

This work is ongoing and empirical validation is still in progress.

## Roadmap

A cautious research roadmap is maintained separately to describe the current
long-term implementation direction of KSODI, including observer-supported
architectures, human-AI team integration and possible future enterprise-oriented
observer components.

This work is under active research, testing and review. It should not be read as
a production-ready implementation reference or release commitment.

→ See: [KSODI Research Roadmap](./ROADMAP.md)

## Structure

### KSODI-Light
Human-facing and prompt-level variant.
Designed for learning, AI literacy, prompt clarity improvement and lightweight
guidance through disclosed K/S/O/D/I expectations or score corridors.
It can be used as a reflective working agreement in user/account prompts or
embedded by agent creators in developer/system-prompt configurations.
KSODI-Light can reflect user input, assistant output and the shared interaction
state across a turn. Formal observer-based monitoring belongs to Standard-Eval,
KSODI-Full or IDAS/SIRA-level implementations.
→ See: [KSODI-Light](./KSODI-Light)

Licence: [Creative Commons Attribution 4.0 International (CC BY 4.0)](./LICENSE.md)

---

### KSODI Standard-Eval & KSODI Full
Evaluation-oriented and governance-capable variants.  
Designed for numeric observability, drift detection and system-level stability monitoring with optional steering.
KSODI v3.5 is being published in successive stages. The five operator
definitions, the monadic state vector `Z(t)` (`Z_vec`) and monadic `IK` form the
current public Standard-Eval release. The relational `R0` gate is released
separately as KSODI-Full Layer 4. `IK_rel` and later R-family layers remain
outside the current release until their own status is stated explicitly.
→ See: [KSODI-Eval-Variants](./KSODI-Eval-Variants)

Licence: [Creative Commons Attribution 4.0 International (CC BY 4.0)](./LICENSE.md)

---

## About

KSODI focuses on structured observation across five operators:

- Observable Context Completeness
- Observable Structural Coherence
- Observable Grounded Objectivity
- Observable Clarity
- Observable Information Impulse

The broader architectural framework integrating KSODI is referred to as IDAS (Interactive Dialog, Analytics & Steering).

For a public development and contribution overview, see:
[KSODI Development Timeline](./docs/timeline/KSODI_Timeline_since_2024-11.md)
([German version](./docs/timeline/KSODI_Timeline_seit_2024-11.md))

For the project origin note and personal context, see:
[ABOUT.md](./ABOUT.md)

---

## Licensing

The published KSODI method documentation and method materials in this repository
are licensed under the [Creative Commons Attribution 4.0 International licence
(CC BY 4.0)](./LICENSE.md), unless a file or subfolder explicitly states
otherwise.

CC BY 4.0 permits reuse, copying, sharing, adaptation, forks, experimentation
and commercial use. When licensed material is shared, the licence requires
appropriate attribution, a reference to the licence, a source link where
reasonably practicable and an indication of whether changes were made. It does
not permit an adaptation to imply endorsement or official status.

A practical attribution form is:

> KSODI method by Anne Steinacker-Folkerts and Heiko Folkerts, with contributors
> as listed in [Contributors.md](./Contributors.md). Source:
> [KSODI-Public](https://github.com/Alkiri-dAraion/KSODI-Public). Licensed under
> [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Changes, if any,
> should be identified.

Where an individual file identifies additional creators or attribution parties,
that information must also be retained as required by CC BY 4.0.

Research, testing, forks, adaptations and contributions are welcome. Returning
changes or research results to this repository is encouraged but is not a
condition of CC BY 4.0.

### Method documentation and implementation code

This repository defines and documents the KSODI method and gives implementation
orientation. Executable implementations are separate works and may use software
licences.

As of July 2026, a beta implementation of KSODI Standard-Eval is expected in
approximately two to three months, possibly sooner, in
[Patrick Barthelmäs's GitHub account](https://github.com/blackbaddl13). The
implementation is currently expected to use the MIT License. Its own repository
and licence file will be authoritative when it is published.

The earlier decision to limit CC BY 4.0 to KSODI-Light while reserving the Eval
variants is preserved and explained in
[LICENSE_HISTORY.md](./LICENSE_HISTORY.md). The current decision separates the
attribution-based licence for method documentation from the software licence for
implementation code.

For questions about attribution, integration or enterprise use, contact:
ksodi@thevoid.email.

The public KSODI v3.3 and v3.42 materials are preserved in historical archives
for transparency and provenance. They are not current implementation guidance.

KSODI v3.5 is being published in successive stages. The current public
Standard-Eval release extends through the monadic interaction-coherence
projection `IK`, which closes the Standard-Eval line. The relational `R0` gate
is released separately as KSODI-Full Layer 4.
