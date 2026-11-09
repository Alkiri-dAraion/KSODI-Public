# Layer 1 Measurement Basis and Reference Discipline v3.51

Version: KSODI v3.51
Scope: Layer 1 operator evaluation and its boundary to source-local sequence,
window aggregation, Hangar projection and relational diagnostics

## 1. Purpose

Every KSODI Layer 1 operator evaluates one declared target event. A numerical
operator value is meaningful only when the measurement basis used for that
evaluation is also declared. The required basis is not the same for every
operator.

An information baseline, a structural profile, a signal-detector profile, a
visible source space, a context scope and a historical Hangar scope answer
different questions. They must not be represented as one interchangeable
reference space.

This document defines:

- what a declared measurement basis is;
- which type of basis each Layer 1 operator requires;
- how target event, context, profile and reference data remain separated;
- when source-local sequential and aggregated comparisons are applicable;
- how Hangar projections are derived without altering original operator
  values;
- which information an implementation must preserve.

This document does not introduce another KSODI operator. It makes the
measurement conditions of the existing operators explicit and reproducible.
The five operator specifications remain authoritative for their own formulas,
components and applicability rules.

A profile may simplify an implementation or adapt it to a bounded observation
setting, but it must not hide the precision it leaves behind. Any deliberate
relaxation of identity, measurement-basis, visibility, applicability,
comparability or provenance requirements must name the relaxed requirement,
the operational reason, the expected information loss and the resulting limit
on comparison. A relaxed result must not be reported as equivalent to the
unrelaxed method result.

This cumulative successor retains the complete v3.50 discipline and adds the
cross-operator identity, representation, window and migration contracts made
explicit during the K/S/O/D/I v3.51 review. It changes no operator formula and
does not claim independent runtime conformance.

Related public references:

- [operator-folder orientation](README.md)
- [Layer-1 operator template](OPERATOR_TEMPLATE_V351.md)
- [operator-distinction research note](LAYER_1_OPERATOR_DISTINCTION_WORKING_NOTE_V351.md)
- [public architecture](../../KSODI-Architecture_V350.md)
- [public implementation guardrails](../../IMPLEMENTATION_GUARDRAILS.md)
- [Hangar, Sigma, drift and point-cloud views](../../KSODI-Hangar_V350.md)
- [O v3.51 Source-Need Gate](KSODI_Operator-O_Source-Need-Gate_V351.md)

### 1.1 Shared v3.51 result and representation contract

Keep reusable rules, concrete operands and representations distinct:

```text
operator profile and version
  != concrete measurement-basis instance
  != exact candidate/admitted/excluded member identities

profile-native observations and evidence
  -> versioned normalization or transformation
  -> raw method operands
  -> raw method result or typed non-numeric result
  -> separately versioned display value, if any
```

The profile states how the bounded operator question is instantiated. The
basis instance records which actual requirement set, context scope, reference
set, detector input or baseline was used. A profile identifier alone is not
the provenance of a concrete result.

Normalization records parameters, units or scale, resolution, clipping and
known loss. A display policy may round, label or simplify, but its value never
becomes a method operand and never overwrites the raw result. Equal display
values do not establish equal raw values, bases, evidence or target events.

One evaluation may support three linked representations:

1. a machine-readable evaluation object with full typed identity, operands,
   result/status and provenance;
2. an attributed assistive-model interpretation over an authorized,
   question-bound projection;
3. a human/governance display with explicit rounding or simplification and a
   reverse route to the machine object.

The latter two are derived views, not replacement truths. Their model,
prompt, tool, projection and display-policy provenance remains recoverable.

## 2. Human Quick Guide: What Fills Which Operator?

Before calculating an operator, identify exactly one target event and answer
the corresponding measurement-basis question:

| Operator | Required measurement basis | What fills the coordinate? | What must not be inserted silently? |
| --- | --- | --- | --- |
| `K` | declared context scope, non-empty expected-requirement set and availability relation | observable fulfillment of expected context requirements under that relation | all available history, mere storage, hidden state or Hangar expectation |
| `S` | declared structural profile | observable form, segmentation, boundaries, order and active structural components | factual support, intended meaning or receiver understanding |
| `O` | Source-Need Gate plus declared visible `Ref` where numeric O is applicable | visible grounding and traceability against that exact reference space | hidden sources, world knowledge or a historical expectation corridor |
| `D` | declared signal, carrier, detector, segmenter and normalizer profile | observable signal support and reconstruction-relevant local dispersion | context proximity, grounding, intent or historical typicality |
| `I` | declared visible information baseline `Ref` | observable information difference of the target relative to that baseline | another entity's event, an undeclared whole-conversation baseline or Hangar expectation |

A human-readable five-dimensional `Z` view contains one static, declared
Layer-1 value for each coordinate. Optional sequential, projection,
aggregation or relational diagnostic views must remain outside those five
coordinates and retain their own names and provenance.

