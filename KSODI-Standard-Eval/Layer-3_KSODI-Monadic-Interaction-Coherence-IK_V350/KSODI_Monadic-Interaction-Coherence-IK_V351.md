# KSODI IK - Source-Attributed Monadic Coherence Projection v3.51

This cumulative successor preserves the v3.50 weighted projection, reduced
profile, dynamics and relational boundaries. It adds the accepted v3.51 fixed
reference geometry, joint evaluation view, representation, window-order and
migration contracts. It does not claim empirical validation or independent
runtime conformance.

This file defines the carrier-neutral IK method against the typed Z contract.
Storage schemas,
pseudocode, migration and test fixtures belong in the separate companion:

- [`KSODI_Monadic-Interaction-Coherence-IK_Implementation-Companion_V351.md`](./KSODI_Monadic-Interaction-Coherence-IK_Implementation-Companion_V351.md)

The complete typed-Z method remains the controlling input contract:

- [`../Layer-2_KSODI-State-Vector-Z_V350/KSODI_State-Vector-Z_V351.md`](../Layer-2_KSODI-State-Vector-Z_V350/KSODI_State-Vector-Z_V351.md)

## 0. What IK is and what it does

V3.51 treats IK as a family of jointly inspectable monadic readings over one
complete typed Z. The established weighted projection asks:

> How strongly does one complete, source-attributed Z state project onto one
> declared and versioned monadic coherence axis?

For one target event `e_A(k_A)`, IK receives the typed Layer-2 record and, when
the complete numerical state exists, projects

```text
Z_A(k_A) = [K_A(k_A), S_A(k_A), O_A(k_A), D_A(k_A), I_A(k_A)]
```

onto one weight vector. The added fixed-reference readings ask about complete
vector magnitude, position on the equal-coordinate diagonal and deviation
from that diagonal. None is a sixth Layer-1 observation; none repairs, imputes
or reinterprets a Z coordinate.

The essential distinction is:

```text
complete typed Z remains the recoverable primary object
IK_w is the active weighted projection
IK_M2 is normalized complete-vector L2 magnitude
IK_ref is the position on the fixed equal-coordinate reference diagonal
AxisDev_ref is normalized distance from that diagonal
IK-Gesamtbild is a navigable joint view, not a total value
reduced IK_w^[M] uses one explicit fixed coordinate set M and is not canonical IK_w
relational coherence begins only after the exact open R0 contract declared by
its branch; current dyadic IK_rel requires explicit dyadic pairing and open
numeric canonical complete dyadic R0 under the exact required profile
```

No IK component is truth, utility, safety, compliance, alignment, resonance
or an overall judgment of an entity. A high `IK_w` means only strong
projection onto its declared axis; the other readings answer their separately
defined geometric questions.

### 0.1 Minimal practical reading

1. Resolve one typed Z record for one source-attributed target event.
2. Select one named, versioned IK result/view profile.
3. For `IK_w`, validate non-negative weights whose sum is one.
4. Construct canonical complete-state IK components only from complete
   `Z_A(k_A)`.
5. If the complete Z state does not exist, preserve `T_Z`; do not substitute
   zero and do not call a renormalized subset canonical IK.
6. If a reduced question is justified, declare non-empty `M` and report
   `IK_w,A^[M]` with its own profile and coverage.
7. Calculate `IK_M2`, `IK_ref` and `AxisDev_ref` under the fixed v3.51
   reference geometry when that result profile is selected.
8. Compute dynamics and windows only under stable identity, result kind,
   profile, geometry and active-coordinate contracts.
9. Keep raw results, assistive interpretation and human display separate and
   preserve the return path to labelled complete Z.

### 0.2 How to read this file

Sections 1-3 establish the reader bridge, identity and typed input. Sections
4-5 define weighted and fixed-reference readings. Sections 6-8 define
comparable dynamics, windows and Hangar views. Sections 9-12 fix downstream,
privacy, migration and formal boundaries.

## 1. Bounded application examples

### 1.1 Human-chatbot interaction

