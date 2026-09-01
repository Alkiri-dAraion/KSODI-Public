# KSODI Operator K0 - Observable Context Completeness v3.50

This file is the authoritative carrier-neutral definition of Operator K.

Layer: KSODI Standard-Eval Layer 1. One static `K0` value belongs to one
explicitly identified, source-attributed target event under one declared and
versioned K profile. A context scope may contain many separately identified
objects and sources; that multiplicity does not make K dyadic or n-adic.

Implementation companion:
[`KSODI_Operator-K_Implementation-Companion_V350.md`](./KSODI_Operator-K_Implementation-Companion_V350.md)
(public conditional guidance subordinate to this method definition).

## 0. What Operator K is and what it does

`K` answers one narrow observable question:

> To what extent are the context requirements declared for this target-event
> evaluation observably fulfilled inside its admissible context scope and
> under its declared availability relation?

K evaluates observable context provisioning. It asks whether the context
objects or features expected by a versioned profile are demonstrably present,
accessible and sufficiently complete for the relation that profile names.

The availability relation matters. An object may be:

- visible to the evaluator;
- available to an emitting human, model or process;
- available only to a receiver or later evaluation stage;
- stored somewhere but not admitted into the target event's context.

These states are not interchangeable. A file in a repository, a tool listed in
an interface or a passage returned by retrieval must not be counted as target
context unless the selected profile can observe the required availability
relation.

K does not establish:

- correctness, truth or evidence quality;
- grounding or traceability of the target contribution;
- compliance of the target with the supplied context;
- structural coherence, clarity or information impulse;
- hidden memory, hidden state, intention or understanding;
- relational agreement, resonance or coupling;
- intelligence, competence or human value.

### 0.1 Minimal Practical Reading

For a reader who does not want to begin with the formula:

- First declare what context is expected for this one target event.
- Declare whose or which access relation is being observed.
- Count only context whose required presence or availability is observable
  under that profile.
- An expected and observably absent requirement contributes numeric `0`.
- An expected but unobservable availability relation makes complete K
  `not_observable`, not zero.
- A context feature that was never expected does not count as missing.
- A partial visible-context summary remains a separately labelled diagnostic;
  it cannot silently become complete K.

High K means that the profile-declared context requirements are strongly
fulfilled. Low K means that the complete question is observable but expected
requirements are absent or only partly fulfilled. Neither result states that
the context is correct, suitable or successfully used.

### 0.2 How to Read This File

New readers may begin with Sections 0-2, the interpretation in Section 4.5 and
the relational boundary in Section 8. Method reviewers should follow the full
path: examples, identity and indices, context scope, availability relation,
profile, applicability, static calculation, comparability, movement and typed
aggregation.

The reader order is deliberate. Concrete prompt fields, marker lists,
containers, pseudocode and detector configurations remain in the separate
implementation companion.

## 1. Bounded Application Examples

Both examples instantiate the same K question. They do not establish domain
equivalence, empirical validation or a universal context taxonomy.

### 1.1 Human-Chatbot Interaction

```text
entity_A             = human
entity_B             = chatbot
target_event_B       = one source-attributed chatbot contribution
trajectory_B         = chatbot contribution trajectory
availability_relation = context demonstrably admitted to the chatbot event
context_scope_B      = separately identified admitted context objects
K_profile            = declared conversational-task context profile
```

The profile may expect a task goal, constraints, an output form, admitted
assets and declared tool availability. K evaluates whether those expected
context requirements were observably available for the chatbot target event.

A file visible to the human but not demonstrably admitted to the chatbot event
does not satisfy the chatbot-access requirement. A retrieved passage admitted
to the event may satisfy a K availability requirement while still being poor
evidence; its grounding role belongs to O. Whether the response follows the
requested format belongs to S or another explicitly declared compliance
diagnostic, not K.

The human contribution has its own `K_A(k_A)` and context scope. Shared
conversation history does not merge the two K values.

### 1.2 Unknown Morse-Like Signal

```text
entity_A             = stable or explicitly provisional observed signal source
target_event_A       = one bounded source-attributed pulse burst
availability_relation = context visible to the evaluator for this evaluation
context_scope_A      = calibration, observation-window and admitted prior data
K_profile            = declared unknown-signal evaluation-context profile
meaning               = unknown
```

