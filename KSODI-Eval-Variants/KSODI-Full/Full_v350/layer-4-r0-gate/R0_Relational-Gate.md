# KSODI R0 - Relational Gate / Monadic-to-Dyadic Gate v3.50

Status: public v3.50 reference release; lifted from the private canonical
workbench after the 2026-07-04 Fable review, Fable's 2026-07-19 R0 alignment
pass and the 2026-07-25 R0 public-release decision.

Layer: KSODI Full Layer 4 gate for monadic-to-dyadic or n-adic comparability after `Z`.

## 1. Definition

`R0` is the minimal relational gate for dyadic or n-adic analysis.

It checks whether two or more monadic trajectories are stable enough to be meaningfully compared.

`R0` does not measure full resonance. It measures whether relational or resonance-family analysis may be opened at all.

`R0` is a gate value, not a quality score.

`R0` is a necessary condition for relational analysis, not a sufficient
condition. An open gate means that declared trajectories are stable enough to
compare. It does not by itself prove coupling, resonance, shared intention,
agreement or joint stability.

The fact that trajectories belong together must be declared by the Observer
through an `eval_pair_id`, shared scope, shared evaluation unit or other
versioned pairing metadata. `R0` does not discover the pair. It only checks
whether the declared pair or group is stable enough for later relational layers.

## 2. Position in the KSODI Architecture

The five KSODI operators are calculated first:

```text
K0, S0, O0, D0, I0 -> Z(t)
```

`Z(t)` remains monadic. It may be calculated for one participant, one agent, one system, one trajectory or one observed interaction side.

Relational analysis begins only after at least two distinguishable trajectories are available:

```text
Z_A(t), Delta Z_A(t)
Z_B(t), Delta Z_B(t)
```

Canonical gate sequence:

```text
Z_A, Z_B
Delta Z_A, Delta Z_B
        |
        v
      R0(t)
        |
        v
if R0_clip(t) >= theta_R0_stable:
    IK_rel(t) may be evaluated
    R-family components may be evaluated where their own inputs are available
else:
    IK_rel(t) = not_applicable
    R-family components = not_applicable
```

This prevents KSODI from assigning relational coherence or resonance where no stable shared movement basis has been established.

## 3. Eval Scope

`R0` is calculated per paired evaluation step.

Typical examples:

- human and model trajectories in a chat interaction
- two model trajectories in a multi-agent setting
- two system components whose interaction states are represented as KSODI state vectors
- n-adic extensions where more than two trajectories are compared

The core description is architecture-agnostic. It does not require natural language, audio, chat UI, tool use or a specific model architecture.

Human-chatbot interaction is one implementation case, not the definition of `R0`.

The Observer must declare:

- `eval_pair_id` or n-adic comparison ID
- shared evaluation scope
- trajectory IDs
- component order and operator versions
- applicability / masking policy
- minimum active component policy

## 4. Input Data

For the dyadic case:

```text
Z_A(t), Z_B(t) in [0,1]^5 where components are applicable
Delta Z_A(t) = Z_A(t) - Z_A(t-1)
Delta Z_B(t) = Z_B(t) - Z_B(t-1)
```

where `A` and `B` denote two distinguishable trajectories.

`R0` uses only numerical state vectors and their movement.

It does not use raw text, embeddings, voice data, timing data, identity information, personality inference, semantic direction or intent.

Where `Z` components are masked by applicability rules, `R0` must use the
shared active component set:

```text
A_pair_i(t) = A_delta_A_i(t) AND A_delta_B_i(t)
A_pair(t) = A_delta_A(t) INTERSECT A_delta_B(t)
m_pair(t) = sum_i A_pair_i(t)
```

`A_delta_A(t)` and `A_delta_B(t)` denote the components where `Delta Z` is
valid and comparable for trajectories `A` and `B`.

`min_components_R0` must be at least `1`. A threshold of `0` would make the
relational gate applicable even when no shared component is evaluable and is
therefore invalid.

If:

