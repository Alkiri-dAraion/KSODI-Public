# KSODI State Vector Z - Interaction State Representation v3.50

Status: public v3.50 reference release; private canonical workbench origin retained. Lifted from the solid v3.42 state-vector line after Fable Z review, 2026-07-20 hardening and Anne's 2026-07-21 public-release decision.

Layer: KSODI Standard-Eval Layer 2. `Z` is the state-vector layer built from Layer-1 operator values. `Delta Z`, `Delta2 Z`, `ZSigma(W)` and `ZSigma(Hangar)` are state-space views over this layer. `IK` and `R0` are downstream / parallel branches after `Z`, not part of the `Z` definition itself.

Publication note: `Z` is released together with the reviewed public `K0`
operator, so the state-vector definition no longer points to a pending K
placeholder.

## 1. Definition

Canonical source boundary:

```text
e_A(k)
  -> K_A / S_A / O_A / D_A / I_A
  -> Z_A(k)
       |-> IK_A(k)
       +-> R0(A,B,...) -> IK_rel -> R-family
```

Every component of `Z_A(k)` remains attached to the same identified target
event and declared monadic trajectory. Temporal operator comparisons and
`Delta Z_A` use only comparable positions within that trajectory. Context or
reference material admitted by an operator profile does not become another
source component of `Z_A`.

`Z_A` and `Z_B` remain distinguishable. Their parallel availability does not
create `Z_AB`; relational interpretation begins only at a separately declared
`R0` gate.

The state vector `Z_t` describes the observable state of an interaction at turn `t` or evaluation unit `t`.

It is composed of the five normalized KSODI operator values:

```text
Z_t = [K0(t), S0(t), O0(t), D0(t), I0(t)]
```

`Z_t` is not another language object. It is the state representation created from the operators.

In v3.50, `Z_t` must also carry an applicability mask because some operator
values may be `not_applicable` under the active profile:

```text
A_Z(t) = [A_K(t), A_S(t), A_O(t), A_D(t), A_I(t)]
```

where `A_X(t) = 1` means that component `X` is applicable and numerically
observed for this unit, and `A_X(t) = 0` means that the component is not
applicable under the active profile.

Missing or non-applicable operator values must not be silently coerced to `0`.
Any numeric projection, aggregation or dashboard view over `Z_t` must declare
its masking and renormalization policy.

## 2. State Space

Where applicable, all five components are normalized:

```text
K0(t), S0(t), O0(t), D0(t), I0(t) in [0, 1]
```

Therefore the fully numeric view lies in:

```text
Z_t in [0, 1]^5
```

The KSODI state space is a five-dimensional unit space when all components are
applicable. Applicability-aware views preserve the five-component ordering but
carry `A_Z(t)` so that downstream layers can distinguish observed low values
from non-applicable values.

## 3. Architectural Role

The operators shape `Z`.

After `Z`, the preferred audit path is numerical:

```text
operators -> Z(t)
          -> Delta Z / Delta2 Z
          -> IK branch and R0 gate in parallel
          -> relational branch after stable R0
          -> window / Hangar views by layer
```

This is the governance-relevant transition:

- before `Z`: language, context, retrieval, and answer material may be inspected to compute operator values
- at `Z`: the interaction becomes a numerical state vector
- after `Z`: analysis should use vectors, deltas, projections, and metadata whenever possible

This reduces the need to retain language while preserving long-term auditability.

## 3.1 Simple and Complex Views After Z

`Z_t` is the base numerical state. From this point on, KSODI can support two
complementary views:

- simple vectors and scalar projections for human-readable observation
- richer vector, trajectory and point-cloud views for machine-side analysis

The simple view is useful for dashboards, audit communication, corridor
explanations and responsibility handover.

The complex view preserves more of the observed structure for machines:

```text
Z trajectories
Delta Z / Delta2 Z
IK projections
IK_rel_cloud(W)
R_geom_cloud(W)
R_pace_cloud(W)
Hangar distributions
```

This distinction is methodically important. Human-readable projections are not
intended to erase the full vector space. They are readable views into it.

Machines may continue to analyze complete vectors, trajectories, component
clouds, distributions and corridor movement where this is useful and properly
versioned.

## 3.2 Analytical Branches After Z

After `Z(t)`, KSODI separates into two analytical branches.