The shortest valid workflow is:

```text
source-attributed target event
  -> operator-specific measurement basis
  -> component applicability
  -> Layer 1 value
  -> canonical evaluation record
       |-> source-local comparability gate
       |     -> Delta / Delta2
       |     -> applicability-aware window
       |     -> optional Hangar projection and contextual deviation
       |
       +-> explicit dyadic pairing or n-adic constellation map
             -> R0: open numeric canonical complete gate
                    under the exact required profile
             |-> IK_rel
             |-> staged R_geom
             +-> staged optional R_pace
```

The three post-`R0` branches remain parallel calculations with their own
measurement bases, profiles, applicability and weights. A branch output is not
the undeclared input of another branch.

All five Layer-1 operators are strictly monadic and source-attributed. Temporal
comparisons occur only within the same declared trajectory. This does not mean
that every static operator formula uses its own predecessor: each operator
retains its appropriate current-state measurement basis, while `Delta X_A(k_A)`
compares applicable values of `X_A` along trajectory `A`.

Layer-1 operators may be inspected individually through monadic trajectory,
projection or aggregation views. After an open numeric canonical complete
`R0` gate under the exact required profile, operator-specific
relational comparison views could be defined as separate later-layer
diagnostics. No such comparison is active in the v3.51 Layer-1 operator line;
candidate post-`R0` views and operator-only bypass routes belong to v3.60
Future Work and require their own applicability and comparability contracts.
They are neither complete `Z`, canonical `IK`, `IK_rel` nor resonance. A
projection of one operator must not be reported as full `IK`, and one
operator-specific relational signal is not by itself an R-family result.

## 2.1 Bounded Examples at a Glance

### Human and chatbot

A human source `A` emits one contribution and a chatbot source `B` emits a
reply. The events share an exchange but remain separate target events and
source-local trajectories. Sender and receiver roles may reverse at the next
event without changing `A` and `B`. Each Layer-1 coordinate is calculated
monadically before an explicit pairing can open `R0`.

### Unknown Morse-like carrier

A detector observes repeated marks and gaps on a channel. The physical emitter
and semantic code may still be unknown, so the records use an explicitly
provisional observed-source identity. A declared noise or prior-carrier
baseline may make informational difference observable without supplying the
message meaning. D can evaluate distinguishability under a carrier and detector
profile; O may remain non-numeric while no admissible reference space is
available. Repetition may support an anomaly or contact-attempt hypothesis but
does not prove acknowledgement, decoding, intent, attack or causal coupling.

### Robots or embodied agents

Two robots may exchange formally structured signals while their spatial paths
diverge, or remain geometrically close while their response pace separates.
Layer 1 still evaluates attributable events one operator at a time. After an
open numeric canonical complete `R0` gate under the exact required profile,
staged `R_geom` and staged optional `R_pace` remain parallel
research branches with separate bases; neither is a motion controller or
physical safety mechanism.

## 2.2 Coordinate Order and Process Topologies

The five operator values remain independently evaluable under their own
measurement bases and profiles. Their canonical coordinate order is a reporting
convention:

```text
Z_A(k_A) =
  (K_A(k_A), S_A(k_A), O_A(k_A), D_A(k_A), I_A(k_A))
```

It is not a universal causal execution order. Where process orientation helps
explain a declared event, distinguish:

```text
sender-side formation:        K -> S -> O -> D -> I
receiver-side reconstruction: I -> D -> O -> S -> K
```

The receiver-side direction is preferred, iterative and profile-sensitive. It
does not require every operator to be selected in every practical pass and
does not claim access to hidden biological or machine processing. A known
convention may abbreviate or parallelize reconstruction. An unfamiliar carrier
may require repeated movement among detection, distinguishability, source
checking, structural hypotheses and context.

## 3. Core Principle

A Layer 1 value must be interpretable as:

```text
X_A(k_A | declared measurement basis, p_X)
```

where:

- `X` is one KSODI operator;
- `A` is the stable source-attributed entity or provisional observed-source
  identity associated with the target event;
- `k_A` is the source-local position in trajectory `A`;
- `p_X` is the declared and versioned operator profile.

The phrase *declared measurement basis* is an explanatory umbrella term. It
does not introduce a new canonical mathematical symbol. Each operator retains
its own appropriate terminology.

A measurement basis may determine:

- which current-state calculation is permitted;
- which detector, normalizer or profile is active;
- which source or context material is visible and admissible;
- which components are applicable;
- whether a numerical value may be calculated at all.

It must not silently introduce:

- events outside the declared evaluation unit;
- hidden sources;
- another entity's state;
- historical expectations from the Hangar;
- inferred intention;
- a causal explanation for an observed deviation.

## 4. Atomic Evaluation Unit

The target of a Layer 1 evaluation is one observable event:

```text
e_A(k_A)
```

A minimal event record must distinguish at least:

```text
target_event_id
source_entity_id
emitting_entity_id, if established
source_attribution_status
trajectory_id
trajectory_index = k_A
global_event_index = n
context_event_ids
exchange_id, if applicable
reply_to_event_id, if applicable
carrier_type
observed_at
```

These fields are not interchangeable:

```text
source_entity_id != trajectory_id != target_event_id
```

One attributed source entity may produce multiple trajectories. One trajectory
contains multiple events. One target event may be connected to context events
without becoming part of a mixed multi-entity state. If the physical emitter
is unknown, a provisional observed-source identity keeps repeated carrier
events attributable without pretending that attribution has already been
solved. Later attribution changes require provenance; they must not silently
rewrite the earlier trajectory.

`context_event_ids` may identify visible contextual material admitted by a
declared operator profile. They must not replace `target_event_id`.

### 4.1 Sender and receiver are exchange-relative roles

Entity A and Entity B are stable source identifiers within the declared
observation. They may represent established entities or explicitly provisional
observed sources. Sender and receiver are roles associated with a particular
event or exchange edge; they are not permanent entity types.

For one contribution:

```text
sender_event_id = event_A_42
source_entity_id = entity_A
emitting_entity_id = entity_A
source_attribution_status = confirmed
sender_entity_id = entity_A
receiver_entity_id = entity_B
exchange_id = exchange_09
```

For a later contribution, Entity B may become the emitting entity:

```text
target_event_id = event_B_17
source_entity_id = entity_B
emitting_entity_id = entity_B
source_attribution_status = confirmed
reply_to_event_id = event_A_42
exchange_id = exchange_09
```

Both target events are evaluated monadically before any explicitly relational
calculation is performed.

## 5. Operator-Specific Measurement Bases

### 5.1 Operator I — declared static baseline

The canonical static Operator I value uses an explicit, visible and versioned
reference baseline `Ref`. It remains attached to one target event and one
source trajectory.

A direct event-to-predecessor information comparison may be retained as an
optional source-local diagnostic. It is not a competing static I coordinate,
must not fill the I slot of `Z`, and must remain distinct from `Delta I`, which
compares two already calculated static I values.

The implementation must not silently substitute:

- the most recent event from another entity;
- an entire conversation;
- an undeclared context summary;
- a Hangar expectation corridor.

If the required baseline, operation or provenance exists or is expected but
cannot be inspected by the evaluator:

```text
I_A(k_A) = not_observable
```

If no permitted static baseline exists under the selected profile, or a
completed selection produces no admissible non-empty basis:

```text
I_A(k_A) = not_applicable
```

Malformed identity, an invalid profile or a calculation failure is a
processing failure and produces no valid I result. Every successful applicable
finite calculation emits `operator_result_status = numeric` and a
`result_value in [0,1]`. The baseline record must identify the exact declared
reference used in the calculation. Any optional predecessor diagnostic must
identify its predecessor separately and must not be merged with static I.

See [Operator I](KSODI_Operator-I_Observable-Information-Impulse_V351.md).

### 5.2 Operator S — declared structural profile

Operator S requires a declared structural evaluation profile. The profile may
specify:

- carrier type;
- segmentation rules;
- structural detectors;
- required or observable markers;
- active S components and component mask;
- weights and normalizers;
- minimal or extended numeric profile;
- applicability rules.

S evaluates the observable or reconstructable form under this profile. The
structural profile is not a semantic source space. It does not establish
whether a contribution is factually supported, contextually expected or
correctly interpreted by a receiver.

Context may be used to select an applicable structural profile. It must not
then enter the numerical S value as an undeclared positive component.

If required structural evidence exists or is expected but cannot be inspected
under a valid selected profile:

```text
S_A(k_A) = not_observable
```

If no valid structural basis applies to the event under that profile:

```text
S_A(k_A) = not_applicable
```

A missing or invalid constitutive profile, invalid detector configuration,
invalid weights or a calculation failure is a processing failure and produces
no valid S result. Every successful applicable finite calculation emits
`operator_result_status = numeric` and a `result_value in [0,1]`.

See [Operator S v3.51](KSODI_Operator-S_Observable-Structural-Coherence_V351.md).

### 5.3 Operator D — declared signal and detector profile

Operator D requires a declared signal, carrier, segmentation, detector and
normalizer profile. D evaluates the observable conditions under which the
target signal can be detected, segmented and reconstructed.

The D measurement basis may specify:

- carrier type;
- observable support units and support ceiling;
- local-unit segmentation;
- expected local variation;
- detector and distance-function versions;
- normalization;
- active D components and component mask;
- applicability rules.

This basis does not determine whether the signal fits surrounding context. A
signal may be highly detectable even when it is:

- unfamiliar;
- unexpected in the current account;
- not grounded in an available source space;
- produced by an unknown system;
- a previously unseen bit pattern;
- a repeated contact sequence.