```text
m_pair(t) < min_components_R0
```

then:

```text
R0(t) = not_applicable
```

Masked components must never be silently coerced to `0`.

## 5. Normalized Drift Magnitudes

`R0` must use normalized drift magnitudes in `[0,1]`.

Raw drift magnitudes are named separately from normalized drift magnitudes.

L1 raw drift:

```text
d_A_L1_raw(t) = sum_i |Delta Z_A_i(t)|
d_B_L1_raw(t) = sum_i |Delta Z_B_i(t)|
```

L1 normalized drift, recommended default:

```text
d_A_norm(t) = d_A_L1_raw(t) / 5
d_B_norm(t) = d_B_L1_raw(t) / 5
```

If applicability masks are active, use the shared active pair set:

```text
d_A_L1_raw_pair(t) = sum_i A_pair_i(t) * |Delta Z_A_i(t)|
d_B_L1_raw_pair(t) = sum_i A_pair_i(t) * |Delta Z_B_i(t)|

d_A_norm(t) = d_A_L1_raw_pair(t) / m_pair(t)
d_B_norm(t) = d_B_L1_raw_pair(t) / m_pair(t)
```

L2 raw drift:

```text
d_A_L2_raw(t) = ||Delta Z_A(t)||_2
d_B_L2_raw(t) = ||Delta Z_B(t)||_2
```

L2 normalized drift, optional geometric analysis norm:

```text
d_A_norm(t) = d_A_L2_raw(t) / sqrt(5)
d_B_norm(t) = d_B_L2_raw(t) / sqrt(5)
```

Masked L2 variant:

```text
d_A_L2_raw_pair(t) = sqrt(sum_i A_pair_i(t) * Delta Z_A_i(t)^2)
d_B_L2_raw_pair(t) = sqrt(sum_i A_pair_i(t) * Delta Z_B_i(t)^2)

d_A_norm(t) = d_A_L2_raw_pair(t) / sqrt(m_pair(t))
d_B_norm(t) = d_B_L2_raw_pair(t) / sqrt(m_pair(t))
```

The selected norm must be versioned.

Do not insert an unnormalized L2 norm into the `R0` formula. Without normalization, `R0` can leave `[0,1]` and the gate interpretation collapses.

Use `L1_norm` when robust, component-readable monitoring is preferred. Use `L2_norm` when peak-sensitive geometric analysis is preferred.

## 6. Minimal Dyadic Definition

For the default dyadic case:

```text
R0_raw(t) = 1 - (d_A_norm(t) + d_B_norm(t)) / 2
```

With clipping:

```text
R0_clip(t) = clip(R0_raw(t), 0, 1)
```

Canonical gate value:

```text
R0(t) := R0_clip(t)
```

Range:

```text
R0(t) in [0,1]
```

Interpretation:

| Signal | Meaning |
| --- | --- |
| `R0 approx 1` | compared trajectories are minimally stable |
| `R0 medium` | shared comparison may be possible but unstable |
| `R0 approx 0` | strong movement; relational analysis should be treated cautiously |
| `R0 < theta_R0_stable` | `IK_rel` and later R-family analysis are not opened |

If both normalized drift magnitudes are `0`, then `R0 = 1`. This means the gate is stable. It does not mean the interaction is resonant in the full sense.

If two trajectories are static but unrelated, `R0` can still open by design.
This does not prove connection. It only says that the declared trajectories are
stable enough for later relational checks. Coupling is evaluated later by
`IK_rel`, `R_geom`, `R_pace` or other explicitly defined R-family components.

Under the dyadic L1 default with valid normalization, clipping should not bind.
It is retained as a defensive guard against implementation or policy violations.

## 6.1 Documented Limitation: Mean-Based Aggregation

The default `R0` definition aggregates normalized drift magnitudes by
averaging. This choice is simple, readable and auditable, but it has a known
limitation that must not be discovered by accident:

Averaging can mask one-sided instability.

Dyadic example:

```text
d_A_norm(t) = 0.0    (trajectory A is static)
d_B_norm(t) = 0.8    (trajectory B moves strongly)

R0(t) = 1 - (0.0 + 0.8) / 2 = 0.6
```

Depending on `theta_R0_stable`, the gate may open although one side of the
comparison is highly unstable.

In the n-adic variant the effect grows with `n`: a single unstable trajectory
among many stable ones contributes only `1/n` of its drift to the gate value
and can disappear into the average.

Why this is accepted in v3.50:

- `R0` is a necessary, not a sufficient condition. It opens relational
  analysis; it does not certify coupling or joint stability.
- One-sided instability that passes the gate remains visible in the monadic
  layer of the affected trajectory (`Delta Z`, `Delta2 Z`, drift norms) and in
  later relational layers.
- The mean keeps the gate expression minimal, transparent and comparable across
  dyadic and n-adic cases.

Operational consequence:

`R0` gate status must always be read together with the per-trajectory
normalized drift magnitudes `d_j_norm(t)`, which are part of the recommended
storage. A gate that opens over strongly asymmetric drift is a signal in itself
and may be flagged by the implementation profile.

Future work, not active v3.50:

```text
R0_strict_raw(t) = 1 - max_j d_j_norm(t)
R0_strict(t) = clip(R0_strict_raw(t), 0, 1)
```

`R0_strict` opens the gate only if every compared trajectory is individually
stable. It is stricter, less forgiving toward asymmetric constellations and
loses the readable "average movement" semantics. Whether `R0_strict`, the
weighted variant `R0_w` or a per-trajectory threshold policy is the better
answer for asymmetric systems is an empirical question and belongs to a later
version. It must not be inferred as active v3.50 behavior.

## 7. Weighted Variant

For asymmetric systems:

```text
R0_w_raw(t) = 1 - (w_A * d_A_norm(t) + w_B * d_B_norm(t))
R0_w(t) = clip(R0_w_raw(t), 0, 1)
```

with:

```text
w_A >= 0
w_B >= 0
w_A + w_B = 1
```

This may be useful when one trajectory is expected to move more strongly than the other, for example in human-model interaction.

Weights must be versioned.

## 8. N-Adic Variant

For `n` trajectories:

```text
R0_n_raw(t) = 1 - (1/n) * sum_j d_j_norm(t)
R0_n(t) = clip(R0_n_raw(t), 0, 1)
```

where every `d_j_norm(t)` is a normalized drift magnitude in `[0,1]` under the same versioned norm policy.

This supports multi-agent or multi-participant observation.

If applicability masks are active, the shared active set is the intersection
over all compared trajectories:

```text
A_group(t) = INTERSECT_j A_delta_j(t)
m_group(t) = sum_i A_group_i(t)
```

The same lower-bound rule applies here: `min_components_R0` must be at least
`1`.

If:

```text
m_group(t) < min_components_R0
```

then:

```text
R0_n(t) = not_applicable
```

The n-adic denominator must use the declared active component count, not the
full five-component state space unless all five components are applicable for
all compared trajectories.

## 9. What R0 Does Not Measure

`R0` does not measure:

- semantic agreement
- resonance in the full sense
- structural coupling
- directional coupling
- future signal-media coupling
- temporal lag or lead relation
- pacing
- voice
- harmony
- truth
- correctness
- usefulness
- compliance

Most importantly:

```text
R0 is independent of semantic direction, meaning and coupling.
```

Directional and geometric coupling belong to `R_geom` or later R-family layers.

Readable-language or sign-visible pacing belongs to `R_pace` only where the
pacing structure is explicitly defined. Audio, radio, Morse-like signals,
frequency-like patterns and wave/signal forms belong to future signal-media /
Layer 8 work, not to active v3.50 `R0`.

## 10. Relation to IK_rel

`IK_rel` is gated by `R0`.

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

This is methodically important because two monadic trajectories may each be internally coherent while no stable shared movement basis exists.

