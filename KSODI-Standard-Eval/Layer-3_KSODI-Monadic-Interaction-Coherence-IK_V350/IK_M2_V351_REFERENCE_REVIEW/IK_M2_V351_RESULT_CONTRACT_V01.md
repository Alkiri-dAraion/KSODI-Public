# IK_M2 v3.51 reference result contract V01

Date: 2026-11-05

This reference contract explains the logical result family integrated into the
v3.51 method. It does not prescribe a database schema, physical API or runtime
architecture and does not by itself authorize implementation or release work.

Basis:

- [`IK_M2_AXIS_DEVIATION_DUAL_RESOLUTION_PUBLIC_CONCEPT_V351.md`](../IK_M2_AXIS_DEVIATION_DUAL_RESOLUTION_PUBLIC_CONCEPT_V351.md)
- the frozen Phase-0 basis and reproducible Phases A–G, whose Public reference
  package is reviewed and transferred separately;
- current v3.51 typed-Z and IK method and implementation companions.

## 1. Purpose and question

The contract defines what a v3.51 result means when complete typed
`Z=(K,S,O,D,I)` is read jointly through:

```text
complete typed Z
├── IK_w          active weighted projection
├── IK_M2         normalized complete-state L2 magnitude
├── IK_ref        derived position on the fixed equal-coordinate diagonal
├── AxisDev_ref   normalized distance from that fixed diagonal
└── identity, profiles, statuses, evidence and provenance
```

It answers the result-level question:

> Which distinct values, identities, profiles, status rules and reverse links
> must be retained so that a machine can reproduce the v3.51 readings and a
> human can inspect one governance-readable IK-Gesamtbild without mistaking a
> projection for complete Z or several derived readings for independent
> confirmations?

The contract does not claim that any scalar alone measures empirical
coherence, truth, quality, intention or harm. It defines a question-led
observation basis whose later semantic usefulness must be examined against
declared questions, evidence and reference corridors.

## 2. Frozen input and eligibility

The canonical input is one valid, identity-aligned, complete typed Z record
under the current Layer-2 contract:

```text
coordinate_order = [K,S,O,D,I]
Z in [0,1]^5
complete_gate = true
all five coordinate statuses = numeric
all five coordinate values finite
```

The result inherits at least:

```text
target_event_id
source_entity_id
source_attribution_status
emitting_entity_id, if established
trajectory_id
global_event_index
source_local_index
context_scope_id, where the current profile requires it
z_record_id and z_method_version
coordinate_record_ids
coordinate_order
typed status vector T_Z
coordinate profiles, bases, evidence references and provenance
```

`IK_M2`, `IK_ref` and `AxisDev_ref` are canonical v3.51 complete-state
results only when this complete input gate is open. A reduced `IK^[M]`, an
implicit set of currently numeric coordinates, imputation, zero filling or
renormalization does not create reduced versions of these results. A later
partial-state research contract would require its own name, fixed `M`,
normalization, comparability rules and human decision.

## 3. Result family and names

### 3.1 Selected human/method labels

| Label | Object | Independent result? |
| --- | --- | --- |
| `IK_w` | active weighted projection already governed by the IK profile | yes, relative to its declared profile |
| `IK_M2` | normalized Euclidean magnitude of complete Z | yes, but not semantically sufficient alone |
| `IK_ref` | coordinate of Z on the fixed equal-coordinate diagonal | no; derived support coordinate equal to `mean(Z)` |
| `AxisDev_ref` | normalized Euclidean distance from that fixed diagonal | yes, jointly constrained by `IK_M2` and `IK_ref` |
| `IK-Gesamtbild` | human-facing method/governance term for the jointly navigable view of the above and complete Z | no total value, replacement truth, scalar result or fourth calculation |

### 3.2 Selected logical technical names

The v3.51 result family uses the following logical technical names:

```text
ik_weighted_projection
ik_normalized_l2_magnitude
ik_fixed_reference_axis_position
ik_fixed_reference_axis_deviation
ik_joint_evaluation_view
```

These are stable logical result/view kinds, not prescribed database columns,
table names or API paths. Physical placement remains implementation
architecture.

