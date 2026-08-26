# KSODI Research Roadmap

> Scope: research direction, not a product announcement or release commitment

## Why this roadmap exists

KSODI began in sustained human-AI interaction work. The method has since been
abstracted beyond that origin: it observes source-attributed events and
trajectories of distinguishable entities wherever an applicable carrier,
measurement basis and observation profile can be declared.

Human-AI interaction remains an important and accessible application case. It
is not the boundary of the method. Depending on the domain, an entity may be a
human, an artificial agent, a machine, an animal, an organization or another
distinguishable signal-producing or signal-processing unit.

The current public repository focuses on the methodological layer, KSODI-Light
and cautious public orientation toward observer-supported systems.

This roadmap describes the current research and implementation direction of
KSODI in a more explicit way.

It is not a promise of production readiness. It is not a delivery commitment. It
is not a final architecture specification.

It is a transparent statement of direction.

## Abstraction and dependency boundaries

The roadmap separates five levels that must not be collapsed:

| Level | Question | Boundary |
| --- | --- | --- |
| Observed reality | Which attributable event from which entity is observed? | Entity identity, target event, source and trajectory remain distinguishable. Sender and receiver are exchange-relative roles, not permanent entity types. |
| Monadic method representation | How is one entity's attributable event reconstructed? | Applicable `K/S/O/D/I` values form `Z_A(k)`; monadic `IK_A(k)` and monadic drift remain inside the same declared trajectory. |
| Relational observation | When may distinguishable trajectories be compared? | Relational interpretation begins only at separately declared `R0(A,B,...)`. Stable `R0` gates `IK_rel`; later R-family work requires its own release and evidence boundary. |
| Operational architecture | Where do local guidance, observation and intervention belong? | KSODI-Light and an Observer may each operate independently. A future Controller depends on declared Observer findings and approved governance corridors while remaining separate from the Observer. |
| Domain instantiation | How is the general schema made usable here? | Each application defines its own targets, carriers, profiles, visible reference spaces, windows and governance conditions. Similar patterns do not make different domains numerically interchangeable. |

The canonical coordinate order `Z_A(k) = (K_A,S_A,O_A,D_A,I_A)` is not a
causal calculation chain. Sender-side formation may be described as
`K -> S -> O -> D -> I`; receiver-side reconstruction may use
`I -> D -> O -> S -> K` as a preferred iterative direction. These
role-relative process descriptions do not merge the entities or replace the
independent operator definitions.

In a human-chatbot setting, one human contribution and one chatbot contribution
remain separate target events with separate source-local trajectories. A reply
link may declare a possible relation; only `R0` determines whether the
distinguishable trajectories are stable enough for relational comparison.

The same boundary applies outside language. Two industrial robots may share a
machine hall, timing system and production goal while their work cycles remain
separate monadic trajectories. They form an evaluated dyad only where a process
relation is explicitly declared and the required trajectory evidence is
available. Shared surroundings alone do not create relational coherence.

## Core direction

A long-term direction of KSODI is the exploration of deployable
observer-supported components for environments in which distinguishable
entities produce, receive or transform observable signals. Application cases
include artificial agents interacting with:

- humans,
- teams,
- documents,
- workflows,
- business systems,
- compliance functions,
- governance structures,
- and other agents.

The goal is not to monitor living beings as persons, infer hidden internal
states or assign one entity's observations to another. The goal is to observe
whether attributable events and source-local trajectories remain
reconstructable, reviewable and stable, and whether separately declared
relations remain comparable across hybrid environments.

Entity identity remains stable across an observation. Sender and receiver are
roles relative to a particular exchange and may reverse in the next event.
Shared context, platform, task or timing does not by itself merge sources,
trajectories or evaluation units.

In other words:

> KSODI is being explored as a cross-layer observation method for communicative
> connectability, drift detection and process coherence.

## What KSODI is meant to complement

KSODI is not intended to replace:

- communication theory,
- enterprise governance,
- compliance frameworks,
- security measures,
- classical observability,
- explainability methods,
- or platform-native monitoring from providers such as Microsoft, SAP, IBM or
  others.

Instead, KSODI is being explored as a complementary layer.

Existing platforms may tell an organization:

- who acted,
- what system was used,
- which data source was accessed,
- which workflow was triggered,
- which log event occurred,
- or which policy applied.

KSODI asks an additional question:

> Did the communication and process transitions remain contextually anchored,
> structurally coherent, sufficiently grounded, distinct enough to be
> interpretable and information-bearing enough to remain connectable?

This is especially relevant where multiple platforms, departments, workflows,
prompts, tools and human review points interact.

## Current methodological assumption

