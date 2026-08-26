# KSODI State Vector Z - Source-Attributed Interaction State v3.50

Status: public v3.50 reference release, strictly reviewed and released on
2026-08-26. This file is the authoritative carrier-neutral Layer-2 Z method.
Implementation storage, pseudocode, migration and test fixtures belong in the
separate companion:

- [`KSODI_State-Vector-Z_Implementation-Companion_V350.md`](./KSODI_State-Vector-Z_Implementation-Companion_V350.md)

## 0. What Z is and what it does

Z asks one narrow compositional question:

> Which five Layer-1 coordinate results belong to the same source-attributed
> target event, and do their result types permit one complete numerical state
> vector?

Z does not measure a sixth property. It assembles the five separately defined
Layer-1 results in canonical coordinate order:

```text
(K, S, O, D, I)
```

For one target event `e_A(k_A)`, every coordinate keeps its own operator
profile, basis, status and provenance. Z confirms that the records share the
same target identity, source identity and trajectory position before it
constructs a vector.

The essential distinction is:

```text
typed Z record exists for every valid assembly attempt
complete numeric Z exists only when all five coordinate statuses are numeric
partial projection is not complete Z
```

### 0.1 Minimal practical reading

1. Resolve one source-attributed target event.
2. Collect exactly one final static result record for each of K, S, O, D
   and I.
3. Preserve each coordinate status:
   `numeric`, `not_selected`, `not_observable` or `not_applicable`.
   A processing failure produces no valid coordinate result and therefore no
   valid Z assembly record.
4. Derive the binary numeric-availability mask from those statuses.
5. Construct canonical `Z_A(k_A) in [0,1]^5` only if all five coordinates are
   numeric and identity-aligned.
6. Name every reduced coordinate view as a partial projection with its active
   set and status vector.
7. Compare states only within the same source trajectory and only after a
   declared comparability gate passes.

### 0.2 How to read this file

- Section 1 shows two bounded examples.
- Sections 2 and 3 define identity, result types and complete/partial Z.
- Sections 4 and 5 define dynamics, norms and status transitions.
- Section 6 defines windows and Hangar views.
- Sections 7 and 8 define downstream and governance boundaries.
- Section 9 contains the compact contract and variable reference.

## 1. Bounded application examples

The examples demonstrate the same Z assembly contract in different domains.
They do not claim that language, chatbot systems and unknown signals are
equivalent.

### 1.1 Human-chatbot interaction

Suppose a human A contributes `e_A(k_A)` and a chatbot B later contributes
`e_B(k_B)`.

Each event receives its own Layer-1 records:

```text
e_A(k_A) -> K_A, S_A, O_A, D_A, I_A -> typed record R_Z,A(k_A)
e_B(k_B) -> K_B, S_B, O_B, D_B, I_B -> typed record R_Z,B(k_B)
```

If all five A coordinates are numeric, Z may construct:

```text
Z_A(k_A) = (K_A, S_A, O_A, D_A, I_A)
```

If the chatbot used reference material that the evaluator cannot inspect, its O
record may be `not_observable`. The B status vector then preserves that fact:

```text
T_Z,B(k_B)
= (numeric, numeric, not_observable, numeric, numeric)
```

There is a valid typed B record, but no complete numeric `Z_B(k_B)`. A declared
four-coordinate diagnostic may be formed, but it must carry its active set and
must not be called complete Z or canonical IK.

The shared conversation does not create `Z_AB`. A and B remain distinguishable
until a later method explicitly pairs their trajectories.

### 1.2 Unknown Morse-like signal

Let `e_U(k_U)` be one observed signal group attributed to provisional source U.
The observer may obtain numeric I and D values while codebook grounding,
structure and context remain unavailable or inapplicable:

```text
T_Z,U(k_U)
= (not_observable, not_observable, not_applicable, numeric, numeric)
```

This is informative. It states that an impulse and discriminable signal are
observable without pretending that the observer has reconstructed a complete
five-dimensional state.

