# KSODI Research Status and Open Questions v3.50

This note makes the research boundary of the public v3.50 method visible before
empirical or operational use. It does not replace the authoritative layer and
operator files, change a formula or define an implementation profile.

The central distinction is:

```text
mathematically defined != empirically validated
internally consistent != necessary or sufficient
bounded to [0,1] != calibrated, unique or universally comparable
common mathematical form != standard KSODI semantics or evidence of novelty
```

The descriptions below classify the current public construction. Calling a
mathematical form common or conventional is a structural description, not a
claim that KSODI was derived from one particular theory, source or prior
method. Intellectual lineage, theoretical connection and novelty require
separate source-based comparison.

## 1. How to read the classifications

| Classification | Meaning in this note |
| --- | --- |
| Defined | The public v3.50 method specifies the observation object, basis, applicability, construction and boundaries. |
| Common mathematical form | The calculation uses a broadly used construction such as a finite weighted mean, vector assembly, linear projection, finite difference, norm, threshold, rate or distribution summary. |
| KSODI-specific choice | KSODI selects and combines observation semantics, identities, typed statuses, profiles, gates, branches or reporting rules for its own method question. |
| Empirically open | Reliability, calibration, validity, sensitivity, necessity, sufficiency or usefulness has not been established for all intended domains. |
| Alternative open | Another basis, detector, norm, weight, projection, threshold, aggregator or branch definition could answer the question differently and still needs comparison. |
| Non-claim | A result must not be interpreted as something the method does not establish. |

Public v3.50 supplies formal method contracts and bounded implementation
guidance. It does not supply universal calibrated profiles, universal
thresholds or independent empirical validation across the proposed application
domains.

### Current evidence boundary

The repository documents sustained practice observations, iterative formal and
semantic review, historical implementation work and exploratory tests. This
supports provenance, feasibility and the formulation of testable method
contracts. The reported practice observations are not controlled studies.
KSODI-specific selection, composition, weights, thresholds, construct validity
and application have not undergone independent formal review and
application-specific empirical validation. No universal causal performance
gain is claimed.

## 2. Layer 0 — KSODI-Light

### Defined

KSODI-Light provides a reflective K/S/O/D/I working agreement and disclosed
0–5 local scoring language for prompting, review and interaction hygiene.

### Common form and KSODI-specific choice

Ordinal working scales and structured checklists are common forms. The five
questions, their meanings, their reciprocal use and the rule that the score is
shown only when requested are KSODI-Light choices.

### Open questions and non-claims

The scale is not a calibrated conversion of the formal `[0,1]` Observer
operators. Inter-rater reliability, learning effects, domain adaptation and
comparison with simpler prompting checklists remain empirical questions.
Light does not create a formal `Z`, `IK`, relational result or Controller
instruction.

## 3. Layer 1 — K/S/O/D/I operators

### Shared defined contract

Each operator evaluates one source-attributed target event under its own
declared measurement basis and profile. Numeric results lie in `[0,1]`;
`not_selected`, `not_observable` and `not_applicable` remain distinct from zero,
and processing failure produces no valid operator result.

Finite weighted means, proportions, clipping, pairwise distances, cosine
distance, finite differences and window summaries are common mathematical
forms. Their use does not validate the five-operator selection or prove that
the operators are independent, necessary, sufficient or functionally
non-redundant.

### Operator-specific boundary matrix

