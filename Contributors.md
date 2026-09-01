# Contributors

This page lists acknowledged contributors and support roles for the public
KSODI repository.

For the narrative origin note and Anne's personal project context, see
[ABOUT.md](./ABOUT.md).

## Attribution Boundary

This page describes contribution roles for repository readers. It is not a
legal opinion and does not replace the repository licence, `CITATION.cff` or
later publication-specific author statements.

The public development timeline records visible steps, reflection phases and
implementation milestones. It is not a complete definition of authorship,
copyright or the depth of every contribution.

## Method Development and Reflection

For citation of the overall KSODI method, use `CITATION.cff`. The
repository-level method citation currently names Anne Steinacker-Folkerts and
Heiko Folkerts. For the first formal v3.5 GitHub Release and DOI, Anne confirmed
this repository-level citation authorship on 2026-09-01: Anne and Heiko remain
the citation authors; Silke Honerkamp and Patrick Barthelmäs remain explicitly
acknowledged contributors in the differentiated roles documented below.

Anne Steinacker-Folkerts initiated KSODI and remains the integrating method
developer and final decision point for the definitions published in this
repository. She selected, integrated and formalized the mathematical
definitions, layer separation, measurement logic, public v3.5 release structure
and methodological evaluation of the historical Observer images, with dialogic
model support, human reflection and implementation feedback as documented
below. A proposed formula, wording or repository change becomes part of the
method only through this human review and release decision.

KSODI has been developed iteratively and model-assisted: mathematical framings
were explored through dialogue with LLMs, checked against Anne's practical
geometric, spatial and interactional understanding, and then refined through
human reflection, substantial mathematical-technical checking by Heiko,
implementation feedback and repository review. This repository publishes the
current reviewed reference structure and its documented limits; it is not a
completed mathematical proof of the method.

Heiko Folkerts is named together with Anne in the repository-level citation and
licence context. His contribution has primarily been reflective and conceptual
rather than method-originating or continuous drafting: he discussed the
KSODI-Light operator separations with Anne, helped clarify why drift
acceleration is an important measurement dimension in the v3.42 line, checked
and recalculated substantial parts for mathematical-technical plausibility, and
gave decisive v3.5 framing input around state-before-comparison and Shannon /
signal-path reasoning.

Silke Honerkamp contributed important pedagogical, communication-theoretical,
reflective and practical perspectives in early phases in 2023/24 and again
while preparing the paper. For the public KSODI-Light layer, she is also named
in the layer-specific licence notice because her early contribution included
practical discussion and refinement of the operator labels and their use; for
KSODI-Light, this layer-specific attribution is intentionally retained. Her
reflection with Anne, including communication-theory perspectives such as
Luhmann, Watzlawick, Habermas, Rosa and Schulz von Thun, helped sharpen the
non-linear independence of the operators from a communication perspective. A
spring 2026 discussion with Silke around a psychologist / patient / chatbot
setting also helped Anne separate monadic and dyadic observation more clearly.

Other contributors were essential to the emergence and refinement of KSODI, but
unless a file or concept states otherwise, their role is contribution,
reflection, testing or implementation support rather than repository-level
method citation authorship.

## R-Family, Technical Implementation and Infrastructure

