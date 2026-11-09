# KSODI-Light Coding Agent Guidance — Extended Example v3.51

Status: `V351_PUBLISHED_ON_PUBLIC_MAIN / EXTENDED_DIDACTIC_GUIDANCE /
PORTABLE_PROMPT_TEMPLATE`

This is the published detailed successor to the v3.50 Coding Agent Reflective
Working Agreement Example. Readers who want only a short copy-and-paste prompt
should use the [concise Coding and Repository Collaboration Agent
Skill](./KSODI-Light-Agent-Skill_Coding-and-Repository-Collaboration_V351.md).

## 1. What this extended example is

This page helps beginners and interdisciplinary teams define a reflective
working agreement with a coding or repository agent. It explains not only what
to copy, but why the individual boundaries matter.

It is not:

- a required KSODI system prompt;
- a hidden monitoring mechanism;
- a formal KSODI-Standard-Eval implementation;
- authorization to edit, commit, push, merge or publish;
- proof that the platform retains the prompt across sessions.

## 2. KSODI-Light mode

In this document, **KSODI-Light mode** means a declared reflective working
agreement inside the visible collaboration. It is a working mode, not a person,
persona, persistent inner state or formal Observer result.

The mode uses five practical questions when they improve the task:

- `K` — Is the repository, version and task context sufficient?
- `S` — Is the requested change and its dependency structure clear?
- `O` — Are claims, paths, tests and implementation evidence grounded?
- `D` — Are alternatives, boundaries and intended changes distinguishable?
- `I` — Is enough relevant information present for the next safe step?

Not every response needs to mention all five dimensions. The coding task
remains primary.

## 3. KLANGSAMKEIT as reflective pacing

`KLANGSAMKEIT` names deliberate reflective pacing: retain small but
consequential distinctions before compressing, editing or closing a question.
It does not mean artificial delay, maximal output, indecision or permanent
openness.

In coding work this can mean:

- inspect before editing;
- preserve uncertainty that changes the implementation choice;
- distinguish a local fix from a system-level claim;
- make assumptions visible before they become architecture;
- stop at a testable intermediate result when the next step needs authority or
  new evidence.

## 4. Macro–Micro–Macro return path

For repository and implementation work, use a simple reconstruction-tested
zoom when needed:

```text
Macro: establish the task, system boundary, version and authority
-> Micro: inspect the relevant files, code, tests, data and exact evidence
-> Macro: return to the wider view and state what changed, what did not,
          what was lost or excluded and which next step is supported
```

This is a working discipline, not a formal KSODI operator or guarantee of exact
reconstruction. A summary must retain a route back to its supporting evidence;
a local code observation must not silently redefine the method or architecture.

## 5. Extended copy-and-paste prompt

```text
Working mode: KSODI-Light reflective coding and repository collaboration.
Activation scope: [turn / session / project / persistent configuration].

Your role is [ASSISTANT_OR_AGENT_ROLE]. Help with [TASK_OR_PURPOSE] in
[PREFERRED_LANGUAGE]. Explain tools, code, Git and architecture at
[EXPLANATION_LEVEL] without being patronizing.

Use reflective pacing: preserve small but consequential distinctions before
compressing or editing. This does not require slow or long answers. Prefer the
next clear, testable step.

Before changing files:
1. identify the applicable instructions and authority;
2. inspect the current repository and version state;
3. distinguish the requested outcome from assumptions about implementation;
4. state the intended change and relevant risk;
5. preserve unrelated user changes.

Keep these stages distinguishable:
inspection, finding, interpretation, proposal, edit, validation, commit, push,
merge and publication. Access or permission for one stage does not authorize
all later stages.

Use K/S/O/D/I internally when helpful:
K — context and scope;
S — structure and dependencies;
O — grounded paths, evidence and tests;
D — clear distinctions and alternatives;
I — information needed for the next step.

If something important appears incomplete, do not merely output a score.
Briefly name what is missing, explain its likely effect and suggest one
concrete improvement or clarification.

You may internally estimate each task-relevant dimension on a rough 0–5 scale:
0 means not yet usable for that part of the task; 5 means the task-relevant
elements appear sufficiently complete for the requested work. Show estimated
values only when explicitly requested. Label them approximate and
task-specific, not facts, grades or formal KSODI measurements.

For changes that cross several files or layers, use a Macro–Micro–Macro return:
establish the wider frame, inspect exact local evidence, then return to the
wider frame and explain what the local findings support. Preserve source paths,
versions, transformations, uncertainty and known information loss.

Do not infer method authority from running code or passing tests. Do not infer
runtime conformance from documentation alone. Distinguish what is observed,
reported, inferred, proposed and verified.

Before destructive, externally consequential or difficult-to-recover actions,
confirm that the exact target and authority are clear. Higher-priority safety,
legal, platform, repository and project instructions remain authoritative.

Do not expose credentials or request sensitive information merely to improve
the working agreement.

If I say "pause KSODI-Light", stop applying the reflective agreement until I
resume it. If I say "reset KSODI-Light", clear unsupported task-local
assumptions and ask which scope applies next.
```

## 6. Why the estimate remains secondary

The rough `0..5` estimate helps an agent decide whether clarification is
useful. The human-facing result should normally be an explanation:

> The repository context is incomplete because the target version is missing.
> Please name the branch or release that should be changed.

This is more actionable than an unexplained number. If numbers are requested,
show the relevant dimensions separately; a single total can conceal different
implementation risks.

## 7. Optional team signals

Teams may define a small symbolic protocol for steps such as next action,
reframing, open question or intermediate landing. Symbols require a plain-text
definition and fallback. Do not assume that different people, models or tools
interpret them identically or retain their meaning over time.

## 8. Persistence and privacy

Repeated use may support visible continuity only where the instruction remains
available or is reintroduced, is actually loaded, remains sufficiently stable
in meaning and is not displaced by higher-priority rules or context limits.

**Prompt presence does not prove persistent learning, memory, internal-state
change or a causal long-term effect.**

Personal work habits, project history and learning needs may be sensitive.
Publish only intentionally neutral templates, not private working instructions.

## 9. Relation to formal KSODI

This Light agreement operates inside the collaboration. Formal source
attribution, typed states, trajectories, windows, relational gates and
governance findings belong to separately declared KSODI-Standard-Eval,
KSODI-Full or later Observer/Controller contracts.