```text
K/S/O/D/I
   |
   v
Z(t)
   |
   v
Delta Z / Delta2 Z
   |-------------------------------|
   v                               v
IK branch                       R0 gate
  IK                              checks whether distinguishable
  Delta IK / Delta2 IK            trajectories are stable enough
  IKSigma                         for relational comparison
  IKSigma(Hangar)
                                  |
                                  v
                               relational branch
                                  IK_rel
                                  R_geom
                                  R_pace
                                  future signal-media extension
```

The IK branch observes monadic projection and coherence dynamics.

The `R0` gate and the later relational branch observe dyadic or n-adic trajectory coupling.

The R-family denotes the relational and resonance observation family. It is not a single scalar score.

Individual Layer-1 components may receive optional monadic trajectory,
projection or aggregation views. After stable `R0`, separately defined
operator-specific relational comparison views may also be used. None of these
partial views is complete `Z`, canonical `IK`, `IK_rel` or resonance.

`R0` runs after `Z` and in parallel to monadic `IK`. It is not downstream of
`IK`. Relational projection begins only after `R0`, because `R0` checks whether
two or more monadic trajectories can meaningfully be related at all.

## 4. Eval Scope

`Z_t` is calculated per evaluation unit or turn.

Inputs are the already computed operator values:

- `K0(t)`: observable context completeness
- `S0(t)`: observable structural coherence
- `O0(t)`: observable grounded objectivity
- `D0(t)`: observable clarity
- `I0(t)`: observable information impulse

Typical source material for those operator values may include:

- user chunk `u_t`
- assistant chunk `a_t`
- system prompt `SP`
- tool profile `TP`
- retrieval set `RET_k(u_t)`

`Z_t` itself stores only the resulting operator values, applicability mask and required metadata.

## 5. State Change

Because the system is turn-based, movement is represented as a discrete difference:

```text
Delta Z_t = Z_t - Z_{t-1}
```

Component-wise:

```text
Delta Z_{t,i} = Z_{t,i} - Z_{t-1,i}
```

`Delta Z_{t,i}` is defined only where component `i` is applicable in both
compared states under a compatible operator profile. Otherwise the component
delta is `not_applicable` or skipped according to the declared window policy.

`Delta Z_t` describes the direction and magnitude of state movement.

It is not a quality judgment.

## 6. Drift Acceleration

The second discrete difference describes how the movement itself changes:

```text
Delta2 Z_t = Delta Z_t - Delta Z_{t-1}
```

Component-wise:

```text
Delta2 Z_{t,i} = Delta Z_{t,i} - Delta Z_{t-1,i}
```

`Delta2 Z_{t,i}` is defined only where the relevant first-difference values are
applicable and comparable.

Interpretation:

| Pattern | Meaning |
| --- | --- |
| `Delta2 Z approx 0` | steady movement; stable drift |
| increasing `abs(Delta2 Z)` | drift acceleration; potential early warning |
| decreasing `abs(Delta2 Z)` | drift deceleration |
| sign change | possible directional reversal |

`Delta2 Z_t` is an early-warning signal, not an evaluation score.

## 7. Drift Norms

The movement of `Z_t` can be summarized by norms.

L1 drift:

```text
Drift_L1(t) = sum_i |Z_{t,i} - Z_{t-1,i}|
Drift_L1_norm(t) = Drift_L1(t) / 5
```

L2 drift:

```text
Drift_L2(t) = ||Z_t - Z_{t-1}||_2
Drift_L2_norm(t) = Drift_L2(t) / sqrt(5)
```

For applicability-aware views, compute norms over the active shared component
set:

```text
A_delta(t) = {i | A_Z_i(t) = 1 and A_Z_i(t-1) = 1}
```

and declare the normalization denominator:

```text
Drift_L1_active_norm(t)
= sum_{i in A_delta(t)} |Z_{t,i} - Z_{t-1,i}| / |A_delta(t)|

Drift_L2_active_norm(t)
= sqrt(sum_{i in A_delta(t)} (Z_{t,i} - Z_{t-1,i})^2) / sqrt(|A_delta(t)|)
```

If `A_delta(t)` is empty, the drift norm is `not_applicable`.

Use both when possible:

| Norm | Useful for |
| --- | --- |
| `L1` | stable monitoring and component-readable movement |
| `L2` | peak-sensitive movement analysis |

## 8. Interpretation

| Signal | Meaning |
| --- | --- |
| low drift | stable interaction state |
| medium drift | moderate state change |
| high drift | strong state change |
| increasing acceleration | drift is changing faster |

Drift describes movement in state space, not answer quality.

## 9. Comparability

