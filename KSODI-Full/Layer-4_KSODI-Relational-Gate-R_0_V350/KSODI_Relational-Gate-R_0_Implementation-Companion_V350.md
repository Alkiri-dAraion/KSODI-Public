# KSODI R_0 v3.50 - Implementation Companion

> **Status:** public v3.50 implementation companion - subordinate to the released R_0 method.

Date: strictly reviewed and released 2026-08-26

Authority: implementation guidance only. The mathematical source of truth is
[`KSODI_Relational-Gate-R_0_V350.md`](./KSODI_Relational-Gate-R_0_V350.md).

## 1. Purpose and record separation

Keep these objects distinct:

```text
monadic Z trajectory records
source-local movement records
pairing or constellation record
R0 calculation profile
R0 typed result
derived gate state
window / Hangar derivative
processing error
```

## 2. Suggested schemas

```text
R0Profile {
  r0_profile_id
  version
  projection_kind                 # complete | reduced
  active_coordinate_set_M         # all five for complete
  norm_profile                    # L1 | L2
  trajectory_aggregation          # arithmetic_mean | weighted
  trajectory_weights
  theta_r0_stable
  clipping_policy
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
  t_z_snapshots
  delta_t_z_snapshots
  r0_profile_id
  projection_kind
  active_coordinate_set_M
  per_trajectory_raw_norms
  per_trajectory_normalized_drifts
  asymmetry_diagnostics
  status                          # numeric | not_selected | not_observable | not_applicable
  value
  gate_state                      # open | closed | not_evaluable
  reason_codes
}
```

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

    require profile.theta_r0_stable is finite and in [0,1]

    M = profile.active_coordinate_set_M
    require M is explicit and non-empty

    if profile.projection_kind == complete:
        require M == [K,S,O,D,I]
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
    gate = open if value >= profile.theta_r0_stable else closed

    return numeric(value,
                   gate_state=gate,
                   per_trajectory_normalized_drifts=[d_A,d_B],
                   asymmetry=abs(d_A-d_B),
                   active_coordinate_set_M=M)
```

Do not replace M with the event-wise intersection of numeric components.

## 5. Norm implementation

```text
L1(M) = sum_(X in M) abs(delta_X) / |M|
L2(M) = sqrt(sum_(X in M) delta_X^2) / sqrt(|M|)
```

Validate every input delta in `[-1,1]`. Both normalized outputs must lie in
`[0,1]`. Clipping may absorb floating-point noise only.

## 6. N-adic computation

```text
function compute_r0_constellation(constellation, movements, profile):
    validate n >= 2
    validate explicit member and source-local-position map Pi(q)
    freeze one M and one norm profile for all members
    require profile.theta_r0_stable is finite and in [0,1]
    require every member has numeric movement on every X in M

    drifts = [normalized_drift(movements[E], M, norm) for E in members]

    if arithmetic_mean:
        raw = 1 - mean(drifts)
    else:
        validate one fixed weight per stable member identity,
                 finite, nonnegative, sum==1
        raw = 1 - weighted_sum(drifts)

    value = clip_tolerance_only(raw,0,1)
    gate = open if value >= profile.theta_r0_stable else closed
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
      a.active_coordinate_set_M == b.active_coordinate_set_M
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
```

Hangar partitions use the same comparison, profile, kind and M keys.

Validate `total_relational_steps > 0` before computing `coverage_R0`.
Compute `gate_open_rate` only when `eligible_numeric_count > 0`; otherwise the
rate is non-evaluable. Never coerce an empty denominator to `0/0`, zero or a
numeric aggregate. Enforce the declared positive minimum count and coverage
threshold before emitting an aggregate.

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
| gate-open wording as shared movement basis | replace with declared stability/availability comparison basis |

Migration is reversible and stores original IDs, transformation version and
exclusion reasons.

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

## 12. Release and alignment boundary

This companion is released subordinate guidance for the public v3.50 R_0
method. It does not itself authorize software merge, threshold choice, Patrick
alignment, Controller policy, a GitHub tag, GitHub Release, DOI or Zenodo
artifact; each retains its separate authority and gate.
