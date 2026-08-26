# KSODI Hangar, Sigma, Drift and Point Clouds

**Status:** current public v3.50 research reference note; repository visibility is not by itself a formal release marker  
**Scope:** KSODI Standard-Eval and KSODI-Full Observer views  
**Visibility:** public research material; private canonical workbench origin retained  
**Filename marker:** `_V350` denotes KSODI v3.5 / v3.50

---

## 1. Purpose

This note defines where Sigma, Sigma(Hangar), Drift and Drift Acceleration are methodically useful within the KSODI architecture.

KSODI does not only observe isolated source-attributed states. It can also observe how comparable states, trajectories and relational evaluations move, stabilize, diverge or become unstable across declared indices and windows.

A single value may describe a current state.  
A sequence describes movement.  
A window describes a pattern.  
A Hangar describes the distribution of such patterns inside an observation space.

The Hangar is therefore not an additional metaphysical space. It is a formal observation space for state distributions, trajectory behavior and interaction dynamics.

Sigma is not a separate main layer in the architecture. Sigma means window
aggregation within a given layer. The Hangar is the comparison and observation
space in which aggregated windows, distributions, trajectories and point clouds
can be compared.

### 1.1 Term Origin and Boundary

The word "Hangar" comes from Anne's empirical working language and originally
arose from a spelling error. It remained because the accidental name provided
a useful analogy: aircraft enter a hangar for maintenance, while observable
contributions to an interaction can be gathered in a shared observer-side
space for inspection and comparison.

In this analogy, the contributions are represented by source-attributed
traces. They may be placed beside one another, compared across declared
windows and maintained as evidence without being fused into one contribution,
one entity or one trajectory. The Hangar therefore gathers comparable
observation objects; it does not merge their identities. What began as a
spelling error became a stable method term because this boundary proved useful.

The metaphor has a strict boundary.

An entity may internally process ideas, memories, intentions or impressions in
ways that are fluid and not directly observable. KSODI does not claim access to
that inner space.

The canonical KSODI Hangar is the observer-side counterpart: it stores and
compares traces of what has actually become externally observable. It must not
be confused with an imagined "inner hangar" of a participant.

```text
KSODI brings observable runway traces into the observer-side Hangar;
it never enters a participant's inner hangar.
```

The transient Handshake / interaction space between participants belongs to
the interaction process. It is not the canonical Hangar. `R0` opens relational
observation of a declared constellation; it does not establish coupling.

Individual signals remain attributable to their emitting source. Across a
declared window, their reciprocal ordering may form an observable relational
pattern that cannot be reduced to either trajectory alone. No single open gate,
high `IK_rel` value or high branch-specific R value is sufficient to establish
coupling. Any later coupling claim requires an explicitly defined conjunction
of branch-appropriate evidence, window policy and application profile. The
exact empirical definition remains a research question.

The Hangar preserves comparable traces, windows, trajectories and distributions
after interaction has produced observable signals. In turn-taking, the receiver
of one contribution may become the next sender, but the Hangar does not merge
the participants' inner processing spaces, thoughts or internal states.

For the formal Handshake and coupling boundary, see
[`KSODI_Relational-Gate-R_0_V350.md`](./KSODI-Full/Layer-4_KSODI-Relational-Gate-R_0_V350/KSODI_Relational-Gate-R_0_V350.md).

---

### 1.2 The n-Hangar Distinction

The informal **n-Hangar theory** extends the maintenance analogy to any
declared set of distinguishable entities. Each entity `E_i` may be imagined as
having its own private maintenance Hangar: an internal processing space in
which it handles memories, intentions, representations or other entity-specific
material.

These inner Hangars are analogies, not KSODI observation objects. They are not
directly visible to the external Observer and, wherever this boundary can be
maintained, are outside the scope of observation in v3.50. Any
application-specific inference about internal processing must remain clearly
distinguishable from a directly observed KSODI state. For `n` distinguishable
entities, the analogy therefore retains `n` separate inner Hangars.

