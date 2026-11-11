# KSODI Layer-1 Operator Template v3.51

This shared v3.51 authoring and review template is a non-canonical scaffold.
It does not define an additional KSODI operator or formula. Its structural and
boundary checks apply to v3.51 Layer-1 operator work unless a documented
operator-specific reason requires a deviation.

Purpose: provide a shared structure for creating or revising a KSODI v3.51
Layer-1 operator without copying the semantics, formula shape or special gates
of another operator.

Abstraction must not be produced by deleting precision. Move carrier-specific
roles and nouns out of the canonical definition while retaining the exact
evaluation unit, source identity, trajectory, measurement basis, profile,
applicability, comparability, index and layer boundary needed for a valid
calculation.

## Part A - Authoring and review control

### Canonical abstraction and reader order

Every finished Layer-1 operator must present its material in this reader-facing order:

1. **Quick orientation:** the operator family's broad carrier-neutral
   observation question, the bounded question instantiated by the declared
   profile, plain-language purpose, minimal practical reading and explicit
   non-claims.
2. **Two bounded application examples:** one Human–Chatbot example and one
   second-domain example mapped from the same canonical definition.
3. **Canonical definition, scope and boundaries:** entity, target event,
   trajectory, monadic independence, operator distinction and layer boundary.
4. **Measurement basis and static calculation:** profile, applicability,
   components, formula and interpretation.
5. **Movement and pattern observation:** comparability before source-local
   Delta / Delta2, followed by typed Sigma and Hangar views.
6. **Relational boundary:** a concentrated statement of where Layer 1 ends and
   separately gated relational work may begin.
7. **Formal summary and variable reference:** active formulas and their symbols
   after the full semantic path has been explained.
8. **Implementation boundary and optional pointer:** the method file ends with
   a clear separation from implementation material. If an adjacent
   implementation companion exists, link it without making it a condition of
   the method. Storage fields, pseudocode, detector examples and
   architecture-specific mappings belong in that companion or another clearly
   identified implementation artifact.

Application-role or pipeline terms such as question, answer, user prompt,
assistant response, retrieval, web search or chatbot may appear in the bounded
application example or in an explicitly conditional implementation mapping.
They must not silently define the canonical target, event type, measurement
basis or operator.

Both required examples must map from the same canonical definition. Each must
declare its own observation unit, source attribution, measurement basis and
interpretation discipline. The examples explain the schema; they are not
canonical formulas, empirical validation or evidence that their domains are
equivalent.

Before using this template, read:

- [Layer-1 measurement basis and reference discipline](LAYER_1_MEASUREMENT_BASIS_AND_REFERENCE_DISCIPLINE_V351.md)
- [public architecture](../../KSODI-Architecture_V351.md)
- [operator distinction working note](LAYER_1_OPERATOR_DISTINCTION_WORKING_NOTE_V351.md)

### How to use this template

Copy this file to the intended operator filename and replace every
`{{PLACEHOLDER}}`. Remove all authoring instructions that do not belong in the
finished operator. Do not publish a copied template merely because all visible
placeholders have been filled.

This template separates:

- **required blocks**, which every Layer-1 operator must address;
- **conditional blocks**, which are retained only when the operator needs them;
- **operator-specific blocks**, whose content and formula cannot be inherited
  from I, D, O, S or K by analogy alone.

The template does not require identical section numbering across operators.
Semantic completeness and visible boundaries matter more than cosmetic
uniformity.

The same structural questions may later inform separate templates for `Z`,
`IK`, `IK_rel` or R-family material. This file must not be copied upward as a
universal layer template: those constructs have different inputs, gates,
cardinalities and interpretation boundaries.

### Placeholder key

| Placeholder | Meaning |
| --- | --- |
| `{{X}}` | operator symbol, for example `K` |
| `{{X0}}` | static Layer-1 operator, for example `K0` |
| `{{OPERATOR_NAME}}` | observable operator name |
| `{{TARGET}}` | source-attributed target event or carrier-specific target unit |
| `{{BASIS}}` | operator-specific declared measurement basis in prose |
| `{{PROFILE}}` | versioned operator profile |
| `{{COMPONENT}}` | operator-specific component |
| `{{REF_OR_SCOPE}}` | operator-appropriate reference, scope or profile term |
| `{{SECOND_DOMAIN_NAME}}` | short name of the selected non-Human–Chatbot domain |
| `{{SECOND_DOMAIN_OPERATOR_APPLICATION}}` | bounded mapping of the canonical operator into that domain |
| `{{STABLE_OR_PROVISIONAL_SOURCE_ENTITY_ID}}` | stable source identity or an explicitly provisional observed-source identity |
| `{{SOURCE_ATTRIBUTION_STATUS}}` | declared status and provenance of the source attribution |
| `{{ESTABLISHED_EMITTER_ID_OR_OMIT}}` | emitting entity only when independently established; otherwise omit the field |
| `{{IMPLEMENTATION_BOUNDARY_AND_OPTIONAL_COMPANION_LINK}}` | method/implementation boundary plus a companion link only when one exists |
| `{{OPTIONAL_IMPLEMENTATION_COMPANION_LINK}}` | link to an adjacent implementation companion when one exists; otherwise an explicit statement that none is instantiated here |

### Required preservation rules

Every finished operator must preserve these rules:

1. One static operator value belongs to one explicitly identified target event.
2. The target event, visible context, stable or explicitly provisional source
   identity, source-attribution status and any established emitting identity
   remain distinct.