The profile may expect a sampling calibration, pulse-duration convention,
observation window or admitted prior bursts. K can evaluate whether those
context requirements are visibly available to the evaluator. It does not claim
that the unknown source possessed the same context.

A missing codebook may lower K only if the profile declared a codebook as an
expected requirement. The pulse burst may still have high S because its pattern
is orderly, or high D because it is distinct, while K remains low. No result
proves meaning, a confirmed emitter identity or acknowledgement.

If the evaluator cannot determine whether an expected context object was
available under the selected relation, complete K is `not_observable`. An
explicitly named partial observable diagnostic may remain available, but it is
not the K coordinate of a complete Z view.

## 2. Canonical Definition, Scope and Boundaries

`K0_A(k_A | scope_A(k_A), p_K)` evaluates observable context completeness for
one target event `e_A(k_A)` attributed to one stable or explicitly provisional
source A.

Carrier-neutral semantic core:

> Context completeness is the degree to which the non-empty set of context
> requirements declared for one target-event evaluation is observably
> fulfilled inside its admissible context scope under one explicit availability
> relation.

The context scope may contain objects produced by many entities, systems or
tools. Those objects remain separately attributable. K's output is still one
monadic value attached to the target event whose context provisioning is being
evaluated.

Static K does not evaluate change in context across events. Scope drift,
uncertainty, recurrence or update patterns are separate source-local
diagnostics after their own basis and comparability conditions are satisfied.

### 2.1 Atomic Evaluation Unit and Identity

The canonical K evaluation contains or recoverably references:

```text
target_event_id
source_entity_id
emitting_entity_id, if established
source_attribution_status
trajectory_id
global_event_index n
local_trajectory_index k_A
context_object_ids
scope_id
availability_relation_id
observer_vantage_id
evaluation_scope
k_profile_id and version
applicability state
```

Target event, context objects, emitting identity, evaluator vantage and
availability relation remain distinct. Context from another entity may be
admitted without becoming part of A's emitting identity or trajectory.

Sender and receiver are exchange-relative roles. An entity may be sender in
one exchange and receiver in another without changing its stable identity.

The canonical cross-layer identity boundary is summarized in the
[`KSODI Architecture v3.50`](../../KSODI-Architecture_V350.md); this method
retains the K-specific required fields explicitly above.

#### 2.1.1 Canonical Index Discipline

```text
n   = global event index in the observable event stream
k_A = local position inside trajectory A
k_B = local position inside trajectory B
j   = declared relational exchange or paired-evaluation index

pi(j) = (k_A(j), k_B(j))
```

Static K uses the local index of its own target event. `j` and `pi(j)` are not
static K inputs. A timestamp `t` may be stored only with an explicit mapping;
it must not silently imply synchronized local positions or a shared predecessor
across entities.

### 2.2 Static and Source-Local K Views Are Strictly Monadic

```text
K_A(k_A | scope_A(k_A), p_K,A(k_A))
K_B(k_B | scope_B(k_B), p_K,B(k_B))
```

remain separate even where their scopes contain shared objects. Equal profile
names, rooms, tasks, times or interfaces do not create one combined K value.

Removing Entity B does not invalidate the K construction for A whenever A's
own target identity, declared scope and applicability conditions remain
satisfied. If a B-attributed object was an expected part of A's context, its
removal may legitimately change A's observed context completeness; this is an
external context dependency, not a dyadic K formula.

### 2.3 Semantic Distinctness and Symbol Discipline

| Coordinate | Narrow observable question | Boundary to K0 |
| --- | --- | --- |
| `S0` | How are the target's observable parts organized? | the presence of a format instruction is K; the target's resulting organization is S |
| `O0` | Is the target grounded and traceable in a visible admissible reference space? | K observes whether an expected reference object is available; O evaluates grounding relative to it |
| `D0` | Does the carrier support observable discrimination and reconstruction? | context provisioning is not signal discernibility |
| `I0` | What observable information impulse exists relative to a declared basis? | context availability is not information difference or novelty |

Important distinctions:

```text
stored is not admitted
evaluator-visible is not emitter-accessible
available is not suitable
context presence is not context use
context completeness is not grounding
```

`scope` denotes the admissible K context container. `Ref` denotes a declared
reference space for an operator such as O or I and is not a synonym for K
scope. `R`-prefixed symbols remain reserved for the relational and resonance
family.

### 2.4 Coordinate Order and Directed Process Topologies

```text
Z_A(k_A) = (K_A, S_A, O_A, D_A, I_A)
```

This is coordinate order, not a causal calculation chain.

```text
sender-side formation:        K -> S -> O -> D -> I
receiver-side reconstruction: I -> D -> O -> S -> K
```

In sender-side formation, available context constrains or supports what may be
formed. In receiver-side reconstruction, context may be established only after
an event has been noticed, distinguished, provisionally grounded and
structurally organized. Unknown conventions may reopen earlier hypotheses
recursively.

These paths do not make numeric S, O, D or I values inputs to static K. They do
not claim that a human or machine internally processes the coordinates in this
order.

## 3. Measurement Basis, Profiles and Applicability

### 3.1 Declared K Measurement Basis

Before calculation, declare:

- the source-attributed target event;
- the admissible context scope and its construction policy;
- every context object admitted to that scope;
- the non-empty expected context-requirement set;
- the availability relation being evaluated;
- evaluator vantage and visibility boundary;
- detector and requirement-fulfillment rules;
- binary or graded value profile;
- component-attribution and overlap policy;
- weights, missingness and applicability rules;
- interpretation and provenance requirements.

Undeclared history, hidden memory, all repository files, all possible tools,
another entity's private state, Hangar expectations or later relational results
are not admitted merely because they exist somewhere.

### 3.2 Admissible Context Scope and Availability Relation

```text
scope_A(k_A)
= {o_l |
     context object o_l is identified and admissible under p_K
     and evidence for the selected availability relation is observable
       from the declared evaluator vantage}
```

This does not require the evaluator to inspect unrestricted object content in
every profile. A governed manifest, admission record or other declared access
evidence may establish the selected availability relation while payload
visibility remains separately controlled. Object identity, content
visibility, admissibility, availability relation and relation evidence remain
distinct.

The profile declares which relation is being observed. Examples include:

```text
target_access      = observable evidence that o_l was available to the
                     emitting process for target event e_A(k_A)
evaluation_access  = o_l was available to the evaluator for this evaluation
receiver_access    = o_l was available to a declared receiving process
```

These are alternative profile meanings and are not naively comparable. If the
required relation cannot be observed, the affected requirement is
`not_observable`; mere storage or interface visibility does not substitute for
the missing access evidence.

### 3.3 Versioned K Profile

```text
p_K = (
  profile_id,
  profile_version,
  target_unit_profile,
  scope_construction_policy,
  context_object_admission_policy,
  expected_requirement_profile,
  availability_relation_profile,
  observer_vantage_profile,
  detector_profile,
  fulfillment_profile,
  binary_or_graded_profile,
  component_attribution_policy,
  weight_profile,
  applicability_policy,
  interpretation_profile
)
```

Every constitutive choice must be recoverable. A changed scope, expected set,
availability relation, observer vantage, detector, fulfillment rule, value
type, attribution policy, weights or applicability rule may create a new
profile and therefore a comparability boundary.

Exactly one declared K profile fills K in a given five-dimensional Z view.
Unweighted and weighted profiles, target-access and evaluator-access profiles,
or binary and graded profiles remain separate results.

### 3.4 Applicability Before Numeric Interpretation

At minimum, preserve these internal K-gate states:

```text
open           = the complete selected K basis is observable and applicable
not_selected   = K was not requested under the evaluation profile
not_observable = an expected requirement or required availability relation
                 cannot be inspected from the declared vantage
not_applicable = K was selected, but no valid non-empty expected basis applies
```

The common external Layer-1 result handed to Z is:

```text
operator_result_status in {
  numeric,
  not_selected,
  not_observable,
  not_applicable
}
```

`open` remains an internal gate state. A successfully open, applicable and
finite K calculation emits `operator_result_status = numeric` with
`result_value in [0,1]`. Numeric `0` means complete K applies and all expected
requirements observably fail.

