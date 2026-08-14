# KSODI Hangar, Sigma, Drift and Point Clouds

**Status:** public v3.50 reference release; private canonical workbench origin retained, released after Fable Hangar note and Anne's 2026-07-21 public-release decision
**Scope:** KSODI Standard-Eval and KSODI Full  
**Visibility:** public reference; private canonical workbench origin retained  

---

## 1. Purpose

This note defines where Sigma, Sigma(Hangar), Drift and Drift Acceleration are methodically useful within the KSODI architecture.

KSODI does not only observe isolated interaction states. It observes how interaction states move, stabilize, diverge or become unstable over time.

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

The word "Hangar" comes from Anne's empirical working language. The image is
useful because interaction traces can be treated like trajectories that enter
an observation space, are compared, maintained as evidence and later evaluated
against corridors.

The metaphor has a strict boundary.

An entity may internally process ideas, memories, intentions or impressions in
ways that are fluid and not directly observable. KSODI does not claim access to
that inner space.

The canonical KSODI Hangar is the observer-side counterpart: it stores and
compares traces of what has actually become externally observable.

```text
KSODI observes runway traffic, never the inside of the hangar.
```

The transient Handshake / interaction space between participants belongs to
the interaction process. It is not the canonical Hangar. `R0` opens relational
observation of a declared constellation; it does not establish coupling.

Individual signals may remain attributable to their emitting side. Across a
sufficiently long and stable interaction, their reciprocal ordering may form a
shared observable relational pattern. Strong coupling requires sustained high
`IK_rel` together with sustained high branch-specific R-family evidence under
a declared policy. The resulting relational ordering belongs to the shared
observable interaction space and cannot be reduced to either participant alone.

The Hangar preserves comparable traces, windows, trajectories and distributions
after interaction has produced observable signals. In turn-taking, the receiver
of one contribution may become the next sender, but the Hangar does not merge
the participants' inner processing spaces, thoughts or internal states.

For the formal Handshake and coupling boundary, see
[`R0_Relational-Gate.md`](./KSODI-Full/Full_v350/layer-4-r0-gate/R0_Relational-Gate.md).

---

## 2. Simple and Complex Observation Views

KSODI distinguishes between human-readable projection views and richer
machine-readable observation spaces.

Human-readable views may use:

```text
Z(t)
IK(t)
IK_rel_axis(t)
R_geom_axis(t)
R_pace(t)
```

These views support explanation, dashboards, corridor monitoring and
responsible review.

Machine-side analysis may keep the richer vector, trajectory and point-cloud
structure:

```text
Z(t), Delta Z(t), Delta2 Z(t)
G_rel(t), IK_rel_cloud(W)
G_geom(t), R_geom_cloud(W)
G_pace(t), R_pace_cloud(W)
```

This is not a loss of precision. It is a separation of views:

- simple projections for human readability,
- complex vectors and point clouds for deeper analysis,
- Hangar distributions for comparison across windows, sessions or agent
  constellations.

---

## 3. Core distinction

KSODI separates two analytical branches after the state vector Z.

```text
K/S/O/D/I
   ↓
Z(t)
   ↓
ΔZ / Δ²Z
   ├──────────────→ IK branch
   │                 IK
   │                 ΔIK / Δ²IK
   │                 IKΣ
   │                 IKΣ(Hangar)
   │
   └──────────────→ relational branch / KSODI Full
                     R₀
                     IK_rel
                     R_geom
                     R_pace
                     future signal-media extension
                     RΣ
                     RΣ(Hangar)
```

The IK branch observes monadic projection and coherence dynamics.

The relational branch first observes dyadic or n-adic comparability and
relational projection. Later R-family layers may observe trajectory coupling
where their own branch definitions are released.

KSODI Full denotes the relational and resonance observation family. It is not a single scalar score.

The branch begins with
[`R0`](./KSODI-Full/Full_v350/layer-4-r0-gate/R0_Relational-Gate.md),
because R₀ checks whether two or more monadic trajectories can meaningfully be
related at all.

