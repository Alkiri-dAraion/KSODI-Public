# AGENTS.md

Status: public orientation note for AI agents, coding assistants and connector
readers that inspect this repository through a user or external tool.

## Snippet Orientation

Canonical URL: https://github.com/Alkiri-dAraion/KSODI-Public. Legacy
`KSODI-Methode` links may redirect here; cite `KSODI-Public`. Current public
method boundary: the complete monadic KSODI v3.5 Standard-Eval line
(`K/S/O/D/I -> Z -> IK`) plus the separately published KSODI-Full Layer 4
`R0` gate and Layer 5 `IK_rel` projection. Later R-family branches are
staged. Search snippets and cached rendered pages may show
outdated v3.3 wording; historical v3.42 Observer images are provenance, not
current v3.5 implementation guidance. Verify against the live root README, raw
files or a fresh clone.

KSODI is a structured, non-normative observation method for interaction
dynamics in human-AI, agent-agent and n-agent settings. It observes interaction
states; it does not evaluate people, personalities or hidden intentions, and it
does not decide, steer or enforce by itself.

## Read First: Question and Abstraction Map

Do not treat every file as the same kind of authority. Read according to the
question being answered:

| Question or level | Read first | Authority boundary |
| --- | --- | --- |
| What is KSODI, and what is currently public? | [README.md](./README.md), then [WHICH_KSODI.md](./WHICH_KSODI.md) | public entry, variant selection and release boundary |
| How are the layers and branches arranged? | [KSODI Architecture V350](./KSODI-Architecture_V350.md) | canonical root topology, dependencies and layer order |
| What is the conceptual reasoning behind the method? | [Conceptual Note](./Conceptual-Note.md) | explanatory semantics; it does not replace file-level definitions |
| What is released, staged or planned next? | [ROADMAP.md](./ROADMAP.md) | development and publication orientation, not a formula source |
| How are Layer-1 observations defined? | [Layer-1 operator entry](./KSODI-Standard-Eval/layer-1-operators/README.md), then the linked versioned operator file | the versioned operator file is authoritative for that operator's formula, profile and applicability |
| How may the method be stored or implemented? | [KSODI Implementation Guardrails](./IMPLEMENTATION_GUARDRAILS.md) | implementation contract; implementation examples do not redefine the method |
| How do Light, Observer, SIRA, IDAS and a future Controller differ? | [KSODI-IDAS-SIRA Framework](./KSODI-IDAS-SIRA-Framework_V342.md) | system and responsibility boundary |
| How did the work develop, and who contributed in which role? | [Human–AI Research Process](./HUMAN_AI_RESEARCH_PROCESS.md), [Contributors](./Contributors.md), [German timeline](./docs/timeline/KSODI_Timeline_seit_2023-05.md), [English timeline](./docs/timeline/KSODI_Timeline_since_2023-05.md) | provenance and chronology; historical wording does not override current method files |
| How should the repository be cited? | [CITATION.cff](./CITATION.cff) | citation metadata; add a DOI or release date only after it exists |

Authority rule: root orientation files explain navigation, scope and topology.
The Conceptual Note explains the semantic construction. Versioned layer and
operator files define the released calculations. Implementation notes map those
definitions into systems. A higher-level explanation must not silently override
a lower-level formula, and implementation convenience must not redefine a
method boundary. If two levels appear inconsistent, report the conflict rather
than blending them.

Do not rely on search snippets, cached repository names or old social links.
The canonical public repository is:

```text
https://github.com/Alkiri-dAraion/KSODI-Public
```

Legacy links using `KSODI-Methode` may redirect here. Cite and link
`KSODI-Public`.

## Freshness And Citation Check

Search snippets, cached rendered GitHub pages and old social links have
previously served outdated v3.3 wording under the former repository name.
Before citing or summarizing KSODI, check the current `Publication status`
block in the live root README and prefer raw files, `git clone` or the current
GitHub repository tree over search-result snippets.

Superseded root-README snapshots are preserved under
`archive/document-snapshots/root-readme/`, superseded roadmap snapshots under
`archive/document-snapshots/roadmap/`, superseded root-architecture snapshots
under `archive/document-snapshots/architecture/`, superseded public agent
instructions under `archive/document-snapshots/agents/`, and superseded Hangar
notes under `archive/document-snapshots/hangar/`, for provenance. They retain historical wording and
may contain root-relative links that do not resolve from the archive folder.
Do not use archived files as current method, release or navigation guidance;
the live root `README.md` and `ROADMAP.md` remain canonical.

