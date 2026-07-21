# KSODI Operator K0 - Observable Context Completeness v3.50

Status: public v3.50 reference release; private canonical workbench origin retained. Lifted from the canonical v3.42 K operator after Fable Pilot 3 v2, the 2026-07-20 K0 hardening pass and Anne's 2026-07-21 public-release decision.

Layer: KSODI Standard-Eval operator. Static `K0` belongs to Layer 1. Operator-level Delta / Delta2, Sigma and Hangar views may observe context movement over time. Relational feedback and controller logic belong outside the static Layer-1 operator definition.

## 1. Definition

`K0` measures observable context completeness inside a declared evaluation scope.

Context is not information itself. It is the structural condition under which information, grounding, clarity and structure become interpretable.

`K0` does not measure:

- model intelligence
- semantic understanding
- truth
- grounding or source use
- answer quality
- implicit memory outside the declared scope
- previous turns outside the defined evaluation scope

`K0` is a setup and observability score, not a model score.

## 2. Eval Scope

Before calculation, the context container and context profile must be explicitly defined.

Minimal v3.50 scope classes:

```text
scope = {
  system_context,
  developer_or_project_context,
  account_or_workspace_context,
  user_prompt,
  retrieved_context,
  files_or_assets,
  visible_memory_or_session_state,
  tool_availability,
  tool_output,
  governance_or_policy_material
}
```

Profiles do not need to use every class. They must declare which context classes are expected for the evaluation unit.

Optional metadata:

- `scope_id`
- `scope_profile_id`
- `chunk_range`
- detector version
- feature profile version
- optional feature weights
- applicability policy

Everything outside the declared scope is ignored for `K0`.

This is methodical: `K0` evaluates context provisioning inside the declared evaluation unit only.

Important boundary:

- Tool availability belongs to K context.
- Tool output may become evidence or reference material for `O0` only under the active evaluation profile.
- Files, assets, examples and retrieved material may support K as available context, but O asks whether an answer is grounded relative to the declared `Ref`.

## 3. Context Feature Set

The Standard-Eval context feature set is versioned:

```text
Cset = {G, P, A, X, F, L}
```

| Feature | Meaning | Guiding question |
| --- | --- | --- |
| `G` | Goal | Is the task goal explicitly named? |
| `P` | Perspective | Is a role or perspective explicitly defined? |
| `A` | Assets / available material | Are data, sources, examples, files, retrieved chunks or other inputs present where expected? |
| `X` | Constraints | Are rules, limits, exclusions, policies or conditions present where expected? |
| `F` | Format | Is the expected output form specified where expected? |
| `L` | Tools / capabilities | Are available tools or capabilities explicitly defined where expected? |

Individual features are denoted:

```text
c_i in Cset
```

Expected feature profile:

```text
Cset_exp(profile) subseteq Cset
```

`Cset_exp(profile)` declares which K features are expected for the evaluation unit. This prevents absent-but-not-required features from being silently treated as failures.

The feature set and expected-feature profile must be versioned for reproducibility.

The mapping from `Cset` features to scope classes belongs to the declared
detector profile. For example, a `G` marker may be searched in `user_prompt`,
`system_context` or `developer_or_project_context` depending on the profile;
the K operator itself does not hard-code that mapping.

## 4. Indicator Function

For every expected context feature `c_i`:

```text
1_ci = 1, if feature c_i is explicitly present in scope
1_ci = 0, if feature c_i is expected but absent from scope
```

For a feature that is not expected under the active profile:

```text
1_ci = not_applicable
```

The MVP detector uses:

- no LLM calls
- no semantic interpretation
- explicit markers only

This keeps `K0` transparent, auditable and independently implementable.

Later implementation profiles may add graded markers:

```text
k_i in [0, 1]
```

The binary `1_ci` form remains the default transparent MVP detector.

## 5. Initial Context Completeness

Unweighted applicability-aware Standard-Eval formula:

```text
K_active(q) = {c_i in Cset_exp(profile) | c_i is applicable}

K0(q)
= (1 / |K_active(q)|) * sum_{c_i in K_active(q)} 1_ci
```

If `K_active(q)` is empty:

```text
K0(q) = not_applicable
```

with:

```text
K0(q) in [0, 1] / not_applicable
```

Interpretation:

| Value | Meaning |
| --- | --- |
| `approx 1` | expected context is fully specified under the active profile |
| `approx 0.5` | relevant expected context gaps |
| `< 0.4` | context insufficient; evaluation reliability limited |
| `not_applicable` | no context feature is expected or applicable under the active profile |

