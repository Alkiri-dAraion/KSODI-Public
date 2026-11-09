# IK v3.51 window and aggregation-order contract V01

Date: 2026-11-06

This contract extends the reviewed static v3.51 result family without
selecting a physical database, API or user-interface design. It does not
authorize implementation or action from a window result.

Basis:

- [result-contract candidate V01](./IK_M2_V351_RESULT_CONTRACT_CANDIDATE_V01.md);
- [v3.51 public concept companion](../IK_M2_AXIS_DEVIATION_DUAL_RESOLUTION_PUBLIC_CONCEPT_V351.md);
- current Layer-2 Z and Layer-3 IK window rules;
- reproducible static and trajectory Phases A–G in this directory;
- reproducible window-order fixtures, reviewed and transferred with the
  mathematical reference package.

## 1. Purpose

A window is not one self-explanatory average. For nonlinear results, at least
two valid but different questions exist:

```text
derive_then_aggregate:
  derive one result from each eligible complete Z,
  then aggregate the per-state results

aggregate_then_derive:
  aggregate one shared eligible set of complete Z vectors,
  then derive results from that aggregate Z
```

The contract preserves both. It prevents a display, database field or report
from silently presenting one as the other.

## 2. Bounded questions

### 2.1 Derive then aggregate

`derive_then_aggregate` asks:

> What is the distribution or declared summary of the individual eligible
> state readings inside this window?

For every eligible complete state `Z_k`, calculate the selected component:

```text
IK_w(Z_k)
IK_M2(Z_k)
IK_ref(Z_k)
AxisDev_ref(Z_k)
```

Then apply the declared result aggregator to that collection. The output
summarizes per-state readings. It is not a synthetic complete Z state.

### 2.2 Aggregate then derive

`aggregate_then_derive` asks:

> What does the declared aggregate coordinate state of this window look like
> under the selected IK readings?

First construct one aggregate Z from one shared eligible complete-state subset:

```text
Z_agg(W) = (
  Agg({K_k}),
  Agg({S_k}),
  Agg({O_k}),
  Agg({D_k}),
  Agg({I_k})
)
```

Then calculate `IK_w`, `IK_M2`, `IK_ref` and `AxisDev_ref` from
`Z_agg(W)`. The result describes the aggregate state, not the mean person,
mean utterance, representative event or average causal process.

## 3. v3.51 reference window profile family

The following revisable profile family is the v3.51 reference case.
Arithmetic mean is a transparent reference aggregator, not a universal
domain aggregator. Every profile is monadic and retains one source entity, one
trajectory, complete typed Z, exact member identities and both processing
orders for laboratory comparison.

```text
common basis:
  window_profile_version = 1
  window_scope = one source entity and one trajectory
  coordinate_order = [K,S,O,D,I]
  eligible_view = canonical complete typed Z
  state_aggregator = arithmetic_mean
  result_aggregator = arithmetic_mean
  laboratory_processing_orders =
    [derive_then_aggregate, aggregate_then_derive]
  other_processing_orders = explicitly selected by question
  fixed_reference_geometry = z_equal_coordinate_diagonal

event_tumbling:
  window_profile_id = ik_complete_z_event_tumbling_arithmetic_mean
  member_basis = fixed count of consecutive source-local event positions
  overlap_policy = non_overlapping

event_sliding:
  window_profile_id = ik_complete_z_event_sliding_arithmetic_mean
  member_basis = fixed count of consecutive source-local event positions
  overlap_policy = sliding with declared event step

clock_tumbling_event_mean:
  window_profile_id = ik_complete_z_clock_tumbling_event_mean
  member_basis = events falling inside one fixed clock-time interval
  event_weighting = equal_per_eligible_event
  temporal_weighting = none
  overlap_policy = non_overlapping

clock_sliding_event_mean:
  window_profile_id = ik_complete_z_clock_sliding_event_mean
  member_basis = events falling inside one fixed sliding clock-time interval
  event_weighting = equal_per_eligible_event
  temporal_weighting = none
  overlap_policy = sliding with declared clock-time step
```

The two clock profiles summarize eligible events observed within a time span.
They do not estimate a time-weighted latent or continuously valid state. Event
density, absence of events and unknown intervals remain visible and do not
become Pace, duration-weighted evidence or persistence of the last state.