D therefore remains separated from grounding, contextual expectation and
historical Hangar deviation. The phrase "Shannon-style questions" is used only
as an approximate signal-path analogy: a signal must be observable and
discriminable through a bounded carrier before reconstruction can be attempted.
It is not a checked operationalization or derivation of Shannon's theory. D
remains a KSODI observation coordinate, not a direct Shannon measure.

If no valid local-support or dispersion basis applies under the selected D
profile:

```text
D_A(k_A) = not_applicable
```

If the admitted event is observable but required carrier or detector evidence
cannot expose the units needed by D, the result is `not_observable`. A missing
or invalid constitutive profile, invalid detector configuration or calculation
failure is a processing failure and produces no valid D result. Every
successful applicable finite calculation emits
`operator_result_status = numeric` and a `result_value in [0,1]`.

See [Operator D](KSODI_Operator-D_Observable-Clarity_V351.md).

### 5.4 Operator O — declared visible reference space

Operator O requires the O Source-Need Gate before numerical evaluation. A
numeric O value may be evaluated only when a declared reference space is
available and visible to the evaluator under the active gate and O profile.

The reference space may include:

- visible documents;
- retrieved passages;
- declared source records;
- tool-mediated reference influx;
- accessible policy or system material;
- other explicitly visible evidence objects.

The reference space must be source-attributed and versioned. O must
distinguish at least:

```text
reference not expected
reference optional and absent
reference required but unavailable
reference available but not visible to the evaluator
reference visible but inadmissible or empty after admission
reference available, visible, admissible and non-empty
```

A required source basis that is unavailable, evaluator-invisible or
evidence-undetermined does not produce a low O value. It maps to:

```text
O_A(k_A) = not_observable
```

with the specific gate reason retained. A reference basis that is not expected,
optional and absent, inadmissible or empty after admission maps to
`not_applicable`. An invalid or unresolved source-need policy, inconsistent
gate record, invalid O profile or calculation failure is a processing failure
and produces no valid O result. Every successful applicable finite calculation
emits `operator_result_status = numeric` and a `result_value in [0,1]`.

The visible reference space used by O is not a Hangar expectation corridor.
Source-state evaluation and reference drift are separate diagnostics; neither
is a third numeric O profile.

See [Operator O v3.51](KSODI_Operator-O_Observable-Grounded-Objectivity_V351.md) and the
[O v3.51 Source-Need Gate](KSODI_Operator-O_Source-Need-Gate_V351.md).

### 5.5 Operator K — declared context scope and availability relation

Operator K requires an explicitly declared context scope, a non-empty expected
context-requirement set and one selected availability relation. The scope
identifies which context events, context objects and constraints are admissible
for the target-event evaluation. The relation declares what “available” means,
for example observable evidence of target access, evaluation access or receiver
access.

The shared boundary is:

- stored context is not automatically admitted or available under the selected
  relation;
- evaluator visibility, target access and receiver access are not synonyms;
- K may not treat all conversation history, hidden system state or Hangar
  history as admissible context;
- context events remain distinct from the target event;
- capability or tool availability contributes to K only when a declared
  expected requirement and detector make it part of the selected K profile;
- visible tool output may separately become part of O's `Ref` under an O
  profile, but context presence does not establish grounding;
- an empty expected set is `not_applicable`, not perfect K;
- partial visibility, scope drift and uncertainty remain separate diagnostics
  and do not silently fill canonical K.

Required context or availability evidence that exists or is expected but
cannot be inspected maps complete K to `not_observable`. Absence of a valid
non-empty expected basis maps to `not_applicable`; elective omission maps to
`not_selected`. Invalid identity, profile, scope policy, attribution, weights
or calculation is a processing failure and produces no valid K result. Every
successfully open, applicable and finite K calculation emits
`operator_result_status = numeric` and a `result_value in [0,1]`.

See [Operator K v3.51](KSODI_Operator-K_Observable-Context-Completeness_V351.md) and its
[conditional implementation companion](KSODI_Operator-K_Implementation-Companion_V351.md).

## 6. Four Reference Types That Must Remain Separate

### 6.1 Operator measurement basis

This is the basis required to calculate the current Layer 1 value. Examples
include:

- I baseline;
- S structural profile;
- D signal and detector profile;
- O visible reference space;
- K context scope.

It belongs to the evaluation record of the current target event.

### 6.2 Sequential comparison basis

This is the permitted predecessor or earlier state used for a source-local
temporal comparison such as:

```text
Delta X_A(k_A) = X_A(k_A) - X_A(k_A-1)
```

The earlier record must satisfy the operator-specific comparability
conditions. A sequential predecessor is not automatically the operator
measurement basis; it is a second evaluation record used for comparison.

### 6.3 Window and Hangar scope

A window or Hangar scope selects a collection of stored evaluation records. It
may support:

- aggregation;
- distributions;
- historical corridors;
- trajectory views;
- drift, anomaly or deviation diagnostics.

It does not become part of the original Layer 1 value.

### 6.4 Relational pairing or constellation basis

The current v3.51 `R0` gate supports an explicitly declared dyadic pairing or
n-adic constellation map over distinguishable source-attributed trajectories.
The current `IK_rel` method remains dyadic. A relational basis may identify:

- paired target events or constellation-member events;
- exchange direction;
- sender event and receiving entity;
- reply edge;
- approved comparability gate;
- relational profile.

Pairing must not be inferred from shared context, temporal proximity or
membership in the same conversation. It begins only at the methodologically
declared relational layer and after the required gates. An n-adic `R0` result
does not manufacture or open the current dyadic `IK_rel`; every downstream
branch must declare a compatible cardinality, identity, pairing, profile,
formula and result contract.

## 7. Applicability Is Not Numerical Zero

For every operator, the common external result family must distinguish:

```text
numeric
not_applicable
not_observable
not_selected
```

Retained operator-domain reasons may additionally include:

```text
required_basis_unavailable
not_visible_to_evaluator
no_valid_basis
incomparable
```

Processing failures remain outside the common operator-result family and may
include:

```text
invalid_or_unresolved_identity
profile_missing_or_invalid
invalid_policy_or_configuration
invalid_attribution_or_weights
calculation_error
```

Reason details are not extra numeric values or additional Z statuses.
`required_basis_unavailable` and `not_visible_to_evaluator` map to the common
result `not_observable` while retaining their specific reasons.
`no_valid_basis` maps to `not_applicable`. `incomparable` blocks a requested
Delta or Delta2 construction without deleting the stored static result. A
processing failure produces no valid `operator_result_status` or result value.

None of these states may be collapsed into numerical `0`. A value of `0`
means that an applicable measurement produced the lower endpoint of its
declared scale. `not_applicable` means that no valid operator-domain basis
applies or exists under the declared conditions; it is not a substitute for an
invalid profile or failed calculation. `not_observable` means that the method
question applies but the declared evaluator cannot obtain sufficient observable
support. `not_selected` means that a profile omitted the coordinate by choice;
it must not be disguised as an applicability mask. A view with an electively
omitted coordinate is partial and must not be reported as a complete canonical
five-coordinate `Z` or canonical `IK`.

The shared mapping for every future Layer-1 operator action is:

```text
successful applicable finite result
  -> operator_result_status = numeric
  -> result_value in [0,1]

required basis or evidence exists or is expected but cannot be inspected
  -> operator_result_status = not_observable

no valid operator-domain basis applies or exists
  -> operator_result_status = not_applicable

operator omitted by declared choice
  -> operator_result_status = not_selected

invalid identity/profile/policy/configuration/attribution/weights/calculation
  -> processing failure; no valid operator_result_status or result_value
```

This distinction must survive:

- storage;
- aggregation;
- visualization;
- export;
- Hangar reconstruction;
- relational processing.

## 8. Comparability Before Delta

A difference is meaningful only if the underlying evaluations are comparable.
For operator X, define an operator-specific comparability gate:

```text
G_cmp_X(r_A(k_A), r_A(k_A-1)) in {true, false}
```

The gate may require compatibility of:

- operator identity and version;
- profile identity and version;
- active component mask;
- applicability state;
- carrier and segmentation;
- detector and normalizer versions;
- measurement-basis type and identity;
- visibility conditions;
- scale and weights;
- source-local identity;
- operator-specific reference conditions.

Only if:

```text
G_cmp_X(r_A(k_A), r_A(k_A-1)) = true
```

may the implementation calculate:

```text
Delta X_A(k_A) = X_A(k_A) - X_A(k_A-1)
```

Otherwise:

```text
Delta X_A(k_A) = not_applicable
```

Time adjacency alone does not establish comparability. A chronological
transition from an event emitted by A to the next event emitted by B is not a
monadic delta.

## 9. Window Aggregation

A source-local window may be written as:

```text
W_A(K_{A,W}) = {r_A(k_A) | k_A in K_{A,W}}
```

`K_{A,W}` is the declared set of source-local positions selected for the window;
it is not the relational index `j`. Before aggregation, the implementation
constructs a profile-compatible, applicable subset:

```text
W_app_X
= {r in W_A |
   X(r) is applicable
   and r satisfies the declared X aggregation and compatibility profile}
```

The operator-specific aggregation rule is applied only to `W_app_X`. Delta or
Delta2 elements inside the aggregate are included only where their own
comparability and applicability conditions are satisfied. A valid current
operator value must not be discarded merely because no predecessor exists for
a first or second difference.

The aggregation record must preserve:

- included record IDs;
- excluded record IDs and reasons;
- aggregation profile;
- weighting rule;
- operator-profile distribution;
- scope and time range;
- entity and trajectory attribution;
- applicability rate.

