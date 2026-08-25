# KSODI Operator I0 - Observable Information Impulse v3.50

Status: public v3.50 reference release, revised 2026-08-19 and clarified by
identity, editorial and typed-missingness errata on 2026-08-25. This file is
the current public method definition for Operator I. It remains open to
documented review and later versioned refinement.

Layer: KSODI Standard-Eval Layer 1. A static `I0` value belongs to one explicitly identified, source-attributed target event. Source-local change, acceleration and window diagnostics remain monadic Observer views. Relational projection or comparison beyond the gate begins only after explicit pairing, an open numeric canonical complete `R0` gate under the exact required profile and a separately declared later-layer definition.

Implementation boundary: read the public [KSODI Implementation Guardrails](../../IMPLEMENTATION_GUARDRAILS.md) and the adjacent [Operator I Implementation Companion](./KSODI_Operator-I_Implementation-Companion_V350.md). The companion is conditional implementation guidance; this method file remains authoritative.

## 0. What Operator I is and what it does

`I` answers a very narrow question: does this contribution create an observable information difference relative to the baseline that was declared for this evaluation?

This is not a claim about general correctness, universal validity,
intelligence, value, quality, morality or human worth. It is not a score for
“how deep” someone is. It is a measurement of observable informational
movement.

For a developer or reader who does not want to start with the formula: think of `I` as a way to ask whether a contribution creates an observable information difference relative to the baseline declared for this evaluation.

- Does it add new information?
- Does it compress or redirect existing information?
- Does it shift the observable information relation to the declared baseline?

If the answer is “not really,” `I` may stay low even when the contribution is perfectly fine, useful, polite or intentional. A low value is not a failure. It can also mean stability, confirmation, repair or deliberate anchoring.

### 0.1 Strictly monadic; relational comparisons remain separate

Operator I is strictly monadic. It is calculated for one identified target
event attributed to one entity and one declared trajectory, relative to a
declared I baseline.

This is the central validity rule:

- a contribution from entity `A` is evaluated as a contribution of `A`
- a contribution from entity `B` is evaluated as a contribution of `B`
- they remain separate monadic trajectories when a later relational rule
  declares a pair or exchange

Shared context, time, task or environment does not merge source trajectories.
The formulas below therefore keep the target event and every monadic
predecessor inside the same declared trajectory.

After an open numeric canonical complete `R0` gate under the exact required
profile, a separately defined relational comparison of
distinguishable I trajectories could be specified as a later-layer diagnostic.
No such operator-specific relational I view is active in this v3.50 operator
file. It belongs to v3.60 Future Work, does not turn Operator I into a dyadic
operator and must not be reported as canonical `IK_rel` or an R-family result.

Any operator-only I path that bypasses complete `Z` requires its own pairing,
applicability and comparability contract. It is likewise v3.60 Future Work,
not an implicit shortcut in the v3.50 method line.

### 0.2 Why the formula matters

The mathematical form does not create the semantic boundary. The semantic boundary creates the valid formula.

The formula is only correct if it respects these rules:

- the target event remains attached to one stable or explicitly provisional
  `source_entity_id`, one `source_attribution_status` and one `trajectory_id`;
  `emitting_entity_id` is retained separately only when established
- local movement is measured only against the same trajectory's predecessor
- a cross-entity comparison is not silently treated as a monadic difference
- `not_applicable` is not silently encoded as `0`

This is why the file separates the static reference-relative I value from
source-local trajectory diagnostics and preserves source identity, trajectory
identity and applicability status in storage and implementation.

### 0.3 Minimal practical reading

In plain terms, Operator I helps answer:

> “Compared to the declared information baseline, did this contribution create a visible information difference?”

That is the semantic core of the static operator. Source-local `Delta I` and an
optional direct predecessor diagnostic answer later trajectory questions
without becoming alternative I coordinates or dyadic relations.
### 0.4 How to read this file

- New readers may begin with Sections 0-2, the interpretation in Section 4 and the relational boundary in Section 8.
- Method reviewers should follow the complete semantic and mathematical path through Sections 2-9.
- Implementers should read Section 10 and the linked public implementation guardrails without treating implementation choices as method definitions.

The order is deliberate: observable question, two bounded examples, identity and topology, basis and applicability, calculation, movement, pattern and only then the relational boundary.

## 1. Bounded Application Examples

### 1.1 Human–Chatbot Interaction

```text
entity_A = human
entity_B = chatbot
target_event = one source-attributed contribution
interaction_scope = declared conversation or exchange
trajectory_A and trajectory_B remain distinguishable
```

For one human contribution, Operator I compares that contribution with the I
baseline selected and admitted under its own profile. A later chatbot response
is evaluated as a separate target event on the chatbot trajectory, even when
the two events share a conversation or exchange identifier. The human event
may be visible reference or context material for the chatbot evaluation where
the declared I profile permits it; it does not become part of the chatbot
event.

This example does not create a merged Human–Chatbot state and does not derive
relational meaning inside Layer 1. It illustrates one application domain and
does not restrict KSODI or Operator I to language, prompts, questions, answers
or LLMs.
### 1.2 Unknown Morse-like Signal

```text
observed_source_A = stable or explicitly provisional signal source
entity_B = receiving or observing system
target_event = one signal burst attributed to observed_source_A
observation_unit = one declared segmented burst or symbol group
measurement_basis = a visible, admissible baseline of prior signals, known code patterns or declared reference material
trajectory_A and trajectory_B remain distinguishable
sender and receiver remain roles of one declared transmission edge
```

Operator I can evaluate the single signal event without a second trajectory. It asks whether the burst creates observable information difference relative to the declared baseline. Repetition may keep static I low while remaining security-relevant as a recurrence pattern in source-local sequence, window or Hangar views. A second trajectory is required only for a later relational question, such as whether a distinguishable receiver answers in a paired pattern after an open numeric canonical complete `R0` gate under the exact required profile.