The profile must additionally declare:

```text
window_id
source_entity_id
trajectory_id
context_scope_id, where required
ordered declared member IDs
window start/end or exact source-local bounds
time basis and timezone/clock source, if clock time is used
minimum eligible count
coverage threshold
active IK profile and version
Z/result/formula/reference versions
overlap policy
window alignment/origin, boundary convention and incomplete-tail policy
window event count and event step, for event profiles
clock duration and clock step, for clock profiles
numeric/tolerance policy
```

No universal minimum count or coverage threshold follows from the mathematics.
Each accepted profile states them and the reason for their choice.

Median, quantile, trimmed, robust, exponentially weighted, learned and
domain-specific aggregators require separate profile identities. Their
availability does not make them canonical v3.51 defaults.

## 4. One shared eligible complete-Z subset

Let `W_declared` be the exact nonempty ordered set of positions admitted by
the window definition. Define:

```text
W_complete =
  {k in W_declared |
   Z_k is complete, numeric and compatible with the window profile}
```

Every coordinate of `Z_agg(W)` and every paired comparison between the two
processing orders uses this same `W_complete`.

Forbidden:

- one subset for K and another for S/O/D/I;
- automatic use of whichever coordinates or states happen to be numeric;
- zero filling, imputation or changing masks;
- mixing source entities or trajectories in a monadic window;
- mixing active IK profiles, formula versions or reference geometries;
- silently removing inconvenient complete states after observing results.

If a diagnostic uses differing coordinate subsets, it is explicitly partial,
separately named and not a canonical complete-Z window result.

## 5. Linearity, nonlinearity and order gaps

Under the arithmetic-mean reference profile and one stable active IK profile:

```text
mean(IK_w(Z_k)) = IK_w(mean(Z_k))
mean(IK_ref(Z_k)) = IK_ref(mean(Z_k))
```

For the nonlinear norm/deviation results, generally:

```text
mean(IK_M2(Z_k)) != IK_M2(mean(Z_k))
mean(AxisDev_ref(Z_k)) != AxisDev_ref(mean(Z_k))
```

Because both nonlinear functions are norms of linear transforms, the
arithmetic-mean profile satisfies the bounded Jensen relations:

```text
IK_M2(mean(Z_k)) <= mean(IK_M2(Z_k))
AxisDev_ref(mean(Z_k)) <= mean(AxisDev_ref(Z_k))
```

When both orders are calculated, the optional deterministic diagnostics are:

```text
Gap_M2(W)
  = mean(IK_M2(Z_k)) - IK_M2(mean(Z_k))

Gap_AxisDev_ref(W)
  = mean(AxisDev_ref(Z_k)) - AxisDev_ref(mean(Z_k))
```

Both gaps are nonnegative within the numeric tolerance under this exact
profile. They can expose within-window directional/shape heterogeneity that an
aggregate state compresses. They do not by themselves measure incoherence,
error, volatility, conflict, quality or semantic change. A zero gap does not
prove that all states are identical.

Provisional logical identifiers used by this contract:

```text
ik_window_derive_then_aggregate
ik_window_aggregate_then_derive
ik_window_m2_aggregation_order_gap
ik_window_axis_deviation_aggregation_order_gap
```

They identify the four objects in explanatory and test material. A physical
implementation must publish an explicit mapping if it uses different field or
storage names.

## 6. Worked two-state fixture

Use the equal active IK profile and:

```text
Z_1 = (1,0,0,0,0)
Z_2 = (0,1,0,0,0)
mean(Z) = (1/2,1/2,0,0,0)
```

Each individual state has:

```text
IK_w = IK_ref = 1/5
IK_M2 = 1/sqrt(5) ~= 0.447213595500
AxisDev_ref = 2/5
```

Therefore `derive_then_aggregate` returns:

```text
mean(IK_w) = 0.2
mean(IK_ref) = 0.2
mean(IK_M2) ~= 0.447213595500
mean(AxisDev_ref) = 0.4
```

From the aggregate Z, `aggregate_then_derive` returns:

```text
IK_w(mean Z) = 0.2
IK_ref(mean Z) = 0.2
IK_M2(mean Z) = sqrt(1/10) ~= 0.316227766017
AxisDev_ref(mean Z) = sqrt(3/50) ~= 0.244948974278
```

Thus the linear readings agree while the nonlinear readings answer different
questions:

```text
Gap_M2 ~= 0.130985829483
Gap_AxisDev_ref ~= 0.155051025722
```

Complete labelled member states are still required: the scalar window bundle
does not reveal whether K/S, K/I or another coordinate pair produced it.

## 7. Coverage, statuses and failures

For a nonempty declared window:

```text
declared_count = |W_declared|
eligible_complete_count = |W_complete|
complete_coverage = eligible_complete_count / declared_count
```

Retain at least:

- declared, eligible and excluded member IDs;
- complete/not-complete counts;
- coordinate and Z-level typed status counts;
- exclusion reason codes;
- coverage threshold and minimum-count gate;
- selected processing order(s).

Status behavior:

| Situation | Window result |
| --- | --- |
| window/profile not selected | `not_selected`; no numeric aggregate |
| declared window empty | `not_applicable` with `empty_window`; no numeric coverage ratio |
| coverage and count gates open | `numeric`, even if excluded statuses also exist; retain them |
| gate closed and required evidence includes `not_observable` | `not_observable` with coverage reasons |
| gate closed only through selection/applicability/incompatibility | `not_applicable` with reasons |
| corrupt identity, duplicate member, invalid value/profile or arithmetic failure | processing error; no method result |

Presence of one nonnumeric state does not automatically erase an otherwise
accepted numeric window if the declared coverage profile permits it. Conversely,
a numeric aggregate must never hide its exclusions or coverage.

## 8. Derived aggregate-Z window object

`Z_agg(W)` is an observer-side derived window object with its own identity. It
is not a canonical event-level `Z_k`, does not create a target event and must
not be represented as the state of a participant. Its identity and provenance
remain tied to the exact declared window and eligible member set from which it
was derived.

The minimal logical object is:

```text
DerivedZWindowAggregate {
  aggregate_z_record_id
  object_kind = z_window_aggregate
  derived_from_window_id

  source_entity_id
  trajectory_id
  context_scope_id
  window_profile_id_and_version
  window_bounds
  member_basis

  ordered_declared_member_ids
  ordered_eligible_member_ids
  excluded_member_ids_and_reasons
  declared_count
  eligible_complete_count
  complete_coverage
  minimum_count
  coverage_threshold

  coordinate_order = [K,S,O,D,I]
  state_aggregator_id_and_version
  z_method_version
  input_profile_ids_and_versions
  numeric_policy_id_and_version

  result_status
  aggregate_z_value                # present only for a valid numeric object
  member_status_counts
  provenance_record_id
  created_at
}
```

The record has no `target_event_id`. If an implementation requires a generic
carrier field, it must use the separately typed aggregate-object identity and
must not manufacture an event ID, event position or emitting-participant state.

The following boundaries are mandatory:

1. `aggregate_z_record_id` identifies the derived object independently of
   every member and every later IK window result.
2. Exact declared, eligible and excluded members, coverage and reasons remain
   reconstructible; a hash or count alone cannot replace the member identities.
3. The aggregator, its version, coordinate order, input-profile versions and
   numeric policy are part of the object identity and comparability basis.
4. The aggregate record retains a typed status and full provenance even when
   no numeric `aggregate_z_value` exists.
5. `Z_agg(W)` is not canonical `Z_A(k_A)` and cannot satisfy a contract that
   specifically requires one event-bound canonical complete Z unless a later
   separately reviewed method contract explicitly admits this derived object.
6. No aggregate value is written back as a participant state, source event or
   replacement for the retained member records.

When the coverage and count gate is open, `aggregate_z_value` may be a complete
numeric five-coordinate vector under the declared aggregation profile. This
technical completeness does not upgrade it to an event-level canonical Z or a
representative person, utterance, intention or causal process. When the gate is
closed or processing fails, the metadata/status record may remain, but no
numeric aggregate vector or downstream aggregate-then-derive result is emitted.

## 9. Logical window record

