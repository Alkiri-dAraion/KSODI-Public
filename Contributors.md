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
Heiko Folkerts.

Anne Steinacker-Folkerts initiated KSODI and remains the integrating method
developer and final decision point for the definitions published in this
repository. The mathematical definitions, layer separation, measurement logic,
public v3.5 release structure and evaluation of the historical Observer images
for methodological consistency were integrated and formalized by Anne, with
dialogic model support and human reflection as documented below.

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
[KSODI-Light-Agent PoC](https://github.com/blackbaddl13/r-KSODI-POC) and later
work toward the first full implementation of KSODI-Standard Eval & KSODI Full
in a separately versioned implementation line.

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

Executable implementations are separate software works. Published
implementations are expected to live in Patrick's repository context and to use
their own software licence, normally MIT where so stated by the implementation
repository.

## Early testing and feedback

We also thank Benjamin Gage-Prater for one early private controlled RAG check
in March 2025. This single contribution helped observe how KSODI-Light changed
response behavior and the visible working frame in that setting, but it was
limited to testing feedback and does not imply ongoing implementation, method
development or authorship.

## Timeline

See also: [KSODI Development Timeline](./docs/timeline/KSODI_Timeline_since_2023-05.md) ([German version](./docs/timeline/KSODI_Timeline_seit_2023-05.md)).