Only when externally observable, source-attributed signals are exchanged can
an **exchange Hangar** be instantiated for a declared observation window. It
contains the observable traces contributed by the participating entities and
places them in one observer-side comparison space while preserving their
separate event, entity and trajectory identities.

```text
Entity A: private inner Hangar   [not observed]
Entity B: private inner Hangar   [not observed]
... one separate inner Hangar for each distinguishable entity

source-attributed observable signals
                  |
                  v
observer-side exchange Hangar for the declared window and profile
```

"Shared" refers only to the declared comparison space. It does not mean a
shared mind, merged state or common trajectory. The existence of an exchange
Hangar also does not by itself authorize relational calculation: dyadic or
n-adic evaluation still requires explicit pairing or constellation metadata
and an evaluable open `R_0` gate under the declared branch contract. Current
dyadic `IK_rel` additionally requires open canonical complete dyadic `R_0`
under the exact required profile.

The term is retained as an explanatory distinction. Formal definitions and
implementations must use the declared event, entity, trajectory, window and
profile identities rather than relying on the metaphor alone. The labels in
the illustration are not additional KSODI symbols or operators.

---

### 1.3 Why Five Operator Values Define a Five-Dimensional Observation Space

A coordinate space does not require physical directions. It requires a
declared set of distinguishable numerical coordinates.

One normalized value can be shown on a line. Two values locate a point in a
square, and three values locate a point in a cube. KSODI assigns five
normalized values to one explicitly identified, source-attributed observable
event:

```text
Phi(e) = (K(e), S(e), O(e), D(e), I(e)) in [0,1]^5
```

The Cartesian product `[0,1]^5` is mathematically a five-dimensional
hypercube. It represents the complete formal range of possible KSODI operator
combinations under one declared evaluation profile.

This does not mean that the five operators are statistically independent,
physically spatial or empirically uncorrelated. Context, structure, grounding,
clarity and information impulse may influence one another. Their distinction
means that they remain separately defined observation coordinates. Correlation
changes the distribution of observed points inside the space; it does not
remove the coordinate system.

The hypercube is the formal value domain. KSODI does not assume that all
possible coordinate combinations occur empirically. Observed events may occupy
only a restricted, clustered, correlated or curved region inside that domain.

One source-attributed event produces one observable point. A sequence of
comparable points from the same declared trajectory produces a path. Several
trajectories or observation windows may form point clouds. The Hangar is the
Observer-side comparison view for these attributable points, paths, windows
and distributions.

Every monadic state change is assigned to one declared entity or trajectory by
default:

```text
Delta Z_A(k) = Z_A(k) - Z_A(k - 1)
```

There is no implicit shared `Delta Z_AB`. If two or more trajectories are
meant, the participating trajectories and the relational evaluation must be
declared explicitly through exchange, reply, pair or n-adic metadata.
Relational layers compare or relate distinguishable trajectory-local states
and movements; they do not create one mixed monadic state.

If one or more operators are not applicable, the missing coordinates must not
be replaced by zero. The resulting observation is a masked or partial
projection, not a complete point in the five-dimensional hypercube.

For the cross-layer source-attribution and implementation boundary, see
[KSODI Implementation Guardrails](./IMPLEMENTATION_GUARDRAILS.md).

## 2. Simple and Complex Observation Views

KSODI distinguishes human-readable projections from richer machine-readable
observation objects. Every view retains its entity or trajectory identity,
profile, applicability and index type.

Human-readable monadic views may use:

```text
Z_A(k_A)
IK_A(k_A)
Delta Z_A(k_A)
Delta IK_A(k_A)
```

Human-readable relational views may use:

```text
R0(j | pi, p_R0)
IK_rel(j | p_IK_rel)
R_geom(j | p_geom)     [staged]
R_pace(j | p_pace)     [staged, optional]
```

A displayed axis is a projection of the corresponding observation object. It
must not be reported as the complete vector, cloud, branch or R-family.