3. Sender and receiver are exchange-relative roles, not entity types.
4. Static and source-local operator views are strictly monadic.
5. A predecessor for `Delta {{X}}` comes from the same trajectory.
6. Applicability is decided before a numeric value is interpreted.
7. `not_applicable`, `not_observable`, `not_selected` and numeric `0` remain
   distinct states.
8. Comparability is established before differences or aggregations are formed.
9. `{{X}}Sigma(W)` and `{{X}}Sigma(Hangar)` remain distinct views.
10. Hangar is derived from canonical event and evaluation records; it does not
    replace them.
11. Later relational projection or comparison begins only after explicit
    dyadic pairing or an n-adic constellation map and an open numeric canonical
    complete `R0` gate under the exact required profile; `R0` itself is the
    comparability gate, and a downstream construct must match its cardinality.
12. Exactly one declared {{X}} profile fills the {{X}} coordinate of a given
    five-dimensional `Z` view.
13. An operator-specific relational diagnostic does not replace `Z`, canonical
    `IK`, `IK_rel` or an R-family result.
14. This v3.51 template records the relational boundary but activates no
    operator-specific relational comparison. Proposed post-`R0` comparison
    views and operator-only bypass routes remain v3.60 Future Work unless
    separately defined, reviewed and released.
15. Canonical coordinate order, sender-side formation and receiver-side
    reconstruction remain three distinguishable descriptions; none silently
    defines the others.
16. The preferred receiver-side `I -> D -> O -> S -> K` direction is
    recursive and profile-sensitive, not a causal formula dependency or a
    claim about hidden internal processing.
17. Repeated events retain separate event and trajectory identity. Static
    values and sequence-level recurrence, stagnation, burst or oscillation
    diagnostics must not overwrite one another.
18. A pre-agreed convention may support fast decoding; an unknown convention
    may be inferred from repeated observable regularities. Neither case merges
    source identities or creates a relational value by itself.
19. Reusable profile identity and the concrete measurement-basis instance,
    including candidate/admitted/excluded members, remain distinguishable.
20. Profile-native observations, versioned normalization, raw operands, raw
    result and display value remain different typed stages.
21. A display value never becomes a method operand or overwrites the raw
    result; its policy, precision and rounding are explicit.
22. Every window result has its own identity, exact members, status
    partitions, coverage, denominator, aggregator and aggregation order.
23. `derive_then_aggregate` and `aggregate_then_derive` are named separately;
    state/result aggregation, Delta, Delta2, path length and window difference
    do not collapse into one operation.
24. Machine-readable object, assistive-model interpretation and
    human/governance display remain linked but distinct representations.
25. Migration class and runtime-conformance status are explicit; publication
    of a reference method does not prove implementation conformance.

### Mandatory abstraction-consistency tests

Before an operator candidate can pass this template review, record an explicit
result for all five tests:

1. **Monadic-independence / removal test:** remove Entity B from the declared
   setting. `{{X}}_A(k)`, `Z_A(k)` and monadic `IK_A(k)` must remain defined
   whenever their own basis and applicability conditions are satisfied.
   Visible external context may inform the declared basis; it must not silently
   create a relational value.
2. **Role-reversal test:** Entity A may be sender in one exchange and receiver
   in another without changing its stable entity or trajectory identity.
3. **Application-substitution test:** replace Human–Chatbot with the selected
   second domain. The canonical semantic question and formula boundary must
   survive; only the domain-specific instantiation may change.
4. **Layer-dependency test:** no Layer-1 input or formula may depend on `Z`,
   `IK`, `R0`, `IK_rel` or an R-family result. Relational interpretation opens
   only at the separately declared `R0` branch.
5. **Provenance test:** entity, target event, trajectory, local trajectory
   index, exchange and reply/pairing relation remain distinguishable in prose,
   formulas, storage and derived views.

These tests also apply when later layer-specific templates are reviewed. Do
not copy this Layer-1 scaffold upward: `Z`, `IK`, `R0`, `IK_rel` and R-family
constructs require their own inputs, cardinalities, gates and interpretation
boundaries.

### Directed formation and reconstruction topologies

Layer-1 coordinates remain independently evaluable under their own bases and
profiles:

```text
Z_A(k) = (K_A(k), S_A(k), O_A(k), D_A(k), I_A(k))
```

Where process orientation is relevant, distinguish:

```text
sender-side formation:        K -> S -> O -> D -> I
receiver-side reconstruction: I -> D -> O -> S -> K
```

The first path describes how context-bound material may be structured,
grounded, transformed into a channel-appropriate form and emitted as an
observable information impulse. The second is a preferred reconstruction
direction: notice observable difference, establish distinguishability, check
available sources or reference spaces, examine structure and place the result
into context.

These process paths do not impose dependencies between the five static
operator formulas and do not claim access to internal cognition or machine
processing. An established convention may abbreviate or parallelize practical
reconstruction. Without a shared convention, failed grounding may reopen
segmentation, structural analysis, source checking and contextual hypotheses.
Record IDOSK as an iterative, inductive and recursive traversal rather than a
single irreversible pass.

For every domain example, distinguish:

- the carrier event from the `I` value attributed to that event;
- channel transformation or compression from the resulting `D` observation;
- a pre-agreed shared convention from a convention inferred by the receiver;
- practical shortcutting from `not_selected`, `not_applicable` and numeric
  values;
- communication-protocol receipt confirmation from the later Z-based `R0`
  comparability gate.

