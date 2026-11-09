# KSODI-Light Agent Bridge v3.51

Status: `V351_PUBLISHED_ON_PUBLIC_MAIN / DEVELOPER_ORIENTATION /
NOT_IMPLEMENTATION_CONFORMANCE`

## 1. Purpose

KSODI-Light is the independently usable Layer-0 reflection and prompt-guidance
entry. It may be used as:

- a human-facing reflective method;
- user, account, project, developer or suitable system guidance;
- a portable KSODI-Light Agent Skill;
- local guidance for one participant in a wider agent or interaction system.

The current repository architecture keeps this entry independent from the
formal Observer line. During the layerwise Public transition, consult the
[published v3.50 architecture](../../KSODI-Architecture_V350.md) until the
reviewed v3.51 architecture package is present. External Observer calculation
begins with KSODI-Standard-Eval Layer 1; KSODI-Light does not calculate formal
K/S/O/D/I operator results, complete typed `Z`, `IK`, `R0` or `IK_rel`.

## 2. Agent-Skills entry

Published, copy-and-paste-ready templates are collected in the
[KSODI-Light Agent Skills hub](../agent-guidance/README.md). The hub separates:

- short prompts for direct use;
- extended guidance with rationale and safeguards;
- general, coding/repository, research/method and education/communication
  purposes.

These files are portable prompt templates. They are not automatically
installable vendor-specific skill packages and do not prove that a platform
loads, retains or follows them across turns.

## 3. Local guidance versus external observation

```text
KSODI-Light Agent Skill
  local, disclosed guidance inside an interaction
  clarification, reflective pacing and task-fit feedback

KSODI Observer
  separately declared external observation
  source identity, evidence, profiles, typed states and trajectories

Human or future Controller
  separately governed authority for feedback, escalation or action
```

No arrow between these roles is automatic. An Observer may evaluate an
interaction whose participants do not use KSODI-Light. A Light-guided agent may
operate without an external Observer. Observation does not itself authorize
intervention.

## 4. What a developer must declare

Before embedding a KSODI-Light Agent Skill, declare at least:

- purpose and intended audience;
- activation scope: turn, session, project or persistent configuration;
- instruction location and precedence;
- pause, reset or disable route;
- whether optional numeric estimates can be shown;
- privacy and retention boundary;
- who holds decision authority;
- how portability will be tested on the intended platform.

The default reader-facing behavior is a short explanation of missing context,
structure, grounding, clarity or information—not a routine score. An agent may
use a rough internal `0..5` estimate for task-usable completeness and disclose
per-dimension estimates only when requested.

## 5. Longitudinal claim boundary

Repeated prompt use may influence later visible interaction only where the
instruction remains available or is reintroduced, the platform loads it, its
meaning remains sufficiently stable and higher-priority instructions or
context limits do not displace it.

**Prompt presence does not prove persistent learning, memory, internal-state
change or a causal long-term effect.**

Formal longitudinal claims require separately identified events,
trajectories, windows, profiles and evidence.

## 6. External proof-of-concept provenance

The separate [KSODI-Light-Agent proof of concept by Patrick
Barthelmäs](https://github.com/blackbaddl13/r-KSODI-POC) is retained as an
external implementation reference and attributed technical contribution.

This bridge does not document its deployment, define its current runtime state
or establish v3.51 conformance. Implementation behavior and repository status
must be checked independently against the applicable method version and
software licence.

## 7. Developer return path

When moving from a Light prompt to code or architecture, preserve this return:

```text
declared interaction purpose
-> exact instruction and platform placement
-> observable behavior and evidence
-> bounded interpretation
-> wider architecture and governance consequence
```

Do not derive method authority from implementation convenience or treat a
visible response change as proof of hidden learning, alignment or safety.