Let `A` denote the human trajectory and `B` the chatbot trajectory. A response
from `B` is evaluated first as its own event `e_B(k_B)`. If all five final
Layer-1 result records are numeric and identity-aligned, canonical `Z_B(k_B)` and
then canonical `IK_w,B(k_B)` may be constructed.

The human and chatbot values remain separate. Two scalar IK values do not
establish shared meaning, acknowledgement, coupling or relational coherence.

### 1.2 Unknown Morse-like signal

An unknown signal may support numeric D and I observations while O is
`not_observable` and other coordinates are not selected. Then the typed Z
record exists, but complete Z and canonical IK do not.

A declared diagnostic such as

```text
IK_w,A^[D,I](k_A)
```

may be computed only if D and I are numeric and its two-coordinate axis is
named and versioned. It must not be reported as full IK or as evidence about
the unknown source's total coherence.

## 2. Architectural position and identity

### 2.1 Position after Z

```text
Layer 1:  K / S / O / D / I
                 |
Layer 2:         Z and T_Z
                 |\
                 | \-> KSODI Full: R0 -> relational branches
                 |
Layer 3:         IK_w + fixed-reference readings + named IK_w^[M]
                 [monadic Standard-Eval]
```

Z-state dynamics and IK-projection dynamics are parallel diagnostics. IK does
not replace `Delta Z`, and `Delta Z` does not require IK. The R0 branch starts
from distinguishable typed Z trajectories plus its own explicit pairing or
constellation contract; it neither consumes IK nor follows from IK.

### 2.2 Atomic IK evaluation unit

The canonical monadic target is:

```text
e_A(k_A)
```

where `A` is one stable or explicitly provisional source identity and `k_A`
is its source-local trajectory position. Global event index `n`, another
source's `k_B`, relational index `j` and pairing map `pi(j)` remain distinct.

Every IK component record must inherit the complete Z identity tuple and add:

```text
target_event_id
source_entity_id
source_attribution_status
emitting_entity_id, if established
trajectory_id
global_event_index n
local_trajectory_index k_A
ik_profile_id
ik_profile_version
weight_vector
result_kind
formula_id and version
projection_kind = canonical | reduced, where applicable
active_coordinate_set
reference_geometry_id and version, where applicable
metric_id and normalization_id, where applicable
numeric_policy_id and version
```

No IK calculation may combine coordinates from different source events,
profiles or trajectory positions. `IK_w` retains the active weight profile;
the fixed-reference readings retain their separate geometry identity.

## 3. Typed input contract

### 3.1 Required Z input

IK consumes the typed Z record, including:

```text
T_Z,A(k_A)
= [status_K, status_S, status_O, status_D, status_I]
```

with each status in:

```text
numeric(value in [0,1])
not_selected
not_observable
not_applicable
```

The derived binary `A_Z` may assist filtering, but it cannot replace `T_Z` or
its reasons and provenance.

### 3.2 Complete-input gate

Canonical IK is eligible only when:

```text
complete_Z_state = complete
Z_A(k_A) in [0,1]^5 exists
all inherited identities and profiles are valid
```

The presence of five storage fields is insufficient. Every coordinate must be
numeric under the selected Z view.

### 3.3 IK component result type

The external result domain is:

```text
numeric(value in [0,1])
not_selected
not_observable
not_applicable
```

Recommended propagation for each selected complete-state IK component:

| Condition | IK status | Required retention |
| --- | --- | --- |
| no relevant result/view profile selected | `not_selected` | typed Z reference and selection reason |
| complete Z and valid profile/geometry | `numeric` | Z reference, result kind, formula, profile/geometry and numeric policy |
| incomplete Z with any required `not_observable` coordinate | `not_observable` | full `T_Z` and coordinate reasons |
| incomplete Z only because required coordinates are `not_selected` or `not_applicable` | `not_applicable` | full `T_Z` and coordinate reasons |
| invalid identity, malformed weights or calculation failure | no valid IK result | processing error separate from result status |

This precedence communicates that a required observation could not be made.
It does not erase the other coordinate statuses retained in `T_Z`. Each
component remains separately typed; a joint view discloses every component
status and does not manufacture one numeric bundle status.

## 4. Coherence-axis profile

Let the canonical weight vector be:

```text
w(p_IK) = [w_K, w_S, w_O, w_D, w_I]
```

with:

```text
w_X >= 0
sum_X w_X = 1
```

The profile `p_IK` defines the projection axis. It must identify the weight
vector, coordinate order, purpose, version and status.

The transparent equal-weight reference profile is:

```text
w_ref = [0.2, 0.2, 0.2, 0.2, 0.2]
```

It is a declared reference axis, not an empirical optimum or universal claim.
Domain, learned or adaptive axes are different profiles and require separate
validation and comparability rules.

The fixed v3.51 reference geometry is a separate identity:

```text
u_ref = (1,1,1,1,1) / sqrt(5)
reference_geometry_id = z_equal_coordinate_diagonal
metric_id = euclidean_l2
normalization_id = l2_by_sqrt_dimension
```

The equal-coordinate diagonal is retained even when the active `IK_w` profile
is non-equal. It is a transparent reference, not a learned optimum, target or
self-confirming empirical axis. Learned, weight-ray, affine and
question-specific corridor geometries remain separately named later research.

A zero weight does not waive the complete-Z requirement for canonical IK. If a
profile intentionally excludes coordinates, it is clearer to declare a
reduced axis and `IK_w^[M]`.

## 5. Canonical and reduced projections

### 5.1 Canonical IK

For complete Z and a valid profile:

```text
IK_w,A(k_A | p_IK)
= w_K K_A(k_A)
+ w_S S_A(k_A)
+ w_O O_A(k_A)
+ w_D D_A(k_A)
+ w_I I_A(k_A)
```

Equivalently:

```text
IK_w,A(k_A | p_IK) = w(p_IK) dot Z_A(k_A)
IK_w,A(k_A | p_IK) in [0,1]
```

Interpretation is relative to the selected axis:

| Signal | Bounded meaning |
| --- | --- |
| high `IK_w` | strong projection onto the declared monadic axis |
| middle `IK_w` | mixed projection on that axis |
| low `IK_w` | weak projection on that axis |

### 5.2 Declared reduced projection

For one fixed, non-empty coordinate set

```text
M subset of {K,S,O,D,I}
```

and only when every coordinate in `M` is numeric:

```text
IK_w,A^[M](k_A | p_IK_w^[M])
= sum_(X in M) w_tilde_X X_A(k_A)

w_tilde_X >= 0
sum_(X in M) w_tilde_X = 1
```

If a reduced profile is derived from canonical weights, the derivation is:

```text
w_tilde_X = w_X / sum_(Y in M) w_Y
```

and requires a positive denominator. Store the original profile, denominator
and derived profile ID.

`IK_w^[M]` changes the projection question. It is not a missing-data repair and
is not interchangeable with canonical IK or another `IK^[N]`.

The former generic label `IK_applicable` is retired because it hides whether
the active set changed. Legacy values must migrate to an explicit `M` where it
can be recovered; otherwise they remain legacy, non-comparable records.

### 5.3 Complete-state fixed-reference readings

For complete `Z=(K,S,O,D,I)` define:

```text
IK_M2(Z)
  = ||Z||_2 / sqrt(5)
  = sqrt((K^2+S^2+O^2+D^2+I^2)/5)

IK_ref(Z)
  = (u_ref dot Z) / sqrt(5)
  = (K+S+O+D+I)/5

AxisDev_ref(Z)
  = ||Z - (u_ref dot Z)u_ref||_2 / sqrt(5)
  = sqrt(((K-IK_ref)^2 + (S-IK_ref)^2 +
          (O-IK_ref)^2 + (D-IK_ref)^2 +
          (I-IK_ref)^2)/5)
```

Mandatory validation identity:

```text
IK_M2(Z)^2 = IK_ref(Z)^2 + AxisDev_ref(Z)^2
```

Ranges:

```text
0 <= IK_M2 <= 1
0 <= IK_ref <= 1
0 <= AxisDev_ref <= sqrt(6)/5
```

`AxisDev_ref` equals the population standard deviation of the five coordinate
values under this exact geometry. It is not silently rescaled to `[0,1]`.
Compute it from centered differences; use the Pythagorean identity as a
cross-check rather than subtracting rounded near-equal squares.