Repeated events must not be deduplicated merely because their static
information impulse relative to a baseline is low. Recurrence may remain
relevant in source-local trajectory, window and anomaly views. For Operator I,
state explicitly that event-level `I_ref`, optional `C_seq,I`, `Delta I`
and typed Sigma/Hangar patterns answer different questions.

### Optional separate implementation companion requirements

An implementation companion is not required for every operator method.
If operator-specific implementation material is needed, create or maintain it
beside the operator under the following naming convention:

```text
KSODI_Operator-<X>_<Observable-Name>_V351.md
KSODI_Operator-<X>_Implementation-Companion_V351.md
```

The canonical-method file defines the observable, measurement basis,
applicability, calculation, interpretation and permitted monadic views. Its
implementation boundary is required; a companion link is conditional on that
companion actually existing. An adjacent implementation companion may
operationalize the accepted method through storage fields, pseudocode, detector
configuration, data flow, versioning, test fixtures or architecture-specific
integration.

The companion must preserve and make recoverable, where applicable:

- observation-scope, event, target-event and context-event identifiers;
- stable or explicitly provisional `source_entity_id`, its
  `source_attribution_status` and `emitting_entity_id` only when the emitter is
  established;
- trajectory identifiers;
- local and global indices, exchange and reply/pairing identifiers;
- measurement-basis, profile, detector, carrier, segmentation, normalization
  and reference-space provenance;
- concrete measurement-basis instance plus candidate, admitted and excluded
  member identities and reasons;
- profile-native observations, transformation parameters, raw operands, raw
  result, display policy and rounding metadata;
- component masks, component values, applicability and missingness states;
- comparability decisions and same-trajectory predecessor identity;
- separate static, Delta and Delta2 window, Sigma and Hangar policies;
- window-result identity, exact members, status partitions, denominator,
  coverage, aggregator and aggregation order;
- separate machine object, assistive interpretation and governance-view refs;
- migration class, migration record and independent runtime-conformance state;
- raw-material and derived-data provenance;
- implementation/method version differences and unresolved alignment issues.

Binding rule:

> Every implemented static `{{X}}` value remains attributable to one
> identified target event and one monadic trajectory. Every source-local change
> remains anchored at one target event and recoverably references a comparable
> predecessor from the same trajectory.

The implementation companion must not redefine the operator, silently alter a
formula, introduce a carrier-specific concept into the canonical definition or
collapse entity, event, trajectory, exchange and pairing identities. If method
and implementation differ, record the mismatch and decide explicitly which
artifact changes.

A companion begins as review material. After the applicable human review and
explicit release authorization, it may be published beside the
canonical operator and linked in both directions. It must remain visibly
conditional and subordinate: no carrier-specific mapping becomes the
canonical observation object, a sixth operator or a mandatory production
stack. Repository adjacency is not publication authorization.

---

## Part B - Reader-facing finished operator skeleton

Copy the skeleton beginning with the operator title into the target file. Part A
and Part C remain template-control material and must not appear in the finished
operator.

# KSODI Operator {{X0}} - {{OPERATOR_NAME}} v3.51

Layer: KSODI Standard-Eval Layer 1. A static `{{X0}}` value belongs to one
explicitly identified, source-attributed target event. Source-local change,
acceleration and window diagnostics remain monadic Observer views. Relational
projection or comparison beyond the gate begins only after an explicit dyadic
pairing or n-adic constellation map, an open numeric canonical complete `R0`
gate under the exact required profile and a separately declared later-layer
definition with matching cardinality.

Implementation boundary: {{IMPLEMENTATION_BOUNDARY_AND_OPTIONAL_COMPANION_LINK}}

## 0. What Operator {{X}} is and what it does [required]

`{{X}}` names a broad, carrier-neutral observation-question family:

> {{ONE_SENTENCE_OPERATOR_QUESTION}}

Each declared profile instantiates this family as one bounded, testable
question. State positively what the operator family observes, then identify
which bounded profile question is used in each application or calculation.
A profile, example, detector or successful run must not silently narrow the
full operator family. Then state the most important
non-claims in plain language. Avoid using broad labels such as quality,
correctness, intelligence, truth, value or stability unless the operator
definition explicitly and narrowly requires them.

For a developer or reader who does not want to start with the formula:

{{PLAIN_LANGUAGE_EXPLANATION}}

- {{PRACTICAL_QUESTION_1}}
- {{PRACTICAL_QUESTION_2}}
- {{PRACTICAL_QUESTION_3}}

Explain what a low value may mean without treating it as failure. Explain when
no numeric value follows.

### 0.1 Minimal practical reading [required]

> {{MINIMAL_PRACTICAL_QUESTION}}

Close with one paragraph explaining what the question includes and excludes.

### 0.2 How to read this file [required]

- New readers may begin with Sections 0-2, the interpretation in Section 4 and
  the relational boundary in Section 8.
- Method reviewers should follow the complete semantic and mathematical path
  through Sections 2-9.
- Implementers should use any companion linked in Section 10 together with the
  identity, architecture and measurement-basis contracts. If no companion
  exists, the method's implementation boundary still applies.

The section order is part of the review discipline: understand the observable
question first, inspect two bounded instantiations, define the canonical
objects, then follow the calculation from static value through movement,
pattern and relational boundary.

## 1. Bounded Application Examples [required]

### 1.1 Human–Chatbot Interaction

Map the canonical objects explicitly:

```text
entity_A = human
entity_B = chatbot
target_event = one source-attributed contribution
interaction_scope = declared conversation or exchange
trajectory_A and trajectory_B remain distinguishable
```

Show in a few sentences how the operator-specific measurement basis applies
to one human or chatbot contribution:

{{HUMAN_CHATBOT_OPERATOR_APPLICATION}}

Do not introduce a merged human–chatbot state or derive relational meaning
inside Layer 1. A visible contribution by the other entity may be declared as
context or reference material where the operator permits it; it does not
become part of the target event or its source trajectory.

This example illustrates one application domain. It does not restrict KSODI
to language, LLMs, questions or answers.

### 1.2 {{SECOND_DOMAIN_NAME}}

Choose one interaction or signal domain other than Human–Chatbot. Suitable
examples may include dancers, horse–human interaction, robots, whale song,
bit-pattern or network-signal exchange, or another setting with distinguishable
sources and observable events.

Map the canonical objects explicitly:

```text
entity_A = {{SECOND_DOMAIN_ENTITY_A}}
entity_B = {{SECOND_DOMAIN_ENTITY_B}}
target_event = {{SECOND_DOMAIN_TARGET_EVENT}}
observation_unit = {{SECOND_DOMAIN_OBSERVATION_UNIT}}
measurement_basis = {{SECOND_DOMAIN_MEASUREMENT_BASIS}}
trajectory_A and trajectory_B remain distinguishable
sender and receiver remain roles of one declared exchange or transmission edge
```

Apply the same operator question and semantic boundary used in the canonical
definition:

{{SECOND_DOMAIN_OPERATOR_APPLICATION}}

State which domain knowledge, reference basis, detector or segmentation rule
is required for this instantiation. Do not claim that KSODI automatically
decodes the domain, that the two examples are equivalent or that analogy alone
licenses a shared formula. The generality belongs to the schema; the work
belongs to the domain-specific instantiation.

## 2. Canonical Definition, Scope and Boundaries [required]

Define `{{X0}}` in carrier-appropriate but architecture-agnostic language.

The definition must identify:

- the observable target;
- the operator-specific measurement basis;
- the output range or non-numeric state;
- why this is a distinct Layer-1 axis;
- the carrier-neutral semantic core that must survive application substitution;
- the boundary to the other four operators;
- the boundary to later relational layers.

`{{X0}}` does not measure:

- {{NON_GOAL_1}}
- {{NON_GOAL_2}}
- {{NON_GOAL_3}}
- hidden intention or private internal state
- general human or system worth

Use *semantically distinguishable* for the separation established through the
operators' definitions, observation targets, measurement bases and profiles.
Do not claim mathematical orthogonality unless it has been proved. Treat
functional non-redundancy as an open empirical question unless operator
ablation, overlap/correlation analysis and comparison with simpler baselines
support a narrower claim.

### 2.1 Atomic Evaluation Unit and Identity

The static evaluation target is one observable event:

```text
target_event_id = event_A_{{N}}
source_entity_id = {{STABLE_OR_PROVISIONAL_SOURCE_ENTITY_ID}}
source_attribution_status = {{SOURCE_ATTRIBUTION_STATUS}}
emitting_entity_id = {{ESTABLISHED_EMITTER_ID_OR_OMIT}}
trajectory_id = trajectory_A_{{ID}}
trajectory_index = k
context_event_ids = [{{VISIBLE_CONTEXT_IDS}}]
operator_profile_id = {{PROFILE_ID}}
```

Generic notation:

```text
{{X}}_A(k | {{BASIS}}, p_{{X}})
```

`{{BASIS}}` is an explanatory placeholder in this template. Replace it with
the operator's actual basis and notation. Do not introduce a new canonical
symbol merely to make operator files look alike.

The canonical definition must distinguish the semantic identities of the
observation scope, event, target event, visible context, emitting entity,
trajectory, local and global order, applicable pairing metadata, operator
profile and measurement basis. Concrete storage-field mappings belong in the
implementation-oriented section.

Canonical boundary:

> Context may be shared; the evaluation target and source trajectory must
> remain explicit.

#### 2.1.1 Canonical Index Discipline

Keep event-stream, trajectory-local and relational order distinguishable:

```text
n        = global event index in the observable event stream
k_A      = local position inside trajectory A
k_B      = local position inside trajectory B
j        = declared relational exchange or paired-evaluation index

pi(j) = (k_A(j), k_B(j))
```

Compact monadic formulas may use `k` when the trajectory identity is already
explicit. A finished operator file must state that its predecessor is local to
that same trajectory.

The symbol `t` may be retained only as a declared timestamp, implementation
step or legacy paired-evaluation symbol whose mapping to `n`, `k_A`,
`k_B` or `j` is explicit. It must not silently create a common predecessor,
synchronous position or mixed trajectory across distinguishable entities.

### 2.2 Static and source-local operator views are strictly monadic

The static Layer-1 `{{X}}` value and its source-local trajectory views are
strictly monadic. Each value belongs to one identified target event attributed
to one entity and one declared trajectory under one declared `{{PROFILE}}`.

```text
{{X}}_A(k_A | {{REF_OR_SCOPE}}, p_{{X}})
{{X}}_B(k_B | {{REF_OR_SCOPE}}, p_{{X}})
```

These values belong to distinguishable trajectories. Shared conversation,
room, timestamp, task, exchange or environment does not merge them and does
not by itself establish a relational measurement.

After an explicit dyadic pairing or n-adic constellation map and an open
numeric canonical complete `R0` gate under the exact required profile, an
operator-specific relational comparison could be specified as a separate
later-layer diagnostic with matching cardinality. This v3.51 template records
that boundary but does not activate such a comparison. A proposed view belongs
to v3.60 Future Work, does not turn the Layer-1 operator itself into a
relational operator and must not be reported as complete `Z`, canonical
`IK_rel` or an R-family result.