This instantiation requires a declared detector and segmentation rule before the burst can be treated as an event, plus a carrier-appropriate representation, information-unit rule and baseline. I does not automatically discover Morse code, decode an unknown convention or prove meaning. Detectability and reconstructability belong to D; information difference relative to a baseline belongs to I. The example is a bounded instantiation, not empirical validation or domain equivalence.

## 2. Canonical Definition, Scope and Boundaries

`I0` is a strictly monadic Layer-1 operator. It is legitimate as a separately
observable axis because it asks a narrower question than `K`, `S`, `O` or
`D`:

> Does this contribution add, compress or redirect observable information relative to the baseline selected for this evaluation?

`I0` is drift-neutral and non-normative. It does not measure general
correctness, universal validity, usefulness, creativity, semantic correctness,
compliance, depth, intelligence or human value. A low value may indicate
repetition, confirmation, repair, stabilization or deliberate anchoring. A
high value may indicate novelty or redirection without implying that the
contribution is useful or correct.

Operator I identifies an observable information difference relative to its
declared baseline. It does not determine whether a receiving entity noticed,
processed or understood that difference. Detectability, segmentation and
reconstructability belong to Operator D under its own declared profile. Any
directional reconstruction order is therefore an application-level
explanatory view, not an I measurement and not a forced numerical calculation
order.

The canonical static value is the reference-relative profile `I_ref`. In this
file, `I_A(k_A)` denotes that static value unless a diagnostic is explicitly
named:

```text
I_A(k_A) := I_ref,A(k_A)
```

**Semantic reading.** This assignment declares which reviewed static I
profile fills the single I coordinate of `Z_A(k_A)`. It does not create a
second formula or an additional dimension.

A direct comparison between `e_A(k_A)` and its same-trajectory predecessor may
be useful for fine-grained investigation. It is defined below as
`C_seq,I,A(k_A)`, an optional monadic diagnostic. It is not a second I profile,
does not fill the I coordinate of `Z`, and is not the same operation as
`Delta I_A(k_A)`, which compares already calculated static I values.

### 2.1 Atomic Evaluation Unit and Identity

The static evaluation target is one event attributed to one stable or
explicitly provisional source along one declared trajectory. A confirmed
emitting entity is recorded separately only when established. Where several
entities or observed sources are present, their trajectories remain
distinguishable.

Their events may share an interaction space but remain two source-attributed
monadic trajectories:

```text
T_A = (e_A(1), e_A(2), ..., e_A(k_A))
T_B = (e_B(1), e_B(2), ..., e_B(k_B))
```

Two corresponding events may share a declared observation or exchange scope.
They do not share target-event, source-attribution, emitting-entity,
trajectory or local-position identity.

The canonical evaluation identity distinguishes at least:

- observation or interaction scope;
- target event;
- stable or explicitly provisional source identity;
- source-attribution status;
- emitting entity, if established;
- source trajectory and local trajectory position;
- visible context events;
- I measurement basis and profile;
- representation profile;
- applicability state.

The context may be shared; the evaluated object must remain unique.

An event from another entity may be admitted as visible baseline material
under the declared profile. It does not become part of the target event or its
source trajectory. Distinguishable events must not be aggregated into one I
value or one Z state before monadic state formation. Concrete storage-field
mappings belong to separate implementation guidance.

The public implementation boundary for preserving these identities is described
in the [KSODI Implementation Guardrails](../../IMPLEMENTATION_GUARDRAILS.md).
#### 2.1.1 Canonical Index Discipline

```text
n   = global event index in the observable event stream
k_A = local position inside trajectory A
k_B = local position inside trajectory B
j   = declared relational exchange or paired-evaluation index

pi(j) = (k_A(j), k_B(j))
```

Every predecessor below is local to the same declared trajectory. A timestamp `t` may be stored only with an explicit mapping; it must not silently imply a shared predecessor or synchronous position across entities.

### 2.2 Static and Source-local I Views are Strictly Monadic

`I_A(k_A | Ref_A, p_I)` and `I_B(k_B | Ref_B, p_I)` remain distinguishable even inside one interaction. Shared context does not merge them. `C_seq,I`, deltas, Sigma and Hangar remain source-local.
### 2.3 Semantic Distinctness and Symbol Discipline

| Operator | Narrow observable question | Boundary to I0 |
| --- | --- | --- |
| `K0` | context completeness | not information impulse |
| `S0` | structural coherence | not information impulse |
| `O0` | visible grounding and traceability | its evidence space is not automatically the I baseline |
| `D0` | discernibility and reconstruction support | D evaluates the carrier conditions of an admitted signal; it does not replace I's reference-relative information question |

Mathematical symbols are declared shorthand for precisely specified semantic objects and operations. KSODI may choose names such as `I_ref`, `J_ref` or `C_seq,I`; mathematics does not prescribe those names. Legitimacy comes from an explicit semantic question, domain, range, applicability rule, versioned profile and reproducible calculation. Familiar constructions do not validate a new application automatically. Method-specific notation does not make a construction arbitrary, exotic or sophisticated by itself.

Reserve `R`-prefixed notation for the relational and resonance family.
### 2.4 Coordinate Order and Directed Process Topologies

`Z_A(k_A) = (K_A, S_A, O_A, D_A, I_A)` is coordinate order, not a causal calculation chain.

```text
sender-side formation:              K -> S -> O -> D -> I
receiver-side preferred direction:  I -> D -> O -> S -> K
```

Sender and receiver are exchange-relative roles. Under an established convention, reconstruction may be abbreviated or parallelized. Without one, IDOSK may recur through signal recognition, source checking, structural hypotheses and context until reconstruction stabilizes or remains unresolved. Neither topology is an undeclared input to static I or a claim about hidden cognition.

