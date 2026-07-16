# KSODI Operator I0 - Observable Information Impulse v3.50

Status: canonical workbench version v3.50, updated after the 2026-07-04 Fable review. Dynamic / Sigma / Hangar reminders were added for operator-level monitoring alignment.

Layer: KSODI Standard-Eval operator. Static `I0` belongs to Layer 1. Operator-level Delta / Delta2, Sigma and Hangar views may observe information-impulse movement over time. Relational feedback and controller logic belong outside the static Layer-1 operator definition.

## 1. Definition

`I0` measures the observable information impulse of a chunk `q` relative to a turn-specific reference space `Ref_t`.

It is drift-neutral and non-normative. A low value is not a failure. Repetition can indicate stability, confirmation, repair or deliberate anchoring.

`I0` does not measure truth, usefulness, creativity, semantic correctness, compliance or human value. It measures observable informational movement relative to the declared reference space: whether something update-relevant is added, compressed or direction-changing enough that a receiver has reason to account for it.

The earlier "Information Depth" intuition is preserved only in this non-evaluative sense. `I0` asks whether the signal contributes an observable information difference relative to what is already present in `Ref_t`. It does not claim that the sender is deep, valuable or correct.

`I0` consists of two components:

- `J_dir_norm`: normalized directional impulse relative to the reference space
- `G_info` or `G_proxy_ret`: relational information content, meaning novelty or compression relative to the reference space, not utility

Sender / receiver boundary:

- Sender-side KSODI may explain sendability in the order `K/S/O/D/I`.
- Receiver-side reconstruction may begin with `I` because an observable information impulse must first be noticed before it can be clarified, grounded, structurally reconstructed and situated.
- This does not turn `I0` back into the old "Information Depth" label. In v3.50, `I0` remains observable information impulse relative to `Ref_t`: the minimal observable addition that makes receiver-side reconstruction worth continuing.

## 2. Eval Scope

Observable per turn `t`:

- user chunk `u_t`
- assistant chunk `a_t`
- evaluated chunk `q`, usually `u_t` or `a_t`
- system prompt `SP`
- tool or policy profile `TP`, optional
- retrieval set `RET_k(u_t) = {d_1, ..., d_k}` actually injected into the prompt

Turn-specific reference space:

```text
Ref_t := {SP, TP, d_1, ..., d_k}
```

Reference-space embedding:

```text
e_Ref_t = mean(e(SP), e(TP), e(d_1), ..., e(d_k))
```

If no retrieval is present:

```text
Ref_t := {SP, TP}
```

and `e_Ref_t` is computed from the available reference elements.

Important boundary:

```text
RET_k(u_t) = empty
```

makes the retrieval-based proxy `G_proxy_ret` not applicable. It must not be silently evaluated as `0` or `1`. The final project policy for retrieval-empty handling remains pending review.

Until Anne reviews the earlier `RET_k = empty` solution, implementations must store an explicit flag such as:

```text
retrieval_proxy_status = no_retrieval
```

and document whether the active MVP fallback uses `J_dir_norm` alone.

## 3. Normalized Cosine Distance

Cosine similarity lies in `[-1, 1]`. Therefore the raw expression `1 - cos(...)` lies in `[0, 2]` and cannot be used directly as a KSODI state component.

Canonical normalized cosine distance:

```text
d_cos(x, y) = clip((1 - cos(e(x), e(y))) / 2, 0, 1)
```

All `I0` components that enter `Z(t)` must be normalized to `[0, 1]`.

## 4. Components

### 4.1 Directional Impulse

```text
J_dir_norm(q | Ref_t) = clip((1 - cos(e(q), e_Ref_t)) / 2, 0, 1)
```

Interpretation:

| Value | Meaning |
| --- | --- |
| `approx 0` | low directional change relative to `Ref_t` |
| `approx 1` | strong directional change relative to `Ref_t` |

### 4.2 Relational Information Content

Conceptual form:

```text
G_info(q | Ref_t)
= (N_new(q, Ref_t) + N_compressed(q, Ref_t)) / N_total(q)
```