Therefore:

```text
not_selected != not_observable
not_observable != not_applicable
not_applicable != 0
```

The K applicability gate is typed:

```text
G_K,A(k_A | p_K)
in {open, not_selected, not_observable, not_applicable}

# common external result handed to Z
operator_result_status
in {numeric, not_selected, not_observable, not_applicable}
```

Numeric K opens only when:

1. target, source and trajectory identity are resolved;
2. scope, availability relation and evaluator vantage are declared;
3. the expected requirement set is non-empty;
4. every expected requirement has a numeric observable fulfillment value;
5. component attribution and overlap rules are valid;
6. the selected formula has a positive denominator.

The gate is not multiplied into K. A closed or typed non-numeric gate never
turns unavailable measurement conditions into numeric zero.

Missing or inconsistent evaluation identity, a missing or invalid constitutive
profile, an undeclared scope or availability policy, invalid attribution or
weights and calculation failures are processing failures. They produce no
valid `operator_result_status` or K value and must not be disguised as a
common non-numeric status or numeric zero.

## 4. Static Components, Calculation and Interpretation

### 4.1 Why the Mathematical Contract Matters

The formula does not decide what counts as context. The versioned profile
declares the expected requirements, admitted scope, availability relation and
observable fulfillment rules. The formula summarizes those compatible results
without treating hidden or unavailable context as absent.

### 4.2 Expected Context-Requirement Set

```text
E_K,A(k_A | p_K) = {r_1, ..., r_q}
```

where `q > 0`. Each `r_i` is one profile-declared context requirement for the
target-event evaluation. The method does not prescribe a universal list of
goals, roles, assets, constraints, formats or tools. Such lists are application
profiles in the companion.

A context object may contribute evidence to more than one genuinely distinct
requirement only when the profile declares those roles. The
component-attribution policy must prevent silent double counting of the same
requirement or availability fact.

### 4.3 Observable Requirement Fulfillment - `a_i`

For each expected requirement:

```text
a_i,A(k_A | scope_A(k_A), p_K) in [0,1]
```

`a_i = 1` means the requirement is fully fulfilled under the declared
availability relation. `a_i = 0` means the relation is observable and the
expected requirement is absent or wholly unfulfilled. Intermediate values are
permitted only under a graded profile with declared subrequirements or
normalization.

If the required relation cannot be observed:

```text
a_i,A(k_A | scope_A(k_A), p_K) = not_observable
```

If a fixed implementation superset contains a feature that is not expected for
this target event, that implementation feature is `not_selected` and is not a
member of `E_K,A(k_A | p_K)`.

`a_i` measures observable provisioning, not correctness, usefulness or actual
use of the context object.

### 4.4 Static Formula and Profile Selection

Transparent unweighted v3.50 reference profile:

```text
K0_A(k_A | scope_A(k_A), p_K^u)
= (1 / |E_K,A(k_A | p_K^u)|)
  sum_{r_i in E_K,A(k_A | p_K^u)} a_i,A(k_A)
```

This formula applies only when `G_K,A(k_A | p_K^u) = open`. Otherwise K retains
the gate's typed non-numeric state.

Optional weighted profile:

```text
K0_A(k_A | scope_A(k_A), p_K^w)
= sum_i w_i a_i,A(k_A) / sum_i w_i
```

where every selected `w_i > 0`, the denominator is positive and the complete
expected set is numeric. Weights and their semantic justification are
versioned.

The unweighted and weighted profiles are alternatives. If both are computed,
store both separately. Exactly one declared profile supplies K in one Z view;
never average or substitute them silently.

### 4.5 Interpretation

Interpretation is profile-bound:

| Result | Meaning |
| --- | --- |
| high numeric K | expected context requirements are strongly fulfilled under the declared relation |
| medium numeric K | expected requirements are partly fulfilled |
| low numeric K | the complete basis is observable, but many requirements are absent or weakly fulfilled |
| numeric `0` | complete K applies and all expected requirements fail |
| `not_observable` | at least one requirement or required availability relation cannot be inspected |
| `not_applicable` | no valid non-empty expected context basis applies |
| `not_selected` | K was not requested for this evaluation |

