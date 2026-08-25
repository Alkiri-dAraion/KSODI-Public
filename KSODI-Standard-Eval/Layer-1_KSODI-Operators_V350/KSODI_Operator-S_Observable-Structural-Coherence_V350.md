# KSODI Operator S0 - Observable Structural Coherence v3.50

Status: public v3.50 reference release, reviewed and clarified on 2026-08-25
through the reader-first method and common typed-result contract. This file is
the authoritative carrier-neutral definition of Operator S.

Layer: KSODI Standard-Eval Layer 1. One static `S0` value belongs to one
explicitly identified, source-attributed target event under one declared and
versioned S profile. Source-local movement and aggregation remain monadic.

Implementation companion:
[`KSODI_Operator-S_Implementation-Companion_V350.md`](./KSODI_Operator-S_Implementation-Companion_V350.md)
(public conditional guidance; method/companion alignment reviewed 2026-08-25).

## 0. What Operator S is and what it does

`S` answers one narrow observable question:

> How coherently are the observable parts of this source-attributed target
> event organized under the declared structural profile and evaluation scope?

S evaluates relations among observable parts: segmentation, boundaries,
declared structural requirements, ordering and profile-defined structural
disruption. It does not reward length, ornament, formatting density or
complexity by themselves.

S begins with one target event. Visible context may supply a declared schema,
task requirement or structural reference, but it does not become part of the
target event and does not merge source identities.

S does not establish:

- correctness, truth or evidence support;
- successful semantic decoding;
- clarity or signal strength;
- information novelty or update value;
- communicative success, agreement, resonance or coupling;
- hidden intention, cognition or human value.

### 0.1 Minimal practical reading

For a reader who does not want to begin with the formula:

- D asks whether the declared carrier offers enough observable support for a
  reconstruction attempt.
- S asks how the observable parts, once available under the S basis, are
  organized in relation to one another.
- A short or simple event is not structurally weak merely because it has few
  parts.
- Many headings, separators or repeated delimiters do not by themselves prove
  coherent structure.
- Numeric `0`, `not_applicable`, `not_observable` and `not_selected` are
  different results.

High S means that the event's observable parts satisfy the selected
profile-bound structural relations strongly. Low S means that the question is
applicable but those relations are weak or violated. `not_applicable` means
that the declared profile does not provide a valid structural basis for this
event; no numeric structural claim follows.

### 0.2 How to read this file

New readers may begin with Sections 0-2, the interpretation in Section 4.7 and
the relational boundary in Section 8. Method reviewers should follow the full
path: examples, identity, index discipline, measurement basis, applicability,
components, profile selection, comparability, movement and aggregation.

The order is deliberate. The semantic question opens the file; implementation
fields and detector examples remain in the separate companion.

## 1. Bounded Application Examples

The examples instantiate the same canonical S question. They do not establish
domain equivalence, empirical validation or a universal detector.

### 1.1 Human-Chatbot Interaction

```text
entity_A          = human
entity_B          = chatbot
target_event_A    = one source-attributed human contribution
target_event_B    = one source-attributed chatbot contribution
trajectory_A      = human contribution trajectory
trajectory_B      = chatbot contribution trajectory
measurement_basis = visible contribution plus declared text-structure profile
exchange_id       = separate edge metadata where a reply relation exists
```

Each contribution is evaluated separately. A short human question can receive
high S under a profile that treats a concise, correctly bounded interrogative
unit as structurally complete. A longer chatbot response can receive low S if
its sections contradict their headings, its steps are scrambled or its visible
boundaries do not support the declared order.

The example therefore does not equate length, formatting or verbosity with
structure. `S_A(k_A)` and `S_B(k_B)` do not establish structural alignment,
coupling or resonance between human and chatbot.

### 1.2 Unknown Morse-Like Signal

