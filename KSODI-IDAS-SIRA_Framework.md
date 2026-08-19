### IDAS Framework – Public v3.50 Orientation Note

*Interactive Dialogue, Analytics & Steering (IDAS)*  
Author: Anne Steinacker-Folkerts, Heiko Folkerts

---

## Version Note

This file is a public orientation note for the current KSODI v3.50 architecture.
It explains how KSODI, SIRA and IDAS relate; it does not replace the canonical
layer files or claim independent mathematical validation of the KSODI
application profile.

The public wording aligns KSODI-Light with the current understanding of a
**reflective working agreement**: KSODI-Light can reflect user input, assistant
output and the shared interaction state. Formal numeric Observer layers remain
separate. A later Controller is a third, separately governed system and is not
created merely by observing an interaction.

The word *Steering* remains part of the historical IDAS name. In the active
architecture it marks a possible later Controller line, not a released control
function inside KSODI-Light, Standard-Eval or KSODI-Full.

---

## Changelog – Public Orientation Update

- **Two-phase interaction model**
  - Phase 1: reflective exploration space
  - Phase 2: productive interaction space

- **Clarified architecture**
  - IDAS = interaction architecture
  - KSODI = structural observation method
  - SIRA = interaction protocol
  - Controller = separate future-work system based on declared Observer
    findings and approved governance corridors

- **Clear separation between**
  - observation (observability)
  - steering (control mechanisms)

- **Clarified KSODI-Light boundary**
  - KSODI-Light = prompt-level reflective working agreement
  - Standard-Eval / Full = formal observer and monitoring layers

---

# IDAS in One Sentence

**IDAS is an architectural framework for keeping reflective guidance,
structured interaction, formal observation and any later governed steering
distinguishable over time.**

It relates the following distinguishable components and roles:

| Component | Role and boundary |
|---|---|
| KSODI-Light | independently usable reflective working agreement |
| KSODI Standard-Eval / KSODI-Full | separately usable Observer architecture |
| SIRA | lightweight interaction-practice protocol |
| IDAS | architectural integration of the distinguishable systems |
| future Controller | depends on declared Observer findings and governance; not independently usable as KSODI |

---

# Architectural Principle

IDAS intentionally separates three systems that may meet in one application
but must not be collapsed into one another:

1. **KSODI-Light — explainability and reflective working agreement**
2. **Observer — formal observability through Standard-Eval / KSODI-Full**
3. **future Controller — optional governed steering based on Observer findings**

KSODI-Light can be used on its own. The Observer can also be used without a
Controller. A Controller is not a third independent reading of the interaction:
it depends on declared Observer outputs, application-specific policies and
approved governance corridors while remaining technically and methodologically
separate from the Observer and the observed entities.

In this public repository, KSODI-Light belongs to the first layer. It can guide
the interaction from inside a user, account, developer or system prompt. It is
not an external observer by itself.

## From Light to Observer Architecture

KSODI-Light is the practical root layer. It makes the shared interaction frame
explicit before formal mathematics or observer infrastructure is introduced.

For simple chatbot architectures, this prompt-level working agreement may be
sufficient. For MoE systems, multi-agent constellations, tool-using agents or
robotic settings, it is usually not enough to rely on local instructions alone.
In those settings, Light can provide orientation inside the agent or user
interaction while Standard-Eval, KSODI-Full or IDAS-level observers provide a
separate monitoring layer.

The Observer does more than collect logs. It asks which interaction conditions
are changing: whether context is drifting, structure is weakening, grounding is
missing, clarity is collapsing, informational movement is becoming repetitive,
or relational coupling between entities is leaving a defined corridor.

The entities remain source-attributed. `A` and `B` identify stable entities or
sources; *sender* and *receiver* describe exchange-relative roles. A human may
send one event and receive the next. The role change does not exchange the
entity trajectories.

This makes IDAS a bridge between AI literacy, interaction design and
governance-oriented AI observability.

---

# Relationship to Existing Evaluation Methods

IDAS and KSODI do **not replace existing evaluation methodologies**.

The framework intentionally builds on concepts already used in:

- prompt evaluation
- interaction analysis
- system observability
- drift detection
- human–computer interaction research

Many mathematical elements therefore rely on established techniques such as:

