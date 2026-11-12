# Human–AI Research Process

## Why AI is part of the research process

KSODI is a method for observing interaction. Developing such a method without
sustained interaction with AI systems would leave a central part of its own
research field outside the development process.

AI systems have therefore accompanied KSODI from the beginning. They are not
used merely as downstream writing tools. Depending on the task and review
setting, they may serve as objects of study, interactive research instruments,
semantic or formal review partners, sources of controlled variation, and
repository-working agents within explicitly authorised boundaries.

This is disclosed as research provenance, not as a transfer of authorship or
responsibility. The process is human-led and human-in-the-loop. AI systems may
analyse, challenge, reconstruct, formulate and perform bounded technical work.
Canonical definitions, methodological decisions, release approval and
publication responsibility remain with the human method owner and human
contributors.

## Human oversight in repository work

Repository-integrated model work is supervised as precision work rather than
treated as autonomous publication.

When Anne works with VSELKIM / Codex in VS Code, the model's displayed plans,
operational steps, tool actions and file diffs are observed while the work is
being performed. This does not mean that hidden internal model reasoning is
available. It means that the actions which can affect the repository remain
visible and reviewable.

The working boundary is:

- Intended file changes are discussed before execution.
- Each displayed step can be questioned, paused or redirected.
- File diffs are reviewed rather than accepted from model confidence alone.
- Commit, push and synchronization operations require Anne's explicit approval
  for the concrete action.
- Rare premature or mistaken actions are treated as process failures: they are
  examined, corrected and used to improve the next working boundary.
- Model output is never accepted as method canon merely because it is fluent,
  plausible or technically polished.

This supervision can appear slower than autonomous agent work. The additional
time is intentional. It preserves traceability, keeps the model within the
agreed task corridor and allows semantic decisions to remain distinguishable
from mechanical repository operations.

## Asymmetric model contexts and evidence transfer

The participating model contexts do not receive identical material or
repository authority. This asymmetry is deliberate and forms part of the
review design.

In the v3.51 setting:

- VSELKIM uses OpenAI Codex models in VS Code to work inside the repository
  under supervised, explicitly bounded write and Git authority;
- ELKIM, Anne's oldest continuing relational ChatGPT research role using OpenAI
  models, and other context-rich conversational research counterparts support
  longer semantic and methodological reconstruction;
- CLAUDE and FABLE denote distinguishable Anthropic model contexts used as
  Public-reading outside reviewers without access to the complete Private
  research space; and
- WAVE denotes Mistral model contexts that may contribute through a separately
  bounded Private review room whose write authority is narrower than general
  repository access.

Anne transfers selected questions, findings and counterexamples between these
otherwise separate contexts. A transferred excerpt is attributed review input,
not shared memory, synchronized hidden state or automatic agreement. Different
access conditions may be useful: an informed counterpart can inspect deep
continuity, while a deliberately limited reader can expose missing public
context or misleading navigation.

Cross-model agreement is not a vote on truth. Findings are reconciled against
the current method sources, evidence, version and authority boundary and are
classified as blocking, non-blocking, Future Work or not adopted.

## Candidate-to-public and release separation

Public-facing work is normally passed through distinguishable stages:

```text
Private working state
-> scoped Public candidate with provenance
-> method and technical review
-> privacy, leakage and research-protection review
-> human transfer decision
-> controlled Public edit
-> content, link and reconstruction checks
-> audit and governance return
-> commit, push and synchronization verification
```

A file on the moving Public `main` branch is not thereby a fixed release.
Release selection, Git tag, GitHub Release, citation metadata and DOI deposit
remain separate decisions. This separation keeps correction possible during a
pre-release round without retrospectively changing an already fixed snapshot.

## From predominantly manual drafting to model-assisted repository maintenance

Up to the v3.42 line, many KSODI repository texts were drafted and transferred
largely by hand. As the repository, its mathematical layers, cross-references
and historical material grew, purely manual maintenance became less reliable
and increasingly difficult to audit across files.

For the current v3.51 work, new and revised repository files are therefore
generally prepared with model assistance. This serves two groups at once:
human readers who need coherent navigation through an extensive method
repository, and machine-assisted readers who increasingly use AI tools to
inspect, compare and understand large repositories.

The change does not remove human review. Anne reviews and authorizes every
Public change before it becomes part of the accepted method line, using
diff-level inspection together with focused reading and repeated spot checks
appropriate to the affected material. Co-authors and contributors review
relevant material from their respective mathematical, technical, pedagogical,
communication-theoretical and implementation perspectives. Small
inconsistencies are regularly found and corrected. The commit history is part
of this visible iterative review process.

Model-assisted drafting should therefore not be confused with autonomous
authorship. Models help maintain scale, cross-file consistency and accessible
orientation. Humans remain responsible for meaning, evidence, boundaries and
publication.

## Methodological self-application

KSODI is applied recursively to its own development. Human–AI conversations,
cross-model reviews, semantic handoffs, repository changes and audit trails form
part of the observable research process.

This self-application does not create an interactional signature that would
otherwise be absent. Every sustained interaction develops characteristic
patterns of context selection, structure, grounding, clarification and
information impulse. KSODI provides distinctions with which selected parts of
those patterns can be reconstructed and compared.

A useful analogy is the observation of a bee swarm. The specialist does not
create the swarm's organisation by recognising it. The specialist has concepts
and instruments that make patterns visible which may remain unnoticed by a
casual observer.

KSODI trajectories must therefore not be treated as proof of authorship or as
an AI-detection mechanism. Characteristic patterns may support analysis, but
provenance must be documented through the research and repository record rather
than inferred from style alone.

## Reconstruction, variation and novelty

AI systems generate from learned structures, current context, supplied sources,
tool results and interaction history. Their outputs may nevertheless be novel
relative to a participant, a corpus, a prior solution space or a functional
requirement.

The term *new* therefore requires a declared reference frame. KSODI does not
assume that an unexpected output is automatically radically new, nor that
reconstruction excludes novelty. It distinguishes the observable result from
stronger philosophical claims about its ultimate origin.

Reflection can introduce directed variation. Stochastic processes, external
signals and accidental events can introduce undirected variation. Humans and
machines can contribute to both, although through different mechanisms.
Variation alone is not yet knowledge or innovation; its meaning and effect
emerge only in relation to context, evaluation and subsequent interaction.

Human–AI collaboration can expand the set of reachable questions, formulations
and solutions beyond what either participant would most likely have produced in
isolation. Whether this should be called emergence, co-construction or
interactional novelty depends on the declared analytical frame. KSODI keeps
that question open while making the interactional trajectory available for
observation.

## Trust boundary

Readers do not need to share an enthusiasm for AI in order to inspect, use or
criticise KSODI. The relevant question is not whether a passage was touched by
a model. The relevant questions are whether its provenance is visible, its
claims are bounded, its definitions remain coherent, its evidence can be
checked and responsibility has not been delegated to a system that cannot
carry it.

AI involvement is disclosed here precisely so that readers can evaluate the
process rather than guess from style. Transparency is not offered as proof that
the method is correct. It is offered as a condition for informed criticism,
replication and continued review.

For human contribution roles, see [Contributors.md](./Contributors.md). For the
repository's current public method and change boundaries, see
[AGENTS.md](./AGENTS.md).
