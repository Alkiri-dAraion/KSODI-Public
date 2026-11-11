# KSODI v3.51 Glossary and Variable Reference

Status: `PUBLIC_V3.51_GLOSSARY / SECTIONS_0_TO_8_AND_PUBLIC_APPENDICES /
METHOD_FILES_RETAIN_FORMULA_AUTHORITY`

Date: 2026-11-11

## Review and authority boundary

This cumulative Public glossary contains Sections 0–8 and compact reader
appendices. It gives independent human and machine readers the vocabulary
needed to study, reproduce, critique and compare the public v3.51 Method.
Versioned method files remain authoritative for formulas and local contracts;
this glossary provides navigation, semantic distinctions and return paths.

The reader route is:

0. how to read the glossary;
1. general reading vocabulary;
2. Project, Method and architecture spaces;
3. shared identity, index and status vocabulary.
4. KSODI-Light, the formal Layer-1 boundary and K/S/O/D/I.
5. Layer-2 complete typed Z, its projections, dynamics and windows.
6. Layer-3 monadic IK and the IK-Gesamtbild.
7. Layer-4 R0 relational eligibility.
8. Layer-5 dyadic IK_rel.

The glossary is not a method amendment, physical runtime schema,
implementation-conformance result, empirical validation or action authority.
Its publication on moving Public `main` does not by itself authorize a tag,
GitHub Release or DOI.

---

<a id="glossary-reading-authority"></a>

## 0. How to read this glossary

### 0.1 Purpose

This glossary is a terrain map for KSODI vocabulary. It helps a human or
machine reader determine:

- which object a term names;
- in which Layer and scope it applies;
- which version and maturity it has;
- whether it is a value, status, profile, policy, identity, view or research
  candidate;
- what it must not be confused with;
- where the authoritative definition and the reconstruction route live.

The glossary explains and connects terms. Exact formulas and method contracts
remain authoritative in the linked versioned method sources. A glossary entry
cannot by itself validate a method, prescribe a physical database field,
authorize an implementation or promote a candidate into Method authority.

### 0.2 Authority and version rule

Interpret every term together with its declared scope and maturity:

| Maturity label | Reader meaning |
| --- | --- |
| released v3.50/v3.5.0 | part of the fixed released compatibility basis named by the source |
| public v3.51 method/result term | present in an approved public v3.51 method, result contract or orientation source |
| logical technical identifier | stable machine-oriented name for a method object or view; not automatically a database/API field |
| view or presentation term | arranges retained results for a consumer; does not create a new calculation |
| staged/Future Research | preserved question or candidate outside current method closure |
| legacy/retired | retained for reconstruction; not a default for new results |
| unresolved | classification or wording still requires review |

Repository presence, repetition, implementation behavior and a passing test do
not promote a term into the KSODI Method. Public method authority,
implementation evidence and research status remain distinguishable.

Primary orientation sources:

- [Conceptual Note v3.51](./Conceptual-Note_V351.md);
- [Architecture v3.51](./KSODI-Architecture_V351.md);
- [Implementation Guardrails v3.51](./IMPLEMENTATION_GUARDRAILS_V351.md);
- the exact linked Layer method file for formulas and local contracts.

### 0.3 Entry anatomy

A complete reader entry follows this route:

```text
human label and symbol
  -> everyday orientation
  -> precise KSODI meaning
  -> object type, Layer, scope and maturity
  -> minimum method placement
  -> important non-equivalences
  -> example
  -> authoritative source
  -> reconstruction and related-term links
```

The compact first surface may omit derivation detail, but it may not erase
identity, status, version, authority or the route back to the richer object.

### 0.4 Two reading routes

The canonical narrative is frame-first:

```text
KSODI Project and Method
  -> architecture space and Layer
  -> object family
  -> local term
  -> authoritative source
```

A searched term may also be entered detail-first:

```text
term or symbol
  -> local explanation
  -> parent object and Layer
  -> wider frame
  -> authoritative source and reconstruction route
```

The detail route is navigation, not a second authority order. A local formula
must not silently replace its wider question, evidence basis or claim boundary.

### 0.5 Human label, symbol and technical identifier

Keep these interfaces distinguishable:

```text
human-facing label
<-> mathematical symbol or notation
<-> logical technical identifier
<-> optional reviewed physical implementation field
```

They may refer to the same object, but they are not interchangeable strings.
For example, `IK-Gesamtbild` and `ik_joint_evaluation_view` map one human view
to one logical identifier; neither is an extra scalar. A logical identifier
does not prescribe a table, column or API shape.

### 0.6 Values, statuses and blank-looking displays

A number exists only for a numeric result. A dash, blank field or zero may not
stand in silently for a nonnumeric result. Every nonnumeric or gated display
must reveal or link to:

- the status family;
- the exact status/state and reason;
- the object whose status is shown;
- the controlling profile/gate/window;
- retained upstream evidence and results.

The common method-result statuses are `numeric`, `not_selected`,
`not_observable` and `not_applicable`. Processing failure, incomparability,
incomplete assembly and gate states belong to other typed families described
in Section 3.

### 0.7 `Σ` and aggregation

Reader wording uses **aggregation** or **aggregated view**. `Σ` is used only
for an actual aggregation; `Sigma` remains a searchable source/technical
alias. Always qualify the object level, for example `Z_Σ`, `IK_Σ`, `R0_Σ` or
`IK_rel_Σ`. An unqualified “Sigma result” is too ambiguous.

Aggregation never erases exact members, exclusions, counts, coverage,
statuses, processing order, profile or provenance.

### 0.8 Reconstruction rule

Every derived result points to:

- its exact input object type and identities;
- profile/formula/version;
- status and comparability contract;
- authoritative source;
- the next richer object needed for reconstruction.

A presentation additionally states what it retains and omits. Reconstruction
is a traceable attempt under retained evidence and known loss—not a guaranteed
inverse and not permission to invent missing provenance.

---

<a id="glossary-general-vocabulary"></a>

## 1. General reading vocabulary

These words explain the language used by later entries. They are not new
operators or formulas.

### 1.1 Output and state vocabulary

| Term | In everyday terms | In KSODI precisely | Not the same as |
| --- | --- | --- | --- |
| **Result** | what a declared examination produced | typed output bound to operands, method, profile, version, identity, status and provenance | number alone, display, interpretation or evidence |
| **Value** | numerical content when a number exists | unrounded computational value under one numeric policy, present only for a numeric result | status, rounded display, truth or quality |
| **Status / state** | what kind of result exists / where a particular object or decision stands | object-specific typed vocabularies; method-result status remains separate from processing, assembly, gate, window and workflow states | one universal enum or implicit number |

Example: R0 can simultaneously have `result_status=numeric` and
`gate_state=closed`. The closed state does not erase the numeric result.

### 1.2 Identity, grounding and traceability

| Term | In everyday terms | In KSODI precisely | Not the same as |
| --- | --- | --- | --- |
| **Identity** | what is needed to know exactly which object is meant | stable or explicitly provisional IDs plus indices, membership, profiles, versions and operand relations | hidden essence, display name or timestamp |
| **Reference** | the named object, baseline or frame used for grounding/comparison | typed and versioned reference role such as source instance, baseline, geometry, predecessor or target corridor | evidence, universal truth or unqualified `Ref` |
| **Evidence** | attributable material supporting or constraining an observation | retained source material or governed reference plus basis and selection/extraction path | result, proof, fluent explanation or provenance alone |
| **Provenance** | where an object came from and what happened to it | source, processing, transformation, profile, version, evaluator and predecessor links | evidence content, authority or correctness guarantee |
| **Scope / Geltungsbereich** | the declared boundary of a question and answer | versioned context, domain, granularity, member/source set and exclusions | complete reality or permission to generalize |
| **Basis** | material or frame on which a calculation rests | exact evidence, reference, representation, coordinate semantics or comparison foundation required by a profile | profile, result or source identity alone |

### 1.3 Profiles, policies and retention

| Term | In everyday terms | In KSODI precisely | Not the same as |
| --- | --- | --- | --- |
| **Profile** | named and versioned recipe for one question | governed configuration binding components, weights, references, norms, thresholds, eligibility and/or aggregation | evidence, participant trait, result or universal default |
| **Policy** | declared rule for a decision or boundary | versioned rule for tolerance, status precedence, threshold, display, retention, access or aggregation | formula, empirical fact or legal authority by itself |
| **Retention / Aufbewahrung** | what is kept, for how long and under which conditions | object- and environment-specific policy for evidence, records, results, profiles, provenance, processing outcomes and expiry/deletion | operator function, universal keep-all permission or promise to reconstruct deleted evidence |

Laboratory retention may deliberately preserve rich synthetic evidence and
calculation paths. Operational retention remains bound to purpose, authority,
access, security, privacy and applicable law.

### 1.4 Selection, membership and eligibility

| Term | In everyday terms | In KSODI precisely | Not the same as |
| --- | --- | --- | --- |
| **Mask** | structured indication of selected or available parts | explicitly typed map, for example profile-selected components or derived numeric availability | every fixed subset, status vector or imputation rule |
| **Fixed set / subset** | collection chosen beforehand and kept stable | named nonempty set such as coordinate set `M` or relational component set `N`, bound to one profile/version | event-wise numeric intersection or silent renormalization |
| **Membership / pairing map** | record of which objects/events belong together for one analysis | direction- and version-aware mapping to exact members and source-local positions | adjacency, similarity or proof of relationship |
| **Gate** | check whether a later question may be evaluated | typed eligibility decision over exact operands and profile; result, result status and gate state remain separate | proof of relation, truth, approval or action authority |
| **Eligibility** | whether prerequisites for a next step are met | question-bound classification preserving reasons and excluded objects | applicability, observability, validity or goodness |
| **Applicability** | whether the selected question validly applies | typed method decision under its declared evidence/basis conditions | selection, observability or general relevance |

<a id="glossary-window-aggregation"></a>

### 1.5 Windows and aggregation

| Term | In everyday terms | In KSODI precisely | Not the same as |
| --- | --- | --- | --- |
| **Window** | deliberately bounded collection considered together | identified object with bounds, order, overlap, opportunities, members/exclusions and aggregation profile | one event, participant state or automatically numeric aggregate |
| **Opportunity** | occasion on which a question could be attempted | identified candidate retained through gate, observability, applicability, processing and numeric partitions | eligible numeric result or proof of relation |
| **Coverage** | how much of a declared opportunity set produced the named usable result | typed numerator, denominator and profile; each question defines its own rate | quality, gate-open rate or completeness of reality |
| **Aggregation / `Σ`** | declared summary of several retained members | typed derived object with member basis, aggregator, processing order, counts, coverage, partitions and provenance | event state, truth about the whole window or silent averaging |

### 1.6 Transformations, comparison and reconstruction

| Term | In everyday terms | In KSODI precisely | Not the same as |
| --- | --- | --- | --- |
| **Projection** | simplified view of a richer object along a declared direction/question | formula/profile-bound transformation retaining input link and known loss | full state or replacement truth |
| **View / presentation** | arrangement for a machine, assistive system or human | consumer-specific projection with retained/omitted fields, display policy and reverse link | additional calculation, method authority or later operand |
| **Complete / reduced / partial** | every required part / fixed declared subset / retained incompleteness | object-specific identities with separate eligibility, profiles and comparison rules | complete truth or silent equivalence among subsets |
| **Comparison** | calculation or description of a difference | declared operation over identified operands | proof that the operands were comparable |
| **Comparability** | check whether a requested comparison is legitimate | identity/profile/basis/predecessor contract; failure is a separate classification | numerical equality, proximity or applicability |
| **Reconstruction** | traceable attempt to recover how something arose | procedure preserving candidates, uncertainty, dependencies, transformations and known loss | guaranteed inverse or recovered hidden state |
| **Uncertainty** | what remains unresolved or only partly supported | attributable limitation tied to source, observation, representation, reconstruction, profile or inference | processing failure, non-applicability or reason to erase a bounded result |

These reader definitions are bounded by the versioned method files and the
cross-layer Architecture, Conceptual Note, Hangar and Guardrails.

---

<a id="glossary-project-method-architecture"></a>

## 2. Project, Method and architecture spaces

<a id="ksodi"></a>

### 2.1 `KSODI`

**In everyday terms:** KSODI is the proper name of the overall undertaking.

**In KSODI precisely:** unqualified informal use is acceptable only where the
scope is obvious. Consequential statements distinguish Project, Method,
research, implementation/instrument and publication status.

**Not the same as:** one expansion of the letters, the five-operator baseline,
one score, one implementation or one released method version.

Sources: [Conceptual Note v3.51](./Conceptual-Note_V351.md) and
[KSODI Framework and Protocol naming transition](./KSODI-Framework-and-Protocol-Naming-Transition_V351.md).

### 2.2 K/S/O/D/I baseline

The concrete baseline comprises five connected but non-interchangeable
observation-question families:

| Symbol | German reader orientation | Formal current family name |
| --- | --- | --- |
| `K` | beobachtbare Kontextvollständigkeit | Observable Context Completeness |
| `S` | beobachtbare strukturelle Kohärenz | Observable Structural Coherence |
| `O` | beobachtbare, referenzgebundene Objektivierbarkeit/Grundierung | Observable Grounded Objectivity |
| `D` | beobachtbare Deutlichkeit/Klarheit | Observable Clarity |
| `I` | beobachtbarer Informationsimpuls/-beitrag | Observable Information Impulse |