| Operator | What v3.50 defines | Common mathematical form | KSODI-specific selection or composition | Empirically open / alternatives | Explicit non-claim |
| --- | --- | --- | --- | --- | --- |
| K — Observable Context Completeness | Fulfilment of a non-empty expected context-requirement set inside an admissible scope and declared availability relation | Unweighted or weighted finite mean | Expected requirements, scope, availability relation, applicability and profile | How requirements are elicited; weight calibration; evaluator agreement; effects of hidden or inaccessible context; comparison with simpler coverage baselines | Not general response quality, intent, usefulness or permission to inject context |
| S — Observable Structural Coherence | Profile-selected structural requirements, segmentation/boundary support, order relations and an optional disruption penalty | Weighted mean, normalized ratios, convex component combination, clipping and optional subtractive penalty | Component meanings, mandatory set, sufficiency rule, disruption definition and profile-controlled renormalization | Component overlap; detector dependence; penalty necessity; carrier-specific calibration; alternative graph, sequence or schema representations | Not meaning, truth, grounding, clarity, information novelty or general quality |
| O — Observable Grounded Objectivity | A Source-Need Gate plus profile-defined grounding/traceability components relative to a visible admissible non-empty `Ref` | Logical applicability gate followed by a bounded profile-defined aggregation | Source-need states, visible reference-space contract, admissibility, component semantics and the permitted aggregation profile | Functional non-redundancy from K/S/D/I; source quality and conflict handling; evaluator/retrieval dependence; calibration; alternative evidence and provenance models | Not universal correctness, world knowledge, usefulness, compliance, intent or retrieval permission |
| D — Observable Clarity | Local observable signal support and, in the full profile, reconstruction-relevant local dispersion | Normalized count ratio, mean pairwise distance, affine normalization and weighted combination | Carrier/detector/segmenter basis, support-unit definition, dispersion interpretation, L-only alternative and the reference `0.6/0.4` weighting | Detector reliability; expected-dispersion baseline; weight sensitivity; whether dispersion helps across carriers; alternative signal-quality measures | Not grammar, grounding, meaning, successful decoding, attack attribution or general semantic precision |
| I — Observable Information Impulse | Reference-relative information difference using an admitted baseline; optional source-local sequence and drift diagnostics remain separate | Mean representation, cosine distance, proportions, convex weighting, median/mean/standard-deviation diagnostics | Reference construction, representation, novelty/compression counts, `eta_ref`, retrieval typing and separation of canonical I from sequence diagnostics | Embedding/model sensitivity; baseline dependence; novelty and redundancy definitions; compression proxy validity; weight calibration; alternatives based on other distance or information measures | Not truth, causal influence, intent, attack attribution, complete semantic difference or action authority |

### Cross-operator research boundary

The five operators are semantically distinguished by their questions, targets,
bases and profiles. That does not establish statistical independence or
functional non-redundancy. Required research includes:

- overlap and correlation analysis across profiles and domains;
- operator ablation and comparison with simpler baselines;
- necessity and sufficiency tests for the five-coordinate set;
- inter-evaluator and test-retest reliability;
- calibration and boundary/failure-case studies;
- sensitivity to evaluator model, detector, reference material and profile;
- fairness and access effects where missing setup or invisible evidence changes
  applicability.

## 4. Layer 2 — typed state vector Z

### Defined

`Z_A(k_A)` assembles five aligned numeric operator results for one
source-attributed event:

```text
Z_A(k_A) = (K_A, S_A, O_A, D_A, I_A) in [0,1]^5
```

The mandatory typed status vector `T_Z` is retained. Complete Z exists only
when all five coordinates are numeric and identity-aligned. Reduced views use
one explicit fixed coordinate set `M`. Comparable source-local differences,
L1/L2 drift norms, windows and distributions are defined under their own
contracts.

### Common mathematical form and KSODI-specific choice

Vector assembly, component-wise finite differences, L1/L2 norms and normalized
window rates are common constructions. KSODI specifically selects the ordered
K/S/O/D/I coordinate system, typed missingness, completeness gate,
source-local identity and fixed-M rules.

### Open questions, alternatives and information loss

Z does not apply one additional normalization to the five coordinates; it
assembles operator outputs that have already been mapped to `[0,1]` under
different profiles. Consequently:

- equal numeric ranges do not establish equal scale meaning, variance,
  reliability or empirical importance;
- different raw events and measurement records can map to the same Z;
- correlation and overlap among coordinates may reduce the effective
  dimensionality;
- reduced `Z^[M]` views omit coordinates and are not directly interchangeable
  with complete Z;
- L1, L2 and other possible distance choices emphasize movement differently;
- cross-profile, cross-domain and cross-evaluator comparability remains open.

The typed operator records, bases and provenance therefore remain necessary;
the vector alone is not a lossless representation of the observed event.

Z is not a merged participant state, a causal model, empirical truth or proof
that five coordinates are the unique or sufficient state description.

## 5. Layer 3 — monadic IK projection

### Defined

For complete canonical Z and one named profile:

```text
w_X >= 0
sum_X w_X = 1
IK_A(k_A | p_IK) = w dot Z_A(k_A)
```

Reduced projections require a separately named fixed-M profile. Comparable
`Delta IK`, `Delta2 IK`, windows and coverage remain source-local and
profile-bound.

### Common mathematical form and KSODI-specific choice

A weighted linear projection, finite differences and window aggregation are
common mathematical forms. The interpretation as a monadic KSODI coherence
axis, the eligible Z input, profile identity and reduced-view restrictions are
KSODI-specific.

### Open questions, alternatives and information loss

The equal-weight axis is a transparent reference, not an empirically optimal
axis. Weight rationale, calibration and domain transfer remain open. Because
IK maps a five-dimensional vector to one scalar, it is non-injective: many
different Z states can have the same IK value. A stable scalar may therefore
hide compensating coordinate movement.

Required research includes:

- characterize which substantively different Z states collapse to the same IK;
- weight and normalization sensitivity, including correlated coordinates;
- uncertainty propagation from the five operator records;
- comparison of equal, expert-selected, learned, multiple-axis, nonlinear and
  no-scalar alternatives;
- practical interpretation of low, middle, high and changing IK values;
- limits of `Delta`, `Delta2`, window and corridor interpretation.

IK is not a complete state, relation, resonance, truth, safety, alignment or
action score. It does not consume or open `R_0`.

## 6. Layer 4 — relational comparability gate R_0

### Defined

`R_0` compares complete comparable source-local Z movement from a declared dyad
or constellation. The canonical dyadic reference uses normalized trajectory
drift and a transparent mean:

```text
R_0 = 1 - mean(d_A, d_B)
numeric R_0 >= theta -> gate_state = open
numeric R_0 < theta  -> gate_state = closed
```

Numeric value and gate state remain separate. Reduced profiles require one
fixed shared `M`; n-adic profiles require an explicit constellation. Windows
report typed result counts, coverage and gate-open rate.

### Common mathematical form and KSODI-specific choice

L1/L2 norms, range normalization, arithmetic or weighted means, thresholds and
rates are common constructions. KSODI specifically defines the source-local
movement input, pairing/constellation identity, bounded-drift interpretation,
typed gate states, fixed-M discipline and branch handoff.

### Open questions and alternatives

- empirical selection and calibration of `theta`;
- false-open and false-closed behavior under noise, sparse data and profile
  drift;
- L1 versus L2 and other possible norms or robust distances;
- mean versus maximum, quantile, asymmetric, weighted or member-specific
  aggregation;
- whether joint stillness should count as stability, insufficient movement or
  a separately typed condition in a given profile;
- sensitivity to pairing, window, normalization and cardinality;
- relation between an open gate and useful downstream analysis;
- hysteresis, lead/lag and threshold dynamics.

An open `R_0` is methodological eligibility only. It does not prove contact,
receipt, acknowledgement, meaning, relation, coupling, resonance, causality,
alignment, desirability or permission to act.

## 7. Layer 5 — dyadic IK_rel

### Defined

Current primary IK_rel is strictly dyadic. After the exact compatible open
canonical-complete dyadic `R_0` gate, it compares paired movement on one shared
canonical monadic IK axis:

```text
g_move = |Delta IK_A - Delta IK_B|
IK_rel = 1 - g_move / 2
```

Joint zero movement is `not_applicable` under the current policy. Extended
profiles use one fixed declared component set `N` from gap, movement and
acceleration; unavailable components are not silently removed or
renormalized.

### Common mathematical form and KSODI-specific choice

Absolute difference, range normalization, weighted component aggregation,
finite differences and window rates are common constructions. KSODI
specifically selects the same-pairing `R_0` handoff, shared monadic axis,
zero-movement policy, component typing and strictly dyadic current scope.

### Open questions and alternatives

- sensitivity to both monadic IK axes and their weights;
- pairing policy, lag/lead alignment and `R_0`-profile dependence;
- information loss inherited from IK and added by the relational scalar;
- normalization and zero-movement/zero-acceleration policies;
- interpretation and validation of gap, movement and acceleration components;
- component weights, fixed-N alternatives and comparison with simpler
  movement-similarity baselines;
- robustness to sparse eligible steps and gate transitions;
- a separately defined n-adic relational projection rather than pairwise
  averaging.

IK_rel is not agreement, shared meaning, causation, coupling, resonance,
alignment, successful communication or Controller authority.

## 8. Sigma, windows and Hangar views

### Defined

Sigma denotes a declared aggregation within one layer or branch. It is not a
new universal layer. Hangar views retain typed, attributable distributions,
trajectories, window aggregates or point clouds under declared object,
identity, profile, basis, status and provenance contracts.

### Common mathematical form and KSODI-specific choice

Means, medians, counts, coverage rates, finite differences, distribution
summaries and distance-based comparison are common forms. KSODI specifically
requires layer-local eligibility sets, typed missingness, fixed bases,
source/trajectory identity and branch-specific rather than generic R-family
aggregation.

### Open questions and alternatives

- window length, alignment, overlap and minimum eligible count;
- mean, median, quantile, robust or domain-specific aggregators;
- coverage thresholds and the interpretation of sparse eligible windows;
- typed missingness mechanisms and selection bias;
- distribution distance, clustering, corridor and anomaly definitions;
- cross-session, cross-group, cross-profile and cross-domain comparability;
- uncertainty propagation and multiple-comparison effects;
- privacy and linkability of derived vectors, trajectories and distributions.