- vector spaces
- distance measures
- sequence analysis
- statistical distributions

KSODI primarily contributes **a structured way of combining these techniques into a coherent interaction model.**

---

# Two Phases of Interaction

IDAS distinguishes two interaction environments.

## Phase 1 – Reflective Space

A protected exploratory environment.

Characteristics:

- experimentation
- open thinking
- idea generation
- iterative dialogue
- reflective working agreement between user and assistant

This phase does not require formal Observer-based monitoring or governance
evaluation. It may nevertheless become an explicitly declared observation
object in research, safety or quality work. That choice requires a legitimate
purpose, attributable entities, a defined trajectory boundary and appropriate
data governance; exploratory interaction is not automatically exempt from or
subject to observation.

Its purpose is cognitive exploration and interaction clarification.

KSODI-Light may be used here as a prompt-level reflective frame. It can help
user and assistant notice missing context, unclear structure, weak grounding or
answers that do not fit the shared task.

---

## Phase 2 – Productive Interaction Space

A structured environment where observation boundaries and expected outputs can
be prepared explicitly.

Characteristics:

- structured prompts
- analyzable interaction states
- reproducible outputs
- defined observation boundaries

This phase is the ordinary application case for system-level Observer
evaluation because its boundaries and expected outputs can be declared in
advance. It is not the only logically observable interaction space.

---

# KSODI – Structural Observation Model

KSODI provides a structured way to observe interaction states.

Five monadic operators describe observable aspects of one attributable event
inside one declared entity trajectory:

- **K — Context**
- **S — Structure**
- **O — Objectivity / grounding**
- **D — Clarity**
- **I — Information Depth**

At the KSODI-Light level, these operators can be used as coarse orientation
signals, for example on a 0-5 scale per operator.

At the formal observer level, the short labels are mapped to the observable
operator names: **Observable Grounded Objectivity**, **Observable Clarity** and
**Observable Information Impulse**. This is a relation and placement issue, not
a competing definition. The observer does not have direct access to objectivity
or information depth as such; it observes grounding, clarity, impulse and
reconstructability within a declared context and reference space.

In formal observer layers, operator values may be normalized into numeric
representations such as:

```text
[0,1]
```

Together they form an entity- and position-attributed interaction state vector:

```text
Z_A(k_A) = (K_A(k_A), S_A(k_A), O_A(k_A), D_A(k_A), I_A(k_A))
```

From this vector further observable interaction structures can be derived.

The coordinate order `(K,S,O,D,I)` is a stable reporting order, not a claim
that an entity internally executes five universal serial steps. For explanatory
process topology, sender-side formation may be read preferentially as
`K -> S -> O -> D -> I`. When an incoming signal is not yet understood,
receiver-side reconstruction may be read preferentially as
`I -> D -> O -> S -> K`: first notice enough signal to distinguish it, then
test available references, inspect structure and place a reconstruction into
context. Known conventions can shorten or reorder this work. The preferred
topologies do not prove hidden internal processing order.

Global event order `n`, source-local positions `k_A` / `k_B` and a later
relational evaluation index `j` remain distinct. A relational comparison
requires an explicit pairing map `pi(j) = (k_A(j), k_B(j))`; adjacency in a log
or a shared visible context is not sufficient.

At the Light level, K/S/O/D/I may refer to:

- user input,
- assistant output,
- the shared interaction state across a turn.

This is why KSODI-Light should not be read as scoring only the user's prompt.
It is better understood as a reflective working agreement for keeping the
interaction understandable, grounded and task-fit.

## Three Boundary Examples

### Human and chatbot

A human entity `A` sends a request and a chatbot entity `B` answers. Each event
first belongs to its own source-local trajectory. In the next turn `B` may be
the sender and `A` the receiver without either entity changing identity.
Monadic `Z_A(k_A)` and `Z_B(k_B)` remain separate. Only an explicitly declared
exchange or comparison rule may pair positions for `R0` and later relational
observation.

### Unknown Morse-like signal

A receiver notices repeated pulses on a channel. Informational density and
repetition may make the carrier detectable before its meaning is known. The
receiver can distinguish marks and gaps, compare available sources, search for
structure and gradually test contextual reconstructions. A shared Morse
convention would accelerate decoding; it is not required for detecting that a
structured signal may be present.