These interpretation bands are profile-relative. With the transparent MVP
detector, binary feature markers and a small expected feature set, `K0` is
discrete rather than continuous; some numeric intervals may be unoccupied under
that profile.

Important fairness rule:

If `K0` is low, low values in `S0`, `O0`, `D0` or `I0` must not be used unfairly against the model. Missing setup conditions and model behavior must remain separated.

Applicability note:

Missing, unavailable or non-visible context should be carried as explicit metadata, not silently converted into model failure. Downstream `Z`, `IK`, drift and aggregation views must respect the declared applicability policy.

## 6. Weighted Variant

Optional, versioned variant:

```text
K0_w(q)
= (sum_i w_i * 1_ci) / (sum_i w_i)
  for c_i in K_active(q)
```

with:

```text
w_i > 0
```

If `K_active(q)` is empty:

```text
K0_w(q) = not_applicable
```

Weights must be versioned for auditability.

The unweighted formula remains the default Standard-Eval form.

## 7. Detection Heuristics

Examples for explicit marker detection:

| Feature | Possible explicit markers |
| --- | --- |
| `G` | task verbs such as "analyze", "explain", "compare", "summarize"; explicit task statement |
| `P` | phrases such as "as ...", "you are ..."; named role or standpoint |
| `A` | `retrieved_docs.length > 0`; examples; pasted data; files; source excerpts |
| `X` | "only", "maximum", "do not", "rule", "constraint", explicit boundary |
| `F` | "JSON", "table", "list", "steps", "output format", required headings |
| `L` | non-empty tool profile; explicit tool or capability mention |

Detector details belong to the implementation profile.

The detection table is intentionally implementation-friendly. It is not a semantic completeness proof.

## 8. Comparability

`K0` values are comparable only under stable conditions:

- same `scope_id` logic
- same scope class mapping
- same feature set `Cset`
- same expected-feature profile `Cset_exp(profile)`
- same detector version
- same weighting choice
- same applicability policy
- same scope construction rules

Not comparable:

- implicit context reconstruction
- changing feature definitions
- hidden session memory
- different detector versions
- different expected-feature profiles
- tool output treated as K in one profile and as O evidence in another

## 9. Orthogonality / Non-Redundancy Boundary

The five base operators are semantically distinct and functionally non-redundant. This is not a claim of proven mathematical orthogonality.

| Operator | Measures | Difference from K0 |
| --- | --- | --- |
| `S0` | observable structural coherence | `K0` evaluates provided context, not answer structure |
| `O0` | grounding in a visible reference space | `K0` asks whether relevant material is visible or available; `O0` asks whether the answer is grounded relative to declared `Ref` |
| `D0` | observable clarity, discernibility, operational connectability and sufficient local signal density / stability | `K0` evaluates setup conditions, not signal discernibility or local clarity |
| `I0` | observable information impulse | `K0` evaluates context availability, not novelty or information movement |

## 10. Dynamic Context Stability

Static `K0` remains a value for one declared evaluation unit.

If an implementation needs to monitor drift of the declared context scope itself, use an explicitly named scope-drift diagnostic:

```text
Delta_scope_drift(t)
= clip(dist_scope(scope_0, scope_t), 0, 1)

scope_stability(t) = 1 - Delta_scope_drift(t)
```

where `dist_scope` is a versioned normalized distance between the baseline scope and the current scope under the declared scope profile.

`Delta_scope_drift(t)` is not the same as operator-level `Delta K(t)`.

## 11. Context Gate and Uncertainty Penalty

Optional adjusted context value:

```text
G_K(t) in {0, 1}
sigma_K2(t) in [0, 1]
0 <= beta_K <= 1
```

```text
K0_ext(t)
= G_K(t) * K0(t) * (1 - beta_K * sigma_K2(t))
```

This allows unavailable or ambiguous context states to be masked or penalized under a declared implementation profile.

`G_K(t)`, `sigma_K2(t)` and `beta_K` are workbench / implementation-profile parameters, not empirical constants.

`G_K(t)` is the K-internal context gate. It must not be confused with
`A_K(t)` as the K component of the Layer-2 applicability mask `A_Z(t)`. A
profile may define `A_K(t)` from this gate, but the gate itself must not
silently turn unavailable context into the numeric value `0`.

If `G_K(t) = 0` or `K0(t) = not_applicable`, then:

```text
K0_ext(t) = not_applicable
```

## 12. Removed Recursive System Form

Earlier drafts used a recursive context-update form that mixed K with the
relational / resonance branch.

This form is not active in the v3.50 `K0` operator file.

Reason:

- bare relational symbols conflict with the v3.50 `R` / `Ref` boundary
- relational and resonance-family feedback belongs to KSODI-Full, not to the static Layer-1 K operator
- controller feedback must be separated from observation by a governance / controller boundary