```text
entity_A          = stable or explicitly provisional observed signal source
target_event_A    = one bounded source-attributed pulse burst
carrier           = observable pulses and gaps
measurement_basis = declared pulse/gap segmentation and structural profile
meaning           = unknown
reply_relation    = absent unless separately observed and declared
```

The evaluator may observe repeatable pulse groups, stable boundaries and an
ordered pattern without knowing what the signal means. Under a profile that
declares pulse/gap segmentation and admissible order relations, S can evaluate
the organization of the burst. High S would not prove decoding, truth,
grounding, a confirmed emitter identity or protocol acknowledgement.

If the burst is not sufficiently observable for the declared S segmenter, the
result is `not_observable`. If it is observable but no structural relation is
applicable under the profile, the result is `not_applicable`. Repetition across
several bursts belongs to a separately typed source-local trajectory
diagnostic; it does not overwrite the static S value of one burst.

## 2. Canonical Definition, Scope and Boundaries

`S0_A(k_A | p_S)` evaluates the observable structural coherence of one target
event `e_A(k_A)` emitted by one entity A under one declared versioned S profile
`p_S`.

Carrier-neutral semantic core:

> Structural coherence is the degree to which observable parts of one target
> event satisfy the profile-declared segmentation, boundary, requirement and
> order relations needed to reconstruct its observable organization.

“Reconstruct its observable organization” is narrower than reconstructing the
signal or decoding its meaning. Static S concerns relations within the target
event. Stability, recurrence or change across target events belongs to
source-local dynamics and diagnostics after comparability has been established.

S is architecture-agnostic. A carrier-specific use must declare its own target
unit, segmentation, structural evidence, detector, normalizer, applicability
policy and interpretation boundary.

### 2.1 Atomic Evaluation Unit and Identity

The canonical evaluation unit contains or recoverably references:

```text
target_event_id
source_entity_id
source_attribution_status
emitting_entity_id, if established
trajectory_id
global_event_index n
local_trajectory_index k_A
observable_target_payload or carrier reference
visible_context_event_ids
evaluation_scope
s_profile_id and version
applicability state
```

The target event, its visible context and its source identity remain distinct.
An entity may have several trajectories. Sender and receiver are roles attached
to a concrete exchange edge, not permanent entity types.

The canonical cross-layer identity boundary is summarized in the
[`KSODI Architecture v3.50`](../../KSODI-Architecture_V350.md); this method
retains the S-specific required fields explicitly above.

Context may contain a schema, task instruction or convention admitted by
`p_S`. That context does not become part of the target payload, and a response
from another entity does not retroactively alter the static S value unless a
new, explicitly versioned evaluation is created.

#### 2.1.1 Canonical Index Discipline

```text
n   = global event index in the observable event stream
k_A = local position inside trajectory A
k_B = local position inside trajectory B
j   = declared relational exchange or paired-evaluation index

pi(j) = (k_A(j), k_B(j))
```

Static S uses the local index of its own source-attributed event. `j` and
`pi(j)` are not inputs to static S. A timestamp `t` may be retained only with
an explicit mapping; it must not silently imply synchronized local positions
or a shared predecessor across entities.

### 2.2 Static and Source-Local S Views Are Strictly Monadic

```text
S_A(k_A | p_S,A(k_A))
S_B(k_B | p_S,B(k_B))
```

are separate values on separate source trajectories. The profiles may be equal
by declaration but equality is never inferred from a shared room, task,
conversation, timestamp or interface.

Removing Entity B leaves `S_A(k_A)`, `Z_A(k_A)` and monadic `IK_A(k_A)`
defined whenever A's own basis and applicability conditions are satisfied.
Source-local Delta, Delta2, Sigma and Hangar views do not change this arity.

### 2.3 Semantic Distinctness and Symbol Discipline