A raw set of operator values, an arithmetic aggregate and a distribution are
different objects and must be named accordingly.

Every window result is a derived object with its own identity. It must not be
written back as the target event or participant state. Retain:

```text
window_result_id
window_profile_id and version
window_kind and exact boundary rule
exact member identities and ordering
included and excluded partitions with reasons
status partitions
coverage and denominator definitions
aggregator_id and version
aggregation_order
```

Name the aggregation order explicitly:

```text
derive_then_aggregate:
  derive one result from each eligible complete record,
  then aggregate the per-record results

aggregate_then_derive:
  aggregate one shared eligible set of native or complete records,
  then derive one result from the aggregate object
```

The two operations may coincide for a linear construction, but they are not
therefore the same operation. State aggregation, result aggregation, `Delta`,
`Delta2`, path length and window difference remain distinct.

The v3.51 reference policy `strict_integrity_v351` preserves every status
partition and admits only the declared valid partition to a numeric aggregate.
The future `partition_preserving_bounded_tolerance` policy (`PPWA-bounded`)
may tolerate only a separately declared bounded processing partition. It is
not a current universal default and never converts an excluded record to zero.

## 10. Hangar as a Derived Observer View

Canonical event and evaluation records remain the source of record. The
Hangar is reconstructed from those records as an Observer-side view. It is not
the primary storage location of operator state.

A Hangar view may organize records by:

- operator;
- entity;
- trajectory;
- profile;
- carrier;
- context class;
- time window;
- evaluation scope;
- applicability;
- explicitly declared grouping variables.

The Hangar may derive:

- windows and aggregates;
- distributions;
- expectation corridors;
- drift views;
- anomaly or deviation candidates;
- projections.

Every derived object must retain links to the underlying canonical event and
evaluation records. Hangar history is Observer-side historical material; it
does not become participant-visible context or an input to the original
Layer 1 value unless a separately declared future profile explicitly creates a
new evaluation with that visible material.

### 10.1 Research status of the operator-specific corridor construction

The released Hangar method permits declared, versioned corridor and anomaly
views in general. The exact operator-specific historical-set, quantile-corridor
and `d_ctx` construction below is a conditional research proposal. It
is not a released v3.51 coordinate, a required Hangar component, a canonical
default or an empirically validated detector.

If explored, it requires its own declared diagnostic profile, minimum sample
size, scaling rule, sensitivity analysis, typed failure behaviour and
provenance. Any adoption into the canonical method requires a separate
semantic, empirical and release review.

## 11. Operator-Specific Historical Expectation

An operator-specific historical expectation corridor may be explored
separately for each operator, declared entity and trajectory attribution,
operator profile and Hangar scope.
An account, project or other grouping variable may select the Hangar scope,
but it must not erase the source-attributed trajectories inside that scope.

For operator X, Entity A, profile `p_X` and Hangar scope `H_s`, a comparable
historical set may be written as:

```text
H_cmp_X,A(H_s, p_X)
= {r in H_s |
   r satisfies the declared X comparability conditions}
```

From this set, a robust expectation corridor may be derived:

```text
[Q_minus_X,A, Q_plus_X,A]
```

The quantile levels, minimum sample size, recency rule, weighting and fallback
behaviour belong to a versioned Hangar diagnostic profile.

The corridor is not inserted into the original Layer 1 formula. It does not
reopen the operator's applicability gate, change its measurement basis or
retroactively reweight the observed value.

## 12. Optional Contextual-Deviation Diagnostic

For a current applicable operator value `X_A(k_A)`, an optional separate
contextual deviation may be calculated under a declared Hangar diagnostic
profile:

```text
d_ctx_X,A(k_A | H_s, p_X)
= clip(
    max(
      Q_minus_X,A - X_A(k_A),
      0,
      X_A(k_A) - Q_plus_X,A
    )
    / s_X,A,
    0, 1
  )
```

where `s_X,A > 0` is a declared robust scaling value.

If the comparable historical set is insufficient, the corridor cannot be
established or the scale is undefined:

```text
d_ctx_X,A(k_A | H_s, p_X) = not_applicable
```

The diagnostic must not overwrite, renormalize or penalize `X_A(k_A)`:

```text
X_A(k_A) != d_ctx_X,A(k_A | H_s, p_X)
```

An optional categorical display state may later be derived:

```text
within_corridor
deviating
not_applicable
```

The canonical symbol and registry entry for such a flag remain a separate
symbol-registry decision. The numerical deviation itself is an optional
derived diagnostic, not a sixth operator and not a default component of every
Hangar point.

A deviation does not establish:

- failure;
- attack;
- hallucination;
- harmful intent;
- incorrectness;
- receiver misunderstanding.

It identifies an operator-specific difference from a declared historical
corridor that requires interpretation.

## 13. Why the Separation Matters

