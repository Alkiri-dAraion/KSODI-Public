# KSODI R_0 v3.51 — Conditional Implementation Companion

Authority: implementation guidance only. The mathematical source of truth is
[`KSODI_Relational-Gate-R_0_V351.md`](./KSODI_Relational-Gate-R_0_V351.md).

The schemas below are logical record contracts. They are not a required
database layout, API, programming language, storage technology or proof that a
runtime conforms. Implementations may use another physical schema only when
all required identities, typed states, transformations and reverse links stay
reconstructible.

## 1. Purpose and record separation

Keep these objects distinct:

```text
monadic Z trajectory records
source-local movement records
pairing or constellation record
R0 calculation profile
R0 typed result
derived gate state
display / assistive interpretation records
window / Hangar derivative
processing error
```

## 2. Suggested schemas

```text
R0Profile {
  r0_profile_id
  version
  method_version
  projection_kind                 # complete | reduced
  active_coordinate_set_M         # all five for complete
  coordinate_metric_profile_id    # canonical: fixed equal-coordinate
  coordinate_metric_version
  norm_profile_id                 # canonical: normalized L1; L2 is separate
  norm_profile_version
  trajectory_aggregation          # arithmetic_mean | weighted
  trajectory_weights
  trajectory_weight_profile_id
  theta_r0_gate_open_min
  aggregate_drift_max_derived     # exactly 1 - theta_r0_gate_open_min
  threshold_profile_id
  threshold_profile_version
  threshold_parameter_origin
  threshold_evidence_reference
  threshold_calibration_method
  threshold_calibration_status    # e.g. set_not_empirically_calibrated
  clipping_policy
  numeric_policy_id
  numeric_policy_version
}

R0Result {
  r0_result_id
  relational_eval_id              # j or q
  comparison_id
  comparison_kind                 # dyad | constellation
  pairing_or_constellation_map_id
  member_event_identities[]       # one record per paired/grouped trajectory
    target_event_id
    source_entity_id              # stable or provisional
    source_attribution_status
    emitting_entity_id            # present only when established
    trajectory_id
    global_event_index_n
    source_local_position_k
  predecessor_positions
  z_movement_record_ids
  current_z_result_ids
  predecessor_z_result_ids
  t_z_snapshots
  delta_t_z_snapshots
  r0_profile_id
  r0_method_version
  projection_kind
  active_coordinate_set_M
  coordinate_metric_profile_id
  norm_profile_id
  trajectory_aggregation_profile_id
  threshold_profile_id
  threshold_parameter_origin
  threshold_calibration_status
  numeric_policy_id
  per_trajectory_raw_norms
  per_trajectory_normalized_drifts
  asymmetry_diagnostics
  status                          # numeric | not_selected | not_observable | not_applicable
  raw_value
  value
  gate_state                      # open | closed | not_evaluable
  gate_state_derivation_version
  reason_codes
  processing_record_id_if_any
  provenance_record_ids
}

R0DisplayView {
  view_id
  r0_result_id
  display_policy_id
  rounding_policy
  display_value
  rendered_mark
  drill_down_route
}

R0AssistiveInterpretation {
  interpretation_id
  r0_result_id
  input_envelope_id
  model_and_prompt_identity
  bounded_interpretation
  uncertainty_and_missing_evidence
  created_at
}
```

Display and interpretation records must not overwrite `raw_value`, `value`,
typed status, gate state or provenance.

The optional Phase-H candidates `max_abs_coordinate_delta_E` and
`max_abs_coordinate_ids_E` are derived diagnostics, not required v3.51 result
fields. If emitted experimentally, retain the active coordinate set, metric
profile and complete signed `Delta Z_E`; represent all tied coordinate IDs and
never feed the diagnostic back into R0 or the gate.

Malformed identity, range, profile or arithmetic is a processing error.

## 3. Source-local movement eligibility

```text
function movement_coordinate(current, predecessor):
    require same source trajectory
    require declared predecessor relation
    inspect coordinate method/profile/basis compatibility

    if identity, predecessor or comparison contract differs:
        return incomparable(reasons)  # processing record; no valid delta

    if either status == not_observable:
        return not_observable(reasons)
    if either status != numeric:
        return not_applicable(reasons)

    delta = current.value - predecessor.value
    require delta in [-1,1] within tolerance
    return numeric(delta)
```

Build complete movement only from five numeric coordinate differences. Build
`Delta Z^[M]` only when M was selected before the event and every member is
numeric.