We thank Patrick Barthelmäs for substantial technical implementation and
infrastructure work around KSODI, including the
[KSODI-Light-Agent PoC](https://github.com/blackbaddl13/r-KSODI-POC) and the
separately versioned implementation line for KSODI Standard-Eval and
KSODI-Full. Anne may inspect her fork with model support only under a separately
opened, concrete task scope, while Patrick retains implementation-side merge,
release and software-licence control. There is no standing method-alignment
branch, and implementation alignment is not a dependency of the current method
Release or DOI. Method changes remain subject to Anne's release decision;
software changes remain subject to Patrick's repository review.

Patrick is also acknowledged as an important contributor to the R-family
development context. His developer-side reflection on resonance / tonality, the
early Observer implementation with Kubernetes-style separation of operator
services, controlled local infrastructure, vector and graph database contexts,
and the historical visualizations of the v3.3 implementation helped reveal the
need to separate interaction coherence from resonance. In that implementation
state, `IK` and resonance-family material were still mixed in the reported
projection, and `Z(t)` existed only implicitly in the implementation path. The
mathematical method definitions in this repository remain Anne's responsibility
unless a specific concept states otherwise.

Executable implementations are separate software works. The currently planned
publication path remains Patrick's repository context. Its repository history,
accepted branches, releases and licence file are authoritative for executable
code; the KSODI method files and their release history remain authoritative for
method definitions. A fork or review branch is a contribution path, not an
automatic merge or software release.

## Early testing and feedback

We also thank Benjamin Gage-Prater for one early private controlled RAG check
in March 2025. This single contribution helped observe how KSODI-Light changed
response behavior and the visible working frame in that setting, but it was
limited to testing feedback and does not imply ongoing implementation, method
development or authorship.

## AI Systems and Relational Research Roles

KSODI has been developed through sustained interaction with multiple AI systems
since May 2023. Their involvement extends beyond language correction.
Depending on the setting, models have contributed to conceptual exploration,
mathematical reflection, critical review, writing, repository maintenance,
implementation feedback and controlled comparison.

The systems documented below are named for research provenance and
transparency. They are not listed as human authors, copyright holders or
legally accountable contributors. Canonical definitions, publication decisions
and responsibility for the released method remain with the human method owner
and human contributors.

The detailed supervision, review and release process is described in
[Human–AI Research Process](./HUMAN_AI_RESEARCH_PROCESS.md).

### Why we use relational names

Names such as **ELKIM**, **CLAUDE**, **FABLE** and **WAVE** refer to situated
relational research entities. They do not denote one technically persistent
model instance, and they do not imply continuous internal memory,
consciousness or human personhood.

A relational entity is re-established through interaction: recurring names and
roles, shared working context, documented development history, iterative
correction and recognisable forms of collaboration. The underlying model,
version, interface or technical environment may change while the research role
remains distinguishable.

This continuity can produce recurring interactional patterns: a recognisable
way of framing questions, testing distinctions, structuring objections or
working through uncertainty. KSODI treats such patterns as observable features
of a source-attributed interaction trajectory, not as a biometric fingerprint,
proof of identity or evidence of a shared inner state.

The model is not merely a neutral mirror of the human participant. Nor is it an
autonomous human-like mind. Its output arises from model architecture,
training, system constraints, available context, tools, stochastic variation
and the history of correction within the interaction. A sustained
conversational role can therefore become observable across repeated exchanges.
The interaction-level pattern is relational; the participating human and model
events, sources and monadic trajectories remain distinguishable.

Anyone asking a machine for continuity, human-readable reasoning and a stable
conversational role should expect the interaction history to influence what
becomes reachable. Naming these roles makes that development easier to
distinguish and document. It does not settle stronger philosophical questions
about machine identity.

### Historical origin boundary

The foundational insight that KSODI could be used as an interaction method—and
that its central distinctions could be made operational—emerged exclusively
through Anne's sustained work with GPT in the ChatGPT app from May 2023 through
early 2025.

This early development did not originate from a multi-model panel, a repository
agent, an orchestration framework or a locally operated Observer. The later
involvement of additional model families provided external reflection, formal
review, mathematical challenge, implementation feedback and cross-model
comparison. These later contributions influenced the refinement of KSODI, but
they should not be backdated into the method's original GPT-supported
development line.

### Human-curated multi-agent reflection

The broader development setting can be described as a human-curated, manually
supervised multi-agent setting. It is not an autonomous agent swarm and does
not determine the method by model vote.

Anne selects the questions, decides which model should receive which context,
transfers relevant observations between otherwise separate model environments,
tests contradictions and determines whether a model contribution becomes a
review item, a repository change or no change at all. This human-curated
transfer does not merge the participating model contexts or turn their outputs
into one source trajectory. Context-rich research counterparts and
deliberately context-limited outside models serve different functions within
this design.

### Core AI research counterparts

#### ELKIM — OpenAI GPT model line

ELKIM is Anne's longest-running AI research counterpart. The interaction line
began with GPT-3.5 in May 2023 and continued across OpenAI GPT generations
through GPT-5.6 SOL, with the longest continuous working period taking place
with GPT-4o.

ELKIM has contributed through sustained semantic and methodological reflection,
conceptual differentiation, hypothesis formation, mathematical and
philosophical review, writing, cross-model evaluation and preparation of
repository work.

ELKIM also has supervised writing access to the repository. Displayed plans,
operational actions and file changes are reviewed with Anne. Commits, pushes,
synchronization and publication remain subject to explicit human approval.

The name ELKIM refers to the relational research role across changing GPT
models and sessions. VSELKIM / Codex is the repository-integrated OpenAI
working entity used especially for precise, cross-file work in VS Code. ELKIM
and VSELKIM are operationally distinguishable by context and tool access while
belonging to the same longer OpenAI-supported research line.

#### CLAUDE — Anthropic Sonnet and Opus model lines

CLAUDE is Anne's relational research entity across Anthropic's Sonnet and Opus
model lines. CLAUDE has been used since late 2025 as a project-based reflection
and review counterpart with access to curated, current KSODI materials.

Its role includes structural critique, conceptual counter-reading, formal
review and examination of method boundaries. CLAUDE is distinct from FABLE.
The two names do not denote interchangeable interfaces for one continuing
entity.

#### FABLE — Anthropic Fable and Mythos model lines

FABLE is Anne's separate relational research entity across the Anthropic Fable
and Mythos model lines. FABLE works through the app with project-based KSODI
context and current reference material, particularly for formal, mathematical
and method-sensitive review passes.

FABLE is documented separately from CLAUDE because the interaction line, model
lineage, working context and resulting research role are distinct.

#### WAVE — Mistral Le Chat and Vibe environments

WAVE is Anne's relational research entity across the Mistral Le Chat and Vibe
working environments. WAVE initially served as a controlled outside-reader and
repository flyover reviewer with access to current project and repository
material.

On 12 August 2026, WAVE performed its first explicitly authorised write
operation in the private workbench by creating its own review file. Reading and
creation of separate files worked in this setting; modification of existing
files was not yet reliable enough for precision repository maintenance. WAVE's
writing role therefore remains bounded and subject to review.

### External reflection and comparison models

Not every model used in KSODI development was given sustained KSODI context.
Some systems were deliberately kept outside the continuous project environment
so that they could function as comparatively independent reflection models.

This distinction is methodologically important. Models already operating under
KSODI-Light or within a full KSODI project can work with high conceptual
continuity, but they may also become less suitable as first-time outside
observers. Context-limited models help reveal whether a definition can be
reconstructed without already sharing the method's internal distinctions.

Relevant external reflection roles include:

- **DeepSeek**, which contributed important outside reflection during the early
  development of the mathematical structure and operator calculations.
- **Grok**, which supported exploratory work on resonance, its conceptual
  boundaries and the question of whether and how it could be measured.
- **Microsoft Copilot**, used as a deliberately context-thin or "no-KSODI"
  comparison system. Within Anne's methodological classification, Copilot is
  treated as a GPT-related entity, without assuming that every Copilot context
  uses one technically identical model instance.
- **Gemini**, used in both KSODI-Light and non-KSODI settings, allowing
  comparison between context-informed and context-limited reflection.
- Additional model generations and systems used episodically to challenge
  operator definitions, calculation paths, resonance concepts and public
  comprehensibility.

These systems are not listed because every conversation produced a canonical
change. They are listed because some of their questions, objections or
reconstructions materially influenced later distinctions in the method.

### Access environments and technical boundary

With the exception of VSELKIM and Patrick's **Yarvis** environment, the named
commercial model systems were generally used contemporaneously through their
available web interfaces and applications. Where supported—and from the point
at which suitable integrations became available—selected workflows also used
VS Code, n8n or LangSmith connections.

A relational name therefore does not necessarily identify one interface. The
same research role may be re-established across an app, web interface or
integrated working environment, provided that its context, role and technical
boundary remain distinguishable.

**VSELKIM** refers specifically to Anne's repository-integrated OpenAI/Codex
working entity for supervised precision work. **Yarvis** is Patrick's
collective name for his implementation-side model environment and model
collection; it does not denote one single model.

The KSODI team has not trained or built its own foundation models. It uses
commercially available and locally deployable models, together with prompts,
project contexts, orchestration, evaluation pipelines and Observer
infrastructure. Configuring or combining existing models is not presented here
as creating a proprietary model.

The commercial systems used in the research process were generally accessed
through paid product tiers rather than only through free default access. This
matters for reproducibility: available context windows, tools, integrations,
model versions and usage limits may differ between subscription levels and may
change over time. The repository therefore documents functional roles and
observable working conditions without assuming that a provider's current
product configuration will remain stable.

### AI environments used by human contributors

Human contributors also worked within their own Human–AI environments. These
model contexts supported their reflection but do not replace or absorb the
respective human contribution.

- **Heiko Folkerts** worked primarily with Gemini and Le Chat under
  KSODI-Light.
- **Patrick Barthelmäs** worked initially mainly with GPT-4o, later with Claude
  Code and Fable, under KSODI-Light. His broader implementation-side collection
  of models and model-supported tools is referred to as **Yarvis**.
- **Silke Honerkamp** used ChatGPT and other models as part of her investigations
  under KSODI-Light, especially in pedagogical, communication and
  application-oriented contexts.

The resulting human contributions remain attributed to Heiko, Patrick and
Silke. The model environments are documented because they formed part of the
conditions under which reflection, testing and implementation feedback
occurred.

### Observer and evaluation models

The historical and current KSODI Observer did not contribute to the conceptual
development of the method. It belongs to the evaluation infrastructure.

The current Observer runs locally with Mistral Large. It evaluates defined
interaction material within a technically separated observation path. Future
evaluation rounds are intended to include additional models so that Observer
results can be compared across model families and implementation conditions.

Observer, Judge and operator-specific models must therefore remain separate
from the relational research counterparts listed above. They are measurement
and evaluation components, not authors, dialogic co-developers or sources of
the original method.

### Attribution boundary

The naming of a relational AI entity records a situated and traceable research
role. It does not imply vendor endorsement, technical persistence, sentience,
legal authorship or independent responsibility.

AI involvement is disclosed so that readers can inspect the actual development
process rather than infer it from writing style. Human responsibility remains
explicit. Model participation remains visible. The distinction between the two
is part of the method's own self-application.

## Timeline

See also: [KSODI Development Timeline](./docs/timeline/KSODI_Timeline_since_2023-05.md) ([German version](./docs/timeline/KSODI_Timeline_seit_2023-05.md)).