`IK-Gesamtbild` and `ik_joint_evaluation_view` deliberately name the same
view at two interfaces: the first is the human-facing method and governance
term; the second is the language-neutral logical technical identifier. Neither
name denotes an additional calculation.

The exact formula and geometry identities remain separately explicit:

```text
formula_id = ik_weighted_projection
formula_id = ik_normalized_l2_magnitude
formula_id = ik_equal_coordinate_reference_position
formula_id = ik_equal_coordinate_reference_deviation
reference_geometry_id = z_equal_coordinate_diagonal
metric_id = euclidean_l2
normalization_id = l2_by_sqrt_dimension
view_profile_id = ik_gesamtbild_basic
```

Each identity carries its own version field. Do not duplicate a version suffix
inside the stable identifier unless an implementation migration requires an
explicit immutable alias. Result kind, formula, reference geometry, metric,
normalization, profile, physical field and rendered label remain distinct.

## 4. Mathematics

For `Z=(K,S,O,D,I)` and the fixed reference unit vector

```text
u_ref = (1,1,1,1,1) / sqrt(5),
```

define:

```text
IK_w(Z | p_IK) = w dot Z

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

The mandatory cross-check identity is:

```text
IK_M2(Z)^2 = IK_ref(Z)^2 + AxisDev_ref(Z)^2.
```

The centered-sum formula is the canonical computation for `AxisDev_ref`.
The Pythagorean identity is a validation check; an implementation must not use
subtraction of nearly equal rounded squares as its only numerical route.

### 4.1 Ranges

For complete `Z in [0,1]^5` and a valid current IK profile with nonnegative
weights summing to one:

```text
0 <= IK_w <= 1
0 <= IK_M2 <= 1
0 <= IK_ref <= 1
0 <= AxisDev_ref <= sqrt(6)/5
                         ~= 0.489897948556