## 4. Dyadic computation

```text
function compute_r0_dyad(pairing, movements_A, movements_B, profile):
    validate_explicit_pairing(pairing)

    if profile is absent:
        return result(not_selected, gate_state=not_evaluable)

    require profile.theta_r0_gate_open_min is finite and in [0,1]
    aggregate_drift_max = 1 - profile.theta_r0_gate_open_min
    if a derived maximum is stored:
        require stored aggregate_drift_max == aggregate_drift_max
    require declared threshold profile, parameter origin and calibration status

    M = profile.active_coordinate_set_M
    require M is explicit and non-empty

    if profile.projection_kind == complete:
        require M == [K,S,O,D,I]
        require coordinate_metric_profile == equal_coordinate_reference
    else:
        require M subset_of {K,S,O,D,I}

    status = propagate_required_movement_status(movements_A[M],
                                                movements_B[M])
    if status == incomparable:
        return processing_block(incomparable, no_valid_r0_result,
                                retain all typed reasons)
    if status != numeric:
        return result(status, gate_state=not_evaluable,
                      retain all typed reasons)

    d_A = normalized_drift(movements_A, M, profile.norm_profile)
    d_B = normalized_drift(movements_B, M, profile.norm_profile)

    if profile.trajectory_aggregation == arithmetic_mean:
        raw = 1 - (d_A + d_B)/2
    else:
        validate dyadic weights: finite, nonnegative, sum==1
        raw = 1 - (w_A*d_A + w_B*d_B)

    value = clip_tolerance_only(raw, 0, 1)
    gate = open if value >= profile.theta_r0_gate_open_min else closed

    return numeric(raw_value=raw,
                   value=value,
                   gate_state=gate,
                   per_trajectory_normalized_drifts=[d_A,d_B],
                   asymmetry=abs(d_A-d_B),
                   active_coordinate_set_M=M)
```

Do not replace M with the event-wise intersection of numeric components.
Do not substitute a test coordinate-weight vector `g` for the canonical
equal-coordinate metric. Do not confuse trajectory weights with coordinate or
IK-axis weights.

## 5. Norm implementation

```text
L1(M) = sum_(X in M) abs(delta_X) / |M|
L2(M) = sqrt(sum_(X in M) delta_X^2) / sqrt(|M|)
```

Validate every input delta in `[-1,1]`. Both normalized outputs must lie in
`[0,1]`. Clipping may absorb floating-point noise only.

The canonical profile is the equal-coordinate normalized L1 expression.
Equal-coordinate L2 is separately named. A coordinate-weighted test control
requires a different profile kind and cannot be emitted as canonical R0.

## 6. N-adic computation

```text
function compute_r0_constellation(constellation, movements, profile):
    validate n >= 2
    validate explicit member and source-local-position map Pi(q)
    freeze one M and one norm profile for all members
    require profile.theta_r0_gate_open_min is finite and in [0,1]
    aggregate_drift_max = 1 - profile.theta_r0_gate_open_min
    if a derived maximum is stored:
        require stored aggregate_drift_max == aggregate_drift_max
    require every member has numeric movement on every X in M

    drifts = [normalized_drift(movements[E], M, norm) for E in members]

    if arithmetic_mean:
        raw = 1 - mean(drifts)
    else:
        validate one fixed weight per stable member identity,
                 finite, nonnegative, sum==1
        raw = 1 - weighted_sum(drifts)

    value = clip_tolerance_only(raw,0,1)
    gate = open if value >= profile.theta_r0_gate_open_min else closed
    return numeric(value, gate, drifts,
                   drift_range=max(drifts)-min(drifts))
```

Do not use the relational index as the entity summation index.

## 7. Result-status propagation

| Required-input situation | R0 result | Gate state |
| --- | --- | --- |
| profile absent | `not_selected` | `not_evaluable` |
| at least one required observation is `not_observable` | `not_observable` | `not_evaluable` |
| pairing/predecessor/fixed-M contract does not apply | `not_applicable` | `not_evaluable` |
| all required movement numeric, value below threshold | `numeric` | `closed` |
| all required movement numeric, value at/above threshold | `numeric` | `open` |
| malformed profile or identity | processing error | absent |

Preserve all trajectory-specific reasons.

When several required inputs are non-numeric, preserve every reason and apply
this result precedence only after comparability validation: any required
`not_observable` yields `not_observable`; otherwise required `not_selected` or
`not_applicable` yields `not_applicable`. `incomparable` and processing errors
remain outside the valid R0 result family.