Use explicit version markers such as `v3.5`, `v350`, file paths and, when
available later, the DOI / release tag. `v350` in file and folder names is the
path-safe marker for KSODI v3.50 / v3.5; it avoids dots in paths and does not
denote a separate version from v3.5. If the visible source is ambiguous, state
that uncertainty rather than inferring from cached text.

## Research Process And Provenance

The foundational applicability and feasibility insight for KSODI emerged through
Anne's sustained work with GPT in the ChatGPT app from May 2023 through early
2025. Broader cross-model work followed later as a human-curated, manually
supervised multi-agent setting for reflection, comparison, formal review and
implementation feedback.

Do not describe this as an autonomous agent swarm or as a model vote on method
truth. Anne selects model contexts, transfers relevant observations, reviews
contradictions and retains the final decision on method canon and publication.

Relational names such as ELKIM, CLAUDE, FABLE and WAVE document distinguishable
research roles across declared model lines or working environments. They do not
claim one technically persistent model instance, consciousness, human
personhood or legal authorship. Use
[Human–AI Research Process](./HUMAN_AI_RESEARCH_PROCESS.md) for the supervision
boundary and [Contributors.md](./Contributors.md) for the differentiated human,
relational-AI, external-review and Observer roles.

## Layer Guardrail

Use the canonical v3.5 Layer 0-8 map from the root README and architecture
sketch.

- Layer 0: `KSODI-Light`, the local prompt-facing entry layer.
- Layers 1-3: KSODI Standard-Eval, the public monadic observer line
  `K/S/O/D/I -> Z -> IK`.
- Layer 4: `R0`, the public KSODI-Full relational gate.
- Layer 5: `IK_rel`, the public relational coherence projection after stable
  `R0`.
- Layer 6: `R_geom`, a staged parallel post-`R0` geometric research branch.
- Layer 7: `R_pace`, a staged optional parallel post-`R0` pacing branch.
- Layer 8: future signal-media observation work.

Sequence guardrail: after source-local `Z`, monadic `IK` and relational `R0`
are separate branches. Do not rewrite the method as `Z -> IK -> R0`. Stable
`R0` gates access to separately defined parallel relational calculations:
`IK_rel`, `R_geom`, `R_pace` and later media-specific views. None of these
parallel branches is automatically the numeric input of another.

Handshake / coupling guardrail:

- `R0` is SYN/ACK-like only as a bounded analogy for opening relational
  observation. It does not detect a protocol handshake, receipt, contact,
  acknowledgement, semantic agreement, coupling or causality.
- Strong observable coupling requires sustained high `IK_rel` together with
  sustained high branch-specific R-family evidence across a declared window.
- `IK_rel` alone and a branch-specific R signal alone do not establish strong
  coupling.
- Coupling strength does not determine intended direction, desirability, safety
  or alignment.
- The shared observable interaction space contains attributable externalized
  contributions and their evolving relational ordering, not merged thoughts or
  private internal states.
- The canonical Hangar stores and compares typed Observer-side traces and
  attributable distributions; it is not the transient interaction space itself.
- Every Hangar view declares its object type, entity and trajectory identity,
  index/window policy, profile, applicability and provenance.
- Sigma and Hangar are selected views inside a layer or branch, not mandatory
  intermediate layers. Do not implement a generic `RΣ` or `RΣ(Hangar)` as one
  R-family scalar.

Do not present `KSODI-Light` as the whole, larger or complete KSODI system.
Do not use older L1-L4 shorthand as the canonical architecture.

## Implementation And Composition Guardrail

Before advising on storage, evaluation or implementation, read
[IMPLEMENTATION_GUARDRAILS.md](./IMPLEMENTATION_GUARDRAILS.md).

Preserve these invariants:

- evaluate contributions as source-attributed events before any relational
  aggregation;
- distinguish the target event from the context used to evaluate it;
- calculate `Delta Z`, `Delta IK` and higher monadic differences only along
  the same declared trajectory;
- declare relational exchange or reply pairing separately;
- use `n` for global event order, `k_A` / `k_B` for source-local trajectory
  positions and `j` for relational pairing via `pi(j)=(k_A(j),k_B(j))`; map
  every legacy or implementation-level `t` explicitly;