A specialized operator-only relational path that bypasses complete `Z` is not
defined by this v3.51 template. It is likewise v3.60 Future Work and requires
its own pairing, applicability and comparability gate.

### 2.3 Semantic Distinctness and Symbol Discipline

| Operator | Measures | Difference from {{X0}} |
| --- | --- | --- |
| `K0` | context completeness | {{BOUNDARY_TO_K}} |
| `S0` | structural coherence | {{BOUNDARY_TO_S}} |
| `O0` | visible grounding and traceability | {{BOUNDARY_TO_O}} |
| `D0` | signal detectability and reconstructability | {{BOUNDARY_TO_D}} |
| `I0` | information impulse | {{BOUNDARY_TO_I}} |

Remove the self-row or identify it clearly in the finished table.

Reserve `R`-prefixed notation for the relational / resonance family. Check all
component symbols against the other operator names, `Z`, `IK`, Sigma, Hangar
and active R-family notation.

### 2.4 Coordinate order and directed process topologies [required boundary]

State whether this operator is being discussed as:

1. one independently evaluated coordinate of `Z_A(k)`;
2. one question inside the sender-side formation path
   `K -> S -> O -> D -> I`; or
3. one question inside the receiver-side preferred reconstruction direction
   `I -> D -> O -> S -> K`.

The process position must not become an undeclared input to the static formula.
Sender and receiver remain exchange-relative roles. Under an established
convention, practical reconstruction may be abbreviated or parallelized;
without one, IDOSK may recur through segmentation, source checking, structural
hypotheses and context until reconstruction stabilizes or remains unresolved.

Use a Morse, signal, smoke, bit-pattern or comparable carrier example where it
clarifies the distinction. Do not identify compression with `D`, the emitted
carrier with `I`, or protocol acknowledgement with `R0`.

## 3. Measurement Basis, Profiles and Applicability [required]

### 3.1 Declared measurement basis

Describe exactly what fills this operator:

```text
{{BASIS_DEFINITION}}
```

State what must not be inserted silently, especially:

- another entity's event or state;
- undeclared history or whole-conversation aggregation;
- hidden sources or hidden model state;
- Hangar expectations;
- inferred intention;
- another operator's measurement basis.

Keep the reusable profile and concrete basis instance separate:

```text
operator_profile_id and version
measurement_basis_instance_id and version
candidate_basis_member_ids
admitted_basis_member_ids
excluded_basis_member_ids and reasons
```

Where native evidence is normalized, record the complete route:

```text
profile_native_observation and evidence refs
  -> versioned normalization / transformation and known loss
  -> raw operands
  -> raw method result or typed non-numeric result
  -> separately versioned display value, if any
```

The display value is never an operand and never overwrites the raw result.

### 3.2 Versioned profile

```text
p_{{X}} = ({{PROFILE_COMPONENTS}})
```

Record every constitutive detector, carrier, segmentation, normalization,
reference, threshold, weight and masking dependency under an
operator-appropriate generic category. Architecture-specific mappings such as
embedding or retrieval configuration belong in the conditional implementation
section.

### 3.3 Applicability before numeric interpretation

Define the conditions under which numeric evaluation is open:

```text
app_{{X}},A(k) = {{APPLICABILITY_RULE}}
```

Preserve:

```text
not_applicable != not_observable
not_applicable != not_selected
not_applicable != 0
```

<!-- Conditional: use a named companion gate only when the operator genuinely
requires one. O uses the Source-Need Gate; that does not make a companion gate
mandatory for every operator. -->

### 3.4 Conditional companion gate

{{COMPANION_GATE_DEFINITION_AND_STATE_MODEL}}

## 4. Static Components, Calculation and Interpretation [required]

### 4.1 Why the formula matters

Use this sentence unless an operator-specific reason requires a more precise
variant:

> The mathematical form does not create the semantic boundary. The semantic
> boundary creates the valid formula.

List the invariants that make this operator's formula legitimate:

- target-event and emitting-entity identity;
- trajectory-local predecessor discipline;
- declared and versioned measurement basis and profile;
- component applicability and active mask;
- reference, detector, carrier or scope visibility where relevant;
- no silent cross-entity subtraction;
- no silent conversion of missingness to zero.

### 4.2 Components [required when the formula is component-based]

Define every component separately. Each component definition must include:

- semantic question;
- observable input;
- formula or detector rule;
- range;
- applicability rule;
- profile and version dependencies;
- non-goals and collision boundaries.

#### 4.2.1 {{COMPONENT_1_NAME}} - `{{COMPONENT_1_SYMBOL}}`

```text
{{COMPONENT_1_FORMULA}}
```

If the component is not applicable:

```text
{{COMPONENT_1_SYMBOL}} = not_applicable
```

#### 4.2.2 {{COMPONENT_2_NAME}} - `{{COMPONENT_2_SYMBOL}}`

```text
{{COMPONENT_2_FORMULA}}
```

<!-- Add further components only when semantically necessary. -->

### 4.3 Static Formula and Profile Selection

Choose the formula pattern that belongs to this operator. Do not retain all
patterns merely because the template lists them.

#### Pattern A - one static profile

```text
{{X0}}_A(k | p_{{X}}) = {{STATIC_FORMULA}}
```

#### Pattern B - applicability-aware component set

```text
{{X}}_active_A(k)
= {C_i,A(k) | C_i,A(k) is applicable under p_{{X}}}

{{X0}}_A(k | p_{{X}})
= clip(
    (sum_i w_i * C_i,A(k)) / (sum_i w_i),
    0, 1
  )
```

