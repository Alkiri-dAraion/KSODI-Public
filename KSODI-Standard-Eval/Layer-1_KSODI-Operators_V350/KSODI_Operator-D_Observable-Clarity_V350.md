# KSODI Operator D0 - Observable Clarity v3.50

Status: public v3.50 reference release, revised 2026-08-19, released
2026-08-21 and clarified by a typed-result erratum on 2026-08-25. This file is
the current public method definition for Operator D. It remains open to
documented review and later versioned refinement.

Layer: KSODI Standard-Eval Layer 1. Static D and all source-local D trajectory,
window and Hangar views remain strictly monadic and source-attributed.

Implementation boundary: read the public
[KSODI Implementation Guardrails](../../IMPLEMENTATION_GUARDRAILS.md) and the
adjacent [Operator D Implementation Companion](./KSODI_Operator-D_Implementation-Companion_V350.md).
The companion is conditional implementation guidance; this method file remains
authoritative.

## 0. What Operator D is and what it does

Operator `D` asks a bounded signal-facing question:

> Given one already observed, source-attributed or provisionally attributable
> target event, is its signal distinct, locally supported and stable enough
> under the declared detector and carrier profile to justify continuing a
> reconstruction attempt?

D does not decide whether communication exists. It does not discover an
information impulse for the first time. That process-facing threshold belongs
to I: an observable impulse, repetition, change or absence-of-change must first
be distinguishable as an event relative to its declared basis. D then examines
the observable carrier conditions of that already declared target event.

D also does not establish that reconstruction has succeeded. It estimates
profile-bound *reconstruction support*: whether the signal offers sufficient
local support and sufficiently reconstruction-compatible variation for the
Observer to continue examining it.

### 0.1 Minimal practical reading

In plain terms:

- I asks: “Is there an observable information impulse or event here?”
- D asks: “Is that observed signal clear and stable enough to keep trying to
  reconstruct it?”
- O asks, where a source need exists: “Can it be grounded or traced against an
  admissible visible reference space?”
- S asks: “What observable structure, segmentation, boundaries or order does
  it have?”
- K asks: “Which declared context is visible or available?”

A signal may therefore have:

- observable I but low D: an impulse is evident, but its carrier is too sparse,
  noisy or unstable for a reliable reconstruction attempt;
- high D but unresolved O/S/K: the signal is crisp and repeatable, while its
  source, code or context remains unknown;
- high S but low D: a structural hypothesis is visible, but the carrier remains
  too weak or unstable to support reconstruction confidently.

### 0.2 How to read this file

Sections 1 and 2 establish the examples and semantic boundary before the
mathematics. Sections 3 and 4 define the measurement basis, applicability,
components and static formula. Sections 5 through 7 cover edge cases,
comparability, source-local movement and typed window/Hangar views. Sections 8
and 9 close the relational and formal boundaries. Implementation details are
kept in the separate adjacent companion named in Section 10.

## 1. Bounded Application Examples

The examples map different domains onto the same canonical definition. They
are explanatory mappings, not separate definitions and not empirical
validation by themselves.

### 1.1 Human-Chatbot Interaction

One human contribution and one chatbot contribution remain two independently
source-attributed events. For one target contribution from entity A:

```text
target_event_id = event_A_42
source_entity_id = entity_A
trajectory_id = trajectory_A
trajectory_index = k_A
exchange_id = exchange_09
```

The Observer has already admitted `event_A_42` as an observable target event.
D does not infer that event from the chatbot's reply and does not merge the
human and chatbot trajectories. Under a declared language/carrier profile, D
may examine whether the contribution contains enough locally observable signal
support and whether its local variation remains compatible with segmentation
and continued reconstruction.

A grammatically elegant contribution can still have lower D if the signal is
fragmentary, corrupted or locally unstable. A blunt contribution can have high
D when it is clearly observable and reconstructable. Neither result establishes
truth, usefulness, intelligence, politeness or shared understanding.

### 1.2 Unknown Morse-Like Signal

An Observer notices repeated marks and gaps on a channel and assigns a
provisional observed-source identity `U`. I can register the repeated impulse
before the physical emitter, code, intent or message meaning is known.

D then asks whether the marks and gaps have enough contrast, duration support
and local timing stability to justify continued reconstruction. A crisp unknown
code may have high D even while:

- O cannot yet ground it in an admissible visible source space;
- S has not yet identified a stable symbol grammar;
- K has several competing contextual hypotheses.

Repetition may improve D only where it improves discernibility or
reconstruction support under the declared profile. It may also remain important
as a separate source-local persistence or anomaly observation. No intention,
attack, acknowledgement or successful decoding is inferred from repetition
alone.

## 2. Canonical Definition, Scope and Boundaries

`D0_A(k_A | p_D)` estimates the observable discernibility and reconstruction
support of one already observed target signal `q_A(k_A)` under a declared and
versioned detector/carrier profile `p_D`.

D is not:

- a first-event or communication-existence detector;
- completed decoding or receiver understanding;
- a grounding, source-traceability or context-proximity score;
- a direct measure of Shannon entropy or channel capacity;
- factual correctness, quality, usefulness, writing skill, intelligence,
  persuasion, intent, attack, error or human worth;
- a structural-order score or a substitute for S.

Its connection to Shannon-style questions is methodological. A signal must be
observable and discriminable through a bounded carrier before reconstruction
can be attempted. D remains a KSODI observation coordinate, not a direct
Shannon measure.

### 2.1 Atomic Evaluation Unit and Identity

The atomic evaluation unit is one observable event:

```text
e_A(k_A) = one target event attributed to entity A, or to one explicitly
           provisional observed-source identity, at local trajectory index k_A
```

This notation fixes the unit of observation. `A` names the stable or
provisional source identity used for attribution; `k_A` names the position
inside A's declared trajectory. It does not introduce entity B into the
calculation.

For distinguishable entities A and B:

```text
D_A(k_A) = D(q_A(k_A) | p_D_A, source_entity_id_A, trajectory_id_A)
D_B(k_B) = D(q_B(k_B) | p_D_B, source_entity_id_B, trajectory_id_B)
```

These expressions define two separate monadic D values. They are not averaged,
paired or compared by the static operator.

#### 2.1.1 Canonical Index Discipline

The active notation distinguishes:

```text
n    = global event index in the declared observation log
k_A  = source-local trajectory index for entity A
k_B  = source-local trajectory index for entity B
j    = later relational pairing or constellation index, only after R0
t    = optional physical or wall-clock time, explicitly mapped when retained
```

`k_A - 1` means A's preceding comparable trajectory position. It does not mean
the immediately preceding global event and must not silently select an event
from B.

### 2.2 Static and source-local D views are strictly monadic

Static D, `Delta D`, `Delta2 D`, `DΣ(W)` and `DΣ(Hangar)` remain attached to
one source trajectory. A shared room, task, timestamp, channel, exchange or
reference object does not merge A and B and does not create a relational D
value.

### 2.3 Semantic Distinctness and Symbol Discipline

| Coordinate | D boundary |
| --- | --- |
| `I` | I admits an observable impulse or event relative to its declared basis. D evaluates the discernibility and reconstruction support of that already declared target signal. |
| `S` | S evaluates observable structure, order, boundaries and patterning. D uses segmentation only as part of a declared detector profile needed to estimate signal discernibility; it does not score the resulting structural organization. |
| `O` | O evaluates visible grounding or traceability where a source need exists. D does not use reference-space proximity to raise or lower the signal-facing value. |
| `K` | K evaluates declared context availability/completeness. D does not infer contextual fit or meaning. |

A visible feature may be relevant to more than one detector, but it must not be
counted twice inside D or silently treated as proof of another coordinate.
Shared embeddings, corpora or markers must remain visible as possible sources
of detector correlation.

The symbols in this file are KSODI's declared mathematical notation. Their
legitimacy comes from explicit semantic definitions, valid mathematical
constructions, units, domains, applicability rules and reproducible profiles;
not from a requirement that another method use the same names. The particular
KSODI composition and its weights remain subject to domain validation.

### 2.4 Coordinate order and directed process topologies

The canonical state-vector coordinate order is:

```text
Z_A(k_A) = (K_A, S_A, O_A, D_A, I_A)
```

This is a coordinate order, not a causal formula chain.

For an unfamiliar observed signal, the preferred receiver-side reconstruction
direction is:

```text
I -> D -> O -> S -> K
```