Repeated numeric I/D observations may support a separately named partial
trajectory diagnostic. They do not prove meaning, source identity,
acknowledgement, coupling or a relational handshake.

## 2. Canonical identity and assembly boundary

### 2.1 Atomic Z evaluation unit

One Z assembly attempt belongs to exactly one Layer-1 target event:

```text
e_A(k_A)
= target_event_id
+ source_entity_id
+ source_attribution_status
+ emitting_entity_id, if established
+ trajectory_id_A
+ local_trajectory_index k_A
+ global_event_index n
```

Canonical indices:

```text
n        = global observable-event index
k_A      = local position in source trajectory A
k_B      = local position in source trajectory B
j        = later relational pairing or constellation index
pi(j)    = explicit map from j to source-local positions
```

An implementation field `t` may represent a timestamp, step or legacy turn
index only when it is explicitly mapped to the canonical event and trajectory
identities. It must not imply a global shared predecessor.

### 2.2 Required coordinate records

For every `X in {K,S,O,D,I}`, Z consumes one final static Layer-1 result
record:

```text
r_X,A(k_A)
= (
    operator_id,
    method_version,
    target_event_id,
    source_entity_id,
    source_attribution_status,
    emitting_entity_id if established,
    trajectory_id,
    local_trajectory_index,
    global_event_index,
    result_status,
    result_value if numeric,
    profile_id and version,
    basis_id,
    component or gate provenance
  )
```

Z does not recalculate operator values. It validates and composes their records.

### 2.3 Assembly gate

The identity assembly gate opens only when:

```text
G_Z,identity,A(k_A) = true
```

where all five coordinate records:

- identify the same target event;
- identify the same source or provisional source;
- identify the same trajectory and local position;
- use the canonical coordinate order;
- contain exactly one final static result record per operator;
- retain their own profile, basis, status and provenance.

If the identity gate fails, no valid Z record is produced. This is an assembly
error, not `not_applicable` and not a numeric zero.

Context events, reference objects, tool outputs and prior events used inside an
operator basis remain provenance inputs. They do not become additional source
coordinates or change the target identity of Z.

## 3. Typed Z record, complete vector and partial projections

### 3.1 Common coordinate-result domain

For each coordinate:

```text
tau_X,A(k_A)
in {numeric, not_selected, not_observable, not_applicable}
```

The typed Z status vector is mandatory:

```text
T_Z,A(k_A)
= (
    tau_K,A(k_A),
    tau_S,A(k_A),
    tau_O,A(k_A),
    tau_D,A(k_A),
    tau_I,A(k_A)
  )
```

Gate-specific reasons such as `not_visible_to_evaluator`, empty expected set,
missing detector or inadmissible reference space remain inside the coordinate
record. `T_Z` preserves the common result type; it does not erase the reason.

`processing_failure` is not a fifth coordinate-result status. If a Layer-1
calculation produces no valid final result record, Z cannot turn that failure
into `not_applicable`, `not_observable`, a mask bit or numeric zero. The
assembly fails and no valid `R_Z` is constructed.

### 3.2 Derived numeric-availability mask

The binary mask is derived from `T_Z`:

```text
A_X,A(k_A) = 1 if tau_X,A(k_A) = numeric, else 0

A_Z,A(k_A)
= (A_K,A, A_S,A, A_O,A, A_D,A, A_I,A)
```

`A_Z` answers only whether a numeric coordinate is available. It cannot and
must not replace `T_Z`, because all three non-numeric states map to zero in the
mask.

### 3.3 Complete canonical Z

Define:

```text
G_Z,complete,A(k_A)
:= G_Z,identity,A(k_A)
   and A_Z,A(k_A) = (1,1,1,1,1)
```

Only when this gate is open:

```text
Z_A(k_A)
= (K_A(k_A), S_A(k_A), O_A(k_A), D_A(k_A), I_A(k_A))

Z_A(k_A) in [0,1]^5
```