## 8. Comparability, dynamics and windows

```text
function comparable_r0(a,b):
    return (
      a.status == numeric and b.status == numeric and
      a.comparison_id == b.comparison_id and
      same_pairing_or_constellation_semantics(a,b) and
      same_source_local_predecessor_policy(a,b) and
      a.r0_profile_id == b.r0_profile_id and
      a.projection_kind == b.projection_kind and
      a.active_coordinate_set_M == b.active_coordinate_set_M and
      a.coordinate_metric_profile_id == b.coordinate_metric_profile_id and
      a.norm_profile_id == b.norm_profile_id and
      a.trajectory_aggregation_profile_id == b.trajectory_aggregation_profile_id and
      a.threshold_profile_id == b.threshold_profile_id and
      a.numeric_policy_id == b.numeric_policy_id
    )
```

Only then compute Delta/Delta2 over the relational index.

Window output should retain:

```text
eligible_numeric_count
total_relational_steps
coverage_R0
gate_open_count / gate_closed_count / not_evaluable_count
typed result-status counts
per-trajectory drift summaries
asymmetry summaries
aggregator/profile IDs
window_result_id and window_profile/version
ordered candidate members and eligible member IDs
status partitions and denominator
derived-object provenance
```

Hangar partitions use the same comparison, profile, kind and M keys.

Validate `total_relational_steps > 0` before computing `coverage_R0`.
Compute `gate_open_rate` only when `eligible_numeric_count > 0`; otherwise the
rate is non-evaluable. Never coerce an empty denominator to `0/0`, zero or a
numeric aggregate. Enforce the declared positive minimum count and coverage
threshold before emitting an aggregate.

The aggregate is not a participant event, a Z state or one relational step.
Keep `Delta R0`, `Delta2 R0`, window-to-window difference, movement length and
aggregate statistics separately typed.

## 9. Migration from the legacy R0 file

| Legacy construct | Migration |
| --- | --- |
| generic shared `t` | map to relational j plus explicit `pi(j)` |
| event-wise `A_pair(t)` intersection | recover exact M and split by fixed M; otherwise legacy non-comparable |
| division by current `m_pair(t)` | replace only after fixed-M reconstruction |
| binary masks without typed reasons | return to Z source records; otherwise retain legacy ambiguity |
| `R0=not_applicable` for numeric closed gate | retain numeric value and set `gate_state=closed` |
| complete and masked values under one name | migrate to canonical R0 versus `R0^[M]` |
| n-adic summation over `j` | rename entity index and create explicit constellation map |
| gate-open wording as shared movement basis | replace with declared availability/bounded-drift comparison basis |
| `theta_r0_stable` | retain only as a v3.50 legacy alias; migrate to `theta_r0_gate_open_min` without interpreting it as observed stability |
| generic `L1` without coordinate-metric identity | reconstruct the fixed equal-coordinate reference only when the formula/operands prove it; otherwise retain ambiguity |
| threshold value without origin/calibration metadata | retain the value and declare missing provenance; never infer empirical calibration |
| rounded display stored as result | recover the raw result where evidence exists; otherwise classify the record as partially reconstructible |
| generic downstream `IK` reference | require the exact compatible current branch and explicit paired `Delta IK_w` profile before v3.51 handoff |

Migration is reversible and stores original IDs, transformation version and
exclusion reasons.

Use the record classes:

```text
v351_conformant
legacy_reconstructible
legacy_partially_reconstructible
legacy_noncomparable
reconstruction_pending
```

Missing provenance may be declared unknown; it must not be reconstructed as
fact. A nonconforming historical record may remain useful evidence without
becoming comparable or eligible for the v3.51 downstream handoff.

## 10. Worked fixtures

### 10.1 Complete dyadic reference

```text
d_A = 0.10
d_B = 0.20
R0 = 1 - (0.10+0.20)/2 = 0.85
theta = 0.80
status = numeric
gate_state = open
```

### 10.2 Numeric closed gate

```text
d_A = 0.50
d_B = 0.70
R0 = 0.40
status = numeric
gate_state = closed
```

### 10.3 Same movement, different declared basis

```text
Delta K_A=1, Delta K_B=0

M={K}:            R0^[K] = 0.50
M={K,S,O,D,I},
other deltas zero: R0 = 0.90
```

Both are valid answers to different declared questions. They are not directly
comparable.

### 10.4 Typed missingness