This is an iterative process topology, not a numerical dependency among the
five coordinates. D does not require the numeric value `I_A(k_A)` as an input.
It requires a declared observable target event. A known convention may shorten,
parallelize or reorder practical reconstruction; an unfamiliar carrier may
reopen earlier hypotheses recursively.

## 3. Measurement Basis, Profiles and Applicability

### 3.1 Declared measurement basis

D requires a declared signal-facing measurement basis. At minimum it names:

- the target event and source/provisional-source identity;
- carrier type and valid observation unit;
- detector and segmentation conditions;
- local support-unit definition and support ceiling;
- local-unit definition and reconstruction-relevant distance function;
- expected local variation and normalization;
- active component mask, fallback policy and applicability rules.

Historical expectation, context proximity, source grounding, intent and
Hangar deviation are outside the canonical numeric D basis.

### 3.2 Versioned profile

```text
p_D = (p_L, p_V, detector_profile, carrier_profile,
       segmenter_profile, normalizer_profile, weight_profile,
       applicability_profile)
```

This tuple declares the complete profile needed to reproduce one D value.
`p_L` controls local support; `p_V` controls reconstruction-relevant local
dispersion; the remaining fields bind the detector, carrier, segmentation,
normalization, weights and applicability policy. Equal symbol names without
equal or explicitly compatible profile versions do not establish comparability.

### 3.3 Applicability before numeric interpretation

Applicability is typed before any numeric D value is calculated. Two status
levels remain distinct.

The common external Layer-1 result handed to Z is:

```text
operator_result_status in {
  numeric,
  not_selected,
  not_observable,
  not_applicable
}
```

Internal component and processing detail may additionally distinguish:

```text
applicable
not_selected
not_observable
not_applicable
profile_missing
profile_incompatible
```

A successfully applicable finite D calculation maps to
`operator_result_status = numeric` and carries `result_value in [0,1]`.
`applicable` remains an internal component/applicability state; it is not an
additional external Layer-1 result status. `profile_missing` and
`profile_incompatible` remain processing detail and do not become numeric or
an extra Z status.

These states are not numeric zero. If mandatory local support cannot be
evaluated, canonical D is `not_applicable`. If D was not selected for a use
case, it is `not_selected`. If the already admitted event is observable but
the carrier or detector cannot expose the units required by D, the common D
result is `not_observable` and retains the more specific deployment reason.
This status does not revoke I's earlier admission of the event.

### 3.4 Conditional L-only profile

The full v3.50 profile uses local support L and local dispersion V. An L-only
value is permitted only under an explicitly declared and versioned L-only
profile. It must not appear as an undeclared runtime substitution merely
because V could not be calculated.

Where fewer than two valid V units exist, the result is:

```text
V_A(k_A | p_V) = not_applicable
```

This expression means that pairwise local dispersion cannot be evaluated for
this event/profile. It does not mean zero dispersion. A predeclared L-only
profile may still calculate D from L; otherwise D is `not_applicable`.

## 4. Static Components, Calculation and Interpretation

### 4.1 Why the formula matters

The formulas are compact semantic contracts. Each expression below names one
observable object, its profile, its range, its applicability boundary and the
limited claim that follows from it.

### 4.2 Local Observable Signal Support - `L_A(k_A | p_L)`

```text
L_A(k_A | p_L)
= clip(
    n_effective_support_units_A(k_A | p_L)
    / N_L(q_A(k_A), p_L),
    0, 1
  )
```

**Semantic reading.** The numerator counts profile-valid local units that
support signal discernibility or continued reconstruction. The denominator is
the profile-defined saturation or normalization basis for this target signal.
Clipping bounds the result to `[0,1]`.

**What it establishes.** High L means that the observed carrier exposes strong
local support under `p_L`.

**What it does not establish.** L does not prove meaning, truth, grounding,
intent, completed decoding or successful communication. Repetition raises L
only when the declared profile treats it as useful support, and the support
ceiling prevents unlimited repetition from increasing L without bound.

If `N_L(q_A(k_A), p_L)` is zero/undefined or valid support units cannot be
observed, L is `not_applicable` or `not_observable` according to the declared
failure state; it is not zero by default.

### 4.3 Reconstruction-Relevant Local Dispersion - `V_A(k_A | p_V)`

First declare the valid local units and their normalized profile-bound
distance:

```text
U_A(k_A | p_V) = {u_1, ..., u_m}
d_p_V(u_i, u_j) in [0,1]
```

**Semantic reading.** `U_A` is the set of valid local units selected by the
segmenter under `p_V`; `d_p_V` measures only the kind of pairwise difference
that the profile declares relevant to reconstruction. The symbol `m` counts
local units and is not an event index.

For `m >= 2`, calculate mean pairwise local dispersion:

```text
V_raw_A(k_A | p_V)
= (2 / (m * (m - 1))) * sum_{i < j} d_p_V(u_i, u_j)
```

**Semantic reading.** The factor `2 / (m(m-1))` divides the sum by the number
of unordered pairs. `V_raw` is therefore the mean normalized pairwise distance
among the valid local units.

**What it establishes.** It estimates average profile-relevant local variation.
It does not yet distinguish expected variation from excess variation.

Adjust for the profile's expected local variation:

```text
V_A(k_A | p_V)
= clip(
    (V_raw_A(k_A | p_V) - tau_expected_p_V)
    / (1 - tau_expected_p_V),
    0, 1
  )

where 0 <= tau_expected_p_V < 1
```

**Semantic reading.** Variation at or below the declared expected threshold is
mapped to zero excess dispersion. Variation between the threshold and the
maximum is linearly normalized into `[0,1]`; clipping protects the range.

**What it establishes.** High V means high *excess reconstruction-relevant*
dispersion under `p_V`.

**What it does not establish.** V is not novelty, anomaly, error, attack,
entropy or general semantic diversity. The threshold is profile-bound and must
be justified or calibrated for the application domain.

A declared language/embedding profile may use normalized cosine distance:

```text
d_cos(u_i, u_j) = (1 - cos(e(u_i), e(u_j))) / 2
```

**Semantic reading.** Assuming cosine similarity lies in `[-1,1]`, the affine
transformation maps it into a distance in `[0,1]`: identical directions map to
`0`, opposite directions to `1`.

**Boundary.** This is one profile example, not D's universal distance function.
Embedding choice and preprocessing may create detector-specific correlations.

### 4.4 Static Formula and Profile Selection

For the full L/V profile:

```text
D0_A(k_A | p_D_LV)
= w_L * L_A(k_A | p_L)
  + w_V * (1 - V_A(k_A | p_V))

w_L >= 0
w_V >= 0
w_L + w_V = 1
```

**Semantic reading.** D combines positive local support with the complement of
excess reconstruction-relevant dispersion. Non-negative normalized weights
make the result a convex combination in `[0,1]` when L and V are applicable.

The v3.50 default profile is:

```text
w_L = 0.6
w_V = 0.4
```

**Semantic reading.** These values preserve the former `0.3 : 0.2` relation
after normalization. They are a declared KSODI v3.50 profile choice, not a
universal constant or an empirically optimal result. Alternative weights must
use a new versioned profile and require application-specific justification or
calibration.

For an explicitly selected L-only profile:

```text
D0_A(k_A | p_D_L_only) = L_A(k_A | p_L)
```

**Semantic reading.** Under this named profile, D is the normalized local
support value because V is not part of the selected component mask.

**Boundary.** `p_D_L_only` and `p_D_LV` are different measurement conditions.
Their values are not naively comparable. The L-only expression must not be used
as a silent fallback after an L/V calculation fails.

If mandatory L is not applicable, or a selected L/V profile has no applicable
V and no predeclared fallback mapping:

```text
D0_A(k_A | p_D) = not_applicable
```

This is an applicability result, not a low discernibility score.

### 4.5 Interpretation

| D range | Bounded interpretation under the declared profile |
| --- | --- |
| high | strong local support and low excess reconstruction-relevant dispersion; continued reconstruction is well supported |
| medium | partial support or moderate excess dispersion; reconstruction may remain possible but less robust |
| low | weak local support or high excess dispersion; the carrier offers little support for continued reconstruction |

No threshold labels are universal. A deployment must version its corridor or
report continuous values without inventing unstated cutoffs.

## 5. Edge Cases, Fairness, Privacy and Retention

### 5.1 Edge cases

- Fewer than two valid V units make V `not_applicable`, not zero.
- Zero or undefined `N_L` makes L and numeric D `not_applicable` unless the
  profile declares a more specific non-numeric state.
