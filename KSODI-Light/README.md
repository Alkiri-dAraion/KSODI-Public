[cc-by-badge]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
[cc-by]: http://creativecommons.org/licenses/by/4.0/


[![CC BY 4.0][cc-by-badge]][cc-by]
<br>
The published method documentation and method materials in this repository are licensed under a [Creative Commons Attribution 4.0 International License][cc-by], unless a file or subfolder in this repository explicitly states otherwise. Separately published software implementations are distinct works with their own repository licences.


## CC-License

This work, *KSODI – Method for Structuring and Optimising Human-AI Interactions* © 2024 by<br>
Anne Steinacker-Folkerts, Heiko Folkerts, and Silke Honerkamp is licensed under CC BY 4.0.<br>
To view a copy of this licence, visit [![CC BY 4.0][cc-by-shield]][cc-by].
The complete KSODI-Light licence text is available in
[LICENSE.md](./LICENSE.md); the transition history is documented in the
[KSODI licence transition note](../KSODI-License-Transition-Note_V342-to-V350.md).


## Acknowledgements

Special thanks to Benjamin Gage-Prater for early RAG testing and feedback, and to Patrick Barthelmäs for platform and integration support, including the [KSODI-Light-Agent PoC (GitHub)](https://github.com/blackbaddl13/r-KSODI-POC).

[cc-by-image]: ../assets/ksodi-lab-banner.png


# KSODI-Light

## Current Scope — released v3.5 and v3.51 publication candidate

KSODI v3.5 is being published to this repository in successive stages. The
current public KSODI-Standard-Eval release contains all five Layer-1 operator
definitions, the Layer-2 monadic state vector `Z_A(k)` and the Layer-3 monadic
interaction-coherence projection `IK_A(k)`.

KSODI-Standard-Eval is the complete monadic line
`K/S/O/D/I -> Z_A(k) -> IK_A(k)` and ends with `IK_A(k)`. KSODI-Full begins
with dyadic or explicitly n-adic observation at the public Layer 4 gate `R_0`;
current dyadic Layer 5 `IK_rel` requires explicit pairing and an open numeric
canonical complete dyadic `R_0` under the exact required profile. Both belong
to KSODI-Full, not KSODI-Standard-Eval. The Layer 6–8 R-family and signal-media
extensions remain staged or future research and are outside the current public
method scope.

The v3.51 publication candidate retains that layer boundary while refining the
monadic result surface: complete typed `Z` remains available alongside the
distinguishable `IK_w`, `IK_M2`, `IK_ref` and `AxisDev_ref` views in the
non-total-score IK-Gesamtbild. Candidate files may appear on Public `main`
during the layerwise review; this does not change the fixed v3.5.0 release or
constitute a tagged v3.51 release before separate authorization.

Earlier v3.3 and v3.42 materials are retained in clearly marked historical
archives. They are not current implementation guidance.

KSODI-Light is the human-facing entry to communication understanding and to
the KSODI method. It provides accessible reflective questions without
collapsing communication into formal scores or requiring the later Observer
architecture.

It can be used as a **reflective working agreement** between user and
assistant. In that sense, KSODI-Light does not only reflect the user's prompt.
It can also reflect assistant output, feedback from the user and the visible
shared working frame across a turn. This does not create a merged interaction
state.

## Copy-and-Paste Agent Skills

Readers looking for a prompt they can use directly should begin with the
[KSODI-Light Agent Skills and Copy-and-Paste Prompts](./agent-guidance/README.md).
The hub offers purpose-specific v3.51 candidates for general assistants,
coding and repository collaboration, reflective research/method review, and
education or communication contexts.

These files are portable prompt templates, not guaranteed vendor-specific
executable skill packages. They use placeholders for roles and scope; no
personification is required. KSODI-Light remains one entry point in the wider
method and does not replace the Standard-Eval or Full Observer layers.

## Reflective, Dyadic and Local Self-Adjustment Boundary

KSODI-Light is a reflective, dyadically situated local-guidance layer for
human-AI, agent-agent or other distinguishable interaction sides.

It can support lightweight internal steering. For example, a participant may
be instructed to name an operator, ask for clarification or adjust its own
contribution when a declared context-specific threshold is not reached.

When both interaction sides know and use the KSODI-Light frame, each side may
reflect on and adjust its own contribution. This creates reciprocal,
dyadically situated local self-adjustment within a shared working agreement.

When KSODI-Light is implemented only on the agent side, the steering remains
local and asymmetric. The interaction is still dyadic, but the reflective
method is not necessarily shared by both participants. Whether this improves
task handling or reconstructibility must be observed empirically and must not
be assumed from prompt compliance alone.

KSODI-Light does not rank or evaluate persons. Its thresholds are
context-specific orientation, clarification or fallback points, not universal
quality standards.

Dyadic use at the Light level does not mean formal dyadic measurement.
KSODI-Light does not calculate `R_0`, `IK_rel` or R-family components. Formal
monadic trajectory observation, complete typed `Z` and the applicable IK result
surface belong to KSODI-Standard-Eval. Relational observation begins separately
in KSODI-Full at `R_0`; current dyadic `IK_rel` requires its exact open
canonical complete dyadic gate contract.

It supports:

- clearer prompt formulation
- explainability
- AI literacy development
- structured reflection on visible task fit and interaction conditions
- bidirectional feedback when a request, answer or shared working frame does
  not fit the task
- beginner-friendly collaboration with coding agents
- lightweight guidance when K/S/O/D/I expectations are embedded into user,
  account, developer or system prompts

KSODI-Light does not evaluate correctness and does not judge users.
It supports learning and clarity.

## Operator Labels in Light and Eval

KSODI-Light uses short, human-facing operator labels because this layer is a
reflective working agreement for people, trainers and local prompt guidance.
The short labels name practical working questions:

- Is there enough context?
- Is the request or response structured?
- Is it grounded or objectifiable enough for the task?
- Is it clear and distinguishable enough to continue?
- Does it add an information impulse?

In the formal Observer layers, these same questions are named more precisely as
observable reconstruction categories: **Observable Context Completeness**,
**Observable Structural Coherence**, **Observable Grounded Objectivity**,
**Observable Clarity** and **Observable Information Impulse**.

The names differ slightly because the layers ask the same questions from
different positions. Light supports local reflection inside an interaction.
KSODI-Standard-Eval and KSODI-Full observe exposed states, trajectories, reference spaces
and reconstruction conditions from outside the prompt.

For the observer-facing terminology and v3.5 boundary, see
[KSODI-Standard-Eval](../KSODI-Standard-Eval/README.md) and
[KSODI-Full](../KSODI-Full/README.md).

## Why This Layer Matters

KSODI-Light is the human-facing and prompt-level entry variant of the KSODI
method. The later observer architecture grew from the same practical question: how can humans and machines
notice missing context, weak structure, insufficient grounding, unclear wording
or low informational movement before an interaction becomes unusable?

For AI literacy and organizational training, KSODI-Light provides a shared
language for discussing prompts, answers, uncertainty and task fit without
requiring mathematical implementation.

For simple assistants, it may be enough to use KSODI-Light as a user/account
prompt or as developer-level guidance. In more complex settings, such as MoE,
multi-agent systems or embodied-agent interaction layers, KSODI-Light can
provide local orientation while KSODI-Standard-Eval or KSODI-Full observer layers
observe trajectories, drift and declared relational evidence from outside the
prompt. This does not make KSODI-Light a robotics controller or safety system. In human-facing
settings, its use should be disclosed at the applicable user, account,
developer, system or application level; it does not need to be named again in
every interaction.

## Relation to Observer-Supported Agentic Systems

KSODI-Light belongs to the local agent side of the architecture. It may appear as a user prompt, account prompt, developer prompt, system prompt, skill instruction or other disclosed guidance layer.

It can support local reflection, clarification, uncertainty visibility, corridor awareness and fallback behavior. In agentic systems, this local Light layer becomes especially useful when it is paired with a separate Observer layer.

That Observer layer is not part of KSODI-Light. It belongs to KSODI-Standard-Eval, KSODI-Full or IDAS/SIRA-level implementations and is responsible for formal observation of trajectories, drift, acceleration, retrieval behavior, vector movement, relational coherence and corridor exits.

KSODI-Light and the Observer can each be used independently. When combined,
Light provides local reflective guidance, while KSODI-Standard-Eval or
KSODI-Full provides external, auditable observation and reports findings. Any
feedback, intervention or action based on those findings requires a separately
declared human or Controller responsibility. An Observer may also evaluate
interactions whose participants do not use KSODI-Light.

## Agent Literacy and Prompt Guidance

KSODI-Light can also support beginners who work with coding agents.
The examples below show how users can define reflective collaboration modes
and lightweight agent prompts without publishing private personal instructions:

- User and account prompts:
  [General Assistant Agent Skill](./agent-guidance/KSODI-Light-Agent-Skill_General-Assistant_V351.md),
  [Education and Communication Agent Skill](./agent-guidance/KSODI-Light-Agent-Skill_Education-and-Communication_V351.md)
- Coding, repository and method work:
  [Coding and Repository Collaboration Agent Skill](./agent-guidance/KSODI-Light-Agent-Skill_Coding-and-Repository-Collaboration_V351.md)
  and [Reflective Research and Method Review Agent Skill](./agent-guidance/KSODI-Light-Agent-Skill_Reflective-Research-and-Method-Review_V351.md)
- Extended didactic guidance:
  [Coding Agent Guidance v3.51](./agent-guidance/KSODI-Light-Coding-Agent-Guidance-Extended-Example_V351.md)
  and [General Assistant Guidance v3.51](./agent-guidance/KSODI-Light-General-Assistant-Guidance-Extended-Example_V351.md)
- User feedback:
  [Prompt Feedback Example v3.51](./user-feedback/KSODI-Light-Prompt-Feedback-Example_V351.md)
- Developer and system-prompt notes:
  [KSODI-Light Agent Bridge v3.51](./developer-notes/KSODI-Light-Agent-Bridge_V351.md)
  and [Reflection, Local Self-Adjustment and Prompt-Level Steering
  v3.51](./developer-notes/KSODI-Light-Self-Alignment-vs-Steering_V351.md)
- Method orientation:
  [KSODI-Light Method Comparison and Combination Guide v3.51](./KSODI-Light-Method-Comparison_EN_V351.md)
  and the [KSODI English Translation Table v3.51](./KSODI-Light-English-Translation-Table_V351.md)

The guidance examples are not hidden system prompts. They are public,
copy-and-paste-ready orientation prompts for user accounts, training contexts
and simple assistant setups. More specialized variants, such as research,
education, creative writing or child-friendly prompts, can be added separately.

KSODI-Light may support reflective local self-adjustment patterns in assistants,
such as asking for clarification, keeping uncertainty visible and adapting
K/S/O/D/I expectations to the task context.

When embedded by a user, trainer, developer or agent creator, KSODI-Light can
also support lightweight steering. Examples include:

- asking for clarification if `K`, `S`, `O`, `D` or `I` is too low for the
  task,
- using different expectation corridors for different domains,
- defining fallback behavior such as "if objectivity is too low, ask before
  answering",
- keeping the assistant inside a reflective collaboration mode.

Users can also use the same grid to give feedback when an assistant answer does
not fit the shared frame, for example because it lost context, overclaimed,
answered the wrong task or moved too quickly.

These patterns remain prompt-level guidance. They are not the same as formal
KSODI-Standard-Eval or KSODI-Full monitoring.

## Optional Internal Completeness Estimates

KSODI-Light normally produces short natural-language feedback rather than a
visible score. An agent may use a rough internal `0..5` estimate for each
task-relevant K/S/O/D/I dimension to decide whether clarification would help:

- `0` means that the visible material is not yet usable for that part of the
  declared task;
- `5` means that the task-relevant elements appear sufficiently complete for
  the requested processing.

If a dimension appears incomplete, the useful response is not merely a number.
The agent should briefly explain what is missing, why it matters and one way to
improve the request, answer or visible working frame.

Numeric estimates are disclosed only when requested. They must be named as
approximate, task-specific estimates and shown per dimension. A single total
is not the preferred view because it can hide which dimension needs attention.
This didactic Light scale is not a rescaling of formal Observer coordinates in
`[0,1]`, not a formal Layer-1 operator result and not a judgement of a person,
truth, intelligence or general quality.

Different tasks may need different corridors:

- creative or science-fiction discussion may allow lower objectivity while
  still requiring clear context and structure,
- documentation of an image may require high grounding/objectifiability and
  clarity/discernibility,
- legal, medical, safety or governance contexts may require much stricter
  grounding and source boundaries.

If numeric estimates are requested, their task scope, ascending polarity and
approximate status must be disclosed and explained. Hidden or automated
score-based intervention does not belong to the Observer alone. It requires a
separately governed human or Controller action boundary and is not part of this
public KSODI-Light example set.

Repeated prompt use may affect later visible interaction only under additional
conditions: the instruction remains available or is reintroduced, the platform
loads it, its meaning remains sufficiently stable and higher-priority rules or
context limits do not displace it. **Prompt presence does not prove persistent
learning, memory, internal-state change or a causal long-term effect.**

## Observer Boundary

An external observer can add an auditable layer around an agent. It can monitor
drift, compare trajectories over time, report corridor exits and support human
oversight.

That observer layer belongs to KSODI-Standard-Eval, KSODI-Full or IDAS/SIRA-level
implementations.

KSODI-Light may guide an assistant from inside the prompt. Observer-based
monitoring evaluates behavior from outside the prompt. Both can be useful, but
they are different layers.

## Scope

Suitable for:

- individual users
- training contexts
- educational environments
- organizations introducing structured AI usage

This variant can be used independently of the full governance framework.

## Licence

Creative Commons Attribution 4.0 International (CC BY 4.0)

You are free to use, adapt, fork and share this material, including
commercially. When licensed material is shared, appropriate attribution must be
retained, changes must be indicated and the licence and source must be
referenced as required by CC BY 4.0.

See the KSODI-Light [LICENSE.md](./LICENSE.md) for the complete legal text and
the [KSODI licence transition note](../KSODI-License-Transition-Note_V342-to-V350.md)
for the documented decision change.

---

© 2026 Anne Steinacker-Folkerts, Heiko Folkerts and Silke Honerkamp
Licensed under CC-BY-4.0