The complete vector preserves references to every constitutive coordinate
record. It does not overwrite their profiles or provenance.

If the gate is closed, the typed Z record remains valid but:

```text
complete_Z_state,A(k_A) = not_complete
Z_A(k_A) is not constructed
```

`not_complete` is a Z assembly state, not a fifth Layer-1 result type and not a
numeric vector.

### 3.4 Typed Z record

The method-level record is:

```text
R_Z,A(k_A)
= (
    identity,
    ordered coordinate-record references,
    T_Z,A(k_A),
    A_Z,A(k_A),
    G_Z,identity,A(k_A),
    G_Z,complete,A(k_A),
    Z_A(k_A) if complete,
    provenance
  )
```

`R_Z` is not itself a sixth coordinate. It is the typed assembly record.

### 3.5 Declared partial projection

Let `M` be a non-empty declared subset of the five coordinates. A partial
numeric projection is permitted only when every coordinate in `M` is numeric:

```text
Z_A^{[M]}(k_A)
= P_M Z_record,A(k_A)
= (X_A(k_A)) for X in ordered M
```

The projection must retain:

- `M` and its order;
- the full `T_Z` and `A_Z` records;
- the partial-projection profile and reason;
- coordinate profiles and provenance.

It must be named `Z^{[M]}`, `partial_Z` or another visibly reduced form. It is
not canonical `Z_A(k_A)`, is not automatically comparable with another mask
and must not silently fill canonical IK.

No imputation is part of the v3.50 Z method. A separately proposed imputation
profile would create a derived estimate, not an observed canonical Z.

## 4. Comparability and source-local dynamics

### 4.1 Z comparability gate

Two complete Z records are comparable only when:

```text
G_cmp_Z,A(k_A) = true
```

The gate requires at least:

- same source and trajectory identity;
- consecutive or otherwise explicitly paired local positions;
- same Z method version and coordinate order;
- compatible operator method/profile versions for every coordinate;
- compatible measurement-basis types and visibility conditions;
- compatible coordinate scales;
- compatible complete/partial view type;
- declared predecessor and provenance.

Similarity of timestamps, conversation membership or shared context is not a
comparability gate.

### 4.2 Complete first difference

If both states are complete and `G_cmp_Z,A(k_A) = true`:

```text
Delta Z_A(k_A)
= Z_A(k_A) - Z_A(k_A-1)
```

Component range:

```text
Delta Z_X,A(k_A) in [-1,1]
```

Otherwise complete `Delta Z_A(k_A)` is `not_applicable` with the failed gate
reason retained. Coordinates are not silently skipped.

### 4.3 Complete second difference

If three consecutive complete states satisfy the required comparability gates:

```text
Delta2 Z_A(k_A)
= Delta Z_A(k_A) - Delta Z_A(k_A-1)
```

Component range:

```text
Delta2 Z_X,A(k_A) in [-2,2]
```

Otherwise complete `Delta2 Z_A(k_A)` is `not_applicable`.

### 4.4 Partial dynamics

A partial difference may be calculated only over one fixed declared coordinate
set `M` that is numeric and comparable in every required state:

```text
Delta Z_A^{[M]}(k_A)
= Z_A^{[M]}(k_A) - Z_A^{[M]}(k_A-1)
```

For `Delta2 Z^{[M]}`, the same `M` must remain valid across all three positions.
Changing `M` creates a new diagnostic profile and blocks naive comparison.

### 4.5 Status transitions remain categorical

Numeric drift does not describe a change such as `not_observable -> numeric`.
Store a separate categorical transition record:

```text
Delta T_Z,A(k_A)
= (tau_X,A(k_A-1) -> tau_X,A(k_A)) for every coordinate X
```

A newly observable coordinate may change the available vector dimension without
implying that its unknown former numeric value moved from zero.

## 5. Drift norms and interpretation

### 5.1 Complete-state norms

For comparable complete states:

```text
Drift_L1,A(k_A)
= sum_X |Delta Z_X,A(k_A)|

Drift_L1_norm,A(k_A)
= Drift_L1,A(k_A) / 5

Drift_L2,A(k_A)
= sqrt(sum_X (Delta Z_X,A(k_A))^2)

Drift_L2_norm,A(k_A)
= Drift_L2,A(k_A) / sqrt(5)
```

Ranges:

```text
Drift_L1 in [0,5]
Drift_L1_norm in [0,1]
Drift_L2 in [0,sqrt(5)]
Drift_L2_norm in [0,1]
```

### 5.2 Partial-state norms

For a fixed comparable partial set `M`:

```text
Drift_L1_norm,A^{[M]}(k_A)
= sum_{X in M} |Delta Z_X,A(k_A)| / |M|

Drift_L2_norm,A^{[M]}(k_A)
= sqrt(sum_{X in M} (Delta Z_X,A(k_A))^2) / sqrt(|M|)
```

These results must display `M` and must not be compared naively with a complete
five-coordinate norm or another partial mask.

### 5.3 Interpretation boundary

Drift means state-space movement under a declared comparable profile. It does
not by itself mean improvement, deterioration, causality, intent, instability
or relational coupling.

`Delta2 Z` describes change in movement and may support early-warning review.
It is not an evaluation score.

## 6. Sigma, Sigma(Hangar) and coverage

### 6.1 Complete source-local window

For a declared non-empty source-local window `W_A`, define one joint complete
subset:

```text
W_complete_Z,A
= {k_A in W_A |
   Z_A(k_A) is complete and compatible with p_ZSigma}
```

A complete window aggregation uses the same positions for all coordinates:

```text
Z_Σ_A(W_A).value
= (
    Agg_K({K_A(k_A) | k_A in W_complete_Z,A}),
    Agg_S({S_A(k_A) | k_A in W_complete_Z,A}),
    Agg_O({O_A(k_A) | k_A in W_complete_Z,A}),
    Agg_D({D_A(k_A) | k_A in W_complete_Z,A}),
    Agg_I({I_A(k_A) | k_A in W_complete_Z,A})
  )
```

Static, Delta and Delta2 window fields remain separate typed records. Empty
applicable sets are `not_applicable`, not zero.

### 6.2 Coverage and coordinate-wise diagnostics

Store:

```text
complete_rate_Z,A(W_A)
= |W_complete_Z,A| / |W_A|

numeric_rate_X,A(W_A)
= # numeric X statuses in W_A / |W_A|
```

These numeric rates require `|W_A| > 0`. An empty or invalid window emits a
typed non-numeric window result under its declared profile; it never evaluates
`0/0` and never reports zero coverage by convention.

If coordinate summaries use different effective subsets, the result is a
coordinate-wise diagnostic, not one joint state-vector aggregate. It must
carry each subset and coverage value.

### 6.3 Hangar view

The complete event-level Hangar set is:

```text
H_Z,A^(event)
= {Z_A(k_A) | k_A in W_complete_Z,A}
```

`Z_Σ_A(Hangar)` is a typed distribution or point-cloud view derived from
canonical records. Partial points may be retained only in mask/status-stratified
collections such as `H_Z,A^{[M]}`; they are not silently embedded by zero filling.

Hangar preserves source, event, trajectory, profile, status, mask, window and
derivation provenance. It does not replace canonical event or Z storage.

## 7. Downstream boundaries

### 7.1 Relation to IK

Canonical monadic IK is a declared projection of complete canonical Z:

```text
IK_A(k_A) = w dot Z_A(k_A)
```

where the IK method controls weights, applicability and interpretation. A
reduced projection from `Z^{[M]}` requires a separately named IK profile and must
not be reported as canonical IK.

Where weights and complete comparability remain stable:

```text
Delta IK_A(k_A) = w dot Delta Z_A(k_A)
```

This is a projection identity, not an independent observation.

