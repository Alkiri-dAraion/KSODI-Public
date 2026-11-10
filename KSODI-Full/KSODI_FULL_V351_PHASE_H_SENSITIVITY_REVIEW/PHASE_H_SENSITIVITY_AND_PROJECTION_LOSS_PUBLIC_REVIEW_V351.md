# KSODI-Full v3.51 Phase H — Sensitivity and Projection-Loss Review

Status: `PUBLIC_V351_REVIEW / SYNTHETIC_REPRODUCIBLE_REVIEW /
NO_NEW_METHOD_PROFILE`

## 1. Why this review is public-facing

`R_0` and `IK_rel` answer deliberately bounded questions. Their results depend
on declared operands, profiles and status rules, and scalar projections cannot
retain every distinction in the complete movement vectors.

Phase H makes these boundaries inspectable. It asks:

- when does a declared metric or weighting profile change an `R_0` result?
- which distinctions are compressed by a coordinate-extreme diagnostic?
- when do different complete movements share the same scalar `IK_rel`
  projection?
- how do exact zero and positive epsilon policies alter result status?
- does the complete `R_0` to `IK_rel` route preserve the identities needed to
  reconstruct those effects?

Publishing this review does not imply that every observed information loss is
a defect. It exposes the losses so researchers and implementers can judge
their relevance for a particular question.

## 2. Frozen basis and test scope

The review is bound to the v3.51 Public method state at commit
`0a9238268a24dbad782061680d619c6752f5550e`.

It contains 52 synthetic cases in five blocks:

| Block | Rows | Scope |
| --- | ---: | --- |
| H-A | 12 | `R_0` norm, threshold and coordinate-metric sensitivity |
| H-B | 7 | optional coordinate-extreme diagnostic and tied maxima |
| H-C | 7 | `IK_rel` scalar projection collisions |
| H-D | 16 | exact zero, all three positive-epsilon kinds and calibration provenance |
| H-E | 10 | complete `R_0` → `IK_rel` route |

The canonical equal-coordinate normalized L1 profile remains unchanged. L2,
coordinate-weight vectors and alternative `IK_w` weights are explicitly named
test controls. Positive epsilon values are synthetic and marked
`set_not_empirically_calibrated`.

## 3. Main findings

### 3.1 Profile sensitivity is real and attributable

The same movement can produce different `R_0` values under L1, L2 or a fixed
coordinate-weight control. This is not an arithmetic contradiction: the
profiles ask different geometric questions.

For example, one full-unit movement on a single coordinate yields:

```text
equal-coordinate normalized L1: R_0 = 0.8 -> open at threshold 0.8
equal-coordinate normalized L2: R_0 ≈ 0.552786404500042 -> closed
```

The result therefore requires its profile identity. A value without that
identity is not safely comparable.

### 3.2 A coordinate extreme is useful but incomplete

The optional candidate

```text
max_abs_coordinate_delta_E
max_abs_coordinate_ids_E
```

can identify one largest coordinate movement and preserve every tied
coordinate ID. It does not preserve sign, secondary movement or the complete
distribution. The complete signed `Delta Z_E` remains authoritative.

Phase H does not make this candidate a required v3.51 field. Its possible
inclusion in a later controlled record schema remains a separate decision.

### 3.3 Scalar projection collisions are visible

Five deliberately selected H-C cases share a raw projected compatibility
expression of `1` while retaining different complete movement vectors.

- Three are numeric `C_move = 1` collisions.
- Two have both projected operands at exact zero and therefore return
  `not_applicable_joint_projected_zero`, not numeric `IK_rel = 1`.

Examples include movement on different coordinates, concentrated versus
distributed movement and disjoint zero-sum transfers.

This is the expected consequence of projecting richer movement onto one
scalar. `IK_rel` reports compatibility for its selected projected question; it
does not claim that the complete movements are identical. The reverse route to
both complete `Delta Z` vectors is therefore part of the result contract.

### 3.4 Epsilon kinds and provenance remain distinct

The review covers:

- `epsilon_numeric_tolerance`;
- `epsilon_observation_resolution`;
- `epsilon_question_relevance`.

At the boundary the comparison uses `<= epsilon`. Missing parameter origin,
missing calibration status, an unsupported empirical-calibration claim or a
negative epsilon yields a processing error rather than a repaired numeric
result.

The synthetic tests verify contract behavior. They do not empirically
calibrate an epsilon.

### 3.5 No tested contract contradiction

The complete 52-case suite finds:

- confirmed contract behavior;
- expected profile sensitivity;
- reproducible diagnostic information loss;
- zero observed contract contradictions.

This is a bounded synthetic result, not proof of completeness, semantic
validity or runtime conformance.

## 4. How to read information loss

An information loss may be acceptable for one question and unacceptable for
another. Its relevance depends at least on:

- the investigation context and exact question;
- selected resolution and observation window;
- available infrastructure and retained evidence;
- intended human or machine consumer;
- expected decision or follow-up;
- privacy, sensitivity and governance constraints.

A scalar result should not be expanded until it appears to answer every
possible question. Conversely, a compressed result should not conceal the
route back to richer evidence needed for a foreseeable standard question.

For v3.51, the observed scalar collisions do not require a formula change: the
method already requires the reverse route to both complete movements. A later
version may still improve controlled records and reader views.

## 5. Questions for research and implementation collaboration

Contributions are especially welcome on the following bounded questions:

1. For which recurring investigation questions is the scalar projection
   sufficient, and when is a richer diagnostic bundle necessary?
2. Which minimal bundle should accompany `IK_rel` for human explanation,
   machine analysis or later reconstruction?
3. Is the coordinate-extreme candidate useful enough to justify a controlled
   record field, or should it remain a selectable derived diagnostic?
4. How should tied extrema, signs and secondary movement be displayed without
   overwhelming a reader?
5. Which empirical designs could calibrate an epsilon for a declared
   observation resolution or question without turning it into a universal
   default?
6. Which information losses are material for common questions, and which are
   acceptable under declared storage, privacy and infrastructure constraints?
7. Which adversarial or counterexample cases should be added to distinguish a
   real contract defect from expected profile sensitivity?

Suggested contributions should state the observation question, profile,
evidence basis, expected consumer and the distinction that the proposal would
preserve or recover.

## 6. Reproduction and limits

The proposed Public package includes:

- the exact frozen basis;
- one standard-library Python generator;
- five CSV fixture families;
- the detailed result report;
- a SHA-256 manifest.

The generator performs deterministic arithmetic and explicit assertions. A
passing run does not establish empirical calibration, production suitability,
semantic equivalence, hidden-state access, causality or action authority.

The review changes no canonical formula, threshold, gate rule or default
profile. Runtime conformance and future schema changes remain separately
governed.