- Repeated material inside one event contributes only under a bounded support
  rule. Repetition across events belongs additionally in source-local sequence,
  window and anomaly views.
- A cryptographic or unfamiliar signal may be crisp and repeatable, hence high
  D, while its code, source or context remains unresolved.
- A profile change does not itself represent movement in D.

### 5.2 Fairness and setup boundary

A low D value may reflect an unsuitable detector, carrier mismatch, missing
accessibility accommodation, lossy preprocessing or an under-specified profile
rather than a property of the emitting entity. D must therefore be reported
with its profile and applicability evidence. It must not be used as a proxy for
human competence, language ability, disability, trustworthiness or worth.

### 5.3 Privacy and retention boundary

Raw signals, embeddings, local units, scores, deltas and Hangar distributions
may remain sensitive or personal data. Derived values are not automatically
anonymous. Retention, access, deletion and reuse require a declared governance
basis. The detailed storage contract belongs to the separate implementation
companion.

## 6. Comparability and Source-Local Dynamics

### 6.1 Comparability Contract

Two D states are comparable only when their target-unit granularity, component
mask, detector, carrier, support-unit definition, support ceiling, segmenter,
distance function, expected-variation threshold, normalizer and weight profile
are equal or explicitly mapped as compatible.

Represent the required record for one D state as `r_D,A(k_A)`. Then:

```text
G_cmp_D(r_D,A(k_A), r_D,A(k_A-1)) = true
```

means that the two source-local D records belong to the same declared
trajectory and satisfy the versioned comparability contract. The gate is a
Boolean applicability decision; it is not a similarity score.

### 6.2 Source-Local Dynamics and Separate Diagnostics

The active source-local D value is the selected static D profile result:

```text
D_A(k_A | p_D) = D0_A(k_A | p_D)
```

This identity states that Layer-1 D dynamics operate over already calculated
static D values. It does not add another component.

When the first-difference gate is true:

```text
Delta D_A(k_A)
= D_A(k_A | p_D) - D_A(k_A-1 | p_D)
```

**Semantic reading.** Positive values mean that A's current signal offers more
profile-bound reconstruction support than A's comparable predecessor; negative
values mean less. This is source-local movement, not an A/B comparison and not
causal attribution.

Otherwise:

```text
Delta D_A(k_A) = not_applicable
```

The non-numeric result prevents a profile change, missing predecessor or
trajectory break from becoming false movement.

When three D states support two comparable first differences:

```text
Delta2 D_A(k_A)
= Delta D_A(k_A) - Delta D_A(k_A-1)
```

**Semantic reading.** `Delta2 D` describes change in source-local D movement.
It requires `k_A`, `k_A-1` and `k_A-2` under compatible conditions. It does not
measure acceleration in physical time unless an explicit time mapping and
sampling policy justify that interpretation.

Otherwise:

```text
Delta2 D_A(k_A) = not_applicable
```

An optional one-sided improvement diagnostic may be declared:

```text
B_D_A(k_A) = max(0, Delta D_A(k_A))
```

**Semantic reading.** `B_D` retains only applicable positive source-local D
movement. It is not a reward for producing more material and not a canonical D
component. If `Delta D` is not applicable, `B_D` is also `not_applicable`.

Historical-context deviation, reference drift and persistence remain separate
diagnostics. They neither modify nor penalize canonical D.

## 7. Sigma and Sigma(Hangar)

Let `W_A` be a declared source-local window of A's trajectory. Define typed
applicable subsets:

```text
W_app_D,A
= {k_A in W_A | D_A(k_A | p_D) is applicable under the window profile}

W_app_DeltaD,A
= {k_A in W_A | Delta D_A(k_A) is applicable and comparable}

W_app_Delta2D,A
= {k_A in W_A | Delta2 D_A(k_A) is applicable and comparable}
```

**Semantic reading.** Each set selects only records valid for its own object
type. Static values, first differences and second differences therefore retain
separate denominators and are never collapsed into one untyped sample.

For a non-empty static subset:

```text
Dbar_A(W_A) = mean({D_A(k_A) | k_A in W_app_D,A})
Dmin_A(W_A) = min({D_A(k_A) | k_A in W_app_D,A})
Dvar_A(W_A) = var({D_A(k_A) | k_A in W_app_D,A})
```

