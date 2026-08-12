# KSODI IK_rel - Relational Coherence Projection v3.50

Status: public v3.50 reference release; private canonical workbench origin
retained. Released after the 2026-07-31 FABLE formal pass, the 2026-08-01
VSELKIM fix pass, the 2026-08-12 pre-gate observation clarification and Anne's
public Layer-5 release decision.

Layer: relational projection branch after stable `R0`.

## 1. Definition

`IK_rel` describes relational coherence between distinguishable trajectories after `R0` has opened relational comparability.

`IK` is monadic. `IK_rel` is relational.

`IK_rel` asks whether the coherence movements of distinguishable trajectories remain compatible.

It does not ask whether each trajectory is internally coherent. That is the role of `IK`.

It does not ask whether trajectories are geometrically coupled in the full resonance sense. That belongs to the R_full family, especially `R_geom`.

`IK_rel` is not a truth, quality, utility, compliance, safety or alignment score.

## 2. Gate Rule

`IK_rel` must not be evaluated before `R0`.

Canonical rule:

```text
IK_rel is observable only if R0 is stable enough.
```

Operational form:

```text
if R0(t) >= theta_R0_stable:
    IK_rel(t) may be evaluated
else:
    IK_rel(t) = not_applicable
```

This prevents KSODI from assigning relational coherence where no stable shared movement basis has been established.

Pre-gate observation boundary:

The `R0` gate does not forbid monadic parallel observation. An observer may
always compute and inspect `IK_A(t)`, `IK_B(t)`, `Delta IK_A(t)` and
`Delta IK_B(t)` as separate monadic trajectories under their own applicability
rules.

The gate only forbids turning their scalar distance or movement comparison into
a relational compatibility signal before stable relational comparability has
been established. Placing two high or stable `IK` curves side by side is
observation; reporting `C_ik_gap(t)`, `C_ik_move(t)` or `IK_rel(t)` as
relationship evidence is relational interpretation and requires `R0`.

## 3. Architectural Position

```text
Z_A(t), Z_B(t)
Delta Z_A(t), Delta Z_B(t)
   |
   v
R0(t) gate
   |
   +--> if stable:
          IK_A(t), IK_B(t)
          Delta IK_A(t), Delta IK_B(t)
             |
             v
           IK_rel(t)
           G_rel(t)
           IK_rel_axis(t)
           Delta IK_rel / Delta2 IK_rel
           IK_relSigma
           IK_relSigma(Hangar)
```

`R0` is evaluated from distinguishable `Z` trajectories and their movement, not
from `IK_A` / `IK_B`. The monadic `IK` projections and their deltas become
inputs for `IK_rel` only after the `R0` gate has opened relational
comparability.

For n-adic systems, `A` and `B` generalize to a set of trajectories:

```text
{Z_j(t) | j = 1...n}
```

v3.50 defines `IK_rel` formally for the dyadic case. The n-adic extension
(pairwise component matrices over the shared applicability intersection and an
explicit aggregation policy) is Future Work and is not released by this file.

The core description is architecture-agnostic. It may apply to human-machine interaction, multi-agent systems, robots interacting with environments, or other distinguishable entities whose interaction states can be represented in KSODI state space.

## 4. Input Data

For the dyadic case:

```text
R0(t)
theta_R0_stable
IK_A(t)
IK_B(t)
Delta IK_A(t)
Delta IK_B(t)
optional Delta2 IK_A(t)
optional Delta2 IK_B(t)
```

Required metadata:

- `trajectory_ids`
- `context_scope_id`
- operator version IDs
- `ik_config_id`
- `r0_config_id`
- optional `ik_rel_axis_config_id`
- gate status
- eval-unit pairing policy
- zero-movement policy ID
- `epsilon_move`
- `min_components_rel`
- `C_shared` activation status and config ID if active

No raw text is required after `Z` and `IK` have been calculated.

## 5. Projection Distance

A simple relational distance between monadic projections is:

```text
deltaIK_AB(t) = |IK_A(t) - IK_B(t)|
```

This captures the gap between the two projection values.

It is useful but insufficient. Two trajectories may have similar `IK` values while moving in incompatible directions.

## 6. Minimal Relational Movement Definition

Because `IK(t) in [0,1]`, first differences satisfy:

```text
Delta IK(t) in [-1,1]
```

Therefore the absolute difference of two projection movements can lie in `[0,2]` and must be normalized before being converted into a compatibility value.

Raw movement gap:

```text
move_gap_raw(t) = |Delta IK_A(t) - Delta IK_B(t)|
```

Normalized movement compatibility:

```text
C_ik_move(t) = clip(1 - move_gap_raw(t) / 2, 0, 1)
```

Minimal definition:

```text
IK_rel(t) := C_ik_move(t)
```

Zero-movement policy:

`C_ik_move(t)` compares movements and is informative only where movement exists.
With a declared threshold `epsilon_move >= 0` versioned in
`ik_rel_axis_config_id` or a dedicated policy ID:

```text
if |Delta IK_A(t)| <= epsilon_move and |Delta IK_B(t)| <= epsilon_move:
    C_ik_move(t) = not_applicable
    static_step = true
```

Since `IK_rel(t) := C_ik_move(t)`, a static step yields:

```text
IK_rel(t) = not_applicable
```

Joint stillness is not evidence of relational compatibility. It is absence of
comparable movement. A versioned alternative policy may later report static
compatibility while marking the step, but the v3.50 canonical default is
masking.

Interpretation:

| Signal | Meaning |
| --- | --- |
| `IK_rel approx 1` | coherence projections move similarly |
| `IK_rel medium` | partial relational compatibility |
| `IK_rel approx 0` | coherence projections diverge strongly |
| `not_applicable` | `R0` gate is not stable, no comparable movement exists or a required applicability policy is not met |

`IK_rel` is a relational projection-compatibility signal.

## 7. Relational Component Vector G_rel

The minimal definition observes only one relational component: movement compatibility of the monadic projections.

For longer observation, corridor discovery and visualization, `IK_rel` may also be represented as a relational component vector projected onto a versioned relational axis.

`G_rel(t)` is a relational feature vector. It preserves the component structure that may be hidden by a scalar axis projection.

It is not a language object, not a raw embedding and not a full resonance score.

For the dyadic case:

```text
C_ik_gap(t)   = clip(1 - |IK_A(t) - IK_B(t)|, 0, 1)
C_ik_move(t)  = clip(1 - |Delta IK_A(t) - Delta IK_B(t)| / 2, 0, 1)
C_ik_accel(t) = clip(1 - |Delta2 IK_A(t) - Delta2 IK_B(t)| / 4, 0, 1)
```

Range note: `Delta IK in [-1,1]` and `Delta2 IK in [-2,2]`. The movement gap
therefore lies in `[0,2]` and is normalized by 2; the acceleration gap lies in
`[0,4]` and is normalized by 4. Clipping remains defensive only.

`C_ik_accel(t)` is applicable only when both second differences are defined and comparable.

`C_shared(t)` is a reserved component slot, not active in the v3.50 default.
Activation requires its own versioned definition and config ID specifying what
compatibility it measures. Until then it is `not_applicable` and excluded from
the active set.

Active component vector:

```text
G_rel_active(t) = [C_i(t) | C_i(t) is applicable]
```

Expanded notation:

```text
G_rel(t) = [C_ik_gap(t), C_ik_move(t), C_ik_accel(t), C_shared(t)]
```

where every active `C_i(t)` must already be clipped or otherwise normalized to `[0,1]`.

If one component is `not_applicable`, remove it from the active component set and renormalize the remaining weights.

## 8. Relational Axis Projection

Define a versioned relational weight vector over active components:

```text
w_rel = [w_gap, w_move, w_accel, w_shared]
w_i >= 0
sum_i w_i = 1
```

Extended relational axis projection:

```text
active(t) = {i | C_i(t) is applicable}
IK_rel_axis(t) =
    sum_{i in active(t)} w_i * C_i(t) / sum_{i in active(t)} w_i
```

Defined only if `active(t)` is non-empty and
`sum_{i in active(t)} w_i > 0`.

Minimum-components policy:

```text
|active(t)| >= min_components_rel
min_components_rel >= 1
```

Below the declared minimum, `IK_rel_axis(t) = not_applicable`.
`min_components_rel` and `epsilon_move` belong to the comparability list.

The minimal definition in section 6 is a special case of this axis logic where only `C_ik_move(t)` is active.

Static-step clarification: during a static step, `IK_rel(t)` remains
`not_applicable` because the minimal movement signal is masked. Other active
components such as `C_ik_gap(t)` or `C_ik_accel(t)` may still be reported
through `IK_rel_axis(t)` if their own applicability policies are met. `W_app`
and `IK_rel_cloud(W)` follow the applicability of `IK_rel(t)` unless a
versioned implementation profile explicitly declares a different policy.

`w_rel` is not a final claim about the world. It is a versioned observation choice. Equal start weights may be used as a neutral workbench convention, but domain-specific weights should emerge from observation over time.

## 9. Point-Cloud View

The relational component vector should be preserved where possible:

```text
G_rel(t)
```

The scalar projection:

```text
IK_rel_axis(t)
```

is a human-readable and observer-readable view, not a replacement for the full relational vector.

For a window:

```text
IK_rel_cloud(W) = {G_rel_active(t) | t in W_app}
```

The point cloud can be observed across windows:

```text
IK_rel_cloud(W_1), IK_rel_cloud(W_2), ..., IK_rel_cloud(W_n)
```

This supports questions such as:

- Does the relational coherence cloud stay compact?
- Does it drift away from the current axis?
- Does it become wider, thinner, compressed or unstable?
- Does it move in a similar direction as `R_geom` or `R_pace`?
- Does `IK_rel` remain stable while geometric or pacing coupling changes?

The cloud image is a visualization aid, not a separate mathematical definition.

## 10. Shared Projection Set

An optional shared projection can be defined over a transient shared projection
set:

```text
H_AB(t) = {Z_A(t), Z_B(t)}
Zbar_AB(t) = mean(H_AB(t))
IK_shared(t) = w dot Zbar_AB(t)
```

Terminology note: `H_AB(t)` is a transient shared set, not a Hangar observation
space. Final naming remains subject to the ELKIM semantic pass.

Componentwise mean is taken over the shared active set:

```text
A_pair(t) = A_Z_A(t) INTERSECT A_Z_B(t)
```

Use the same minimum-components policy as `R0` for shared `Z` components. Below
the minimum, `IK_shared(t) = not_applicable`. Masked components are never
coerced.

Linear-equivalence note: under stable `w` and full shared applicability,
`IK_shared(t) = mean(IK_A(t), IK_B(t))`. In that case `IK_shared` adds no
independent information and must not be read as a new relational signal; its
value is notational and visual.

## 11. Delta IK_rel

The first difference of relational coherence is:

```text
Delta IK_rel(t) = IK_rel(t) - IK_rel(t-1)
```

It is defined only when both values are applicable:

```text
IK_rel(t) != not_applicable
IK_rel(t-1) != not_applicable
```

When the axis form is active, differences of the axis projection are named
`Delta IK_rel_axis(t)` and stored as a separate optional field.

## 12. Delta2 IK_rel

The second difference is:

```text
Delta2 IK_rel(t) = Delta IK_rel(t) - Delta IK_rel(t-1)
```

It is defined only when the required consecutive applicable values exist.

`Delta2 IK_rel` is an early-warning signal, not a judgment.

When the axis form is active, second differences of the axis projection are
named `Delta2 IK_rel_axis(t)` and stored as a separate optional field.

## 13. IK_relSigma

`IK_relSigma` aggregates relational coherence over a window after `R0` has opened the relational branch.

For a window:

```text
W = {t_1, ..., t_n}
W_app = {t in W | IK_rel(t) != not_applicable}
```

Minimal aggregation:

```text
IK_relSigma(W) = aggregate({IK_rel(t) | t in W_app})
```

Recommended aggregate functions:

- mean
- median
- percentile profile
- share of applicable steps
- share of gate closures
- point-cloud profile of `IK_rel_cloud(W)`

The applicability rate should be stored:

```text
applicability_rate(W) = |W_app| / |W|
```

This matters because a high `IK_relSigma` over very few applicable steps can be misleading.

## 14. Delta IK_relSigma and Delta2 IK_relSigma

Between ordered windows:

```text
Delta IK_relSigma(W_i) =
    IK_relSigma(W_i) - IK_relSigma(W_{i-1})
```

Second difference:

```text
Delta2 IK_relSigma(W_i) =
    Delta IK_relSigma(W_i) - Delta IK_relSigma(W_{i-1})
```

These signals show whether relational projection compatibility stabilizes, degrades, recovers or accelerates across windows.

They must be interpreted together with `applicability_rate`.

## 15. IK_relSigma(Hangar)

`IK_relSigma(Hangar)` observes the distribution of relational coherence windows inside an observation space.

The Hangar may contain:

```text
H_IK_rel = {
    IK_relSigma(W_i),
    applicability_rate(W_i),
    IK_rel_cloud(W_i),
    optional shared projection summaries
}
```

Useful metrics:

- distribution of `IK_relSigma`
- distribution of `IK_rel_axis`
- distribution and drift of `IK_rel_cloud`
- applicability-rate distribution
- gate-closure frequency
- relational corridor drift
- cluster migration
- tail-risk or outlier-pressure change
- optional shared projection drift

## 16. Delta IK_relSigma(Hangar) and Delta2 IK_relSigma(Hangar)

For ordered Hangar observation spaces:

```text
H_i = H_IK_rel(W_i)
H_{i-1} = H_IK_rel(W_{i-1})
```

