# KSODI IK - Interaction Coherence Projection v3.50

Status: public v3.50 reference release; private canonical workbench origin retained. Lifted from the stable v3.42 projection line after Fable IK review, v3.50 Z hardening and Anne's 2026-07-21 public-release decision. Aligned with `KSODI_State-Vector-Z_V350.md`, `KSODI-Hangar_V350.md`, `KSODI-Glossar.md` and the `R0` relational-gate boundary.

Layer: monadic projection branch after `Z`

## 1. Definition

`IK` describes interaction coherence as a scalar projection of the KSODI state vector onto a versioned coherence axis.

It is calculated from the already computed numerical state vector:

```text
Z(t) = [K0(t), S0(t), O0(t), D0(t), I0(t)]
```

`IK` is not a new language object.

`IK` is not a time derivative of `Z`.

`IK` is not an independent measurement beside `Z`.

`IK` is not a truth, quality, utility, compliance or alignment score.

It is a projection of the observable interaction state.

## 2. Architectural Position

After `Z`, KSODI separates monadic projection from state-space movement.

```text
K/S/O/D/I
   |
   v
Z(t)
   |
   +--> state-space diagnostics
   |      Delta Z
   |      Delta2 Z
   |      Drift_L1 / Drift_L2
   |
   +--> IK branch
          IK
          Delta IK / Delta2 IK
          IKSigma
          IKSigma(Hangar)
```

`Delta Z` observes movement in the full five-dimensional state space.

`IK` observes projection onto a coherence direction.

These are parallel diagnostic branches. They are not redundant, but they are
not mathematically independent under stable `w` and stable applicability:

```text
Delta IK(t) = w dot Delta Z(t)
```

## 3. Input Data

For an evaluation unit `u` or turn `t`:

```text
Z(u) in [0,1]^5 where all components are applicable
Z(u) = [K0(u), S0(u), O0(u), D0(u), I0(u)]
```

In v3.50, `Z` also carries the applicability mask inherited from the
operator layer:

```text
A_Z(u) = [A_K(u), A_S(u), A_O(u), A_D(u), A_I(u)]
```

where `A_X(u) = 1` means component `X` is applicable and numerically observed,
and `A_X(u) = 0` means that the component is not applicable under the active
profile.

Missing or non-applicable operator values must not be silently coerced to `0`.

Required metadata:

- `context_scope_id`
- operator version IDs
- ordering of components in `Z`
- applicability mask `A_Z(u)`
- `ik_config_id`
- weight vector `w`
- masking / renormalization policy where a masked view is used

No raw text is required after the operator values have been calculated.

## 4. Projection Vector

Let:

```text
w = [w_K, w_S, w_O, w_D, w_I]
```

with:

```text
w_j >= 0
sum_j w_j = 1
```

Default:

```text
w_K = w_S = w_O = w_D = w_I = 0.2
```

The weight vector defines the coherence axis.

It must be versioned.

## 5. Standard Definition

```text
IK(t) = w dot Z(t)
```

Expanded:

```text
IK(t) = w_K*K0(t) + w_S*S0(t) + w_O*O0(t) + w_D*D0(t) + w_I*I0(t)
```

Range:

```text
IK(t) in [0,1]
```

This full `IK(t)` definition assumes that all components are applicable under
the active profile.

Applicability-aware variant:

```text
IK_applicable(t)
= sum_i(A_Z_i(t) * w_i * Z_i(t)) / sum_i(A_Z_i(t) * w_i)
```

If the denominator is `0`, the projection is `not_applicable`.

A masked projection must be explicitly named, for example
`IK_applicable(t)`. It must never be presented as the same thing as full
`IK(t)`.

Interpretation:

| Signal | Meaning |
| --- | --- |
| high `IK` | state projects strongly onto the configured coherence axis |
| medium `IK` | mixed state relative to the configured coherence axis |
| low `IK` | weak projection onto the configured coherence axis |

This is not a judgment of truth, usefulness or moral quality.

## 6. Delta IK

Because `IK(t)` is scalar, its first difference is scalar:

```text
Delta IK(t) = IK(t) - IK(t-1)
```

Range:

```text
Delta IK(t) in [-1,1]
```

