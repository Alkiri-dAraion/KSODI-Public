# KSODI Operator O0 - Observable Grounded Objectivity v3.50

Status: public v3.50 reference release, clarified and extended on 2026-08-25
by the jointly reviewed reader-first method, typed-result contract and
Source-Need Gate. This file is the authoritative carrier-neutral definition
of Operator O.

Layer: KSODI Standard-Eval Layer 1. A static `O0` value belongs to one
explicitly identified, source-attributed target event. Static O and all
source-local O trajectory, window and Hangar views remain strictly monadic.

Semantic applicability companion:
[`KSODI_Operator-O_Source-Need-Gate_V350.md`](./KSODI_Operator-O_Source-Need-Gate_V350.md).

Implementation companion:
[`KSODI_Operator-O_Implementation-Companion_V350.md`](./KSODI_Operator-O_Implementation-Companion_V350.md)
(public conditional guidance; method/implementation alignment reviewed
2026-08-25).

## 0. What Operator O is and what it does

Operator `O` asks one bounded grounding question:

> Given one identified target event and one declared reference space, to what
> extent is the event observably supported by and traceable to that reference
> space under the selected O profile?

O does not decide whether the reference material is universally true, complete
or valuable. It does not measure general correctness, usefulness, intelligence,
integrity, compliance, causal origin, shared understanding or human worth.

Before a numeric O value can exist, the separate O Source-Need Gate asks:

- Is reference material not expected, optional or required for this event?
- Is a declared reference space available?
- Is it visible to the evaluator?
- Is it admissible for this evaluation?
- Is the admitted reference space non-empty?

Only after those questions open the numeric path does O examine observable
grounding and traceability. A missing, invisible or inadmissible reference
space is therefore a typed applicability condition, not low grounding and not
numeric zero.

### 0.1 Minimal practical reading

> Can observable parts of this one target event be connected to the declared
> reference material admitted for exactly this evaluation?

A high applicable value means that the selected O profile finds strong visible
support or traceability. A low applicable value means that the admitted
reference space offers weak observable support under that profile. A
non-numeric state means that the grounding question could not validly be
calculated; it does not mean that grounding was calculated and found absent.

### 0.2 How to read this file

- New readers may begin with Sections 0-2, the interpretation in Section 4 and
  the relational boundary in Section 8.
- Method reviewers should follow the complete semantic and mathematical path
  through Sections 2-9.
- Implementers must also read the Source-Need Gate and the separate
  implementation companion named in Section 10.

The order is deliberate: observable question, two bounded examples, identity
and topology, basis and applicability, calculation, movement, pattern and only
then the relational boundary.

## 1. Bounded Application Examples

The examples map two domains onto the same canonical question. They are
explanatory instantiations, not competing definitions, automatic domain
translations or empirical validation.

### 1.1 Human-Chatbot Interaction

Assume two stable entities:

```text
entity_A = human
entity_B = chatbot
target_event = one source-attributed contribution e_A(k_A)
interaction_scope = one declared conversation or exchange
trajectory_A and trajectory_B remain distinguishable
```

For one chatbot contribution, a declared reference space may contain admitted
documents, retrieval results, visible tool outputs, web material, policies or
conversation elements. The Source-Need Gate first determines whether such
material is expected and usable for this target event. If the gate opens, a
declared O profile may examine support relations, attribution traces or other
profile-valid grounding evidence.

The human contribution and chatbot contribution receive separate O
evaluations. Material from one contribution may be admitted to the other's
reference space where the profile permits it, but it does not become part of
the other target event or merge the two trajectories.

A well-grounded response can be terse or inelegant. An articulate response can
remain weakly grounded. Neither result proves usefulness, truth, intent,
agreement or successful communication.

The conditional Conversation-/RAG-oriented formulas belong in the separate
implementation companion. They instantiate this method; they do not define O
for every carrier.

### 1.2 Unknown Morse-Like Signal