`IK_ref` is a derived support coordinate, not an independent confirmation of
`IK_M2` or `AxisDev_ref`. In governed laboratory work it is retained as a
first-class result initially; productive retention remains purpose-, law- and
governance-bound.

No partial `IK_M2^[M]`, `IK_ref^[M]` or `AxisDev_ref^[M]` belongs to the v3.51
canonical method. A later partial-state question requires its own fixed `M`,
normalization, names, profiles and validation.

### 5.4 IK-Gesamtbild / `ik_joint_evaluation_view`

The `IK-Gesamtbild` is the human-facing term for a jointly navigable view of:

```text
complete labelled typed Z
IK_w
IK_M2
IK_ref
AxisDev_ref
component identities, statuses, profiles, geometry and provenance
```

The language-neutral logical view identifier is
`ik_joint_evaluation_view`. The view is not an `IK-Gesamtwert`, another
calculation or an Ersatzwahrheit. It retains direct drill-down to labelled
K/S/O/D/I, exact operands and evidence. Every rendered line, ring, point,
tooltip or rounded value remains a presentation object under its own policy.

## 6. Comparability and dynamics

### 6.1 Comparability gate

Two numeric IK component results are comparable only when they preserve:

- source identity and intended source-local trajectory;
- evaluation-unit granularity and context scope;
- Layer-1 and Z definitions, versions and coordinate order;
- result kind, formula version and numeric policy;
- projection kind and active coordinate set, where applicable;
- reference geometry, metric and normalization, where applicable;
- complete numeric Z at every required point.

Two `IK_w` values additionally require the same weight-profile identity and
weight vector. Two reduced values additionally require the same fixed `M`,
parent profile and reduced profile. Canonical and reduced values are not
directly comparable. The component results inside one `IK-Gesamtbild` may
therefore have different comparison eligibility; the bundle does not erase
that component-level distinction.

### 6.2 First and second differences

For comparable canonical values:

```text
Delta IK_w,A(k_A)
= IK_w,A(k_A) - IK_w,A(k_A-1)
in [-1,1]

Delta2 IK_w,A(k_A)
= Delta IK_w,A(k_A) - Delta IK_w,A(k_A-1)
in [-2,2]
```

Under stable weights and complete comparable Z states:

```text
Delta IK_w,A(k_A) = w dot Delta Z_A(k_A)
```

The identity does not hold across changing profiles or active sets. A change
in `T_Z` is a categorical status transition, not numeric IK drift.

Reduced dynamics are named `Delta IK_w,A^[M]` and `Delta2 IK_w,A^[M]` and require
the same fixed `M` and profile at all points.

For each comparable fixed-reference component `Q` in
`{IK_M2, IK_ref, AxisDev_ref}`:

```text
Delta Q_A(k_A) = Q_A(k_A) - Q_A(k_A-1)
Delta2 Q_A(k_A) = Delta Q_A(k_A) - Delta Q_A(k_A-1)
```

These scalar changes answer different questions from complete state movement.
Every trajectory record used for interpretation must therefore keep:

```text
Z_start
Delta Z = Z_target - Z_start
||Delta Z||_2
Z_target
component-wise Delta Z
profile, geometry and provenance
```

In particular:

```text
Delta IK_M2 != ||Delta Z||_2 / sqrt(5)
```

in general. The left side is a change in distance from the origin; the right
side is the length of the travelled state step. Neither alone exposes the
direction of `Delta Z`. A multi-step path length may also exceed the direct
distance between its endpoints. Detours should remain visible rather than be
compressed into endpoint equality.

### 6.3 Changing axes

If weights change, do not report a canonical `Delta IK_w`. An implementation
may separately diagnose state movement and axis movement, but must name both
terms and retain both profiles. The fixed-reference readings may remain
comparable when their geometry, metric, normalization and all other comparison
conditions remain unchanged. Stable fixed-reference geometry does not make
changed `IK_w` profiles comparable.

## 7. Windows and Sigma

Every window first exists as a separately identified derived object. It must
declare at least:

```text
window_id
window_kind                      # event | clock | semantic/episodic | other named profile
boundary policy                  # tumbling | sliding | explicitly named alternative
exact ordered member references
included and excluded partitions with reasons
source_entity_id and trajectory_id
context_scope_id and observation granularity
result kinds and profiles
aggregation_order
aggregator and version
minimum count and coverage policy
status counts, processing failures and provenance
```

A derived window or aggregate is not a target event and must never be written
back as the state of a participant.

### 7.1 Eligible component subset

For a declared non-empty source-local window `W_A` and result kind `Q`, define
the complete compatible subset:

```text
W_A^Q
= {k_A in W_A | Q_A(k_A) is numeric and comparable under one fixed contract}

coverage_Q(W_A) = |W_A^Q| / |W_A|
```

`|W_A|` must be positive. An empty or invalid window produces no valid numeric
coverage or aggregate; it must not be represented through `0/0`, zero coverage
or a numeric zero aggregate. V3.51 defines no universal minimum count or
coverage threshold. Each profile must declare them; a numeric aggregate is
incomplete reporting without denominator, coverage and status partitions.

### 7.2 Derive then aggregate

For one declared component aggregator `Agg_Q`:

```text
Q_Sigma,A(W_A)
= Agg_Q({Q_A(k_A) | k_A in W_A^Q})
```

This order derives one component result from each eligible complete Z and then
aggregates those per-state results.

### 7.3 Aggregate then derive

The alternative order first aggregates one shared eligible set of complete Z
vectors coordinate-wise:

```text
Z_agg,A(W_A) = Agg_Z({Z_A(k_A) | k_A in W_A^Z})
Q_from_Z_agg,A(W_A) = Q(Z_agg,A(W_A))
```

`Z_agg,A(W_A)` has its own derived-object identity, exact members, coverage,
aggregator, status and provenance. It is neither a participant state nor an
observed target event.

For the transparent v3.51 arithmetic-mean reference case, stable weights and
one identical complete subset give:


```text
mean(IK_w,A) = w dot mean(Z_A)
mean(IK_ref,A) = IK_ref(mean(Z_A))
```

The equalities are linear, not permission to mix different subsets.
`IK_M2` and `AxisDev_ref` are nonlinear, so in general:

```text
mean(IK_M2(Z)) != IK_M2(mean(Z))
mean(AxisDev_ref(Z)) != AxisDev_ref(mean(Z))
```

For the convex functions used here, Jensen's inequality supplies a mathematical
direction for the arithmetic-mean reference case; it does not make either
order the universally preferred semantic answer. The order must be named
because the two objects answer different questions.

### 7.4 Reference window family and open profiles

The transparent v3.51 reference family permits event- or clock-based,
tumbling or sliding windows using arithmetic means, exact member lists and
explicit coverage. This is a reproducible reference case, not an empirically
optimal window policy.

Later profiles may use median, quantiles, robust estimators,
semantic/episodic boundaries, change points or distribution views. They must
be named and validated separately. They do not invalidate the v3.51 reference
contract and must not be silently reported as its arithmetic mean.

Reduced window projections must disclose the same fixed `M`, reduced profile,
subset and coverage. Deltas between windows require compatible window policy,
profile, result kind and processing order.

Window aggregation, state movement and result movement are distinct:

```text
Delta Z
Delta2 Z
Delta Q
Delta2 Q
movement length
window-to-window difference
```

Their operands and order must be explicit. None may be substituted for another
merely because all are described as change.

## 8. Sigma(Hangar)

Hangar stores derived views, not a new monadic formula and not the transient
interaction space. An IK Hangar may contain complete typed Z points, each IK
component, compatible window objects, trajectory steps and declared
distribution diagnostics.

Required stratification includes:

- result kind and formula version;
- canonical versus reduced `IK_w` projection;
- `M` for every reduced record;
- IK profile or fixed reference geometry and version;
- source/context scope and window policy;
- numeric coverage and non-numeric status counts;
- aggregation order and exact members;
- distribution-distance definition for cross-window drift.