The formal Observer coordinate order is `(K,S,O,D,I)`. This order does not
make the operators one serial causal pipeline or a complete theory of
communication, cognition, relation, truth or control.

Source: current Layer-1 files under
[KSODI Operators v3.50](./KSODI-Standard-Eval/Layer-1_KSODI-Operators_V350/).

<a id="ksodi-method"></a>
<a id="ksodi-project"></a>
<a id="ksodi-research"></a>
<a id="ksodi-implementation-instrument"></a>

### 2.3 KSODI Method, Project, research and implementation

| Term | Reader meaning | Essential boundary |
| --- | --- | --- |
| **KSODI Method** | explicitly versioned methodological contract of operators, objects, profiles, statuses, layers, gates, formulas and non-claims | Project inclusion or implementation behavior does not create Method authority |
| **KSODI Project** | wider research, development, validation, implementation, governance and publication programme | contains several distinguishable activities and maturity levels |
| **KSODI research** | declared investigation inside the Project | a hypothesis or Future Work route is not automatically Method |
| **KSODI implementation / instrument** | technical realization or observation instrument | produces implementation evidence, not automatic method authority |

Forbidden silent promotion:

```text
within the KSODI Project
  != part of the KSODI Method
  != formalized
  != validated
  != implemented
  != released
  != action-authorized
```

Sources: [Conceptual Note v3.51](./Conceptual-Note_V351.md) and
[KSODI Framework and Protocol naming transition](./KSODI-Framework-and-Protocol-Naming-Transition_V351.md).

<a id="ksodi-public-private-collaboration"></a>

### 2.4 Repository and authority scopes

| Scope | Role | Boundary |
| --- | --- | --- |
| **Private** | internal workbench, research space and candidate/governance record | not public or citeable merely because material exists there |
| **Public** | self-contained public method/documentation and citation surface | a tagged snapshot governs the cited released version |
| **Collaboration** | selective implementation-facing handoff and decision surface | not a mirror of Private, runtime or third method canon |
| **implementation repository** | technical realization and conformance evidence | architecture/code authority remains distinct from method/publication authority |

Moving material between these scopes is a reviewed transfer, not automatic
synchronization.

### 2.5 KSODI-Light, Standard-Eval and Full

| Space | Reader orientation | Current boundary |
| --- | --- | --- |
| **KSODI-Light** | accessible reflection on observable communication/interaction conditions and bridge into the formal Method | human-facing task orientation; not the complete Method or a person score |
| **KSODI-Standard-Eval** | formal monadic observation through K/S/O/D/I, typed Z and monadic IK | does not by itself establish a relation between trajectories |
| **KSODI-Full** | relational extension beginning with declared pairing and R0 eligibility, then current dyadic IK_rel where eligible | does not make every later R-family idea active v3.51 Method |

The optional Light `0..5` estimate is nested later under Section 4 and remains separate
from formal Observer coordinates on `[0,1]`.

### 2.6 Observer and Controller

**Observer** names the role that declares observation objects, questions,
profiles and evidence, then produces attributable results under the selected
method. Observation does not create intervention authority.

**Controller** names a staged later role for authorized use of observations in
decision or intervention contexts. It remains separate from Observer and is
not an active v3.51 calculation layer.

```text
Observer result != Controller decision != permission to act
```

Sources: [Architecture v3.51](./KSODI-Architecture_V351.md) and the
[cumulative Observer/controlled-action boundary v3.51](./KSODI-Full/KSODI_Observability-and-Controlled-Action-Boundary_V351.md).

### 2.7 Hangar, Interaction Space and Interaction Navigator

**Observable interaction event** names an attributable signal, event or
retained state change entering a declared relational observation space. It is
not automatically reconstructible communication, understanding, agreement,
resonance or causal influence.

**Reconstructible communication** requires signals that can be treated as
contributions under an explainable code, context or reconstruction relation.
Correct or shared understanding remains a separate question.

Four spaces remain distinguishable:

| Space | Reader meaning | Essential boundary |
| --- | --- | --- |
| participant processing/library/archive space | entity-specific processing or retained material | not automatically visible to the external Observer |
| transient interaction/work space | bounded availability of externalized contributions, signals and tool outputs | does not merge sources, archives, understanding or responsibility |
| Observer-side Hangar | qualified retention, comparison and reconstruction view over typed observation objects | not the interaction itself and not a participant's inner state |
| Controller/action space | separately authorized decision or intervention space | no score, display or Observer result authorizes it by itself |

A **qualified Hangar** declares Hangar kind, owner/operator, Observer vantage,
participants and object kinds, time/window, location, access/visibility,
retention, profiles/transformations and action authority. It additionally
retains the identities, members, statuses and provenance required by its
question. An unqualified collection of points is not automatically a Hangar.

**Interaction navigator** is the human-facing method image for using retained
KSODI views to inspect positions, directions, deviations, boundaries and
return paths. It is not a target score, cruise control, truth claim or
Controller command.

Source: [Hangar v3.51](./KSODI-Hangar_V351.md).

### 2.8 Layer

A **Layer** is an architectural position with its own object family, inputs,
outputs and authority boundary—not merely a folder number.

| Layer | Current orientation |
| --- | --- |
| 0 | KSODI-Light human-facing reflection/orientation |
| 1 | formal K/S/O/D/I operator results |
| 2 | typed Z assembly and conditional numeric projection |
| 3 | monadic IK result/view family |
| 4 | R0 relational eligibility gate |
| 5 | current dyadic IK_rel coherence-compatibility projection |
| 6+ | staged/Future Research such as later R-family branches unless separately released |

The Layer number does not establish empirical validity, greater importance or
automatic permission to proceed.

### 2.9 Relational namespace: `R`, `R0`, `Ref` and `R_full`

- **`R`** is a relational namespace/family marker. It is not one result.
- **`R0` / `R_0`** is the Layer-4 gate asking whether declared trajectories
  meet one named availability/comparability/bounded-drift contract for a
  downstream branch. An open gate is eligibility, not relation or resonance.
- **`Ref`** is unsafe without qualification. O reference instance, I baseline,
  fixed IK geometry and other references are different objects.
- **`R_full`** is retained as a staged descriptive/Future label, not a current
  canonical v3.51 result.

Detailed R0 and IK_rel entries follow in Sections 7 and 8. High-risk aliases
and collisions are summarized in Appendix F.

<a id="ksodi-framework-protocol"></a>

### 2.10 KSODI Framework, Architecture, working mode and Protocol

| Term | Reader meaning | Essential boundary |
| --- | --- | --- |
| **KSODI Framework** | connective orientation across Project, versioned Method, roles, spaces, evidence handoffs, working practices, implementations and separately governed action surfaces | adds no operator, formula, score, Method layer or action authority |
| **KSODI Architecture** | topology showing where current Method objects, layers and staged branches are arranged | does not by itself govern every project role, workflow or handoff |
| **working discipline** | question-appropriate Micro/Macro reconstruction, visible uncertainty, repair and retained provenance | is neither a sixth operator nor one compulsory protocol episode |
| **KSODI Protocol** | optional candidate practice for orienting, retaining offers/signals, declaring inquiry, inspecting observable response, repairing and forming a bounded handoff | is not part of the versioned Method, a rigid turn sequence, validated effect or Controller permission |

These terms may support one another but must not be collapsed:

```text
Project != Method != Framework != Architecture
working mode != Protocol != formal evaluation != authorized action
```

Earlier work used `IDAS` for a broader framework candidate and `SIRA` for an
interaction-practice candidate. Those names remain provenance locators rather
than additional active public product names. **KSODI Framework** and **KSODI
Protocol** keep the established KSODI name central and avoid implying hidden
intention, steering authority or resonance claims the current Method does not
make.

Source: [KSODI Framework and Protocol naming transition v3.51](./KSODI-Framework-and-Protocol-Naming-Transition_V351.md).

<a id="ksodi-zoom"></a>

### 2.11 KSODI-Zoom

**In everyday terms:** a disciplined movement between a broad overview and
the local evidence needed to support or revise it.

**In KSODI precisely:** a reconstructible navigation rule that preserves
identity, profile, transformation, uncertainty and known loss across
Macro-to-Micro and Micro-to-Macro movement. It is not merely visual
magnification and does not promise exact recovery of unavailable evidence.

Sources: [Architecture v3.51](./KSODI-Architecture_V351.md) and
[Conceptual Note v3.51](./Conceptual-Note_V351.md).

### 2.12 Directed formation and reconstruction readings

The fixed coordinate family can be considered through different directional
process readings:

```text
formation-oriented:       K -> S -> O -> D -> I
reconstruction-oriented:  I -> D -> O -> S -> K
```

The reconstruction-oriented reading moves from an observable information
impulse through distinguishability, grounding/reference and structure toward
context. It is not the numeric calculation order of Z, a rigid serial
algorithm, proof of causality or guarantee of successful reconstruction.
Parallel checks, shortcuts and recurrence remain possible when declared
evidence and profiles support them.