**Semantic reading.** These are respectively the mean, minimum and variance of
applicable static D values in the declared source-local window. The aggregation
profile must declare whether `var` denotes population or sample variance. If
the static subset is empty, each result is `not_applicable`; a sample-variance
profile must also type a one-record subset as inapplicable rather than divide
by zero.

The typed window view is:

```text
DΣ_A(W_A)
= {
    value: Agg_D({D_A(k_A) | k_A in W_app_D,A}),
    delta: Agg_DeltaD({Delta D_A(k_A) | k_A in W_app_DeltaD,A}),
    delta2: Agg_Delta2D({Delta2 D_A(k_A) | k_A in W_app_Delta2D,A})
  }
```

**Semantic reading.** `DΣ_A(W_A)` is a typed container, not one scalar. Each
field uses its own declared aggregation function and becomes `not_applicable`
when its subset is empty. If all fields are inapplicable, the complete view is
`not_applicable`.

For a non-empty declared window:

```text
applicability_rate_D_A(W_A) = |W_app_D,A| / |W_A|
```

**Semantic reading.** This rate reports the share of window positions with an
applicable static D value. It does not fill missing values and does not describe
average clarity. If `|W_A| = 0`, the rate is `not_applicable`.

For an event-level Hangar projection, let `H_D,A^(event)` be a declared
source-attributed collection of canonical D records from A. Define separate
applicable subsets for static values, first differences and second differences.
The corresponding distribution view is:

```text
DΣ_A(Hangar | event_level)
= {
    value_distribution:
      distribution_view({D_A(k_A) | r_D,A(k_A) in H_app_D,A^(event)}),
    delta_distribution:
      distribution_view({Delta D_A(k_A)
                         | r_D,A(k_A) in H_app_DeltaD,A^(event)}),
    delta2_distribution:
      distribution_view({Delta2 D_A(k_A)
                         | r_D,A(k_A) in H_app_Delta2D,A^(event)})
  }
```

**Semantic reading.** The Hangar preserves distributions of the three distinct
object types with their provenance and applicability masks. The explicit
`event_level` profile prevents event records from being mixed silently with
window summaries, trajectories or other Hangar objects. Other object types
require their own named projection profile. The view may expose collapse,
sparse-support regions, outliers or changing dispersion. It does not create a
shared A/B space by itself and does not explain causality.

An optional persistence diagnostic may later be defined as:

```text
P_D_A(W_A) = versioned source-local persistence diagnostic
```

This line is a named interface placeholder, not a completed formula. Until a
separate definition declares its inputs, profile, range and applicability, it
must not be numerically implemented or reported as canonical D.

## 8. Relational Boundary

Operator D ends with source-local views. After distinguishable trajectories
pass a separately declared `R0` gate, a later operator-specific relational D
diagnostic may be researched. It requires its own pairing index `j`,
comparability, applicability, name and interpretation.

Such a future diagnostic:

- does not change `D_A` or `D_B`;
- is not complete `Z`, canonical `IK_rel` or an R-family result;
- must not be inferred from a shared channel, timestamp, exchange or similar D
  values;
- remains v3.60 Future Work unless separately released.

## 9. Formal Summary and Variable Reference

### 9.1 Compact Formula Block

