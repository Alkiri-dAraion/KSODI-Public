# R₀ v3.51 bounded reference results

Date: `2026-11-10`

Basis: [Phase 0 frozen basis](./PHASE_0_FROZEN_BASIS.md).

## Reproducible artifacts

- [`calculate_r0_v351_reference.py`](./calculate_r0_v351_reference.py)
- [`r0_v351_numeric_reference.csv`](./r0_v351_numeric_reference.csv)
- [`r0_v351_status_precedence.csv`](./r0_v351_status_precedence.csv)

Reference execution:

```text
verified_numeric_cases=9
verified_status_cases=11
numeric_sha256=aacd768555cc7ddde756d9004962f0f6b53df37c75c68d4f31c87bc61c70dd21
status_sha256=e4d9976dda3a2cb761f68d2cee2516e3bbdac477e24bb3d64894160f2b28b3b3
```

The generator uses only Python's standard library. Decimal columns are
deterministic fixture outputs; they do not claim empirical precision.

## Numeric findings

| Case | Question | Result |
| --- | --- | --- |
| `R0-01` | both trajectories static | canonical L1 R0 `1`, gate open at fixture threshold `0.8`; no relational claim follows |
| `R0-02` | low uniform drift `0.1` and `0.2` | canonical L1 R0 `0.85`, open at `0.8` |
| `R0-03` | one concentrated unit movement under L1 | R0 `0.9`, open at `0.8` |
| `R0-04` | same complete movement under separate L2 profile | R0 `0.776393202250021`, closed at `0.8` |
| `R0-05` | high equal uniform movement `0.75` | R0 `0.25`, closed at `0.5` despite equal movement magnitudes |
| `R0-06` | one-sided uniform movement `0` versus `0.8` | R0 `0.6`, open at `0.5`; stored asymmetry is `0.8` |
| `R0-07` | fixed reduced `M={K}` | reduced R0 `0.5`, open at equality |
| `R0-08` | same physical movement under complete five-axis question | canonical R0 `0.9`; it is not comparable to `R0^[K]` merely because operands overlap |
| `R0-09` | threshold equality | numeric R0 `0.5`, gate open under the declared `>=` policy |

Cases `R0-03` and `R0-04` isolate norm-family sensitivity. They do not test
coordinate weighting. Cases `R0-07` and `R0-08` show why the declared active
coordinate set changes the question and cannot be treated as missing-data
renormalization.

## Typed status findings

Seven single-condition status cases retain these distinctions:

- absent profile → `not_selected / not_evaluable`;
- required unobservable movement → `not_observable / not_evaluable`;
- substantively inapplicable declared contract →
  `not_applicable / not_evaluable`;
- incompatible identity/profile → no valid result plus an `incomparable`
  processing record;
- malformed threshold/arithmetic → no valid result plus processing error;
- numeric below threshold → valid numeric result plus `closed`;
- numeric at threshold → valid numeric result plus `open`.

The result status and gate state are not one enum. A closed gate is not
missing, failed or not applicable.

Four mixed-condition cases execute the printed precedence rather than merely
repeat declared rows:

- `not_observable` takes precedence over an otherwise inapplicable required
  input;
- under a selected R0 profile, required `not_selected` or `not_applicable`
  inputs resolve to `not_applicable` when none is unobservable;
- incomparability blocks a valid result before method-status propagation;
- an absent R0 profile returns `not_selected` before inspecting downstream
  required-input statuses.

## Bounded interpretation

The suite supports the v3.51 reference contract:

1. canonical R₀ is tied to complete comparable paired `Delta Z` and the fixed
   equal-coordinate normalized L1 reference profile;
2. L2 is a separately identified profile and can change the gate result;
3. the arithmetic mean can mask one-sided movement, so per-trajectory drifts
   and asymmetry remain available;
4. reduced fixed-M results answer another question and never silently open the
   current primary IK_rel branch;
5. `theta_R0_gate_open_min`, its derived `aggregate_drift_max`, threshold
   identity, origin and calibration status remain distinguishable;
6. an open gate is eligibility only, not relational evidence or action
   authority.

## Limits and reopening route

- all movements, identities and thresholds are synthetic;
- no alternative `g` profile or empirical threshold is selected;
- no n-adic, window/PPWA or downstream IK_rel result is validated here;
- no external implementation runtime was inspected;
- any governed-source hash change reopens Phase 0 and requires regeneration;
- later changes require renewed method-owner review, leakage/version-return review,
  predecessor awareness and complete package verification.