An Observer detects repeated marks and gaps from a provisionally attributed
observed source `U`:

```text
entity_or_observed_source = U
target_event = one source-attributed signal unit e_U(k_U)
observation_unit = one declared pulse, sign group or transmission segment
reference_space = admitted codebooks, known signal patterns or documented
                  transmission conventions
trajectory_U remains distinguishable from every receiving or replying entity
```

If the selected policy does not expect a reference for the initial detection,
numeric O is `not_applicable`; I and D may still observe the impulse and its
discernibility. If a codebook or comparison corpus is required but missing,
invisible or inadmissible, numeric O also remains closed. If a non-empty,
evaluator-visible and admissible reference space exists, a domain-specific O
profile may evaluate how strongly the target signal is traceable to it.

A close match to a codebook can support grounding relative to that codebook.
It does not prove who emitted the signal, what was intended, whether anyone
received it, whether a later signal is an acknowledgement or whether the
entities are coupled. Those claims require different evidence and, where
relational, later gated constructs.

This example requires a declared signal segmentation rule, reference-admission
policy, trace relation and detector profile. KSODI does not automatically
decode an unknown convention.

## 2. Canonical Definition, Scope and Boundaries

For one source or entity `A`, one target event `e_A(k_A)`, one declared
reference space `Ref_A(k_A)` and one versioned O profile `p_O`:

```text
O0_A(k_A | Ref_A(k_A), p_O)
= profile-defined observable grounding and traceability
  of e_A(k_A) relative to Ref_A(k_A)
```

When applicable:

```text
O0_A(k_A | Ref_A(k_A), p_O) in [0,1]
```

Otherwise O produces a typed non-numeric state.

The carrier-neutral semantic core is:

1. identify one target event and its attributed source trajectory;
2. declare why reference material is or is not needed;
3. admit one visible, non-empty reference space under a versioned policy;
4. apply one versioned O profile that defines observable grounding and
   traceability relations;
5. retain value, applicability and provenance with the target event.

O0 does not measure:

- universal truth or general factual correctness;
- the intrinsic quality of the reference space;
- context completeness, structural order, signal clarity or information
  impulse;
- hidden intention, private internal state or causal origin;
- mutual understanding, coupling, resonance or relational quality;
- general human or system worth.

The five KSODI base operators are semantically distinct and functionally
non-redundant. They are not claimed to be mathematically orthogonal or
statistically independent.

### 2.1 Atomic Evaluation Unit and Identity

```text
target_event_id = event_A_42
source_entity_id = entity_A
source_attribution_status = confirmed
emitting_entity_id = entity_A, if established
trajectory_id = trajectory_A_01
trajectory_index = k_A
context_event_ids = [visible_context_ids]
reference_space_id = ref_A_42
source_need_policy_id = p_G_O_id
operator_profile_id = p_O_id
```

The target event, visible context, emitting or provisionally attributed source,
trajectory and admitted reference elements remain distinct objects.

Entity `B` is not required to calculate `O0_A(k_A)`. B may be an interaction
partner, receiver, later sender or provider of visible reference material
without becoming part of A's target identity.

Exactly one declared numeric O profile may fill the O coordinate of one
concrete five-dimensional `Z_A(k_A)` view. Alternative profiles remain
separately named and recoverable.

#### 2.1.1 Canonical Index Discipline

```text
n    = global event index in the declared observable event stream
k_A  = local position inside trajectory A
k_B  = local position inside trajectory B
j    = later relational exchange or paired-evaluation index

pi(j) = (k_A(j), k_B(j))
```

In this file, `k_A - 1` always denotes A's preceding comparable trajectory
position. It never silently selects the preceding global event or an event
from B. The symbol `t` may be used only as an explicitly declared timestamp
or mapped implementation step.

### 2.2 Static and Source-Local O Views Are Strictly Monadic

```text
O0_A(k_A | Ref_A(k_A), p_O_A)
O0_B(k_B | Ref_B(k_B), p_O_B)
```

