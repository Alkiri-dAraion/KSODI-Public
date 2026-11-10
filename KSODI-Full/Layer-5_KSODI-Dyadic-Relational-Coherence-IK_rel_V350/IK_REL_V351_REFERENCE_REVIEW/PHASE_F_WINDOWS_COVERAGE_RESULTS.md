# Phase F — relational windows, coverage, overlap and dynamics

Status: `PUBLIC_V3.51_ASSERTION_CHECKED_REFERENCE_RESULTS /
NOT_RUNTIME_CONFORMANCE`

Basis:

- [Phase 0 frozen basis](./PHASE_0_FROZEN_BASIS.md);
- [Phase-C typed epsilon direction](./PHASE_C_EPSILON_BOUNDARY_RESULTS.md);
- [Phase-D R0 handoff](./PHASE_D_R0_HANDOFF_IDENTITY_RESULTS.md);
- [Phase-E fixed component sets](./PHASE_E_FIXED_COMPONENT_SET_RESULTS.md).

## 1. Question and transparent test profile

Can a relational window distinguish sustained numeric compatibility from a
high mean over sparse eligible steps while retaining gate, epsilon-band,
status, overlap and profile partitions?

The fixtures use only a transparent test policy:

```text
aggregator = arithmetic mean
minimum numeric aggregate count = 3
minimum coverage_rel = 1/2
```

These values are not v3.51 defaults or empirical recommendations.

## 2. Reproducible artifacts

- [`calculate_phase_f_window_reference.py`](./calculate_phase_f_window_reference.py)
- [`phase_f_window_coverage.csv`](./phase_f_window_coverage.csv)
- [`phase_f_window_overlap.csv`](./phase_f_window_overlap.csv)
- [`phase_f_relational_dynamics.csv`](./phase_f_relational_dynamics.csv)

Reference execution:

```text
verified_window_scenarios=5
verified_overlap_windows=5
verified_dynamic_steps=6
test_minimum_count=3
test_minimum_coverage=1/2
```

SHA-256:

```text
phase_f_window_coverage.csv
56bdb1b307be2d5cb641a2f1fd4d12cde0fd4522d8af1b74c19658ee880196d3

phase_f_window_overlap.csv
61aac0cb75c4a965958485b78b7815f0e65a4ef4e889aec480243ebb71941e74

phase_f_relational_dynamics.csv
fbd218f22d66cc5c4c1c3787f29cb4de08f06158a64ab8e94c298930ad629d6a
```

## 3. Distinct denominators

One declared nonempty relational-opportunity window retains at least:

```text
coverage_rel
= eligible numeric comparable IK_rel / all declared relational opportunities

gate_open_rate
= open numeric exact gates / valid numeric exact gates

movement_epsilon_band_rate
= movement-policy opportunities inside the joint projected epsilon band
   / all movement-policy opportunities reached after an open gate
```

Each rate has its own numerator, denominator, eligibility rule and status.
`coverage_rel` remains numeric zero when the declared nonempty window contains
no numeric IK_rel. `gate_open_rate` and the epsilon-band rate are non-evaluable
when their respective denominators are empty; they are not numeric zero.

`movement_epsilon_band_rate` is the v3.51 term replacing the
overstrong general label `static_rate`. At `epsilon_method = 0` it reduces to
the exact joint projected-zero rate; at a positive named profile it does not
claim stillness or full-Z zero movement.

## 4. Sparse-high versus sustained evidence

The sustained fixture has eight numeric values, full coverage and arithmetic
mean `87/100`; it passes the test-only emission policy.

The sparse-high fixture has eligible-subset mean `199/200` but only two numeric
values among eight opportunities:

```text
eligible mean = 0.995
coverage_rel = 1/4
gate_open_rate = 1/4
```

It emits no numeric aggregate under the test policy. Reporting only `0.995`
would convert sparse eligibility into an appearance of sustained coherence.

The current method states when no numeric aggregate may be emitted, but does
not fully fix the resulting nonnumeric aggregate status for every mixture of
closed, not-observable, not-applicable and processing records. The fixture
therefore records `not_emitted` and leaves final status/reason precedence to
the v3.51 result contract rather than inventing `not_applicable` universally.

## 5. Relational dynamics and categorical gaps

`Delta IK_rel` and `Delta2 IK_rel` are computed only over consecutive
comparable numeric relational steps. A gate closure or typed status transition
breaks the numeric derivative chain:

```text
j1 numeric 4/5
j2 numeric 9/10  -> Delta = 1/10
j3 gate closed   -> categorical transition, no numeric Delta
j4 numeric 7/10  -> no Delta across j3
j5 numeric 3/5   -> Delta = -1/10
j6 numeric 4/5   -> Delta = 1/5, Delta2 = 3/10
```

The closed step remains in the opportunity/status sequence; it is not removed
to create a false numeric adjacency.

## 6. Overlap and window-difference boundary

Two sliding windows retain exact members and overlap:

```text
W_left  = {j1,j2,j3,j4}, mean = 1/2
W_right = {j3,j4,j5,j6}, mean = 33/40
overlap = {j3,j4}
window-summary difference = 13/40
```

The summary difference is not an event-level `Delta IK_rel` and does not by
itself identify which member changed. Tumbling windows retain their disjoint
members. Identical numeric summaries under different profiles remain
non-comparable despite value equality.

## 7. Point-cloud and Hangar boundary

The same window partitions apply to `IK_rel` point clouds:

- the numeric cloud contains only `W_AB^rel` under one exact profile;
- closed, non-evaluable, epsilon-band and processing opportunities remain in
  adjacent typed partitions and coverage counts;
- no excluded point is inserted as numeric zero;
- changing dyad, pairing, N, weights, gate/profile or status policy creates a
  different cloud partition;
- distribution distance, centroid and cluster drift are derived nonnegative
  Hangar diagnostics, not signed `Delta IK_rel`;
- overlap and member identity remain available for every cloud/window
  comparison.

This permits analogous calculations over compatible point sets without
pretending that the numeric subset is the whole opportunity population.

## 8. Runtime-conformance evidence still required

The independent reference work fixes expected logic but does not prove a
runtime. A later implementation handoff must demonstrate:

- persistent enumeration of all declared relational opportunities;
- exact numerators, denominators and typed exclusions;
- stable dyad/pairing/profile/N keys;
- retained window members and overlap;
- no zero filling or numeric adjacency across categorical transitions;
- correct minimum-count/coverage enforcement;
- reconstructible point-cloud partitions and provenance;
- commit, code/profile versions and integration tests.

These requirements do not block publication of the method/reference package.
They block only a runtime-conformance claim.

## 9. Contract conclusions

1. the three denominator definitions remain distinct;
2. `movement_epsilon_band_rate` replaces the overbroad `static_rate` label;
3. high eligible-subset means remain non-emitted when declared minimum count
   or coverage fails;
4. final aggregate status/reason precedence is decided explicitly in Phase G;
5. categorical gate/status transitions do not enter numeric derivative chains;
6. overlapping windows/clouds retain exact members and overlap, and their
   summary difference remains distinct from event-level Delta;
7. point-cloud partitions remain typed and no excluded observation is
   zero-filled;
8. the five window, five overlap and six dynamics fixtures form the independent
   Phase-F basis while runtime-conformance evidence remains pending.