define:

```text
Delta IK_relSigma(Hangar)_i = D_H_rel(H_i, H_{i-1})
```

where `D_H_rel` is a versioned distribution-distance function.

`D_H_rel(H_i, H_{i-1}) >= 0` by definition as a distribution distance.
`Delta IK_relSigma(Hangar)` is therefore a nonnegative change magnitude.
`Delta2 IK_relSigma(Hangar)` may be negative, indicating deceleration of
distributional change, not improvement or degradation by itself.

Second difference:

```text
Delta2 IK_relSigma(Hangar)_i =
    Delta IK_relSigma(Hangar)_i - Delta IK_relSigma(Hangar)_{i-1}
```

These signals indicate whether the distribution of relational coherence patterns is changing and whether that change accelerates.

They are observation signals, not automated decisions.

## 17. Limitations

- `IK_rel` measures compatibility of coherence movements, not coupling,
  causation, agreement or resonance.
- Static steps are masked by the zero-movement policy. High `IK_relSigma` must
  always be read together with `applicability_rate` and the `static_step`
  share.
- Single-scalar reporting can hide component divergence; `G_rel_active` and the
  point cloud remain the richer view.

## 18. Relation to the R-family

`R0` opens dyadic or n-adic comparability.

`IK_rel` is the next relational projection after a stable `R0` gate. It asks
whether monadic coherence projections and their movements remain relationally
compatible.

Branch-specific R-family layers follow as separate questions. They may use the
same declared trajectories and stable `R0` gate, and they should read `IK_rel`
as relational-coherence context where the application compares coherence,
geometry or pacing.

`IK_rel` asks:

```text
Do coherence projections remain relationally compatible?
```

Branch-specific R-family layers ask:

- `R_geom`: Do trajectories couple geometrically in the KSODI state space?
- `R_pace`: Does readable-language or sign-visible pacing remain stable where explicitly defined?
- future signal-media extension: Do temporal rhythms, voice indicators or timing artifacts fit as a later additional layer?

Logical compatibility is not the same as resonance.

`IK_rel` must not be reduced to `R_geom`.

`R_geom` must not be reduced to `IK_rel`.

`R_full` is only the family label for this broader relational / resonance
research branch. It is not a single scalar and does not introduce a generic
`R_fullSigma` layer.

These axes can be compared over time, especially through their point clouds and
Hangar distributions, but they answer different questions and must remain
branch-specific in formal release wording.

## 19. Comparability

`IK_rel`, `Delta IK_rel`, `Delta2 IK_rel`, `IK_relSigma` and `IK_relSigma(Hangar)` are comparable only under stable conditions:

- same operator definitions
- same operator versions
- same ordering of components in `Z`
- same `ik_config_id`
- same `r0_config_id`
- same `ik_rel_axis_config_id`
- same `w_rel`
- same `theta_R0_stable`
- same eval-unit pairing policy
- same windowing policy
- same aggregate functions
- same Hangar distance function `D_H_rel`
- same applicability policy
- same component activation and clipping policy for `G_rel`
- same `epsilon_move`
- same `min_components_rel`
- same zero-movement / `static_step` policy
- same `C_shared` activation status and config ID if active
- same delta naming policy for `IK_rel` versus `IK_rel_axis`

## 20. Storage Principle

Recommended storage per paired evaluation step:

- `eval_pair_id`
- `trajectory_ids`
- `context_scope_id`
- `IK_A(t)`, `IK_B(t)`
- `Delta IK_A(t)`, `Delta IK_B(t)`
- `R0(t)`
- gate status
- `static_step`
- `IK_rel(t)` or `not_applicable`
- optional `G_rel_active(t)`
- optional `w_rel` or `ik_rel_axis_config_id`
- optional `IK_rel_axis(t)`
- optional `Delta IK_rel(t)`
- optional `Delta2 IK_rel(t)`
- optional `Delta IK_rel_axis(t)`
- optional `Delta2 IK_rel_axis(t)`
- zero-movement policy ID
- `epsilon_move`
- `min_components_rel`
- optional `C_shared` config ID if active
- `ik_config_id`
- `r0_config_id`

Recommended storage per window:

- `window_id`
- `IK_relSigma(W)`
- `applicability_rate(W)`
- optional `IK_rel_cloud(W)`
- optional `Delta IK_relSigma(W)`
- optional `Delta2 IK_relSigma(W)`
- `static_step` count or share
- gate-closure count
- thresholds version

Recommended storage per Hangar summary:

- `hangar_id`
- distribution summary of `IK_relSigma`
- distribution summary of `IK_rel_axis`
- distribution summary of `IK_rel_cloud`
- distribution summary of applicability rates
- optional `Delta IK_relSigma(Hangar)`
- optional `Delta2 IK_relSigma(Hangar)`
- `D_H_rel` version

Avoid storing full prompt text, full answer text, unnecessary source language, embeddings unless explicitly justified, identity or personality inference.

## 21. Compact Formula Block

```text
if R0(t) >= theta_R0_stable:
    IK_rel(t) may be evaluated
else:
    IK_rel(t) = not_applicable

deltaIK_AB(t) = |IK_A(t) - IK_B(t)|

C_ik_gap(t)   = clip(1 - |IK_A(t) - IK_B(t)|, 0, 1)
C_ik_move(t)  = clip(1 - |Delta IK_A(t) - Delta IK_B(t)| / 2, 0, 1)
C_ik_accel(t) = clip(1 - |Delta2 IK_A(t) - Delta2 IK_B(t)| / 4, 0, 1)

if |Delta IK_A(t)| <= epsilon_move and |Delta IK_B(t)| <= epsilon_move:
    C_ik_move(t) = not_applicable
    static_step = true

IK_rel(t) := C_ik_move(t)

G_rel(t) = [C_ik_gap(t), C_ik_move(t), C_ik_accel(t), C_shared(t)]
G_rel_active(t) = [C_i(t) | C_i(t) is applicable]

active(t) = {i | C_i(t) is applicable}
IK_rel_axis(t) =
    sum_{i in active(t)} w_i * C_i(t) / sum_{i in active(t)} w_i

IK_rel_axis(t) is defined only if:
    |active(t)| >= min_components_rel
    sum_{i in active(t)} w_i > 0

Delta IK_rel(t) = IK_rel(t) - IK_rel(t-1)
Delta2 IK_rel(t) = Delta IK_rel(t) - Delta IK_rel(t-1)
Delta IK_rel_axis(t) = IK_rel_axis(t) - IK_rel_axis(t-1)
Delta2 IK_rel_axis(t) =
    Delta IK_rel_axis(t) - Delta IK_rel_axis(t-1)

W_app = {t in W | IK_rel(t) != not_applicable}
IK_rel_cloud(W) = {G_rel_active(t) | t in W_app}
IK_relSigma(W) = aggregate({IK_rel(t) | t in W_app})
applicability_rate(W) = |W_app| / |W|

Delta IK_relSigma(Hangar)_i = D_H_rel(H_i, H_{i-1})
Delta2 IK_relSigma(Hangar)_i =
    Delta IK_relSigma(Hangar)_i - Delta IK_relSigma(Hangar)_{i-1}
```

## 22. Variable Reference

| Variable | Semantic role |
| --- | --- |
| `IK_A(t)`, `IK_B(t)` | Monadic projections of compared trajectories |
| `Delta IK_A(t)`, `Delta IK_B(t)` | Movement of monadic projections |
| `deltaIK_AB(t)` | Scalar distance between monadic projection values |
| `move_gap_raw(t)` | Absolute difference between monadic projection movements |
| `IK_rel(t)` | Relational coherence projection after stable R0 gate |
| `G_rel(t)` | Relational coherence component vector |
| `G_rel_active(t)` | Applicable, clipped relational components used for axis projection |
| `C_ik_gap(t)` | Compatibility of monadic projection values |
| `C_ik_move(t)` | Compatibility of projection movement |
| `C_ik_accel(t)` | Compatibility of projection acceleration |
| `C_shared(t)` | Reserved shared component slot; inactive by default in v3.50 |
| `w_rel` | Versioned relational projection weight vector |
| `IK_rel_axis(t)` | Weighted relational axis projection |
| `IK_rel_cloud(W)` | Point cloud of relational component vectors in a window |
| `IK_shared(t)` | Optional shared projection over the shared active `Z` components |
| `Delta IK_rel(t)` | Movement of relational coherence |
| `Delta2 IK_rel(t)` | Change of relational-coherence movement |
| `Delta IK_rel_axis(t)` | Optional movement of the axis projection |
| `Delta2 IK_rel_axis(t)` | Optional second difference of the axis projection |
| `IK_relSigma(W)` | Aggregated relational coherence over a window |
| `applicability_rate(W)` | Share of window where `IK_rel` was applicable |
| `IK_relSigma(Hangar)` | Distribution of relational coherence windows |
| `D_H_rel` | Versioned distance function for relational Hangar distributions |
| `epsilon_move` | Threshold for zero-movement masking |
| `static_step` | Flag for steps masked because both compared movements are below threshold |
| `min_components_rel` | Minimum active relational components required for axis projection |