| Coordinate | Narrow observable question | Boundary to S0 |
| --- | --- | --- |
| `K0` | Is the required context available and complete? | context availability is not structural organization |
| `O0` | Is the target grounded and traceable in a visible admissible reference space? | grounding is not structure |
| `D0` | Does the carrier support observable discrimination and reconstruction? | detectability and signal reconstruction are not organization among observed parts |
| `I0` | What observable information impulse exists relative to its declared basis? | information difference is not structure |

Important distinctions:

```text
visible markers are not coherent structure
structure is not clarity
order is not meaning
repetition is not acknowledgement
coherence is not resonance
```

This file uses `Ref` only for declared reference material and reserves
`R`-prefixed symbols for the relational and resonance family. `P_disrupt`
denotes an optional structural disruption penalty; it is not Operator D.

### 2.4 Coordinate Order and Directed Process Topologies

```text
Z_A(k_A) = (K_A, S_A, O_A, D_A, I_A)
```

This is coordinate order, not a causal calculation chain.

```text
sender-side formation:        K -> S -> O -> D -> I
receiver-side reconstruction: I -> D -> O -> S -> K
```

In sender-side formation, structure may organize material before it is adapted
to a carrier. In receiver-side reconstruction, structural hypotheses arise
only after an event has been noticed and sufficiently distinguished under the
relevant observation conditions. With an unknown convention, segmentation and
order hypotheses may be reopened recursively.

These role-relative topologies do not make numeric I, D, O or K values inputs
to the static S formula. They do not claim access to hidden cognition or
internal machine processing.

## 3. Measurement Basis, Profiles and Applicability

### 3.1 Declared S Measurement Basis

Before calculation, declare:

- the source-attributed target event and observable carrier;
- evaluation-unit and evaluation-scope boundaries;
- segment or part definition;
- explicit structural requirements, if any;
- structural order reference or hypothesis rule, if any;
- accepted boundary and marker evidence;
- detector, segmenter and normalizer profiles;
- mandatory and optional component masks;
- component-attribution and overlap policy;
- component weights and optional disruption policy;
- observability, applicability and missingness rules.

Undeclared whole-conversation history, another entity's output, a later reply,
Hangar expectations or an R-family result are not part of the static S basis.

### 3.2 Versioned S Profile

```text
p_S = (
  profile_id,
  profile_version,
  carrier_profile,
  target_unit_profile,
  evaluation_scope,
  segmenter_profile,
  requirement_profile,
  boundary_detector_profile,
  order_reference_profile,
  normalizer_profile,
  mandatory_component_mask,
  optional_component_mask,
  component_attribution_policy,
  weight_profile,
  disruption_profile,
  applicability_policy,
  interpretation_profile
)
```

Every constitutive choice must be recoverable. Changing the target unit,
carrier, segmentation, requirements, structural reference, detector,
normalizer, component mask, attribution policy, weights, penalty or
applicability policy may create a new profile and therefore a comparability
boundary.

Exactly one declared S profile fills the S coordinate of a given
five-dimensional Z view. Minimal and extended profiles are alternative results,
not simultaneous S coordinates.

### 3.3 Applicability Before Numeric Interpretation

At minimum, preserve these typed states:

```text
operator_result_status in {
  numeric,
  not_selected,
  not_observable,
  not_applicable
}
```

`not_selected` means S was not requested under the declared evaluation
profile. `not_observable` means the target or required observable structural
evidence exists or is expected under the selected profile but cannot be
inspected. `not_applicable` means S was selected but no valid structural basis
applies. A successfully applicable finite calculation emits
`operator_result_status = numeric` with `result_value in [0,1]`; numeric `0`
means that applicable structural relations fail completely.

Therefore:

```text
not_selected != not_observable
not_observable != not_applicable
not_applicable != 0
```

A numeric S value opens only when:

1. the target event and stable or explicitly provisional source identity are
   resolved;
2. the target is observable under the declared S basis;
3. the selected segmenter and structural evidence are applicable;
4. every mandatory component is available;
5. the profile's active evidence configuration is structurally sufficient;
6. the sum of active weights is greater than zero.

