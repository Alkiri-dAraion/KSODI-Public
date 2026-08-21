# KSODI v350 Eval Architecture Sketch

Status: canonical public root-level orientation sketch for the current v3.5
research repository state. Public visibility does not by itself mark a formal
reference release.

Purpose: show the architecture, inputs and methodological need of each layer
while preserving source identity, role-relative process directions and the
boundary between monadic and relational observation.

Reading rule: layer numbers show architectural position and research
organization. They do not automatically mean that the value of one layer is
the numeric input of the next layer. Every arrow below denotes an explicit
input or dependency; parallel branches remain separate calculations.

## 1. Independent Entry Points and Dependency Boundary

```text
independently usable                      independently usable

+--------------------------+             +---------------------------+
| KSODI-Light              |             | Observer method           |
| local reflection         |             | Standard-Eval / Full      |
| prompt / agent guidance  |             | observable reconstruction |
+--------------------------+             +---------------------------+
           no required arrow between these two entry points
                                                  |
                                                  | declared findings,
                                                  | approved corridors
                                                  v
                                      +---------------------------+
                                      | Future Controller         |
                                      | governed feedback/action  |
                                      +---------------------------+
                                      not independently usable
```

`KSODI-Light -> Observer -> Controller` is not one mandatory pipeline.
KSODI-Light needs no external Observer calculation. Standard-Eval and
KSODI-Full do not require Light. A future Controller requires a separate
Observer and governance boundary; it must not collapse into the Observer or
the observed entity.

## 2. Entity Identity, Roles and Index Convention

`A`, `B` and further labels identify distinguishable entities, sources or
trajectories. Their identity remains stable through role changes. Sender and
receiver are exchange-relative roles.

```text
exchange j:       A sends  -------------------->  B receives
next exchange:    A receives <------------------  B sends

entity identity:  A remains A                     B remains B
```

Canonical indices:

```text
n        global event index in the observable event stream
k_A      local position inside trajectory A
k_B      local position inside trajectory B
j        declared relational exchange / paired-evaluation index

pi(j) = (k_A(j), k_B(j))
```

Compact monadic formulas may use `k` when the trajectory is already explicit.
Existing formulas that use `t` must declare whether it is a timestamp,
implementation step or legacy paired-evaluation index and map it to the
canonical identities. `t` must never silently create a shared predecessor
across trajectories.

## 3. Coordinate Order and Directed Process Topologies

Canonical coordinate order:

```text
Z_A(k_A) = (K_A(k_A), S_A(k_A), O_A(k_A), D_A(k_A), I_A(k_A))
```

This order identifies five separately defined coordinates. It is not a causal
calculation chain, not a claim of statistical independence and not a required
serial execution order.

Role-relative process readings:

```text
sender-side formation:

K  ->  S  ->  O  ->  D  ->  I
context  structure  grounding  clarity / reconstruction  information impulse

receiver-side preferred iterative reconstruction:

I  ->  D  ->  O  ->  S  ->  K
detect an impulse  reconstruct  check sources  infer structure  place in context
```

Established conventions may permit immediate decoding, shortcuts or parallel
checks. Without a sufficient convention, the receiver-side direction may
recur until reconstruction stabilizes or remains unresolved. Repetition must
not be discarded automatically; recurring signals may reveal persistence,
contact attempts, attacks or anomaly.

Correlation, temporal adjacency, a shared room, one chat or one task do not
establish causality, shared state or relation.

## 4. Canonical Monadic Source and Trajectory Boundary

Every Layer-1 value belongs to one identified target event attributed to one
declared entity and trajectory under one versioned profile.

```text
observable event e_A(k_A)
          |
          | why: retain one attributable target before aggregation
          v
K_A / S_A / O_A / D_A / I_A
          |
          | why: retain five distinguishable observable questions
          v
Z_A(k_A)
          |
          | why: preserve the complete five-coordinate state
          v
IK_A(k_A)
             why: optional readable monadic coherence projection
```

The same construction remains separate for `B`:

```text
e_A(k_A) -> K_A/S_A/O_A/D_A/I_A -> Z_A(k_A) -> IK_A(k_A)
e_B(k_B) -> K_B/S_B/O_B/D_B/I_B -> Z_B(k_B) -> IK_B(k_B)
```

A visible context, reference space or measurement basis may contain material
from outside one trajectory where the operator profile permits it. The result
still belongs to the declared target event. Context visibility does not merge
sources and does not create a relational value.

Monadic movement uses only the local comparable predecessor:

```text
Delta Z_A(k_A) = Z_A(k_A) - Z_A(k_A - 1)
Delta Z_B(k_B) = Z_B(k_B) - Z_B(k_B - 1)
```

There is no implicit mixed `Z_AB` or monadic `Delta Z_AB`.

## 5. Branching After Z: Monadic Projection and Relational Gate

`IK` and `R0` answer different questions and use different inputs.

```text
source-local branch A

Z_A(k_A) -------------------------------> IK_A(k_A)
   |                                       monadic projection
   |                                       input: Z_A only
   |
   +---- contributes trajectory T_A ----\
                                        \
                                         +--> R0(j | pi, p_R0)
                                        /
   +---- contributes trajectory T_B ----/
   |
Z_B(k_B) -------------------------------> IK_B(k_B)

R0 inputs:
  distinguishable T_A and T_B
  explicit pi(j) or n-adic constellation map
  compatible profiles, applicability and selected stability policy
```

`R0` is not calculated from `IK_A` or `IK_B`. `IK` may remain useful even when
no relational evaluation is opened.

## 6. R0 Gate and Parallel Relational Research Branches

```text
T_A ----\
         +--> R0(j | pi, p_R0)
T_B ----/          |
                   | if applicable and R0 >= theta_R0_stable
                   |
                   +--> IK_rel(j | p_IK_rel)
                   |      relational coherence projection
                   |
                   +--> R_geom(j | p_geom)       [staged]
                   |      geometric coupling in KSODI state space
                   |
                   +--> R_pace(j | p_pace)       [staged, optional]
                   |      explicitly observable pacing / rhythm
                   |
                   +--> signal-media views       [future research]
                          media-specific signal observations
```

These are parallel post-`R0` branches:

```text
IK_rel  is not an input to R_geom
R_geom  is not an input to R_pace
R_pace  is not an input to IK_rel
```

Their eventual empirical relationships remain an open research question.
Entities may show similar pacing while their KSODI state-space trajectories
diverge, or geometric similarity without matching pace. A Morse-like reply may
match both sign structure and timing. No one example defines the branch
relation universally.

Physical distance is not automatically `R_geom`. It becomes an input only
where a declared application profile maps spatial observation into the
relevant relational feature space.

### Why each relational calculation exists

| Component | Required methodological question | Minimum declared basis | Status |
| --- | --- | --- | --- |
| `R0` | May these distinguishable trajectories be evaluated relationally under this policy? | trajectories, pairing/constellation, compatible profiles, applicability and normalized stability inputs | public research material |
| `IK_rel` | What relational coherence projection is visible after the gate opens? | stable `R0` plus its own complete relational projection basis | public research material |
| `R_geom` | What geometric coupling is visible in KSODI state space? | stable `R0` plus a separately defined geometric feature basis | staged; detailed definition pending |
| `R_pace` | What explicitly observable pacing or rhythmic coordination is visible? | stable `R0` plus a separately defined pacing basis | staged optional research |
| signal-media views | What medium-specific patterns are visible in voice, radio, Morse-like or waveform material? | stable `R0` where relation is claimed plus a media-specific observation profile | future research |

Layer numbers 5-8 preserve orientation and research organization. They do not
turn the parallel branches into a numeric chain.

## 7. SYN/ACK Analogy, Coupling and Causality Boundary

`R0` is SYN/ACK-like only as an analogy for the methodological opening of
relational observation.

`R0` does not:

- detect a protocol handshake;
- prove that contact or acknowledgement occurred;
- demonstrate semantic agreement;
- establish coupling, resonance or causality;
- determine correctness, desirability, safety or alignment.