If no mandatory or permitted component is applicable:

```text
{{X0}}_A(k | p_{{X}}) = not_applicable
```

State whether renormalization over applicable components is allowed. A changed
active component set is a profile or comparability concern, not an invisible
implementation detail.

#### Pattern C - alternative baseline or numeric profiles

```text
p_{{X}} in {{{PROFILE_A}}, {{PROFILE_B}}, {{OPTIONAL_COMBINED_PROFILE}}}
```

Alternative profiles answer different questions. Store them separately. A
combined profile must be explicitly named, versioned and recoverable; it is
never the silent default.

Exactly one declared profile fills the {{X}} coordinate in a given `Z` view.
Multiple stored profiles create a richer feature record or multiple declared Z
projections, not an extra canonical Z dimension.

#### Pattern D - minimal and extended formula

```text
{{X0}}_A(k | p_min) = {{MINIMAL_FORMULA}}
{{X0}}_ext,A(k | p_ext) = {{EXTENDED_FORMULA}}
```

Optional penalties or precision components are disabled by default unless the
profile explicitly activates them. Minimal and extended values are not naively
interchangeable.

### 4.4 Interpretation

| Value or state | Operator-specific meaning |
| --- | --- |
| high | {{HIGH_INTERPRETATION}} |
| medium | {{MEDIUM_INTERPRETATION}} |
| low | {{LOW_INTERPRETATION_WITHOUT_FAILURE_CLAIM}} |
| `not_observable` | required or expected basis or evidence cannot be inspected under the declared Observer/profile boundary |
| `not_applicable` | {{APPLICABILITY_INTERPRETATION}} |
| `not_selected` | the operator was electively omitted under the declared profile |

Use numeric thresholds only when the declared profile defines and justifies
them. Never import one operator's thresholds into another.

## 5. Edge Cases, Fairness, Privacy or Retention [conditional]

Retain only the subsections that the operator needs.

### 5.1 Edge cases

- {{EDGE_CASE_AND_REQUIRED_STATE_1}}
- {{EDGE_CASE_AND_REQUIRED_STATE_2}}

### 5.2 Fairness or setup boundary

Separate unavailable setup, reference material, visibility or detector support
from an observed low operator value.

### 5.3 Privacy and retention boundary

State the deployment-specific retention and access policy for raw and derived
data. Embeddings, vectors, scores and trajectory summaries may also contain
sensitive or personal information. Do not prescribe a repository-wide
retention period inside one operator.

Derived does not mean anonymous, non-sensitive or automatically safe to retain.
Assess re-identification risk, linkability, inference risk, access scope and
approved retention separately for raw material, identifiers, embeddings,
scores, deltas, distributions and other derived records. Data minimization and
the applicable consent, governance and deletion rules continue to apply.

## 6. Comparability and Source-Local Dynamics [required]

### 6.1 Comparability Contract

Two `{{X}}` values are directly comparable only when all constitutive
conditions are equal or explicitly mapped as compatible:

- same target-unit and source-attribution rule;
- same operator and numeric profile;
- same measurement-basis construction;
- same active component mask;
- same detector, carrier, segmentation and normalization where applicable;
- same operator-specific reference or evidence-space construction where
  applicable;
- same thresholds and weights;
- same applicability and missingness policy;
- same Observer and operator version;
- same window and aggregation policy for Sigma views.

Operator-specific additions:

- {{COMPARABILITY_REQUIREMENT_1}}
- {{COMPARABILITY_REQUIREMENT_2}}

If compatibility is not established, the comparison or delta is
`not_applicable`; profile change is not ordinary movement.

### 6.2 Source-Local Dynamics and Separate Diagnostics

For one entity A, one trajectory and one compatible profile:

```text
{{X}}_A(k) = {{X0}}_A(k | {{BASIS}}, p_{{X}})

Delta {{X}}_A(k)
= {{X}}_A(k) - {{X}}_A(k-1)

Delta2 {{X}}_A(k)
= Delta {{X}}_A(k) - Delta {{X}}_A(k-1)
```

These values are defined only when the participating evaluations are
applicable and comparable. Otherwise:

```text
Delta {{X}}_A(k) = not_applicable
Delta2 {{X}}_A(k) = not_applicable
```

There is no implicit cross-entity monadic difference:

```text
Delta {{X}}_AB = {{X}}_B - {{X}}_A  [not defined as a Layer-1 monadic delta]
```

#### 6.2.1 Conditional companion diagnostics

List optional improvement, persistence, reference-drift, historical-context or
uncertainty diagnostics here. Each must remain separately named, stored and
interpreted. It must not silently modify `{{X0}}`.

```text
{{SEPARATE_DIAGNOSTIC}} = {{DIAGNOSTIC_FORMULA_OR_STATE}}
```

## 7. Sigma and Sigma(Hangar) [required]

Before writing an aggregate, define the derived window object itself:

```text
window_result_id
window_profile_id and version
window_kind and boundary rule
exact member identities and ordering
included/excluded/status partitions
coverage and denominator definitions
aggregator_id and version
aggregation_order
```

Choose and name one order:

```text
derive_then_aggregate
aggregate_then_derive
```

Explain why that order answers the declared question. The v3.51 reference
policy is `strict_integrity_v351`. A future PPWA-bounded profile remains
separately named and may not erase excluded partitions or convert them to zero.

Define a type-appropriate applicable subset of a declared source-local window
for every selected view:

```text
W_app_{{X0}},A
= {k in W | {{X}}_A(k) is applicable under the static aggregation profile}

W_app_Delta{{X}},A
= {k in W | Delta {{X}}_A(k) is applicable and comparable}

W_app_Delta2{{X}},A
= {k in W | Delta2 {{X}}_A(k) is applicable and comparable}
```

Static values, first differences and second differences are different data
types. Aggregate each selected type separately:

```text
{{STATIC_SIGMA_VIEW}}
= {{STATIC_AGGREGATION}}({{{X}}_A(k) | k in W_app_{{X0}},A})

{{DELTA_SIGMA_VIEW}}
= {{DELTA_AGGREGATION}}({Delta {{X}}_A(k) | k in W_app_Delta{{X}},A})

{{DELTA2_SIGMA_VIEW}}
= {{DELTA2_AGGREGATION}}({Delta2 {{X}}_A(k) | k in W_app_Delta2{{X}},A})
```

Apply the same type separation to derived Hangar distribution views:

```text
{{STATIC_HANGAR_VIEW}}
= distribution_view({{{X}}_A(k) | k in W_app_{{X0}},A})

{{DELTA_HANGAR_VIEW}}
= distribution_view({Delta {{X}}_A(k) | k in W_app_Delta{{X}},A})

{{DELTA2_HANGAR_VIEW}}
= distribution_view({Delta2 {{X}}_A(k) | k in W_app_Delta2{{X}},A})
```

These placeholders impose type separation, not universal new symbols. Choose
and define the final notation, aggregation function and output type in the
operator-specific review. A structured record may carry all selected views;
it must not collapse them into one untyped scalar.

Required boundary:

- `{{X}}Sigma_A(W)` is a window aggregation inside the operator layer;
- `{{X}}Sigma_A(Hangar)` is a derived distribution or comparison view;
- static, Delta and Delta2 aggregates retain separate types, applicability
  sets and provenance;
- side-by-side display of A and B does not create a dyadic metric;
- canonical event and evaluation records remain authoritative.

Choose the final operator-specific Sigma notation deliberately. Do not perform
a mechanical repository-wide symbol replacement for cosmetic consistency.

## 8. Relational Boundary [required]

`{{X0}}`, `Delta {{X}}`, `Delta2 {{X}}`, `{{X}}Sigma(W)` and
`{{X}}Sigma(Hangar)` describe monadic operator behavior.

Relational comparison requires:

1. distinguishable source trajectories;
2. an explicit dyadic pairing or n-adic constellation map;
3. compatible operator profiles and applicable values;
4. an open numeric canonical complete `R0` gate under the exact required
   profile;
5. a separately declared later-layer construct with matching cardinality.

The Layer-1 operator does not define coupling, resonance, mutual understanding
or relational quality.

This v3.51 section records where relational work could begin but does not
define or activate an operator-specific relational comparison. A proposed
post-`R0` comparison remains a partial v3.60 Future Work diagnostic.

A route that uses one operator to bypass `Z`, canonical `IK` or `IK_rel` and
then enters the R-family as if the complete relational construction had been
performed is likewise not active v3.51 method. Such an operator-only
relational bypass remains v3.60 Future Work and requires its own definition,
applicability policy, comparability gate, review and release.

## 9. Formal Summary and Variable Reference [required]

### 9.1 Compact Formula Block

Provide one self-contained block containing only the active formulas and their
applicability conditions. It must be possible to read this block without
accidentally activating optional profiles or companion diagnostics.

```text
{{ACTIVE_STATIC_FORMULA}}

{{ACTIVE_APPLICABILITY_RULE}}

{{ACTIVE_PROFILE_SELECTION_RULE}}

{{ACTIVE_COMPARABILITY_GATE}}

{{ACTIVE_DELTA_AND_DELTA2_RULES}}

{{ACTIVE_SIGMA_AND_HANGAR_RULES}}

Separate companion diagnostics:
{{ACTIVE_SEPARATE_DIAGNOSTICS}}
```

### 9.2 Variable Reference

| Variable | Semantic role |
| --- | --- |
| `{{TARGET_SYMBOL}}` | source-attributed target event or observable unit |
| `p_{{X}}` | versioned operator profile |
| `{{BASIS_SYMBOL}}` | operator-specific declared measurement basis |
| `{{COMPONENT_SYMBOL}}` | operator-specific component |
| `{{X0}}_A(k)` | static operator value for entity A's target event |
| `Delta {{X}}_A(k)` | first source-local difference under comparable conditions |
| `Delta2 {{X}}_A(k)` | second source-local difference under comparable conditions |
| `W_app_{{X0}},A` | applicable subset for static operator values |
| `W_app_Delta{{X}},A` | applicable and comparable subset for first differences |
| `W_app_Delta2{{X}},A` | applicable and comparable subset for second differences |
| `{{STATIC_SIGMA_VIEW}}` | typed source-local aggregation of static values |
| `{{DELTA_SIGMA_VIEW}}` | typed source-local aggregation of first differences |
| `{{DELTA2_SIGMA_VIEW}}` | typed source-local aggregation of second differences |
| `{{STATIC_HANGAR_VIEW}}` | derived distribution view of static values |
| `{{DELTA_HANGAR_VIEW}}` | derived distribution view of first differences |
| `{{DELTA2_HANGAR_VIEW}}` | derived distribution view of second differences |
| `not_observable` | required or expected basis or evidence cannot be inspected under the declared Observer/profile boundary; never numeric zero |
| `not_applicable` | no valid operator-domain basis exists for the declared question; never numeric zero |
| `not_selected` | the operator was electively omitted under the declared profile; never numeric zero |