Missing or inconsistent evaluation identity, a missing or invalid constitutive
profile, invalid weights and calculation failures are processing failures. They
produce no valid `operator_result_status` or S value and must not be disguised
as `not_applicable`, `not_observable`, `not_selected` or numeric zero.

`M_vis` alone does not open numeric S under the default v3.50 discipline.
Visible delimiters may support segmentation while failing to establish a
coherent relation among parts. A specialized profile may treat a marker pattern
as sufficient only when that structural rule, detector and justification were
declared before evaluation; it remains a separately named profile.

## 4. Static Components, Calculation and Interpretation

### 4.1 Why the Mathematical Contract Matters

The formula does not create the meaning of S. The declared semantic question,
measurement basis, profile and applicability rules determine what the numbers
refer to. The formula then combines compatible component results without
silently treating missing evidence as success, failure or zero.

### 4.2 Explicit Structural-Requirement Conformance - `C_req`

`C_req,A(k_A | E_S,p_S)` asks how strongly the target event satisfies the
explicit structural requirements selected by `p_S`.

Requirements may concern fields, nesting, boundaries or phases. Their weights
and fulfillment rules must be declared. Explicit transition or order relations
are assigned to `P_order` unless a profile deliberately assigns them to
`C_req`; the same evidence must not be counted in both components without an
explicit overlap rule and justification. A carrier with no selected structural
requirements makes `C_req` `not_applicable`, not `0.5`.
If selected requirements exist but their required observable fulfillment
evidence cannot be inspected, `C_req` is `not_observable`.

```text
C_req,A(k_A | E_S,p_S)
= fulfilled_requirement_weight / selected_requirement_weight
```

where the denominator is greater than zero. The result lies in `[0,1]`.

### 4.3 Visible Segmentation and Boundary Support - `M_vis`

`M_vis,A(k_A | p_S)` asks whether profile-accepted observable boundaries or
markers support a stable segmentation of the target event.

The component is normalized against carrier- and unit-appropriate structural
opportunities or extent. It is never the unscaled count of headings,
delimiters, gaps or labels.

```text
M_vis,A(k_A | p_S)
= N_boundary(
    effective_nonredundant_boundary_evidence,
    eligible_structural_opportunities,
    carrier_extent,
    p_S
  )
```

`N_boundary` must return `[0,1]`. Artificial repetition, redundant delimiters
and marker inflation do not increase the component. If required boundary
evidence cannot be inspected, `M_vis = not_observable`; if no valid boundary
basis applies, `M_vis = not_applicable`.

`M_vis` measures segmentation support, not complete structural coherence. It
does not open numeric S by itself under the default profile discipline.

### 4.4 Order-Relation Coherence - `P_order`

`P_order,A(k_A | StructRef_S,p_S)` asks how strongly the observable parts
satisfy the selected order relations.

```text
P_order,A(k_A | StructRef_S,p_S)
= satisfied_transition_weight / applicable_transition_weight
```

where the denominator is greater than zero and the result lies in `[0,1]`.

`StructRef_S` may come from an explicit schema, a declared task, a domain
protocol or a profile-permitted hypothesis rule. A structure inferred from the
same target must not be fitted ad hoc merely to reward that target. The
hypothesis rule, uncertainty treatment and evaluation procedure must be fixed
and versioned before scoring.

If required order evidence cannot be inspected, `P_order = not_observable`. If
no order relation applies, `P_order = not_applicable`.

### 4.5 Optional Structural-Disruption Penalty - `P_disrupt`

`P_disrupt,A(k_A | p_S)` is an optional profile-bound penalty for observable
structural disruption. An implementation may expose distinct duplication and
fragmentation diagnostics, but it must not conflate them invisibly.

```text
P_disrupt,A(k_A | p_S)
  in [0,1] or not_observable or not_applicable
```