Sources: [Architecture — directed process topologies](./KSODI-Architecture_V351.md#3-coordinate-order-and-directed-process-topologies)
and [Conceptual Note v3.51](./Conceptual-Note_V351.md).

---

<a id="glossary-identity-index-status"></a>

## 3. Shared identity, index and result vocabulary

### 3.1 Identity spine

Values are interpreted only after the object is identified. The minimum spine
is question-dependent but can include:

```text
source
  -> observed unit and granularity
  -> event
  -> trajectory and source-local position
  -> evaluation/pairing/window identity
  -> profile and version
  -> typed result and provenance
```

Identity does not claim a hidden essence. It prevents different records from
being merged merely because their values, timestamps or labels resemble one
another.

### 3.2 Source, emitter and observed unit

| Term | Meaning | Essential warning |
| --- | --- | --- |
| `source_entity_id` | identity to which the observation/evidence trajectory is attributed | attribution may be provisional; source is not automatically emitter or observed unit |
| `source_attribution_status` / `source_attribution_basis` | how securely and on what basis the source is attributed | stable/provisional/unknown are reader orientations, not an exhaustive universal schema enum |
| `emitting_entity_id` | conditional identity of the entity/device/process that emitted the carrier/event | not automatically author, source, controller or intentional agent |
| `observed_unit_id` / `observed_unit_type` | exact object or part being evaluated | must state whether the unit is message, turn, segment, signal, packet, organism, system part, etc. |
| `observation_granularity_id` | declared level at which the unit is observed | changes object identity and comparability; not merely display zoom |
| parent/membership/composition map | explicit part/whole and membership relation | does not rewrite member identity as parent identity or aggregation |

Source-artifact, parser-run and source-span IDs remain later provenance/
technical appendix vocabulary. They are required where the instrument needs
them, but they do not replace the reader-level source and observed-unit spine.

### 3.3 Event and trajectory

**`event_id`** is the stable identity of one observation event. A
`target_event_id` identifies that event's role in a particular evaluation; it
does not create a second event.

**`trajectory_id`** identifies one ordered source-attributed sequence whose
predecessor policy supports movement and change calculations. Two events with
similar content or timestamps are not thereby members of the same trajectory.

Corrections, retries and alternate evaluations retain lineage instead of
silently overwriting the original event/result identity.

### 3.4 Index spaces

| Symbol | Index space | Reader rule |
| --- | --- | --- |
| `n` | canonical/global event order where defined | does not replace source-local or relational ordering |
| `k_E` | source-local position in trajectory `E` | equal integers in different trajectories do not identify equal events |
| `j` | relational opportunity/evaluation order | binds a declared pairing, not either monadic position |
| `t` | time/sample/legacy step only where explicitly mapped | never interpret globally without unit, clock and mapping |

Physical time, observed time, event order and implementation processing order
must not be silently collapsed.

### 3.5 Pairing map `pi(j)`

**In everyday terms:** the explicit declaration of which two events are being
considered together.

**In KSODI precisely:** a direction- and version-aware map such as
`pi(j)=(k_A(j),k_B(j))`, retaining the ordered dyad, both event/source/
trajectory identities, predecessor chains and relational scope.

**Not the same as:** chronological adjacency, similar values, one shared chat,
reciprocity or proof that a relation exists.

Lower-level relation-ledger fields remain implementation-facing until their
reader need and authority are separately reviewed.

### 3.6 Profile identity

`profile_id` and `profile_version` identify the governed recipe used for one
result. They are part of result meaning and comparability, but are not the
method version, evidence, observed-unit identity or result value.

Changing a profile, axis, norm, component set, threshold or epsilon policy can
change the question. Such a change must not be reported as observed movement
of an unchanged object.

### 3.7 Common method-result statuses

These four statuses describe valid method-result kinds:

| Status | Meaning | Numeric value? |
| --- | --- | --- |
| `numeric` | selected method produced a valid number under its contract | yes |
| `not_selected` | method/profile/component was deliberately not selected | no |
| `not_observable` | required evidence was not observable from the declared vantage/instrument | no |
| `not_applicable` | selected question did not validly apply or pass its method eligibility | no |

Nonnumeric statuses retain reasons and evidence routes. They are not zero,
missing database fields or processing failure.

### 3.8 Other typed state families

| Family | Typical vocabulary | Question answered |
| --- | --- | --- |
| processing outcome | processing/configuration/identity/arithmetic failure | could a valid method result be produced correctly? |
| comparison classification | `comparable`, `incomparable` | may these exact operands be compared? |
| assembly state | complete / `not_complete` / assembly error | was the richer object assembled and is its numeric projection complete? |
| gate state | `open`, `closed`, `not_evaluable` | did one valid gate result admit the named branch? |
| component status | per-component result state, for example in `T_G` | which fixed-profile components are numeric/available? |
| window/aggregate state | empty, eligible, insufficient coverage, emitted | can an aggregate be emitted for this opportunity set? |
| migration class | conformant/reconstructible/partial/noncomparable | how does legacy material relate to v3.51? |
| reconstruction workflow | pending/in progress/reconstructed/failed | what reconstruction work was attempted/completed? |
| evidence/attribution state | stable/provisional/unknown plus basis | how securely is evidence/source identity established? |

`incomparable` remains a comparison classification unless a reviewed method
defines a separately typed outward result envelope. `not_complete` is a Z
assembly state. `not_evaluable` is a gate state. None is a fifth common
method-result status.

### 3.9 Gate-state example

R0 illustrates why status families must remain separate:

```text
R0 result_status = numeric
R0 value         = 0.62
threshold        = 0.80
gate_state       = closed

downstream primary IK_rel status = not_applicable
reason                            = exact R0 gate closed
```

The R0 value remains valid. The downstream question is ineligible. Reporting
only “not applicable” would lose the numeric upstream finding and the exact
reason.

### 3.10 Tagged observation object `x=(iota,z)`

The tagged form keeps a coordinate representation `z` attached to identity
tag `iota`. The tag may retain object type, source, event, trajectory, indices,
granularity, evaluation, basis, profile and version.

Equal `z` does not imply equal observation objects. Projection
`p(iota,z)=z` may intentionally lose identity detail, so every use must retain
a reverse route to the tagged source object. The tag does not invent an
identity-distance metric or hidden ontology.

Sources: [Architecture v3.51](./KSODI-Architecture_V351.md) and
[Implementation Guardrails v3.51](./IMPLEMENTATION_GUARDRAILS_V351.md#21-tagged-observation-object-and-reconstruction-boundary).

### 3.11 Section-3 reconstruction guard

Before interpreting any number or status, a reader should be able to answer:

1. Which source and observed unit?
2. Which event, trajectory and position?
3. Which granularity and scope?
4. Which profile/version and evidence basis?
5. Which status family—not merely which label?
6. Which pairing/window membership where relational or aggregated?
7. Which richer object and evidence can be reached from this result?

If those questions cannot be answered, the limitation is declared. Missing
identity or provenance is not reconstructed as fact merely to make a record
look complete.

---

<a id="glossary-layer0-layer1-operators"></a>

## 4. KSODI-Light and the formal K/S/O/D/I operator families

### 4.1 Light is an entry surface, not a second formal evaluator

KSODI-Light is a dual human entry:

1. it provides accessible questions for reflecting on observable conditions
   of communication or interaction; and
2. it provides an orientation bridge into the more exact, versioned KSODI
   Method.

Its five labels map to the broad K/S/O/D/I question families, but a Light
reading is not a formal Layer-1 result. Light does not require a machine
instrument, and it must not be used as a person ranking, universal quality
score or substitute for a declared Observer evaluation.

Optional Light completeness estimates are task-relative human orientations on
`0..5`:

```text
Light K/S/O/D/I on 0..5
  != formal Layer-1 K/S/O/D/I on [0,1]
  != a rescaling contract between those two spaces
```

Polarity, task, participant/viewpoint and interpretation must be stated. An
estimate may suggest a question or clarification; it does not authorize an
intervention or become a formal operand for Z, IK, R0 or IK_rel. Natural-
language feedback remains the default; values are shown only when requested,
labelled approximate and kept separate by dimension rather than collapsed into
one preferred total.

Whether one inquiry needs all five dimensions, a declared subset or
non-uniform relevance/weight remains an open context- and purpose-dependent
question. Light may foreground task-relevant dimensions without judging a
person. Formal Standard-Eval may use only explicitly named and validated
profiles; non-use, disagreement or missing evidence never silently removes an
operator or authorizes dynamic renormalization.

Source: [KSODI-Light README](./KSODI-Light/README.md#operator-labels-in-light-and-eval).

### 4.2 Shared formal Layer-1 contract

Formal K, S, O, D and I are five related but semantically non-interchangeable
monadic observation-question families. Each result belongs to one declared
source-attributed target event on one trajectory and retains at least:

- target, source, event and trajectory identity;
- observation scope and granularity;
- evidence/basis and evaluator vantage;
- named versioned profile and instrument where applicable;
- result status and reason;
- provenance and reconstruction route.

One evidence item may inform more than one operator. That does not make the
operator questions equal, and it does not permit silent double counting.

```text
context availability != grounding
grounding != clarity
clarity != structure
information difference != correctness or reconstruction success
```

The formal English names remain searchable method names. The German
orientations are reader aids, not competing definitions.

### 4.3 Formation, reconstruction and coordinate order

The fixed coordinate order is `(K,S,O,D,I)`. Two directed readings may be
useful around it:

```text
formation-oriented:       K -> S -> O -> D -> I
reconstruction-oriented:  I -> D -> O -> S -> K
```

Neither direction is the mandatory numeric calculation order of Z. The second
path is an iterative reconstruction orientation, not a causal proof or
guarantee of successful reconstruction. Parallel checks, shortcuts and
renewed passes may be appropriate when their evidence and assumptions remain
visible.

### 4.4 Domain instantiation and instrument boundary

The K/S/O/D/I families are broader than one language-semantic implementation.
A concrete domain makes one family observable through this retained chain:

```text
operator family
  -> domain instantiation
  -> evidence profile
  -> instrument or query set
  -> attributable evidence
  -> typed result
```

A domain may use text, signal, timing, protocol, biological, technical or
other carrier-specific evidence. It may therefore fill the operator evidence
records very differently. It may not silently redefine the operator question,
claim cross-domain comparability or infer hidden meaning, intention or state.

A language-semantic implementation is one possible bounded instantiation; it
is not the universal semantic definition of the operators. Laboratory
retention and operational/product retention are governed separately;
retention is not an operator function.

Source: [Implementation Guardrails — operator family and instrument](./IMPLEMENTATION_GUARDRAILS_V351.md#11-operator-family-domain-instantiation-and-instrument).

### 4.5 `K` — Observable Context Completeness

**German reader orientation:** beobachtbare Kontextvollständigkeit.

**Question:** To what extent are the nonempty context requirements declared
for one target-event evaluation observably fulfilled inside its admissible
context scope under the named availability relation?

K distinguishes stored, evaluator-visible, target-accessible,
emitter-accessible, receiver-accessible and actually delivered context. Mere
presence does not prove use, attention, understanding, suitability or
grounding.

| K term | Reader meaning and boundary |
| --- | --- |
| `scope_A(k_A)` | admissible context-object scope; not all stored history or everything visible to the evaluator |
| `availability_relation_id` | identifies whose/which observable availability is being tested; presence, delivery and use remain distinct |
| `observer_vantage_id` | visibility boundary of the evaluator/instrument; not target access or complete system state |
| `E_K,A(k_A | p_K)` | nonempty profile-bound set of expected context requirements; an empty set is `not_applicable`, not perfect context |
| `a_i,A(k_A | scope_A(k_A), p_K)` | evidence-linked fulfillment value for one declared requirement; unobservable is not silently `0` |
| `G_K,A(k_A | p_K)` | internal K calculation gate checking whether a valid numeric K path exists; not R0 or action authority |
| `p_K` | complete named K profile binding scope, requirements, relations, weights, evidence and missingness |
| `K0_A(k_A | scope_A(k_A), p_K)` | canonical static K result under the declared basis |
| `K_A(k_A)` | selected K coordinate alias used for typed Z; it does not add another result |
| `G_cmp_K,A(k_A)` | source-local K comparability decision for a requested predecessor comparison |
| `Delta K_A(k_A)` | first source-local change of comparable K results; not A/B difference |
| `Delta2 K_A(k_A)` | change of that K movement; not squared `Delta K` |
| `KΣ_A(W_A)` | typed K window aggregate with exact members, eligible set, counts, statuses, profile and provenance |
| `KΣ_A(Hangar)` | typed K distribution/view; not one participant state or one universal scalar |
| K-specific diagnostic boundary | component evidence and missingness may be retained, but optional diagnostics do not become extra Z coordinates |

Authoritative source: [Operator K v3.51 method](./KSODI-Standard-Eval/Layer-1_KSODI-Operators_V350/KSODI_Operator-K_Observable-Context-Completeness_V351.md).

### 4.6 `S` — Observable Structural Coherence

**German reader orientation:** beobachtbare strukturelle Kohärenz.

**Question:** How coherently are the observable parts of one target event
organized under the declared structural profile and scope?

Formatting density, length, marker count or complexity do not by themselves
establish structural coherence. S evaluates declared segmentation,
requirements, visible boundaries, order relations and—only where selected—an
explicit disruption component.

| S term | Reader meaning and boundary |
| --- | --- |
| `p_S` | complete named structural profile, including component selection, rules, weights and missingness |
| `E_S` | declared expected structural requirements; not the observed target structure itself |
| `StructRef_S` | structural reference/basis for the selected question; not universal ideal form |
| `profile_selection_basis` | records whether the S profile route was predeclared or resolver-derived; not the same question as how units and relations were resolved |
| `structure_resolution_basis` | records whether structural units and relations came from the profile or a declared resolver; it does not by itself select the profile |
| `semantic_measurement_anchor` | binds the intended S question, method/profile version and requirement instance; not an implementation run fingerprint |
| `execution_fingerprint` | identifies result-affecting implementation conditions and actual tool/instrument lineage; not comparability permission by itself |
| `C_req,A(k_A | E_S,p_S)` | requirement-coverage component over declared structural requirements |
| `M_vis,A(k_A | p_S)` | visible marker/boundary component under the profile |
| `N_boundary` | denominator/count basis for the declared boundary question; not raw text length |
| `P_order,A(k_A | StructRef_S,p_S)` | explicit relative-order component; surface order or a bare list does not automatically create a directed edge |
| `P_disrupt,A(k_A | p_S)` | optional declared disruption component; absent selection is not zero disruption |
| `gamma_S` | profile-bound influence/weight of the optional disruption component |
| `C_S,A(k_A)` | declared base-component family for the target event |
| `M_S(p_S)` | profile-fixed mandatory S component set; mandatory components are not removed event by event |
| `A_S,A(k_A)` | event's applicable selected component set after typed applicability checks; it does not authorize changing the profile mask |
| `component_attribution_policy` | declares how overlapping evidence contributes without silent double counting |
| `S_base,A(k_A | p_S)` | base structural combination before any explicitly selected extension |
| `S0_A(k_A | p_S)` | canonical static S result for the selected profile |
| `S_A(k_A)` | selected S coordinate alias for typed Z |
| `G_cmp_S,A(k_A)` | S comparability decision for a source-local dynamic comparison |
| `Delta S_A(k_A)` | first source-local change of comparable S values |
| `Delta2 S_A(k_A)` | change of S movement, not squared delta |
| `S_Σ_A(W_A)` | typed S window aggregate retaining members, component/profile identity and status partitions |
| `S_Σ_A(Hangar)` | typed S distribution/view; not one event or merged trajectory |
| `not_emitted` | evaluation-envelope state for a selected route with no accepted applicable instrument; no Layer-1 operator status or numeric value is emitted |

Minimal and extended S profiles are predeclared alternatives. Required
components may not be removed event by event and remaining weights silently
renormalized.

Authoritative sources: [Operator S v3.51 method](./KSODI-Standard-Eval/Layer-1_KSODI-Operators_V350/KSODI_Operator-S_Observable-Structural-Coherence_V351.md),
[S v3.51 implementation companion](./KSODI-Standard-Eval/Layer-1_KSODI-Operators_V350/KSODI_Operator-S_Implementation-Companion_V351.md).

### 4.7 `O` — Observable Grounded Objectivity

**German reader orientation:** beobachtbare, referenzgebundene
Objektivierbarkeit/Grundierung.

**Question:** Given one target event and an admitted reference basis, to what
extent is the event observably supported by and traceable to that basis under
the selected O profile?

O does not establish universal truth, correctness, causal origin, source
authority or shared understanding. A numeric path is possible only after
source need, availability, evaluator visibility, admissibility and a nonempty
admitted reference basis have been resolved.

| O term | Reader meaning and boundary |
| --- | --- |
| `G_O_sem,A(k_A)` | semantic/source-need decision route for the O question; not the numeric O result |
| `p_G_O` | profile governing that need/admission route; not the numeric O profile `p_O` |
| `reference_space_need` | typed need state such as `not_expected`, `optional` or `required` for this event/question |
| `source_need_policy_selection_basis` | why the versioned need policy applies to this event; source presence alone does not select it |
| `source_need_reason` | why a source/reference is or is not expected; distinct from a failure/missing reason |
| `missing_reason` | why required/selected reference material was not available/admissible/delivered; not the source-need decision itself |
| `reference_space_available` | whether the declared reference space exists/is accessible under the gate contract |
| `reference_space_visible_to_evaluator` | whether the evaluator can inspect the declared reference material |
| `reference_space_admissible_for_evaluation` | whether visible material is methodically admitted for this evaluation |
| `reference_space_nonempty` | whether the admitted reference instance contains at least one usable element; raw nonempty retrieval is not enough |
| `reference_space_profile_id` | identity of the rules for constructing a reference space; not the event-bound instance |
| `reference_instance_id` | identity of the concrete event-bound reference instance supplied to O |
| `candidate_reference_element_ids` | exact elements considered before policy, budget and admission decisions |
| `admitted_reference_element_ids` | exact candidates admitted under the declared policy |
| `delivered_reference_element_ids` | exact admitted elements actually supplied as `Ref_A(k_A)` |
| `budget_status` | optional budget-stage status: `measured`, `deferred`, `skipped` or `cancelled`; deferred is not measured |
| `o_applicability_state` | O-specific applicability/admission state; it maps to but is not identical with the common method-result status |
| `Ref_A(k_A)` | concrete event-bound admitted O reference instance/basis; not raw retrieval, all context, I baseline or truth |
| `p_O` | complete numeric O profile binding claims/units, support rules, weights and missingness |
| `app_O,A(k_A)` | internal O applicability predicate for the selected numeric calculation |
| `C_O,A` | profile-defined O component record/set; its concrete content is not a universal citation or RAG formula |
| `c_O,r,A` | evidence-linked result for one declared O component/question |
| `F_p_O` | profile-bound aggregation/function over the fixed O unit results |
| `O0_A(k_A | Ref_A,p_O)` | canonical static O result under the admitted reference instance and profile |
| `O_A(k_A)` | selected O coordinate alias for typed Z |
| `G_cmp_O` | O comparability decision retaining both concrete reference instances |
| `Delta O_A` | first source-local change of comparable O values |
| `Delta2 O_A` | change of O movement, not squared delta |
| `Rise_O,A(k_A)` | optional direction-specific O movement diagnostic; not the canonical result |
| `RefDrift_O,A(k_A)` | optional diagnostic for movement/change in the reference basis |
| `P_ref,A(W_A)` | retained/reference-window profile needed to interpret reference drift |
| `O_A Sigma(W_A)` | typed O window aggregate over a declared eligible set |
| `O_A Sigma(Hangar)` | typed O distribution/view retaining reference-instance provenance |
| v3.51 reference-basis precision seam | keeps profile, concrete reference instance, candidate pool, admitted set and actually delivered subset distinguishable |

The reference seam is essential for reconstruction: an identical O number
does not prove that the same candidates, admitted references or delivered
subset produced it.

Authoritative sources: [Operator O v3.51 method](./KSODI-Standard-Eval/Layer-1_KSODI-Operators_V350/KSODI_Operator-O_Observable-Grounded-Objectivity_V351.md),
[O v3.51 Source-Need Gate](./KSODI-Standard-Eval/Layer-1_KSODI-Operators_V350/KSODI_Operator-O_Source-Need-Gate_V351.md),
[O v3.51 implementation companion](./KSODI-Standard-Eval/Layer-1_KSODI-Operators_V350/KSODI_Operator-O_Implementation-Companion_V351.md).

### 4.8 `D` — Observable Clarity

**German reader orientation:** beobachtbare Deutlichkeit/Klarheit.

**Question:** Is an already observed target signal distinct, locally supported
and stable enough under its carrier/detector profile to justify continuing a
reconstruction attempt?

D does not first discover I, decode meaning, prove understanding or establish
grounding. It examines a declared signal/carrier representation and keeps
local support separate from excess variation/dispersion.

| D term | Reader meaning and boundary |
| --- | --- |
| `p_D` | complete D profile selecting the allowed D construction and all dependencies |
| `p_L` | local-support profile |
| `p_V` | variation/dispersion profile |
| `q_A(k_A)` | admitted target-signal/carrier representation for D; not decoded meaning |
| `L_A(k_A | p_L)` | local support/redundancy component under `p_L` |
| `N_L` | support-unit denominator/count basis; not arbitrary token length |
| `U_A(k_A | p_V)` | declared set of local units/representations used by the variation question |
| `m` | cardinality/denominator of that declared set |
| `d_p_V(u_i,u_j)` | profile-bound pairwise distance; identical arithmetic in another operator does not imply identical meaning |
| `V_raw_A` | observed raw dispersion before comparison with the expected profile level |
| `tau_expected_p_V` | expected/profile reference dispersion |
| `V_A` | excess local dispersion after the declared comparison; this is not I's `V_A(k_A)` candidate baseline material |
| `p_D_LV` | predeclared D profile using both local-support and variation components |
| `p_D_L_only` | separately named local-support-only profile; it is not an event-wise fallback when V fails |
| `w_L`, `w_V` | profile-bound component weights; no silent target-dependent learning or renormalization |
| `D0_A(k_A | p_D)` | canonical static D result under the selected profile |
| `D_A(k_A | p_D)` | selected D coordinate alias for typed Z |
| `G_cmp_D` | D comparability decision for source-local dynamics |
| `Delta D_A` | first source-local change of comparable D results |
| `Delta2 D_A` | change of D movement, not squared delta |
| `B_D_A(k_A)` | optional positive D-movement diagnostic `max(0, Delta D_A)` where the signed delta is applicable; not reward, causality or a replacement for signed movement |
| `DΣ_A(W_A)` | typed D window aggregate retaining profile and component/status partitions |
| `DΣ_A(Hangar | event_level)` | typed event-level D distribution/view |
| `P_D_A(W_A)` | inactive Future-Work interface, not an active canonical v3.51 calculation |

If V is `not_applicable` or unavailable under an L/V profile, it does not
become zero and does not authorize undeclared fallback to L-only.

Authoritative source: [Operator D method](./KSODI-Standard-Eval/Layer-1_KSODI-Operators_V350/KSODI_Operator-D_Observable-Clarity_V351.md).

### 4.9 `I` — Observable Information Impulse

**German reader orientation:** beobachtbarer Informationsimpuls/-beitrag.

**Question:** Does one source-attributed contribution create an observable
information difference relative to the baseline declared for that evaluation?

I does not measure truth, value, intelligence, understanding, usefulness or
novelty in every sense. Low I can accompany confirmation, repair, repetition
or stabilization; high I can still be incorrect, unsafe or irrelevant.

| I term | Reader meaning and boundary |
| --- | --- |
| `p_I` | complete named I profile binding baseline, units/equivalence, representation, retrieval, normalization, weights and missingness |
| `V_A(k_A)` | visible candidate baseline material for I; not D's excess dispersion `V_A` |
| `Ref_A(k_A | p_I)` | selected admissible event-bound I baseline; not automatically O's reference instance |
| `ret_status,A(k_A)` | typed retrieval outcome where retrieval is constitutive; distinguishes not requested, unavailable, empty, inadmissible and available |
| `retrieval_basis_ok,A(k_A)` | retrieval-basis applicability predicate for the selected profile; not universal I architecture |
| `emb` | versioned target/baseline representation function for a vector-compatible profile |
| `emb_Ref_A` | aggregation/representation of the admitted I baseline |
| `d_cos` | normalized cosine-distance instance where selected; not meaning or a universal I definition |
| `app_ref,A(k_A)` | static reference-relative I applicability predicate |
| `J_ref,A(k_A)` | directional target-to-baseline difference component |
| `G_ref,A(k_A)` | share of declared target information units new relative to, or compressing, the admitted baseline |
| `eta_ref` | profile-bound weight combining `G_ref` and `J_ref` |
| `I_ref,A(k_A)` | canonical static reference-relative I result |
| `I_A(k_A)` | selected I coordinate alias for typed Z; no sixth coordinate is created |
| `G_cmp_I` | I comparability decision retaining target, baseline-construction and both concrete baseline instances |
| `Delta I_A` | first source-local change of comparable static I results; may contain both target and baseline movement |
| `Delta2 I_A` | change of I movement, not squared delta |
| `Prev_A` | exact same-trajectory predecessor for an optional direct sequence comparison |
| `J_seq`, `G_seq`, `eta_seq`, `C_seq,I` | optional predecessor components/weight/result; a separate diagnostic, not static I or `Delta I` |
| `F_A(k_A)` | rich feature record containing canonical coordinates and optional diagnostics; not Z itself |
| `Drift_I,A(k_A)` | optional median-window absolute I drift diagnostic |
| `I_standardized,A(k_A)` | optional standardized I window deviation under a declared scale |
| `A_I`, `sigma_I2`, `epsilon_I`, `I_star` | optional exogenous selection/uncertainty attenuation family; never canonical I and never a zero-fill route |
| `I_A Sigma(W)` | typed I window summary keeping static I, `Delta I` and `Delta2 I` separate |
| `I_A Sigma(Hangar)` | typed I distribution/view, not one scalar or merged trajectory |
| conditional retrieval/representation boundary | permits reproducible profiles without making retrieval, embeddings or one model universal I semantics |

The static baseline comparison, the direct predecessor diagnostic and the
change of already calculated I results are three different derivation
families:

```text
I_ref != C_seq,I != Delta I
```

Authoritative source: [Operator I method](./KSODI-Standard-Eval/Layer-1_KSODI-Operators_V350/KSODI_Operator-I_Observable-Information-Impulse_V351.md).

### 4.10 Cross-operator collision and reconstruction guard

Before a Layer-1 result is assembled into typed Z, retain these distinctions:

| Collision or near-alias | Required reading |
| --- | --- |
| D `V_A` / I `V_A(k_A)` | excess local dispersion / visible candidate baseline material |
| O `Ref_A` / I `Ref_A` | O grounding instance / I information baseline; overlap does not establish identity |
| D or I `d_cos` | same arithmetic may instantiate different profile-bound questions |
| operator-local `G_*` | calculation/applicability/comparability gates are not interchangeable and are not R0 |
| `Delta X` / `Delta2 X` | first change / change of change; `Delta2` is not squared delta |
| event result / `XΣ(W)` / Hangar view | target-event result / aggregate / distribution or observation view |
| optional diagnostic / canonical coordinate | retained extra information / one of exactly five Z coordinates |

For every K/S/O/D/I result, reconstruction should reach the target event,
evidence, scope, profile, component records, common result status and any
operator-local applicability or processing state. A numeric coordinate alone
is insufficient for later Z, IK, relational or governance interpretation.

### 4.11 Section-4 draft decisions and reopening points

This first reader integration makes the following reversible drafting choices:

- the optional Light `0..5` estimate remains nested in the main Light/formal interface
  because its separation from formal `[0,1]` coordinates is stated directly;
- formal English operator names retain method-search authority while German
  phrases provide human orientation;
- `K0`, `S0`, `O0`, `D0` and `I_ref` remain visible as principal static
  result labels; `K_A` through `I_A` are selected coordinate aliases;
- operator-local components, profiles, gates, diagnostics, deltas and window
  views are grouped under their parent operator instead of appearing as
  disconnected top-level concepts;
- released notation collisions such as D/I `V_A` and O/I `Ref_A` are not
  renamed silently; they are exposed and scope-qualified;
- inactive `P_D` and conditional retrieval/vector I constructs remain visible
  with their maturity and profile boundaries.

Human review may still revise which controlled reason values, default weights,
diagnostics and implementation-profile details belong in the main reader,
technical appendix or Public selection. Such movement must preserve the term,
its status, authoritative source and recovery route. It may not make an open
profile question look like settled universal Method content.

---

<a id="glossary-layer2-z"></a>

## 5. Layer 2 — complete typed Z and the transition to IK

### 5.1 Z assembles Layer-1 results; it does not recalculate them

Layer 2 receives exactly one final K, S, O, D and I result record for one
source-attributed target event. It aligns and preserves those five records in
canonical coordinate order:

```text
(K, S, O, D, I)
```

Z does not decide the Layer-1 evidence questions again. It must retain their
statuses, profiles, bases, components, gates and provenance. The primary
loss-protected object is the complete **typed assembly record** `R_Z`; the
five-number vector `Z_A(k_A)` exists only when a stricter complete-numeric
condition is satisfied.

```text
valid typed assembly R_Z
  does not imply
complete numeric Z_A(k_A)
```

Coordinate order is not sender/receiver process order, causal sequence or a
claim that the five observations exhaust communication.

Source: [Layer-2 Z method](./KSODI-Standard-Eval/Layer-2_KSODI-State-Vector-Z_V350/KSODI_State-Vector-Z_V351.md).

### 5.2 Coordinate-result inputs and identity alignment

| Z input or gate | Reader meaning and boundary |
| --- | --- |
| `r_X,A(k_A)` | final typed Layer-1 result record for `X in {K,S,O,D,I}`; contains more than a scalar and remains attributable to its operator/profile/evidence |
| `G_Z,identity,A(k_A)` | assembly gate confirming exactly one final record per canonical coordinate and the same target, source, trajectory and local position |

An identity-gate failure is an assembly/configuration error. It is not a
Layer-1 `not_applicable` result, a zero coordinate or permission to align
records by timestamp or content similarity.

If this gate fails, no valid `R_Z` is constructed. The later distinction
between a valid typed record and an incomplete numeric projection applies only
after successful identity alignment.

The coordinate records retain their operator-local `component_mask` where one
exists. That mask is not the same object as Z's numeric-availability mask or a
declared partial-coordinate set.

Sources: [required coordinate records](./KSODI-Standard-Eval/Layer-2_KSODI-State-Vector-Z_V350/KSODI_State-Vector-Z_V351.md#22-required-coordinate-records)
and [assembly gate](./KSODI-Standard-Eval/Layer-2_KSODI-State-Vector-Z_V350/KSODI_State-Vector-Z_V351.md#23-assembly-gate).

### 5.3 Typed coordinate statuses, numeric mask and completeness

| Term | Reader meaning and boundary |
| --- | --- |
| `tau_X,A(k_A)` | common method-result status of coordinate X: `numeric`, `not_selected`, `not_observable` or `not_applicable` |
| `T_Z,A(k_A)` | mandatory ordered five-coordinate status vector; retains the result kind of every aligned coordinate |
| `A_X,A(k_A)` | derived bit saying only whether coordinate X is numeric |
| `A_Z,A(k_A)` | derived ordered five-bit numeric-availability mask |
| `G_Z,complete,A(k_A)` | gate permitting canonical numeric Z only when identity aligns and every coordinate is numeric |
| `complete_Z_state` | typed assembly state such as complete or `not_complete`; not a fifth common Layer-1 result status |

`A_Z` is derived deterministically from `T_Z`, but it cannot replace it. A
zero bit does not reveal whether the coordinate was not selected, not
observable or not applicable. Processing failure remains outside both valid
result vocabularies.

```text
not_complete
  != invalid typed Z record
  != zero vector
  != assembly error
  != low-quality communication
```

Source: [typed Z record and complete-vector boundary](./KSODI-Standard-Eval/Layer-2_KSODI-State-Vector-Z_V350/KSODI_State-Vector-Z_V351.md#3-typed-z-record-complete-vector-and-partial-projections).

### 5.4 `R_Z,A(k_A)` — primary complete typed Z record

`R_Z,A(k_A)` is the complete typed Layer-2 assembly record. It preserves:

- shared target/source/event/trajectory identity;
- references to the five exact Layer-1 result records;
- `T_Z` and detailed result reasons;
- `A_Z`;
- identity and completeness gates/states;
- the optional complete numeric vector when eligible;
- assembler/profile/version and provenance.

The record is complete as a typed assembly object even when its numeric vector
is incomplete, provided the identity gate has succeeded. It is not a sixth
coordinate, a participant's hidden inner state, a complete truth about
communication or an assembly-error audit record.

Source: [State Vector Z — typed Z record](./KSODI-Standard-Eval/Layer-2_KSODI-State-Vector-Z_V350/KSODI_State-Vector-Z_V351.md#34-typed-z-record).

### 5.5 `Z_A(k_A)` — conditional complete numeric projection

`Z_A(k_A)` is the canonical ordered numeric tuple

```text
Z_A(k_A) = (K_A, S_A, O_A, D_A, I_A) in [0,1]^5
```

It exists only when `G_Z,identity` and `G_Z,complete` succeed. It is a
projection of `R_Z`, not the whole typed object. It remains linked to the five
coordinate profiles, bases, statuses, events and evidence routes.

`Z_A(k_A)` is the standard complete input to canonical monadic IK and to
complete source-local Z dynamics. It is not `Z_AB`, a window aggregate,
partial Z, hidden state, causal chain or relational result.

### 5.6 Declared partial Z projections

| Term | Reader meaning and boundary |
| --- | --- |
| `M` | predeclared nonempty ordered subset of the five canonical coordinates |
| `P_M` | projection operator selecting exactly that fixed subset |
| `Z_A^{[M]}(k_A)` | visibly partial numeric diagnostic, emitted only when every coordinate in `M` is numeric |
| Z assembly/projection profiles | named/versioned contracts for assembly, fixed partial projection, comparability, norm, window and display choices |

A partial projection is not created by taking the event-wise intersection of
whatever happened to be numeric. It has its own profile identity, fixed mask,
status and provenance. Observed Z uses `allow_imputation=false`; zero or mean
filling is forbidden.

Different partial masks are not naively comparable. A partial Z is not
canonical complete Z and cannot silently enter canonical IK. A reduced IK
question requires its own separately named reduced profile.

Source: [declared partial projection](./KSODI-Standard-Eval/Layer-2_KSODI-State-Vector-Z_V350/KSODI_State-Vector-Z_V351.md#36-declared-partial-projection).

### 5.7 Comparability, numeric movement and categorical status movement

| Term | Reader meaning and boundary |
| --- | --- |
| `G_cmp_Z,A(k_A)` | decides whether current and predecessor complete or fixed-mask Z views are comparable under identity, version, profile, basis and object-type rules |
| `Delta Z_A(k_A)` | signed coordinate-wise first difference between two comparable complete Z states; retains all five components in `[-1,1]` |
| `Delta Z_A^{[M]}(k_A)` | signed first difference over one unchanged predeclared partial set `M`; not an event-wise changing intersection |
| `Delta2 Z_A(k_A)` | coordinate-wise change of comparable movement across three complete states; components lie in `[-2,2]` |
| `Delta T_Z,A(k_A)` | categorical before/after transition of the five typed coordinate statuses |
| `Drift_L1,A(k_A)`, `Drift_L2,A(k_A)` | raw scalar L1/L2 magnitudes derived from an applicable complete Z difference |
| `Drift_L1_norm,A(k_A)`, `Drift_L2_norm,A(k_A)` | dimension-normalized complete-state movement sizes under a declared norm profile |
| `Drift_L1_norm,A^{[M]}(k_A)`, `Drift_L2_norm,A^{[M]}(k_A)` | separately identified normalized movement sizes over one fixed partial set `M` |

`Delta2 Z` means second difference, not `(Delta Z)^2`. Without an explicit
time/sampling contract it is not physical acceleration. `Delta T_Z` is not
numeric movement from zero: for example, `not_observable -> numeric` reports a
status transition without inventing the earlier numeric value.

Norms lose direction and coordinate attribution. They therefore remain linked
to the signed source delta, active dimension/mask and metric profile. A larger
norm is movement size—not automatically loss, error, instability, improvement
or relational coupling.

Sources: [Z comparability and source-local dynamics](./KSODI-Standard-Eval/Layer-2_KSODI-State-Vector-Z_V350/KSODI_State-Vector-Z_V351.md#4-comparability-and-source-local-dynamics)
and [drift norms](./KSODI-Standard-Eval/Layer-2_KSODI-State-Vector-Z_V350/KSODI_State-Vector-Z_V351.md#5-drift-norms-and-interpretation).

### 5.8 Complete Z windows and joint aggregation

| Term | Reader meaning and boundary |
| --- | --- |
| `W_A` | identified source-local window with bounds, order, overlap and declared opportunity/member basis |
| `W_complete_Z,A` | one shared subset of complete numeric Z members inside `W_A` |
| `p_ZSigma` | named/versioned joint Z aggregation profile, including count, coverage, aggregator and status policies |
| `Z_Σ_A(W_A)` | typed joint five-coordinate window aggregation over the one shared complete subset |
| `complete_rate_Z,A(W_A)` | complete-Z member count divided by its declared opportunity denominator |
| `numeric_rate_X,A(W_A)` | coordinate-specific numeric availability rate; a diagnostic, not the joint aggregate basis |

All five coordinates of `Z_Σ_A(W_A)` use the same complete member set.
Coordinate-wise summaries over different subsets can be useful diagnostics,
but they do not form one joint state-vector aggregate.

The aggregate retains exact members and exclusions, counts, denominator,
status partitions, coverage, aggregation functions, profile/version and
provenance. An empty opportunity set and `0/0` do not become numeric zero.

Source: [Z Sigma, Hangar and coverage](./KSODI-Standard-Eval/Layer-2_KSODI-State-Vector-Z_V350/KSODI_State-Vector-Z_V351.md#6-sigma-sigmahangar-and-coverage).

### 5.9 Point collections and Hangar views

| Term | Reader meaning and boundary |
| --- | --- |
| `H_Z,A^(event)` | attributed collection of complete event-level Z points |
| `H_Z,A^{[M]}` | separately stratified collection of partial points sharing the same fixed mask `M` |
| `Z_Σ_A(Hangar)` | typed distribution/point-cloud view over declared members and object levels |

Every point retains source, event, trajectory, profile, status/mask, window and
derivation provenance. Partial points are not silently embedded into complete
five-dimensional space. Aggregate points are not event points. Display jitter,
colour or layout changes no mathematical geometry and creates no new state.

These collections support observation and later question-led analysis; they do
not by themselves establish semantics, relation, resonance or evaluation.

### 5.10 `Z_agg(W)` — a derived window object, not an event state

`Z_agg(W)`, logically typed as `DerivedZWindowAggregate`, is the separately
identified aggregate-Z object used by an `aggregate_then_derive` question. It
must carry:

1. its own derived-object identity;
2. exact window, member and exclusion identities;
3. counts, coverage and status partitions;
4. aggregator and version;
5. coordinate/profile/numeric policies;
6. result status and provenance;
7. a clear boundary from canonical event-level `Z_A(k_A)`.

It has no `target_event_id`, does not pretend to be an utterance or
participant state and is never written back as the state of one member. Its
technical five-coordinate completeness does not make it canonical event Z.

Source: [IK window contract — derived aggregate-Z object](./KSODI-Standard-Eval/Layer-3_KSODI-Monadic-Interaction-Coherence-IK_V350/IK_M2_V351_REFERENCE_REVIEW/IK_V351_WINDOW_AGGREGATION_ORDER_CONTRACT_V01.md#8-derived-aggregate-z-window-object).

### 5.11 Two window processing orders

```text
derive_then_aggregate:
  derive one result from each eligible complete Z,
  then aggregate the per-state results

aggregate_then_derive:
  aggregate one shared eligible set of complete Z vectors,
  then derive results from that aggregate Z
```

These orders answer different questions and nonlinear result families need not
agree. The processing order, member basis, state/result aggregator versions,
coverage and order-gap result remain explicit.

Window aggregation, state derivation, result derivation, `Delta`, `Delta2`,
path length and window-to-window difference are separate operations. None may
be substituted for another merely because their displays look similar.

Source: [IK v3.51 window aggregation-order contract](./KSODI-Standard-Eval/Layer-3_KSODI-Monadic-Interaction-Coherence-IK_V350/IK_M2_V351_REFERENCE_REVIEW/IK_V351_WINDOW_AGGREGATION_ORDER_CONTRACT_V01.md).

### 5.12 Z-to-IK and relational branch boundaries

Complete typed Z remains the reconstructible machine object. Layer-3 IK
provides declared projections and geometric views:

```text
complete typed Z
  -> IK_w
  -> IK_M2
  -> IK_ref
  -> AxisDev_ref
  -> jointly navigable IK-Gesamtbild
```

The arrows show dependency routes, not replacement. Scalar or geometric
equality does not establish equality of complete Z states. Every IK view must
retain the route back to `R_Z`, complete labelled Z, the five coordinate
records, profiles and evidence.

After typed Z, monadic IK and relational R0 are separate branches. The
canonical v3.51 architecture is not a serial numeric chain
`Z -> IK -> R0`. A separately named IK-conditioned R0 transition analysis
remains research and does not make IK an undeclared R0 operand.

Source: [State Vector Z — downstream boundaries](./KSODI-Standard-Eval/Layer-2_KSODI-State-Vector-Z_V350/KSODI_State-Vector-Z_V351.md#7-downstream-boundaries).

### 5.13 Section-5 collision and reconstruction guard

| Related terms | Required distinction |
| --- | --- |
| `R_Z` / `Z_A(k_A)` | complete typed assembly record / conditional complete numeric projection |
| `T_Z` / `A_Z` | five typed coordinate statuses / derived numeric-availability bits |
| Layer-1 `component_mask` / `A_Z` / `M` | operator component selection / numeric availability / predeclared partial coordinate set |
| `G_Z,identity` / `G_Z,complete` / `G_cmp_Z` | assembly alignment / numeric completeness / legitimacy of one requested comparison |
| `Delta Z` / `Delta2 Z` / `Delta T_Z` | signed movement / change of movement / categorical status transition |
| `Delta Z` / drift norm | directed full coordinate movement / compressed movement size |
| `Z_A(k_A)` / `Z_Σ_A(W_A)` / `Z_agg(W)` | event state projection / joint window aggregate / derived aggregate-then-derive operand |
| event point / aggregate point / partial point | different identities and object levels; display proximity does not merge them |

For every derived Layer-2 object, reconstruction should reach exact member or
event identities, all five Layer-1 result records, statuses/reasons, profiles,
transformations, exclusions and provenance. Missing evidence is not recreated
from a mean, norm, curve or point cloud.

### 5.14 Section-5 draft decisions and reopening points

This reader gives `R_Z` priority while retaining `Z_A(k_A)` as a separate,
equally searchable canonical numeric projection. It keeps `Z_agg(W)` and both
aggregation orders visible because they protect object identity and later IK
interpretation.

Still open for later method, implementation and presentation work:

1. which assembly/projection/window profile names belong in the main reader
   versus a controlled technical appendix;
2. the final visual language distinguishing operator component masks, `A_Z`
   and partial set `M`;
3. how much partial-Z and aggregate-Z detail different reader views require;
4. concrete Basic-Visuals treatment of statuses, complete/partial points,
   coverage and reconstruction drill-down;
5. physical implementation schema and independent runtime-conformance evidence.

These questions keep presentation and implementation open. They do not permit
silent zero filling, dynamic masks, loss of Layer-1 records or confusion of an
aggregate with an event.

---

<a id="glossary-layer3-ik"></a>

## 6. Layer 3 — monadic IK and the `IK-Gesamtbild`

### 6.1 IK is a family of declared views, not a replacement for Z

Layer 3 derives question- and profile-bound monadic views from one exact
complete typed Z. The released v3.50 weighted projection remains the
compatibility basis; v3.51 adds tested fixed-reference geometry and a jointly
navigable view without turning several results into one verdict.

```text
complete typed Z
├── IK_w          active weighted-axis position
├── IK_M2         normalized complete-vector magnitude
├── IK_ref        fixed equal-coordinate-axis position
├── AxisDev_ref   deviation from that fixed axis
└── complete identities, profiles, statuses and provenance
```

Equal scalar values do not establish equal complete Z states. None of these
results by itself proves semantic coherence, goodness, truth, stability or a
hidden inner state.

Sources: [IK v3.51](./KSODI-Standard-Eval/Layer-3_KSODI-Monadic-Interaction-Coherence-IK_V350/KSODI_Monadic-Interaction-Coherence-IK_V351.md)
and [v3.51 IK result contract](./KSODI-Standard-Eval/Layer-3_KSODI-Monadic-Interaction-Coherence-IK_V350/IK_M2_V351_REFERENCE_REVIEW/IK_M2_V351_RESULT_CONTRACT_V01.md).

### 6.2 Active weighted projection: `p_IK`, `w(p_IK)` and `IK_w`

| Term | Reader meaning and boundary |
| --- | --- |
| `p_IK` | named/versioned active monadic projection profile for one intended question |
| `w(p_IK)` | ordered nonnegative weights summing to one; binds the active projection direction |
| `w_ref` | transparent equal-weight profile `(0.2,...,0.2)`; not a validated optimum or the fixed unit geometry `u_ref` |
| `IK_A(k_A | p_IK)` / `IK_w` | profile-relative scalar `w(p_IK) dot Z`; released v3.50 calculation with the distinguishing v3.51 reader label `IK_w` |

The result requires exact complete Z, source/event identity, profile/version,
unrounded value, typed status and provenance. A zero weight does not waive
complete-input eligibility. `IK_w` is an axis position—not full Z, magnitude,
quality or relational `IK_rel`.

### 6.3 Typed IK status and declared reduced projection

Every selected IK result distinguishes `numeric`, `not_selected`,
`not_observable`, `not_applicable` and processing failure. Nonnumeric states
have no numeric value; processing failure is not a method-result status.

`p_IK^{[M]}`, `IK_A^{[M]}` and the within-`M` renormalized weights
`w_tilde_X` form a separately named reduced diagnostic over one fixed
predeclared nonempty coordinate set. They do not provide dynamic fallback,
imputation or canonical complete IK, and results over changing masks/profiles
are not silently comparable.

### 6.4 Fixed-reference geometry

| Term | Reader meaning and boundary |
| --- | --- |
| `u_ref` / `z_equal_coordinate_diagonal` | fixed unit direction `(1,1,1,1,1)/sqrt(5)` with stable geometry identity |
| `IK_M2` / `ik_normalized_l2_magnitude` | `||Z||_2/sqrt(5)`: normalized complete-vector magnitude; not composition or coherence by itself |
| `IK_ref` / `ik_fixed_reference_axis_position` | fixed-axis position `(u_ref dot Z)/sqrt(5)=mean(Z)`; retained as a first-class laboratory result |
| `AxisDev_ref` / `ik_fixed_reference_axis_deviation` | normalized Euclidean distance from the fixed diagonal; exposes unequal coordinate composition at the same axis position |

`w_ref` and `u_ref` share an equal-coordinate intuition but are different
objects with different normalization and function. The fixed reference is not
an active learned axis, target corridor, truth direction or self-confirming
norm.

The same complete Z under the declared Euclidean geometry satisfies:

```text
IK_M2^2 = IK_ref^2 + AxisDev_ref^2
```

This is a decomposition identity and consistency check—not three independent
votes on coherence or correctness.

Source: [IK v3.51 public geometry concept](./KSODI-Standard-Eval/Layer-3_KSODI-Monadic-Interaction-Coherence-IK_V350/IK_M2_AXIS_DEVIATION_DUAL_RESOLUTION_PUBLIC_CONCEPT_V351.md).

### 6.5 `IK-Gesamtbild` / `ik_joint_evaluation_view`

`IK-Gesamtbild` is the human-facing method/governance name; the language-
neutral logical identifier is `ik_joint_evaluation_view`. It makes `IK_w`,
`IK_M2`, `IK_ref`, `AxisDev_ref` and their return route to complete Z jointly
navigable.

It is:

- no `IK-Gesamtwert`;
- no fourth calculation or scalar average;
- no replacement truth;
- no permission to discard coordinate composition, statuses or provenance.

Its minimum record includes component result IDs/statuses, active profile,
fixed geometry, raw result links, Z/evidence references and renderer/view
version. Concrete Basic-Visuals rules remain later work.

### 6.6 Comparability and movement

IK comparison requires stable source/trajectory identity, Z semantics, result
kind, formula, profile/weights, geometry, predecessor relation and numeric
statuses. Numeric equality or timestamp proximity does not establish this
contract.

| Dynamic | Question answered |
| --- | --- |
| `Delta IK_w`, `Delta2 IK_w` | change along one stable active weighted axis / change of that movement |
| `Delta IK_M2`, `Delta2 IK_M2` | change of complete-vector magnitude / its second difference |
| `Delta IK_ref`, `Delta2 IK_ref` | change along the fixed reference diagonal / its second difference |
| `Delta AxisDev_ref`, `Delta2 AxisDev_ref` | change of deviation from the fixed diagonal / its second difference |

All remain linked to signed `Delta Z`/`Delta2 Z`. They do not reconstruct
vector direction, path length, detour or physical acceleration without the
missing contracts. A changed axis/profile is not reported as state movement;
reprojection and counterfactual comparisons must be labelled separately.

### 6.7 Windows, processing order and Hangar views

| Term | Reader meaning and boundary |
| --- | --- |
| `W_A^IK` | identified source-local IK opportunity window |
| `coverage_IK(W_A)` | numeric eligibility coverage with explicit numerator, denominator and status |
| `IK_Σ,A(W_A | p_IK)` | typed aggregate weighted-IK result over one exact eligible member set |
| IK `Sigma(Hangar)` | profile/status-stratified distribution or trajectory view, not a new method result |

Members, exclusions, overlap, count, coverage, status partitions, aggregator,
profiles and provenance remain visible. Sparse high values do not become a
strong whole-window claim; an empty denominator is not numeric zero.

`derive_then_aggregate` and `aggregate_then_derive` retain different question
identities. Linear `IK_w` and `IK_ref` may commute with arithmetic mean under
matching conditions; nonlinear `IK_M2` and `AxisDev_ref` generally need not.
The processing order and any order-gap result remain explicit.

### 6.8 Raw result, numeric policy and presentation

Keep three objects separate:

```text
unrounded method result
  -> versioned numeric policy
  -> derived presentation value
```

Readable real-valued displays may round, label or transform axes only under a
declared display policy with reverse link. Displayed zero need not be exact
zero. A presentation value never becomes stored evidence or a later
calculation operand.

### 6.9 Reverse navigation and downstream boundary

Every IK result/view must navigate back to its complete typed Z, all labelled
K/S/O/D/I coordinate records, statuses, profiles, evidence and provenance.
The governance line is a navigable projection of the retained machine object,
not an Ersatzwahrheit.

R0 still consumes complete comparable signed `Delta Z`; primary `IK_rel`
later compares paired raw `Delta IK_w` only after the exact required R0
handoff. `IK_M2`, `IK_ref`, `AxisDev_ref` and the IK-Gesamtbild do not
implicitly enter either contract.

### 6.10 Section-6 collision and reopening guard

| Related terms | Required distinction |
| --- | --- |
| `IK_w` / `IK_M2` / `IK_ref` / `AxisDev_ref` | active-axis position / magnitude / fixed-axis position / fixed-axis deviation |
| `w_ref` / `u_ref` | equal-weight profile / fixed unit geometry |
| `IK-Gesamtbild` / `IK-Gesamtwert` | navigable multi-result view / forbidden silent scalar compression |
| state movement / axis change | changed complete Z under stable rule / changed projection or geometry rule |
| raw value / numeric policy / presentation value | calculation / calculation handling / human-facing display |
| `Delta IK_*` / signed `Delta Z` / path length | scalar-view movement / full directed movement / accumulated route |

Open for later method, implementation and presentation work are main-reader
versus technical-appendix placement, final bilingual labels/examples,
Basic-Visuals rules, window profile choices and runtime-conformance evidence.
These questions do not permit compression into a single score or loss of the
reverse route.

---

<a id="glossary-layer4-r0"></a>

## 7. Layer 4 — R0 relational eligibility gate

### 7.1 R0 starts relational eligibility, not relational proof

`R_0` (path-safe: `R0`) asks whether explicitly declared, separately retained
trajectories meet one named availability, comparability and bounded-movement
policy for a specified later branch. It does not establish receipt, agreement,
shared meaning, coupling, resonance, alignment or permission to act.

Keep six objects distinct:

```text
declared pairing
  -> source-local movement eligibility
  -> numeric R0 result and typed result status
  -> separate gate state
  -> exact branch-specific handoff
  -> retained exclusions and reasons
```

Source: [R0 v3.51 method](./KSODI-Full/Layer-4_KSODI-Relational-Gate-R_0_V350/KSODI_Relational-Gate-R_0_V351.md).

### 7.2 Atomic identity, pairing and independent predecessors

`rho_AB(j | pi(j))` identifies one atomic dyadic gate opportunity. The pairing
map `pi(j)=(k_A(j),k_B(j))` binds exact current positions from two separate
source-local trajectories to relational index `j`. Chronological adjacency,
shared conversation or similar values do not create this pair.

Each member resolves its own predecessor and complete signed `Delta Z_E`.
Neither a shared fabricated predecessor, unsigned drift nor `Delta IK` can
replace those two full movement records. Movement-level `incomparable` remains
a processing/comparison classification, not an external R0 result status or
numeric zero.

### 7.3 Profile, movement norms and canonical result

| Term | Reader meaning and boundary |
| --- | --- |
| `p_R0` / `R0Profile` | named/versioned projection, coordinate metric, norm, trajectory aggregation, threshold, clipping and numeric-policy contract |
| `d_E,L1(j)` | normalized complete L1 movement magnitude for member trajectory `E`; canonical only with the fixed equal-coordinate reference metric |
| `d_E,L2(j)` | separately profiled normalized complete Euclidean movement magnitude under the fixed equal-coordinate basis |
| `R0_raw,AB(j)` | unclipped canonical dyadic result before numeric tolerance handling |
| `R0_AB(j)` | typed/clipped canonical result: one minus the arithmetic mean of A's and B's L1 movement magnitudes |
| `coordinate_metric_profile_id` | identifies equal coordinate contribution in canonical v3.51; alternative `g` controls are not silently active profiles |

High R0 means low average movement under that exact profile. It does not say
the members moved in the same direction, were semantically compatible or were
in relation. L1 and L2 are separately named profiles, not interchangeable
calculations.

### 7.4 Result status, gate state and threshold

| Object | Values and boundary |
| --- | --- |
| R0 result status | `numeric`, `not_selected`, `not_observable`, `not_applicable`; processing failure and movement `incomparable` remain separate |
| `gate_state` | `open`, `closed`, `not_evaluable`; derived from typed R0 result plus profile threshold |
| `theta_R0_gate_open_min` | finite versioned `[0,1]` minimum numeric R0 value using the declared `>=` opening rule; it is not a stability claim |
| `aggregate_drift_max` | exact derived counterpart `1 - theta_R0_gate_open_min`; it must not become an independently drifting second parameter |
| `theta_R0_stable` | v3.50 legacy alias only; migrate to `theta_R0_gate_open_min` and do not interpret it as observed social, semantic, relational or systemic stability |
| threshold parameter origin / evidence reference | records where the declared value came from without inventing empirical support |
| threshold calibration status | distinguishes a set value such as `set_not_empirically_calibrated` from an evidenced calibration claim |

A valid numeric closed gate is not `not_applicable`; `not_evaluable` is not a
numeric closed result. The threshold is a policy parameter, not observed
evidence, universal constant, coupling fact, moral cutoff or action authority.
`open` means eligible for the exact named downstream comparison; `closed`
means only that the numeric gate threshold was not met.

### 7.5 Alternative and extended profiles

| Term | Reader meaning and boundary |
| --- | --- |
| `R0_AB^[M](j)` | visibly reduced dyadic gate over the same predeclared fixed set `M` on both trajectories; does not open current primary IK_rel |
| `R0_w,AB(j)` | separately named fixed member-weight aggregation; weights are not empirical importance facts |
| `a_AB(j)` | optional movement-asymmetry diagnostic `|d_A-d_B|`; exposes mean-hidden imbalance without changing canonical R0 |
| `C(q)`, `Pi(q)`, `R0_C(q)` | declared n-adic constellation, member mapping and complete n-adic gate; no automatic n-adic IK_rel follows |

Complete, fixed-partial, weighted and n-adic R0 results retain distinct profile
and result identities. Members or coordinates are never silently removed and
remaining weights renormalized.

### 7.6 Comparability, dynamics and windows

R0 comparison requires stable membership semantics, map, predecessor policy,
Z definitions, complete/partial kind, `M`, norm, aggregation, weights,
clipping and threshold. Equal displayed results or the same dyad name are not
enough.

`Delta R0_AB(j)` and `Delta2 R0_AB(j)` are first and second differences of
comparable numeric R0 results. They are not member `Delta Z`, gate-state
transitions, path length or change in the relationship.

| Window term | Reader meaning and boundary |
| --- | --- |
| `W_AB^R0` | exact eligible numeric R0 member set inside one declared relational window |
| `coverage_R0` | numeric R0 coverage under its own opportunity denominator |
| `gate_open_rate` | open gates among the relevant valid gate opportunities; not coverage or mean R0 |
| `R0_Sigma` | typed aggregate under minimum-count/coverage and aggregation profile |
| R0 `Sigma(Hangar)` | profile/status/gate-stratified distribution and trajectory view |

Every excluded step remains in the opportunity ledger with reasons. Empty
denominators are non-evaluable, not zero. Mixed masks, norms, thresholds or
statuses are not pooled into an unlabeled population.

### 7.7 Exact handoff to current primary `IK_rel`

The current primary dyadic `IK_rel` requires the actual matching R0 record to
be compatible, numeric, canonical-complete and open for the same ordered dyad,
paired events, predecessors, profile and relational step. Reduced, n-adic or
merely projected feasibility cannot substitute for that handoff.

Its current monadic movement operands are explicitly paired comparable
`Delta IK_w` under one shared identifiable canonical IK weight profile. Generic
`Delta IK`, `IK_M2`, `IK_ref` or `AxisDev_ref` cannot silently replace them.

`R0_max_from_projection` is an assertion-checked diagnostic bound on
the maximum canonical L1 R0 attainable from a specified equal-weight projected
movement pair. It asks whether opening may be geometrically possible—not
whether the actual off-axis movements produced a valid open gate. It neither
replaces R0 nor fabricates an `IK_rel` operand.

### 7.8 Gate exclusions and staged transition research

A closed, non-evaluable or mismatched gate does not delete the observation
opportunity. Retain both full monadic trajectories, complete movements, R0
record/profile/state, exclusion reason and applicable privacy/retention policy.
This makes later behind-the-gate analysis possible without emitting current
primary `IK_rel`.

The bounded [Phase-D+ complete-Z gate-exclusion regression](./KSODI-Full/Layer-5_KSODI-Dyadic-Relational-Coherence-IK_rel_V350/IK_REL_V351_REFERENCE_REVIEW/PHASE_D_PLUS_GATE_EXCLUSION_RESULTS.md)
keeps this route inspectable across five asserted boundary cases. It is
reference evidence for status separation and operand retention, not empirical
threshold calibration, runtime-conformance proof or activation of a new
behind-the-gate method.

The accepted staged working name is:

- human: **IK-konditionierte R0-Übergangsanalyse**;
- technical: `ik_conditioned_r0_transition_analysis`.

It asks retrospectively, counterfactually or exploratively when a declared R0
corridor would be entered, left or crossed under explicit assumptions. It is
Future Research: IK does not thereby become an R0 input, and the actual gate
record is never overwritten.

### 7.9 Section-7 collision and reconstruction guard

| Related terms | Required distinction |
| --- | --- |
| pairing / numeric R0 / gate state / handoff | declared membership / result / threshold decision / branch eligibility |
| `closed` / `not_evaluable` / `incomparable` | valid numeric gate state / no evaluable gate state / blocked operand comparison |
| L1/L2 drift / `IK_M2` / `Delta IK_w` | movement norms / state magnitude / projected axis movement |
| complete / fixed-M / weighted / n-adic R0 | separately identified profiles and result kinds |
| actual R0 / `R0_max_from_projection` | observed gate calculation / existential projected feasibility diagnostic |
| exclusion / deletion / sidecar diagnosis | retained blocked opportunity / loss / separately named future analysis |

Open for later review are reader placement of profile symbols and feasibility
diagnostics, wording for bounded movement without value judgement, empirical
threshold profiles and the first safe transition-analysis fixture. These do
not weaken the strict current handoff.

---

<a id="glossary-layer5-ik-rel"></a>

## 8. Layer 5 — dyadic `IK_rel`

### 8.1 Current bounded claim

Current primary `IK_rel` measures compatibility of paired observable monadic
movement along one shared declared `IK_w` axis, inside the exact open R0
stability corridor. It does not create a shared state or establish agreement,
truth, alignment, causation, coupling, resonance or control authority.

`rho_AB(j | pi(j))` is the exact relational evaluation identity: ordered dyad,
pairing, paired events, separate trajectories/predecessors, relational index,
scope and all R0/IK/component profiles remain attributable.

The required handoff is the actual matching compatible, numeric, open,
canonical-complete dyadic R0 record. Another branch's gate, reduced/n-adic R0,
high monadic IK or projected feasibility cannot substitute.

Sources: [IK_rel v3.51](./KSODI-Full/Layer-5_KSODI-Dyadic-Relational-Coherence-IK_rel_V350/KSODI_Dyadic-Relational-Coherence-IK_rel_V351.md)
and the [v3.51 reference-review package](./KSODI-Full/Layer-5_KSODI-Dyadic-Relational-Coherence-IK_rel_V350/IK_REL_V351_REFERENCE_REVIEW/README.md).

### 8.2 Typed result decision and primary movement component

IK_rel result status distinguishes `numeric`, `not_selected`,
`not_observable`, `not_applicable` and processing failure under an explicit
decision order. Closed-gate `not_applicable`, unobservable operands and
numeric zero are different states.

For the primary movement profile:

```text
g_move,AB(j) = |Delta IK_w,A - Delta IK_w,B|
C_move,AB(j) = 1 - g_move,AB(j) / 2
primary IK_rel = C_move under profile N={move}
```

High `C_move` means similar signed projected movement on the shared axis. It
does not establish equal complete `Delta Z`, equal coordinate direction in
five dimensions or resonance.

`static_step` makes the movement component non-applicable only for joint
projected first-order zero under the recorded exact-zero reference policy. It
does not prove complete-Z stillness, silence or intent.

The precise v3.51 reason label for that non-applicable result is
`joint_projected_zero_under_numeric_policy`. Shorter historical or review
labels remain searchable aliases, not a second status or reason definition.

### 8.3 Three derivative-order questions

| Component | Question and boundary |
| --- | --- |
| `C_gap(j)` | compatibility of current positions `1-|IK_w,A-IK_w,B|`; not movement or trajectory similarity |
| `C_move(j)` | compatibility of first projected differences; primary current profile |
| `C_accel(j)` | compatibility of second projected differences; not physical acceleration without a time contract |

`zero_accel_step` belongs only to the second-order component. Derivative-order
eligibility is independent: a numeric movement component can coexist with
non-applicable acceleration, and joint rest can still leave a separately
defined second-order question.

`C_shared` remains reserved/unselected. `T_G,AB(j)` preserves the ordered typed
status and reasons of gap, movement, acceleration and shared components; it is
not a dynamically shortened numeric vector.

Even the full `(C_gap,C_move,C_accel)` triplet is not a trajectory, path-length
or activity measure.

### 8.4 Fixed component sets and extended projections

`N` is one predeclared nonempty subset of `{gap,move,accel}`. `v_rel(N)` binds
finite nonnegative weights by component name and sums them to one;
`p_rel^[N]` identifies the complete projection contract.

`IK_rel^[N]`, logically `ik_rel_fixed_component_projection`, exists only when
all required components in unchanged `N` are numeric. Components are not
removed and remaining weights renormalized at runtime. Different `N`, weights,
definitions or epsilon policies produce different result kinds. The primary
current `IK_rel` is the fixed `{move}` projection.

### 8.5 Positive epsilon taxonomy

| Epsilon kind | Meaning and boundary |
| --- | --- |
| `epsilon_numeric_tolerance` | handling of numerical calculation/representation near a boundary |
| `epsilon_observation_resolution` | declared instrument limit below which movement is not observably resolved; unresolved is not inserted as numeric zero |
| `epsilon_question_relevance` | question-specific relevance band; membership does not imply physical stillness or unobservability |

Each epsilon records component, value/domain/scale, boundary rule,
rationale/evidence, profile/version, raw operands and status consequence.
Rounding and the R0 threshold are not epsilon kinds. No positive universal
default has been selected.

`movement_epsilon_band_rate` reports the share of reached post-open-gate
movement opportunities inside the declared joint band. It is not
`static_step`, complete-Z stillness, coverage or gate-open rate.

### 8.6 Diagnostic bundle and comparability

The logical `ik_rel_diagnostic_bundle` keeps the selected relational result
together with:

```text
raw paired Delta IK_w
both complete directed Delta Z
componentwise differences and statuses
exact R0 handoff/exclusion record
separately selected and valid later R-branch diagnostics
```

It is a question-led navigation bundle, not a fourth scalar or total
relational state.

IK_rel comparison requires stable dyad/pairing, R0 profile/threshold, monadic
IK axis, component set/definitions/weights, epsilon policy and typed result
state. Equal scalar values do not identify dyads, paths or complete movements.
`Delta IK_rel` and `Delta2 IK_rel` are first and second differences of
consecutive comparable numeric relational results—not monadic movement,
gate-state change, window difference or change of the relation itself.

### 8.7 Opportunity ledger, rates and strict window result

| Set/rate | Reader meaning and boundary |
| --- | --- |
| `W_AB` | all declared relational opportunities in the identified window |
| `W_AB^gate` | opportunities with valid matching R0 handoff records |
| `W_AB^open` | valid gate opportunities whose gate state is open |
| `W_AB^move` | open opportunities that reach the selected movement/epsilon policy |
| `W_AB^rel` | opportunities yielding numeric selected IK_rel results |
| `coverage_rel` | numeric results over its declared relational opportunity denominator |
| `gate_open_rate` | open gates over valid gate opportunities |
| `movement_epsilon_band_rate` | in-band cases over opportunities reaching the movement-band question |

Each rate has its own numerator, denominator, status and profile. Empty
opportunity, zero eligible members and failed coverage remain different
states; no `0/0` becomes zero.

`ik_rel_window_aggregate` under `strict_integrity_v351` emits an official
numeric aggregate only under stable identity/profile, declared minimum count
and coverage, contained processing conditions and explicit status precedence.
No universal empirical thresholds are selected; reference-fixture values are
not production recommendations.

If official emission fails, `diagnostic_numeric_subset_summary` may describe
the exact numeric subset only when marked `diagnostic_only=true` and
`conditional_on_numeric_subset=true`, with every partition and failed
condition visible. It is not a complete-window result.

### 8.8 PPWA and long/dense windows

PPWA means `partition_preserving_window_aggregation`. It preserves every
numeric, nonobservable, nonapplicable, gate-closed and processing partition
with counts, reasons, denominators, membership and provenance.

The future profile names are:

- `bounded_processing_tolerance`;
- `partition_preserving_bounded_tolerance`;
- compact: `PPWA-bounded`.

The PPWA principle and names are accepted; the bounded-tolerance profile is
not activated or empirically calibrated. It may later support a separately
bounded conditional view for large/dense windows, but never deletion, zero
filling, majority truth or relabelling the numeric subset as the whole window.

### 8.9 Point clouds and three consumer projections

`P_rel,AB(j)` is a rich typed relational point record. The logical
`ik_rel_window_point_cloud` partitions points by compatible profiles,
component sets, statuses and gate/window identities. It is not a merged dyadic
inner state; cluster movement is not signed `Delta IK_rel`.

One attributable basis may support three distinguishable projections:

1. deterministic machine calculation with exact operands and policies;
2. bounded assistive-LLM interpretation with declared inputs, uncertainty and
   non-authoritative semantics;
3. human-governance display with comprehensible labels and drill-down.

Neither LLM interpretation nor rounded display overwrites method results,
statuses, profiles or computational operands.

### 8.10 Migration and reconstruction

The v3.51 migration classes are:

| Classification | Meaning |
| --- | --- |
| `v351_conformant` | full required identities, operands, profiles, statuses and provenance retained |
| `legacy_reconstructible` | missing current structure can be recovered from attributable retained evidence |
| `legacy_partially_reconstructible` | only a bounded subset can be recovered; loss/uncertainty remain explicit |
| `legacy_noncomparable` | required basis cannot support the requested current comparison |

`reconstruction_pending` and related workflow states remain separate from
method-result status. Nonconformant does not mean worthless, and missing
provenance is never invented as fact.

Every IK_rel result/view retains the reverse route:

```text
IK_rel result/view
  -> exact R0 handoff and pairing
  -> paired Delta IK_w
  -> both complete directed Delta Z histories
  -> both typed Z trajectories
  -> both Layer-1 evidence/profile/provenance chains
```

This prevents the dyadic scalar from swallowing distinguishable monadic
movements. Reconstruction access does not prove causality or shared state.

### 8.11 Claim boundary toward R-family

```text
monadisch kohärent
  != dyadisch kohärent
  != dyadisch resonant
```

Monadic IK is a profile-relative view of one trajectory. Current IK_rel is
dyadic projected-movement compatibility after its gate. Resonance requires a
separately defined later R-family question with its own geometry, timing,
voice/evidence, profiles and validity. High IK_rel need not mean resonance;
resonance is not truth.

### 8.12 Section-8 collision and reopening guard

| Related terms | Required distinction |
| --- | --- |
| `C_gap` / `C_move` / `C_accel` | static position / first-order movement / second-order movement compatibility |
| result status / component status / gate state / window status / reconstruction state | separate typed vocabularies |
| exact zero / numeric tolerance / observation resolution / question relevance | different policies and epistemic claims |
| primary `{move}` / fixed `N` / diagnostic bundle / window aggregate / point cloud | different result/view kinds |
| `coverage_rel` / `gate_open_rate` / movement-band rate | different opportunity sets and denominators |
| strict aggregate / diagnostic subset / PPWA | official reference result / conditional description / partition-preserving future principle |
| monadic IK / current IK_rel / later resonance | different objects, gates, questions and claim limits |

Open for later method, implementation and presentation work are logical-
identifier placement, plain-language component diagrams, empirically
justified epsilon/count/coverage profiles, PPWA Basic Visuals,
consumer-specific diagnostic bundles and final resonance-boundary language.
These do not alter the strict v3.51 reference contract.

---

## Current review boundary

Sections 0–8 cover the frame, shared vocabulary and Layers 0–5. The compact
appendices below provide alternative status, mask/set, movement, identifier,
collision, migration and authority routes. Public reference suites preserve
worked calculations and reverse routes to the declared operands. Their
presence is bounded reference evidence, not independent runtime conformance or
empirical validation.

---

## Appendix A — Public layer and terrain index

| Terrain | Reader section | Primary public route |
| --- | --- | --- |
| scope, architecture and shared vocabulary | Sections 0–3 | [Architecture v3.51](./KSODI-Architecture_V351.md) |
| KSODI-Light and K/S/O/D/I | Section 4 | [KSODI-Light](./KSODI-Light/README.md) and [Layer 1](./KSODI-Standard-Eval/Layer-1_KSODI-Operators_V350/README.md) |
| complete typed Z | Section 5 | [Layer 2](./KSODI-Standard-Eval/Layer-2_KSODI-State-Vector-Z_V350/README.md) |
| monadic IK | Section 6 | [Layer 3](./KSODI-Standard-Eval/Layer-3_KSODI-Monadic-Interaction-Coherence-IK_V350/README.md) |
| relational gate R0 | Section 7 | [Layer 4](./KSODI-Full/Layer-4_KSODI-Relational-Gate-R_0_V350/README.md) |
| dyadic IK_rel | Section 8 | [Layer 5](./KSODI-Full/Layer-5_KSODI-Dyadic-Relational-Coherence-IK_rel_V350/README.md) |
| window aggregation | Sections 5–8 and Appendix D | [IK window contract](./KSODI-Standard-Eval/Layer-3_KSODI-Monadic-Interaction-Coherence-IK_V350/IK_M2_V351_REFERENCE_REVIEW/IK_V351_WINDOW_AGGREGATION_ORDER_CONTRACT_V01.md) |

The private development record retains the exhaustive 215-entry inventory,
disposition ledger and cross-file reconciliation evidence. Those workbench
artifacts are not required to use or cite this Public reader.

<a id="glossary-status-families"></a>

## Appendix B — Typed status-family index

| Family | Examples | Never collapse into |
| --- | --- | --- |
| method-result status | `numeric`, `not_selected`, `not_observable`, `not_applicable` | one universal number or enum |
| processing outcome | identity, configuration or arithmetic failure | valid nonnumeric method result |
| comparison classification | `comparable`, `incomparable` | method-result status |
| assembly state | complete, `not_complete`, assembly error | Layer-1 result status |
| gate state | `open`, `closed`, `not_evaluable` | numeric R0 or downstream result status |
| component status | entries of `T_G` | dynamically shortened active set |
| window/aggregate state | empty, insufficient, emitted, processing-affected | atomic member status |
| migration class | conformant, reconstructible, partial, noncomparable | reconstruction workflow |
| reconstruction workflow | pending, in progress, reconstructed, failed | truth or evidence status |
| attribution state | stable, provisional, unknown | method score |

Every dash, blank, colour or omitted number in a human view must reveal its
status family, exact state, object, reason and reverse route. The table above
is the compact Public status-family map; exact state vocabularies remain in
their versioned method and result contracts.

## Appendix C — Masks, fixed sets and membership

| Object | What it selects or records | Boundary |
| --- | --- | --- |
| Layer-1 `component_mask` | profile-selected operator components | not numeric availability |
| `T_Z` | five coordinate-result statuses | not a mask |
| `A_Z` | derived five-bit numeric availability | does not retain absence reasons |
| `M` | fixed predeclared Z-coordinate subset | not event-wise numeric intersection |
| `pi(j)` | exact dyadic pairing map | not temporal adjacency |
| `C(q)` / `Pi(q)` | n-adic membership and member-position mapping | not a group state |
| `T_G` | typed statuses of fixed IK_rel components | not an active numeric vector |
| `N` | fixed nonempty IK_rel component set | not Z-coordinate set `M` |
| window member sets | opportunities and sequential eligibility partitions | exclusions remain in the ledger |

No mask, set or membership map permits silent deletion, filling, dynamic
intersection or renormalization.

## Appendix D — Delta and movement index

| Object | Operand level | Meaning |
| --- | --- | --- |
| `Delta X`, `Delta2 X` | one Layer-1 operator result | first/second source-local difference under stable profile |
| `Delta Z`, `Delta2 Z` | complete or fixed-M state vectors | directed coordinate movement / change of movement |
| `Delta T_Z` | typed coordinate statuses | categorical transition, not movement from zero |
| `Delta IK_*`, `Delta2 IK_*` | one monadic IK result kind | scalar-view movement under stable profile/geometry |
| `Delta R0`, `Delta2 R0` | comparable numeric gate results | gate-value dynamics, not gate-state transition |
| `Delta IK_rel`, `Delta2 IK_rel` | comparable numeric relational results | relational-projection dynamics, not relation change |
| path length/detour | sequence of directed movements | accumulated route, not endpoint difference |
| window/distribution difference | aggregate/distribution objects | a different operand level and question |

`Delta2 x` denotes a second difference. `(Delta x)^2` must be written
explicitly when a square is intended.

## Appendix E — Human labels, symbols and logical identifiers

| Human/method label | Symbol/source notation | Logical technical identifier | Maturity/boundary |
| --- | --- | --- | --- |
| typed aggregate-Z window object | `Z_agg(W)` | `DerivedZWindowAggregate` | derived object identity; not event Z |
| normalized complete magnitude | `IK_M2` | `ik_normalized_l2_magnitude` | accepted/tested v3.51 result kind |
| fixed equal-coordinate diagonal | `u_ref` | `z_equal_coordinate_diagonal` | accepted v3.51 geometry |
| fixed reference position | `IK_ref` | `ik_fixed_reference_axis_position` | accepted v3.51 result kind |
| fixed reference deviation | `AxisDev_ref` | `ik_fixed_reference_axis_deviation` | accepted v3.51 result kind |
| IK-Gesamtbild | combined IK view | `ik_joint_evaluation_view` | view, not scalar calculation |
| R0 profile | `p_R0` | `R0Profile` | logical schema kind, not prescribed table |
| IK-conditioned R0 transition analysis | staged analysis | `ik_conditioned_r0_transition_analysis` | Future Research |
| fixed-component IK_rel | `IK_rel^[N]` | `ik_rel_fixed_component_projection` | profile-bound result kind |
| relational diagnostic bundle | linked findings | `ik_rel_diagnostic_bundle` | view/bundle, not scalar |
| relational window aggregate | `IK_rel_Sigma` context | `ik_rel_window_aggregate` | strict v3.51 result kind |
| conditional subset summary | numeric subset description | `diagnostic_numeric_subset_summary` | diagnostic only |
| partition-preserving aggregation | PPWA | `partition_preserving_window_aggregation` | accepted principle; bounded profile future |
| relational point cloud | `P_rel,AB(j)` collection | `ik_rel_window_point_cloud` | derived view |

Logical identifiers are stable interface labels, not automatically physical
database columns, API fields or filenames.

<a id="glossary-alias-collision"></a>

## Appendix F — Collision and alias index

The Public high-risk collision and alias index includes:

- `R`, `R0`, `R_full` and R-family;
- `w_ref` versus `u_ref`;
- O/I `Ref_A` and D/I `V_A`;
- `n`, `k`, `j` and `t`;
- `M`, `N` and operator component masks;
- result status, assembly state, comparison class and gate state;
- `static_step`, epsilon-band membership and complete-Z stillness;
- complete event Z, partial Z and aggregate Z;
- `IK_w`, `IK_rel` and later R-family resonance.

Use the class—`ALIAS`, `COLLISION`, `RELATED_NOT_ALIAS`, `RETIRED` or
`PATH_SAFE`—before selecting reader wording. The private living register
retains the fuller review history and reopening notes.

<a id="glossary-legacy-migration"></a>

## Appendix G — Legacy, migration and Future Research

| Kind | Terms/routes | Reader rule |
| --- | --- | --- |
| released compatibility | v3.50 operator/Z/IK/R0/IK_rel contracts | retain released authority and mark v3.51 sharpening separately |
| migration class | `v351_conformant`, `legacy_reconstructible`, `legacy_partially_reconstructible`, `legacy_noncomparable` | not method-result status |
| retired | event-wise active-component renormalization, shared-inner-Hangar reading | reconstruction and explicit non-use only |
| conditional legacy label | `static_rate` | exact-zero legacy only; prefer band-specific rate where appropriate |
| v3.52 seam | Basic Visuals and detailed display/window profiles | not active v3.51 formula authority |
| v3.60+ seam | R-family, timing, voice and resonance questions | separately defined later methods/research |
| staged reconstruction | IK-conditioned R0 transition analysis and behind-gate diagnostics | never overwrite observed forward-method records |
| unactivated window profile | `PPWA-bounded` / bounded processing tolerance | principle named; thresholds and claim not calibrated |

### G.1 Exact v3.50 compatibility locators

| Exact locator | v3.51 reading |
| --- | --- |
| `XSigma_A(W_A)`, `.value`, `.delta`, `.delta2` | typed operator-window record and separate static/first-/second-difference fields |
| `R0_Sigma`, `IK_rel_Sigma` | explicitly identified R0 or IK_rel window-result kinds |
| `R0_w,C(q)` | separately named weighted n-adic R0 profile; not current primary IK_rel input without a compatible contract |
| `epsilon_move`, `epsilon_accel` | exact v3.50 names; v3.51 also requires epsilon kind, profile/version and consequence |
| `static_step`, `zero_accel_step` | first-/second-order joint-band flags; not trajectory measures or universal semantic stillness |
| `legacy_non_numeric_unspecified` | migration-only state when the older nonnumeric reason cannot be reconstructed |
| `derived_weight_denominator` | provenance for canonical-weight-derived fixed-M projections; not event-wise renormalization |
| `not_visible_to_evaluator` | operator-local reason that may map to `not_observable` while retaining its specificity |

### G.2 Retired-name register

| Retired locator family | Required current route |
| --- | --- |
| `IK_applicable(t)` | complete canonical IK or a named fixed-M reduced IK projection |
| `A_delta(t)` | complete directed movement or fixed-M movement with declared denominator |
| `A_pair_i(t)`, `m_pair(t)`, `min_components_R0` | complete canonical R0 or separately named fixed-M R0; result and gate state stay separate |
| `G_rel(t)`, `G_rel_active(t)`, `active(t)`, `IK_rel_axis(t)`, `min_components_rel` | typed component statuses, fixed `N`, name-bound weights and no runtime removal/renormalization |
| numeric-multiplier `G_K(t)`, event-wise `K_active(q)`, `S_active(q)` | typed K gate plus declared K/S component bases |
| `P_dup` | `P_disrupt` where that released S profile applies |

The retired formulas are not reproduced here. Reconstruction begins from the
archived or released source and checks every imported assumption against the
current v3.51 contract.

<a id="glossary-source-authority"></a>

## Appendix H — Authority and source index

Interpret sources in this order:

1. applicable versioned method/result contract;
2. cumulative v3.51 Root explanation and identity/guardrail contracts;
3. implementation companion for realization guidance;
4. asserted reference calculation/test as bounded evidence;
5. glossary explanation and navigation;
6. Future Work/open research as explicitly noncanonical possibility space.

Primary Root routes:

- [Conceptual Note v3.51](./Conceptual-Note_V351.md);
- [Architecture v3.51](./KSODI-Architecture_V351.md);
- [Implementation Guardrails v3.51](./IMPLEMENTATION_GUARDRAILS_V351.md);
- [Hangar v3.51](./KSODI-Hangar_V351.md);
- [Public Roadmap and open-research route](./ROADMAP.md).

Layer routes and exact locators are preserved in the linked public method,
result-contract, implementation-companion and reference-review files.

<a id="glossary-reconstruction-examples"></a>

## Appendix I — Public reconstruction and reference evidence

- [IK v3.51 reference review](./KSODI-Standard-Eval/Layer-3_KSODI-Monadic-Interaction-Coherence-IK_V350/IK_M2_V351_REFERENCE_REVIEW/README.md)
  preserves asserted calculations for scalar projections, fixed-reference
  geometry, trajectories and window order.
- [R0 v3.51 reference review](./KSODI-Full/Layer-4_KSODI-Relational-Gate-R_0_V350/R0_V351_REFERENCE_REVIEW/README.md)
  preserves numeric boundary and typed-status cases for the relational gate.
- [IK_rel v3.51 reference review](./KSODI-Full/Layer-5_KSODI-Dyadic-Relational-Coherence-IK_rel_V350/IK_REL_V351_REFERENCE_REVIEW/README.md)
  preserves component, gate-exclusion, status, profile and window cases.
- [Full Phase-H sensitivity review](./KSODI-Full/KSODI_FULL_V351_PHASE_H_SENSITIVITY_REVIEW/README.md)
  makes projection loss, metric/profile sensitivity and diagnostic boundaries
  inspectable across R0 and IK_rel.

These suites are public navigation and bounded reference evidence. They do not
create method authority, empirical validation or independent runtime-
conformance proof.
