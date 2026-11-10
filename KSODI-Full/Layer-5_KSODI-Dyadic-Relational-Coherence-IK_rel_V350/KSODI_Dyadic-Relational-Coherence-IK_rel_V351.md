# KSODI `IK_rel` — Dyadic Relational Coherence Compatibility v3.51

Status: `PUBLIC_V3.51_METHOD / REFERENCE_FORMULA_AND_CONTRACT /
NOT_RUNTIME_CONFORMANCE`

Authority: released Public v3.51 method source. Conditional schemas and
pseudocode belong in the
[implementation companion](./KSODI_Dyadic-Relational-Coherence-IK_rel_Implementation-Companion_V351.md).
The assertion-checked basis is retained in
[`IK_REL_V351_REFERENCE_REVIEW/`](./IK_REL_V351_REFERENCE_REVIEW/).

## 0. Question and claim boundary

`IK_rel` asks one narrow relational question:

> After an exact compatible `R_0` handoff has admitted one explicitly paired
> dyadic step, how compatible is the observable movement of the two distinct
> monadic trajectories along one shared, declared `IK_w` axis?

The primary profile compares paired first differences

```text
Delta IK_w,A(k_A(j))
Delta IK_w,B(k_B(j))
```

under the explicit pairing

```text
pi(j) = (k_A(j), k_B(j)).
```

`IK_rel` is not inferred from isolated values. It requires two distinct
monadic trajectories, source-local predecessors, one shared exact `IK_w`
profile, an explicit pairing and an exact compatible open numeric
canonical-complete dyadic `R_0` result.

It is not agreement, truth, alignment, causation, coupling, resonance, shared
meaning, shared consciousness or action authority. A high value says only that
the selected projected movements are compatible under the declared profile.

### 0.1 Minimal reading

1. Preserve A and B as distinct trajectories.
2. Resolve an explicit `pi(j)` and both source-local predecessors.
3. Require the exact compatible Layer-4 handoff for the same dyad, events,
   pairing, step, gate profile and threshold.
4. Require comparable numeric `Delta IK_w` operands under one shared profile.
5. Apply one named epsilon kind and policy without changing raw operands.
6. Compute the selected fixed component profile only when every required
   component is numeric.
7. Keep status, exclusions and complete `Delta Z` reverse links visible.
8. Aggregate only within one declared opportunity, profile and partition
   contract.

### 0.2 Bounded examples

In a human–agent dialogue, each participant first receives its own typed Z and
monadic IK records. Parallel curves may be displayed before `R_0`, but their
proximity is not yet current relational evidence. After an exact handoff,
`IK_rel` may describe paired movement compatibility; it does not prove mutual
understanding or an inner representation.

For an unfamiliar signal carrier and a responding system, partial typed states
or reduced monadic views may remain diagnostically useful. They do not qualify
for current primary `IK_rel` without the exact canonical operands, identities,
pairing and gate. A future reduced profile must be separately named and
validated; source uncertainty must not be converted into a fabricated source
fact.

## 1. Architectural position and identity

```text
A: K/S/O/D/I -> typed Z_A -> IK_w,A --\
                                         +--> IK_rel_AB(j)
B: K/S/O/D/I -> typed Z_B -> IK_w,B --/

Delta Z_A --\
              +--> exact R_0_AB(j) handoff
Delta Z_B --/
```

`R_0` and monadic `IK_w` are parallel prerequisites. `R_0` is not calculated
from `IK_w`; `IK_rel` consumes its gate decision plus declared monadic
operands. The atomic unit is

```text
rho_AB(j | pi(j)),  pi(j) = (k_A(j), k_B(j)).
```

It retains at least:

- result, method, formula and profile identities;
- ordered dyad, directionality, member identities and attribution status;
- paired events, pairing-map ID and relational evaluation index `j`;
- both trajectory IDs, source-local positions and predecessor references;
- exact `R_0` result/profile/threshold/gate-state reference;
- both `IK_w` results and first-difference records;
- selected component set, named weights and epsilon policy;
- raw computational value or typed reason;
- complete paired `Delta Z` reverse references and provenance.