High `P_disrupt` means stronger profile-defined disruption. Repetition may be
structural, corrective or confirmatory; fragmentation may be legitimate
segmentation. The penalty is therefore disabled unless a named extended
profile declares its detectors, combination rule and weight.

### 4.6 Static Formula and Profile Selection

Let:

```text
C_S,A(k_A) = {C_req,A, M_vis,A, P_order,A}
A_S,A(k_A) = {C_i in C_S,A(k_A) | C_i is applicable and selected by p_S}
M_S(p_S)   = mandatory component set declared by p_S
```

The base value is defined only when every mandatory component is applicable,
the profile's evidence-sufficiency rule passes and active weights are positive:

```text
S_base,A(k_A | p_S)
= clip(
    sum_{C_i in A_S,A(k_A)} w_i C_i
    / sum_{C_i in A_S,A(k_A)} w_i,
    0,
    1
  )
```

Renormalization over applicable optional components is allowed only when the
profile declares it. A mandatory component that is expected but cannot be
observed makes S `not_observable`; a mandatory component for which no valid
structural basis applies makes S `not_applicable`. Mandatory components are
never silently dropped. If a selected optional component is non-numeric and
optional renormalization is disabled, its retained reason maps S to the same
common non-numeric status. Invalid component states or undeclared fallback are
processing failures.

This normalization is a declared component-weight construction inside one
static event evaluation under one fixed S profile. It does not authorize an
event-wise change, intersection or renormalization of active sets across
trajectory dynamics, windows, state-vector projections or relational
constructions; those operations require their own fixed-set and comparability
contracts.

The component-attribution policy must prevent one boundary, requirement or
transition from contributing repeatedly through `C_req`, `M_vis` and
`P_order` unless the profile explicitly models that dependence. Visible
overlap is a calibration choice; silent double counting is invalid.

For a minimal profile:

```text
S0_A(k_A | p_S,min) = S_base,A(k_A | p_S,min)
```

For an extended disruption profile:

```text
S0_A(k_A | p_S,ext)
= clip(S_base,A(k_A | p_S,ext) - gamma_S P_disrupt,A(k_A | p_S,ext), 0, 1)
```

where `gamma_S >= 0` is versioned and `P_disrupt` is applicable. If the
extended profile selects the penalty but the penalty cannot be calculated, the
extended result is `not_observable` when required disruption evidence is
expected but unavailable, or `not_applicable` when no valid disruption basis
applies. Invalid detector configuration or calculation is a processing
failure. The minimal profile may remain separately evaluable.

No universal component weights or thresholds are asserted here. Candidate
weights, detector mappings and pseudocode belong to the implementation
companion and require domain validation.

### 4.7 Interpretation

Interpretation is profile-bound:

| Result | Meaning |
| --- | --- |
| high numeric S | the selected observable structural relations are strongly satisfied |
| medium numeric S | the relations are partly satisfied or locally inconsistent |
| low numeric S | the question applies, but the selected relations are weak or strongly violated |
| numeric `0` | applicable structural relations fail completely under the profile |
| `not_applicable` | no valid structural basis applies under the selected profile |
| `not_observable` | required observable parts cannot be inspected |
| `not_selected` | S was not requested for this evaluation |

Low S does not mean incorrect, unclear, uninformative, aesthetically poor or
humanly inferior. High S does not establish truth, meaning or relational
success.

## 5. Edge Cases, Fairness, Privacy and Retention

### 5.1 Edge Cases

- A one-part or short target may be structurally complete under an atomic
  profile; length is not an S component.
- A marker-rich target may remain low S where the markers do not support the
  declared relations.
- An unknown but repeatable pattern may have observable structure without
  known meaning.
- A valid schema with no order requirement may use a profile in which
  `C_req` supplies the mandatory basis and `P_order` is not selected.
- A changed profile or segmenter blocks naive Delta even when both static
  values are numeric.
- Cross-event recurrence, stagnation, burst and oscillation are separate
  trajectory diagnostics; they do not overwrite static S.