The current KSODI line assumes that communication and drift problems may arise
inside one source-local trajectory or across a separately declared relation.
They are not presumed to arise from a merged interaction state.

Potential observation points include:

- transitions between systems,
- exchanges between humans and agents,
- prompt-to-workflow transformations,
- document transformations,
- local corrections and their downstream effects,
- and boundaries between governance functions inside one organization.

These examples name possible observation settings. They do not define the
entities automatically. A workflow, prompt, document, tool, organization and
human may occupy different methodological roles: target event, carrier,
context, source material, observed entity, Observer input or governance
condition. Each role must be declared for the selected use case.

For that reason, KSODI is being developed as a method that first reconstructs
attributable monadic states and trajectories across architectural layers.
Relational comparison opens only after the participating trajectories remain
distinguishable and satisfy the separately declared `R0` gate.

## Intended future implementation pattern

A future KSODI-based Observer deployment would not start by applying a
universal score to everything. It would begin with a bounded observation
question and an explicitly declared evaluation unit.

Examples:

- What must remain connectable in this workflow?
- Which handoff or transition is most risk-sensitive?
- Which kind of drift matters here?
- Which human oversight point may reduce or increase uncertainty?
- Where do we need earlier visibility before a problem becomes a compliance or
  process failure?

Before calculation, the deployment must identify at least:

- the attributable target event `e_A(k)`,
- the source entity `A` and its declared trajectory,
- the carrier and detector conditions,
- context material that informs evaluation without becoming the target event,
- operator-specific measurement profiles,
- and visible reference spaces where the operator definition requires them.

Only then can the five observer-facing KSODI operators be reconstructed:

- **K — Observable Context Completeness**
- **S — Observable Structural Coherence**
- **O — Observable Grounded Objectivity**
- **D — Observable Clarity**
- **I — Observable Information Impulse**

KSODI-Light uses shorter, human-facing working questions: Is there enough
context? Is the contribution structured? Is it sufficiently grounded or
objectifiable for the task? Is it clear and distinguishable enough to continue?
Does it add an information impulse? These are reflective prompts, not alternate
formal operator definitions.

For one entity and one attributable event, the monadic path is:

```text
e_A(k) -> K_A(k) / S_A(k) / O_A(k) / D_A(k) / I_A(k)
       -> Z_A(k)
       -> IK_A(k)
```

Applicable operator values are reconstructed under their own measurement bases
and profiles. `Delta Z`, `Delta IK` and other monadic changes compare only
comparable positions inside the same declared trajectory.

Relational observation is a separate branch. `R0(A,B,...)` checks whether
distinguishable `Z`-trajectories are stable enough for comparison. It does not
create the relation, merge the sources or establish coupling. Only stable
`R0` gates `IK_rel`; later R-family constructs require their own declared
status, profiles and observation windows.

The broader KSODI mathematics and Observer layers may then derive
domain-specific findings across time, transitions and larger architectural
spaces. Cross-domain use preserves the schema, not automatic numeric
comparability.

## Governance Boundary Between Light, Observer and Controller

KSODI-Light, the Observer architecture and any future Controller are separate
method and governance roles. They are not interchangeable deployment names.

KSODI-Light is local guidance for reflection, prompting, training and
interaction hygiene. It may be used independently, with or without an external
Observer. It supports work inside the locally available frame; it does not
perform formal Observer calculation.

KSODI Standard-Eval and KSODI-Full are external observer-oriented method
layers. An Observer may evaluate interactions whose participants do not use
KSODI-Light, and it may operate without a Controller. In that case it
reconstructs and reports attributable states, trajectories, drift and
separately gated relational conditions. It does not decide, intervene or steer.

A future Controller is not a standalone KSODI variant. It depends on declared
Observer findings, explicit policy authority and pre-approved governance
corridors. It may route feedback, escalation or intervention decisions while
remaining architecturally separate from the Observer and from the observed
entities.

This is a governance boundary, not merely a software pattern. Observer output
must not be fed back through an undeclared loop that lets the Observer alter
the conditions it then evaluates. Human responsibility, auditability, access
control and intervention authority remain separately declared.

## Human-AI team integration

One major application direction is the safe integration of artificial agents
into human teams. It is an application of the entity-general method, not its
ontological boundary.

This does **not** mean that KSODI is intended for employee surveillance. It
means that KSODI may help organizations observe whether communication between
artificial agents and human teams remains:

- role-consistent,
- context-aware,
- reviewable,
- grounded in sources or process reality,
- and usable for further decision-making.

This may become important in settings such as:

- AI assistants inside departments,
- agent-supported document workflows,
- human-agent collaboration in operations,
- internal copilots,
- multi-agent systems,
- and hybrid enterprise processes.