Each value remains attached to its own target event, source identity,
trajectory, reference-space provenance and profile. A shared room, task,
conversation, timestamp, exchange, environment or document does not merge the
values and does not create a dyadic O value.

Visible material from outside trajectory A may enter `Ref_A(k_A)` when the
selected policy permits it. The resulting O value still belongs to
`e_A(k_A)`.

### 2.3 Semantic Distinctness and Symbol Discipline

| Coordinate | O boundary |
| --- | --- |
| `K` | K observes declared context availability and completeness. O evaluates support and traceability relative to an admitted reference space where a source need exists. K does not open or close O numerically. |
| `S` | S observes structural coherence, segmentation, boundaries and order. A citation marker may support both structure and attribution, but profiles must expose and control that overlap. |
| `D` | D observes discernibility and reconstruction support. A clear signal may remain ungrounded; a grounded event may remain hard to reconstruct. |
| `I` | I observes information impulse relative to its basis. A repeated event may carry low I while remaining strongly grounded, or high I while its source remains unresolved. |

The O reference space and an I baseline may contain some of the same visible
material. Admission to one does not imply admission to the other.

Use `Ref` for reference-space notation. Reserve `R0`, `R_geom`,
`R_pace` and other R-prefixed names for relational or R-family constructs.

### 2.4 Coordinate Order and Directed Process Topologies

```text
Z_A(k_A) = (K_A, S_A, O_A, D_A, I_A)
```

This is a coordinate order, not a causal formula chain.

```text
sender-side formation:        K -> S -> O -> D -> I
receiver-side reconstruction: I -> D -> O -> S -> K
```

In sender-side formation, O marks grounding or reference support before
material is adapted to an observable carrier. In receiver-side reconstruction,
O asks whether the already noticed and sufficiently distinguishable target can
be checked against visible admissible references.

These paths do not make numeric K, S, D or I inputs to the static O formula.
They do not claim access to hidden cognition or machine processing. With an
unknown convention, failed grounding may recursively reopen segmentation,
structural hypotheses, source checking and context.

## 3. Measurement Basis, Profiles and Applicability

### 3.1 Declared O Measurement Basis

The O measurement basis identifies:

- the source-attributed target event;
- the event-bound Source-Need Gate record and policy;
- the declared reference space, its version and admitted elements;
- evaluator visibility and admissibility;
- the profile-defined grounding or trace relation;
- valid observation units;
- component definitions, detector and normalization rules;
- component mask, weights or combination rule;
- applicability, missingness and comparability policy.

It must not silently include another entity's state, undeclared history, hidden
sources or model state, presumed truth of the reference space, Hangar
expectation, inferred intention or another operator's basis.

### 3.2 Versioned O Profile

```text
p_O = (
  reference_selection,
  target_unit,
  trace_relation,
  component_definitions,
  detector_and_representation,
  normalization,
  active_component_mask,
  weights_or_combination_rule,
  applicability_and_missingness,
  version
)
```

The canonical method imposes no universal carrier, detector, embedding,
citation rule or numeric component family. A valid concrete profile must define
all constitutive choices well enough to reproduce its O value.

### 3.3 Applicability Before Numeric Interpretation

```text
app_O,A(k_A)
:= reference_space_need in {optional, required}
   and reference_space_available = true
   and reference_space_visible_to_evaluator = true
   and reference_space_admissible_for_evaluation = true
   and Ref_A(k_A) != empty
   and all mandatory inputs of p_O are applicable

Source-Need result mapping:
  required basis unavailable, not visible or evidence-undetermined
    -> operator_result_status = not_observable
  basis not expected, optional absent, inadmissible or admitted empty
    -> operator_result_status = not_applicable
  O coordinate not selected
    -> operator_result_status = not_selected
  invalid identity/policy/profile or calculation failure
    -> processing failure; no valid operator result
```