The Observer declares the pair or constellation first. `R0` then evaluates
whether the distinguishable trajectories satisfy the selected applicability,
compatibility and stability policy. Two unrelated but static declared
trajectories may pass the minimal stability gate. Later relational branches
must still provide their own evidence.

Within the current research architecture, strong observable coupling may be
reported only from sustained conjunction of appropriate relational evidence
across a declared window and profile. One open gate, one high `IK_rel` or one
high branch-specific R value is insufficient.

## 8. Layer 0-8 Orientation Map

```text
Layer 0 - KSODI-Light
  independent local reflection / prompt and agent guidance
  no external Observer calculation required

Observer method - monadic line

Layer 1 - K/S/O/D/I
  five source-attributed coordinates for one target event
  selected views: X, Delta X, Delta2 X, XSigma, XSigma(Hangar)

Layer 2 - Z
  complete source-local state vector
  selected views: Z, Delta Z, Delta2 Z, ZSigma, ZSigma(Hangar)

Layer 3 - IK
  optional monadic coherence projection from one Z
  selected views: IK, Delta IK, Delta2 IK, IKSigma, IKSigma(Hangar)

Observer method - relational gate and parallel branches

Layer 4 - R0 / R_0
  gate over distinguishable trajectories and a declared pairing/constellation

Layer 5 - IK_rel
  relational coherence projection after stable R0

Layer 6 - R_geom [staged]
  parallel post-R0 geometric-coupling research branch

Layer 7 - R_pace [staged, optional]
  parallel post-R0 pacing research branch

Layer 8 - signal-media views [future research]
  media-specific voice, timing, audio, radio, Morse-like or waveform work

Future Controller
  separate governed architecture that may consume approved Observer findings
  not part of the current v3.5 method material
```

The current public repository state contains the complete monadic
Standard-Eval line and public `R0` and `IK_rel` research material. `R_geom`,
`R_pace` and later signal-media work remain staged or future research unless a
file-level status explicitly changes. Folder presence is not a release claim.

## 9. Scope and Application Selection

Not every use case needs every aggregation, Hangar view, drift value or
second-order drift value. Select observations per layer, application and
question.

Common observation focus may include:

- `Z_A(k)` and source-local corridor behavior;
- `IK_A(k)` where a monadic projection helps;
- `R0(j)` and `IK_rel(j)` where relational comparison is justified;
- a branch-specific R view only where its basis is defined;
- `O` and reference-space visibility where grounding matters.

In adversarial, safety-sensitive or drift-sensitive settings, operator-level
movement may become important. For example, `I` stagnation, bursts, recurrence
or oscillation may reveal attack patterns, prompt-injection pressure,
repetitive collapse, contact attempts or missing update-relevant information.

Decision rule: do not enable Sigma, Hangar, Delta or Delta2 everywhere by
default. Do not remove recurrence merely because one event was insufficiently
reconstructable.

## 10. Sigma and Hangar Views

`Sigma` means typed window aggregation inside a selected layer. It is not a
separate main layer.

`Sigma(Hangar)` means a derived distribution or comparison view over
attributable values, windows, trajectories or point-cloud-like observation
objects. The Hangar is an Observer-side view, not an additional metaphysical
space, not a merged inner state and not the transient interaction itself.

```text
single value  -> current state
sequence      -> source-local movement
window        -> pattern
Hangar view   -> position or distribution of patterns in an observation space
```

Static, Delta and Delta2 aggregates remain separate typed views with their own
applicability sets and provenance.

## 11. Weighting Modes and Future Corridors

For a complete applicable five-operator `Z`, the transparent initial `IK`
baseline may use:

```text
w_IK = (0.2, 0.2, 0.2, 0.2, 0.2)
```

This is not a universal optimum. Weights must follow the declared question,
application field and use case. Observation may later support learned or
calibrated weight profiles and possible Controller corridors. Such profiles
must be explicit, versioned and compared only under compatible conditions.

R-family branches use their own branch-specific features and weights. They do
not automatically inherit the five equal `IK` weights.