Compression is not D. The emitted carrier is not I. Protocol acknowledgement is not `R0`.

## 3. Measurement Basis, Profiles and Applicability

### 3.1 Declared I Measurement Basis

For target event `e_A(k_A)`, distinguish visible candidate material from the admitted baseline:

```text
V_A(k_A) := visible candidate material for the declared I evaluation

Ref_A(k_A | p_I)
:= {x in V_A(k_A) |
    x is selected by p_I
    and x is admissible
    and x is visible to the evaluator}
```

**Semantic reading.** `V_A(k_A)` states what the evaluator could consider. `Ref_A(k_A | p_I)` states what the declared I profile actually permits into the baseline. The set-builder form requires selection, admissibility and visibility together. Visible but undeclared material cannot enter silently.

The baseline may include attributable material outside trajectory A when the profile permits it. That changes the measurement basis, not the monadic identity of the target event. The I baseline and the O evidence space may overlap but are not interchangeable.

For readability below, `Ref_A(k_A)` abbreviates `Ref_A(k_A | p_I)` under the
declared profile. The abbreviation never removes the profile dependency.

#### 3.1.1 Retrieval-result typing where retrieval is used

Retrieval is one possible reference operation. It is not communication itself
and is not required by every I profile. For a retrieval-backed profile, retain
the operation result as a typed state:

```text
ret_status,A(k_A) in {
  missing,
  not_requested,
  unavailable,
  empty,
  inadmissible,
  admissible_available
}
```

| State | Meaning |
| --- | --- |
| `missing` | the retrieval record or its provenance is absent, so the operation state cannot be reconstructed |
| `not_requested` | the declared retrieval operation was not invoked |
| `unavailable` | retrieval was required or requested, but the operation, channel or result was unavailable |
| `empty` | a completed retrieval operation returned no candidate elements |
| `inadmissible` | candidates were returned, but none may enter `Ref_A(k_A)` under the declared profile |
| `admissible_available` | at least one returned element is selected, admissible, visible and applicable |

`RET_A(k_A) = ∅` (written `empty` in the plain-text state labels) is the
result of a completed reference operation, not a communication-free state. Missing, not-requested, unavailable, empty,
inadmissible and admissible-available retrieval outcomes must not collapse into
one generic no-retrieval state. A reference-dependent information value must not
be inferred silently as numeric zero from any of them.

For profiles that require retrieval:

```text
retrieval_basis_ok,A(k_A)
:= ret_status,A(k_A) = admissible_available
```

For a profile whose declared baseline is constructed without retrieval,
`retrieval_basis_ok,A(k_A) := true`; the ordinary selection, admissibility,
visibility and representation gates still apply.

A non-empty raw retrieval set can still yield an empty admitted baseline when
all candidates are inadmissible. Conversely, `not_requested` does not make a
non-retrieval profile inapplicable merely because that profile does not require
retrieval. Where retrieval is constitutive, every state other than
`admissible_available` interrupts the reference-dependent evaluation path for
the current event. If no admissible basis can later be reconstructed and no
separately declared non-retrieval profile applies, `I_ref,A(k_A)` remains
non-reconstructable for that event. None of these states proves that no signal
or communication occurred.

For a profile that requires retrieval, retain the retrieval reason and map it
to the common Layer-1 result family as follows:

| Retrieval state | Common I result consequence |
| --- | --- |
| `missing` | `not_observable`: the required operation state or provenance cannot be reconstructed by the evaluator |
| `not_requested` | `not_applicable`: a retrieval required by the selected profile was not performed |
| `unavailable` | `not_observable`: the required operation, channel or result is unavailable to the evaluator |
| `empty` | `not_applicable`: the completed operation produced no candidate basis |
| `inadmissible` | `not_applicable`: no returned candidate may enter the declared baseline |
| `admissible_available` | the numeric path may open if every remaining basis and representation condition succeeds |

This mapping applies only when retrieval is constitutive for the selected I
profile. A non-retrieval profile is not made non-numeric by
`not_requested`.

### 3.2 Versioned I Profile

```text
p_I
= (carrier, segmentation, equivalence, representation,
   reference_selection, retrieval_policy, normalization, eta_ref,
   applicability, missingness, version)
```

**Semantic reading.** `p_I` makes every constitutive choice recoverable. The formula does not choose a carrier, segmentation, equivalence rule, embedding, normalization or weight by itself. Changing one of these choices may create a new profile and therefore a comparability boundary.

### 3.3 Conditional Vector-compatible Representation

A vector-compatible profile may instantiate the declared representation through a versioned embedding function and normalized cosine distance:

```text
d_cos(v_x, v_y)
= clip((1 - cos(v_x, v_y)) / 2, 0, 1)
```

**Semantic reading.** `d_cos` asks how far two applicable vector representations differ in direction. Cosine similarity lies in `[-1,1]`; subtraction from one and division by two map the distance to `[0,1]`, while `clip` protects against numerical overshoot. This does not measure truth, causal influence or complete semantic difference.

Reference-space representation:

```text
emb_Ref_A(k_A)
= mean(emb(x) for x in Ref_A(k_A | p_I))
```

**Semantic reading.** The arithmetic mean creates one declared reference vector from the admitted elements. It is a profile choice, not a universal definition of information. Another carrier may require another representation and aggregation.

### 3.4 Applicability before Numeric Interpretation

```text
app_ref,A(k_A)
:= retrieval_basis_ok,A(k_A)
   and Ref_A(k_A | p_I) != empty
   and emb(e_A(k_A)) is finite
   and emb_Ref_A(k_A) is finite
   and norm(emb(e_A(k_A))) > 0
   and norm(emb_Ref_A(k_A)) > 0
```