If a valid gate reaches a common non-numeric terminal state:

```text
O0_A(k_A | Ref_A(k_A), p_O)
= not_observable or not_applicable according to the retained gate reason
```

At the common Layer-1 operator boundary, preserve:

```text
not_selected != not_observable != not_applicable != 0
```

The common external Layer-1 result is:

```text
operator_result_status in {
  numeric,
  not_selected,
  not_observable,
  not_applicable
}
```

The Source-Need Gate maps a required but unavailable reference basis,
evaluator invisibility and evidence-dependent undetermined gate conditions to
`not_observable`. It maps a reference basis that is not expected, an absent
optional basis, an inadmissible basis or an empty admitted basis to
`not_applicable`. The gate retains the exact controlled reason. `not_selected`
is emitted only when the O coordinate or an optional O view was not selected
by the declared profile.

Malformed identity, an invalid source-need policy, an invalid O profile or a
calculation failure is a processing failure and produces no valid operator
result. It must not be converted to another Z status merely to complete a
record. The complete gate state model and ordered decisions are defined in the
Source-Need Gate companion.

### 3.4 K Does Not Control O Applicability

K may separately observe context visibility or completeness. It is not the O
Source-Need Gate. `K_A(k_A)=0` does not canonically mean that no O reference
material exists. Conversely, visible context does not automatically become an
admissible O reference space.

## 4. Static Construction and Interpretation

### 4.1 Why the Mathematical Contract Matters

The mathematical form does not create the semantic boundary. The semantic
boundary creates the valid formula.

Every valid O profile preserves target-event and source identity, one declared
visible non-empty admissible reference space, an open Source-Need Gate, one
versioned profile and component mask, explicit component applicability, no
cross-entity subtraction and no conversion of missingness to zero.

### 4.2 Profile-Defined Components

```text
C_O,A(k_A | Ref_A(k_A), p_O)
= {c_O,1,A(k_A), ..., c_O,q,A(k_A)}
```

Each component declares its narrow grounding question, observable target and
reference inputs, range, detector or calculation rule, applicability,
profile/version dependencies and collision boundaries with K, S, D and I.

The profile also declares which components are mandatory, which optional
components may be selected and whether renormalization is permitted. A changed
active component set is a profile or comparability event.

### 4.3 Static Profile Rule

```text
if app_O,A(k_A) = true
   and the selected profile's mandatory components are applicable
   and its declared combination rule is defined:

  O0_A(k_A | Ref_A(k_A), p_O)
  = clip(
      F_p_O(C_O,A(k_A | Ref_A(k_A), p_O)),
      0,
      1
    )
  operator_result_status = numeric
  result_value = O0_A(k_A | Ref_A(k_A), p_O)

otherwise:
  retain the mapped common non-numeric result and its controlled reason,
  or record a processing failure when no valid operator result exists
```

`F_p_O` is the complete, versioned combination rule carried by the selected
O profile, not an unspecified universal algorithm. This allows different
carriers to instantiate grounding without pretending that embeddings,
codebooks or fictional canon use one detector.

Exactly one declared profile supplies the O coordinate of one concrete Z view:

```text
O_A(k_A) := O0_A(k_A | Ref_A(k_A), p_O)
```

The alias preserves the complete O profile, gate state, reference-space identity,
component record and provenance. It only names the selected static result at the
Layer-1-to-Z boundary.

### 4.4 Interpretation

| Value or state | Bounded O interpretation |
| --- | --- |
| high | strong observable support and traceability relative to the admitted reference space under the selected profile |
| medium | partial observable support or traceability |
| low | weak observable support or traceability despite an open applicability gate |
| `not_applicable` | the grounding question is not expected or no admissible non-empty basis exists under the declared profile |
| `not_observable` | required observable support cannot be inspected; gate reason may be `not_visible_to_evaluator` |
| `not_selected` | an optional profile or diagnostic was not selected |