Never pool different result kinds, changing `M`, changing weight profiles,
different aggregation orders or categorical statuses into one unlabeled
numeric distribution. A Hangar distance is non-negative distribution movement
and must not be confused with a signed component delta. Every point or summary
must retain a drill-down path to exact Z operands, identities, profiles and
admissible evidence.

Corridor, learned-axis and adaptive-axis analysis remains research work unless
its profile, validation and comparison contract is explicitly accepted.

## 9. Downstream boundaries

**Cross-cutting evidence-object guard.** Every IK view inherits the exact
tagged `Z` observation object from which it is derived. A future residual-view
IK therefore remains distinct from its raw-view counterpart even under the
same weights and even when scalar values happen to match. Subtracting finished
IK scores does not construct a residual IK. The later compatibility contract
is Future Work and changes no v3.51 formula.

### 9.1 Relation to R0

`R0` is evaluated on its separate relational branch from distinguishable typed
monadic Z trajectories and an explicit pairing or constellation contract. It
is not calculated from IK, does not consume IK as a prerequisite and cannot be
opened by two high `IK_w` values.

### 9.2 Relation to IK_rel and the R-family

Canonical IK is monadic. Current `IK_rel` is dyadic and begins only after an
explicit dyadic pairing and an open numeric canonical complete dyadic `R0` gate
under the exact required profile. A reduced or n-adic R0 result does not open
that branch. `IK_rel` cannot be inferred from, or reduced to, two scalar
monadic readings. Its current primary movement component uses comparable
paired `Delta IK_w` only under its own contract; `IK_M2`, `IK_ref` and
`AxisDev_ref` remain available as separately typed diagnostic inputs and do not
silently redefine the released relational formula. Any later component bundle
must name its question, basis, eligibility, cardinality and profile.

IK does not establish receipt, acknowledgement, shared meaning, successful
decoding, coupling, causality or resonance.

## 10. Fairness, privacy, retention and implementation boundary

Weights are governed analytic configuration choices, not observed facts. They
may encode declared priorities, and a changed profile may change rankings
without any change in observations. Report the profile and avoid
cross-group or cross-domain interpretation without validation.

No IK value, ranking, corridor result, dynamic, assistive interpretation or
Hangar view selects or authorizes steering or intervention. Any later action
requires a separately governed Controller or human decision outside the IK
calculation.

IK, reduced projections, dynamics, windows and Hangar views may remain
identifiable or linkable even without raw text. Retain the minimum data needed
for the declared purpose; protect source IDs, trajectory maps and provenance;
do not describe pseudonymized values as anonymous.

Every implementation and display must distinguish:

```text
raw mathematical result
numeric/tolerance policy
display value and rounding policy
assistive interpretation
```

A rounded human display is not the stored mathematical operand. The richest
purpose-required machine object retains complete typed Z, component results,
identities, profiles, geometry, status, uncertainty and provenance. An
assistive LLM may receive a governed, purpose-bound projection of that object;
it must not invent missing evidence or treat its interpretation as a method
result. A human/governance view may simplify further, but must disclose its
loss and retain a route back to the admissible machine record.

The mathematical method is authoritative. The companion is subordinate
implementation guidance. No storage convention, threshold, visualization,
LLM explanation or software default may silently redefine a result.

## 11. Migration and conformance classes

V3.51 distinguishes method conformance from continued research value. A record
or corpus may be classified as:

```text
v351_conformant
legacy_reconstructible
legacy_partially_reconstructible
legacy_noncomparable
```

`reconstruction_pending` is a workflow state for material whose class has not
yet been established; it is not a numeric or method result status.

Migration must preserve the original object, transformation identity and
reason for every exclusion or uncertainty. Missing provenance may be reported
as missing, but must not be reconstructed as fact. `not v3.51 conformant` does
not mean worthless, false or unusable for every research question.

## 12. Formal summary and variable reference

### 12.1 Compact contract