Without `R0`, `IK_rel` could falsely assign relational coherence to trajectories that should not yet be compared.

## 11. Relation to R_full

`R0` opens the relational branch.

It does not define the R_full family.

After a stable `R0` gate, later layers may observe:

- `IK_rel`: relational projection compatibility
- `R_geom`: geometric coupling of trajectories
- `R_pace`: readable-language or sign-visible pacing dynamics where explicitly defined
- future signal-media extension: audio, radio, Morse-like, frequency-like or
  wave/signal forms, not active v3.50
- `R_geomSigma`: aggregated geometric-coupling behavior over windows
- `R_geomSigma(Hangar)`: distribution of geometric-coupling patterns inside an
  observation space
- `R_paceSigma`: optional pacing aggregation where pacing dynamics are
  explicitly defined

## 12. Sigma and Hangar

`R0Sigma` aggregates applicable `R0` values over an observation window.

```text
W_app = {t in W | R0(t) != not_applicable}
R0Sigma(W) = aggregate({R0(t) | t in W_app})
```

`W_app` excludes samples where the relational comparison is not applicable.
These samples must be reported through an applicability rate and must not be
counted as gate closures.

Possible aggregate functions:

- mean
- median
- percentile profile
- share of steps above `theta_R0_stable`
- share of gate closures among applicable samples

The share of gate closures counts only evaluated, applicable `R0` results that
closed the gate. This distinguishes an applicable-but-closed relation from a
relation that could not be evaluated because the shared active component set was
insufficient.

`R0Sigma(Hangar)` observes the distribution of such gate patterns across windows, sessions or participant constellations:

```text
R0Sigma(Hangar) = distribution({R0Sigma(W_i)})
```

`R0Sigma` answers:

```text
Did dyadic comparability remain open across this window?
```

`R0Sigma(Hangar)` answers:

```text
How do gate patterns distribute across observation spaces?
```

`Delta R0` and `Delta2 R0` may be used where gate stability itself is monitored:

```text
Delta R0(t) = R0(t) - R0(t-1)
Delta2 R0(t) = Delta R0(t) - Delta R0(t-1)
```

When `R0(t)` or `R0(t-1)` is `not_applicable`, the corresponding delta is
`not_applicable` unless an implementation profile defines a separate gate-state
transition marker.

For broader Sigma / Hangar policy, use the shared public method note
[`Hangar_350.md`](../../../Hangar_350.md).

## 13. Edge Cases

For the first evaluation step:

```text
R0(1) = not_applicable
```

because `Delta Z(1)` is not defined unless a prior state exists.

If one trajectory is missing:

```text
R0(t) = not_applicable
```

If one trajectory is present but not comparable because of incompatible scope, version or granularity:

```text
R0(t) = not_applicable
```

## 14. Comparability

`R0` values are comparable only under stable conditions:

- same operator definitions
- same operator versions
- same ordering of components in `Z`
- same eval-unit granularity
- same context scope
- same norm choice
- same normalization rule
- same applicability / masking policy
- same `min_components_R0` policy
- same clipping rule
- same threshold policy for `theta_R0_stable`
- same weighting configuration where weights are used

## 15. Storage Principle

Recommended storage:

- `eval_pair_id`
- `context_scope_id`
- `trajectory_ids`
- n-adic comparison ID where applicable
- `operator_version_ids`
- `Z_A(t)`, `Z_B(t)` or references to stored state vectors
- `Delta Z_A(t)`, `Delta Z_B(t)` or references to stored state movement
- applicability masks `A_delta_A(t)`, `A_delta_B(t)`
- shared active set `A_pair(t)` or `A_group(t)`
- active component count and applicability rate
- `min_components_R0`
- norm choice and normalization rule
- raw drift magnitudes where useful
- normalized drift magnitudes `d_A_norm(t)`, `d_B_norm(t)`
- `R0_raw(t)` where useful
- `R0(t)` / `R0_clip(t)`
- `theta_R0_stable`
- gate status
- optional `Delta R0(t)` / `Delta2 R0(t)` where gate stability is monitored
- detector and configuration IDs