```text
IKWindowResult {
  window_result_id
  window_profile_id
  window_profile_version
  processing_order

  source_entity_id
  trajectory_id
  context_scope_id
  ordered_declared_member_ids
  ordered_eligible_member_ids
  excluded_member_ids_and_reasons
  window_bounds
  member_basis
  time_basis

  declared_count
  eligible_complete_count
  complete_coverage
  minimum_count
  coverage_threshold

  z_method_version
  active_ik_profile_id_and_version
  result/formula versions
  fixed_reference_geometry_id_and_version
  state_aggregator_id_and_version
  result_aggregator_id_and_version
  numeric_policy_id_and_version

  result_status
  aggregate_z_record_id             # aggregate_then_derive only; Section 8
  component_result_refs_or_values
  component_distributions_or_summary_refs
  aggregation_order_gap_refs
  provenance_record_id
  created_at
}
```

A physical implementation may normalize this record across tables or views.
The logical distinctions and reverse references are mandatory; physical
storage shape remains an implementation choice.

## 10. Time, ordering and overlap

The arithmetic mean is insensitive to member order, but the window is not.
Retain exact source-local order because trajectories, deltas, path length,
detours and second differences depend on it.

Event-count windows and clock-time windows are different profiles. Clock-time
windows additionally retain clock source, resolution, timezone, synchronization
quality and known gaps. Irregular event density must not be interpreted as
elapsed-time pace.

When comparing or sliding windows:

- retain window bounds, step size and member overlap;
- disclose overlapping membership;
- do not treat overlapping windows as statistically independent;
- distinguish state/result change from changed membership or coverage;
- distinguish profile/reference change from source-state movement;
- keep linguistic rhythm, runtime latency and later R-family Pace outside this
  monadic window contract unless separately defined.

### 10.1 Delta and second-difference guard

`WINDOW-DELTA-GUARD` — window aggregation, state derivation and result
derivation are distinct operations. Their order must be named. Do not collapse
`Delta`, `Delta2`, movement magnitude and window difference into one field,
curve or interpretation.

Retain at least these distinctions:

```text
state movement:
  Delta Z_k = Z_k - Z_(k-1)

change of a derived state result:
  Delta IK_M2_k = IK_M2(Z_k) - IK_M2(Z_(k-1))

magnitude of complete state movement:
  MoveL2_Z,k = ||Delta Z_k||_2 / sqrt(5)

second ordinal difference:
  Delta2 Z_k = Delta Z_k - Delta Z_(k-1)

difference between two window results:
  DeltaWindowResult = Result(W_2) - Result(W_1)
```

`MoveL2_Z` and `DeltaWindowResult` are explanatory working labels in this
guard, not yet accepted logical result-kind or storage names.

In particular:

```text
Delta IK_M2_k != MoveL2_Z,k
```

The left side is the signed change of state magnitude. The right side is the
nonnegative size of complete vector movement. Magnitude can remain unchanged
while Z moves, and a fixed movement size can increase or decrease magnitude
depending on start state and direction.

The following are also distinct and require separate result identities:

```text
aggregate eligible per-step deltas inside one window
delta between two aggregate window states
delta between two aggregated per-state result summaries
```

For nonlinear results, changing the order may change the value. For
overlapping or differently covered windows, an apparent difference may also
arise from changed membership rather than source-state movement. Preserve
both member sets, overlap, coverage and the reconstruction path before making
a movement claim.

`Delta2 Z` requires at least three ordered comparable complete states. Without
a declared clock/time basis it remains an ordinal second difference, not
acceleration, Pace or an R-family result. Plain-ASCII technical material may
write `Delta2_Z`; `Delta^2 Z` and `Delta Z^2` must not be used when they could
be mistaken for squaring the vector or a value.

### 10.2 Other window profiles

The four profiles in Section 3 are transparent v3.51 reference cases, not
universal defaults. A different member basis, boundary, weighting, overlap
scheme, aggregator or state-validity assumption requires a separately named
and versioned profile.

Every additional profile must retain its investigation question, member
selection, ordering, coverage, aggregator, comparability, uncertainty and
reverse provenance. No interpolation, duration weighting, state carry-forward
or other transition assumption is imported into the clock-time event-mean
profiles defined here.

