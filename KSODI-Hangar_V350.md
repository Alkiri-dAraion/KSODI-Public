# KSODI Hangar, Sigma, Drift and Point Clouds

**Scope:** KSODI Standard-Eval and KSODI-Full Observer views  
**Filename marker:** `_V350` denotes KSODI v3.5 / v3.50

Authority: this note governs cross-layer Sigma/Hangar interpretation only.
The released Layer 1–5 method files remain authoritative for formulas, result
types, gates, windows and component contracts.

---

## 1. Purpose

This note defines where Sigma, Sigma(Hangar), Drift and Drift Acceleration are
methodically useful and which comparability, typing and provenance constraints
their cross-layer use must preserve.

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

The longer origin image, aircraft/tool analogy and its methodological limits
are documented separately in the
[KSODI Hangar Origin and Analogy Companion V350](./KSODI-Hangar_Origin-and-Analogy-Companion_V350.md).
That companion is explanatory; this file and the versioned layer methods retain
formal authority.

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
the interaction process. It is not the canonical Hangar. `R0` records whether
the declared constellation is eligible for a separately defined relational
observation under the selected gate contract; it does not establish coupling.

Individual signals retain their declared stable or provisional source
attribution; an emitting entity is recorded only when established. Across a
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
and an open numeric `R_0` gate under the exact contract required by the
downstream branch. Current `IK_rel` additionally requires the same ordered
dyad, paired member events, pairing map and relational step in an open numeric
canonical complete dyadic `R_0` result under the exact required profile.

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
event. In the following illustration only, `Phi` names the coordinate assembly
map; it is not an additional canonical v3.50 method symbol:

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

One source-attributed event whose five aligned coordinate results are numeric
produces one complete observable point in `[0,1]^5`. A sequence of comparable
complete points from the same declared trajectory produces a path. Several
trajectories or observation windows may form point clouds. Typed non-complete
records remain observable records but do not become five-dimensional numeric
points. The Hangar is the Observer-side comparison view for these attributable
points, paths, windows and distributions.

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

If one or more operator coordinates are non-numeric—including `not_selected`,
`not_observable` or `not_applicable`—they must not be replaced by zero. The
resulting record is typed partial / `not_complete`, not a complete point in the
five-dimensional hypercube. Complete Z requires all five coordinates to be
aligned and numeric.

For the cross-layer source-attribution and implementation boundary, see
[KSODI Implementation Guardrails](./IMPLEMENTATION_GUARDRAILS.md).

## 2. Simple and Complex Observation Views