```text
required Delta O_A = not_observable
R0.status = not_observable
gate_state = not_evaluable
value = absent
```

### 10.5 Concentrated movement separates L1 and L2 profiles

```text
Delta Z_A = [1,0,0,0,0]
Delta Z_B = [0,0,0,0,0]

d_A,L1 = 1/5
d_A,L2 = 1/sqrt(5)

R0_L1 = 9/10
R0_L2 = 1 - 1/(2 sqrt(5)) ~= 0.7763932023
```

At a transparent fixture threshold of `0.8`, the L1 reference opens and the
separate L2 profile closes. This is norm-family sensitivity, not evidence that
one norm is universally correct and not an empirical threshold calibration.

### 10.6 Minimal machine record and human view

```text
R0Result {
  r0_result_id: "r0-fixture-01"
  r0_method_version: "3.51"
  comparison_id: "dyad-A-B"
  pairing_or_constellation_map_id: "pair-01"
  z_movement_record_ids: ["dz-A-01", "dz-B-01"]
  coordinate_metric_profile_id: "equal-coordinate-reference"
  norm_profile_id: "normalized-L1-reference"
  trajectory_aggregation_profile_id: "arithmetic-mean"
  threshold_profile_id: "fixture-theta-080"
  theta_r0_gate_open_min: 0.8
  aggregate_drift_max_derived: 0.2
  threshold_calibration_status: "set_not_empirically_calibrated"
  raw_value: 0.85
  value: 0.85
  status: "numeric"
  gate_state: "open"
}

R0DisplayView {
  r0_result_id: "r0-fixture-01"
  display_value: "0.85"
  rendered_mark: "open under fixture-theta-080"
  drill_down_route: "r0-fixture-01 -> dz-A-01 / dz-B-01"
}
```

The human view is navigation, not a stored replacement result or action
instruction.

## 11. Acceptance tests

1. undeclared pair/constellation is rejected;
2. each movement uses its own source-local predecessor;
3. complete profile rejects fewer than five numeric coordinates;
4. reduced profile rejects implicit, empty or changing M;
5. identical fixed M is required across all compared trajectories;
6. L1/L2 normalization stays in `[0,1]`;
7. arithmetic-mean and weighted profiles remain separately named;
8. R0 output stays in `[0,1]`;
9. numeric closed gate remains numeric;
10. typed missingness produces `not_evaluable`, never zero;
11. asymmetry diagnostic does not alter canonical R0;
12. n-adic member and relational indices remain distinct;
13. changing M/profile blocks Delta and pooled windows;
14. windows report coverage, result statuses and gate states;
15. empty windows and zero-eligible windows emit no numeric rate or aggregate;
16. thresholds are finite and lie in `[0,1]`;
17. incomparable movement produces no valid R0 result;
18. n-adic weights are fixed, member-bound, non-negative and sum to one;
19. no output is labeled relation, coupling, resonance or alignment.
20. canonical complete R0 rejects a non-reference coordinate metric;
21. L1 and L2 profiles remain differently identified even when values happen
    to coincide;
22. threshold origin and calibration status are retained and never inferred;
23. raw result, clipped value, gate state and display value remain distinct;
24. downstream handoff rejects a different R0 result/profile/pairing/step;
25. downstream current primary IK_rel names paired comparable `Delta IK_w`
    under one shared exact profile;
26. window aggregates retain derived identity, members, denominator and
    status partitions;
27. excluded opportunities remain reconstructible without emitting IK_rel;
28. `theta_r0_gate_open_min` and its exact derived
    `aggregate_drift_max_derived` remain consistent;
29. the v3.50 alias `theta_r0_stable` is never emitted as the canonical v3.51
    field or interpreted as observed stability;
30. `open` and `closed` remain non-valuative eligibility states;
31. unresolved apparent movement never becomes numeric without a separately
    identified measurement or reconstruction route and profile.
32. mixed nonnumeric conditions execute the declared precedence: profile
    absence short-circuits the attempt, processing/comparability failures stay
    outside the valid result family, `not_observable` precedes applicable
    method exclusions, and remaining required `not_selected`/`not_applicable`
    inputs resolve to `not_applicable` under a selected profile.

## 12. Release and alignment boundary

This public v3.51 companion remains subordinate to the method. It does not establish runtime conformance and does not itself authorize
software merge, threshold choice, external implementation alignment, Controller policy,
a GitHub tag, GitHub Release, DOI or Zenodo artifact; each
retains its separate authority and gate.