Machine-side analysis may retain richer typed structures:

```text
T_A = {Z_A(k_A)}
Delta T_A = {Delta Z_A(k_A)}
G_rel(j),  IK_rel_cloud(W_j)
G_geom(j), R_geom_cloud(W_j)     [staged]
G_pace(j), R_pace_cloud(W_j)     [staged]
```

This is a separation of views, not a loss of precision:

- simple projections support explanation, dashboards and responsible review;
- vectors and trajectories support source-local movement analysis;
- relational feature objects support explicitly paired comparison;
- Hangar views compare typed distributions across compatible windows, profiles
  or declared constellations.

---
## 3. Core Distinction and Dependency Map

The architecture separates source-local observation from relational
observation. Layer numbers describe position and research organization. Every
arrow below denotes an actual input or dependency.

```text
e_A(k_A) -> K_A/S_A/O_A/D_A/I_A -> Z_A(k_A) -> IK_A(k_A)
e_B(k_B) -> K_B/S_B/O_B/D_B/I_B -> Z_B(k_B) -> IK_B(k_B)

T_A = {Z_A(k_A)} ----\
                       +--> R0(j | pi, p_R0)
T_B = {Z_B(k_B)} ----/            |
                                  +--> IK_rel(j | p_IK_rel)
                                  +--> R_geom(j | p_geom) [staged]
                                  +--> R_pace(j | p_pace) [staged, optional]
                                  +--> signal-media views [future]
```

`IK_A` is calculated from `Z_A`; `IK_B` is calculated from `Z_B`. `R0` is not
calculated from either monadic `IK`. It evaluates whether distinguishable
trajectories and an explicit pairing or constellation satisfy the selected
applicability, compatibility and stability policy.

After their compatible open numeric canonical complete `R0` gate contracts,
`IK_rel`, `R_geom` and `R_pace` are parallel relational research branches.
None is automatically the numeric input of another. Every
branch requires its own complete basis, profile and applicability rules.

Drift, acceleration, Sigma and Hangar are selected typed views within a layer
or branch. They are not mandatory intermediate layers and do not change the
dependency direction.

There is no canonical generic `RΣ` value. In this note, family-level shorthand
is explanatory only. Formal files and implementations must name the concrete
branch, such as `IK_relΣ`, `R_geomΣ` or `R_paceΣ`.

---
## 4. Monadic and Relational Observation

The following values are strictly monadic and source-attributed:

```text
K_A / S_A / O_A / D_A / I_A -> Z_A -> IK_A
```

Each value belongs to one identified target event in one declared local
trajectory. A shared chat, room, channel, task or reference space does not
create a mixed monadic state.

The following calculations are relational or potentially n-adic:

```text
R0
  +--> IK_rel
  +--> R_geom   [staged]
  +--> R_pace   [staged, optional]
  +--> signal-media views [future]
```

They require at least two distinguishable trajectories or a declared n-adic
constellation. `R0` is the methodological gate; it does not itself detect a
technical handshake, contact, acknowledgement, coupling or causality.

Entity identity remains stable while sender and receiver roles may reverse:

```text
exchange j:      A sends     -> B receives
next exchange:   A receives <-  B sends

A remains A; B remains B.
```

Canonical indices:

```text
n        global observable-event index
k_A      local position in trajectory A
k_B      local position in trajectory B
j        relational pairing / evaluation index
pi(j) = (k_A(j), k_B(j))
```

A retained `t` must be declared as timestamp, implementation step or legacy
index and mapped to these identities. It must not silently create a common
predecessor across trajectories.

---
## 5. What Sigma Means

Sigma indicates aggregation across a declared, typed observation window. A
window may follow source-local trajectory positions, relational pairing
positions, timestamps or another explicitly ordered basis. The index type must
not remain implicit.

Examples of single observations:

```text
Z_A(k_A)
IK_A(k_A)
IK_rel(j)
R_geom(j)   [staged]
```

Examples of branch-specific window views:

```text
Z_AΣ(W_A)
IK_AΣ(W_A)
IK_relΣ(W_j)
R_geomΣ(W_j)   [staged]
```

`W_A` contains comparable local positions from trajectory A. `W_j` contains
comparable declared relational evaluations. They are not interchangeable.

Where applicability masks are used, the Sigma view declares its active policy:

```text
W_app,X = {q in W_X | X(q) is applicable under profile p_X}
applicability_rate_X(W_X) = |W_app,X| / |W_X|
```

Here `q` is the already declared index type for `X`; it is not a new universal
time index. Masked or applicability-aware windows must be named and must not be
presented as complete full-window values.

Sigma is useful when single observations are insufficient. It can show
stability, drift, oscillation, collapse, convergence or recurrence. Sigma does
not automatically mean improvement, causality or temporal aggregation. It
means aggregation under a declared window policy.

---
## 6. What Sigma(Hangar) Means

A Hangar view compares typed distributions of attributable observation
objects. It is derived from stored or reconstructable Observer-side material;
it is not the transient interaction itself and not a merged internal state.

Examples of point or trajectory distributions:

```text
H_Z(W_A | p_Z)        = {Z_A(k_A) | k_A in W_A}
H_IK(W_A | p_IK)      = {IK_A(k_A) | k_A in W_A}
H_IK_rel(W_j | p_rel) = {IK_rel(j) | j in W_j and R0 is stable}
```

Examples of distributions over already aggregated windows:

```text
{Z_AΣ(W_A,i)}
{IK_AΣ(W_A,i)}
{IK_relΣ(W_j,i)}
```

`Sigma(Hangar)` is therefore not an untyped second aggregation. The view must
declare:

- the observed object type and layer or branch;
- entity, source and trajectory identities;
- index and window policy;
- evaluation profile, basis and applicability mask;
- whether it contains single values, trajectories, window aggregates or
  feature-cloud objects.

The Hangar becomes useful when the question changes from “What is the current
value?” to “Where does this attributable pattern sit among compatible observed
patterns?” It supports comparison, corridor monitoring, anomaly detection and
later governance-oriented review without treating single outputs as isolated
events.

---
## 7. Drift and Acceleration

Drift describes movement between comparable observations inside the same typed
sequence.

For monadic source-local quantities:

```text
Delta Z_A(k_A)  = Z_A(k_A)  - Z_A(k_A - 1)
Delta IK_A(k_A) = IK_A(k_A) - IK_A(k_A - 1)
```

For a relational branch value `X_b` after applicable `R0`:

```text
Delta X_b(j) = X_b(j) - X_b(j - 1)
X_b in {IK_rel, R_geom, R_pace}
```

The two relational evaluations must use a comparable pairing policy, profile
and branch basis. `R_geom` and `R_pace` remain staged. A gate-status difference
may be observed only where the `R0` policy defines an ordered, comparable gate
value.

Acceleration describes change in that movement:

```text
Delta2 Z_A(k_A)  = Delta Z_A(k_A)  - Delta Z_A(k_A - 1)
Delta2 IK_A(k_A) = Delta IK_A(k_A) - Delta IK_A(k_A - 1)
Delta2 X_b(j)    = Delta X_b(j)    - Delta X_b(j - 1)
```

There is no implicit `Delta Z_AB`, no cross-entity predecessor and no generic
untyped relational Delta. Drift answers whether a declared observation sequence is
moving. Acceleration asks whether that movement is itself changing.

---
## 8. Why drift is needed

Drift is needed because interaction is not static.

A single value may look acceptable while the trajectory is already moving away from stability.

Examples:

- A Z value may still be within a normal range while one operator begins to decline.
- An IK value may remain high while ΔIK shows gradual weakening.
- A branch-specific relational value may appear stable while its declared trajectory relation or feature distribution begins to change.

Drift makes the direction and magnitude of change observable.

---

## 9. Why acceleration is needed

Acceleration is needed because gradual drift and sudden instability are different phenomena.