## Human-in-the-loop and human oversight

KSODI is also being explored as a way to better understand human-in-the-loop
(HITL) and human oversight (HO).

Human involvement is often necessary and valuable. But human intervention does
not automatically reduce risk.

A human review step may:

- clarify context,
- correct a wrong path,
- improve source grounding,
- stop unsafe continuation.

But it may also:

- introduce a new prompt problem,
- shift the processing context,
- reduce traceability,
- overlook artefacts,
- or create downstream drift through a local fix.

A human reviewer is not automatically part of the evaluated relation. Human
oversight becomes observable KSODI material only where a specific intervention
is included as an attributable target event with its own source and trajectory
identity. Otherwise, the human remains an external reviewer, decision-maker or
Controller.

The aim is not to remove human judgement. The aim is to make it easier to
observe whether explicitly included interventions are followed by stronger or
weaker communicative connectability. Temporal succession and correlation may
motivate investigation; they do not establish that the intervention caused the
change.

## Privacy and data minimisation direction

KSODI is being developed with a privacy-preserving direction in mind.

The method does not require the permanent storage of full natural-language
conversations in order to observe long-term drift.

Natural language may be needed temporarily to derive and validate the five
operator states, support legally required review, or enable bounded auditability.
However, where possible and legally appropriate, long-term observation should
rely primarily on reduced observation data such as:

- operator values,
- trajectories,
- drift indicators,
- aggregation windows,
- corridor events,
- and audit metadata.

Reduced observation data is not automatically anonymous or harmless.
Operator vectors, trajectories, timestamps, provenance and relational metadata
may remain sensitive or personally identifiable when they can be linked to an
entity, account, role or workflow.

This means:

- raw language should only be retained for the legally permitted and
  purpose-bound period,
- long-term analytical value should come primarily from reduced KSODI state data,
- retention periods, deletion rules and access rights must be defined by the
  deploying organization,
- and KSODI should not be used to create personality profiles or permanent
  behavioural dossiers.

This design direction is intended to support privacy-by-design, data
minimisation and responsible governance.

## Possible future deliverables

The following future directions are currently being explored:

- observer-supported KSODI agent patterns,
- deployable KSODI observer components,
- enterprise-oriented integration patterns,
- configurable operator mappings for different domains,
- drift and connectability monitoring across workflows,
- visualizations for communicative state transitions,
- and human-readable governance surfaces.

Possible future examples may include:

- operator profiles,
- drift trajectories,
- heatmaps,
- workflow transition views,
- multi-agent views that preserve source-local trajectories and open
  relational projections only after their exact compatible open `R0` contract,
- or cross-platform communication diagnostics.

These are research directions, not currently announced deliverables.

## Visual roadmap (planned)

This document may later be extended with explanatory visuals, for example:

- architecture sketches,
- operator heatmaps,
- coherence or drift plots,
- example workflow handoff views,
- and observer-layer diagrams.

The intention is to make the abstract construct easier to understand without
reducing the method to a simplistic dashboard metaphor.

## Current Work

The work is ongoing.

Historical implementation work and practice-based use have produced
substantive intermediate observations, especially around:

- KSODI-Light,
- observer-supported architectures,
- separation of local agent guidance and external observation,
- and the application of KSODI to communicative drift across different contexts.

These observations support feasibility and further investigation. They are not
controlled proof of universal performance or causal effectiveness.

However:

- no production-ready enterprise Observer implementation is currently announced,
- no fixed public release date is defined,
- and further testing, documentation, security review and validation are still
  required.

Progress may move faster in some areas and slower in others. For that reason,
the project does not currently commit to a precise timeline.

## Guardrail

KSODI should not be understood as a universal surveillance mechanism or as a
replacement for governance, compliance, observability or explainability.

Its intended role is narrower and more specific:

> KSODI is being developed as a method for observing source-attributed events,
> communicative connectability and drift across distinguishable entity
> trajectories. Human-agent and agent-agent interactions are important
> application cases, not the boundary of the method.

## Current public/public-private separation

This public repository contains method orientation and selected public
documentation.

More advanced mathematical, architectural and implementation-related work is
currently being refined in private workspaces and may be published later in
carefully reviewed form.

Not every internal experiment or implementation detail will automatically become
public.

## Closing note

KSODI remains a research-driven method under active refinement.

The current roadmap reflects a careful direction:

- preserve entity, event, source and trajectory identity,
- keep method, relational observation, operational architecture and domain
  instantiation distinguishable,
- avoid overclaiming,
- support responsible integration of artificial agents,
- maintain human reviewability,
- and build toward architectures that help organizations detect where
  communication and process coherence begin to degrade.
