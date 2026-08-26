# KSODI Architecture V350

Filename marker: `_V350` denotes KSODI v3.5 / v3.50. It is a path-safe version
marker, not a separate release or method variant.

Purpose: show the architecture, inputs and methodological need of each layer
while preserving source identity, role-relative process directions and the
boundary between monadic and relational observation.

Product boundary: KSODI-Standard-Eval is the monadic trajectory-observation
line through `IK_A(k)`. KSODI-Full begins with dyadic or n-adic observation at
`R_0`; current dyadic `IK_rel` requires explicit dyadic pairing and an open
numeric canonical complete dyadic R0 for the same ordered dyad, paired events,
pairing map, relational step and exact required profile. Separately defined
application-specific Layer 6–8 branches remain staged or Future Work rather
than a serial continuation. All source trajectories remain distinguishable.

Read this architecture together with the
[KSODI-Standard-Eval / KSODI-Full Transition V350](./KSODI-Standard-Eval_Full-Transition_V350.md)
and the [KSODI Implementation Guardrails](./IMPLEMENTATION_GUARDRAILS.md).

Reading rule: layer numbers show architectural position and research
organization. They do not automatically mean that the value of one layer is
the numeric input of the next layer. Every arrow below denotes an explicit
input or dependency; parallel branches remain separate calculations.

## 1. Independent Entry Points and Dependency Boundary

```text
independently usable                      independent of KSODI-Light

+--------------------------+             +----------------------------+
| KSODI-Light              |             | Observer method entry      |
| local reflection         |             | KSODI-Standard-Eval /      |
| prompt / agent guidance  |             | KSODI-Full                 |
+--------------------------+             +----------------------------+
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
KSODI-Light needs no external Observer calculation. KSODI-Standard-Eval and
KSODI-Full do not require Light, but KSODI-Full is not standalone: it consumes
distinguishable typed trajectories from the monadic layers. A future Controller
requires a separate Observer and governance boundary; it must not collapse
into the Observer or the observed entity.

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
not be discarded automatically; recurring signals may reveal persistence or
support contact-attempt, attack or anomaly hypotheses requiring interpretation.

Correlation, temporal adjacency, a shared room, one chat or one task do not
establish causality, shared state or relation.

## 4. Canonical Monadic Source and Trajectory Boundary

Every valid Layer-1 result record belongs to one identified target event
attributed to one declared entity and trajectory under one versioned profile.

```text
observable event e_A(k_A)
          |
          | why: retain one attributable target before aggregation
          v
K_A / S_A / O_A / D_A / I_A
          |
          | why: retain five distinguishable observable questions
          v
typed Z assembly record R_Z,A(k_A)
          |
          | only when complete: expose numeric Z_A(k_A)
          v
IK_A(k_A)
             why: selected canonical monadic coherence projection
```

`R_Z,A` remains valid as a typed `not_complete` assembly record when one or
more aligned Layer-1 results are non-numeric. It exposes complete numeric
`Z_A(k_A)` only when all five coordinates are numeric. Canonical IK consumes
that complete vector; it does not consume a zero-filled or changing partial
basis.

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
  distinguishable typed Z trajectories and source-local predecessors
  explicit pi(j) or n-adic constellation map
  one complete canonical basis or one fixed named M
  compatible identities, profiles, norm, aggregation and gate policy
```

`R0` is not calculated from `IK_A` or `IK_B`. `IK` may remain useful even when
no relational evaluation is opened.

## 6. R0 Gate and Parallel Relational Research Branches