No current public file claims that universally correct weights, corridors or
Controller policies are already known.

## 12. Observer and Controller Boundary

Standard-Eval and KSODI-Full specify Observer-oriented calculations. A deployed
Observer implementation reconstructs and evaluates observable states and
trajectories. It does not decide, intervene or steer by itself.

Prompt-level reflection and lightweight local steering in KSODI-Light must not
be confused with system-level Controller intervention.

A future Controller requires:

- declared Observer findings;
- governance corridors defined before deployment for the application case;
- an explicit feedback and intervention policy;
- a separate control boundary and audit trail.

Observer output must not be fed back in a way that lets the Observer redefine
its own evidence, thresholds or evaluation basis without that control
boundary.

## 13. Bounded Examples

### Human and chatbot

Human `A` sends a question; chatbot `B` receives it. When `B` answers, the
roles reverse but entity identities do not. Each contribution receives its own
source-local operator values, `Z` and optional `IK`. The shared chat is a
context container, not a mixed `Z_AB`. `R0` uses the separately retained
trajectories plus a declared pairing before any relational branch may open.

### Two robots

Two robots can work in the same hall without becoming one trajectory. They may
match execution timing while their KSODI state-space trajectories diverge, or
show similar state-space movement under different timing patterns. This keeps
`R_pace` and `R_geom` as separate parallel research questions. Physical
proximity alone establishes neither relation nor coupling.

### Morse-like exchange

An unknown repeated carrier must first become detectable as a signal before
its convention can be reconstructed. A reply using the same sign and timing
may support several later comparisons, but does not by itself prove meaning,
acknowledgement, causal influence or coupling.

## 14. Optional Diagnostics and Deprecated Identifiers

Layer-1 operators may be inspected individually through source-local
trajectory, projection or aggregation views. After stable `R0`, separately
defined operator-specific relational diagnostics may be researched. Such a
partial view is not complete `Z`, canonical `IK`, `IK_rel` or an R-family
result.

Do not use these legacy identifiers as current v3.5 core terms:

```text
R_phase
R_struc
R_struct
R_takt
R_freq
```

Pace and future voice, rhythm/timing or signal-media work must not be
conflated with those deprecated identifiers.

## 15. Layer Files

- [Layer 0 - KSODI-Light](./KSODI-Eval-Variants/KSODI-Light-Agent_v350.md)
- [Layer 1 - Operators](./KSODI-Eval-Variants/KSODI-Standard-Eval/Standard-Eval_v350/layer-1-operators/README.md)
- [Layer 2 - State Vector Z](./KSODI-Eval-Variants/KSODI-Standard-Eval/Standard-Eval_v350/layer-2-state-vector-z_v350/README.md)
- [Layer 3 - IK](./KSODI-Eval-Variants/KSODI-Standard-Eval/Standard-Eval_v350/layer-3-ik_v350/README.md)
- [Layer 4 - R0 Gate](./KSODI-Eval-Variants/KSODI-Full/Full_v350/layer-4-r0-gate/README.md)
- [Layer 5 - IK_rel](./KSODI-Eval-Variants/KSODI-Full/Full_v350/layer-5-ik-rel/README.md)
- [Layer 6 - R_geom](./KSODI-Eval-Variants/KSODI-Full/Full_v350/layer-6-r-geom/README.md)
- [Layer 7 - Optional Pace Research](./KSODI-Eval-Variants/KSODI-Full/Full_v350/layer-7-r-pace/README.md)
- [Layer 8 - Signal-Media Research](./KSODI-Eval-Variants/KSODI-Full/Full_v350/layer-8-future-signal-media/README.md)
- [Shared Sigma / Hangar Method Note](./KSODI-Eval-Variants/Hangar_350.md)
- [Implementation Guardrails](./IMPLEMENTATION_GUARDRAILS.md)

Historical v3.3 and deprecated public drafts remain under
[`method-history-v33`](./archive/method-history-v33/README.md).
Historical v3.42 Observer assets remain under
[`historical-observer-v342`](./archive/assets-archive/historical-observer-v342/README.md).
