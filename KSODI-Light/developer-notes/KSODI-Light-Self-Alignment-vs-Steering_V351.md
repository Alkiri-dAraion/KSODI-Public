# KSODI-Light Reflection, Local Self-Adjustment and Prompt-Level Steering v3.51

Status: `V351_PUBLISHED_ON_PUBLIC_MAIN / DEVELOPER_NOTE /
EMPIRICAL_EFFECT_OPEN`

## 1. Terminology and claim boundary

KSODI-Light can support **local self-adjustment** in the limited sense that an
assistant follows disclosed instructions to clarify, preserve uncertainty or
revise its visible contribution.

Earlier material used the phrase `self-alignment`. In v3.51 this phrase must be
read narrowly: it does not claim technical AI alignment, changed model goals,
changed weights, persistent learning, autonomous safety or access to hidden
internal state.

`Prompt-level steering` likewise means a declared instruction may influence
visible behavior inside its applicable scope. It is not formal Observer
evaluation, Controller authority or proof of causal control.

## 2. Light-level reflection

A KSODI-Light instruction may ask an assistant to:

- request clarification when important context is missing;
- keep uncertainty visible;
- distinguish observation from inference or proposal;
- avoid judging the user or inferring hidden intentions;
- adapt grounding requirements to the task;
- accept feedback when an answer no longer fits the visible working frame;
- use reflective pacing before premature closure.

The working agreement may concern user input, assistant output or the visible
interaction frame. It does not construct a merged human-machine state.

## 3. KLANGSAMKEIT and feedback behavior

`KLANGSAMKEIT` names deliberate reflective pacing: retain small but
consequential distinctions before compressing or acting. It does not require
slow responses, maximal output, indecision or permanent openness.

For developers, this suggests a simple fallback pattern:

```text
if a task-relevant Light dimension appears incomplete:
  briefly explain what is missing
  explain why it matters for this task
  ask one focused clarification or offer one concrete improvement
else:
  continue with the actual task
```

The agent may use a rough internal `0..5` estimate for each task-relevant
K/S/O/D/I dimension. Routine output remains natural-language feedback. Numeric
estimates are disclosed only when requested, labelled approximate and shown by
dimension rather than collapsed into one preferred total.

These estimates concern task-usable completeness, not a person's quality,
truthfulness, intelligence or a formal Layer-1 operator result.

## 4. Reciprocal and asymmetric placement

When both interaction sides know and use the Light frame, each may reflect on
its own visible contribution. This is reciprocal use of a shared working
agreement, not proof of equal agency, shared meaning or merged state.

When only one agent uses the frame, local adjustment is asymmetric. The wider
interaction remains relational, but the method is not necessarily shared by
the other participant.

Whether either configuration improves task handling is an empirical question.
Prompt compliance alone does not establish improvement.

## 5. Architecture-agnostic does not mean input-agnostic

KSODI-Light may be adapted across chatbots, RAG systems, tool-using agents,
multi-agent workflows, mixture-of-experts settings or embodied systems.
Developers must still declare what the instruction can see and use:

- current request and visible conversation;
- user, account, project, developer or system instructions;
- retrieval results and reference-space visibility;
- tool state and action results;
- memory or persistence boundary;
- selected domain and task profile;
- privacy and retention conditions.

Poorly chosen inputs can make the agent respond to a different interaction
condition than intended. Architecture neutrality does not remove the need for
source, profile and evidence discipline.

## 6. Macro–Micro–Macro developer check

For non-trivial integration, keep a return path:

```text
Macro: intended interaction purpose, architecture and authority
-> Micro: exact prompt, placement, visible inputs, code, tests and traces
-> Macro: bounded behavioral finding, limitations and governance consequence
```

This is a working discipline, not a formal KSODI operator. The return must name
what the local evidence supports and what remains unknown.

## 7. Prompt-level estimates and feedback

Different tasks may need different completeness conditions. Creative work may
permit imaginative, weakly grounded exploration when declared as such;
documentation, research, safety or governance work may need explicit sources
and tighter distinctions.

The useful Light response is explanatory:

> The grounding is still incomplete because the referenced document is not
> available. Please provide it or ask for a clearly marked general answer.

An unexplained score or threshold is insufficient. Hidden automated
intervention does not follow from a Light estimate.

## 8. Observer and Controller boundary

KSODI-Light acts inside the instruction frame. A separately declared Observer
may inspect source-attributed events and trajectories from outside that prompt.

The current v3.51 Observer route distinguishes:

- Layer-1 typed K/S/O/D/I results;
- complete typed `Z` with identities, profiles and provenance;
- the monadic IK result family, including `IK_w`, `IK_M2`, `IK_ref` and
  `AxisDev_ref` where defined;
- the separate `R0` relational eligibility gate;
- current dyadic `IK_rel` only after its exact compatible gate and pairing.

Light does not calculate these results. `R0` is not derived from `IK`, and one
Observer result does not by itself authorize feedback or action.

Any enforced fallback, escalation or intervention requires a separately
declared human or future Controller responsibility, policy and audit trail.

## 9. Longitudinal effect boundary

Repeated use may influence later visible interaction only where the relevant
instruction remains available or is reintroduced, the platform loads it, its
meaning remains sufficiently stable and higher-priority instructions or
context limits do not displace it.

**Prompt presence does not prove persistent learning, memory, internal-state
change or a causal long-term effect.**

Long-term drift or recovery claims require explicit source identity, event and
trajectory records, windows, profiles, retention rules and evidence.

## 10. Target groups

### User, account or project prompts

- make clarification and uncertainty handling visible;
- support task-fit feedback;
- provide a pause and reset route.

### Developer or system instructions

- declare input, reference, tool and persistence boundaries;
- define natural-language fallback behavior;
- test portability instead of assuming it.

### Observer implementations

- remain external to the Light prompt;
- preserve source identity, status, profile and provenance;
- report findings without taking action by themselves.

## 11. Research status

Prompt wording, internal estimates, clarification strategies, model/platform
differences and longitudinal effects remain empirical research questions.
Public examples support orientation, training and reproducible questions; they
do not establish enterprise, regulated-domain or safety conformance.

The current [Agent Skills hub](../agent-guidance/README.md) provides portable
examples. Repository- or implementation-specific instructions remain separate
and must not be inferred from these generic notes.