## 11. Comparability

Two window results are directly comparable only when they have compatible:

```text
source and trajectory identity
window purpose and member basis
window/profile/formula versions
processing order
state/result aggregator
active IK profile
fixed reference geometry
Z coordinate semantics and complete-state contract
coverage/minimum-count policy
time basis and overlap treatment
numeric policy
```

Different processing orders may be shown side by side under one paired window
identity, but their numeric values are not interchangeable. Different window
sizes, coverage or overlap may still be compared only with those differences
visible and under an explicitly accepted comparison profile.

Cross-source, multi-thread, population or dyadic windows require separately
governed contracts. They are not created by concatenating monadic member
lists.

## 12. Persistence

### 12.1 Laboratory

Persist both processing orders when the investigation uses their distinction:

- declared, eligible and excluded member identities;
- full typed member Z and provenance references;
- aggregate Z;
- per-state derived results or immutable references;
- component distributions/summaries;
- `IK_ref` as a first-class laboratory result;
- both nonlinear order gaps when calculated;
- profiles, formulas, numeric policy, coverage and window provenance.

This supports later reconstruction of what the window retained and compressed.

### 12.2 Productive environments

Retention remains purpose-, requirement-, legal- and governance-bound.
Persist enough to reproduce every result used for a decision. A derived window
may be recomputed only when exact members, source results, profiles, formulas,
reference geometry and numeric policy remain available and immutable.

## 13. Minimum conformance tests

1. a constant complete-Z window makes both orders equal for all components;
2. the two-state fixture in Section 6 reproduces all exact values and gaps;
3. arithmetic-mean `IK_w` and `IK_ref` commute under a stable profile;
4. `IK_M2` and `AxisDev_ref` satisfy their Jensen bounds;
5. a zero nonlinear gap is not labelled `all_states_identical`;
6. all coordinates of aggregate Z use the same eligible member set;
7. empty windows emit no numeric coverage or aggregate;
8. coverage below threshold preserves typed reasons and emits no numeric result;
9. an open coverage gate retains excluded-status counts beside numeric output;
10. profile/reference/formula changes block direct window comparability;
11. changing membership is not reported as source-state movement without a
    member-level reconstruction;
12. overlapping windows disclose overlap and are not called independent;
13. event-count and clock-time windows remain distinct;
14. neither order creates R-family, relational, semantic or Controller claims;
15. every result drills down to window members, complete Z and provenance;
16. every aggregate Z has its own derived-object identity and no fabricated
    target event or source-local event position;
17. no aggregate Z is accepted where a contract requires canonical event-level
    Z unless a separately reviewed profile explicitly permits it;
18. no aggregate Z is written back as a participant state or replaces its
    retained member records;
19. tumbling and sliding profiles retain their declared alignment, step,
    boundary and overlap behavior;
20. clock-time event means never claim duration weighting or persistence of
    the last observed state;
21. empty and sparsely populated clock windows preserve event density and
    eligibility rather than fabricating temporal coverage.

## 14. Supported and unsupported claims

Supported:

> Under one declared complete-Z window profile, v3.51 can calculate and retain
> a per-state result summary and an aggregate-state result as distinct,
> reconstructible answers, with coverage and provenance visible.

Not supported:

- one universal best aggregation order;
- a representative person/event from aggregate Z;
- a total coherence, truth or quality score;
- time/Pace meaning from event count alone;
- semantic interpretation of an order gap;
- multi-thread, population, relational or causal claims;
- an implementation schema, alert threshold or release.

## 15. Fixed boundary and open implementation selections

The v3.51 reference boundary fixes:

1. arithmetic mean as a transparent reference aggregator, not a universal
   domain aggregator;
2. both processing orders as distinguishable questions;
3. the four event/clock and tumbling/sliding profiles in Section 3 as the
   revisable reference family;
4. the derived aggregate-Z object boundary and reverse-provenance requirement.

The mathematics does not select one universal minimum count, coverage
threshold, physical storage layout or production retention policy. Each
implementation or investigation must declare those choices and their reasons.

Reopen the contract when a new aggregator, changing profile, partial-state
question, semantic window, multi-thread/population scope or time/Pace claim
changes the object being summarized.
