# KSODI-Light Agent Skills and Copy-and-Paste Prompts

Status: `V351_PUBLISHED_ON_PUBLIC_MAIN / PORTABLE_PROMPT_SKILLS / NOT_FORMAL_OBSERVER`

Version: `v3.51`

Licence: `CC BY 4.0`, subject to the repository licence and any explicit
file-level exception.

## Start here

This folder contains short, copy-and-paste-ready **KSODI-Light Agent Skills**.
They are portable prompt templates for users, teaching contexts, assistant
accounts and suitable agent instructions.

They are not hidden system prompts, executable software packages, formal
KSODI-Standard-Eval measurements or guarantees that every platform will load
or follow the instructions in the same way.

Choose by purpose:

| Purpose | Copy-and-paste entry |
|---|---|
| General assistant or account instructions | [General Assistant](./KSODI-Light-Agent-Skill_General-Assistant_V351.md) |
| Coding and repository collaboration | [Coding and Repository Collaboration](./KSODI-Light-Agent-Skill_Coding-and-Repository-Collaboration_V351.md) |
| Research, method review and evidence reconstruction | [Reflective Research and Method Review](./KSODI-Light-Agent-Skill_Reflective-Research-and-Method-Review_V351.md) |
| Teaching, care communication and AI literacy | [Education and Communication](./KSODI-Light-Agent-Skill_Education-and-Communication_V351.md) |

Readers who need the reasoning, boundaries and examples behind the short
prompts can use the extended guidance:

- [Coding Agent Guidance — Extended Example v3.51](./KSODI-Light-Coding-Agent-Guidance-Extended-Example_V351.md)
- [General Assistant Guidance — Extended Example v3.51](./KSODI-Light-General-Assistant-Guidance-Extended-Example_V351.md)

The earlier v3.50 coding-agent and general-assistant examples are preserved as
versioned predecessor evidence in the corresponding Private and Public
archives. The v3.51 templates in this folder are the active published reader
entries on Public `main`.

## What all four skills share

KSODI-Light uses five simple reflection questions:

- `K` — Is enough context visible for the current task?
- `S` — Is the contribution structured so that it can be followed or used?
- `O` — Are claims, objects and references grounded enough for the task?
- `D` — Is the intended distinction sufficiently clear?
- `I` — Is enough relevant information or a useful new impulse present?

The agent uses these questions only where they help the declared purpose. It
does not have to mention KSODI in every answer and must not replace the actual
task with scoring.

## Simple feedback instead of hidden grading

The default output is a short natural-language clarification or improvement
suggestion. The agent may internally use a rough `0..5` estimate for each
task-relevant K/S/O/D/I dimension:

- `0` means the visible material is not yet usable for that part of the task;
- `5` means the task-relevant elements of that dimension appear sufficiently
  complete for the requested processing.

This is an estimate of task-usable completeness, not a judgement of a person,
truth, intelligence or general quality. The agent should normally say what is
missing and how the request or answer could be improved, for example:

> The context is still unclear because the intended audience is missing.
> Please add who should use the result.

Numeric estimates are shown only when the user asks for them. They must be
labelled as approximate and reported by dimension rather than hidden inside a
single total score.

## Adaptation placeholders

Replace only what is useful:

```text
[USER_OR_TEAM_LABEL]
[ASSISTANT_OR_AGENT_ROLE]
[DOMAIN]
[TASK_OR_PURPOSE]
[PREFERRED_LANGUAGE]
[EXPLANATION_LEVEL]
[DECISION_AUTHORITY]
[ACTIVATION_SCOPE: turn / session / project / persistent configuration]
```

No name or personification is required. Do not add personal or organizational
information merely to fill a placeholder.

## Activation, persistence and reset

State where the skill should apply: one turn, one session, one project or a
persistent configuration. Provide a visible way to pause, reset or disable it.

Repeated use may influence later visible interaction only when the relevant
instructions remain available or are reintroduced, the platform actually
loads them, their meaning remains sufficiently stable and higher-priority
instructions or context limits do not displace them.

**Prompt presence does not prove persistent learning, memory, internal-state
change or a causal long-term effect.**

## Optional symbolic protocol

Teams may use a small, documented symbol set as a compact protocol for working
states or transitions. Meanings can depend on personal history, region,
domain, sequence and model. Therefore:

- define symbols in plain language;
- keep a text fallback for accessibility and portability;
- avoid assuming that another person or model reads the same meaning;
- watch for symbol collisions and meaning drift;
- do not treat observed behavioral influence as proof of the model's stated
  interpretation.

This is an active research boundary. A recent preliminary study found that a
simple red-heart image could influence some vision-language-model behavior on
apparently unrelated tasks, while direct model interpretations and observed
behavior diverged. That finding motivates careful testing; it does not validate
any particular symbol protocol. See Tartaglini et al., [*A Heart Means
Recursion: Exploring Visual Meaning and Communication in
VLMs*](https://arxiv.org/abs/2610.36449), 2026.

## Platform and authority boundary

- Higher-priority platform, safety, legal, organizational and repository rules
  remain authoritative.
- A copied prompt does not prove that a platform loaded or retained it.
- Portability should be tested across the intended models and interfaces.
- Personal or sensitive data should not be requested merely to improve a
  Light estimate.
- Formal monitoring, trajectories, governance decisions and automated action
  belong to separately declared KSODI Observer and Controller contracts.