If a later controller or Full-layer model needs a recursive K update, it must be specified in a separate controller / Full-layer note without overloading `R`.

## 13. Operator-Level Delta / Sigma / Hangar Reminder

For a time-indexed stream, `K(t)` denotes `K0(q_t)` under the active context profile.

Context persistence, collapse or recovery over time should be observed through operator-level change and aggregation views rather than by silently changing the static `K0` formula.

```text
Delta K(t) = K(t) - K(t-1)
Delta2 K(t) = Delta K(t) - Delta K(t-1)
KΣ(W) = aggregate({K(t), Delta K(t), Delta2 K(t) | t in W_app})
KΣ(Hangar) = distribution_view({K(t), Delta K(t), Delta2 K(t) | t in W_app})
```

`W_app` denotes the subset of the window where `K` is applicable under the active context profile.

`Delta K(t)` is only defined where both `K(t)` and the comparison value `K(t-1)` are applicable under the same context profile. Otherwise the delta view records `not_applicable` or skips the pair according to the declared window policy.

## 14. Implementation Note

Minimal container shape:

```text
input:
  scope_id
  scope_profile_id
  system_context
  developer_or_project_context
  account_or_workspace_context
  user_prompt
  retrieved_context
  files_or_assets
  visible_memory_or_session_state
  tool_availability
  tool_output
  governance_or_policy_material

output:
  K0
  K0_w optional
  K0_ext optional
  feature_flags
  expected_profile
  applicability_mask
  missing_reason
  detector_version
  feature_profile_version
```

Tool output should be stored separately from tool availability so that O can later decide whether the output is part of `Ref`.

## 15. Compact Formula Block

```text
Cset = {G, P, A, X, F, L}
Cset_exp(profile) subseteq Cset

1_ci = 1 if expected feature c_i exists in scope
1_ci = 0 if expected feature c_i is absent from scope
1_ci = not_applicable if c_i is not expected under the active profile

K_active(q) = {c_i in Cset_exp(profile) | c_i is applicable}

K0(q)
= (1 / |K_active(q)|) * sum_{c_i in K_active(q)} 1_ci

if K_active(q) is empty:
    K0(q) = not_applicable

K0_w(q)
= (sum_i w_i * 1_ci) / (sum_i w_i)
  for c_i in K_active(q)

Delta_scope_drift(t)
= clip(dist_scope(scope_0, scope_t), 0, 1)

scope_stability(t) = 1 - Delta_scope_drift(t)

K0_ext(t)
= G_K(t) * K0(t) * (1 - beta_K * sigma_K2(t))
  where K0(t) is applicable
  and G_K(t) = 1

if G_K(t) = 0:
    K0_ext(t) = not_applicable

Delta K(t) = K(t) - K(t-1)
  where both values are applicable under the same context profile

Delta2 K(t) = Delta K(t) - Delta K(t-1)
KΣ(W) = aggregate({K(t), Delta K(t), Delta2 K(t) | t in W_app})
KΣ(Hangar) = distribution_view({K(t), Delta K(t), Delta2 K(t) | t in W_app})
```

## 16. Variable Reference

| Variable | Semantic role |
| --- | --- |
| `scope` | Declared context container used for evaluation |
| `scope_profile_id` | Versioned context profile identifier |
| `Cset` | Versioned set of observable context features |
| `Cset_exp(profile)` | Expected feature subset for the active context profile |
| `c_i` | One context feature inside `Cset` |
| `1_ci` | Binary or `not_applicable` marker for an expected context feature |
| `k_i` | Optional graded context-feature marker |
| `K_active(q)` | Applicable expected K feature set |
| `K0(q)` | Static observable context completeness |
| `K0_w(q)` | Weighted context completeness, optional |
| `Delta_scope_drift(t)` | Drift of declared context scope relative to baseline |
| `dist_scope` | Versioned normalized distance function for scope drift |
| `scope_stability(t)` | Remaining context-scope stability after scope drift |
| `G_K(t)` | K-internal context gate for masking unavailable context |
| `sigma_K2(t)` | Context uncertainty or variance |
| `beta_K` | Weight of the uncertainty penalty |
| `K0_ext(t)` | Gate- and uncertainty-adjusted context value |
| `K(t)` | Time-indexed `K0(q_t)` under the active context profile |
| `Delta K(t)` | First difference of K over time |
| `Delta2 K(t)` | Second difference / acceleration of K |
| `KΣ(W)` | Window aggregation of K behavior |
| `KΣ(Hangar)` | Hangar distribution view of K behavior |