Repeated patterns may justify an anomaly or contact-attempt hypothesis. They do
not by themselves prove an acknowledgement, decoded meaning, hostile intent,
successful attack or causal coupling. A responding source remains a second
trajectory until the exchange and pairing rule are explicitly declared.

### Robots and embodied agents

Two robots may exchange formally structured task signals while moving through
the same environment. Their response pace can align even while their spatial
trajectories diverge; conversely, they may remain geometrically close while
their communication pace separates. This is why staged `R_geom` and optional
staged `R_pace` are parallel research branches after stable `R0`, not synonyms
and not a serial chain. Neither branch is a motion controller or a physical
safety system.

---

# Observability vs Steering

A central design principle of IDAS is the separation between:

**Observation**

and

**Control**

### Observability

The system describes interaction states.

Examples include:

- state vectors
- interaction distributions
- interaction dynamics
- drift over time

The Observer reports states, movement, applicability and comparison against a
declared reference or corridor. A corridor may encode a normative governance
choice, but the observation result does not decide or intervene by itself.

---

### Steering

Steering is a possible later system function but **not part of the core
observation model**.

Control mechanisms arise only when policies, thresholds, authorization and an
action path are introduced outside the Observer.

Observer-side findings may include:

- drift alerts
- anomaly detection

A separate Controller may then authorize mechanisms such as:

- workflow automation
- fallback behavior

These mechanisms are external to the core observation model. A future
Controller must declare authorization, feedback routing, permitted corridors,
fallbacks and auditability. It must not let the Observer silently redefine its
own evidence or merge with the observed entity.

Prompt-level guidance in KSODI-Light should be distinguished from formal
Observer-based steering. Light can ask for clarification or define simple
fallback behavior inside an instruction frame. External monitoring belongs to
Standard-Eval or KSODI-Full. Auditable intervention belongs only to the
separate future Controller line built on declared Observer findings and
approved governance policy.

---

# SIRA – Interaction Protocol

While KSODI describes interaction structure, SIRA describes **interaction practice**.

SIRA is a lightweight protocol for structured dialogue.

Steps:

- **Signal** – notice or emit interaction markers
- **Intention** – state or test the declared purpose
- **Resonance** – test observable fit in the response, not hidden mutual understanding
- **Adjustment** – allow adaptation and iteration

The protocol does not enforce behavior but encourages structured interaction.

At the KSODI-Light level, SIRA can support the reflective working agreement:
signals are noticed, declared intention is clarified, observable response fit
is checked and the interaction can be adjusted without treating feedback as
blame. A successful SIRA exchange does not prove identical internal meaning,
acknowledgement, causal influence or resonance in a later quantitative
R-family sense.

---

# Emergence and Interaction Dynamics

Complex interaction patterns may emerge when structured observation and interaction protocols are combined.

However:

The framework does **not assume or guarantee emergent properties**.

Emergent behavior is treated as an empirical observation that must be
critically examined. Correlated movement is not yet causality, and a relational
gate or high branch value is not sufficient evidence of beneficial coupling.

---

# Vision

IDAS approaches interaction not only as a linear chat log but as a navigable
interaction space. That live or reconstructed interaction space must not be
confused with a KSODI Hangar view: the Hangar is a typed Observer-side
comparison view over attributable events, windows, trajectories or derived
objects.

In future systems this could enable:

- interaction maps
- project-level interaction analysis
- visual exploration of dialogue structures

As a long-term working hypothesis, KSODI-Light plus external observer layers
may also become relevant for language-, vision-language- or
vision-language-action-based interaction layers in robotic or embodied agent
contexts. This is a future research direction, not a current implementation
claim.

KSODI is not a robotics controller and not a world model. It does not replace
robotics middleware, sensor-level perception, motion planning, collision
avoidance, emergency mechanisms or physical safety systems.

The possible KSODI layer would be communicative and task-related interaction
orientation: whether the system still shares enough context with humans, keeps
the task structure clear, grounds statements or requests sufficiently, and
remains within defined or empirically learned interaction corridors over time.
In embodied or n-entity environments, this would require separate validation and
may require complex observer forms.

The long-term goal is to make human–AI, human-agent and agentic interaction **more transparent, structured and understandable**.