A small but increasing drift may indicate early instability.

A stable value with rising acceleration may indicate an approaching transition in the observed regime.

A strong negative acceleration may indicate collapse, loss of grounding, loss of pacing or sudden semantic divergence.

Acceleration therefore acts as an early warning signal.

It does not judge the interaction.  
It indicates that the dynamics of change have changed.

---

## 10. Where Sigma and Sigma(Hangar) are useful

### 10.1 Z

ZΣ is useful.

ZΣ aggregates state vectors over a window.

ZΣ(Hangar) is useful.

It shows how interaction states distribute across an observation space.

Relevant metrics:

```text
ΔZ
Δ²Z
Drift_L1
Drift_L2
Dispersion
corridor deviation
cluster movement
```

Use case:

`Z_AΣ` and its compatible Hangar views show whether one source-local observable state trajectory remains stable, disperses, compresses or drifts across its declared index or window.

---

### 10.2 IK

IKΣ is useful.

IKΣ aggregates coherence projections over a window.

IKΣ(Hangar) is useful.

It shows the distribution of coherence projections across sessions, windows or comparison groups.

Relevant metrics:

```text
ΔIK
Δ²IK
ΔIKΣ
Δ²IKΣ
ΔIKΣ(Hangar)
Δ²IKΣ(Hangar)
projection drift
corridor deviation
window stability
cluster migration
```

Use case:

`IK_AΣ` and its compatible Hangar views show whether the monadic coherence projection of one declared trajectory remains stable across its selected window.

For long-running systems, IKΣ(Hangar) drift can show whether a whole interaction corridor, cluster or distribution begins to move even when individual points remain inconspicuous. This is an observation signal, not an automatic judgment.

---

### 10.3 IK_rel

IK_relΣ is useful.

IK_relΣ aggregates relational coherence over a window after R₀ has established dyadic validity.

IK_relΣ(Hangar) is useful.

It shows whether relational coherence between trajectories remains stable across windows, sessions or participant pairs.

For point-cloud analysis, `IK_rel_cloud(W)` stores the relational feature
vectors around the relational axis over an observation window.

Relevant metrics:

```text
ΔIK_rel
Δ²IK_rel
ΔIK_relΣ
Δ²IK_relΣ
ΔIK_relΣ(Hangar)
Δ²IK_relΣ(Hangar)
relational distance drift
corridor deviation
pairwise dispersion
applicability rate
gate-closure frequency
```

Use case:

`IK_relΣ` and its compatible Hangar views show how the declared relational coherence projection behaves across comparable paired evaluations.

They must be interpreted together with R₀ gate status. A high IK_relΣ over a very low applicability rate is not equivalent to stable relational coherence across the full window.

---

### 10.4 R₀

R₀Σ is useful.

`R0Σ` aggregates comparable gate evaluations over a declared relational window and policy.

R₀Σ(Hangar) may be useful.

It shows how relational applicability and gate stability vary across compatible pairing windows or declared constellations.

Relevant metrics:

```text
ΔR₀
Δ²R₀
dyadic stability drift
threshold crossings
```

Use case:

`R0Σ` shows whether relational evaluation remains methodically applicable across the declared pairing window. It does not establish coupling or semantic agreement.

---

### 10.5 R_geom

`R_geomΣ` is a staged research view. Where a versioned geometric basis is
explicitly defined, it may aggregate dyadic or n-adic geometric-coupling
observations across comparable relational evaluations.

`R_geomΣ(Hangar)` is likewise staged. It may compare geometric feature
distributions across compatible windows, pairs or declared constellations.

Where a geometric basis has been defined, a staged `R_geom_cloud(W_j)` may retain its geometric feature vectors over a compatible relational window.

Candidate research metrics may include:

```text
Delta R_geom
Delta2 R_geom
proximity features
direction features
response and balance features where separately defined
geometric corridor movement
```

These labels do not create an active formula by themselves. Physical distance
is not automatically `R_geom`; an application profile must explicitly map
spatial observations into the selected relational feature space.