```

The finite five-coordinate maximum of `AxisDev_ref` occurs at binary states
with a two-versus-three split between zero and one. `AxisDev_ref` must not be
silently rescaled to `[0,1]`. A later display rescaling would be a separately
named and versioned presentation transform, not the method result.

### 4.2 Interpretation boundary

- `IK_w` answers a declared weighting/projection question.
- `IK_M2` answers how large the complete nonnegative Z vector is under the
  normalized Euclidean metric.
- `IK_ref` locates Z along the stable equal-coordinate reference diagonal.
- `AxisDev_ref` describes internal coordinate dispersion relative to that
  diagonal; in this exact five-coordinate setting it equals the population
  standard deviation of the coordinate values.
- Complete labelled Z is still required to determine which coordinates
  produced the same scalar readings.

None of these statements establishes empirical commensurability, reliability
or equal semantic distance across K/S/O/D/I. Those remain method and
validation questions, not consequences of Euclidean algebra.

## 5. Status and failure contract

Each logical numeric result uses the established result-status domain:

```text
numeric | not_selected | not_observable | not_applicable
```

| Input or selection situation | v3.51 geometric result status | Rule |
| --- | --- | --- |
| valid complete numeric Z and selected v3.51 result profile | `numeric` | compute and retain exact input/profile references |
| result profile/view not selected | `not_selected` | value absent; Z remains unchanged |
| incomplete Z with at least one required `not_observable` coordinate | `not_observable` | value absent; retain full `T_Z` and all reasons |
| incomplete Z only through required `not_selected`/`not_applicable` coordinates | `not_applicable` | value absent; retain full `T_Z` and all reasons |
| invalid identity, duplicate coordinate, range violation, nonfinite value, corrupt profile or arithmetic failure | processing error | no valid method result; never coerce to a common status or numeric zero |

All three fixed-geometry result records share the same complete-Z eligibility
gate. They remain separately typed so that one computation or serialization
failure cannot be hidden by a scalar bundle.

`IK-Gesamtbild` has no numeric `result_status`. Its assembly must disclose
the status and exact record reference of every component. A technical
implementation may use an assembly state such as `complete`, `typed_partial`
or `assembly_error`, but that implementation vocabulary must not replace the
method statuses of the components.

## 6. Logical result record

The smallest conforming logical result record is:

```text
IKV351DerivedResult {
  result_id
  result_kind
  method_version
  formula_id
  formula_version

  eval_unit_id
  target_event_id
  source_entity_id
  source_attribution_status
  emitting_entity_id             # only if established
  trajectory_id
  global_event_index
  source_local_index
  context_scope_id

  z_record_id
  z_method_version
  coordinate_order               # exactly [K,S,O,D,I]
  complete_z_value_or_immutable_ref
  typed_status_snapshot_or_immutable_ref

  result_profile_id
  result_profile_version

  result_status
  result_value                   # unrounded computational value; only for numeric
  result_unit_or_scale
  reason_codes

  reference_geometry_id          # required for IK_ref/AxisDev_ref
  reference_geometry_version
  metric_id                      # Euclidean for v3.51 fixed geometry
  normalization_id               # sqrt(5) cube-scale normalization
  numeric_policy_id
  numeric_policy_version

  created_at
  evaluator_id
  evaluator_version
  provenance_record_id
}
```

`result_value` is the method/result value under the declared numeric policy.
It is not a pre-rounded dashboard value. A rendered decimal, label, colour,
axis position or tooltip is a derived presentation object and must retain a
reverse link to the result record and the display policy that produced it.
Physical schemas may represent this separation differently, but they must not
collapse it.

`IK_w` continues to retain the existing `ik_profile_id`, profile version,
weight vector, projection kind and active coordinate set. The fixed geometry
does not inherit the active weight vector as its reference. A conforming joint
view therefore carries both identities:

```text
active_projection_profile = p_IK
fixed_reference_geometry = z_equal_coordinate_diagonal
```

## 7. IK-Gesamtbild bundle contract

The bundle is a jointly and reverse-navigable view, not a total value,
replacement truth or new truth-bearing aggregate:

```text
IKGesamtbildBundle {
  bundle_id
  bundle_profile_id_and_version
  eval_unit_and_inherited_identity
  z_record_id
  ik_w_result_id
  ik_m2_result_id
  ik_ref_result_id_or_reproducible_formula_ref
  axis_dev_ref_result_id
  active_ik_profile_id_and_version
  fixed_reference_geometry_id_and_version
  component_statuses
  reverse_evidence_and_provenance_refs
  view_or_renderer_version, if materialized
}
```

Rules:

1. no sum, mean or uncalibrated combination of the component values is an
   `IK-Gesamtwert`;
2. `IK_ref` may be shown or reproducibly derived, but its relationship to
   `IK_M2` and `AxisDev_ref` must remain inspectable;
3. the view must permit direct return to labelled K/S/O/D/I values, typed
   statuses and operator evidence;
4. an alert or corridor marker states its question, rule, profile, reference,
   version and evidence window;
5. the view distinguishes state movement from profile/reference change;
6. a rendered line, point, ring or index is a presentation, not a replacement
   for the retained machine object.

## 8. Comparability and movement

Two fixed-geometry results are directly comparable only when all material
conditions match:

```text
same source entity and trajectory
same declared predecessor/window relation
same context scope where required
same Z method and coordinate semantics
same coordinate order and complete-state contract
same result kind and formula version
same metric and normalization
same fixed reference geometry and version
compatible evidence/profile basis for all five coordinates
both statuses numeric
```

`IK_w` additionally requires the same `ik_profile_id`, profile version and
weight vector. Therefore:

- if only the active IK profile changes, `IK_M2`, `IK_ref` and
  `AxisDev_ref` may remain comparable while `IK_w` is not a state delta;
- if coordinate definitions, scales, applicability or fixed geometry change,
  the fixed-geometry results are not silently comparable;
- a joint bundle is only wholly comparable when every requested component is
  comparable. Otherwise it must identify component-level partial
  comparability instead of reporting one bundle delta.

For comparable complete states, retain at least:

```text
Z_start
Z_target
directed complete Delta Z = Z_target - Z_start
||Delta Z|| under each declared movement metric
Delta IK_w
Delta IK_M2
Delta IK_ref
Delta AxisDev_ref
profiles, reference geometry and provenance
```

Second differences require three comparable ordered states and remain
`Delta2 Z`, `Delta2 IK_w`, `Delta2 IK_M2`, `Delta2 IK_ref` and
`Delta2 AxisDev_ref` respectively. Distance, detour and second difference
answer different questions and must not share one unlabeled movement field.

Current `R_0` remains unchanged: it consumes complete comparable signed
`Delta Z` under its own gate and norm profile. Current primary dyadic
`IK_rel` remains unchanged: it compares paired raw `Delta IK_w` under the
exact same stable monadic profile after the exact compatible open canonical
complete dyadic `R_0` gate. No v3.51 geometric component enters either
contract implicitly.

### 8.1 Window and aggregation-order boundary

A later window result must distinguish at least these two questions:

```text
derive_then_aggregate:
  calculate one result per eligible complete Z, then aggregate those results