In this note, `RΣ` and `RΣ(Hangar)` are generic R-family Sigma labels. They do
not introduce a separate active v3.50 Sigma layer. In concrete v3.50 files, the
R-family Sigma view must be named by its branch, for example `R_geomΣ` /
`R_geomΣ(Hangar)` or `R_paceΣ` / `R_paceΣ(Hangar)` where pacing dynamics are
explicitly defined.

---

## 4. Monadisch vs dyadisch

The following layers are monadic:

```text
K/S/O/D/I → Z → IK
```

This means they can be calculated for one interaction sequence, one agent, one participant or one observed trajectory.

The following layers are dyadic or potentially n-adic:

```text
R₀ → IK_rel → R_geom → R_pace → future signal-media extension → RΣ → RΣ(Hangar)
```

They require at least two trajectories or two distinguishable interaction participants, for example:

```text
Z_A(t), ΔZ_A(t)
Z_B(t), ΔZ_B(t)
```

R₀ is the methodological gate between monadic and dyadic analysis.

IK_rel must not be evaluated before R₀. It is a relational projection layer that becomes methodically valid only after R₀ has established that a dyadic comparison is meaningful.

---

## 5. What Sigma means

Sigma indicates aggregation across an observation window.

A single value describes one point in time:

```text
Z(t)
IK(t)
R(t)
```

A Sigma value describes a window:

```text
ZΣ(W)
IKΣ(W)
RΣ(W)
```

where W is a defined observation window.

Here `RΣ(W)` is only a family-level placeholder for branch-specific relational
aggregations such as `R_geomΣ(W)` or `R_paceΣ(W)`. The implementation or
release file must use the branch-specific name.

Where applicability masks are used, a Sigma value must declare the active
window policy:

```text
W_app = {t in W | the relevant value is applicable under the declared policy}
applicability_rate(W) = |W_app| / |W|
```

Masked or applicability-aware window views must be named and must not be
presented as full-window values.

Sigma is useful when single-turn values are not sufficient. It shows whether a sequence stabilizes, drifts, oscillates, collapses, converges or develops recurring patterns.

Sigma does not automatically mean improvement. It only means aggregation over time.

---

## 6. What Sigma(Hangar) means

Sigma(Hangar) describes the distribution of aggregated values inside a comparison or observation space.

A Hangar may contain:

```text
{ Z(t) | t ∈ W }
{ IK(t) | t ∈ W }
{ R(t) | t ∈ W }
```

or aggregated window objects:

```text
{ ZΣ(W_i) }
{ IKΣ(W_i) }
{ RΣ(W_i) }
```

Sigma(Hangar) is useful when we no longer ask only:

```text
What is the current value?
```

but instead:

```text
Where does this interaction pattern sit inside the observed space?
How stable is the distribution?
Does the trajectory remain inside an expected corridor?
Does it move toward another cluster?
Does it show dispersion, compression or abnormal acceleration?
```

The Hangar therefore allows comparison, monitoring, anomaly detection and later governance-oriented observation without treating single outputs as isolated events.

---

## 7. Drift and acceleration

Drift describes movement between states.

For vector-valued quantities such as Z:

```text
ΔZ(t) = Z(t) - Z(t-1)
```

For scalar projections such as IK:

```text
ΔIK(t) = IK(t) - IK(t-1)
```

For relational or resonance values:

```text
ΔR(t) = R(t) - R(t-1)
```

Acceleration describes the change of movement:

```text
Δ²Z(t) = ΔZ(t) - ΔZ(t-1)
Δ²IK(t) = ΔIK(t) - ΔIK(t-1)
Δ²R(t) = ΔR(t) - ΔR(t-1)
```

Drift answers:

```text
Is the interaction moving?
```

Acceleration answers:

```text
Is the movement itself changing?
```

Acceleration is important because instability often becomes visible before the absolute value itself looks problematic.

A system may still appear coherent while its trajectory already accelerates away from a stable corridor.

---

## 8. Why drift is needed

Drift is needed because interaction is not static.

A single value may look acceptable while the trajectory is already moving away from stability.

Examples:

- A Z value may still be within a normal range while one operator begins to decline.
- An IK value may remain high while ΔIK shows gradual weakening.
- An R value may appear stable while the dyadic trajectories begin to lose directional coupling.

Drift makes the direction and magnitude of change observable.

---

## 9. Why acceleration is needed

Acceleration is needed because gradual drift and sudden instability are different phenomena.

A small but increasing drift may indicate early instability.

A stable value with rising acceleration may indicate that the system is about to change phase.

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

ZΣ and ZΣ(Hangar) show whether the observable interaction state remains stable, disperses, compresses or drifts across time.

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

IKΣ and IKΣ(Hangar) show whether monadic interaction coherence remains stable over time.

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

IK_relΣ and IK_relΣ(Hangar) show whether two trajectories remain structurally relatable over time.

They must be interpreted together with R₀ gate status. A high IK_relΣ over a very low applicability rate is not equivalent to stable relational coherence across the full window.

---

### 10.4 R₀

R₀Σ is useful.

R₀Σ aggregates minimal dyadic stability checks over a window.

R₀Σ(Hangar) may be useful.

It shows whether dyadic comparability itself remains stable across interaction windows or participant pairs.

Relevant metrics:

```text
ΔR₀
Δ²R₀
dyadic stability drift
threshold crossings
```

Use case:

R₀Σ shows whether dyadic analysis remains methodically justified over time.

---

### 10.5 R_geom

R_geomΣ is useful.

R_geomΣ aggregates geometric dyadic or n-adic coupling over time.

R_geomΣ(Hangar) is useful.

It shows how geometric coupling patterns distribute across interaction windows, participant pairs or agent constellations.

For point-cloud analysis, `R_geom_cloud(W)` stores geometric coupling vectors
over an observation window.

Relevant metrics:

```text
ΔR_geom
Δ²R_geom
C_prox
C_dir
C_resp
C_bal
R_geom_axis
geometric coupling drift
directional consistency
corridor movement
```

Use case:

R_geomΣ and R_geomΣ(Hangar) show whether the geometric coupling between trajectories stabilizes, weakens, shifts or drifts jointly into an unexpected corridor.

High R_geom is not automatically desirable. It may indicate strong coupling even when two trajectories move together in an unwanted direction. Therefore R_geom must be interpreted together with Z, IK, IK_rel, drift, acceleration and Hangar corridors.

---

### 10.6 Future Signal-Media Extension

Frequency, rhythm, voice, radio, Morse, waveform or other signal-media
features are not active v3.50 core terms.

Earlier work used labels such as `R_takt`, `R_freq` or `V(t)` for mixed
frequency, rhythm, voice, takt or timing overlays. In the current v3.50 line,
these belong to future signal-media / Layer-8 research unless a concrete
application profile explicitly defines them.

Future signal-media Sigma or Sigma(Hangar) variants may be useful when such
features are consistently measured across windows, sessions or participant
constellations.

Relevant metrics:

```text
frequency drift
rhythm stability
waveform or signal-media drift
turn-timing asymmetry
```

Use case:

Future signal-media Hangar views may show whether timing, rhythm, voice,
radio, Morse or waveform-related interaction traces remain coupled or begin to
desynchronize. They are not part of the active v3.50 Standard-Eval release.

---

### 10.7 R_pace

R_paceΣ is useful when pacing dynamics are measured consistently.

R_paceΣ aggregates pacing, lag, lead, timing asymmetry or rhythm changes over time.

R_paceΣ(Hangar) may be useful when pacing patterns are compared across windows, sessions or participant constellations.

For point-cloud analysis, `R_pace_cloud(W)` stores pacing, lag, lead or
timing-asymmetry vectors over an observation window.

Relevant metrics:

```text
ΔR_pace
Δ²R_pace
pacing stability
oscillation
desynchronization
```

Use case:

R_paceΣ and R_paceΣ(Hangar) show whether interaction timing remains paced, begins to lag, leads, oscillates or desynchronizes.

`R_phase`, `R_struc`, `R_struct`, `R_takt`, `R_freq` and `V(t)` are not active
v3.50 terms. Earlier versions mixed geometric orientation, structural relation,
temporal phase, lag, lead, rhythm and voice overlays. Current terminology keeps
geometry in `R_geom`, readable pacing dynamics in `R_pace`, and signal-media
extensions in future Layer-8 work.

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