Timestamps or global event indices may be mapped to these identities but may
not replace them. v3.51 remains dyadic; an n-adic extension requires its own
constellation and hyperedge contract.

## 2. Exact `R_0` handoff

The current primary branch is eligible only when the referenced `R_0` result:

```text
comparison_kind = dyad
projection_kind = canonical_complete
active_coordinate_set_M = {K,S,O,D,I}
status = numeric
gate_state = open
```

and its ordered dyad, member-event identities, pairing map, relational step,
profile/version and threshold equal those required by the `IK_rel` attempt.
The gate-state derivation must be internally consistent with Layer 4:

```text
numeric R_0 >= theta_R0_gate_open_min -> open
numeric R_0 <  theta_R0_gate_open_min -> closed
```

`theta_R0_stable` is a legacy alias, not v3.51 method language. An open gate
means eligibility for this exact downstream branch; it does not assert social,
semantic or systemic stability.

A valid closed gate yields `not_applicable` and an exclusion record. A required
unobservable gate input yields `not_observable`. An invalid, incomparable or
failed `R_0` record yields no valid downstream method result. Reduced or n-adic
`R_0` does not open the current primary branch.

The projected feasibility calculations in Phase D are diagnostics. They never
replace the complete-`Delta Z` Layer-4 result.

## 3. Primary movement profile

For canonical numeric `Delta IK_w` operands in `[-1,1]`:

```text
g_move,AB(j)
= |Delta IK_w,A(k_A(j)) - Delta IK_w,B(k_B(j))| in [0,2]

C_move,AB(j)
= clip(1 - g_move,AB(j) / 2, 0, 1) in [0,1]

IK_rel,AB(j | p_rel_move) := C_move,AB(j).
```

Clipping is defensive numerical containment only. The selected computational
value remains unrounded. Display rounding is a later view and never feeds a
threshold, derivative, aggregate or method result.

### 3.1 Epsilon kinds and projected null/band semantics

The reference method has `epsilon_method = 0`. Positive epsilons are never one
undifferentiated parameter. v3.51 distinguishes:

```text
epsilon_numeric_tolerance
epsilon_observation_resolution
epsilon_question_relevance
```

- Numerical tolerance belongs to a versioned arithmetic policy. Joint zero
  under that policy is `not_applicable` with reason
  `joint_projected_zero_under_numeric_policy`.
- Observation resolution belongs to the instrument. Indistinguishable required
  movement is `not_observable`; it is never inserted as zero.
- Question relevance belongs to a declared investigation. Joint movement
  inside that band is `not_applicable` with reason
  `joint_projected_movement_below_question_relevance`.

These findings concern the selected `IK_w` projection. None establishes
complete-Z stillness, universal irrelevance or absence of relation. The legacy
field `static_step` is accepted only as an explicitly migrated alias for exact
joint projected zero under recorded `epsilon_method = 0`. The v3.51 record uses
typed projected-null/band reasons instead.

Each positive profile declares kind, component, value, domain/scale, boundary
inclusivity, parameter origin, explicit calibration status, evidence or
rationale, version, status consequence and raw-operand retention. A set or
test-only value must not be presented as empirically calibrated; for example,
`calibration_status = set_not_empirically_calibrated` remains distinguishable
from a later validated calibration record. Movement and acceleration policies
remain separate. Display rounding and the `R_0` threshold are not epsilon
kinds.

## 4. Typed components and fixed profiles

After the same exact handoff and component-local eligibility checks:

```text
C_gap(j)   = 1 - |IK_w,A - IK_w,B|
C_move(j)  = 1 - |Delta IK_w,A - Delta IK_w,B| / 2
C_accel(j) = 1 - |Delta2 IK_w,A - Delta2 IK_w,B| / 4
```

Each numeric component lies in `[0,1]`. `C_gap`, `C_move` and `C_accel`
answer different questions. Their tuple is not a trajectory-length, activity
or resonance measure.

`C_gap` is static. Movement and acceleration have independent null/band
policies. Joint projected zero movement does not imply joint zero acceleration:
a transition to rest can leave `C_accel` numeric. Equal nonzero constant
movement can leave `C_move` numeric while `C_accel` is non-applicable.