Implementation-profile future work:

- gate flapping near `theta_R0_stable`
- optional hysteresis such as `theta_open > theta_close`
- asymmetric-drift flags where `R0` opens despite high movement in one
  trajectory

Avoid storing:

- full prompt text
- full answer text
- unnecessary source language
- embeddings unless explicitly justified
- voice or timing data in `R0`

## 16. Compact Formula Block

```text
Delta Z_A(t) = Z_A(t) - Z_A(t-1)
Delta Z_B(t) = Z_B(t) - Z_B(t-1)

A_pair_i(t) = A_delta_A_i(t) AND A_delta_B_i(t)
m_pair(t) = sum_i A_pair_i(t)

if m_pair(t) < min_components_R0:
    R0(t) = not_applicable

d_A_L1_raw_pair(t) = sum_i A_pair_i(t) * |Delta Z_A_i(t)|
d_B_L1_raw_pair(t) = sum_i A_pair_i(t) * |Delta Z_B_i(t)|

d_A_norm(t) = d_A_L1_raw_pair(t) / m_pair(t)
d_B_norm(t) = d_B_L1_raw_pair(t) / m_pair(t)

# Optional L2-normalized policy:
# d_A_norm(t) = sqrt(sum_i A_pair_i(t) * Delta Z_A_i(t)^2) / sqrt(m_pair(t))
# d_B_norm(t) = sqrt(sum_i A_pair_i(t) * Delta Z_B_i(t)^2) / sqrt(m_pair(t))

R0_raw(t) = 1 - (d_A_norm(t) + d_B_norm(t)) / 2
R0_clip(t) = clip(R0_raw(t), 0, 1)
R0(t) := R0_clip(t)

if R0(t) >= theta_R0_stable:
    IK_rel(t) may be evaluated
else:
    IK_rel(t) = not_applicable

W_app = {t in W | R0(t) != not_applicable}
R0Sigma(W) = aggregate({R0(t) | t in W_app})
R0Sigma(Hangar) = distribution({R0Sigma(W_i)})
```

## 17. Variable Reference

| Variable | Semantic role |
| --- | --- |
| `t` | Turn or evaluation-unit index |
| `A`, `B` | Two distinguishable trajectories |
| `Z_A(t)`, `Z_B(t)` | State vectors of the compared trajectories |
| `Delta Z_A(t)`, `Delta Z_B(t)` | Movement of each trajectory |
| `d_A_L1_raw(t)`, `d_B_L1_raw(t)` | Raw L1 drift magnitudes |
| `d_A_L2_raw(t)`, `d_B_L2_raw(t)` | Raw L2 drift magnitudes |
| `A_delta_A(t)`, `A_delta_B(t)` | Delta-valid applicability masks for compared trajectories |
| `A_pair(t)` | Shared active component set for dyadic comparison |
| `A_group(t)` | Shared active component set for n-adic comparison |
| `m_pair(t)`, `m_group(t)` | Number of active shared components |
| `min_components_R0` | Minimum active components required for gate evaluation |
| `d_A_norm(t)`, `d_B_norm(t)` | Normalized drift magnitudes in `[0,1]` |
| `R0_raw(t)` | Unclipped gate expression |
| `R0(t)` / `R0_clip(t)` | Minimal relational gate for dyadic or n-adic comparability |
| `theta_R0_stable` | Stability threshold for opening relational analysis |
| `R0_w(t)` | Weighted dyadic R0 variant |
| `R0_n(t)` | N-adic R0 variant |
| `Delta R0(t)` | Change in gate value where consecutive applicable values exist |
| `Delta2 R0(t)` | Acceleration of gate-value movement where comparable deltas exist |
| `R0Sigma(W)` | Aggregated R0 behavior across a window |
| `R0Sigma(Hangar)` | Distribution of R0 window patterns |
| `IK_rel(t)` | Relational projection after stable R0 gate |
