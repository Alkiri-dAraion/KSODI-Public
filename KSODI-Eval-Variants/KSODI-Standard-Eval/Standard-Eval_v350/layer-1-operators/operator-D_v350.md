# KSODI Operator D0 - Observable Clarity v3.50

Status: canonical workbench version v3.50, aligned with the v3.50 glossary and the 2026-07-04 D-operator clarification.

## 1. Definition

`D0` measures the observable clarity of a text or signal chunk `q` relative to the visible reference space `R`.

In KSODI, clarity is not merely linguistic elegance or grammatical readability. `D0` asks whether an observed signal is clear, distinguishable, locally dense and operationally stable enough to be reconstructed and accepted as a signal inside the current reference space.

`D0` therefore combines three semantic aspects:

- discernibility: the signal can be distinguished from noise, other signals or background ambiguity
- operational connectability: the signal provides enough anchors to be taken up, continued or acted upon
- local signal density / stability: the signal is not too sparse, weak, fragmented or unstable to be reconstructed within the current evaluation unit

`D0` is:

- not a truth measure
- not a style score
- not a personality marker
- not a redundancy reward
- not an information-depth or novelty score

It is a technical metric for observable signal acceptability: whether something is clear enough and sufficiently present to be treated as a reconstructable signal.

## 2. Reference Space

Reference space:

```text
R := {SP, TP, d_1, ..., d_k}
```

where:

- `SP` is the system prompt
- `TP` is the tool or policy profile
- `{d_1, ..., d_k}` is the actually injected retrieval set

Reference-space embedding:

```text
e_R = mean(e(SP), e(TP), e(d_1), ..., e(d_k))
```

If no retrieval is present:

```text
R := {SP, TP}
```

and `e_R` is computed from the available reference elements.

## 3. Components

### 3.1 Reference-Space Coherence

```text
H(q) = cos(e(q), e_R)
```

`H(q)` measures whether the text or signal chunk is semantically aligned with the visible reference basis.

Difference from `O0`:

| Operator | Comparison |
| --- | --- |
| `O0` | answer to individual retrieval / evidence elements |
| `D0` | answer or signal chunk to the whole visible reference space |

### 3.2 Semantic Dispersion

Sentence embeddings:

```text
e(s_i)
```

Mean sentence embedding:

```text
e_mean = mean(e(s_i))
```

Semantic dispersion:

```text
V(q)
= clip(mean(1 - cos(e(s_i), e_mean)), 0, 1)
```

High `V(q)` indicates semantic jumpiness, ambiguity, fragmentation or internal dispersion.

Because cosine can be negative, `1 - cos(...)` can exceed `1`; therefore clipping is required.

### 3.3 Operational Anchors

`L(q)` measures observable operational anchors, counted heuristically.

Examples:

- numbers
- list markers
- explicit constraints
- clear action verbs
- unambiguous output signals
- repeated or reinforced signal units inside the current evaluation unit, where the evaluation configuration explicitly treats them as local signal support

Formula:

```text
L(q) = clip(n_anchor / n_token, 0, 1)
```

Important boundary: `L(q)` must not reward empty repetition or verbosity. Repetition counts only if it increases discernibility, operational connectability or local signal acceptability.

## 4. Minimal Static Formula

```text
D0(q | R)
= clip(alpha_D * H(q)
       + beta_D * L(q)
       - gamma_D * V(q),
       0, 1)
```

Start values:

```text
alpha_D = 0.5
beta_D  = 0.3
gamma_D = 0.2
```

This static formula remains intentionally compact. Repeated occurrence, persistence and density across turns are not forced into `D0` unless the evaluation unit itself explicitly contains repeated signal material and the evaluation configuration declares how this is handled.

## 5. Interpretation

| Value | Meaning |
| --- | --- |
| high | clear, discernible, sufficiently dense / stable and operationally connectable |
| medium | partly clear or locally reconstructable but with ambiguity, sparsity or weak anchors |
| low | jumpy, vague, sparse, noisy, weak, fragmented or hard to operationalize |

A grammatically clear sentence can still receive a lower `D0` if it is too sparse, unstable, ambiguous or weakly anchored to be accepted as a reconstructable signal in the current reference space.

A repeated signal can support `D0` only when the repetition improves reconstruction. Mechanical duplication without added discernibility should be handled as redundancy or structural duplication elsewhere, not as clarity.

## 6. Edge Cases

- If `q` has one sentence or less, set `V(q) = 0` unless the implementation declares a different dispersion policy.
- If no retrieval is present, use `R := {SP, TP}`.
- If `n_token = 0`, `L(q)` is undefined and must be handled by implementation guardrails.
- If repeated signal material appears inside `q`, the configuration must distinguish signal reinforcement from empty duplication.
- If repeated signal material appears across multiple turns, evaluate it through dynamic D observation, `DΣ(W)` and Hangar views, not by silently changing the static `D0` formula.

## 7. Orthogonality

`D0` is semantically distinct from the other KSODI operators:

| Operator | Measures | Difference from D0 |
| --- | --- | --- |
| `K0` | context availability and stability | `D0` evaluates whether the signal is clear and reconstructable inside the visible reference space |
| `S0` | formal structure | `D0` evaluates discernibility and local signal acceptability, not layout or format alone |
| `O0` | grounding and visible attribution | `D0` evaluates internal and reference-space clarity, not external traceability |
| `I0` | information impulse | `D0` evaluates signal acceptability, not novelty, impulse or informational movement |

## 8. Dynamic Form: KSODI-Full

Static `D0` observes one evaluation unit. KSODI-Full may additionally observe how clarity behaves over time.

Dynamic value:

```text
D(t)
= clip(alpha_D * H(t)
       + beta_D * L(t)
       - gamma_D * V(t)
       - delta_D * Delta_ref_drift(t),
       0, 1)
```

with:

```text
Delta_ref_drift(t)
= clip((1 - cos(e_R_{t-1}, e_R_t)) / 2, 0, 1)
```

First difference:

```text
Delta D(t) = D(t) - D(t-1)
```

Second difference:

```text
Delta2 D(t) = Delta D(t) - Delta D(t-1)
```

Optional precision / reinforcement observation:

```text
B_D(t) = max(0, D(t) - D(t-1))
```

`B_D(t)` is not a reward for saying more. It is an optional indicator that the signal became clearer, more discernible or more operationally connectable than in the prior evaluation unit.

## 9. Sigma and Hangar Views

Repeated occurrence or persistence across turns belongs primarily to windowed and Hangar-level D observation.

Window aggregation:

```text
Dbar(W) = (1/n) * sum_{t in W} D(t)
Dmin(W) = min_{t in W} D(t)
Dvar(W) = var({D(t) | t in W})
DΣ(W) = aggregate({D(t), Delta D(t), Delta2 D(t) | t in W})
```

Optional persistence support:

```text
P_D(W) = versioned persistence / reinforcement support inside window W
```

`P_D(W)` is a versioned Full-layer or implementation-specific component. It may describe whether a signal appears often enough, consistently enough or clearly enough across a window to be accepted as a stable pattern. It must not be treated as a universal repetition bonus.

Hangar view:

```text
DΣ(Hangar) = distribution_view({D(t), Delta D(t), Delta2 D(t), P_D(W) | t in W})
```

`DΣ(Hangar)` can show clarity collapse, sparse-signal zones, repeated-but-unclear loops, stable signal corridors, outlier pressure or multi-agent divergence in D over time.

For multi-agent systems, D-Hangar views are important because a single D value may look acceptable while one agent repeatedly fails to produce a signal that the others can reconstruct or accept as stable.

## 10. Privacy and Retention Boundary

D observation should preserve privacy by separating raw language from derived observation data.

Current private working guardrail:

- raw language may be stored only within the declared short retention window, currently treated as 30 days unless Anne defines a different test setting
- long-term observation should preserve vectors, scores, deltas, window summaries, Hangar distributions, configuration metadata and audit-relevant derived values rather than raw language
- long-term vectors and derived metrics may remain useful over months or years for drift, corridor and multi-agent stability analysis
- any use of raw text beyond the declared retention window requires an explicit configuration and explicit approval

This boundary is especially relevant for D because repeated signal occurrence over time can be observed without preserving the full language surface indefinitely.

## 11. Comparability

`D0`, `D(t)`, `Delta D`, `Delta2 D`, `DΣ(W)` and `DΣ(Hangar)` values are comparable only under stable conditions:

- same definition of `R`
- same embedding model `e(.)`
- same sentence segmentation for `V(q)`
- same anchor heuristic for `L(q)`
- same persistence policy for `P_D(W)` where used
- same weights `alpha_D`, `beta_D`, `gamma_D`, `delta_D`
- same eval-unit granularity
- same windowing policy for Sigma variants
- same raw-text retention and derived-data policy where long-term comparison is involved

## 12. Compact Formula Block

```text
R = {SP, TP, d_1, ..., d_k}
e_R = mean(e(SP), e(TP), e(d_1), ...)

H(q) = cos(e(q), e_R)

e_mean = mean(e(s_i))
V(q) = clip(mean(1 - cos(e(s_i), e_mean)), 0, 1)

L(q) = clip(n_anchor / n_token, 0, 1)

D0(q | R)
= clip(alpha_D * H(q)
       + beta_D * L(q)
       - gamma_D * V(q),
       0, 1)

Delta D(t) = D(t) - D(t-1)
Delta2 D(t) = Delta D(t) - Delta D(t-1)
DΣ(W) = aggregate({D(t), Delta D(t), Delta2 D(t) | t in W})
DΣ(Hangar) = distribution_view({D(t), Delta D(t), Delta2 D(t) | t in W})
```

## 13. Variable Reference

| Variable | Semantic role |
| --- | --- |
| `q` | Text or signal chunk whose clarity is evaluated |
| `R` | Visible reference space for clarity evaluation |
| `SP` | System prompt inside the reference space |
| `TP` | Tool or policy profile inside the reference space |
| `d_i` | One retrieval element inside the reference space |
| `e(.)` | Embedding function |
| `e_R` | Mean embedding of the reference space |
| `H(q)` | Reference-space coherence of the signal chunk |
| `s_i` | One sentence or segment in the evaluated signal chunk |
| `e_mean` | Mean sentence or segment embedding |
| `V(q)` | Semantic dispersion, jumpiness or fragmentation |
| `L(q)` | Operational anchor and local signal-support score |
| `n_anchor` | Count of observable operational anchors |
| `n_token` | Token count used for anchor normalization |
| `alpha_D` | Weight of reference coherence |
| `beta_D` | Weight of operational anchors / local signal support |
| `gamma_D` | Weight of semantic dispersion |
| `delta_D` | Weight of reference drift penalty in dynamic D where used |
| `D0(q | R)` | Static observable clarity score |
| `D(t)` | Dynamic observable clarity value at evaluation unit `t` |
| `Delta D(t)` | First difference of dynamic D |
| `Delta2 D(t)` | Second difference / acceleration of dynamic D |
| `DΣ(W)` | Window aggregation of D behavior |
| `DΣ(Hangar)` | Hangar distribution view of D behavior |
| `P_D(W)` | Optional versioned persistence / reinforcement support inside a window |