Numeric thresholds are profile-bound. A low value is diagnostic, not a final
verdict; it may reflect weak support, an unsuitable admitted reference space,
material outside that space or detector failure.

## 5. Edge Cases, Fairness, Privacy and Retention

- Reference not expected, optional-but-absent or required-but-missing never
  produces O=0; the first two map to `not_applicable`, while a required but
  unavailable basis maps to `not_observable`.
- A visible but inadmissible or empty admitted reference space cannot open O.
- A non-empty raw retrieval result may yield an empty admitted reference set.
- A target can be strongly grounded relative to a weak reference space. O does
  not validate that space's intrinsic quality.
- Fictional canon can be valid when explicitly admitted; O then measures
  internal grounding, not external-world factuality.
- Profile or reference-construction change is not ordinary O movement.

A low or non-numeric result may reflect evaluator access, source restrictions,
reference policy, detector, carrier, accessibility or provenance rather than a
property of the attributed source.

Raw and derived target, source, retrieval, embedding, identifier, score, delta
and Hangar data may remain sensitive or personal. Derived does not mean
anonymous. Retention and access require a declared governance basis.

## 6. Comparability and Source-Local Dynamics

### 6.1 Comparability Contract

Two O values are comparable only under equal or explicitly compatible:

- target-unit and source-attribution rules;
- O profile and Source-Need Gate policy;
- active component mask, weights and combination rule;
- reference-space construction, inclusion, version and visibility;
- detector, representation, segmentation and normalization;
- applicability and missingness policy;
- Observer/operator version and selected aggregation policy.

```text
G_cmp_O,A(k_A)
= comparable(r_O,A(k_A), r_O,A(k_A - 1))
```

If compatibility is not established, the difference is `not_applicable`.
Profile or reference-policy change is a comparison boundary.

### 6.2 Source-Local Dynamics

```text
if G_cmp_O,A(k_A) = true:
  Delta O_A(k_A) = O_A(k_A) - O_A(k_A - 1)
otherwise:
  Delta O_A(k_A) = not_applicable
```

```text
if three consecutive O records are applicable and comparable:
  Delta2 O_A(k_A)
  = Delta O_A(k_A) - Delta O_A(k_A - 1)
otherwise:
  Delta2 O_A(k_A) = not_applicable
```

Delta O may reflect target movement, admitted-reference movement, detector
response or several together. It does not establish that the attributed
source alone became better or worse grounded.

An optional non-negative rise diagnostic may be selected:

```text
if G_cmp_O,A(k_A) = true:
  Rise_O,A(k_A) = max(0, Delta O_A(k_A))
otherwise:
  Rise_O,A(k_A) = not_applicable
```

`Rise_O` preserves only the positive part of an applicable O difference. It
does not attribute the rise causally to the attributed source or to an emitter
whose identity may or may not be established. The earlier
private symbol `B_O` maps to `Rise_O`; the descriptive name avoids collision
with stable Entity B and the former RAG trace component `B`.

### 6.3 Separate Reference-Space Diagnostics

```text
RefDrift_O,A(k_A)
= versioned profile-defined change between comparable
  Ref_A(k_A - 1) and Ref_A(k_A)

P_ref,A(W_A)
= versioned source-local reference-space stability diagnostic
```

These remain separate and do not modify, penalize or reweight O0. A
vector-compatible cosine instantiation belongs in the implementation companion.

## 7. Sigma and Sigma(Hangar)

```text
W_app_O,A
= {k_A in W_A | O0_A(k_A) is applicable}

W_app_DeltaO,A
= {k_A in W_A | Delta O_A(k_A) is applicable and comparable}

W_app_Delta2O,A
= {k_A in W_A | Delta2 O_A(k_A) is applicable and comparable}
```

```text
O_A Sigma(W_A)
= {
    static_O:
      Agg_O({O_A(k_A) | k_A in W_app_O,A}),
    delta_O:
      Agg_DeltaO({Delta O_A(k_A) | k_A in W_app_DeltaO,A}),
    delta2_O:
      Agg_Delta2O({Delta2 O_A(k_A) | k_A in W_app_Delta2O,A})
  }
```