There is no universal Hangar metric, corridor, clustering rule, anomaly
threshold, `R_Sigma` scalar or mandatory first aggregation set. A trend,
corridor exit or anomaly is an Observer-side review signal, not proof of cause,
quality or a required intervention.

## 9. Layers 6–8 and future Controller

| Layer or role | Public v3.50 boundary | What remains open |
| --- | --- | --- |
| Layer 6 — R_geom | Orientation only; no current public calculation contract | Geometric basis, cardinality, normalization, coupling semantics, validation, windows and evidence requirements |
| Layer 7 — R_pace | Orientation only; no current public calculation contract | Carrier-visible pacing basis, timing/index policy, relation to structure, synchronization alternatives, validation and windows |
| Layer 8 — signal-media research | No defined public architecture or implementation guidance | Audio/radio/Morse/wave observation objects, sampling, segmentation, transforms, features, identities, source separation and relational contracts |
| Future Controller | Separate governed action architecture, not a KSODI Observer layer | Authority, policy, permitted actions, evidence envelope, oversight, rollback, logging, feedback delay and anti-circularity controls |

No missing Layer-6-to-8 formula may be filled from plausible geometry,
physics, signal processing, timing or infrastructure defaults and then called
canonical KSODI.

No Observer value, gate, trend, aggregate, corridor or alarm selects an action.
Any later intervention requires a separately declared human or Controller
decision, independent authority, policy and audit trail.

### Outcome and optimization boundary

KSODI observations are not independent outcome measures of truth, learning,
task success, safety, intention or human value. Those outcomes require their
own definitions and evidence. A correlation between a KSODI trace and an
external outcome does not by itself establish causality or generalize across
profiles, evaluators, models, carriers or domains.

If a KSODI score, gate, corridor or alarm is later used as an optimization
target or Controller input, the observation setting changes. Strategic
adaptation to visible metrics, intervention endogeneity, proxy optimization
and Goodhart-type failure modes then require separate study, governance and
audit. The current v3.50 Observer definitions do not validate such use.

## 10. Cross-layer empirical programme

The following work remains necessary before claims stronger than formal method
definition or bounded feasibility can be made:

1. construct domain-specific annotated datasets with explicit evaluation units,
   sources, trajectories, profiles and provenance;
2. measure inter-evaluator reliability and evaluator-model sensitivity;
3. test calibration, boundary cases, missingness and adversarial/failure cases;
4. perform operator ablation, overlap/correlation and necessity/sufficiency
   studies;
5. compare every composite with simpler baselines and reasonable alternatives;
6. run weight, norm, threshold, pairing, window and aggregation sensitivity
   analyses;
7. quantify uncertainty and information loss at every normalization,
   projection and aggregation step;
8. validate each domain separately before cross-domain comparison;
9. assess fairness, privacy, retention and feedback-loop risks;
10. preserve Observer/Controller separation in every implementation test.

Until such evidence exists, the public formulas are versioned research-method
definitions and testable hypotheses. They are not universal empirical laws,
certifications or production guarantees.

## 11. Repository reading path

- Layer 1 definitions:
  [K/S/O/D/I operator entry](./KSODI-Standard-Eval/Layer-1_KSODI-Operators_V350/README.md).
- Layer 2 definition:
  [State Vector Z](./KSODI-Standard-Eval/Layer-2_KSODI-State-Vector-Z_V350/KSODI_State-Vector-Z_V350.md).
- Layer 3 definition:
  [Monadic IK](./KSODI-Standard-Eval/Layer-3_KSODI-Monadic-Interaction-Coherence-IK_V350/KSODI_Monadic-Interaction-Coherence-IK_V350.md).
- Layer 4 definition:
  [Relational Gate R_0](./KSODI-Full/Layer-4_KSODI-Relational-Gate-R_0_V350/KSODI_Relational-Gate-R_0_V350.md).
- Layer 5 definition:
  [Dyadic IK_rel](./KSODI-Full/Layer-5_KSODI-Dyadic-Relational-Coherence-IK_rel_V350/KSODI_Dyadic-Relational-Coherence-IK_rel_V350.md).
- Cross-layer Sigma/Hangar interpretation:
  [KSODI Hangar V350](./KSODI-Hangar_V350.md).
- Architecture and dependencies:
  [KSODI Architecture V350](./KSODI-Architecture_V350.md).
- Implementation invariants:
  [KSODI Implementation Guardrails](./IMPLEMENTATION_GUARDRAILS.md).
- Research direction: [KSODI Research Roadmap](./ROADMAP.md).
- Observation/action separation:
  [Observability and Controlled-Action Boundary](./KSODI-Full/KSODI_Observability-and-Controlled-Action-Boundary_V350.md).