`C_shared` remains reserved and `not_selected` until a separate definition,
question and profile are accepted. It is not selectable merely because legacy
material contains the name.

For one fixed, nonempty set

```text
N subset_of {gap, move, accel}
```

and finite name-bound nonnegative weights summing to one:

```text
IK_rel,AB^[N](j) = sum_(c in N) v_c C_c,AB(j)
```

only when every required component is numeric. All seven nonempty sets are
structurally possible; only `{move}` is the current primary profile. No other
set is canonical merely because the formula can be evaluated.

Required components are never removed event-wise and remaining weights are
never silently renormalized. Non-required evidence may remain visible without
blocking the selected scalar. Point clouds and aggregates are partitioned by
the complete profile identity.

## 5. Typed result and decision order

The method domain is:

```text
numeric(value in [0,1])
not_selected
not_observable
not_applicable
```

Processing failure is not a fifth valid method status. The atomic order is:

1. no selected profile -> `not_selected`;
2. malformed identity/profile/arithmetic or missing valid predecessor -> no
   valid result; processing block;
3. invalid/incomparable `R_0` -> no valid downstream result;
4. required gate evidence unobservable -> `not_observable`;
5. valid closed or otherwise ineligible gate -> `not_applicable`;
6. after an open gate, required component evidence unavailable ->
   `not_observable`;
7. valid component-local projected null/band exclusion -> `not_applicable`;
8. all conditions pass -> `numeric`;
9. invalid weights, changing `N` or profile mismatch -> processing error.

Underlying reasons remain visible. A later scalar status never erases its
path.

## 6. Diagnostic bundle and Layer-3 return

The first question-led diagnostic bundle is:

```text
current primary IK_rel
+ raw Delta IK_w,A / Delta IK_w,B
+ complete Delta Z_A / Delta Z_B
+ explicitly directed componentwise differences
+ R_geom direction only when separately selected, defined and valid
```

It is a linked evidence view, not a fourth scalar or universal diagnosis.
`IK_M2`, `IK_ref`, `AxisDev_ref` and the `IK-Gesamtbild` are parallel monadic
views; they are not implicit primary operands. Equality of two `IK_rel` values
never identifies the dyad, paths or complete movement that produced them.

Three consumers remain distinct:

1. deterministic Observer record: typed operands, identities, profiles,
   statuses, exact calculations and provenance;
2. assistive LLM package: attributable question, context, selected evidence,
   uncertainty and claim limits;
3. human/governance view: comprehensible real-valued display, status and
   coverage visibility plus drill-down.

No interpretation overwrites the method result.

## 7. Dynamics, windows and PPWA

Comparable consecutive numeric results under one complete profile permit:

```text
Delta IK_rel(j)  = IK_rel(j) - IK_rel(j-1) in [-1,1]
Delta2 IK_rel(j) = Delta IK_rel(j) - Delta IK_rel(j-1) in [-2,2].
```

Gate/status transitions are categorical gaps and break the numeric derivative
chain. Differences between window summaries are not event-level deltas.

Every window declares a nonempty opportunity set and retains each attempted
member. At least these rates remain separate:

```text
coverage_rel
= numeric comparable IK_rel / declared relational opportunities

gate_open_rate
= open numeric exact gates / valid numeric exact gates

movement_epsilon_band_rate
= post-open-gate movement opportunities inside the declared joint band
  / all movement-policy opportunities reached after an open gate.
```

Each rate stores numerator, denominator, status and profile. Empty denominators
are non-evaluable, not zero. `movement_epsilon_band_rate` replaces the
ambiguous legacy name `static_rate`.

A numeric window aggregate additionally requires one fixed profile, declared
minimum numeric count and coverage, contained processing policy, named
aggregator and retained membership/overlap. No excluded opportunity is filled
with zero. The Phase-F mean and thresholds are fixture-only controls, not
production defaults.

The strict reference policy is `strict_integrity_v351`. For later large or
dense windows, `partition_preserving_window_aggregation` (PPWA) retains all
numeric, nonnumeric, gate and processing partitions. Its proposed later policy
is `partition_preserving_bounded_tolerance`, compactly `PPWA-bounded`. It is
Future Work, not a v3.51 empirical default.