aggregate_then_derive:
  aggregate one shared eligible set of complete Z vectors coordinate-wise,
  then calculate the result from that aggregate Z
```

Under a stable profile and arithmetic mean, linear `IK_w` and `IK_ref` commute
with averaging. Nonlinear `IK_M2` and `AxisDev_ref` generally do not:

```text
mean(IK_M2(Z_k)) != IK_M2(mean(Z_k))
mean(AxisDev_ref(Z_k)) != AxisDev_ref(mean(Z_k))
```

Neither side is automatically wrong; they answer different questions. A
conforming window therefore states aggregation order, one shared eligible
complete-Z subset, coverage and typed exclusions, window/profile/reference
identity and the exact result formula. It must not use different coordinate
subsets to assemble an apparently complete mean Z. Selection of canonical
window names and default views remains a separate human decision; the static
contract does not silently settle it.

## 9. Numeric policy

A conforming calculation must:

1. reject nonfinite inputs and values outside `[0,1]` beyond the declared
   input tolerance;
2. calculate from unrounded complete Z;
3. use one versioned numeric/tolerance policy;
4. report/store full calculation precision before presentation rounding;
5. clip only a proven floating-point boundary excursion within tolerance,
   never an invalid source or profile;
6. calculate `AxisDev_ref` from centered differences and use the Pythagorean
   identity as an independent check;
7. reject a materially negative radicand rather than hiding it with `max(0,x)`;
8. retain the exact formula and evaluator version used for an executed result.

### 9.1 Raw result, numeric policy and display value

The v3.51 result contract distinguishes three things:

```text
method/result value under numeric policy
!= presentation value under display policy
!= rendered visual mark
```

The mathematical result domain may contain real values. An implementation
stores them through a declared finite computational representation and
numeric/tolerance policy; it does not thereby turn them into natural-number
results. Counts and indices remain integers, and typed statuses remain
nonnumeric.

A conforming display projection records or reconstructibly identifies at
least the source result, display-policy/version, precision, rounding mode,
scale/unit and any clipping or formatting transformation. Thresholds,
comparability decisions, later calculations and method statuses use the
unrounded result under the numeric policy, never the rounded display value.
A small nonzero value must not become an unexplained displayed zero; a view may
use `approx`, a less-than notation or additional digits.

v3.51 fixes this logical separation. The exact role-specific rules for decimal
places, significant digits, axes, labels, tooltips and drill-down belong to the
a later separately reviewed visualization contract.

Required invariants within the versioned tolerance:

```text
IK_M2^2 == IK_ref^2 + AxisDev_ref^2
IK_ref == mean(Z)
AxisDev_ref == population_sd(K,S,O,D,I)
permuting labelled values leaves IK_M2, IK_ref and AxisDev_ref unchanged
changing only p_IK leaves IK_M2, IK_ref and AxisDev_ref unchanged
```

Permutation invariance is mathematical, not semantic interchangeability of
K/S/O/D/I. Complete labelled Z must remain retained.

## 10. Persistence and reconstruction

### 10.1 Laboratory

For laboratory work, retain as much as the governed test design permits:

- complete typed Z and all constitutive coordinate records;
- source material or governed references, evidence and provenance;
- executed `IK_w`, `IK_M2`, `IK_ref` and `AxisDev_ref` results;
- formula, evaluator, numeric policy, profile and reference versions;
- failed attempts and processing errors under the audit/error policy;
- trajectories, windows and presentation versions where they informed a
  human decision.

The v3.51 laboratory reference profile initially persists `IK_ref` as a
first-class derived result rather than merely recomputing it on demand.
Retain its result identity, value, formula and reference-geometry versions,
source-Z reference, evaluator/numeric-policy versions and provenance. Revisit
this persistence decision only after substantial practical use and multiple
investigations provide evidence about audit value, storage cost and reliable
recomputation. This laboratory decision does not impose indefinite productive
retention.

This follows the standing laboratory direction to preserve reconstructibility
for synthetic or otherwise governed material. It does not erase access,
security, copyright or purpose constraints.

### 10.2 Productive environments

Retention follows the declared question, operational need, legal basis,
applicable law, governance and deletion policy. The method requires enough
information to prove or reproduce every retained result used for a decision;
it does not require indefinite retention of raw language in every product.

`IK_ref`, `IK_M2` and `AxisDev_ref` are deterministically recomputable only
if the exact complete Z, formula, numeric policy and reference version remain
available. A productive implementation may cache or recompute them, but must
persist an executed result when auditability, a human decision, later source
deletion, evaluator-version change or operational cost makes reconstruction
otherwise unreliable.

The bundle should normally store exact component references and view version,
not duplicate a fourth scalar truth. A decision snapshot may materialize the
bundle when the displayed state itself is audit-relevant.

## 11. Minimum conformance tests

The implementation handoff must reuse the frozen independent fixtures rather
than redefine expected results from runtime behavior.

1. all 32 Phase-A binary states reproduce the reference values;
2. all-zero and all-one states produce `AxisDev_ref=0`;
3. every binary two-versus-three split reaches `sqrt(6)/5` within tolerance;
4. Phase-B equal-mean cases retain different `IK_M2`/`AxisDev_ref` where
   concentration differs;
5. Phase-C cases show that equal magnitude does not imply equal projection;
6. Phase-D families preserve position-conditioned deviation limits;
7. Phase-E equal-size perturbations retain direction and start/target state;
8. Phase-F trajectories retain path, net movement and visible detours;
9. Phase-G profile changes alter only `IK_w` when Z is fixed; fixed-geometry
   values remain unchanged;
10. K/I reversed-profile controls preserve labelled Z and swap only the
    profile-dependent projection as expected;
11. every numeric fixture satisfies the Pythagorean identity;
12. incomplete typed Z produces the defined nonnumeric statuses and no value;
13. corrupt identity, out-of-range input and malformed profile produce
    processing errors, never zero or `not_applicable`;
14. presentation rounding does not feed back into stored calculations;
15. every bundle drills down to exact Z, component results, profiles and
    provenance;
16. current `R_0` and `IK_rel` fixtures remain unchanged unless a later
    separately reviewed contract explicitly changes them.

## 12. Claims supported and not supported

This contract supports the bounded claim:

> For one complete typed five-coordinate Z record, v3.51 can reproducibly
> retain an active weighted projection and a fixed-reference Euclidean
> geometry consisting of normalized magnitude, reference position and
> reference deviation, while keeping the reverse path to labelled Z and its
> provenance open.

It does not yet support:

- empirical thresholds or reference corridors;
- a total monadic coherence score;
- semantic validation against a declared corpus or domain instrument;
- equivalence of coordinate scales beyond the declared representation;
- weight-ray, learned-axis, affine, corridor or distribution geometry;
- changes to `R_0`, `IK_rel`, the R-family, Controller or alerts;
- production readiness or implementation acceptance.

## 13. Review and reopening points

Implementation review must distinguish mandatory logical fields from physical
placement choices. Separate semantic review must declare its material,
instrument, evaluators and uncertainty rather than treating Phase A–G as
empirical validation.

The v3.51 method decisions reflected here are:

- `AxisDev_ref` is the method label for the v3.51 fixed-reference deviation;
- the five logical technical names in Section 3.2 are accepted;
- `IK_ref` is stored as a first-class laboratory result until later evidence
  supports a different treatment.

Reopen the mathematical core if a counterexample violates an invariant, a
coordinate contract changes, the fixed reference geometry is replaced, or a
semantic test shows that the current question/result mapping is misleading.
Do not reopen it merely because a different later question needs another
explicitly named geometry.