```text
O_A Sigma(Hangar)
= {
    static_O_distribution:
      distribution_view({O_A(k_A) | k_A in W_app_O,A}),
    delta_O_distribution:
      distribution_view({Delta O_A(k_A) | k_A in W_app_DeltaO,A}),
    delta2_O_distribution:
      distribution_view({Delta2 O_A(k_A) | k_A in W_app_Delta2O,A})
  }
```

Each empty field is `not_applicable`; if all selected sets are empty, the
complete view is `not_applicable`.

Where the selected static aggregation profile includes elementary summaries
and `|W_app_O,A| > 0`:

```text
Obar_A(W_A) = mean({O0_A(k_A) | k_A in W_app_O,A})
Omin_A(W_A) = min({O0_A(k_A) | k_A in W_app_O,A})
Ovar_A(W_A) = var({O0_A(k_A) | k_A in W_app_O,A})
```

These summarize applicable static O values only. They do not mix static,
Delta and Delta2 types. If the applicable static subset is empty, all three
are `not_applicable`. The aggregation profile must declare whether `var`
denotes population or sample variance and its minimum sample count; a
single-value sample variance must not be invented as zero.

```text
if |W_A| > 0:
  applicability_rate_O,A(W_A) = |W_app_O,A| / |W_A|
otherwise:
  applicability_rate_O,A(W_A) = not_applicable
```

Sigma(W) is typed source-local aggregation. Sigma(Hangar) is a derived
attributable distribution view. Side-by-side A/B display is not dyadic O.

## 8. Relational Boundary

O0, Delta O, Delta2 O, O Sigma(W) and O Sigma(Hangar) remain monadic.
Relational comparison requires distinguishable trajectories, explicit pairing
or constellation, compatible profiles, an open numeric canonical complete R0
gate under the exact required profile and a separately declared later-layer
construct.

Operator O does not define coupling, resonance, mutual understanding or
relational quality. A proposed post-R0 O comparison and any O-only route that
bypasses complete Z remain v3.60 Future Work and are not canonical IK_rel or an
R-family result.

## 9. Formal Summary and Variable Reference

### 9.1 Compact Formula Block

```text
app_O,A(k_A)
:= reference_space_need in {optional, required}
   and reference_space_available = true
   and reference_space_visible_to_evaluator = true
   and reference_space_admissible_for_evaluation = true
   and Ref_A(k_A) != empty
   and all mandatory inputs of p_O are applicable

C_O,A(k_A | Ref_A(k_A), p_O)
= {c_O,1,A(k_A), ..., c_O,q,A(k_A)}

if app_O,A(k_A) and mandatory components apply and F_p_O is defined:
  O0_A(k_A | Ref_A(k_A), p_O)
  = clip(F_p_O(C_O,A(k_A | Ref_A(k_A), p_O)), 0, 1)
  operator_result_status = numeric
  result_value = O0_A(k_A | Ref_A(k_A), p_O)
otherwise:
  retain the mapped common non-numeric result and controlled reason,
  or the separate processing failure when no valid result exists

# selected static handoff to Layer 2
O_A(k_A) := O0_A(k_A | Ref_A(k_A), p_O)

if G_cmp_O,A(k_A):
  Delta O_A(k_A) = O_A(k_A) - O_A(k_A - 1)
otherwise:
  Delta O_A(k_A) = not_applicable

if three consecutive O records are applicable and comparable:
  Delta2 O_A(k_A) = Delta O_A(k_A) - Delta O_A(k_A - 1)
otherwise:
  Delta2 O_A(k_A) = not_applicable

W_app_O,A = {k_A in W_A | O_A(k_A) is applicable}
W_app_DeltaO,A = {k_A in W_A | Delta O_A(k_A) is applicable and comparable}
W_app_Delta2O,A = {k_A in W_A | Delta2 O_A(k_A) is applicable and comparable}

O_A Sigma(W_A)
= {
    static_O: Agg_O({O_A(k_A) | k_A in W_app_O,A}),
    delta_O: Agg_DeltaO({Delta O_A(k_A) | k_A in W_app_DeltaO,A}),
    delta2_O: Agg_Delta2O({Delta2 O_A(k_A) | k_A in W_app_Delta2O,A})
  }

O_A Sigma(Hangar)
= {
    static_O_distribution:
      distribution_view({O_A(k_A) | k_A in W_app_O,A}),
    delta_O_distribution:
      distribution_view({Delta O_A(k_A) | k_A in W_app_DeltaO,A}),
    delta2_O_distribution:
      distribution_view({Delta2 O_A(k_A) | k_A in W_app_Delta2O,A})
  }

Separate diagnostics, never canonical O:
RefDrift_O,A(k_A)
P_ref,A(W_A)
Rise_O,A(k_A) = max(0, Delta O_A(k_A)) where comparable
```