**Semantic reading.** The gate asks whether any retrieval required by the profile has an admissible result and whether the selected baseline and both vector representations exist in a form on which the declared distance is defined. It does not ask whether the event is correct, useful or valuable. A closed retrieval-dependent gate interrupts this evaluation path; it does not describe a communication-free state.

The common external Layer-1 result handed to Z is:

```text
operator_result_status in {
  numeric,
  not_selected,
  not_observable,
  not_applicable
}
```

A successful finite calculation maps to `numeric` and carries
`result_value in [0,1]`. If the gate is closed, the reason determines the
common non-numeric result:

```text
required basis, operation or provenance exists or is expected
but is unavailable to the evaluator
  -> J_ref,A(k_A) = not_observable
  -> I_ref,A(k_A) = not_observable

required basis or operation does not exist under the selected profile,
or a completed selection/retrieval produces no admissible non-empty basis
  -> J_ref,A(k_A) = not_applicable
  -> I_ref,A(k_A) = not_applicable

I coordinate not selected by the declared view
  -> I_ref,A(k_A) = not_selected
```

Malformed identity, invalid profile or calculation failure is a processing
failure and produces no valid operator result. It does not become another Z
status. `not_applicable`, `not_observable`, `not_selected` and numeric zero
remain distinct.

Embeddings are one v3.50 vector-compatible profile, not the architecture-independent definition for every carrier. Model, version, preprocessing and chunking changes must remain recoverable.

## 4. Static Components, Calculation and Interpretation

### 4.1 Formula Legitimacy

The mathematical form does not create the semantic boundary. The semantic boundary creates the valid formula. Every formula below is valid only under declared identity, basis, profile, applicability and missingness conditions.

### 4.2 Directional Component



```text
J_ref,A(k_A)
= d_cos(emb(e_A(k_A)), emb_Ref_A(k_A))
```

**Semantic question.** How much directional difference exists between the target event and the declared baseline representation? The result is in `[0,1]`. It does not by itself measure new or compressed information.

This component is calculated only when the applicability conditions in
Section 3.4 hold.

### 4.3 Information-Content Component

Conceptual form:

```text
G_ref,A(k_A)
= (N_new(e_A(k_A), Ref_A(k_A))
   + N_compressed(e_A(k_A), Ref_A(k_A)))
  / N_total(e_A(k_A))

N_total(e_A(k_A)) > 0

0 <= N_new(e_A(k_A), Ref_A(k_A))
     + N_compressed(e_A(k_A), Ref_A(k_A))
  <= N_total(e_A(k_A))
```

**Semantic question.** What share of the event's declared information units is new relative to the baseline or compresses baseline material into a denser usable form? Division by `N_total` normalizes the component to `[0,1]`.

The profile must ensure that each unit enters the numerator at most once; overlapping new/compressed labels must be disambiguated or deduplicated.

`N_new`, `N_compressed` and `N_total` count information units under a declared
carrier-appropriate segmentation and equivalence method. In a language
profile, these units may be semantic equivalence classes rather than raw token
counts; that example does not define every carrier.

If `N_total(e_A(k_A)) = 0`, the declared count bounds fail or the required
count basis does not exist under the selected profile:

```text
G_ref,A(k_A) = not_applicable
```

If required count evidence exists or is expected but is unavailable to the
evaluator, `G_ref,A(k_A) = not_observable`. Invalid concept profiles and
calculation failures remain processing failures rather than operator-result
states.

### 4.4 Reference-Relative Formula

Conceptual formula:

```text
I_ref,A(k_A)
= eta_ref * G_ref,A(k_A)
  + (1 - eta_ref) * J_ref,A(k_A)
```

with `eta_ref in [0,1]` and `I_ref,A(k_A) in [0,1]`.

**Semantic question.** What information impulse results when declared content share and directional difference are combined? The convex weight preserves `[0,1]` when both components apply. `eta_ref` is a declared and versioned application choice, not a universal constant or a value silently learned from the target event. If either mandatory component is non-numeric, canonical `I_ref` retains the mapped common result status and its specific reason; no silent renormalization is active.

Conditional retrieval-backed proxies and controlled implementation fallbacks
belong in separate implementation guidance. They do not redefine this
canonical conceptual formula and are not active unless a separately versioned
profile explicitly selects them.

### 4.5 Interpretation

| Value | Interpretation |
| --- | --- |
| high | strong observable information difference relative to the selected baseline |
| medium | moderate observable information difference |
| low | low observable difference; repetition or stabilization may be present |
| `not_applicable` | the required baseline or component does not exist under the declared profile |
| `not_observable` | required material exists or is expected but is not visible to the evaluator |
| `not_selected` | an optional derived view or component was not selected by its declared profile |

Interpretation must preserve the declared `Ref`, operator configuration and
applicability status. `C_seq,I` must always be named as a diagnostic rather
than reported as the static I value.

```text
not_applicable != not_observable
not_applicable != not_selected
not_applicable != 0
```



## 5. Edge Cases, Privacy and Retention

Repeated low-I events remain attributable and may form contact-attempt, attack or anomaly patterns in sequence, window or Hangar views. Empty and invisible bases remain distinguishable typed non-numeric states; zero denominators and inapplicable representations are not low values, while invalid profiles or calculations remain processing failures.

### 5.1 Privacy and Retention Boundary



Reference material, event representations, embeddings, concept features,
retrieval traces, operator values and derived diagnostics remain subject to
the declared privacy, consent, access and retention policy. Visibility to an
evaluator does not by itself establish lawful or methodically admissible use.