Use case:

A future `R_geomΣ` view may show whether a declared geometric relation between
trajectories stabilizes, weakens or changes corridor. High geometric similarity
is not automatically desirable, causal or equivalent to pacing similarity.

---

### 10.6 R_pace

`R_paceΣ` is a staged optional research view. It becomes meaningful only
where pacing, lag, lead, timing asymmetry or rhythm has been made explicitly
observable under a versioned profile.

`R_paceΣ(Hangar)` may then compare pacing-feature distributions across
compatible relational windows or declared constellations.

Candidate research metrics may include:

```text
Delta R_pace
Delta2 R_pace
pacing stability
lag / lead
oscillation
desynchronization
```

These labels do not define the final empirical relation between pace and
geometry. Two robots may move through KSODI state space in similar directions
while their execution timing diverges. Conversely, they may answer at the same
pace while their state-space trajectories move apart.

`R_phase`, `R_struc`, `R_struct`, `R_takt`, `R_freq` and `V(t)` are not
active v3.50 terms.

---

### 10.7 Future Signal-Media Extension

Frequency, rhythm, voice, radio, Morse-like, waveform or other signal-media
features are not active v3.50 core terms. They belong to future Layer-8
research unless a concrete application profile explicitly defines the
observable unit, carrier, segmentation, index, feature basis and comparison
policy.

Future Sigma or Hangar views may become useful when those features are measured
consistently across source-local or relational windows. Recurrence, density,
timing and waveform regularity may support anomaly or contact-attempt
observation. They do not by themselves establish meaning, acknowledgement,
intent, attack, coupling or causality.

---
### 10.8 R-family boundary

`R_full` is a family label for the relational / Full branch, not a single
scalar, operator, projection or independently aggregable layer.

Therefore there is no canonical generic `R_fullΣ` or `R_fullΣ(Hangar)` in
v3.50. Aggregation must be resolved through the concrete branch that is being
observed.

Current or research-facing branch-specific examples include:

```text
R0Σ
IK_relΣ
R_geomΣ
R_paceΣ
future signal-media Sigma views where explicitly defined
```

and their corresponding Hangar views:

```text
R0Σ(Hangar)
IK_relΣ(Hangar)
R_geomΣ(Hangar)
R_paceΣ(Hangar)
future signal-media Hangar views where explicitly defined
```

Relevant metrics:

```text
branch-specific drift
branch-specific acceleration
window stability
dyadic or n-adic dispersion
```

Use case:

The Hangar may compare branch-specific relational patterns across windows,
sessions or participant constellations. It must not collapse the R-family back
into a generic combined resonance score unless a separate, explicitly versioned
composition function has been defined.

---

## 11. Why Sigma Is Selected Rather Than Enabled Everywhere

The five base operators `K`, `S`, `O`, `D` and `I` construct the complete
source-local state vector `Z` where all five are applicable. Their individual
Sigma and Hangar views can be useful diagnostics:

```text
K_AΣ, S_AΣ, O_AΣ, D_AΣ, I_AΣ
```

Examples include context loss, structural decay, grounding drift,
signal-density collapse and informational stagnation. Such diagnostics remain
operator-local. They are not complete `Z`, canonical `IK`, a relational
projection or an R-family result.

There is no universally mandatory first aggregation set. Selection follows the
question:

- use operator Sigma views when one coordinate's behavior matters;
- use `Z_AΣ` when complete source-local state movement matters;
- use `IK_AΣ` when the monadic projection matters;
- use `R0Σ` when relational applicability or gate stability matters;
- use branch-specific relational Sigma views only after applicable `R0` and
  only where that branch has its own complete basis.

Do not implement a generic `RΣ` or `RΣ(Hangar)` as though the R-family were one
scalar. Aggregation must remain branch-specific.

---
## 12. Minimal Matrix