```text
# typed Layer-2 input
T_Z,A(k_A) preserves numeric / not_selected / not_observable / not_applicable

# canonical profile
w(p_IK) >= 0
sum_X w_X = 1

# complete canonical projection
complete Z_A(k_A) -> IK_w,A(k_A | p_IK) = w dot Z_A(k_A)

# fixed-reference complete-state readings
IK_M2(Z) = ||Z||_2 / sqrt(5)
IK_ref(Z) = mean(K,S,O,D,I)
AxisDev_ref(Z) = population_sd(K,S,O,D,I)
IK_M2^2 = IK_ref^2 + AxisDev_ref^2

# reduced, visibly non-canonical projection
M != empty
all X in M numeric
IK_w,A^[M](k_A | p_IK_w^[M]) = sum_(X in M) w_tilde_X X_A(k_A)

# source-local comparable dynamics
Delta IK_w,A(k_A) = IK_w,A(k_A) - IK_w,A(k_A-1)
Delta2 IK_w,A(k_A) = Delta IK_w,A(k_A) - Delta IK_w,A(k_A-1)
Delta IK_w,A(k_A) = w dot Delta Z_A(k_A)  # only under stable complete contract

# windows: name one of two orders
derive_then_aggregate: Q(Z_k) -> Agg_Q({Q_k})
aggregate_then_derive: Agg_Z({Z_k}) -> Q(Z_agg)
report exact members, denominator, coverage, statuses, order and provenance

# relational boundary
IK is monadic
R0 does not derive from IK
current dyadic IK_rel begins only after explicit dyadic pairing and open
numeric canonical complete dyadic R0 under the exact required profile; it is
not two scalar `IK_w` values
```

### 12.2 Variable reference

| Variable | Semantic role |
| --- | --- |
| `e_A(k_A)` | source-attributed target event |
| `T_Z,A(k_A)` | mandatory typed five-coordinate status vector |
| `Z_A(k_A)` | complete canonical numerical state |
| `p_IK` | named and versioned canonical projection profile |
| `w(p_IK)` | canonical coherence-axis weights |
| `IK_w,A(k_A \| p_IK)` | canonical monadic projection |
| `IK_M2` | normalized complete-vector L2 magnitude |
| `IK_ref` | fixed-reference-axis position; arithmetic mean of complete Z |
| `AxisDev_ref` | normalized Euclidean deviation from the fixed diagonal; population standard deviation |
| `ik_joint_evaluation_view` | technical identifier for the non-scalar IK-Gesamtbild |
| `M` | explicit non-empty coordinate set for a reduced view |
| `p_IK_w^[M]` | named reduced projection profile |
| `IK_w,A^[M]` | visibly reduced, non-canonical projection |
| `Delta IK_w,A`, `Delta2 IK_w,A` | comparable source-local projection dynamics |
| `W_A^Q` | complete compatible subset for one result kind Q |
| `coverage_Q(W_A)` | numeric comparable coverage for Q |
| `Z_agg,A(W_A)` | separately identified derived aggregate Z object |
| `Q_Sigma,A(W_A)` | declared aggregate over comparable per-state Q results |
| `R0` | relational comparability gate, independent of IK construction |
| `IK_rel` | strictly dyadic relational coherence branch after explicit dyadic pairing and open numeric canonical complete dyadic R0 under the exact required profile |

### 12.3 Consistency tests

A conforming method or implementation must satisfy:

1. no canonical IK without complete canonical Z;
2. no status loss from `T_Z` to a binary mask;
3. no zero fill or silent subset renormalization;
4. every reduced value discloses fixed `M` and its profile;
5. canonical/reduced projections and different result kinds are not mixed in dynamics or windows;
6. the weighted projection identity is claimed only under stable complete conditions;
7. weights are non-negative, sum to one and are versioned;
8. fixed-reference readings satisfy their ranges and Pythagorean identity within declared tolerance;
9. `Delta IK_M2` is never labelled as Z-step length;
10. windows are non-empty, and members, order, coverage plus non-numeric statuses accompany aggregate views;
11. nonlinear derive/aggregate orders are not treated as interchangeable;
12. raw results, numeric policy, display values and interpretations remain distinct;
13. IK remains monadic and does not open or replace R0;
14. IK_rel and the R-family remain outside this method.

## 13. Separate implementation companion

The adjacent implementation companion supplies conditional schemas,
pseudocode, migration rules, examples and tests. It must preserve this method's
identity, typed-status, projection-kind and relational-boundary contracts.