### 7.2 Relation to R0 and relational branches

Z_A and Z_B remain separate monadic states and trajectories:

```text
T_A = {R_Z,A(k_A)}
T_B = {R_Z,B(k_B)}
```

R0 receives complete comparable movement derived from distinguishable typed
trajectory records plus an explicit dyadic pairing or n-adic constellation
map. It runs after Z and in parallel to monadic IK. Z does not define the R0
formula, profile or stability threshold.

Only an open numeric canonical complete R0 gate under the exact required
profile may admit a compatible downstream relational construct. Downstream
cardinality must match: current IK_rel is dyadic and is not opened by an
n-adic R0 result. Parallel availability of `Z_A` and `Z_B` does not create
`Z_AB`, shared state, acknowledgement or coupling.

### 7.3 Coordinate order is not a causal chain

```text
canonical Z order:             (K, S, O, D, I)
sender-side formation:          K -> S -> O -> D -> I
receiver-side reconstruction:   I -> D -> O -> S -> K
```

The first is a representation order. The latter two are directed process
topologies. Z does not assert that operators are calculated causally in either
order.

## 8. Fairness, privacy, retention and implementation boundary

Status and mask patterns may reveal which context, source, detector or access
basis was available. Profile IDs, event links, embeddings, hashes and
trajectories may remain identifying even when raw language is deleted.

Retention must therefore be declared for:

- raw target and basis material;
- coordinate evaluation records;
- typed status and reason records;
- complete and partial Z views;
- trajectory, window and Hangar derivations.

Z does not require indefinite storage of raw language. Auditability may use
governed references or approved derived evidence where the operator method and
policy permit it. Derived data is not automatically anonymous.

Implementation-specific schemas, pseudocode, migration mappings, database
choices, API objects, visualization behavior and test fixtures belong in the
subordinate companion. They must not redefine complete Z, erase `T_Z`, impute
missing coordinates or collapse source identities.

## 9. Formal summary and variable reference

### 9.1 Compact contract

```text
# one source-attributed target event
e_A(k_A)

# common coordinate statuses
tau_X,A(k_A)
in {numeric, not_selected, not_observable, not_applicable}

# mandatory typed status vector
T_Z,A(k_A) = (tau_K, tau_S, tau_O, tau_D, tau_I)

# derived numeric-availability mask
A_X,A(k_A) = 1[tau_X,A(k_A) = numeric]
A_Z,A(k_A) = (A_K, A_S, A_O, A_D, A_I)

# complete canonical state only when identity aligns and all five are numeric
G_Z,complete,A(k_A)
= G_Z,identity,A(k_A) and A_Z,A(k_A) = (1,1,1,1,1)

if G_Z,complete,A(k_A):
  Z_A(k_A) = (K_A, S_A, O_A, D_A, I_A) in [0,1]^5
else:
  complete_Z_state,A(k_A) = not_complete
  Z_A(k_A) is not constructed

# visibly partial diagnostic
Z_A^{[M]}(k_A) = ordered numeric projection on declared non-empty M

# complete source-local dynamics only after comparability
Delta Z_A(k_A)  = Z_A(k_A) - Z_A(k_A-1)
Delta2 Z_A(k_A) = Delta Z_A(k_A) - Delta Z_A(k_A-1)

# categorical status movement remains separate
Delta T_Z,A(k_A) = coordinate-wise status transitions

# complete normalized norms
Drift_L1_norm,A = sum_X |Delta Z_X,A| / 5
Drift_L2_norm,A = sqrt(sum_X Delta Z_X,A^2) / sqrt(5)

# partial norms require one fixed displayed M
Drift_L1_norm,A^{[M]} = sum_{X in M} |Delta Z_X,A| / |M|
Drift_L2_norm,A^{[M]} = sqrt(sum_{X in M} Delta Z_X,A^2) / sqrt(|M|)

# complete joint window uses one shared complete subset
W_complete_Z,A = {k_A in W_A | complete and window-compatible Z_A(k_A)}
Z_Σ_A(W_A) = typed coordinate aggregation over W_complete_Z,A

# Hangar remains derived and status-aware
H_Z,A^(event) = {Z_A(k_A) | k_A in W_complete_Z,A}

# downstream branches
Z_A -> IK_A
distinguishable typed trajectories + explicit pairing -> R0
open numeric canonical complete R0 under the exact required profile
  -> separately defined compatible relational branches
current IK_rel additionally requires matching dyadic cardinality
```