The strict nonnumeric aggregate order is:

1. no selected aggregate profile -> `not_selected`;
2. invalid window/profile/membership/arithmetic or uncontained required
   processing failure -> no valid aggregate;
3. valid attempted scope resolving to no opportunities -> `not_applicable /
   empty_resolved_opportunity_window`;
4. every otherwise eligible opportunity unobservable -> `not_observable`;
5. insufficient numeric count or coverage in another valid mixture ->
   `not_applicable / insufficient_numeric_coverage`;
6. all emission conditions pass -> `numeric`.

Every mixed partition remains counted. A diagnostic eligible-subset summary
may be retained as explicitly conditional and diagnostic-only; it is not the
official result for the complete window.

## 8. Migration and reconstructibility

Equal numeric values do not establish compatibility. Migration uses:

```text
v351_conformant
legacy_reconstructible
legacy_partially_reconstructible
legacy_noncomparable
```

with separate workflow states such as `reconstruction_pending`.
`reconstruction_pending` is not a method result.

Migration guards include:

- legacy `static_step` is exact projected zero only when recorded epsilon is
  exactly zero;
- changing component sets, event-wise renormalization or unnamed positional
  weights are not comparable to fixed v3.51 profiles;
- unknown source attribution may remain explicit and provisional; missing
  provenance is never reconstructed as fact;
- missing event, pairing, predecessor, `IK_w` profile or exact `R_0` handoff
  prevents current-result conformance without erasing the retained evidence;
- window summaries without exact opportunities, membership, denominators,
  partitions and profile are not conforming aggregates;
- display-rounded values are not computational operands.

`not v3.51 conformant` does not mean worthless or invalid.

## 9. Point clouds, privacy and branch boundary

Typed relational point records retain the scalar beside component, gate and
reverse evidence. They are partitioned by dyad, pairing, `R_0` profile,
`IK_w` profile, `IK_rel` profile, fixed `N`, weights and status policy.
Distribution distance, centroid and cluster drift are separately named
nonnegative diagnostics, not signed `Delta IK_rel`.

The legacy display notation `H_AB = {Z_A, Z_B}` may denote only a transient
observer-side set. It is not a merged participant state, a Hangar shared by A
and B or an independent relational signal. Projecting a pair mean on the same
linear axis does not create information independent of the two monadic
projections.

`R_geom`, staged `R_pace` and later R-family work remain separate post-gate
questions. A closed gate does not prove absence of relevant coordinated
movement; behind-gate diagnosis requires its own named question, eligibility
and validation. It must not be emitted as current `IK_rel`.

Pairing maps and trajectories can expose behavioral patterns. Retain only what
the declared question requires and protect identities and provenance. Pairing,
threshold, axis, epsilon and missingness policies can materially change the
result; disclose and validate them for the stated question.

## 10. Consistency tests and reopening route

The v3.51 package must verify at least:

1. exact same-step `R_0` identity and gate consistency;
2. distinct source-local predecessors and explicit pairing;
3. the shared canonical `IK_w` axis and complete-Z reverse path;
4. formula ranges and genuine numeric zero;
5. projection collisions against complete `Delta Z`;
6. separate gap, move and acceleration questions;
7. all seven fixed sets, 45 typed-status cases and nine invalid profiles;
8. three distinct epsilon kinds and derivative-order behavior;
9. no dynamic component deletion or renormalization;
10. categorical gaps breaking numeric derivative chains;
11. empty-denominator, sparse-coverage and overlap behavior;
12. exact raw/policy/display separation and three consumer projections;
13. migration identity and preservation of nonconforming evidence;
14. no resonance, alignment, causality or action claim.

The adjacent assertion-checked Phases A–F provide reference evidence. They do
not establish runtime conformance. The contract reopens if the shared monadic
axis, Layer-4 handoff, atomic identity, component profile, status precedence,
window basis or supported claim changes.

## 11. Release boundary

This method source changes no software and establishes no implementation
conformance, production threshold, epsilon calibration, coupling, action or
Controller authority. Repository publication, a release tag, a GitHub Release
and a DOI remain separate publication acts.