Under stable `w` and stable applicability:

```text
Delta IK(t) = w dot Delta Z(t)
```

Interpretation:

| Signal | Meaning |
| --- | --- |
| `Delta IK > 0` | projection moves upward along the coherence axis |
| `Delta IK < 0` | projection moves downward along the coherence axis |
| `Delta IK approx 0` | projection remains stable |

`Delta IK` describes movement of the projection.

It does not describe the full movement of `Z`.

If a masked projection is used, first differences require the same masking /
renormalization policy across the compared units. Otherwise `Delta IK` is
`not_applicable` or must be named as a profile-specific masked delta.

## 7. Delta2 IK

The second difference describes how the projection movement itself changes:

```text
Delta2 IK(t) = Delta IK(t) - Delta IK(t-1)
```

Range:

```text
Delta2 IK(t) in [-2,2]
```

Interpretation:

| Signal | Meaning |
| --- | --- |
| `Delta2 IK approx 0` | steady projection movement |
| increasing `abs(Delta2 IK)` | changing coherence dynamics; potential early warning |
| `Delta2 IK > 0` | upward acceleration of projection movement |
| `Delta2 IK < 0` | deceleration or downward acceleration depending on prior movement |

`Delta2 IK` is an early-warning signal, not a quality score.

A direction reversal is defined by a sign change in `Delta IK`, not by `Delta2 IK` alone:

```text
Delta IK(t-1) * Delta IK(t) < 0
```

## 8. Why Delta IK Adds Information Beyond Delta Z

`Delta Z` and `Delta IK` answer different questions.

| Signal | Question |
| --- | --- |
| `Delta Z` | How does the full state vector move? |
| `Delta IK` | How does the projection onto the coherence axis move? |
| `Delta2 Z` | Is state-space movement accelerating or changing direction? |
| `Delta2 IK` | Is coherence-axis movement accelerating, slowing or preparing a reversal? |

Example:

```text
Delta Z != 0
Delta IK approx 0
```

The state moves, but mostly outside the configured coherence axis.

For stable `w` and stable applicability this follows from the linear
projection:

```text
Delta IK(t) = w dot Delta Z(t)
```

The diagnostic point is not independence. The diagnostic point is dimensional:
`Delta Z` preserves the full state-space movement, while `Delta IK` shows the
movement along the configured coherence axis.

Example:

```text
Delta Z != 0
Delta IK != 0
```

The state moves and this movement is coherence-relevant under the chosen `w`.

This is the diagnostic gain of the IK branch.

## 9. IKSigma

`IKSigma` aggregates projection behavior over a window.

For a window:

```text
W = {u_1, ..., u_n}
```

Applicable window under a stable mask:

```text
W_app = {u in W | IK_applicable(u) is numerically defined under the declared policy}
applicability_rate_IK(W) = |W_app| / |W|
```

Mean state vector:

```text
Zbar(W) = (1/n) * sum_i Z(u_i)
```

Canonical window projection:

```text
IKSigma(W) = w dot Zbar(W)
```

This is the projection of the mean state vector.

It is not merely an unexamined average of individual `IK(u)` values.

For linear full `IK`, both values are mathematically equivalent under stable
`w` and stable applicability:

```text
w dot mean(Z) = mean(w dot Z)
```

If units inside the window use different applicability masks,
`IK_applicable` has different denominators. Then the mean of masked
projections is not automatically equal to the projection of a masked mean.
The window must declare `W_app`, `applicability_rate_IK(W)` and the active
masking / renormalization policy.

The canonical expression remains `w dot Zbar(W)` because it preserves the relation to the state-space layer.

## 10. Delta IKSigma and Delta2 IKSigma

Between ordered windows:

```text
Delta IKSigma(W_i) = IKSigma(W_i) - IKSigma(W_{i-1})
```

Second difference:

```text
Delta2 IKSigma(W_i) = Delta IKSigma(W_i) - Delta IKSigma(W_{i-1})
```

Use case:

- observe stabilization or degradation across windows
- detect slow coherence drift
- detect acceleration of projection changes before single-turn signals become obvious

## 11. IKSigma(Hangar)

`IKSigma(Hangar)` observes the distribution of IK-related state windows inside an observation space.