Consider the same clearly observable signal in two different account
histories. In Account 1, repeated references to dogs in a forest are common.
In Account 2, the same contribution has not occurred before and is unexpected.

The contribution may receive similar Layer 1 D values in both accounts because
its observable signal properties and D profile are similar. Its separate
historical contextual deviation may nevertheless be larger under the declared
Account 2 Hangar scope:

```text
d_ctx_D,A(k_A | H_Account1, p_D) < d_ctx_D,A(k_A | H_Account2, p_D)
```

This does not mean that D failed in Account 2. Signal detectability and
reconstructability answer a different question from historical expectation.

The same principle applies to the other operators:

- an I value may be locally high or low independently of its historical
  frequency;
- an S value may be structurally strong but historically unusual;
- an O value may be well grounded yet atypical for the account;
- a K value may fit the declared immediate context but deviate from a broader
  historical pattern.

Operator value and Hangar deviation must remain separately inspectable.

## 14. Detailed Human–Chatbot Record Example

Assume two stable entities:

```text
entity_A = human
entity_B = chatbot
```

The human emits:

```text
target_event_id = event_A_42
source_entity_id = entity_A
emitting_entity_id = entity_A
source_attribution_status = confirmed
trajectory_id = trajectory_A_01
trajectory_index = k_A = 15
global_event_index = n_A42
observed_at = timestamp_A42
exchange_id = exchange_09
receiver_entity_id = entity_B
```

The chatbot later emits:

```text
target_event_id = event_B_17
source_entity_id = entity_B
emitting_entity_id = entity_B
source_attribution_status = confirmed
trajectory_id = trajectory_B_01
trajectory_index = k_B = 12
global_event_index = n_B17
observed_at = timestamp_B17
exchange_id = exchange_09
reply_to_event_id = event_A_42
receiver_entity_id = entity_A
```

The two contributions share an exchange but remain separate target events.

### 14.1 Evaluation of the human contribution

For `event_A_42`:

- I uses its declared visible static reference baseline;
- S uses the active structural profile;
- D uses the active signal and detector profile;
- O uses the visible reference space only when numeric evaluation is open
  under the Source-Need Gate;
- K uses the declared admissible context scope.

### 14.2 Evaluation of the chatbot contribution

For `event_B_17`, the same operator categories are evaluated again with Entity
B's own:

- target-event identity;
- trajectory;
- profiles;
- visible reference conditions;
- applicability states.

The chatbot contribution is not appended to the human contribution as if both
formed one monadic event.

### 14.3 Handshake direction

When Entity A prepares a contribution, internal complexity must pass through a
limited observable carrier such as speech, writing, symbols, signals or
another output channel. KSODI evaluates the observable contribution, not the
unobservable internal intention.

On the receiving side, Entity B may attempt reconstruction from the available
signal, declared references and context. A later contribution by B becomes a
new target event with its own measurement bases. The exchange relation connects
the records; it does not erase their monadic identities. A reply edge or
protocol receipt flag does not prove acknowledgement, shared meaning, successful
decoding, `R0` stability or causal influence.

Here, “R0 stability” is only informal reading language. A later relational
calculation requires the stored open numeric canonical complete `R0` gate under
the exact required profile; no weaker stability label opens the branch.

## 15. Implementation Sequence

For every Layer 1 evaluation:

1. Identify exactly one target event.
2. Preserve attributed source, established emitter where known, trajectory,
   event, context and exchange identities separately.
3. Select the operator and versioned operator profile.
4. Resolve the operator-specific measurement basis.
5. Record the common operator-result status and retained reason, or record a
   processing failure when no valid operator result exists.
6. Calculate only applicable components.
7. Store the raw operator value and complete provenance.
8. Apply the operator-specific comparability gate before calculating a delta.
9. Construct window aggregations only from records admitted by the declared
   applicability and compatibility policy.
10. Reconstruct Hangar views from canonical records.
11. Calculate historical expectation or deviation only as a separate derived
    diagnostic.
12. Never overwrite the original Layer 1 value with a Hangar-derived result.
13. Perform relational calculations only through an explicit dyadic pairing or
    n-adic constellation contract and the required relational gates; require
    every downstream branch to match the admitted cardinality.

## 16. Minimum Evaluation Record

A reproducible implementation should preserve at least:

```text
evaluation_id
operator_id
operator_version
operator_result_status
result_value, only when operator_result_status = numeric
status_reason
processing_status
processing_reason, only when processing_status = failed
operator_profile_id
operator_profile_version

target_event_id
source_entity_id
emitting_entity_id
source_attribution_status
trajectory_id
trajectory_index
global_event_index
observed_at
context_event_ids
observation_object_type

exchange_id
reply_to_event_id
receiver_entity_id
role_in_exchange

measurement_basis_type
measurement_basis_id
measurement_basis_version
measurement_basis_visibility

carrier_type
segmenter_version
detector_versions
normalizer_versions
active_component_mask
component_values
component_statuses
component_status_reasons

operator_gate_status
operator_gate_reason
comparability_profile_id

created_at
observer_id
implementation_version
provenance_record_ids

profile_native_observations
normalization_profile_id and version
normalization_parameters and known_loss
raw_method_operands
raw_result_value, only when numeric
display_policy_id and version, if produced
display_value and rounding metadata, if produced
execution_fingerprint
assistive_interpretation_ref, if produced
governance_view_ref, if produced
```

