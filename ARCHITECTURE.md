# KSODI Architecture

Status: public root orientation for the current KSODI v3.5 research repository
state. This file describes the method architecture; it does not by itself mark
a formal reference release.

The canonical detailed architecture sketch is
[KSODI_V350_ARCHITECTURE_ASCII.md](./KSODI_V350_ARCHITECTURE_ASCII.md). The
cross-layer data, trajectory and composition conditions are defined in the
[KSODI Implementation Guardrails](./IMPLEMENTATION_GUARDRAILS.md).

## 1. Purpose and Reading Rule

KSODI separates local reflection, observation and later controlled action. It
also separates source-local state from relational observation.

Layer numbers show architectural position and research organization. They do
not automatically define a serial function composition. An arrow means a
declared input or dependency only where this file says so explicitly.

## 2. Independent Entry Points and Dependencies

| Area | Can be used independently? | Function | Dependency boundary |
| --- | --- | --- | --- |
| `KSODI-Light` | yes | Local reflective working agreement for prompting, learning, training and agent guidance. | Does not require an external Observer calculation. It is not a prerequisite for Standard-Eval or KSODI-Full. |
| Observer method | yes | Standard-Eval and KSODI-Full reconstruct and evaluate observable source-local and relational states. | Does not require KSODI-Light. It observes; it does not decide, intervene or steer by itself. |
| Future Controller | no | Routes approved feedback or intervention within declared governance corridors. | Requires declared Observer outputs, a separate control boundary and prior governance decisions. It must not collapse into the Observer or the observed entity. |

`KSODI-Light -> Observer -> Controller` is therefore not one mandatory
pipeline. Light and the Observer are separate usable entry points. A future
Controller may depend on validated Observer findings; the Observer does not
depend on Light.

## 3. Entity Identity, Exchange Roles and Process Topologies

`A`, `B` and further entity labels identify distinguishable sources or
trajectories. Their identities remain stable. Sender and receiver are
exchange-relative roles: when `B` answers `A`, `B` becomes the sender without
ceasing to be entity `B`.

Two directed process readings remain visible:

```text
sender-side formation:
K -> S -> O -> D -> I

receiver-side preferred iterative reconstruction:
I -> D -> O -> S -> K
```

The receiver-side path is a preferred reconstruction direction for an unknown
or insufficiently conventionalized signal. Established conventions may allow
shortcuts, parallel checks or immediate decoding. Repetition may remain
evidence: it can reveal persistence, contact attempts, attack patterns or
recurring anomaly even when one occurrence was not reconstructable.

The canonical vector order is different in kind:

```text
Z_A(k) = (K_A(k), S_A(k), O_A(k), D_A(k), I_A(k))
```

This is a coordinate order, not a causal chain and not a claim that the five
operators must be calculated serially. Correlation, temporal adjacency and a
shared context do not establish causality or relation.

### Index convention

- `n` is a global event index in the observable event stream.
- `k_A` and `k_B` are local positions inside the distinguishable trajectories
  of `A` and `B`; compact monadic formulas may use `k` when the trajectory is
  already explicit.
- `j` is a declared relational exchange or paired-evaluation index, for
  example `pi(j) = (k_A(j), k_B(j))`.
- `t` may remain an implementation timestamp or a legacy paired-evaluation
  symbol only when its mapping to the canonical event, trajectory or pairing
  indices is declared. It must not silently create a shared predecessor across
  different trajectories.

## 4. Monadic Observer Line

All five Layer-1 operators are strictly monadic and source-attributed. Each
static value belongs to one identified target event in one declared
trajectory. A context, reference space or measurement basis may contain
visible material from outside that trajectory where the operator profile
permits it; this does not merge sources or create a relational value.

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

The five operators are needed to retain distinguishable questions about
observable context, structure, grounding, clarity and information impulse.
`Z` is needed to preserve their complete state instead of collapsing the event
prematurely into one score. `IK` is needed where a declared scalar projection
supports readable monitoring or comparison of one monadic trajectory. `IK`
does not feed `R0` and does not establish resonance.

For a complete applicable five-operator `Z`, an initial normalized `IK` view
may use equal weights:

```text
w_IK = (0.2, 0.2, 0.2, 0.2, 0.2)
```

This is a transparent baseline, not a universal optimum. Question-, domain-
or use-case-specific weights may later be learned or calibrated from declared
observation data. Every weight profile must remain explicit, versioned and
comparable. No current KSODI file claims that universally correct weights or
future Controller corridors are already known.

## 5. Relational Gate and Parallel Observation Branches

Relational evaluation requires at least two distinguishable source-local
trajectories plus an explicit pairing or constellation declaration:

```text
T_A = {Z_A(k_A), Delta Z_A(k_A), ...}
T_B = {Z_B(k_B), Delta Z_B(k_B), ...}

pi(j) = (k_A(j), k_B(j))

T_A ----\
         +--> R0(j | pi, profile_R0)
T_B ----/          |
                   | only when the gate is stable
                   +--> IK_rel(j)
                   +--> R_geom(j)   [staged]
                   +--> R_pace(j)   [staged, optional]
                   +--> later signal-media views [future research]
```

The branches after stable `R0` are conceptually parallel. `R_geom` is not
calculated from `IK_rel`; `R_pace` is not calculated from `R_geom`. Each branch
requires its own declared inputs, profile, applicability rule, weights and
validation. Their layer numbers preserve architectural orientation without
asserting a causal chain.

The current research need for each branch is distinct:

| Component | Question opened by the component | Current status |
| --- | --- | --- |
| `R0` | Are the declared distinguishable trajectories sufficiently applicable, compatible and stable for relational evaluation under the selected gate policy? | public research material |
| `IK_rel` | How can relational coherence be projected after the gate has opened? | public research material |
| `R_geom` | How can geometric coupling between trajectories be represented in KSODI state space? | staged construct; detailed definition pending further review |
| `R_pace` | How can explicitly observable pacing or rhythmic coordination be represented without reducing it to geometry? | staged optional construct; detailed definition pending further review |
| signal-media views | How may voice, radio, Morse-like, waveform or other media-specific signals be observed under their own profiles? | future research |

Physical distance is not automatically `R_geom`. It becomes an input only if
a declared application profile maps spatial observations into the relevant
relational feature space. Likewise, similar timing does not by itself prove
geometric coupling, shared meaning or desired direction.

Relational branch weights are branch-specific. They do not inherit the five
equal `IK` operator weights automatically. Weighting must follow the declared
question, observation profile and use case.

## 6. Layer Map and Public Repository Boundary

| Layer | Variant | Component | Repository status | Meaning |
| --- | --- | --- | --- | --- |
| 0 | [KSODI-Light](./KSODI-Light/README.md) | Local reflective layer | public | Independently usable working agreement for learning, prompting, training and agent guidance. |
| 1 | [KSODI Standard-Eval](./KSODI-Eval-Variants/KSODI-Standard-Eval/README.md) | `K/S/O/D/I` | public | Five source-attributed monadic observation coordinates. |
| 2 | [KSODI Standard-Eval](./KSODI-Eval-Variants/KSODI-Standard-Eval/README.md) | `Z` | public | Complete state vector over the five operator coordinates for one entity and trajectory position. |
| 3 | [KSODI Standard-Eval](./KSODI-Eval-Variants/KSODI-Standard-Eval/README.md) | `IK` | public | Monadic coherence projection; closes Standard-Eval. |
| 4 | [KSODI-Full](./KSODI-Eval-Variants/KSODI-Full/Full_v350/README.md) | `R0` / `R_0` | public | Relational applicability, compatibility and stability gate over distinguishable trajectories. |
| 5 | [KSODI-Full](./KSODI-Eval-Variants/KSODI-Full/Full_v350/README.md) | `IK_rel` | public | Relational coherence projection after stable `R0`. |
| 6 | [KSODI-Full](./KSODI-Eval-Variants/KSODI-Full/Full_v350/README.md) | `R_geom` | staged | Parallel post-`R0` research branch for geometric coupling in KSODI state space. |
| 7 | [KSODI-Full](./KSODI-Eval-Variants/KSODI-Full/Full_v350/README.md) | `R_pace` | staged | Parallel optional post-`R0` research branch for explicitly defined pacing. |
| 8 | [KSODI-Full](./KSODI-Eval-Variants/KSODI-Full/Full_v350/README.md) | Signal-media views | future research | Voice, rhythm/timing, audio, radio, Morse-like or other signal-media observation under media-specific profiles. |

The current public repository state contains the complete monadic
Standard-Eval line together with public `R0` and `IK_rel` research material.
`R_geom`, `R_pace` and later signal-media work remain staged or future research
unless their own file status explicitly changes. Public visibility is not the
same as a formal reference release.

## 7. Handshake, Coupling, Hangar and Controller Boundaries

`R0` is SYN/ACK-like only as an analogy for the methodological opening of
relational observation. It does not detect a protocol handshake, prove that
contact occurred, establish mutual acknowledgement or demonstrate coupling.
The Observer first declares the pair or constellation; `R0` then evaluates
whether its distinguishable trajectories satisfy the selected gate policy.

Within the current research architecture, strong observable coupling may be
reported only through sustained conjunction of relational evidence across a
declared window and profile. A high `IK_rel` alone, one R-family signal alone
or an open `R0` does not establish coupling. Coupling strength also does not
determine correctness, desirability, safety, alignment or causal direction.

Layer-1 operators may be inspected individually through monadic trajectory,
projection or aggregation views. A one-operator projection is not full `IK`,
and an operator-specific relational diagnostic is not complete `IK_rel` or an
R-family result.

`Sigma` denotes typed window aggregation within a selected layer.
`Sigma(Hangar)` denotes a derived distribution or comparison view. The Hangar
preserves attributable observer-side traces, trajectories, windows and
distributions; it is not a merged inner space and not the transient interaction
itself.

A future Controller may consume approved Observer findings only through a
separate governed feedback route. Observer output must not be fed back in a
way that allows the Observer to redefine its own evidence or thresholds
without an explicit control boundary.

## 8. Bounded Examples

### Human and chatbot

Human `A` sends a question and chatbot `B` receives it. The question is one
source-attributed event on trajectory `A`. When `B` answers, the roles reverse,
but the answer remains an event on trajectory `B`. The shared chat provides a
context container; it does not create one mixed `Z_AB`. Relational observation
begins only after the two trajectories and their exchange pairing are declared
and `R0` is applicable and stable.

### Two robots

Two robots may work in the same hall without forming one trajectory. They may
match cycle timing while their KSODI state-space trajectories diverge, or show
similar state-space movement while executing different timing patterns.
`R_pace` and `R_geom` therefore remain separate parallel questions. Physical
proximity alone establishes neither relation nor coupling.

### Morse-like exchange

A repeated carrier must first become detectable as a signal before an unknown
convention can be reconstructed. A reply using the same Morse-like sign and
timing may provide evidence for both structural or pacing comparison, but the
meaning of the sign, the existence of acknowledgement and the relation between
the sources still require separately declared observation steps.

For choosing an entry point, see
[Which KSODI Variant Do I Need?](./WHICH_KSODI.md). Before translating this
architecture into storage, evaluation or code, read the
[KSODI Implementation Guardrails](./IMPLEMENTATION_GUARDRAILS.md).
