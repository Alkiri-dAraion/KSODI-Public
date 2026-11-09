# KSODI-Light Method Comparison and Combination Guide v3.51

Status: `V351_PUBLISHED_ON_PUBLIC_MAIN / EXPLANATORY_NOTE /
OBSERVATION_BASED_COMBINATION_HYPOTHESES`

Licence: `CC BY 4.0`, subject to the repository licence and any explicit
file-level exception.

## 1. Purpose and claim boundary

This note compares KSODI-Light with common prompting and reflection methods.
It asks which practical question each method helps answer and where two methods
may be combined without being treated as interchangeable.

The comparison is explanatory. Current combination statements are based on
structured observation and method analysis, not controlled comparative
measurement. No row proves that one method is universally better or that a
combination causes improved outcomes.

KSODI-Light remains a human-facing reflective working agreement. It does not
perform the formal calculations of KSODI-Standard-Eval or KSODI-Full.

## 2. Short comparison matrix

| Method | Main question | Typical structure | Useful for | Does not establish by itself |
|---|---|---|---|---|
| KSODI-Light | What is missing or sufficiently usable in the visible interaction frame? | Context, Structure, Objectivity/Grounding, Clarity, Information/Impulse | Reflection, clarification, agent guidance, teaching and bidirectional feedback | Correctness, truth, formal Observer values or long-term causal effect |
| RTF — Role, Task, Format | Who should do what, and in which output form? | Role, Task, Format | Compact task specification | Adequate evidence, correct referents or continued fit across turns |
| STAR | How can a situation or experience be narrated coherently? | Situation, Task, Action, Result | Cases, interviews, retrospectives and incident reports | Continued task fit, adequate grounding or causal explanation |
| Iterative prompting | How can an output be improved through repeated attempts? | Ask, review, adjust, ask again | Drafting, exploration and debugging | A stable criterion for distinguishing improvement from mere change |
| Self-consistency | Do several generated answers converge? | Generate variants, compare and select | Reasoning or classification uncertainty | That shared assumptions or shared errors are correct |
| ReAct | How can reasoning, actions and observations be interleaved? | Reasoning/action cycles with environmental observations | Tool use and environment interaction | That retrieved evidence is relevant, sufficient or correctly attributed |

## 3. What KSODI-Light adds

KSODI-Light keeps five practical questions available across a request, answer
or visible interaction frame:

```text
K — context
S — structure
O — objectivity, grounding and reference for the task
D — clarity and distinguishability
I — relevant information or a useful impulse
```

The agent may use a rough internal `0..5` estimate for each task-relevant
dimension. Ordinary output should remain simple: briefly identify what appears
missing, explain why it matters and suggest one improvement. Numeric estimates
are shown only when requested and must be labelled approximate and
task-specific.

This Light estimate is not a formal operator result, person rating or universal
quality score. A single sum is not the preferred view because it can conceal
which dimension needs attention.

## 4. Combination candidates

The following combinations are **complementary-question candidates**. The
status is `observation_based / not_comparatively_validated`.

| Combination | First method contributes | KSODI-Light contributes | Example use | Open validation question |
|---|---|---|---|---|
| Role–Task–Format + KSODI-Light | Explicit role, requested task and output form | Checks whether the surrounding context, grounding, clarity and information are usable for that task | A coding request specifies role/task/format; Light notices that repository version or acceptance evidence is missing | Does the combination reduce clarification loops across domains and models? |
| STAR + KSODI-Light | A narrative structure for situation, task, action and result | Checks task-fit, grounding, clarity and missing information within and after the narrative | An incident report is structured with STAR; Light identifies an unclear source, omitted context or unsupported conclusion | Does the combination improve reconstructibility without over-standardizing the account? |
| Iterative prompting + KSODI-Light | Repeated revision | Stable questions for why a revision is needed | A draft is revised several times while Light keeps the intended audience and evidence requirements visible | Can it distinguish meaningful improvement from stylistic drift? |
| ReAct + KSODI-Light | Tool/action/observation loop | Reflection on whether observations actually ground the task and retain provenance | An agent retrieves a source and acts; Light prompts a check that the source supports the stated claim | How portable is the combination across tool and agent architectures? |

Do not describe these relations as mathematical orthogonality unless a later
study defines and tests that property.

## 5. Additional research candidates

Earlier work also considered Chain-of-Thought-style prompting, Least-to-Most,
Tree of Thoughts, Self-Refine and CARE (Context, Action, Result, Example).
They remain comparison candidates rather than accepted KSODI components.
Their exact source, operational level, assumed inputs, evaluation criterion and
possible complementarity with KSODI-Light must be reviewed before a combination
claim is made. This v3.51 guide neither rejects them nor treats their omission
from the short matrix as a negative finding.

## 6. RTF naming boundary

In this active v3.51 comparison, **RTF** means **Role–Task–Format**. This is the
expansion used for compact task specification in the cited public guidance.
Other expansions are outside the active v3.51 comparison and must not be
silently imported under the same acronym.

## 7. Longitudinal boundary

KSODI-Light can be reused across turns or configured for a session, project or
persistent account context. Repetition alone does not establish a longitudinal
effect. Relevant conditions include whether the instructions remain available
or are reintroduced, whether the platform loads them, whether their meaning
remains stable and whether higher-priority instructions or context limits
displace them.

**Prompt presence proves neither persistent learning, memory, internal-state
change nor a causal long-term effect.**

Longitudinal observation and formal trajectory analysis require separately
declared evidence, identity, window and Observer contracts.

## 8. Practical choice

- Use RTF when a compact role, task and output-format specification is enough.
- Use STAR when the immediate need is a structured case or experience.
- Use iterative prompting when exploration and revision are central.
- Use KSODI-Light when people or agents need a small shared vocabulary for
  noticing missing context, structure, grounding, clarity or information.
- Combine methods only when their distinct questions help the declared task.

## 9. Formal-method boundary

KSODI-Light operates inside visible interaction and prompt guidance. Formal
numeric states, trajectories, drift, relational gates and auditable Observer
findings belong to KSODI-Standard-Eval, KSODI-Full or later explicitly
declared implementations. Any automated intervention requires a separate
human or Controller authority and governance contract.

## 10. Selected sources and predecessor

- Public predecessor: `KSODI-Light-Method-Comparison_EN_V350.md`.
- Role–Task–Format orientation: [Goethe University Frankfurt prompting
  guidance](https://lehre-virtuell.uni-frankfurt.de/knowhow/prompting-tipps-beim-einsatz-generativer-ki/).
- ReAct: [Yao et al., 2022](https://arxiv.org/abs/2210.03629).
- Self-consistency: [Wang et al., 2022](https://arxiv.org/abs/2203.11171).
- Least-to-Most: [Zhou et al., 2022](https://arxiv.org/abs/2205.10625).
- Tree of Thoughts: [Yao et al., 2023](https://arxiv.org/abs/2305.10601).
- Self-Refine: [Madaan et al., 2023](https://arxiv.org/abs/2303.17651).

Further comparison candidates remain open research. Their presence in a table
does not make them part of the KSODI method.