```text
Target event:
e_A(k_A), with stable or provisional source identity and declared trajectory

Profile:
p_D = (p_L, p_V, detector_profile, carrier_profile,
       segmenter_profile, normalizer_profile, weight_profile,
       applicability_profile)

Mandatory local support:
L_A(k_A | p_L)
= clip(n_effective_support_units_A(k_A | p_L)
       / N_L(q_A(k_A), p_L), 0, 1)

Optional full-profile dispersion for m >= 2 valid local units:
V_raw_A(k_A | p_V)
= (2 / (m * (m - 1))) * sum_{i < j} d_p_V(u_i, u_j)

V_A(k_A | p_V)
= clip((V_raw_A(k_A | p_V) - tau_expected_p_V)
       / (1 - tau_expected_p_V), 0, 1)

Full L/V profile:
D0_A(k_A | p_D_LV)
= w_L * L_A(k_A | p_L) + w_V * (1 - V_A(k_A | p_V))
where w_L >= 0, w_V >= 0 and w_L + w_V = 1

v3.50 default: w_L = 0.6, w_V = 0.4

Explicit L-only profile:
D0_A(k_A | p_D_L_only) = L_A(k_A | p_L)

Applicability:
mandatory component failure or undeclared fallback -> D0_A = not_applicable

Common Layer-1 result handoff:
successful applicable finite D0_A -> operator_result_status = numeric
non-numeric D0_A -> operator_result_status in
  {not_selected, not_observable, not_applicable}, with reason retained

Source-local value:
D_A(k_A | p_D) = D0_A(k_A | p_D)

Comparable first difference:
Delta D_A(k_A) = D_A(k_A | p_D) - D_A(k_A-1 | p_D)

Comparable second difference:
Delta2 D_A(k_A) = Delta D_A(k_A) - Delta D_A(k_A-1)

Typed window and Hangar views:
DΣ_A(W_A) = {value, delta, delta2}
DΣ_A(Hangar | event_level)
= {value_distribution, delta_distribution, delta2_distribution}
```

This block is a compact index. The adjacent semantic and applicability rules
in Sections 3 through 8 remain part of the definition.

### 9.2 Variable Reference

| Variable | Semantic role |
| --- | --- |
| `e_A(k_A)` | One observable target event attributed to A or one provisional observed source at local trajectory index `k_A` |
| `q_A(k_A)` | Observable target signal carried by that event |
| `n` | Global event index in the declared observation log |
| `k_A` | Source-local trajectory index for A |
| `j` | Later relational pairing/constellation index, not used inside canonical D |
| `p_D` | Complete versioned D measurement profile |
| `p_L` | Versioned local-support profile |
| `p_V` | Versioned reconstruction-relevant dispersion profile |
| `L_A(k_A \| p_L)` | Normalized local observable signal support; mandatory for numeric D |
| `n_effective_support_units_A` | Count of profile-valid units that support signal discernibility/reconstruction |
| `N_L` | Profile-defined support normalizer and saturation basis |
| `U_A(k_A \| p_V)` | Set of valid local units selected under `p_V` |
| `m` | Number of valid local units; not an event index |
| `d_p_V` | Profile-bound normalized pairwise distance in `[0,1]` |
| `V_raw_A` | Mean normalized pairwise local-unit distance |
| `tau_expected_p_V` | Expected local-variation threshold, with `0 <= tau < 1` |
| `V_A(k_A \| p_V)` | Excess reconstruction-relevant local dispersion in `[0,1]` |
| `w_L`, `w_V` | Non-negative versioned component weights summing to one |
| `p_D_LV` | Full D profile with L and V active |
| `p_D_L_only` | Separately declared D profile with only L active |
| `D0_A(k_A \| p_D)` | Static profile-bound D value or typed non-numeric state |
| `D_A(k_A \| p_D)` | Source-local D value used for trajectory views |
| `r_D,A(k_A)` | Stored D record required by the comparability gate |
| `G_cmp_D` | Boolean comparability gate for two source-local D records |
| `Delta D_A(k_A)` | First source-local difference under comparable conditions |
| `Delta2 D_A(k_A)` | Change in source-local D movement across three comparable states |
| `B_D_A(k_A)` | Optional positive-movement diagnostic; not a D component |
| `W_A` | Declared source-local observation window |
| `DΣ_A(W_A)` | Typed applicability-aware D window view |
| `H_D,A^(event)` | Declared source-attributed event-record collection used by the event-level Hangar projection |
| `DΣ_A(Hangar \| event_level)` | Typed source-attributed D event-level distribution view |
| `P_D_A(W_A)` | Reserved interface for a separately defined persistence diagnostic |

## 10. Public Implementation Boundary

Storage fields, algorithm order, typed status handling, profile validation,
tests, privacy controls and implementation prohibitions are defined separately
in [Operator D Implementation Companion](./KSODI_Operator-D_Implementation-Companion_V350.md).

The companion operationalizes one conditional profile-oriented implementation
contract; it does not narrow the carrier-neutral method or make its detector,
carrier, storage or data-flow choices mandatory. It may not silently change the
canonical D question, component semantics, weights, applicability, source
identity, trajectory discipline or relational boundary. If the companion and
this method appear to differ, this method controls and the mismatch must remain
visible until reviewed.