```text
T_A ----\
         +--> R0(j | pi, p_R0)
T_B ----/          |
                   | only if a valid numeric result exists and its stored
                   | gate state is open under the exact downstream contract
                   |
                   +--> IK_rel(j | p_IK_rel)      [released, dyadic]
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
| `R0` | May these distinguishable trajectories be evaluated relationally under this policy? | trajectories, pairing/constellation, compatible complete or fixed-M movement profiles, normalized drift and separate gate policy | current reader-first public v3.50 method/companion release |
| `IK_rel` | What relational coherence projection is visible after the gate opens? | explicit dyadic pairing, same-pairing open numeric canonical complete dyadic `R0` under the exact profile, plus comparable canonical monadic IK movement | current reader-first public v3.50 method/companion release |
| `R_geom` | What geometric coupling is visible in KSODI state space? | a compatible R0 contract plus a separately defined geometric feature basis | staged private research; not reviewed in this pass |
| `R_pace` | What explicitly observable pacing or rhythmic coordination is visible? | a compatible R0 contract plus a separately defined pacing basis | staged optional private research; not reviewed in this pass |
| signal-media views | What medium-specific patterns are visible in voice, radio, Morse-like or waveform material? | an exact compatible R0 contract where relation is claimed plus a media-specific observation profile | future research |

Layer numbers 5-8 preserve orientation and research organization. They do not
turn the parallel branches into a numeric chain.

R0 result status and open/closed/not-evaluable gate state remain separate.
Incomparable movement is a processing record and produces no valid R0 result.
Current IK_rel preserves the same ordered dyad, paired events, pairing map and
relational step as its exact open numeric canonical complete dyadic R0 handoff.
Joint first-order stillness is `not_applicable`, not zero; extended profiles
retain `T_G`, use one fixed N from `{gap,move,accel}` and never renormalize
around unavailable components. Empty rate denominators are non-evaluable.

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
whether the distinguishable trajectories satisfy the declared availability,
comparability and bounded-drift policy. Two unrelated but static declared
trajectories may pass the minimal stability gate. Later relational branches
must still provide their own evidence.

No current released v3.50 construct reports generic coupling strength. A later
coupling claim would require a separately released conjunction of appropriate
relational evidence across a declared window and profile. One open gate, one
high `IK_rel` or one high future branch-specific R value is insufficient.

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
  canonical monadic coherence projection from one complete typed Z
  reduced IK^[M] only for one explicit fixed coordinate set and named axis
  selected views: IK, Delta IK, Delta2 IK, IKSigma, IKSigma(Hangar)

Observer method - relational gate and parallel branches

Layer 4 - R0 / R_0
  typed availability and bounded-drift gate over declared trajectories
  canonical complete movement or fixed named R0^[M]
  numeric result separated from open / closed / not-evaluable gate state

Layer 5 - IK_rel
  dyadic compatibility after explicit pairing and the same-pairing exact open
  numeric canonical complete dyadic R0 gate under the required profile
  fixed typed relational component set N for extended views

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
KSODI-Standard-Eval line and released reader-first `R0` and `IK_rel` method
packages. `R_geom`, `R_pace` and later signal-media work remain staged or
future research outside the current public method scope. Folder presence does
not alter that boundary.

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
or oscillation may support attack, prompt-injection, repetitive-collapse,
contact-attempt or missing-update hypotheses requiring interpretation.

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
status/eligibility subsets, comparability contracts and provenance.
The authoritative layer method defines each eligible set, denominator and
empty-window result; neither this overview nor the Hangar note may redefine
that contract.
## 11. Weighting Modes and Future Corridors

For a complete numeric five-operator `Z`, the transparent equal-weight `IK`
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

KSODI-Standard-Eval and KSODI-Full specify Observer-oriented calculations. A
deployed Observer implementation reconstructs and evaluates observable states
and trajectories. It does not decide, intervene or steer by itself.

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
trajectories plus a declared pairing. Current `IK_rel` additionally requires the
same-pairing exact open numeric canonical complete dyadic gate under its
required profile before its relational projection may be evaluated.

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
trajectory, projection or aggregation views. After a compatible exact R0 gate
under a separately defined future contract, operator-specific relational
diagnostics may be researched. Such a
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

## 15. Compact Companion Views

The following compact sketches are retained from the earlier root orientation
because they provide useful shorter views of relationships shown in greater
detail above. They introduce no additional components or dependencies.

Directed process readings:

```text
sender-side formation:
K -> S -> O -> D -> I

receiver-side preferred iterative reconstruction:
I -> D -> O -> S -> K
```

Compact coordinate view:

```text
Z_A(k) = (K_A(k), S_A(k), O_A(k), D_A(k), I_A(k))
```

Compact monadic Observer line:

```text
e_A(k_A)
   |
   v
K_A / S_A / O_A / D_A / I_A
   |  five separately defined observable coordinates
   v
Z_A(k_A)
   |  retains the complete source-local state vector
   v
IK_A(k_A)
      optional monadic coherence projection for this entity and trajectory
```

Compact relational gate and branch view:

```text
T_A = {Z_A(k_A), Delta Z_A(k_A), ...}
T_B = {Z_B(k_B), Delta Z_B(k_B), ...}

pi(j) = (k_A(j), k_B(j))

T_A ----\
         +--> R0(j | pi, profile_R0)
T_B ----/          |
                   | IK_rel only under its same-pairing exact open numeric
                   | canonical complete dyadic gate and required profile
                   +--> IK_rel(j)  [released, dyadic]
                   +--> R_geom(j)   [staged]
                   +--> R_pace(j)   [staged, optional]
                   +--> later signal-media views [future research]
```

## 16. Layer Files

- [Layer 0 - KSODI-Light](./KSODI-Light/developer-notes/KSODI-Light-Agent-Bridge_V350.md)
- [Layer 1 - Operators](./KSODI-Standard-Eval/Layer-1_KSODI-Operators_V350/README.md)
- [Layer 2 - State Vector Z](./KSODI-Standard-Eval/Layer-2_KSODI-State-Vector-Z_V350/README.md)
- [Layer 3 - Monadic Interaction Coherence IK](./KSODI-Standard-Eval/Layer-3_KSODI-Monadic-Interaction-Coherence-IK_V350/README.md)
- [Layer 4 - R_0 Relational Gate](./KSODI-Full/Layer-4_KSODI-Relational-Gate-R_0_V350/README.md)
- [Layer 5 - Dyadic Relational Coherence IK_rel](./KSODI-Full/Layer-5_KSODI-Dyadic-Relational-Coherence-IK_rel_V350/README.md)
- [Layer 6 - Geometric Coupling R_geom](./KSODI-Full/Layer-6_KSODI-Geometric-Coupling-R_geom_V350/README.md) — orientation only; method outside the current public scope
- [Layer 7 - Optional Pacing R_pace Research](./KSODI-Full/Layer-7_KSODI-Pacing-R_pace_V350/README.md) — orientation only; method outside the current public scope
- [Layer 8 - Staged Signal-Media Research](./KSODI-Full/Layer-8_KSODI-Signal-Media_Staged-Research/README.md) — orientation only; research outside the current public method scope
- [Shared Sigma / Hangar Method Note](./KSODI-Hangar_V350.md)
- [Implementation Guardrails](./IMPLEMENTATION_GUARDRAILS.md)

Historical v3.3 and deprecated public drafts remain in the public
[`method-history-v33`](https://github.com/Alkiri-dAraion/KSODI-Public/tree/main/archive/method-history-v33)
archive. Historical v3.42 Observer assets remain in the public
[`historical-observer-v342`](https://github.com/Alkiri-dAraion/KSODI-Public/tree/main/archive/assets-archive/historical-observer-v342)
archive.