### 9.2 Variable Reference

| Variable | Semantic role |
| --- | --- |
| `n` | Global event index |
| `k_A` / `k_B` | Source-local trajectory positions |
| `j` / `pi(j)` | Later relational index and explicit pairing map |
| `e_A(k_A)` | One source-attributed target event |
| `Ref_A(k_A)` | Declared non-empty visible admissible reference space |
| `p_O` | Complete versioned O profile |
| `app_O,A(k_A)` | Numeric O applicability gate |
| `C_O,A` / `c_O,r,A` | Profile-defined O component record / component |
| `F_p_O` | Complete combination rule declared by `p_O` |
| `operator_result_status` | Common Layer-1 result: numeric, not selected, not observable or not applicable |
| `result_value` | Numeric O value in `[0,1]`; present only when the result status is numeric |
| `O0_A(k_A)` | Profile-bound static O result |
| `O_A(k_A)` | Selected static O coordinate value handed to Z |
| `r_O,A(k_A)` | Complete attributable O evaluation record |
| `G_cmp_O,A(k_A)` | Comparability gate |
| `Delta O_A(k_A)` / `Delta2 O_A(k_A)` | Source-local movement / acceleration |
| `W_A` | Declared source-local window |
| `W_app_O,A` | Applicable static-O positions |
| `W_app_DeltaO,A` / `W_app_Delta2O,A` | Applicable comparable movement positions |
| `O_A Sigma(W_A)` | Typed source-local aggregation |
| `O_A Sigma(Hangar)` | Typed attributable distribution |
| `RefDrift_O,A` / `P_ref,A` | Separate reference-space diagnostics |
| `Rise_O,A(k_A)` | Optional non-negative part of an applicable O difference; not causal attribution |
| `not_applicable` | Grounding question not expected or no valid admissible basis exists; never numeric zero |
| `not_observable` | Required observable support is unavailable; retain the specific gate reason |
| `not_selected` | Optional profile or diagnostic was not selected |

## 10. Separate Implementation Companion

The canonical method ends with Section 9. Conversation/RAG formulas,
embeddings, citation detectors, unsupported-claim logic, storage fields,
pseudocode, reference-element diagnostics, tests and architecture mappings
belong in the adjacent implementation companion.

- Semantic gate: [O Source-Need Gate](./KSODI_Operator-O_Source-Need-Gate_V350.md).
- Public implementation companion:
  [Operator O Implementation Companion](./KSODI_Operator-O_Implementation-Companion_V350.md)
  (conditional and subordinate).
- Alignment: method, gate and implementation review passed with the typed
  Layer-1-to-Z and complete-Z-to-IK downstream contract on 2026-08-25.

The companions may operationalize or gate O but must not redefine its question,
basis, source identity, applicability, static profile rule or relational
boundary. Any mismatch remains visible until reviewed.