Concepts are semantic equivalence classes, for example via embedding clusters, not tokens.

### 4.3 MVP Retrieval Proxy For G_info

Production-oriented approximation over the actually used retrieval:

```text
G_proxy_ret(q | Ref_t)
= clip((1 - max_{d in RET_k(u_t)} cos(e(q), e(d))) / 2, 0, 1)
```

This proxy is auditable through retrieval IDs.

If `RET_k(u_t)` is empty:

```text
G_proxy_ret(q | Ref_t) = not_applicable
retrieval_proxy_status = no_retrieval
```

## 5. Minimal Formula

Conceptual formula:

```text
I0(q | Ref_t)
= eta * G_info(q | Ref_t)
  + (1 - eta) * J_dir_norm(q | Ref_t)
```

with:

```text
eta in [0, 1]
I0(q | Ref_t) in [0, 1]
```

MVP implementation when retrieval proxy is applicable:

```text
I0(q | Ref_t)
= eta * G_proxy_ret(q | Ref_t)
  + (1 - eta) * J_dir_norm(q | Ref_t)
```

MVP interim fallback when retrieval proxy is not applicable:

```text
I0(q | Ref_t) = J_dir_norm(q | Ref_t)
```

with explicit flag:

```text
retrieval_proxy_status = no_retrieval
```

This fallback is not a final method claim. It is a controlled implementation guardrail until the intended `RET_k = empty` policy is reviewed.

## 6. Optional Extended Variant

Optional masking model:

```text
I_star(t)
= A_I(t) * I(t) * (1 - epsilon * sigma_I2(t))
```

with:

```text
A_I(t) in {0, 1}
sigma_I2(t) in [0, 1]
epsilon in [0, 1]
```

Circularity rule: gates and masks must be determined exogenously, without reference to `I(t)`.

## 7. Interpretation

| Value | Meaning |
| --- | --- |
| high | strong observable impulse or strong deviation from the reference space |
| medium | moderate impulse |
| low | low change; repetition or stabilization may be present |

Important: low does not mean wrong.

## 8. Comparability

`I0` values are comparable only under stable conditions:

- same definition of `Ref_t`
- same embedding model `e(.)`
- same retrieval strategy, including Top-k and injected documents
- same retrieval-empty policy
- same `eta`
- same proxy or cluster definition, if `G_info` is implemented conceptually
- same normalization rule for cosine distance

Values with `retrieval_proxy_status = no_retrieval` must not be compared naively with retrieval-backed values unless the comparison explicitly accounts for that status.

## 9. Dynamic Form: KSODI-Full

Define a turn representation `s_t`, for example an embedding of a defined turn container.

Dynamic directional impulse:

```text
J_dir_norm(t) = clip((1 - cos(s_{t-1}, s_t)) / 2, 0, 1)
```

Dynamic information content with exogenous gate `alpha(t)`:

```text
G_info(t)
= ((N_new(t) + N_compressed(t)) / N_total(t)) * alpha(t)
```

Circularity rule: `alpha(t)` is exogenous and must be determined without reference to `I(t)`, for example from fixed rules or from other operator states outside the I calculation.

Dynamic form:

```text
I(t) = eta * G_info(t) + (1 - eta) * J_dir_norm(t)
```

## 10. Operator-Level Delta / Sigma / Hangar Reminder

Like the D-operator pattern, static `I0` remains a value for one declared evaluation unit. Information impulse persistence, collapse, oscillation or bursts over time should be observed through operator-level change and aggregation views rather than by silently changing the static `I0` formula.

```text
Delta I(t) = I(t) - I(t-1)
Delta2 I(t) = Delta I(t) - Delta I(t-1)
IΣ(W) = aggregate({I(t), Delta I(t), Delta2 I(t) | t in W})
IΣ(Hangar) = distribution_view({I(t), Delta I(t), Delta2 I(t) | t in W})
```

Do not confuse this generic operator-level `Delta I(t)` with the existing `Delta I_t` drift indicator below, which compares an answer-side impulse to a prior window median. Also do not confuse any I-specific standardization with the KSODI state vector `Z(t)`.

## 11. Drift Indication