### 5.2 Fairness and Setup Boundary

S profiles must not silently privilege verbosity, a particular writing system,
markdown usage, normative prose style, neurotypical formatting or one cultural
rhetorical order. Accessibility formats, terse protocols, compressed carriers
and alternative but valid structures require appropriate declared profiles.

Shared detectors, embeddings, segmenters or markers across S and D can create
artificial correlation. Reuse is permitted only when detector identity and the
different operator semantics remain visible.

### 5.3 Privacy and Retention Boundary

Raw carriers, extracted segments, marker maps, embeddings, component values
and derived trajectory views may contain sensitive or personal information.
Derived data is not automatically anonymous or privacy-neutral. An
implementation must preserve applicable access, consent, retention and deletion
rules plus provenance for profile and detector versions.

## 6. Comparability and Source-Local Dynamics

### 6.1 Comparability Contract

Two S values are directly comparable only when their constitutive conditions
are equal or connected by an explicit versioned compatibility mapping:

- target-unit and carrier types;
- evaluation scope;
- S profile and formula variant;
- segmentation, requirement, boundary, order and normalizer profiles;
- mandatory and optional component masks;
- component-attribution and overlap policy;
- active-component and renormalization policies;
- weights and disruption profile;
- observability, applicability and missingness policies;
- interpretation thresholds where used.

```text
G_cmp_S,A(k_A)
= comparable(
    p_S,A(k_A),
    p_S,A(k_A-1),
    target_unit,
    carrier,
    scope,
    component_masks,
    detector_and_normalizer_versions,
    weights,
    formula_variant,
    applicability_policy
  )
```

`G_cmp_S,A(k_A)` applies only inside the same declared trajectory. It is not
`R0` and does not compare A with B. A profile change is not ordinary movement.

### 6.2 Source-Local Dynamics and Separate Diagnostics

```text
S_A(k_A) = S0_A(k_A | p_S,A(k_A))
```

If the current and same-trajectory predecessor values are numeric and
`G_cmp_S,A(k_A) = true`:

```text
Delta S_A(k_A) = S_A(k_A) - S_A(k_A-1)
```

If three consecutive static values are comparable:

```text
Delta2 S_A(k_A)
= Delta S_A(k_A) - Delta S_A(k_A-1)
```

Otherwise the respective result is `not_applicable` with its reason retained.
The first source-local event has no predecessor and therefore no first
difference.

Positive Delta means stronger satisfaction of the same declared structural
profile than the comparable predecessor; negative Delta means weaker
satisfaction. It does not establish improvement or deterioration in general
quality.

Recurrence, burst, stagnation or oscillation may be computed as separately
named source-local diagnostics under a declared window profile. They never
replace static S, Delta S or Delta2 S.

## 7. Sigma and Sigma(Hangar)

For a declared source-local window `W_A`:

```text
W_app_S,A
= {k_A in W_A | S_A(k_A) is numeric under the static aggregation profile}

W_app_DeltaS,A
= {k_A in W_A | Delta S_A(k_A) is numeric and comparable}

W_app_Delta2S,A
= {k_A in W_A | Delta2 S_A(k_A) is numeric and comparable}
```

Typed source-local aggregation remains separate:

```text
S_Σ_A(W_A).value
= Agg_S({S_A(k_A) | k_A in W_app_S,A})

S_Σ_A(W_A).delta
= Agg_DeltaS({Delta S_A(k_A) | k_A in W_app_DeltaS,A})

S_Σ_A(W_A).delta2
= Agg_Delta2S({Delta2 S_A(k_A) | k_A in W_app_Delta2S,A})
```

If one typed subset is empty, only that field is `not_applicable`. Static,
Delta and Delta2 values are not pooled into one number. Aggregation functions,
minimum sample sizes and missingness policies are versioned.

The derived Hangar view is distinct:

```text
S_Σ_A(Hangar).value
= distribution_view({S_A(k_A) | k_A in W_app_S,A})

S_Σ_A(Hangar).delta
= distribution_view({Delta S_A(k_A) | k_A in W_app_DeltaS,A})

S_Σ_A(Hangar).delta2
= distribution_view({Delta2 S_A(k_A) | k_A in W_app_Delta2S,A})
```

Hangar is derived from canonical event and evaluation records; it does not
replace them. Every view preserves source, target-event, trajectory, local
index, profile, applicability and derivation provenance. Side-by-side display
of A and B does not create a dyadic measure.

## 8. Relational Boundary

`S0`, Delta S, Delta2 S, `S_Σ(W)` and `S_Σ(Hangar)` describe monadic
structural behavior. They do not measure structural resonance or coupling.

A later relational comparison requires:

1. distinguishable source-attributed monadic inputs;
2. explicit pairing through `j` and `pi(j)`;
3. compatible S profiles and applicable values;
4. an open numeric canonical complete `R0` gate under the exact required
   profile;
5. a separately defined relational formula, range and interpretation.

This v3.50 file activates no operator-specific relational S comparison.
Post-`R0` partial comparisons and operator-only bypass routes remain v3.60
Future Work. They do not replace Z, canonical IK, `IK_rel` or an R-family
result.

## 9. Formal Summary and Variable Reference

### 9.1 Compact Formula Block

```text
# one source-attributed target event
e_A(k_A), p_S,A(k_A)

# typed applicability before numeric calculation
not_selected != not_observable != not_applicable != 0

# static components
C_req,A(k_A | E_S,p_S)
  in [0,1] or not_observable or not_applicable
M_vis,A(k_A | p_S)
  in [0,1] or not_observable or not_applicable
P_order,A(k_A | StructRef_S,p_S)
  in [0,1] or not_observable or not_applicable
P_disrupt,A(k_A | p_S)
  in [0,1] or not_observable or not_applicable

A_S,A(k_A) = applicable selected base components
M_S(p_S)   = mandatory component set

# M_vis alone is insufficient under the default v3.50 discipline
# all mandatory components and the evidence-sufficiency rule must pass

numeric S_base requires:
  every component in M_S(p_S) is applicable
  and the structural-sufficiency rule passes
  and any optional-component renormalization was declared by p_S
  and sum_{C_i in A_S,A(k_A)} w_i > 0

otherwise:
  required observable basis unavailable
    -> operator_result_status = not_observable
  no valid structural basis applies
    -> operator_result_status = not_applicable
  S not selected
    -> operator_result_status = not_selected
  invalid identity/profile/weights/calculation
    -> processing failure; no valid operator result

S_base,A(k_A | p_S)
= clip(
    sum_{C_i in A_S,A(k_A)} w_i C_i
    / sum_{C_i in A_S,A(k_A)} w_i,
    0,
    1
  )

S0_A(k_A | p_S,min) = S_base,A(k_A | p_S,min)

S0_A(k_A | p_S,ext)
= clip(S_base,A - gamma_S P_disrupt,A, 0, 1)

successful applicable finite S0_A
  -> operator_result_status = numeric
  -> result_value = S0_A(k_A | p_S) in [0,1]

# exactly one declared profile fills S in one Z view
Z_A(k_A) = (K_A, S_A, O_A, D_A, I_A)

# source-local movement only after comparability
Delta S_A(k_A)  = S_A(k_A) - S_A(k_A-1)
Delta2 S_A(k_A) = Delta S_A(k_A) - Delta S_A(k_A-1)

# typed windows
S_Σ_A(W_A).value  = Agg_S(applicable static S values)
S_Σ_A(W_A).delta  = Agg_DeltaS(applicable comparable Delta S values)
S_Σ_A(W_A).delta2 = Agg_Delta2S(applicable comparable Delta2 S values)

# Hangar remains derived and source-attributed
S_Σ_A(Hangar) = typed distribution views derived from canonical records

# relational work begins only after explicit pairing and an open numeric
# canonical complete R0 gate under the exact required profile
```