KSODI distinguishes human-readable projections from richer machine-readable
observation objects. Every view retains its entity or trajectory identity,
profile, typed status/eligibility and index kind.

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
P_rel,AB(j) = (T_G, numeric components, IK_rel result, gate record)
IK_rel_cloud(W_AB)
branch-specific geometric or pacing feature records [staged]
```

The retired unlabeled active-vector form `G_rel_active` and event-wise
renormalized relational axes are not current v3.50 structures. `T_G` retains
all component statuses; a released extended IK_rel profile uses one fixed N.

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
typed Z movements and an explicit pairing or constellation satisfy the
declared availability, comparability and bounded-drift contract.

After an open numeric `R0` under the exact contract required by the downstream
method, `IK_rel`, `R_geom` and `R_pace` are parallel relational research
branches. Current IK_rel requires the exact compatible open numeric canonical complete
dyadic gate; Layer 6 and later remain staged and do not acquire a gate or
formula from this note. No branch is automatically the numeric input of
another. Every branch requires its own complete basis, profile and
applicability rules.

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

Where typed result states or derived numeric-availability masks are used, the
Sigma view declares its status, fixed basis and coverage policy. The following
is explanatory schema, not a replacement for layer-specific names:

```text
T_X(q) = common typed result status at q
W_numeric,X = {q in W_X | T_X(q) = numeric under profile p_X}
coverage_numeric,X(W_X) = |W_numeric,X| / |W_X|
```

Canonical reporting uses the names and eligibility sets of the governing
method: Layer-1 operator windows retain their typed static/Delta/Delta2
subsets; Z reports `complete_rate_Z` and per-coordinate `numeric_rate_X`; IK
reports `coverage_IK`; R0 reports `coverage_R0` and `gate_open_rate`; IK_rel
reports `coverage_rel`, `gate_open_rate` and `static_rate`. Identically named
rates in different layers still retain their own declared numerator,
denominator and eligibility rule.

For Z, the mandatory coordinate-status vector `T_Z` remains authoritative and
the binary `A_Z` numeric-availability mask is derived from it. It is not an
applicability policy. A mask cannot distinguish
`not_selected`, `not_observable` and `not_applicable`.

Here `q` is the already declared index type for `X`; it is not a new universal
time index. A complete Z window uses a shared complete basis. A reduced Z
window declares one fixed non-empty component set `M` for the whole window;
an eventwise `A_Z` must not silently generate a changing basis. Partial Z
points must be stratified by their exact status profile and must not be
zero-filled into the complete five-dimensional Hangar space.

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
H_IK_rel(W_AB | p_rel) = {IK_rel_AB(j) | j in W_AB^rel}
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
- evaluation profile, fixed basis, typed status vector and derived
  numeric-availability mask;
- whether it contains single values, trajectories, window aggregates or
  feature-cloud objects.

Every point-cloud distance, clustering rule, corridor and anomaly threshold
must be declared and versioned. No universal Hangar metric or corridor is
defined by the existence of the view.

Hangar records may remain personal, confidential, copyrighted, identifiable
or linkable even without raw interaction text. Retention, access, purpose and
deletion policies therefore apply to derived distributions and pairing maps as
well as to their source records.

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

For a released relational branch value `X_b` after the exact open `R0`
contract required by that branch:

```text
Delta X_b(j) = X_b(j) - X_b(j - 1)
X_b = IK_rel in current public v3.50
```

The same typed pattern may be adopted by a later released `R_geom` or
`R_pace` contract, but this note does not activate those calculations.

The two relational evaluations must use a comparable pairing policy, profile
and branch basis. Current `IK_rel` is strictly dyadic and requires its
same-pairing exact open numeric canonical complete dyadic `R0` under the
required profile; a reduced-R0 opening does not authorize it. `R_geom` and
`R_pace` remain staged and require their own later branch contracts.
`Delta R0` uses only consecutive comparable numeric R0 values. Transitions
among `open`, `closed` and `not_evaluable` are categorical events, not numeric
deltas.

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

Aggregate or projected stability is therefore not evidence that every basis
operator is healthy. Retain the source-attributed `K/S/O/D/I` traces and their
typed statuses: one coordinate may deteriorate while `Z`, `IK` or a window
aggregate still appears stable.

Examples:

- A Z value may still be within a normal range while one operator begins to decline.
- An IK value may remain high while ΔIK shows gradual weakening.
- A branch-specific relational value may appear stable while its declared trajectory relation or feature distribution begins to change.

Drift makes the direction and magnitude of change observable.

---

## 9. Why acceleration is needed

Acceleration is needed because gradual drift and sudden instability are different phenomena.

A small but increasing drift may indicate early instability.

A stable value with increasing scalar acceleration magnitude may indicate an
approaching transition candidate in the observed regime.

For a signed scalar coordinate or projection, strong negative acceleration may
mark a transition candidate requiring interpretation under the relevant layer,
branch and application profile. A vector such as `Delta2 Z` has no single
global negative direction until a component, projection or directional
functional is declared. Neither case by itself establishes collapse, loss of
grounding, loss of pacing or semantic divergence.

Acceleration can therefore contribute to an explicitly governed warning
profile.

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

#### Typed IK distribution boundary

IK-related Hangar records must be stratified by canonical versus reduced
projection, IK profile and version, source/context scope and window policy.
Every reduced record additionally discloses one fixed active coordinate set M
and retains the originating `T_Z`.

Canonical IK, different `IK^[M]` views, changing axes and non-numeric statuses
must not be pooled into one unlabeled numeric distribution. Coverage and typed
status counts accompany every aggregate. A Hangar distribution distance is a
non-negative distribution diagnostic; it is not the signed source-local
`Delta IK`.

---

### 10.3 IK_rel

IK_relΣ is useful.

IK_relΣ aggregates relational coherence over the numeric comparable subset
`W_AB^rel` after the same-pairing exact open numeric canonical complete dyadic
R₀ gate required by the released IK_rel profile.

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
coverage_rel
gate_open_rate
typed status counts
gate-closure frequency
```

Use case:

`IK_relΣ` and its compatible Hangar views show how the declared relational coherence projection behaves across comparable paired evaluations.

They must be interpreted together with R₀ gate status. A high IK_relΣ over
low `coverage_rel` or a low `gate_open_rate` is not equivalent to stable
relational coherence across the full window. Report typed status counts
separately so that numeric availability, gate eligibility and
`not_applicable` are not collapsed into one rate.

#### Typed IK_rel distribution boundary

IK_rel Hangar records remain observer-side relational distributions, not a
merged inner Hangar of A and B. Partition them by ordered dyad, pairing policy,
R0 profile, shared monadic IK profile, IK_rel profile and fixed relational
component set N.