Derived values are not automatically anonymous or privacy-neutral. Embeddings,
reference IDs, retrieval IDs, deltas, windows and Hangar distributions may
retain identifying or sensitive relationships and must preserve only the
provenance needed under the approved policy. Where raw carrier material has a
shorter retention period, later reconstruction must not falsely claim access
to material that was not retained or was never visible.

## 6. Comparability and Source-local Dynamics

### 6.1 Comparability Contract

I values are directly comparable only when all relevant conditions are stable
or explicitly mapped as compatible:

- same target-unit definition;
- same source-attribution rule;
- same reference-space construction rule and compatible admitted baselines for
  `I_ref`;
- same representation profile and, where the vector profile is used, the same
  embedding model, version, preprocessing and chunking;
- same `eta_ref`;
- same concept/proxy implementation;
- same missingness and applicability policy;
- same Observer and operator version.

The concrete admitted content in `Ref_A(k_A-1)` and `Ref_A(k_A)` need not be the
same instance. Both reference-space IDs, admitted-element IDs, exclusions and
construction-profile versions must nevertheless be preserved. A change in
baseline content is part of the comparison provenance and must not be hidden
as ordinary event movement.

Comparability of the optional `C_seq,I` diagnostic additionally requires the
same local-predecessor rule and `eta_seq`. Static I and `C_seq,I` must not be
compared as if they were the same measurement.

### 6.2 Source-local Dynamics

For the canonical static I value along trajectory `A`:

```text
Delta I_A(k_A)
= I_A(k_A) - I_A(k_A - 1)

Delta2 I_A(k_A)
= Delta I_A(k_A) - Delta I_A(k_A - 1)
```

**Semantic reading.** `Delta I_A(k_A)` asks how the static I value moved between two consecutive comparable positions; its range is `[-1,1]`. `Delta2 I_A(k_A)` asks how that first change itself changed across three comparable evaluations; its range is `[-2,2]`. Neither is causal proof.

These differences are valid only when all participating values are applicable and comparable under compatible static I configurations.

`Delta I_A(k_A)` is the change between two comparable reference-relative I
values. If the admitted reference content changed between the evaluations,
the result may contain both target-event movement and baseline movement. It
must not be interpreted as pure event-to-event information movement unless
baseline stability has been established. Reference-space provenance is
therefore constitutive for interpreting the delta.

Source-local `Delta I` and `Delta2 I` remain monadic Standard-Eval diagnostics. Their existence does not make them KSODI-Full.

There is no implicit:

```text
Delta I_AB = I_B - I_A
```

A relation between `A` and `B` requires an explicit exchange or pairing rule and belongs to a relational evaluation step after the two monadic states remain distinguishable.

### 6.3 Optional Same-trajectory Predecessor Diagnostic

`C_seq,I` is an optional, fine-grained monadic diagnostic over one declared
source trajectory. It asks how much direct information difference exists
between the current event and its immediately preceding same-source event.

It is not the canonical static Operator I value, not an alternative I profile
and not a coordinate of `Z`. It also differs from `Delta I`: `C_seq,I`
compares event representations directly, whereas `Delta I` compares two
already calculated static I values.

For `k_A > 1`:

**Predecessor semantics.** `Prev_A(k_A)` selects the immediately prior event on trajectory A, never merely the prior event in global order.

```text
Prev_A(k_A) = e_A(k_A - 1)

J_seq,A(k_A)
= d_cos(emb(e_A(k_A)), emb(e_A(k_A - 1)))
```

The immediately preceding event in global interaction order is not a valid
substitute if it was produced by another entity.

The predecessor comparison is applicable only when current and predecessor
events use compatible carrier, segmentation, representation/embedding,
concept, normalization and same-trajectory predecessor profiles. Otherwise:

```text
C_seq,I,A(k_A) = not_applicable
sequence_baseline_status = incompatible_predecessor_profile
```

A conceptual content component may be calculated relative to the same source-local predecessor:

**Component semantics.** `J_seq` asks for directional event-to-event difference. `G_seq` asks what share of the current event is new or compressive relative to that predecessor. The range, non-overlap and applicability rules of the corresponding static components apply.

```text
G_seq,A(k_A)
= (N_new(e_A(k_A), e_A(k_A - 1))
   + N_compressed(e_A(k_A), e_A(k_A - 1)))
  / N_total(e_A(k_A))

N_total(e_A(k_A)) > 0

0 <= N_new(e_A(k_A), e_A(k_A - 1))
     + N_compressed(e_A(k_A), e_A(k_A - 1))
  <= N_total(e_A(k_A))
```

If `N_total(e_A(k_A)) = 0` or the declared count bounds fail, then
`G_seq,A(k_A) = not_applicable`. A versioned direction-only sequence profile may
still use `J_seq,A(k_A)` where all of its own applicability and comparability
conditions hold.

Diagnostic formula:

**Formula semantics.** `C_seq,I` combines the two direct event-comparison components under a separately versioned sequence profile. It lies in `[0,1]`, remains optional and never fills Z.

```text
C_seq,I,A(k_A)
= eta_seq * G_seq,A(k_A)
  + (1 - eta_seq) * J_seq,A(k_A)
```

If `G_seq` is not implemented, a controlled direction-only profile may use:

**Fallback semantics.** This is a reduced named diagnostic, not an assumption that missing content information equals directional information.

```text
C_seq,I,A(k_A) = J_seq,A(k_A)
sequence_content_status = direction_only
```

For the first event of a trajectory:

```text
C_seq,I,A(1) = not_applicable
sequence_baseline_status = no_local_predecessor
```

The first value is not `0`. There is no measured absence of movement; there is no admissible predecessor.

`C_seq,I` contains no rolling window, centroid, median or whole-scope
aggregation. Those operations belong to `Sigma` and `Sigma(Hangar)`.

### 6.4 Feature Record and Five-dimensional Z