Low K describes missing setup for one target event under one profile. It does
not establish failure, misunderstanding or poor contribution quality. High K
does not establish that context was correct, sufficient in an absolute sense,
or successfully used.

## 5. Edge Cases, Fairness, Privacy and Retention

### 5.1 Edge Cases

- An empty expected requirement set makes K `not_applicable`, not `1`.
- An expected, observable and absent object contributes numeric `0`.
- An expected object whose access relation is unobservable makes complete K
  `not_observable`, not zero.
- A stored file does not satisfy `target_access` without evidence of admission
  to the target event.
- A context object may be present for K and unusable as evidence for O.
- A visible format instruction may satisfy K while the target's structure
  remains weak under S.
- A changed scope or expected set blocks naive Delta even when both static
  values are numeric.

### 5.2 Fairness and Setup Boundary

K profiles must not assume that more context is always better. They evaluate a
declared expected set, not maximum prompt length, memory volume, document count
or tool count. Minimal, accessibility-oriented, safety-restricted or
privacy-preserving contexts may be complete under their own legitimate
profiles.

Low S, O, D or I should not be attributed to an entity without separately
showing whether relevant setup was present. Conversely, high K does not excuse
or explain another operator result automatically.

### 5.3 Privacy and Retention Boundary

Context scopes, prior events, files, tool outputs, access logs, feature states,
embeddings and derived trajectory views may contain sensitive or personal
information. Derived data is not automatically anonymous. Implementations must
declare access, consent, retention, deletion and provenance policies, including
whether later reconstruction can still verify the original availability
relation.

## 6. Comparability and Source-Local Dynamics

### 6.1 Comparability Contract

Two K values are directly comparable only when their constitutive conditions
are equal or connected by an explicit versioned compatibility mapping:

- target-unit and source-attribution rules;
- trajectory identity;
- scope-construction and context-object admission policies;
- expected requirement set and fulfillment rules;
- availability relation and observer vantage;
- detector and binary/graded value profiles;
- component-attribution and overlap policy;
- unweighted or weighted formula and weight profile;
- applicability and missingness policies;
- interpretation thresholds where used;
- window and aggregation policies for Sigma views.

```text
G_cmp_K,A(k_A)
= comparable(
    p_K,A(k_A),
    p_K,A(k_A-1),
    target_unit,
    trajectory_id,
    scope_and_admission_policies,
    expected_requirement_sets,
    availability_relations,
    observer_vantages,
    detectors_and_fulfillment_rules,
    value_and_weight_profiles,
    applicability_policies
  )
```

`G_cmp_K,A(k_A)` is a same-trajectory comparability gate. It is not `G_K`,
does not compare A with B and is not `R0`. Profile change is not ordinary K
movement.

### 6.2 Source-Local Dynamics

```text
K_A(k_A) = K0_A(k_A | scope_A(k_A), p_K,A(k_A))
```

If the current and same-trajectory predecessor values are numeric and
`G_cmp_K,A(k_A) = true`:

```text
Delta K_A(k_A) = K_A(k_A) - K_A(k_A-1)
```

If three consecutive static values are comparable:

```text
Delta2 K_A(k_A)
= Delta K_A(k_A) - Delta K_A(k_A-1)
```

Otherwise the respective result is `not_applicable` with its reason retained.
The first source-local event has no predecessor and therefore no first
difference.

Positive Delta means stronger fulfillment of the same context-requirement
profile than at the comparable predecessor. It does not establish general
improvement, learning or relational adaptation.

### 6.3 Separate Context Diagnostics

An implementation may compute separately named diagnostics for:

- a partial observable requirement subset;
- context-scope drift;
- detector or access-relation uncertainty;
- context-object recurrence, burst or removal.

These diagnostics require their own formula, profile, applicability and
comparability rules. They do not overwrite static K, Delta K, Delta2 K or the K
coordinate of a complete Z view. Their implementation mappings belong in the
companion.

## 7. Sigma and Sigma(Hangar)

For a declared source-local window `W_A`:

```text
W_app_K,A
= {k_A in W_A | K_A(k_A) is numeric under the static aggregation profile}

W_app_DeltaK,A
= {k_A in W_A | Delta K_A(k_A) is numeric and comparable}

W_app_Delta2K,A
= {k_A in W_A | Delta2 K_A(k_A) is numeric and comparable}
```

Typed source-local aggregation remains separate:

```text
KΣ_A(W_A).value
= Agg_K({K_A(k_A) | k_A in W_app_K,A})

KΣ_A(W_A).delta
= Agg_DeltaK({Delta K_A(k_A) | k_A in W_app_DeltaK,A})

KΣ_A(W_A).delta2
= Agg_Delta2K({Delta2 K_A(k_A) | k_A in W_app_Delta2K,A})
```

If one typed subset is empty, only that field is `not_applicable`. Static,
Delta and Delta2 values are not pooled. Aggregation functions, minimum sample
sizes and missingness policies are versioned.

The derived Hangar view is distinct:

```text
KΣ_A(Hangar).value
= distribution_view({K_A(k_A) | k_A in W_app_K,A})

KΣ_A(Hangar).delta
= distribution_view({Delta K_A(k_A) | k_A in W_app_DeltaK,A})

KΣ_A(Hangar).delta2
= distribution_view({Delta2 K_A(k_A) | k_A in W_app_Delta2K,A})
```

Hangar is derived from canonical event and evaluation records; it does not
replace them. Every view preserves source, target event, trajectory, local
index, profile, availability relation, applicability and derivation
provenance. Side-by-side display of A and B does not create a dyadic K measure.

## 8. Relational and Controller Boundary

`K0`, Delta K, Delta2 K, `KΣ(W)` and `KΣ(Hangar)` describe monadic context
provisioning. They do not measure shared context, mutual understanding,
adaptation, resonance or coupling.

A later relational comparison requires:

1. distinguishable source-attributed monadic inputs;
2. explicit pairing through `j` and `pi(j)`;
3. compatible K profiles and applicable values;
4. an open numeric canonical complete `R0` gate under the exact required
   profile;
5. a separately defined relational formula, range and interpretation.

This v3.50 file activates no operator-specific relational K comparison.
Post-`R0` partial comparisons and operator-only bypass routes remain v3.60
Future Work. They do not replace Z, canonical IK, `IK_rel` or an R-family
result.

Controller feedback, context injection or recursive context adaptation is an
action outside the Observer operator. It requires a separately authorized
policy and must not be written back into static K as though observation and
intervention were one state.

## 9. Formal Summary and Variable Reference

### 9.1 Compact Formula Block

```text
# one source-attributed target event
e_A(k_A), scope_A(k_A), p_K,A(k_A)

# expected context requirements; q > 0
E_K,A(k_A | p_K) = {r_1, ..., r_q}

# observable fulfillment under one declared availability relation
a_i,A(k_A | scope_A(k_A), p_K) in [0,1] or not_observable

# typed gate before numeric calculation
G_K,A(k_A | p_K)
in {open, not_selected, not_observable, not_applicable}

# common external result handed to Z
operator_result_status
in {numeric, not_selected, not_observable, not_applicable}

not_selected != not_observable != not_applicable != 0

# transparent unweighted reference profile
K0_A(k_A | scope_A(k_A), p_K^u)
= (1 / |E_K,A(k_A | p_K^u)|) sum_i a_i,A(k_A)
  only where G_K,A(k_A | p_K^u) = open

# optional weighted alternative
K0_A(k_A | scope_A(k_A), p_K^w)
= sum_i w_i a_i,A(k_A) / sum_i w_i
  only where G_K,A(k_A | p_K^w) = open and all w_i > 0

successful applicable finite K0_A
  -> operator_result_status = numeric
  -> result_value = K0_A(k_A | scope_A(k_A), p_K) in [0,1]

invalid identity/profile/scope policy/attribution/weights/calculation
  -> processing failure; no valid operator result

# exactly one declared K profile fills K in one Z view
Z_A(k_A) = (K_A, S_A, O_A, D_A, I_A)

# source-local movement only after comparability
Delta K_A(k_A)  = K_A(k_A) - K_A(k_A-1)
Delta2 K_A(k_A) = Delta K_A(k_A) - Delta K_A(k_A-1)

# typed windows
KΣ_A(W_A).value  = Agg_K(applicable static K values)
KΣ_A(W_A).delta  = Agg_DeltaK(applicable comparable Delta K values)
KΣ_A(W_A).delta2 = Agg_Delta2K(applicable comparable Delta2 K values)

# Hangar remains derived and source-attributed
KΣ_A(Hangar) = typed distribution views derived from canonical records

# partial visibility, scope drift and uncertainty remain separate diagnostics
# relational work begins only after explicit pairing and an open numeric
# canonical complete R0 gate under the exact required profile
```