| Layer or branch | Cardinality | Sigma / Hangar role | Current boundary |
|---|---|---|---|
| `K/S/O/D/I` | monadic, source-attributed | optional coordinate diagnostics | active where selected |
| `Z` | monadic | state-trajectory windows and distributions | active |
| `IK` | monadic | projection windows and distributions | active where selected |
| `R0` | relational gate | applicability and gate-stability windows | active research material |
| `IK_rel` | relational | relational-projection windows | active research material after applicable `R0` |
| `R_geom` | dyadic / n-adic | branch-specific geometric distributions | staged; basis pending |
| `R_pace` | dyadic / n-adic | branch-specific pacing distributions | staged optional; basis pending |
| signal-media views | source-local or relational as declared | medium-specific distributions | future research |

Every Delta, Delta2, Sigma or Hangar view requires its own comparable index,
profile, applicability set and provenance.

---

## 13. Bounded Examples

### Human and chatbot

Human `A` submits a question and chatbot `B` answers. The roles reverse in the
next contribution, but the entity labels do not. The Hangar may store
source-attributed `Z_A(k_A)` and `Z_B(k_B)` trajectories, their monadic
projections and—only after explicit pairing and applicable `R0`—typed
relational observations. The shared chat is a context container. It is neither
a mixed `Z_AB` nor a store of merged inner states.

### Unknown Morse-like signal

An Observer detects a recurring pulse pattern from source `A`. Before its
meaning is known, the Hangar may retain attributable events, recurrence,
signal density, segmentation hypotheses and source-local trajectory views.
Repeated structure can make an otherwise unfamiliar carrier visible and may
support anomaly detection or the hypothesis of a contact attempt.

If source `B` replies with a similarly structured pattern, the two trajectories
remain separate. A declared pairing may permit `R0` evaluation and later
branch-specific research views. Matching signs or timing do not by themselves
prove acknowledgement, shared convention, hostile intent, successful decoding,
coupling or causality. The security value lies precisely in retaining the
observable pattern without pretending that its meaning is already known.

---
## 14. Canonical Summary

The five operators construct one complete source-local observable state vector
`Z` where all five coordinates are applicable.

`Z_A` supports monadic `IK_A` and contributes to trajectory `T_A`. Relational
observation uses distinguishable trajectories plus explicit pairing or
constellation metadata. `R0` gates separate parallel branches; it does not turn
them into one chain.

Sigma is needed wherever single-turn values are insufficient.

Sigma(Hangar) is needed wherever the distribution of trajectories, windows or interaction patterns becomes relevant.

Drift is needed to observe movement.

Acceleration is needed to observe changing movement and early instability.

The operators themselves may receive diagnostic Sigma variants when a use case
requires them. No aggregation layer is enabled merely because it exists;
selection follows the declared question and branch basis.

---

## 15. Compact Canonical Topology

```text
Monadic A:
e_A(k_A) -> K_A/S_A/O_A/D_A/I_A -> Z_A(k_A) -> IK_A(k_A)
                                      |
                                      +--> T_A

Monadic B:
e_B(k_B) -> K_B/S_B/O_B/D_B/I_B -> Z_B(k_B) -> IK_B(k_B)
                                      |
                                      +--> T_B

Relational:
T_A, T_B, pi(j), profiles
        -> R0(j)
             +--> IK_rel(j)
             +--> R_geom(j)   [staged]
             +--> R_pace(j)   [staged, optional]
             +--> signal-media views [future]

Typed views selected per layer or branch:
Delta / Delta2 / Sigma / Hangar
```

---
## 16. One-Line Principle

The operators measure source-attributed coordinates.  
`Z` is the complete monadic state vector where all five coordinates apply.  
`IK` is a monadic projection.  
`R0` opens methodically applicable relational observation.  
`IK_rel`, `R_geom` and `R_pace` are separate parallel relational branches.  
KSODI-Full is a family label, not a single scalar score.  
Sigma aggregates declared typed windows.  
Hangar views compare compatible attributable distributions.  
Drift shows movement inside one comparable sequence.  
Acceleration shows that this movement is changing.