`Z_t`, `Delta Z_t`, and `Delta2 Z_t` are comparable only under stable conditions:

- same operator definitions
- same operator versions
- same embedding model where operators use embeddings
- same retrieval configuration where relevant
- same `Ref` definition where reference-space logic is used
- same [`O0` source-need gate policy](../Layer-1_KSODI-Operators_V350/KSODI_Operator-O_Source-Need-Gate_V350.md)
- same weighting choices inside operators
- same evaluation-unit granularity
- same ordering of components in `Z_t`
- same applicability / masking and renormalization policy

## 10. Relation to IK

`IK` is a scalar linear projection of the state vector. It is not a time
derivative and not an independent measurement.

```text
IK(t) = w dot Z_t
```

where `w` is a versioned weight vector with:

```text
w_j >= 0
sum_j w_j = 1
```

Under a fully numeric `Z_t in [0,1]^5`, these constraints keep `IK(t)` in
`[0,1]`. Masked or applicability-aware variants must declare their active
component set and renormalization policy.

Important distinction:

| Object | Type | Role |
| --- | --- | --- |
| `Z_t` | vector | state |
| `Delta Z_t` | vector | movement |
| `Delta2 Z_t` | vector | acceleration of movement |
| `IK(t)` | scalar | projection onto a coherence axis |
| `Delta IK(t)` | scalar difference | change in projection |

`Delta Z` and `Delta IK` are parallel diagnostic branches, but they are not
mathematically independent:

```text
Delta IK(t) = w dot Delta Z(t)     # when w and mask are stable
```

The diagnostic gain is dimensional: `Delta Z` preserves full state-space
movement, while `Delta IK` shows movement along the configured coherence axis.

## 11. Relation to R0, IK_rel and the R-family

`R0` and the R-family operate on trajectories.

```text
Z_t, Delta Z_t, A_Z(t) -> R0(t)
R0(t) stable enough -> IK_rel(t)
Z_t, Delta Z_t, dyadic or n-adic trajectory data -> R-family
```

`R0` is the numerical pre-check layer for dyadic or n-adic relational analysis.
It asks whether relational comparison is methodically meaningful at all.

`IK_rel` is not a free early value. It is a relational projection layer and becomes methodically valid only after `R0` has established that dyadic or n-adic comparison is meaningful.

The R-family belongs to the Full layer. In the active v3.50 boundary it may include:

- `R_geom`: geometric coupling of dyadic or n-adic trajectories in the KSODI state space
- `R_pace`: readable-language or sign-visible pacing dynamics where explicitly defined
- `R_geomSigma`: aggregated geometric-coupling behavior over an observation window
- `R_geomSigma(Hangar)`: distribution of geometric-coupling patterns inside an observation space
- `R_paceSigma`: optional pacing aggregation where pacing dynamics are explicitly defined

Audio, radio, Morse, waveform, `R_takt`, `R_freq` and voice-related terms are
future signal-media research or historical wording, not active v3.50 core
terms. The core description remains architecture-agnostic: it observes
trajectories of interacting entities in the KSODI state space.

The R-family must not be reduced to `IK`.

## 11.1 R0 Gate Rule

Canonical gate:

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

This prevents KSODI from assigning relational coherence where no stable shared movement has been established.

## 11.2 Window and Hangar Views

Window and Hangar views can be derived from `Z`, but they are not a third main
branch after `Z`.

The state-space layer defines the numerical state and its movement:

```text
Z_t
Delta Z_t
Delta2 Z_t
Drift_L1 / Drift_L2
```

For `Z`, a window summary may be defined as:

```text
ZSigma(W) = aggregate({Z_t | t in W})
```

where `aggregate` may be a mean vector, median vector, percentile profile, or
another versioned window summary.

The window summary must carry its applicability policy:

```text
W_app = {t in W | Z_t is applicable under the active profile}
applicability_rate_Z(W) = |W_app| / |W|
```

For component-wise summaries, each component may have its own active subset:

```text
W_app_i = {t in W | A_Z_i(t) = 1}
```

The corresponding Hangar view observes the distribution of such state windows:

```text
ZSigma(Hangar) = distribution({ZSigma(W_i)})
```

The terms `ZSigma` and `ZSigma(Hangar)` may be used for these derived state-space
window views. They should not be read as a separate Sigma layer.

Other window views remain in their own method context:

- `IKSigma` belongs to the projection layer.
- `IK_relSigma` belongs to the relational projection layer after stable `R0`.
- `R0Sigma`, `R_geomSigma` and optional `R_paceSigma` belong to the relational
  / R-family layer.

The released shared Hangar method note is maintained separately at the
repository root:

[`KSODI-Hangar_V350.md`](../../KSODI-Hangar_V350.md)

## 12. Storage Principle

Recommended storage after operator calculation:

- `eval_unit_id`
- `context_scope_id`
- operator version IDs
- `Z_t`
- optional `Delta Z_t`
- optional `Delta2 Z_t`
- applicability mask `A_Z(t)`
- optional branch identifiers
- optional gate status for `R0`
- `ZSigma(W)` / `ZSigma(Hangar)` summaries where enabled
- applicability rates for window and Hangar summaries
- drift norms
- detector and configuration IDs

Avoid storing:

- full prompt text
- full answer text
- unnecessary source language
- embeddings unless explicitly justified

This supports longer retention of numerical audit traces while reducing language-retention risk.

## 13. Compact Formula Block

```text
Z_t = [K0(t), S0(t), O0(t), D0(t), I0(t)]
Z_t in [0, 1]^5 where all components are applicable
A_Z(t) = [A_K(t), A_S(t), A_O(t), A_D(t), A_I(t)]

Delta Z_t = Z_t - Z_{t-1}
  where compared components are applicable in both states

Delta2 Z_t = Delta Z_t - Delta Z_{t-1}
  where first-difference values are applicable and comparable

Drift_L1(t) = sum_i |Z_{t,i} - Z_{t-1,i}|
Drift_L1_norm(t) = Drift_L1(t) / 5

Drift_L2(t) = ||Z_t - Z_{t-1}||_2
Drift_L2_norm(t) = Drift_L2(t) / sqrt(5)

A_delta(t) = {i | A_Z_i(t) = 1 and A_Z_i(t-1) = 1}
Drift_L1_active_norm(t)
= sum_{i in A_delta(t)} |Z_{t,i} - Z_{t-1,i}| / |A_delta(t)|
Drift_L2_active_norm(t)
= sqrt(sum_{i in A_delta(t)} (Z_{t,i} - Z_{t-1,i})^2) / sqrt(|A_delta(t)|)

IK(t) = w dot Z_t

if R0(t) >= theta_R0_stable:
    IK_rel(t) may be evaluated
else:
    IK_rel(t) = not_applicable
```

## 14. Variable Reference

| Variable | Semantic role |
| --- | --- |
| `t` | Turn or evaluation-unit index |
| `Z_t` | Numerical KSODI interaction state at `t` |
| `A_Z(t)` | Applicability mask for the five Z components |
| `A_delta(t)` | Shared active component set for comparing `Z_t` and `Z_{t-1}` |
| `K0(t)` | Context component of the state |
| `S0(t)` | Structure component of the state |
| `O0(t)` | Grounding component of the state |
| `D0(t)` | Clarity component of the state |
| `I0(t)` | Information impulse component of the state |
| `Delta Z_t` | Discrete state movement |
| `Delta2 Z_t` | Acceleration of state movement |
| `Z_{t,i}` | Component `i` of the state vector |
| `Drift_L1(t)` | L1 movement magnitude |
| `Drift_L2(t)` | L2 movement magnitude |
| `Drift_L1_active_norm(t)` | Applicability-aware normalized L1 drift |
| `Drift_L2_active_norm(t)` | Applicability-aware normalized L2 drift |
| `ZSigma(W)` | Window aggregation of state vectors |
| `ZSigma(Hangar)` | Distribution view of state-vector window summaries |
| `applicability_rate_Z(W)` | Share of a window where Z is applicable under the active profile |
| `w` | Versioned projection vector for IK |
| `IK(t)` | Scalar projection of `Z_t` |
| `R0(t)` | Gate for dyadic or n-adic comparability |
| `theta_R0_stable` | Stability threshold for opening relational analysis |
| `IK_rel(t)` | Relational projection after stable `R0` |
| `R-family` | Relational and resonance observation family, not a single scalar score |
| `R_geom` | Geometric coupling of dyadic or n-adic trajectories |
| `R_pace` | Pacing dynamics over time |
| `R_geomSigma` | Window aggregation of geometric coupling where `R_geom` is enabled |
| `R_geomSigma(Hangar)` | Hangar distribution view of geometric-coupling patterns |
| `R_paceSigma` | Optional pacing aggregation where pacing dynamics are explicitly defined |
