# KSODI IK v3.50 - Implementation Companion

> **Status:** public v3.50 implementation companion - subordinate to the released IK method.

Date: strictly reviewed and released 2026-08-26
Authority: implementation guidance only. The mathematical source of truth is
[`KSODI_Monadic-Interaction-Coherence-IK_V350.md`](./KSODI_Monadic-Interaction-Coherence-IK_V350.md).

## 1. Purpose and non-authority

This companion translates the typed Z-to-IK contract into implementable
records, gates, migration rules and tests. It does not select an empirical
coherence axis, approve thresholds or redefine missingness.

An implementation is conforming only if it keeps these objects distinct:

```text
typed Z input
IK profile
canonical IK result
reduced IK^[M] result
processing error
window / Hangar derivative
```

## 2. Suggested records

### 2.1 IK profile

```text
IKProfile {
  ik_profile_id
  ik_profile_version
  profile_status                 # reference | domain | research
  coordinate_order              # exactly [K,S,O,D,I]
  weights                       # map coordinate -> number
  purpose
  validation_note
}
```

Validation:

```text
keys(weights) = {K,S,O,D,I}
all finite
all >= 0
abs(sum(weights) - 1) <= epsilon_weight
```

Suggested transparent reference:

```text
ik_profile_id = ik_equal_reference_v350
weights = {K:0.2, S:0.2, O:0.2, D:0.2, I:0.2}
profile_status = reference
```

Do not label it calibrated, learned or optimal.

### 2.2 IK result

```text
IKResult {
  ik_result_id
  eval_unit_id
  target_event_id
  source_entity_id
  source_attribution_status
  emitting_entity_id             # only if established
  trajectory_id
  global_event_index             # n
  source_local_index             # k_A or k_B, never relational j
  context_scope_id
  z_record_id
  t_z_snapshot
  ik_profile_id
  ik_profile_version
  projection_kind                # canonical | reduced
  active_coordinate_set          # [K,S,O,D,I] for canonical; explicit M otherwise
  derived_weight_denominator     # null for canonical or native reduced profile
  status                         # numeric | not_selected | not_observable | not_applicable
  value                          # present only when numeric
  reason_codes
  created_at
}
```

Never use `value = 0` to encode a non-numeric status.

### 2.3 Processing failure

Malformed profiles, identity mismatch, duplicate coordinates, out-of-range
inputs and arithmetic failure are processing errors. Do not coerce them to
`not_applicable`.

## 3. Canonical computation

```text
function compute_canonical_ik(z_record, ik_profile):
    validate_z_record_identity(z_record)

    if ik_profile is absent:
        return IKResult(status = not_selected,
                        t_z_snapshot = z_record.T_Z)

    validate_canonical_profile(ik_profile)

    if z_record.complete_Z_state == complete:
        require z_record.Z exists
        require every coordinate value is finite and in [0,1]
        value = dot(ik_profile.weights, z_record.Z)
        require value in [0,1] within numeric tolerance
        return IKResult(projection_kind = canonical,
                        active_coordinate_set = [K,S,O,D,I],
                        status = numeric,
                        value = clip_tolerance_only(value, 0, 1),
                        t_z_snapshot = z_record.T_Z)

    if any required T_Z coordinate has status not_observable:
        result_status = not_observable
    else:
        result_status = not_applicable

    return IKResult(projection_kind = canonical,
                    active_coordinate_set = [K,S,O,D,I],
                    status = result_status,
                    value = absent,
                    t_z_snapshot = z_record.T_Z,
                    reason_codes = all coordinate reasons)
```

Clipping may absorb floating-point tolerance only. It must not hide an invalid
profile or out-of-range source value.

## 4. Reduced projection computation

### 4.1 Native reduced profile

```text
function compute_reduced_ik(z_record, M, reduced_profile):
    require M is explicit and non-empty
    require M subset_of {K,S,O,D,I}
    require every X in M has T_Z[X].status == numeric
    validate weights exactly over M: finite, nonnegative, sum == 1

    value = sum(reduced_profile.weight[X] * z_record.value[X] for X in M)

    return IKResult(projection_kind = reduced,
                    active_coordinate_set = ordered(M),
                    status = numeric,
                    value = value,
                    t_z_snapshot = z_record.T_Z)
```

### 4.2 Profile derived from canonical weights

```text
denom = sum(canonical_profile.weight[X] for X in M)
require denom > epsilon_weight
w_tilde[X] = canonical_profile.weight[X] / denom
```

Persist `denom`, the canonical profile ID, the derived profile ID and `M`.
Two values with different `M`, canonical parent profile or derived weights are
not comparable.

Do not auto-select `M = numeric coordinates`. That reproduces the retired
changing-mask behavior. Selection of `M` is a declared analytic decision.

## 5. Status propagation table

| Input situation | Canonical IK result | Reduced IK possibility |
| --- | --- | --- |
| complete Z | numeric after valid profile | only if a separately declared reduced question exists |
| one or more `not_observable` | `not_observable` | only for declared M whose members are numeric |
| no `not_observable`, but `not_selected` / `not_applicable` present | `not_applicable` | only for declared M whose members are numeric |
| profile absent | `not_selected` | reduced profile must be selected separately |
| Z identity invalid | processing error | blocked |
| weights invalid | processing error | blocked |

Always retain full `T_Z`, even when a reduced value is numeric.

## 6. Comparability and dynamics