It is not a single score.

A Hangar may contain:

```text
H_IK = {Z(u) | u in W}
```

or window summaries:

```text
H_IKSigma = {Zbar(W_i), IKSigma(W_i)}
```

Useful Hangar metrics:

- dispersion of state vectors inside a window
- drift between window centers
- component-wise corridor deviation
- anomaly distance from window center
- distribution of `IKSigma` values across windows
- frequency of threshold crossings

Minimal examples:

```text
Disp(W) = mean_u ||Z(u) - Zbar(W)||_2^2
WindowDrift(W_i, W_j) = ||Zbar(W_i) - Zbar(W_j)||_2
IKSigmaDrift(W_i, W_j) = |IKSigma(W_i) - IKSigma(W_j)|
```

## 12. IKSigma(Hangar) Drift and Acceleration

For long-running interaction systems, single points may remain inconspicuous while the distribution of interaction states slowly moves.

`IKSigma(Hangar)` can therefore be observed dynamically.

This is especially useful when:

- two agents work together across long periods
- a human and a machine interact repeatedly across many sessions
- a small intervention shifts the interaction corridor gradually
- a previously stable communication pattern begins to move toward a sensitive or risky region

The relevant signal is not necessarily one anomalous point.

The relevant signal may be corridor drift, cluster migration, dispersion growth or increased pressure at the edge of an established interaction space.

### 12.1 Distribution Delta

For ordered Hangar windows:

```text
H_i = H_IKSigma(W_i)
H_{i-1} = H_IKSigma(W_{i-1})
```

define a distribution movement summary:

```text
Delta IKSigma(Hangar)_i = D_H(H_i, H_{i-1})
```

where `D_H` is a versioned distribution-distance function.

This `Delta IKSigma(Hangar)` denotes a nonnegative distribution distance. It is
therefore not the same kind of signed scalar delta as `Delta IK` or
`Delta IKSigma(W)`.

Possible choices:

- centroid drift
- dispersion change
- corridor deviation
- cluster migration distance
- tail-risk or outlier-pressure change
- threshold crossing frequency change

Minimal centroid form:

```text
Centroid(H_i) = mean({Zbar(W) | W in H_i})

Delta IKSigma(Hangar)_i =
    ||Centroid(H_i) - Centroid(H_{i-1})||_2
```

### 12.2 Distribution Acceleration

The second difference describes whether Hangar drift itself accelerates:

```text
Delta2 IKSigma(Hangar)_i =
    Delta IKSigma(Hangar)_i - Delta IKSigma(Hangar)_{i-1}
```

This can act as an early-warning signal when a stable corridor begins to move faster.

It is not an automatic judgment.

It indicates that the distribution of observed interaction states is changing.

### 12.3 Corridor Research Note

KSODI treats corridor detection as a research layer.

The current standard remains:

```text
w_fixed
```

where the projection vector is fixed and versioned.

Future or domain-specific analyses may define:

```text
w_domain
w_learned
w_adaptive
```

with strict versioning and comparability rules.

The research question is whether different interaction domains form stable corridors in the KSODI state space and whether the coherence axis can be empirically characterized for those domains.

This remains future research and is not treated as a finalized v3.50 method claim.

## 13. Relation to IK_rel

`IK` is monadic.

`IK_rel` is relational and belongs to the relational branch (`KSODI Full`) after
a stable `R0` gate.

```text
IK can be evaluated without R0.
IK_rel requires stable R0.
```

This distinction prevents KSODI from confusing internal projection coherence with relational compatibility.

## 14. Comparability

`IK`, `Delta IK`, `Delta2 IK`, `IKSigma` and `IKSigma(Hangar)` are comparable only under stable conditions:

- same operator definitions
- same operator versions
- same ordering of components in `Z`
- same context scope
- same eval-unit granularity
- same weight vector `w`
- same `ik_config_id`
- same applicability / masking and renormalization policy
- same handling of `IK_applicable(t)` versus full `IK(t)`
- same windowing policy for Sigma variants
- same `W_app` and applicability-rate policy where masked windows are used
- same threshold policy where events are used
- same Hangar distance function `D_H` where Hangar drift is used
- same corridor definition where corridor metrics are used