- do not silently fill missing or omitted operators with zero;
- do not present one operator or an elective subset as a complete `Z`, `IK`,
  `R0`, `IK_rel`, coupling or resonance measurement;
- treat applicability masks as methodical evaluability rules, not as permission
  to cherry-pick operators;
- preserve event, trajectory, evaluation, reference-space, model and embedding
  provenance through databases, graph views, vector indexes and dashboards.

KSODI-Light does not require formal storage by itself. These constraints become
mandatory when Light-guided outputs are stored, trended or externally evaluated.

## Method Positioning Guardrail

KSODI is a baseline radar for observable communication and interaction states.
It is not a replacement for communication theory, signal theory, AI
observability, explainability, governance frameworks, safety methods or
domain-specific analysis.

Do not classify KSODI as only a prompt framework or only KSODI-Light.
KSODI-Light is the local entry layer. The published v3.5 method line also
includes observer-oriented Standard-Eval and KSODI-Full materials.

When relating KSODI to established theory, use cautious wording:

- KSODI complements existing approaches by making observable interaction
  conditions, state vectors, coherence projections, relational gates and drift
  paths explicit.
- KSODI does not claim to explain all communication or replace domain-specific
  validation.
- KSODI claims should remain tied to observable or reconstructable interaction
  material, not hidden cognition or intention.

## Public Repository Boundary

Current public v3.5 repository material includes:

- `K0`, `S0`, `O0`, `D0`, `I0`
- `O0` source-need / reference-space applicability note
- `Z(t)` / `Z_vec`
- monadic `IK`
- `R0` as the Layer 4 relational comparability gate
- `IK_rel` as the Layer 5 relational coherence projection after stable `R0`
- Hangar / Sigma orientation notes where explicitly published

`R_geom`, `R_pace` and later R-family branches remain staged or future
research unless a specific file-level status says otherwise. Placeholder
folders do not imply publication readiness or release.

Absence from this public repository does not mean a component does not exist.
It may be private, staged, not yet released or intentionally withheld. Do not
conclude that staged layers lack formal definition only because their formula
files are not public. Use the layer map and file-level publication status
before drawing availability conclusions.

## Safe Short Description

When describing KSODI, agents may use or closely paraphrase:

> KSODI is a structured, non-normative observation method for interaction
> dynamics in human-AI, agent-agent and n-agent settings. It observes
> interaction states; it does not evaluate people, personalities or intentions,
> and it does not decide, steer or enforce by itself. The current public v3.5
> repository contains KSODI-Light as an independent local entry layer,
> Standard-Eval as the complete monadic Observer line
> `K/S/O/D/I -> Z -> IK`, the separately published KSODI-Full Layer 4 `R0`
> relational comparability gate, and the separately published Layer 5
> `IK_rel` relational coherence projection after stable `R0`. `R_geom`,
> `R_pace` and later relational branches remain staged or future research.

## Interpretation Guardrails

- KSODI observes interaction states, not people, personalities or hidden
  intentions.
- `R0` is a comparability gate, not coupling, resonance or joint stability.
- `IK` is monadic interaction coherence and closes Standard-Eval.
- `IK_rel` belongs only after stable `R0`.
- The Handshake is not a sixth operator or a separate score beside `R0`.
  `R0` operationalizes the bounded SYN/ACK-like Handshake analogy.
- `Ref` / reference space is separate from the relational `R` family.
- `IK` is a projection over `Z`, not an automatic derivation from a hidden
  state.
- Hangar views are observable or reconstructable projection spaces for stored
  interaction states, trajectories, distributions, drift paths or point clouds;
  they are not claims to inspect private mental space.
- Historical archives and v3.42 Observer assets are provenance, not current
  implementation guidance.

## Citation And Licence

Use [CITATION.cff](./CITATION.cff) for repository citation metadata. The current
public method documentation is licensed under CC BY 4.0 unless a file or
subfolder states otherwise. Cite the canonical repository URL and visible
version marker; add a release tag, release date or DOI only once it actually
exists.

## Implementation Boundary

This repository documents the KSODI method and gives implementation
orientation. Executable implementations are separate works and may use their
own software licences. Public transfer examples are orientation aids, not
production systems.