If a later relational evaluation is created, its separate record additionally
preserves at least:

```text
relational_evaluation_id
relational_index = j
pairing_map = pi(j)
paired_event_ids
paired_trajectory_ids
R0_profile_id
R0_status
R0_value, only when R0_status = numeric
R0_gate_state = open | closed | not_evaluable
branch_id
branch_profile_id
branch_applicability
```

These relational fields do not turn the Layer-1 event records into a shared
monadic state.

Fields that do not apply to a particular event or operator follow the declared
field-level nullability or typed-field policy; they are not silently stored as
numerical zero and do not manufacture an operator-level `not_applicable`
result. For example, an unestablished physical emitter leaves
`emitting_entity_id` unset while `source_entity_id` and
`source_attribution_status = provisional` preserve attribution.
Where raw-language retention is restricted, approved hashes, identifiers,
derived features and provenance metadata must still preserve the declared
evaluation relationship. Reduced data, hashes, vectors and trajectories may
remain linkable, sensitive or personal data; pseudonymization must not be
reported as anonymity.

## 17. Common Implementation Errors

The following operations violate the measurement-basis discipline:

- treating an entire conversation as one target event;
- equating entity identity with trajectory identity;
- using sender or receiver as a permanent entity type;
- assigning an unknown physical emitter a confirmed entity identity instead of
  preserving provisional source attribution;
- using another entity's last event as a monadic predecessor;
- treating all available context as admissible K context;
- using hidden sources in O;
- converting missing reference material into a low O value;
- inserting contextual expectation or grounding into D;
- treating an absent detector profile as numerical zero;
- calculating deltas across incompatible profiles;
- mixing minimal and extended profile values without an explicit mapping;
- hiding electively omitted operators behind applicability masks;
- treating Hangar history as participant-visible context;
- storing the Hangar as canonical operator state;
- allowing a deviation diagnostic to modify the original operator value;
- interpreting deviation alone as failure, attack, hallucination or intent;
- inferring dyadic pairing from conversation membership or time adjacency;
- treating an optional same-trajectory predecessor diagnostic as the static I
  coordinate or combining it with static I inside `Z`;
- reporting a one-operator projection as canonical `IK`, an operator-specific
  relational comparison as `IK_rel`, or one partial relational signal as
  resonance.

## 18. Migration and Runtime-Conformance Boundary

Classify imported records as:

```text
v351_conformant
legacy_reconstructible
legacy_partially_reconstructible
legacy_noncomparable
```

`reconstruction_pending` is a workflow state, not a compatibility class.
Missing provenance must not be invented. A non-conformant historical record
may remain useful for a lower-resolution question when its limits are stated.

Publication of this reference contract and reproducible tests does not prove
independent runtime conformance. A conformant implementation must demonstrate
identity, profile/basis, typed status, raw/display, window/order, migration and
reverse-trace requirements against pinned code and profiles.

## 19. Boundary Summary

Layer 1 evaluates the current observable target event. The operator-specific
measurement basis defines how that evaluation is valid.

- A source-local sequential comparison relates compatible evaluation records.
- A window aggregation summarizes an explicitly selected applicable set.
- The Hangar derives Observer-side historical views from canonical records.
- A contextual-deviation diagnostic compares a current operator result with a
  compatible historical corridor without changing that result.
- A relational operation relates explicitly paired entities or events after
  the required gates.

These stages may use the same underlying records, but they do not calculate
the same object and must not share undeclared state.

When all listed views are selected, preserve the following dependency and
separation discipline:

```text
target event
  -> Layer 1 evaluation
  -> canonical evaluation record
       |-> comparable source-local sequence
       |     -> window or Hangar projection
       |     -> optional contextual-deviation diagnostic
       |
       +-> declared dyadic pairing or n-adic constellation map
             -> R0: open numeric canonical complete gate
                    under the exact required profile
             |-> IK_rel
             |-> staged R_geom
             +-> staged optional R_pace
```

The contextual-deviation diagnostic is optional and does not gate relational
processing. Each relational branch follows the architecture's own pairing and
requires an open numeric canonical complete `R0` gate under the exact required
profile; it also declares its own basis, profile, applicability and weights. No
branch may consume a Hangar deviation or another branch output as an undeclared
prerequisite or operator component.

The separation preserves interpretability: the operator value states what was
observed under its declared measurement basis. The Hangar states how that
observation relates to a declared historical scope. Neither statement replaces
the other.