## 15. Storage Principle

Recommended storage per evaluation unit:

- `eval_unit_id`
- `context_scope_id`
- operator version IDs
- `Z(t)` or reference to stored state vector
- applicability mask `A_Z(t)`
- applicability rate where a masked projection is used
- `w` or `ik_config_id`
- `IK(t)`
- optional `IK_applicable(t)`
- optional `Delta IK(t)`
- optional `Delta2 IK(t)`

Recommended storage per window:

- `window_id`
- `context_scope_id`
- `Zbar(W)`
- `W_app` where masking is used
- `applicability_rate_IK(W)` where masking is used
- `IKSigma(W)`
- optional `Delta IKSigma(W)`
- optional `Delta2 IKSigma(W)`
- dispersion and drift metrics where needed
- optional `Delta IKSigma(Hangar)`
- optional `Delta2 IKSigma(Hangar)`
- optional corridor or cluster IDs where defined
- thresholds version where events are used

Avoid storing:

- full prompt text
- full answer text
- unnecessary source language
- embeddings unless explicitly justified

## 16. Compact Formula Block

```text
Z(t) = [K0(t), S0(t), O0(t), D0(t), I0(t)]
A_Z(t) = [A_K(t), A_S(t), A_O(t), A_D(t), A_I(t)]
w = [w_K, w_S, w_O, w_D, w_I]
sum_j w_j = 1

IK(t) = w dot Z(t)

IK_applicable(t)
= sum_i(A_Z_i(t) * w_i * Z_i(t)) / sum_i(A_Z_i(t) * w_i)

Delta IK(t) = IK(t) - IK(t-1)
Delta IK(t) = w dot Delta Z(t)     # when w and mask are stable

Delta2 IK(t) = Delta IK(t) - Delta IK(t-1)

Zbar(W) = (1/n) * sum_i Z(u_i)

IKSigma(W) = w dot Zbar(W)

Delta IKSigma(W_i) = IKSigma(W_i) - IKSigma(W_{i-1})

Delta2 IKSigma(W_i) = Delta IKSigma(W_i) - Delta IKSigma(W_{i-1})

Disp(W) = mean_u ||Z(u) - Zbar(W)||_2^2

WindowDrift(W_i, W_j) = ||Zbar(W_i) - Zbar(W_j)||_2

Delta IKSigma(Hangar)_i = D_H(H_i, H_{i-1})

Delta2 IKSigma(Hangar)_i =
    Delta IKSigma(Hangar)_i - Delta IKSigma(Hangar)_{i-1}
```

## 17. Variable Reference

| Variable | Semantic role |
| --- | --- |
| `Z(t)` | Numerical KSODI state vector |
| `A_Z(t)` | Applicability mask for the five Z components |
| `w` | Versioned projection vector / coherence axis |
| `IK(t)` | Scalar projection of `Z(t)` |
| `IK_applicable(t)` | Named masked projection when not all Z components are applicable |
| `Delta IK(t)` | Movement of the projection |
| `Delta2 IK(t)` | Change of projection movement |
| `W` | Observation window |
| `W_app` | Applicable subset of a window under the declared masking policy |
| `applicability_rate_IK(W)` | Share of a window where IK projection is applicable under the active policy |
| `Zbar(W)` | Mean state vector of a window |
| `IKSigma(W)` | Window projection |
| `Delta IKSigma(W)` | Movement of window projection |
| `Delta2 IKSigma(W)` | Change of window-projection movement |
| `H_IK` | Hangar for IK-related state distributions |
| `Disp(W)` | Dispersion inside a window |
| `WindowDrift(W_i, W_j)` | Drift between window centers |
| `Delta IKSigma(Hangar)` | Distribution movement of IK-related Hangar windows |
| `Delta2 IKSigma(Hangar)` | Acceleration of Hangar distribution movement |
| `D_H` | Versioned distribution-distance function for Hangar drift |
| `w_fixed` | Fixed versioned projection vector |
| `w_domain` | Domain-specific projection vector |
| `w_learned` | Empirically learned projection vector |
| `w_adaptive` | Dynamically adapted projection vector; research-only unless strictly versioned |
| `IK_rel` | Relational coherence projection after stable `R0` gate |