## 11. Why Sigma is not required for the five base operators at first

The five base operators K, S, O, D and I are primarily used to construct Z.

They can theoretically be aggregated individually:

```text
KΣ, SΣ, OΣ, DΣ, IΣ
```

This may later be useful for diagnostics, for example:

- context loss over time,
- structural decay,
- grounding drift,
- discernibility / signal-density collapse,
- informational stagnation.

However, in the current v3.50 architecture, operator-level Sigma views are
optional diagnostics selected per use case. They are present as reminders in
the operator files, but they are not the primary aggregation layer for every
application.

The first stable aggregation layers should be:

```text
ZΣ
IKΣ
IK_relΣ
RΣ
```

In this compact list, `RΣ` means the R-family aggregation slot. It must be
resolved into branch-specific names such as `R_geomΣ` and, where applicable,
`R_paceΣ` before implementation or formal release wording.

The reason is methodological discipline.

The operators are measurement components.  
Z is the first complete interaction state.  
IK and R are the first higher-order analytical branches.

Operator-level Sigma may be used as diagnostic detail where the application
needs it, but it should not be treated as the central architecture in every
v3.50 deployment.

---

## 12. Minimal matrix

| Layer | Monadisch / dyadisch | Sigma useful | Sigma(Hangar) useful | Drift useful | Acceleration useful |
|---|---|---:|---:|---:|---:|
| K/S/O/D/I | monadic components | later optional | later optional | optional diagnostics | optional diagnostics |
| Z | monadic | yes | yes | yes | yes |
| IK | monadic | yes | yes | yes | yes |
| R₀ | dyadic gate | yes | maybe / yes | yes | yes |
| IK_rel | dyadic / relational | yes | yes | yes | yes |
| R_geom | dyadic / n-adic | yes | yes | yes | yes |
| future signal-media extension | dyadic / n-adic or signal-specific | research | research | research | research |
| R_pace | dyadic / n-adic timing | yes | maybe / yes | yes | yes |
| R-family branch | dyadic / n-adic | branch-specific only | branch-specific only | branch-specific only | branch-specific only |
| RΣ | dyadic / n-adic aggregation | already Sigma | yes | yes | yes |
| RΣ(Hangar) | dyadic / n-adic distribution | already Sigma(Hangar) | yes | yes | yes |

---

## 13. Canonical summary

The five operators construct the observable state vector Z.

Z enables two branches:

1. The IK branch observes monadic coherence projection.
2. The KSODI Full relational branch observes dyadic or n-adic comparability,
   relational projection and, in later R-family layers, trajectory coupling.

Sigma is needed wherever single-turn values are insufficient.

Sigma(Hangar) is needed wherever the distribution of trajectories, windows or interaction patterns becomes relevant.

Drift is needed to observe movement.

Acceleration is needed to observe changing movement and early instability.

The operators themselves may receive diagnostic Sigma variants when a use case
requires them, but the current primary aggregation layers begin at Z, IK,
IK_rel and the KSODI Full relational family.

---

## 14. Compact canonical formula

```text
Operators:
K/S/O/D/I → Z(t)

Monadic branch:
Z(t) → IK(t) → ΔIK / Δ²IK → IKΣ → IKΣ(Hangar)

Trajectory branch:
Z_A(t), Z_B(t), ΔZ_A(t), ΔZ_B(t)
   → R₀
   → IK_rel
   → R_geom
   → R_pace
   → future signal-media extension
   → RΣ
   → RΣ(Hangar)
```

---

## 15. One-line principle

The operators measure components.  
Z is the first complete state.  
IK is monadic projection.  
R₀ opens relational analysis.  
IK_rel and R belong to the dyadic branch.  
KSODI Full / R-family is the label for relational and resonance observation,
not a single scalar score.
Sigma aggregates windows.  
Sigma(Hangar) compares distributions.  
Drift shows movement.  
Acceleration shows that the movement itself is changing.