### 9.2 Variable Reference

| Symbol | Semantic role |
| --- | --- |
| `e_A(k_A)` | source-attributed target event emitted by A at local position `k_A` |
| `n` | global observable event index |
| `k_A`, `k_B` | local indices of distinguishable source trajectories |
| `j` | declared relational exchange or paired-evaluation index |
| `pi(j)` | explicit mapping from relational index to paired local indices |
| `p_S` | versioned S profile bound to one evaluation |
| `component_attribution_policy` | versioned rule preventing silent evidence reuse across S components |
| `E_S` | selected explicit structural requirements |
| `StructRef_S` | declared structural order reference or hypothesis rule |
| `C_req` | explicit structural-requirement conformance |
| `M_vis` | visible segmentation and boundary support |
| `N_boundary` | versioned carrier- and unit-appropriate boundary normalizer |
| `P_order` | order-relation coherence |
| `P_disrupt` | optional structural-disruption penalty |
| `C_S,A(k_A)` | profile-defined base-component family for the target event |
| `M_S(p_S)` | mandatory component set |
| `A_S,A(k_A)` | applicable selected base-component set |
| `w_i` | non-negative versioned component weight |
| `gamma_S` | non-negative versioned disruption weight |
| `S_base,A(k_A \| p_S)` | applicability-aware weighted base construction before an optional disruption penalty |
| `S0_A(k_A \| p_S)` | static observable structural coherence |
| `S_A(k_A)` | selected static S value used in source-local dynamics |
| `G_cmp_S,A(k_A)` | same-trajectory S comparability gate; not `R0` |
| `Delta S_A(k_A)` | first source-local S difference |
| `Delta2 S_A(k_A)` | second source-local S difference |
| `W_app_S,A` | applicable static S subset of a declared source-local window |
| `W_app_DeltaS,A` | applicable and comparable first-difference subset |
| `W_app_Delta2S,A` | applicable and comparable second-difference subset |
| `Agg_S`, `Agg_DeltaS`, `Agg_Delta2S` | separately versioned type-appropriate window aggregation functions |
| `S_Σ_A(W_A)` | typed source-local S window aggregation |
| `S_Σ_A(Hangar)` | typed derived Hangar distribution view |
| `not_selected` | S not requested under the evaluation profile |
| `not_observable` | required observable basis unavailable |
| `not_applicable` | no valid structural basis applies; never numeric zero |
| `operator_result_status` | common Layer-1 result: numeric, not selected, not observable or not applicable |

### 9.3 Template Consistency Tests

| Test | Result | Reason |
| --- | --- | --- |
| monadic-independence / removal | PASS | removing B does not remove A's valid S basis |
| exchange-role reversal | PASS | stable entity and trajectory identity remain distinct from sender/receiver roles |
| application substitution | PASS | Human-Chatbot and Morse examples use the same structural question and formula boundary |
| layer dependency | PASS | static S depends on no Z, IK, R0, IK_rel or R-family result |
| provenance | PASS | entity, event, trajectory, local/global index and pairing metadata remain distinguishable |

## 10. Separate Implementation Companion

Implementation-specific storage fields, pseudocode, detector mappings,
normalization examples, candidate weights, data flow and architecture
configuration belong in:

- Public implementation companion:
  [`KSODI_Operator-S_Implementation-Companion_V350.md`](./KSODI_Operator-S_Implementation-Companion_V350.md)
- Alignment status: method and companion review passed on 2026-08-25;
  alignment with Patrick's current Observer and KSODI-Light implementation
  remains a separate implementation-side task.

The companion may operationalize S but must not redefine its semantic question,
measurement basis, applicability, source identity, static formula or layer
boundary. Public release does not convert its detector mappings, candidate
profiles or workbench weights into universal S semantics or a mandatory
production architecture.
