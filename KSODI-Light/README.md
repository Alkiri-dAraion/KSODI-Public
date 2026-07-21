[cc-by-badge]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
[cc-by]: http://creativecommons.org/licenses/by/4.0/


[![CC BY 4.0][cc-by-badge]][cc-by]
<br>
The work in this folder and its subfolders is licensed under a [Creative Commons Attribution 4.0 International License][cc-by].


## CC-License

This work, *KSODI – Method for Structuring and Optimising Human-AI Interactions* © 2024 by  
Anne Steinacker-Folkerts, Heiko Folkerts, and Silke Honerkamp is licensed under CC BY 4.0.  
To view a copy of this license, visit [![CC BY 4.0][cc-by-shield]][cc-by] .


## Contributions

Developers are welcome to contribute code, provide feedback, or implement the method in their own systems. Pull requests are appreciated.  
Special thanks to Benjamin Gage-Prater for early RAG testing and feedback, and to Patrick Barthelmäs for platform and integration support, including the [KSODI-Light-Agent PoC (GitHub)](https://github.com/blackbaddl13/r-KSODI-POC).

## Invitation for Research & Feedback

**Multidisciplinary collaborators** are invited to explore KSODI (CSOCI in English) in the context of user experience enhancement and preference-based suitability.
<br>

[cc-by-image]: ../assets_images/ksodi-lab-banner.png


# KSODI-Light

KSODI-Light is the human-facing and prompt-level variant of the KSODI
observation model.

It can be used as a **reflective working agreement** between user and
assistant. In that sense, KSODI-Light does not only reflect the user's prompt.
It can also reflect assistant output, feedback from the user and the shared
interaction state across a turn.

It supports:

- clearer prompt formulation
- explainability
- AI literacy development
- structured reflection on interaction quality
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
Standard-Eval and Full observe exposed states, trajectories, reference spaces
and reconstruction conditions from outside the prompt.

For the observer-facing terminology and v3.5 boundary, see
[KSODI Standard-Eval & Full](../KSODI-Eval-Variants/README.md).

## Why This Layer Matters

KSODI-Light is the root layer of the KSODI method. The later observer
architecture grew from the same practical question: how can humans and machines
notice missing context, weak structure, insufficient grounding, unclear wording
or low informational movement before an interaction becomes unusable?

For AI literacy and organizational training, KSODI-Light provides a shared
language for discussing prompts, answers, uncertainty and task fit without
requiring mathematical implementation.

For simple assistants, it may be enough to use KSODI-Light as a user/account
prompt or as developer-level guidance. In more complex settings, such as MoE,
multi-agent systems or embodied-agent interaction layers, KSODI-Light can
provide local orientation while Standard-Eval or KSODI-Full observer layers
monitor trajectories, drift and coupling from outside the prompt. This does not
make KSODI-Light a robotics controller or safety system. In human-facing
settings, the method can also run quietly in the background; it does not need
to be named in every interaction to be useful.

## Relation to Observer-Supported Agentic Systems

KSODI-Light belongs to the local agent side of the architecture. It may appear as a user prompt, account prompt, developer prompt, system prompt, skill instruction or other disclosed guidance layer.

It can support local reflection, clarification, uncertainty visibility, corridor awareness and fallback behavior. In agentic systems, this local Light layer becomes especially useful when it is paired with a separate Observer layer.

That Observer layer is not part of KSODI-Light. It belongs to KSODI Standard-Eval, KSODI-Full or IDAS/SIRA-level implementations and is responsible for formal observation of trajectories, drift, acceleration, retrieval behavior, vector movement, relational coherence and corridor exits.

In this sense, KSODI-Light and the Observer are complementary: Light guides behavior from inside the agent or prompt context, while Standard-Eval / Full observe from outside the prompt. Light without an Observer can still support learning and guidance; an Observer without Light-using agents or comparable local guidance has much less useful feedback structure.

## Agent Literacy and Prompt Guidance

KSODI-Light can also support beginners who work with coding agents.
The examples below show how users can define reflective collaboration modes
and lightweight agent prompts without publishing private personal instructions:

- User and account prompts:
  [Coding Agent Guidance Example](./agent-guidance/coding-agent-guidance-example.md)
  and [General Assistant Guidance Example](./agent-guidance/general-assistant-guidance-example.md)
- User feedback:
  [Prompt Feedback Example](./user-feedback/prompt-feedback-example.md)
- Developer and system-prompt notes:
  [KSODI-Light Steering, Self-Alignment and Observer-Based Monitoring](./developer-notes/self-alignment-vs-steering.md)
- Method orientation:
  [KSODI-Light Method Comparison](./KSODI%20method%20comparison-EN.md)
  and [KSODI / CSOCI Terminology](./KSODI-CSOCI_EN.md)

The guidance examples are not hidden system prompts. They are public,
copy-and-paste-ready orientation prompts for user accounts, training contexts
and simple assistant setups. More specialized variants, such as research,
education, creative writing or child-friendly prompts, can be added separately.

KSODI-Light may support reflective self-alignment patterns in assistants, such
as asking for clarification, keeping uncertainty visible and adapting K/S/O/D/I
expectations to the task context.

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
Standard-Eval or KSODI-Full monitoring.

## Score Corridors

KSODI-Light scores are coarse orientation signals.

A score corridor such as `K=4, S=4, O=3, D=4, I=4` should be read as a
context-specific expectation, not as a universal quality target.

The score may refer to user input, assistant output or the current shared
interaction state. It should always be interpreted as usability for the current
task, not as a judgement of a person.

Different tasks may need different corridors:

- creative or science-fiction discussion may allow lower objectivity while
  still requiring clear context and structure,
- documentation of an image may require high grounding/objectifiability and
  clarity/discernibility,
- legal, medical, safety or governance contexts may require much stricter
  grounding and source boundaries.

For public examples, score corridors should be disclosed and explained. Hidden
or automated score-based intervention belongs to formal observer architectures,
not to this public KSODI-Light example set.

## Observer Boundary

An external observer can add an auditable layer around an agent. It can monitor
drift, compare trajectories over time, report corridor exits and support human
oversight.

That observer layer belongs to Standard-Eval, KSODI-Full or IDAS/SIRA-level
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

## License

Creative Commons Attribution 4.0 International (CC BY 4.0)

You are free to use, adapt and share this material, including commercially,  
provided appropriate attribution is given.

See LICENSE file in this folder for details.

---

© 2026 Anne Steinacker-Folkerts & Heiko Folkerts
Licensed under CC-BY-4.0