Add every symbol used in the active formula. Remove unused placeholders.

## 10. Implementation Boundary and Optional Companion [required boundary]

The canonical method ends with the formal summary in Section 9.
Implementation-specific storage fields, pseudocode, detector mappings, data
flow and architecture configuration do not belong in this file.

- Adjacent companion, if present: {{OPTIONAL_IMPLEMENTATION_COMPANION_LINK}}

If no companion exists, state that no operator-specific implementation
companion is instantiated here. This does not make the method incomplete.

Where linked, a companion may operationalize this operator but must not
redefine its semantic question, measurement basis, applicability, formula,
source identity or layer boundary. Any mismatch must remain visible until
reviewed.

Public availability of a companion is governed separately from the method
definition. Whether internally reviewed or public, its conditional implementation profile
remains subordinate to this method file.

Where views are emitted, keep three channels distinct: the machine-readable
evaluation object, an attributed assistive-model interpretation over governed
inputs, and a human/governance display. Require a reverse route from each
derived view to its raw result, basis instance, profile, target identity and
evidence references. Classify imported records as `v351_conformant`,
`legacy_reconstructible`, `legacy_partially_reconstructible` or
`legacy_noncomparable`; keep `reconstruction_pending` as workflow state rather
than compatibility class. State independent runtime conformance separately.

---

## Part C - Final authoring check

Template-control section: complete this checklist before review acceptance, then
remove it and all remaining authoring instructions from the finished operator
file.

Before treating the copied file as a review candidate, confirm:

- [ ] Every placeholder and authoring instruction has been removed.
- [ ] The canonical definition is architecture-agnostic.
- [ ] Human–Chatbot terminology appears only in the bounded application
      example or an explicitly conditional implementation mapping.
- [ ] One bounded second-domain example maps from the same canonical
      definition and declares its own observation unit, measurement basis and
      interpretation discipline.
- [ ] Neither example is presented as method canon, domain equivalence,
      automatic decoding or empirical validation.
- [ ] The method file contains a clear implementation boundary and links an
      adjacent companion only when that companion exists.
- [ ] If a public companion exists, it has a separate recorded review and
      explicit release decision; its carrier-specific profile is not presented
      as method canon or a mandatory production stack.
- [ ] Any implementation companion does not redefine the operator.
- [ ] The operator defines one broad carrier-neutral observation-question family.
- [ ] Every concrete profile instance asks a bounded, testable observable question.
- [ ] No profile, example, detector or implementation mapping is presented as the exhaustive operator meaning.
- [ ] No broad quality, truth or human-value claim was introduced.
- [ ] Target, context, source and trajectory identities remain distinct.
- [ ] The measurement basis is operator-specific and declared.
- [ ] Reusable profile identity and concrete basis-instance/member identities
      remain distinguishable.
- [ ] Native observation, transformation, raw operands/result and display
      remain distinct typed stages.
- [ ] Display policy, precision and rounding are explicit; display never
      becomes an operand.
- [ ] Applicability precedes numeric interpretation.
- [ ] Alternative profiles remain separately recoverable.
- [ ] Exactly one profile fills the operator's Z coordinate per view.
- [ ] Comparability precedes Delta, Delta2 and aggregation.
- [ ] Sigma(W) and Sigma(Hangar) remain distinct, and static, Delta and Delta2
      views are aggregated as separate types.
- [ ] Every derived window has its own identity, exact members, partitions,
      coverage, denominator, aggregator and named aggregation order.
- [ ] `derive_then_aggregate` and `aggregate_then_derive` have not been
      silently interchanged.
- [ ] Machine, assistive-model and human/governance views remain linked but
      distinct, with a reverse route to evidence.
- [ ] Migration class and independent runtime-conformance status are explicit.
- [ ] Derived data is not described as anonymous or privacy-neutral merely
      because it is derived.
- [ ] Companion diagnostics do not alter the static operator silently.
- [ ] The monadic-independence / removal test is passed explicitly.
- [ ] The exchange-relative role-reversal test is passed explicitly.
- [ ] The application-substitution test is passed explicitly.
- [ ] The upstream/downstream layer-dependency test is passed explicitly.
- [ ] The provenance test keeps entity, event, trajectory, index, exchange and
      reply/pairing identities distinguishable.
- [ ] Global event index `n`, local trajectory indices `k_A` / `k_B`,
      relational pairing index `j` and any retained `t` are explicitly
      distinguished or mapped.
- [ ] Canonical coordinate order is not presented as a causal calculation
      chain.
- [ ] Sender-side KSODI and receiver-side IDOSK are marked as role-relative
      process topologies, not formula dependencies or hidden-state claims.
- [ ] IDOSK is described as a preferred recursive reconstruction direction,
      with convention-dependent shortcuts kept distinct from missingness.
- [ ] Repeated events remain attributable; static information impulse and
      sequence-level recurrence diagnostics do not overwrite one another.
- [ ] Compression is not equated with D, the carrier is not equated with I and
      protocol acknowledgement is not equated with R0.
- [ ] Relational claims remain after an explicit pairing/constellation map and
      an open numeric canonical complete R0 gate under the exact required
      profile, match the admitted cardinality and remain outside Layer 1.
- [ ] Compact formulas and variable references match the prose.
- [ ] The file has been checked against I, D, O and S without copying their
      operator-specific semantics.
- [ ] K-specific context rules have been reviewed before using this scaffold
      for Operator K.