Store `gate_open_rate`, `coverage_rel`, `static_rate` and typed IK_rel /
component-status counts beside every aggregate. Do not pool changing N,
changing axes, changing pairings or non-numeric statuses into one numeric
cloud. Distribution distance remains distinct from signed relational-index
`Delta IK_rel`.

---

### 10.4 R₀

R₀Σ is useful.

`R0Σ` aggregates comparable gate evaluations over a declared relational window and policy.

R₀Σ(Hangar) may be useful.

It shows how numeric R0 results and their separate gate states vary across
compatible pairing windows or declared constellations.

Relevant metrics:

```text
ΔR₀
Δ²R₀
dyadic stability drift
threshold crossings
```

Use case:

`R0Σ` shows `coverage_R0` and gate behavior across the declared pairing
window. Numeric evaluability, an open gate and downstream relational evidence
remain distinct. It does not establish coupling or semantic agreement.

#### Typed R0 distribution boundary

R0 Hangar records are derived gate distributions, not relational proof and not
a shared inner state. Partition them by dyad/constellation, pairing or member
map, complete versus fixed-M profile, norm, trajectory aggregation, weights,
threshold and window policy.

Store `coverage_R0`, typed R0 result-status counts,
open/closed/not-evaluable gate-state counts, per-trajectory drift and
asymmetry summaries. Do not pool
complete R0 with different `R0^[M]` views or allow non-numeric steps to vanish
silently. Distribution distance is not signed relational-index `Delta R0`.

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
source-local state vector `Z` where all five are aligned and numeric. Their individual
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
- use `R0Σ` when numeric R0 values, coverage and separate gate-state behavior
  matter;
- use branch-specific relational Sigma views only after the exact open `R0`
  contract required by that branch and only where that branch has its own
  complete basis; current `IK_rel` requires its same-pairing exact open numeric
  canonical complete dyadic `R0` under the required profile.

Do not implement a generic `RΣ` or `RΣ(Hangar)` as though the R-family were one
scalar. Aggregation must remain branch-specific.

---
## 12. Minimal Matrix

| Layer or branch | Cardinality | Sigma / Hangar role | Current boundary |
|---|---|---|---|
| `K/S/O/D/I` | monadic, source-attributed | optional coordinate diagnostics | active where selected |
| `Z` | monadic | state-trajectory windows and distributions | active |
| `IK` | monadic | projection windows and distributions | active where selected |
| `R0` | dyadic or n-adic relational gate | evaluability and gate-state windows | public v3.50 method; Hangar view selected where needed |
| `IK_rel` | strictly dyadic | relational-projection windows | public v3.50 method after its exact compatible open canonical complete dyadic `R0` |
| `R_geom` | cardinality defined only by a later profile | branch-specific geometric distributions | orientation only; no public method definition |
| `R_pace` | cardinality defined only by a later profile | branch-specific pacing distributions | orientation only; no public method definition |
| signal-media views | source-local or relational as declared | medium-specific distributions | orientation only; no defined public method architecture |

Every Delta, Delta2, Sigma or Hangar view requires its own comparable index,
profile, fixed basis or component contract, typed eligibility/status and
provenance.

---

## 13. Bounded Examples

### Human and chatbot

Human `A` submits a question and chatbot `B` answers. The roles reverse in the
next contribution, but the entity labels do not. The Hangar may store
source-attributed `Z_A(k_A)` and `Z_B(k_B)` trajectories, their monadic
projections and—for current `IK_rel`, only after explicit dyadic pairing and
the same-pairing exact open numeric canonical complete dyadic `R0` under the
required profile—typed relational observations. The shared chat is a context
container. It is neither
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
`Z` exactly where all five coordinates are aligned and numeric. Any
non-numeric coordinate yields a typed partial / `not_complete` record instead.

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
             +--> IK_rel(j)  [only under its exact compatible open gate]
             +--> R_geom(j)   [staged]
             +--> R_pace(j)   [staged, optional]
             +--> signal-media views [future]

Typed views selected per layer or branch:
Delta / Delta2 / Sigma / Hangar
```

---
## 16. One-Line Principle

The operators measure source-attributed coordinates.  
`Z` is the complete monadic state vector where all five coordinates are
aligned and numeric.
`IK` is a monadic projection.  
`R0` records a typed gate result and, where a valid result exists, its separate
open/closed/not-evaluable gate state.
`IK_rel` is the current strictly dyadic branch after its same-pairing exact
open numeric canonical complete dyadic `R0`; `R_geom` and `R_pace` are separate
staged relational branches.
KSODI-Full is a family label, not a single scalar score.  
Sigma aggregates declared typed windows.  
Hangar views compare compatible attributable distributions.  
Drift shows movement inside one comparable sequence.  
Acceleration shows that this movement is changing.