Window `W` with size `w`:

```text
Delta I_t
= |I_a(t) - median(I_a(t-w), ..., I_a(t-1))|
```

Standardization:

```text
Z_I_internal_t
= (I_a(t) - mu_W) / (sigma_W + epsilon_stab)
```

This is drift indication only, not evaluation.

`Z_I_internal_t` is operator-internal notation and must not be confused with the KSODI state vector `Z(t)`.

## 12. Compact Formula Block

```text
Ref_t = {SP, TP, d_1, ..., d_k}, where {d} = RET_k(u_t)
e_Ref_t = mean(e(SP), e(TP), e(d_1), ...)

d_cos(x, y) = clip((1 - cos(e(x), e(y))) / 2, 0, 1)

J_dir_norm(q | Ref_t) = clip((1 - cos(e(q), e_Ref_t)) / 2, 0, 1)

if RET_k(u_t) is not empty:
    G_proxy_ret(q | Ref_t)
    = clip((1 - max_{d in RET_k(u_t)} cos(e(q), e(d))) / 2, 0, 1)
else:
    G_proxy_ret(q | Ref_t) = not_applicable
    retrieval_proxy_status = no_retrieval

if G_proxy_ret is applicable:
    I0(q | Ref_t) = eta * G_proxy_ret(q | Ref_t) + (1 - eta) * J_dir_norm(q | Ref_t)
else:
    I0(q | Ref_t) = J_dir_norm(q | Ref_t)   # interim MVP fallback, policy pending

I0(q | Ref_t) in [0, 1]

J_dir_norm(t) = clip((1 - cos(s_{t-1}, s_t)) / 2, 0, 1)
I(t) = eta * G_info(t) + (1 - eta) * J_dir_norm(t)

Delta I(t) = I(t) - I(t-1)
Delta2 I(t) = Delta I(t) - Delta I(t-1)
IΣ(W) = aggregate({I(t), Delta I(t), Delta2 I(t) | t in W})
IΣ(Hangar) = distribution_view({I(t), Delta I(t), Delta2 I(t) | t in W})

Delta I_t = |I_a(t) - median(I_a(t-w), ..., I_a(t-1))|
Z_I_internal_t = (I_a(t) - mu_W) / (sigma_W + epsilon_stab)
```

## 13. Variable Reference

| Variable | Semantic role |
| --- | --- |
| `q` | Chunk whose information impulse is evaluated |
| `t` | Turn index |
| `u_t` | User chunk at turn `t` |
| `a_t` | Assistant chunk at turn `t` |
| `Ref_t` | Turn-specific reference space |
| `RET_k(u_t)` | Injected Top-k retrieval set for the user chunk |
| `retrieval_proxy_status` | Implementation flag for retrieval-backed or retrieval-empty proxy state |
| `e(.)` | Embedding function |
| `e_Ref_t` | Mean embedding of the turn-specific reference space |
| `d_cos(x, y)` | Normalized cosine distance in `[0,1]` |
| `J_dir_norm(q \| Ref_t)` | Normalized directional impulse relative to reference space |
| `G_info(q \| Ref_t)` | Conceptual relational information content |
| `G_proxy_ret(q \| Ref_t)` | Auditable retrieval-based proxy for information content |
| `eta` | Mixture weight between information content and directional impulse |
| `I0(q \| Ref_t)` | Static information impulse in `[0,1]` |
| `I(t)` | Dynamic information impulse value |
| `Delta I(t)` | First difference of dynamic I over time |
| `Delta2 I(t)` | Second difference / acceleration of dynamic I |
| `IΣ(W)` | Window aggregation of I behavior |
| `IΣ(Hangar)` | Hangar distribution view of I behavior |
| `A_I(t)` | Optional exogenous gate for information impulse |
| `sigma_I2(t)` | Optional uncertainty term for information impulse |
| `epsilon` | Weight of the uncertainty penalty |
| `s_t` | Dynamic turn representation |
| `Delta I_t` | Window-median drift indication for information impulse |
| `Z_I_internal_t` | Operator-internal standardized I value, not the KSODI state vector `Z` |