```text
function comparable_ik(a, b):
    return (
      a.status == numeric and b.status == numeric and
      a.source_entity_id == b.source_entity_id and
      a.trajectory_id == b.trajectory_id and
      consecutive_or_declared_source_local_predecessors(a, b) and
      a.context_scope_id == b.context_scope_id and
      same_z_contract(a, b) and
      a.projection_kind == b.projection_kind and
      a.active_coordinate_set == b.active_coordinate_set and
      a.ik_profile_id == b.ik_profile_id and
      a.ik_profile_version == b.ik_profile_version
    )
```

Then:

```text
delta_ik = current.value - previous.value
delta2_ik = delta_ik_current - delta_ik_previous
```

Test the identity `delta_ik = dot(w, delta_z)` only for canonical complete
states with stable `w`, identical coordinate order and the same comparable
source-local pair.

### 6.1 Optional axis-change decomposition

For diagnostic research only:

```text
w_k dot Z_k - w_(k-1) dot Z_(k-1)
= w_(k-1) dot (Z_k - Z_(k-1))
+ (w_k - w_(k-1)) dot Z_k
```

Store the first term as state movement under the old axis and the second as
axis-change contribution. Do not store their sum as canonical `Delta IK`,
because the profile changed.

## 7. Windows and Hangar

Window computation must freeze:

```text
source_entity_id
trajectory_id
context_scope_id
projection_kind
active_coordinate_set
ik_profile_id and version
aggregator_id and version
minimum_count
coverage_threshold
```

Suggested output:

```text
IKWindowResult {
  window_id
  eligible_count
  total_count
  coverage_ik
  status_counts_from_T_Z
  aggregate_status
  aggregate_value
  aggregation_profile_id
}
```

Validate `total_count > 0` before computing `coverage_ik`. An empty or invalid
window emits no valid numeric coverage or aggregate and must never be coerced
to `0/0`, zero coverage or a numeric zero aggregate.

For arithmetic mean, verify `mean(IK) = w dot mean(Z)` using exactly the same
complete eligible records. Do not build `mean(Z)` coordinate by coordinate
from different subsets.

Hangar partitions must include projection kind, fixed `M` where reduced,
profile and window policy. Report coverage and typed status counts beside
numeric distributions. Never zero-fill absent coordinates or pool changing
axes into one corridor.

## 8. Migration from the legacy IK file

Legacy fields require explicit treatment:

| Legacy field / behavior | Migration |
| --- | --- |
| `A_Z` as sole applicability record | reconstruct `T_Z` only from source records; otherwise mark status detail unknown |
| `IK(t)` from five numeric values | migrate to canonical only after identity, profile and complete-Z validation |
| `IK_applicable(t)` | recover exact M and weights, then migrate to `IK^[M]`; otherwise keep legacy non-comparable |
| changing per-event mask | split by fixed M or exclude from dynamics/windows |
| generic `t` / `u` | map to source-attributed eval unit and source-local index |
| missing coordinate stored as zero | do not infer genuine zero; return to source evidence or mark legacy ambiguity |

Migration must be reversible and retain the original record ID, transform
version and reason for every exclusion.

## 9. Worked fixtures

### 9.1 Complete equal-weight state

```text
Z_A(k_A) = [0.8, 0.6, 0.5, 0.7, 0.9]
w_ref    = [0.2, 0.2, 0.2, 0.2, 0.2]
IK_A     = 0.70
status   = numeric
kind     = canonical
```

### 9.2 Incomplete typed state

```text
T_Z = [numeric(0.8), numeric(0.6), not_observable,
       numeric(0.7), numeric(0.9)]
```

Expected canonical output:

```text
status = not_observable
value  = absent
```

No zero or automatic four-coordinate renormalization is permitted.

### 9.3 Declared reduced view

With `M = {K,S,D,I}` and a separately declared equal reduced axis:

```text
w_tilde = [0.25, 0.25, 0.25, 0.25]
IK_A^[K,S,D,I] = 0.75
```

The output is numeric but reduced. It does not repair or replace canonical IK.

## 10. Acceptance tests

1. complete Z plus valid weights produces `[0,1]` canonical IK;
2. any non-numeric required coordinate blocks canonical numeric IK;
3. `not_observable` propagates without erasing other `T_Z` states;
4. missing profile returns `not_selected`, not numeric zero;
5. malformed weights produce a processing error;
6. reduced computation rejects empty, implicit or non-numeric M;
7. derived reduced weights record the denominator and parent profile;
8. changing M blocks Delta, Delta2 and pooled windows;
9. changing weights blocks canonical Delta;
10. stable complete pairs satisfy `Delta IK = w dot Delta Z` within tolerance;
11. mean equivalence uses one identical complete subset;
12. Hangar partitions preserve kind, M, profile, coverage and status counts;
13. legacy `IK_applicable` without recoverable M remains non-comparable;
14. empty or invalid windows produce no numeric coverage or aggregate;
15. R0 is not computed from IK and no IK result is labeled relational;
16. current IK_rel requires explicit dyadic pairing plus open numeric canonical
    complete dyadic R0 under the exact required profile; reduced or n-adic R0
    does not open it.

## 11. Release and alignment boundary

This companion is released subordinate guidance for the public v3.50 IK
method. It does not itself authorize software merge, threshold choice, Patrick
alignment, a GitHub tag, GitHub Release, DOI or Zenodo artifact; each retains
its separate authority and gate.