A rich implementation record may preserve the static I value and the optional
predecessor diagnostic:

```text
F_A(k_A)
= (K_A(k_A), S_A(k_A), O_A(k_A), D_A(k_A),
   I_A(k_A), C_seq,I,A(k_A))
```

`F_A(k_A)` is a feature record. It is not the canonical KSODI state vector `Z`.

A KSODI state remains five-dimensional. Only the canonical static I value fills
its I coordinate:

```text
Z_A(k_A)
= (K_A(k_A), S_A(k_A), O_A(k_A), D_A(k_A), I_A(k_A))
```

The same applies independently to `Z_B`. `C_seq,I` stays outside `Z`; its
availability does not create a six-dimensional state.

### 6.5 Drift Indication

For one entity and one trajectory under a stable static I configuration:

```text
Drift_I,A(k_A)
= |I_A(k_A) - median(I_A(k_A-w), ..., I_A(k_A-1))|

I_standardized,A(k_A)
= (I_A(k_A) - mu_W_A) / (sigma_W_A + epsilon_stab)
```

**Formula semantics.** `Drift_I` asks how far current static I lies from the median of a compatible prior window. `I_standardized` asks how unusual it is relative to that window's mean and scale; `epsilon_stab > 0` prevents division by zero. The first is in `[0,1]`; the second is unbounded.

Both diagnostics require a non-empty, applicable and profile-compatible
source-local window. `I_standardized,A(k_A)` additionally requires
`sigma_W_A + epsilon_stab > 0`. Otherwise the affected diagnostic is
`not_applicable`.

This is drift indication only, not evaluation and not relational resonance.

`I_standardized` is an operator-internal standardized diagnostic. It is not
the KSODI state vector `Z` and does not fill or replace the I coordinate.

### 6.6 Optional Exogenous Mask

`I_star` is an optional derived diagnostic, never the canonical static I value
and never the I coordinate of `Z`. For an applicable and exogenously selected
static I value:

```text
A_I,A(k_A) in {0, 1}
sigma_I2,A(k_A) in [0, 1]
epsilon_I in [0, 1]

I_star,A(k_A)
= I_A(k_A)
  * (1 - epsilon_I * sigma_I2,A(k_A))

A_I,A(k_A) = 1
```

**Formula semantics.** `I_star` is an uncertainty-attenuated diagnostic selected by an external profile. Under these bounds it remains in `[0,1]`. Its gate and uncertainty input must be exogenous; they may not be inferred circularly from the I value.

Under these bounds, an applicable `I_star,A(k_A)` remains in `[0,1]`.

If the exogenous selection gate is closed:

```text
A_I,A(k_A) = 0
I_star,A(k_A) = not_selected
```

If the underlying static I value or required uncertainty input is not
applicable:

```text
I_star,A(k_A) = not_applicable
```

Gates and uncertainty masks must be determined exogenously, without circular
reference to the I value they modify. `not_selected` and `not_applicable` must
not be encoded by multiplying a numeric value by zero. Masking is not a
substitute for applicability status.

## 7. Sigma and Sigma(Hangar)

Windows and aggregations begin here, not inside `C_seq,I`.

**Set semantics.** Each `W_app` formula selects only positions for which the corresponding static, first-difference or second-difference data type is applicable and comparable.

**Aggregation semantics.** `I_A Sigma(W)` preserves three typed window summaries. `I_A Sigma(Hangar)` preserves their separate distribution views. The functions are selected by a declared aggregation profile; the formulas do not prescribe one universal aggregator.

```text
W_app_I,A
= {k_A in W_A | I_A(k_A) is applicable under the static aggregation profile}

W_app_DeltaI,A
= {k_A in W_A | Delta I_A(k_A) is applicable and comparable}

W_app_Delta2I,A
= {k_A in W_A | Delta2 I_A(k_A) is applicable and comparable}

I_A Sigma(W)
= {
    static_I: Agg_I({I_A(k_A) | k_A in W_app_I,A}),
    delta_I: Agg_DeltaI({Delta I_A(k_A) | k_A in W_app_DeltaI,A}),
    delta2_I: Agg_Delta2I({Delta2 I_A(k_A) | k_A in W_app_Delta2I,A})
  }

I_A Sigma(Hangar)
= {
    static_I_distribution:
      distribution_view({I_A(k_A) | k_A in W_app_I,A}),
    delta_I_distribution:
      distribution_view({Delta I_A(k_A) | k_A in W_app_DeltaI,A}),
    delta2_I_distribution:
      distribution_view({Delta2 I_A(k_A) | k_A in W_app_Delta2I,A})
  }
```

`W_A` is a declared window over trajectory `A`. Static I values, first
differences and second differences retain separate value ranges, applicability
sets, aggregation functions and output fields. The structured Sigma record
must not be collapsed into one untyped scalar. Multiple trajectories may be
displayed together in Hangar, but their source identity and separate
provenance remain intact.

```text
I_A(k_A) in [0, 1]
Delta I_A(k_A) in [-1, 1]
Delta2 I_A(k_A) in [-2, 2]
```

## 8. Relational Boundary

Standard-Eval can evaluate and monitor one source-attributed signal trajectory without a second trajectory.

`I0`, `C_seq,I`, `Delta I`, `Delta2 I`, `I Sigma(W)` and
`I Sigma(Hangar)` describe monadic operator behavior. A relational comparison
requires distinguishable source trajectories, explicit pairing, compatible
profiles and applicable values, an open numeric canonical complete `R0` gate
under the exact required profile and a separately declared later-layer
construct.

Operator I does not define coupling, resonance, mutual understanding or
relational quality. This v3.50 section records the boundary but does not define
or activate an operator-specific relational I comparison.