### 9.2 Variable Reference

| Symbol | Semantic role |
| --- | --- |
| `e_A(k_A)` | target event attributed to stable or provisional source A at local position `k_A` |
| `n` | global observable event index |
| `k_A`, `k_B` | local indices of distinguishable source trajectories |
| `j` | declared relational exchange or paired-evaluation index |
| `pi(j)` | explicit mapping from relational index to paired local indices |
| `scope_A(k_A)` | admissible context-object set for the target-event evaluation |
| `p_K` | versioned K profile bound to one evaluation |
| `availability_relation_id` | declared relation whose context availability is observed |
| `observer_vantage_id` | declared evaluator visibility boundary |
| `E_K,A(k_A \| p_K)` | non-empty expected context-requirement set |
| `r_i` | one expected context requirement |
| `a_i,A(k_A \| scope_A(k_A), p_K)` | observable fulfillment value for `r_i` |
| `G_K,A(k_A \| p_K)` | typed K applicability gate; never a numeric multiplier |
| `w_i` | positive versioned requirement weight in a weighted profile |
| `K0_A(k_A \| scope_A(k_A), p_K)` | static observable context completeness |
| `G_cmp_K,A(k_A)` | same-trajectory K comparability gate; distinct from `G_K` and `R0` |
| `Delta K_A(k_A)` | first source-local K difference |
| `Delta2 K_A(k_A)` | second source-local K difference |
| `W_app_K,A` | applicable static K subset of a declared window |
| `W_app_DeltaK,A` | applicable and comparable first-difference subset |
| `W_app_Delta2K,A` | applicable and comparable second-difference subset |
| `Agg_K`, `Agg_DeltaK`, `Agg_Delta2K` | separately versioned type-appropriate aggregation functions |
| `KΣ_A(W_A)` | typed source-local K window aggregation |
| `KΣ_A(Hangar)` | typed derived Hangar distribution view |
| `open` | complete selected K basis is observable and applicable |
| `operator_result_status` | common Layer-1 result: numeric, not selected, not observable or not applicable |
| `not_selected` | K was not requested under the evaluation profile |
| `not_observable` | required context or availability relation cannot be inspected |
| `not_applicable` | no valid non-empty K basis applies; never numeric zero |

### 9.3 Template Consistency Tests

| Test | Result | Reason |
| --- | --- | --- |
| monadic-independence / removal | PASS | A's K construction remains defined from A's target and declared context basis; external context changes do not create a dyadic formula |
| exchange-role reversal | PASS | stable entity and trajectory identity remain distinct from sender/receiver roles |
| application substitution | PASS | Human-Chatbot and Morse examples use the same context-completeness question and formula boundary |
| layer dependency | PASS | static K depends on no Z, IK, R0, IK_rel or R-family result |
| provenance | PASS | entity, event, context objects, scope, availability relation, trajectory, indices and pairing metadata remain distinguishable |

## 10. Separate Implementation Companion

Implementation-specific context taxonomies, prompt or container fields,
detector markers, storage mappings, partial diagnostics, pseudocode, candidate
weights, data flow and architecture configuration belong in:

- Public implementation companion:
  [`KSODI_Operator-K_Implementation-Companion_V350.md`](./KSODI_Operator-K_Implementation-Companion_V350.md)

The companion may operationalize K but must not redefine its semantic question,
availability relation, measurement basis, applicability, source identity,
static formula or layer boundary. Public release does not convert its context
taxonomies, detector mappings, candidate profiles or weights into universal K
semantics or a mandatory production architecture.