### 9.2 Variable reference

| Symbol | Semantic role |
| --- | --- |
| `e_A(k_A)` | one source-attributed target event at local position `k_A` |
| `n` | global observable-event index |
| `k_A`, `k_B` | source-local trajectory indices |
| `j`, `pi(j)` | later relational index and explicit pairing map |
| `r_X,A(k_A)` | complete static Layer-1 result record for coordinate X |
| `tau_X,A(k_A)` | common result status of coordinate X |
| `T_Z,A(k_A)` | mandatory five-coordinate status vector |
| `A_Z,A(k_A)` | derived binary numeric-availability mask; never a substitute for `T_Z` |
| `G_Z,identity,A(k_A)` | identity and record-alignment gate |
| `G_Z,complete,A(k_A)` | gate for complete numeric Z |
| `R_Z,A(k_A)` | typed Z assembly record; not a sixth coordinate |
| `Z_A(k_A)` | complete canonical five-dimensional monadic state |
| `M` | declared ordered coordinate subset for a partial projection |
| `Z_A^{[M]}(k_A)` | visibly partial numeric coordinate projection |
| `G_cmp_Z,A(k_A)` | source-local Z comparability gate |
| `Delta Z_A(k_A)` | complete first source-local state difference |
| `Delta2 Z_A(k_A)` | complete second source-local state difference |
| `Delta T_Z,A(k_A)` | categorical coordinate-status transition record |
| `Drift_L1/L2` | complete raw state-movement norms |
| `Drift_L1/L2_norm` | normalized complete or explicitly partial movement norms |
| `W_A` | declared source-local window |
| `W_complete_Z,A` | shared complete and compatible Z subset of the window |
| `Z_Σ_A(W_A)` | typed joint window aggregation over one shared complete subset |
| `complete_rate_Z,A` | share of positions with complete compatible Z |
| `numeric_rate_X,A` | per-coordinate numeric coverage rate |
| `H_Z,A^(event)` | complete event-level Z point set for Hangar derivation |
| `Z_Σ_A(Hangar)` | derived typed Z distribution or point-cloud view |
| `not_complete` | valid typed Z record without a complete numeric vector |

### 9.3 Consistency tests

| Test | Result | Reason |
| --- | --- | --- |
| source removal | PASS | removing B does not change the identity or construction of A's Z record |
| role reversal | PASS | sender/receiver changes do not rewrite stable source identities |
| status preservation | PASS | `T_Z` distinguishes three non-numeric states that `A_Z` cannot distinguish |
| partial-view honesty | PASS | a reduced mask is explicitly named and cannot fill complete Z or canonical IK |
| dynamics | PASS | complete Delta/Delta2 require same-source complete comparable states; partial dynamics require fixed M |
| layer dependency | PASS | Z consumes Layer-1 records and defines neither operator, IK, R0 nor relational formulas |
| provenance | PASS | event, source, trajectory, coordinate profile, status, mask and pairing metadata remain distinguishable |

## 10. Separate implementation companion

The subordinate companion is:

- [`KSODI_State-Vector-Z_Implementation-Companion_V350.md`](./KSODI_State-Vector-Z_Implementation-Companion_V350.md)

It may operationalize record schemas, validation, partial views, migration,
storage and tests. It must not redefine the complete-state gate, treat `A_Z` as
a replacement for `T_Z`, impute missing coordinates into observed Z or merge
source trajectories.