A proposed post-`R0` comparison of distinguishable I trajectories would remain
a partial diagnostic; it would not be canonical `IK_rel` or an R-family
result. Both that comparison and any operator-only route that bypasses complete
`Z` belong to v3.60 Future Work and require their own named definition,
applicability, comparability, review and release.

## 9. Formal Summary and Variable Reference

### 9.1 Compact Formula Block

The block below summarizes formulas already explained above; it does not activate implementation-only proxies.

```text
# typed retrieval state where p_I uses retrieval
ret_status,A(k_A)
in {missing, not_requested, unavailable, empty,
    inadmissible, admissible_available}

if p_I requires retrieval:
  retrieval_basis_ok,A(k_A)
  := ret_status,A(k_A) = admissible_available
otherwise:
  retrieval_basis_ok,A(k_A) := true

if p_I requires retrieval:
  missing or unavailable -> operator_result_status = not_observable
  not_requested, empty or inadmissible
    -> operator_result_status = not_applicable

# declared static I baseline
Ref_A(k_A | p_I)
:= {x in V_A(k_A) |
    x is selected by p_I
    and x is admissible
    and x is visible to the evaluator}

emb_Ref_A(k_A)
= mean(emb(x) for x in Ref_A(k_A | p_I))

app_ref,A(k_A)
:= retrieval_basis_ok,A(k_A)
   and Ref_A(k_A | p_I) != empty
   and emb(e_A(k_A)) is finite
   and emb_Ref_A(k_A) is finite
   and norm(emb(e_A(k_A))) > 0
   and norm(emb_Ref_A(k_A)) > 0

d_cos(v_x, v_y)
= clip((1 - cos(v_x, v_y)) / 2, 0, 1)

# canonical static reference-relative value
if app_ref,A(k_A):
  J_ref,A(k_A) = d_cos(emb(e_A(k_A)), emb_Ref_A(k_A))

if app_ref,A(k_A)
   and N_total(e_A(k_A)) > 0
   and 0 <= N_new(e_A(k_A), Ref_A(k_A | p_I))
            + N_compressed(e_A(k_A), Ref_A(k_A | p_I))
          <= N_total(e_A(k_A)):
  G_ref,A(k_A)
  = (N_new(e_A(k_A), Ref_A(k_A | p_I))
     + N_compressed(e_A(k_A), Ref_A(k_A | p_I)))
    / N_total(e_A(k_A))

if J_ref,A(k_A) and G_ref,A(k_A) are applicable:
  I_ref,A(k_A)
  = eta_ref * G_ref,A(k_A)
    + (1 - eta_ref) * J_ref,A(k_A)
  operator_result_status = numeric

otherwise:
  I_ref,A(k_A) retains the mapped common non-numeric result status and reason

I_A(k_A) := I_ref,A(k_A)

# optional same-source predecessor diagnostic
if k_A > 1 and current/predecessor profiles are compatible
   and their required representations are applicable:
  J_seq,A(k_A) = d_cos(emb(e_A(k_A)), emb(e_A(k_A - 1)))

  if N_total(e_A(k_A)) > 0
     and 0 <= N_new(e_A(k_A), e_A(k_A - 1))
              + N_compressed(e_A(k_A), e_A(k_A - 1))
            <= N_total(e_A(k_A)):
    G_seq,A(k_A)
    = (N_new(e_A(k_A), e_A(k_A - 1))
       + N_compressed(e_A(k_A), e_A(k_A - 1)))
      / N_total(e_A(k_A))

  if J_seq,A(k_A) and G_seq,A(k_A) are applicable:
    C_seq,I,A(k_A)
    = eta_seq * G_seq,A(k_A)
      + (1 - eta_seq) * J_seq,A(k_A)
  else if J_seq,A(k_A) is applicable
          and the sequence profile is direction_only:
    C_seq,I,A(k_A) = J_seq,A(k_A)

otherwise:
  C_seq,I,A(k_A) = not_applicable

# first source-local event
C_seq,I,A(1) = not_applicable

# canonical five-dimensional Z
Z_A(k_A) = (K_A(k_A), S_A(k_A), O_A(k_A), D_A(k_A), I_A(k_A))

# source-local movement after applicability and comparability
if G_cmp_I(r_A(k_A), r_A(k_A - 1)) = true:
  Delta I_A(k_A) = I_A(k_A) - I_A(k_A - 1)
otherwise:
  Delta I_A(k_A) = not_applicable

if G_cmp_DeltaI(r_A(k_A), r_A(k_A - 1), r_A(k_A - 2)) = true:
  Delta2 I_A(k_A) = Delta I_A(k_A) - Delta I_A(k_A - 1)
otherwise:
  Delta2 I_A(k_A) = not_applicable

# typed windows and Hangar views
W_app_I,A = {k_A in W_A | I_A(k_A) is applicable}
W_app_DeltaI,A = {k_A in W_A | Delta I_A(k_A) is applicable and comparable}
W_app_Delta2I,A = {k_A in W_A | Delta2 I_A(k_A) is applicable and comparable}

I_A Sigma(W)
= {
    static_I: Agg_I({I_A(k_A) | k_A in W_app_I,A}),
    delta_I: Agg_DeltaI({Delta I_A(k_A) | k_A in W_app_DeltaI,A}),
    delta2_I: Agg_Delta2I({Delta2 I_A(k_A) | k_A in W_app_Delta2I,A})
  }

I_A Sigma(Hangar)
= {
    static_I_distribution:
      distribution_view({I_A(k_A) | k_A in W_app_I,A}),
    delta_I_distribution:
      distribution_view({Delta I_A(k_A) | k_A in W_app_DeltaI,A}),
    delta2_I_distribution:
      distribution_view({Delta2 I_A(k_A) | k_A in W_app_Delta2I,A})
  }

# separate source-local drift diagnostics under a compatible window profile
if the declared prior window is non-empty, applicable and profile-compatible:
  Drift_I,A(k_A)
  = |I_A(k_A) - median(I_A(k_A-w), ..., I_A(k_A-1))|

  if sigma_W_A + epsilon_stab > 0:
    I_standardized,A(k_A)
    = (I_A(k_A) - mu_W_A) / (sigma_W_A + epsilon_stab)
  else:
    I_standardized,A(k_A) = not_applicable

otherwise:
  Drift_I,A(k_A) = not_applicable
  I_standardized,A(k_A) = not_applicable

# separate optional diagnostic; never canonical I or Z
A_I,A(k_A) in {0, 1}
sigma_I2,A(k_A) in [0, 1]
epsilon_I in [0, 1]

if I_A(k_A) and sigma_I2,A(k_A) are applicable and A_I,A(k_A) = 1:
  I_star,A(k_A) = I_A(k_A) * (1 - epsilon_I * sigma_I2,A(k_A))
else if A_I,A(k_A) = 0:
  I_star,A(k_A) = not_selected
otherwise:
  I_star,A(k_A) = not_applicable
```