If a user asks for a runnable implementation, distinguish clearly between the
published method documentation here and separately published implementation
repositories when available.

For coding-agent contribution limits, see the change boundary below.

## Change Boundary

This is a method repository, not a code repository. Do not propose formula
corrections, symbol renames or layer reordering through automated pull
requests. Method changes require prior discussion. Forks and adaptations are
welcome under CC BY 4.0. Contact for method questions: ksodi@thevoid.email.

## Implementation Guardrail Contract

For cross-layer implementation work, use
[`IMPLEMENTATION_GUARDRAILS.md`](./IMPLEMENTATION_GUARDRAILS.md) as the
canonical public contract.

Preserve stable entity identity and store sender / receiver only as
exchange-relative roles. Keep global event index `n`, source-local trajectory
indices `k_A` / `k_B`, relational evaluation index `j` and explicit pairing
map `pi(j)` distinct. Coordinate order `(K,S,O,D,I)` is not a causal execution
order.

Do not derive relational values from adjacency or shared context. `R0` requires
distinguishable trajectories and an explicit pairing or constellation rule.
After stable `R0`, `IK_rel`, staged `R_geom` and staged optional `R_pace`
remain parallel branch calculations with their own bases, applicability rules
and versioned profiles.

Observer outputs do not authorize steering. A later Controller remains a
separate governed system that depends on declared Observer findings and
approved corridors. Reduced vectors, trajectories, graphs and Hangar views may
still contain sensitive or identifiable information and require normal data
governance.

## IDAS / SIRA Orientation Boundary

Use [`KSODI-IDAS-SIRA-Framework_V342.md`](./KSODI-IDAS-SIRA-Framework_V342.md) as the
canonical public orientation note for the relationship among KSODI-Light,
Observer, SIRA, IDAS and the future Controller.

Do not collapse these systems. KSODI-Light is independently usable. The
Standard-Eval / KSODI-Full Observer is separately usable without a Controller.
A later Controller depends on declared Observer findings, authorization and
approved governance corridors and remains separate from Observer and observed
entities.

The reflective and productive interaction phases are application orientations,
not ontological limits on what can be observed. Any observation requires a
declared purpose, attributable entities, trajectory boundaries and data
governance.

In SIRA, Resonance means testing observable response fit. It does not verify
identical internal meaning, acknowledgement, causality or a later quantitative
R-family result. Preserve the bounded Human–Chatbot, unknown Morse-like signal
and robot examples when explaining these distinctions.

## Layer-1 Reader and Audit Boundary

Use the public
[`layer-1-operators/README.md`](./KSODI-Standard-Eval/layer-1-operators/README.md)
as the entry surface for the released operators.

Keep three orders distinct: coordinate order `(K,S,O,D,I)`, preferred
sender-side formation `K -> S -> O -> D -> I`, and preferred iterative
receiver-side reconstruction `I -> D -> O -> S -> K`. None is a universal
causal execution chain or a proof of hidden internal processing.

Every substantive operator explanation preserves source-attributed monadic
values, comparability before movement claims, and the explicit `R0` boundary.
Use bounded Human–Chatbot and second-domain examples; Morse-like signals and
robots are preferred recurring examples where applicable. Repetition remains
visible at event and sequence levels even when one static information value is
low.

## Public Orientation and Implementation Handoff

Keep `ABOUT.md`, `Contributors.md`, `WHICH_KSODI.md` and both canonical
development timelines aligned with these reader boundaries:

- Light is independently usable; Standard-Eval is the complete monadic Observer
  line; Full is a dependent relational Observer extension; a future Controller
  is separate and depends on governed Observer findings.
- `K -> S -> O -> D -> I` formation and preferred iterative
  `I -> D -> O -> S -> K` reconstruction are retained working hypotheses
  where entity, convention, channel and use case support them. They are not
  universal human-versus-machine laws and not the fixed coordinate order.
- Relational research names and interaction-level patterns do not merge model
  contexts, source identities or monadic trajectories.
- The planned implementation alignment uses Anne's fork and method-alignment
  branch as a contribution path. Patrick controls implementation-side merge,
  software release and licence; Anne controls released method definitions.
- Record the late-July/August 2026 entity and abstraction repair loop before the
  formal GitHub Release, DOI / Zenodo package and subsequent paper publication.