### 9.2 Variable Reference

| Variable | Semantic role |
| --- | --- |
| `n` / `k_A` / `k_B` / `j` | global event, source-local trajectory and relational pairing indices |
| `e_A(k_A)` | target event at local position `k_A` in the trajectory of stable or provisional source A |
| `V_A(k_A)` | visible candidate baseline material before I-profile selection |
| `RET_A(k_A)` | raw result of a completed retrieval operation where retrieval is used; `empty` is not a communication state |
| `ret_status,A(k_A)` | typed retrieval outcome: missing, not requested, unavailable, empty, inadmissible or admissible-available |
| `retrieval_basis_ok,A(k_A)` | gate stating whether a retrieval required by `p_I` provides an admissible basis |
| `p_I` | versioned I profile, including selection, retrieval and applicability rules |
| `Ref_A(k_A \| p_I)` | selected, admissible and evaluator-visible I baseline |
| `app_ref,A(k_A)` | applicability of the admitted I baseline and required representations |
| `operator_result_status` | common Layer-1 result: numeric, not selected, not observable or not applicable |
| `emb(.)` | versioned vector-profile embedding function; not universal carrier definition |
| `emb_Ref_A(k_A)` | admitted reference-space representation under the vector profile |
| `d_cos` | normalized cosine distance between two applicable vector representations |
| `J_ref` | directional difference relative to `Ref` |
| `N_new` / `N_compressed` / `N_total` | declared concept-method counts used by information-content components |
| `G_ref` | conceptual information content relative to `Ref` |
| `I_ref` / `I_A` | canonical static reference-relative I value |
| `eta_ref` | declared weight between static information-content and directional components |
| `Prev_A(k_A)` | immediately preceding event in the same declared source trajectory |
| `J_seq` | directional movement from the previous same-source event |
| `G_seq` | information content relative to the previous same-source event |
| `C_seq,I` | optional same-trajectory predecessor diagnostic; not a Z coordinate |
| `eta_seq` | declared weight for the optional predecessor diagnostic |
| `F_A` | rich feature record; not canonical Z |
| `Z_A` | canonical five-dimensional monadic state |
| `G_cmp_I` | comparability gate for two static I evaluation records |
| `G_cmp_DeltaI` | comparability gate for a second-difference construction |
| `Delta I_A` | first source-local difference of static I values |
| `Delta2 I_A` | second source-local difference of static I values |
| `W_A` | declared source-local window |
| `W_app_I,A` | applicable static-I positions in the declared window |
| `W_app_DeltaI,A` | applicable and comparable first-difference positions |
| `W_app_Delta2I,A` | applicable and comparable second-difference positions |
| `Agg_I` / `Agg_DeltaI` / `Agg_Delta2I` | separately typed aggregation functions selected by the window profile |
| `distribution_view` | derived Hangar distribution constructor retaining type and provenance |
| `I_A Sigma(W)` | typed static, Delta and Delta2 window-aggregation record |
| `I_A Sigma(Hangar)` | typed attributable distribution record |
| `Drift_I,A` | source-local drift indication under a compatible prior window |
| `mu_W_A` / `sigma_W_A` | mean and standard deviation under the declared compatible window profile |
| `epsilon_stab` | declared positive stabilization term for standardization |
| `I_standardized,A` | operator-internal standardized diagnostic; not KSODI `Z` |
| `A_I,A` | exogenous binary selection gate for `I_star` |
| `sigma_I2,A` | optional uncertainty input for `I_star` |
| `epsilon_I` | declared uncertainty weight for `I_star` |
| `I_star,A` | optional exogenously selected derived diagnostic; not canonical I or Z |
| `not_applicable` | required baseline/component absent; never numeric zero |
| `not_observable` | required observable material is unavailable to the evaluator |
| `not_selected` | optional derived view or component was not selected; never numeric zero |

## 10. Public Implementation Boundary

The canonical method ends with the formal summary in Section 9. Implementation-specific storage fields, pseudocode, retrieval mappings, data flow and architecture configuration are separate from this operator definition.

- Public boundary: [KSODI Implementation Guardrails](../../IMPLEMENTATION_GUARDRAILS.md).
- Released conditional implementation companion: [KSODI Operator I Implementation Companion](./KSODI_Operator-I_Implementation-Companion_V350.md).

The companion operationalizes one Conversation-/Retrieval-oriented profile; it does not narrow the carrier-neutral method or make that profile mandatory. An implementation may operationalize Operator I but must not redefine its semantic question, measurement basis, applicability, formula, source identity or layer boundary. If the companion and this method appear to differ, this method controls and the mismatch must remain visible until reviewed.
