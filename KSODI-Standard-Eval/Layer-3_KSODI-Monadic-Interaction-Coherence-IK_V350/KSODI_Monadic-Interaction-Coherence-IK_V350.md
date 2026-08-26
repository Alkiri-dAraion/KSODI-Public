# KSODI IK - Source-Attributed Monadic Coherence Projection v3.50

This file defines the carrier-neutral IK method against the typed Z contract.
Storage schemas,
pseudocode, migration and test fixtures belong in the separate companion:

- [`KSODI_Monadic-Interaction-Coherence-IK_Implementation-Companion_V350.md`](./KSODI_Monadic-Interaction-Coherence-IK_Implementation-Companion_V350.md)

## 0. What IK is and what it does

IK asks one narrow projection question:

> How strongly does one complete, source-attributed Z state project onto one
> declared and versioned monadic coherence axis?

For one target event `e_A(k_A)`, IK receives the typed Layer-2 record and, when
the complete numerical state exists, projects

```text
Z_A(k_A) = [K_A(k_A), S_A(k_A), O_A(k_A), D_A(k_A), I_A(k_A)]
```

onto one weight vector. IK is therefore not a sixth observation and does not
repair, impute or reinterpret a Z coordinate.

The essential distinction is:

```text
canonical IK uses complete canonical Z
reduced IK^[M] uses one explicit fixed coordinate set M
IK^[M] is not canonical IK
relational coherence begins only after the exact open R0 contract declared by
its branch; current dyadic IK_rel requires explicit dyadic pairing and open
numeric canonical complete dyadic R0 under the exact required profile
```

IK is not truth, utility, safety, compliance, alignment, resonance or an
overall judgment of an entity. A high value means only strong projection onto
the declared axis.

### 0.1 Minimal practical reading

1. Resolve one typed Z record for one source-attributed target event.
2. Select one named, versioned IK profile.
3. Validate non-negative weights whose sum is one.
4. Construct canonical IK only from complete `Z_A(k_A)`.
5. If the complete Z state does not exist, preserve `T_Z`; do not substitute
   zero and do not call a renormalized subset canonical IK.
6. If a reduced question is justified, declare non-empty `M` and report
   `IK_A^[M]` with its own profile and coverage.
7. Compute dynamics and windows only under stable identity, profile and active
   coordinate contracts.

### 0.2 How to read this file

Sections 1-3 establish the reader bridge, identity and typed input. Sections
4-5 define canonical and reduced projections. Sections 6-8 define comparable
dynamics, windows and Hangar views. Sections 9-11 fix downstream, privacy and
formal boundaries.

## 1. Bounded application examples

### 1.1 Human-chatbot interaction

Let `A` denote the human trajectory and `B` the chatbot trajectory. A response
from `B` is evaluated first as its own event `e_B(k_B)`. If all five final
Layer-1 result records are numeric and identity-aligned, canonical `Z_B(k_B)` and
then canonical `IK_B(k_B)` may be constructed.

The human and chatbot values remain separate. Two scalar IK values do not
establish shared meaning, acknowledgement, coupling or relational coherence.

### 1.2 Unknown Morse-like signal

An unknown signal may support numeric D and I observations while O is
`not_observable` and other coordinates are not selected. Then the typed Z
record exists, but complete Z and canonical IK do not.

A declared diagnostic such as

```text
IK_A^[D,I](k_A)
```

may be computed only if D and I are numeric and its two-coordinate axis is
named and versioned. It must not be reported as full IK or as evidence about
the unknown source's total coherence.

## 2. Architectural position and identity

### 2.1 Position after Z

```text
Layer 1:  K / S / O / D / I
                 |
Layer 2:         Z and T_Z
                 |\
                 | \-> KSODI Full: R0 -> relational branches
                 |
Layer 3:         IK or named IK^[M]  [monadic Standard-Eval]
```

Z-state dynamics and IK-projection dynamics are parallel diagnostics. IK does
not replace `Delta Z`, and `Delta Z` does not require IK. The R0 branch starts
from distinguishable typed Z trajectories plus its own explicit pairing or
constellation contract; it neither consumes IK nor follows from IK.

### 2.2 Atomic IK evaluation unit

The canonical monadic target is:

```text
e_A(k_A)
```

where `A` is one stable or explicitly provisional source identity and `k_A`
is its source-local trajectory position. Global event index `n`, another
source's `k_B`, relational index `j` and pairing map `pi(j)` remain distinct.

An IK record must inherit the complete Z identity tuple and add:

```text
target_event_id
source_entity_id
source_attribution_status
emitting_entity_id, if established
trajectory_id
global_event_index n
local_trajectory_index k_A
ik_profile_id
ik_profile_version
weight_vector
projection_kind = canonical | reduced
active_coordinate_set
```

No IK calculation may combine coordinates from different source events,
profiles or trajectory positions.

## 3. Typed input contract

### 3.1 Required Z input

IK consumes the typed Z record, including:

```text
T_Z,A(k_A)
= [status_K, status_S, status_O, status_D, status_I]
```

with each status in:

```text
numeric(value in [0,1])
not_selected
not_observable
not_applicable
```

The derived binary `A_Z` may assist filtering, but it cannot replace `T_Z` or
its reasons and provenance.

### 3.2 Complete-input gate

Canonical IK is eligible only when:

```text
complete_Z_state = complete
Z_A(k_A) in [0,1]^5 exists
all inherited identities and profiles are valid
```

The presence of five storage fields is insufficient. Every coordinate must be
numeric under the selected Z view.

### 3.3 IK result type

The external result domain is:

```text
numeric(value in [0,1])
not_selected
not_observable
not_applicable
```

Recommended propagation for canonical IK:

| Condition | IK status | Required retention |
| --- | --- | --- |
| no IK profile selected | `not_selected` | typed Z reference and selection reason |
| complete Z and valid profile | `numeric` | Z reference, profile and weights |
| incomplete Z with any required `not_observable` coordinate | `not_observable` | full `T_Z` and coordinate reasons |
| incomplete Z only because required coordinates are `not_selected` or `not_applicable` | `not_applicable` | full `T_Z` and coordinate reasons |
| invalid identity, malformed weights or calculation failure | no valid IK result | processing error separate from result status |

This precedence communicates that a required observation could not be made.
It does not erase the other coordinate statuses retained in `T_Z`.

## 4. Coherence-axis profile

Let the canonical weight vector be:

```text
w(p_IK) = [w_K, w_S, w_O, w_D, w_I]
```

with:

```text
w_X >= 0
sum_X w_X = 1
```

The profile `p_IK` defines the projection axis. It must identify the weight
vector, coordinate order, purpose, version and status.

The transparent equal-weight reference profile is:

```text
w_ref = [0.2, 0.2, 0.2, 0.2, 0.2]
```

It is a declared reference axis, not an empirical optimum or universal claim.
Domain, learned or adaptive axes are different profiles and require separate
validation and comparability rules.

A zero weight does not waive the complete-Z requirement for canonical IK. If a
profile intentionally excludes coordinates, it is clearer to declare a
reduced axis and `IK^[M]`.

## 5. Canonical and reduced projections

### 5.1 Canonical IK

For complete Z and a valid profile:

```text
IK_A(k_A | p_IK)
= w_K K_A(k_A)
+ w_S S_A(k_A)
+ w_O O_A(k_A)
+ w_D D_A(k_A)
+ w_I I_A(k_A)
```

Equivalently:

```text
IK_A(k_A | p_IK) = w(p_IK) dot Z_A(k_A)
IK_A(k_A | p_IK) in [0,1]
```

Interpretation is relative to the selected axis:

| Signal | Bounded meaning |
| --- | --- |
| high IK | strong projection onto the declared monadic axis |
| middle IK | mixed projection on that axis |
| low IK | weak projection on that axis |

### 5.2 Declared reduced projection

For one fixed, non-empty coordinate set

```text
M subset of {K,S,O,D,I}
```

and only when every coordinate in `M` is numeric:

```text
IK_A^[M](k_A | p_IK^[M])
= sum_(X in M) w_tilde_X X_A(k_A)

w_tilde_X >= 0
sum_(X in M) w_tilde_X = 1
```

If a reduced profile is derived from canonical weights, the derivation is:

```text
w_tilde_X = w_X / sum_(Y in M) w_Y
```

and requires a positive denominator. Store the original profile, denominator
and derived profile ID.

`IK^[M]` changes the projection question. It is not a missing-data repair and
is not interchangeable with canonical IK or another `IK^[N]`.

The former generic label `IK_applicable` is retired because it hides whether
the active set changed. Legacy values must migrate to an explicit `M` where it
can be recovered; otherwise they remain legacy, non-comparable records.

## 6. Comparability and dynamics

### 6.1 Comparability gate

Two canonical IK values are comparable only when they preserve:

- source identity and intended source-local trajectory;
- evaluation-unit granularity and context scope;
- Layer-1 and Z definitions, versions and coordinate order;
- canonical projection kind;
- identical IK profile and weight vector;
- complete numeric Z at every required point.

Two reduced values additionally require the same fixed `M` and same reduced
profile. Canonical and reduced values are not directly comparable.

### 6.2 First and second differences

For comparable canonical values:

```text
Delta IK_A(k_A)
= IK_A(k_A) - IK_A(k_A-1)
in [-1,1]

Delta2 IK_A(k_A)
= Delta IK_A(k_A) - Delta IK_A(k_A-1)
in [-2,2]
```

Under stable weights and complete comparable Z states:

```text
Delta IK_A(k_A) = w dot Delta Z_A(k_A)
```

The identity does not hold across changing profiles or active sets. A change
in `T_Z` is a categorical status transition, not numeric IK drift.

Reduced dynamics are named `Delta IK_A^[M]` and `Delta2 IK_A^[M]` and require
the same fixed `M` and profile at all points.

### 6.3 Changing axes

If weights change, do not report a canonical `Delta IK`. An implementation may
separately diagnose state movement and axis movement, but must name both terms
and retain both profiles. The companion gives the bounded decomposition.

## 7. Windows and Sigma

For a declared non-empty source-local window `W_A`, define the complete
compatible subset:

```text
W_A^IK
= {k_A in W_A | canonical IK_A(k_A | p_IK) is numeric and comparable}

coverage_IK(W_A) = |W_A^IK| / |W_A|
```

`|W_A|` must be positive. An empty or invalid window produces no valid numeric
coverage or aggregate; it must not be represented through `0/0`, zero coverage
or a numeric zero aggregate.

For one declared aggregator `Agg_IK`:

```text
IK_Sigma,A(W_A | p_IK)
= Agg_IK({IK_A(k_A | p_IK) | k_A in W_A^IK})
```

The aggregator, minimum count and coverage threshold are versioned. A numeric
aggregate without coverage is incomplete reporting.

For the arithmetic mean, stable weights and the identical complete subset:

```text
mean(IK_A) = w dot mean(Z_A)
```

The equality is linear, not a reason to mix different subsets. Coordinate-wise
means, imputed Z means and changing profiles do not define canonical
`IK_Sigma`.

Reduced window projections must disclose the same fixed `M`, reduced profile,
subset and coverage. Deltas between windows require compatible window policy,
profile and projection kind.

## 8. Sigma(Hangar)

Hangar stores derived distribution views, not a new monadic formula. An IK
Hangar may contain typed point records, compatible window aggregates and
declared distribution diagnostics.

Required stratification includes:

- canonical versus reduced projection;
- `M` for every reduced record;
- IK profile and version;
- source/context scope and window policy;
- numeric coverage and non-numeric status counts;
- distribution-distance definition for cross-window drift.

Never pool canonical IK, changing `M`, changing weight profiles or categorical
statuses into one unlabeled numeric distribution. A Hangar distance is
non-negative distribution movement and must not be confused with signed
`Delta IK`.

Corridor, learned-axis and adaptive-axis analysis remains research work unless
its profile, validation and comparison contract is explicitly accepted.

## 9. Downstream boundaries

### 9.1 Relation to R0

`R0` is evaluated on its separate relational branch from distinguishable typed
monadic Z trajectories and an explicit pairing or constellation contract. It
is not calculated from IK, does not consume IK as a prerequisite and cannot be
opened by two high IK values.

### 9.2 Relation to IK_rel and the R-family

Canonical IK is monadic. Current `IK_rel` is dyadic and begins only after an
explicit dyadic pairing and an open numeric canonical complete dyadic `R0` gate
under the exact required profile. A reduced or n-adic R0 result does not open
that branch. `IK_rel` cannot be inferred from, or reduced to, two scalar IK
values. Any later use of IK, `Delta IK` or reduced projections must satisfy its
own relational basis, applicability, cardinality and profile contract.

IK does not establish receipt, acknowledgement, shared meaning, successful
decoding, coupling, causality or resonance.

## 10. Fairness, privacy, retention and implementation boundary

Weights are governed analytic configuration choices, not observed facts. They
may encode declared priorities, and a changed profile may change rankings
without any change in observations. Report the profile and avoid
cross-group or cross-domain interpretation without validation.

IK, reduced projections, dynamics, windows and Hangar views may remain
identifiable or linkable even without raw text. Retain the minimum data needed
for the declared purpose; protect source IDs, trajectory maps and provenance;
do not describe pseudonymized values as anonymous.

The mathematical method is authoritative. The companion is subordinate
implementation guidance. No storage convention, threshold or software default
may silently redefine the projection.

## 11. Formal summary and variable reference

### 11.1 Compact contract

```text
# typed Layer-2 input
T_Z,A(k_A) preserves numeric / not_selected / not_observable / not_applicable

# canonical profile
w(p_IK) >= 0
sum_X w_X = 1

# complete canonical projection
complete Z_A(k_A) -> IK_A(k_A | p_IK) = w dot Z_A(k_A)

# reduced, visibly non-canonical projection
M != empty
all X in M numeric
IK_A^[M](k_A | p_IK^[M]) = sum_(X in M) w_tilde_X X_A(k_A)

# source-local comparable dynamics
Delta IK_A(k_A) = IK_A(k_A) - IK_A(k_A-1)
Delta2 IK_A(k_A) = Delta IK_A(k_A) - Delta IK_A(k_A-1)
Delta IK_A(k_A) = w dot Delta Z_A(k_A)  # only under stable complete contract

# windows
IK_Sigma,A(W_A) = Agg_IK({compatible numeric IK_A(k_A)})
report coverage_IK(W_A)

# relational boundary
IK is monadic
R0 does not derive from IK
current dyadic IK_rel begins only after explicit dyadic pairing and open
numeric canonical complete dyadic R0 under the exact required profile; it is
not two scalar IK values
```

### 11.2 Variable reference

| Variable | Semantic role |
| --- | --- |
| `e_A(k_A)` | source-attributed target event |
| `T_Z,A(k_A)` | mandatory typed five-coordinate status vector |
| `Z_A(k_A)` | complete canonical numerical state |
| `p_IK` | named and versioned canonical projection profile |
| `w(p_IK)` | canonical coherence-axis weights |
| `IK_A(k_A | p_IK)` | canonical monadic projection |
| `M` | explicit non-empty coordinate set for a reduced view |
| `p_IK^[M]` | named reduced projection profile |
| `IK_A^[M]` | visibly reduced, non-canonical projection |
| `Delta IK_A`, `Delta2 IK_A` | comparable source-local projection dynamics |
| `W_A^IK` | complete compatible subset used by a window |
| `coverage_IK(W_A)` | numeric comparable window coverage |
| `IK_Sigma,A(W_A)` | declared aggregate over compatible IK values |
| `R0` | relational comparability gate, independent of IK construction |
| `IK_rel` | strictly dyadic relational coherence branch after explicit dyadic pairing and open numeric canonical complete dyadic R0 under the exact required profile |

### 11.3 Consistency tests

A conforming method or implementation must satisfy:

1. no canonical IK without complete canonical Z;
2. no status loss from `T_Z` to a binary mask;
3. no zero fill or silent subset renormalization;
4. every reduced value discloses fixed `M` and its profile;
5. canonical and reduced values are not mixed in dynamics or windows;
6. the projection identity is claimed only under stable complete conditions;
7. weights are non-negative, sum to one and are versioned;
8. windows are non-empty, and coverage plus non-numeric statuses accompany aggregate views;
9. IK remains monadic and does not open or replace R0;
10. IK_rel and the R-family remain outside this method.

## 12. Separate implementation companion

The adjacent implementation companion supplies conditional schemas,
pseudocode, migration rules, examples and tests. It must preserve this method's
identity, typed-status, projection-kind and relational-boundary contracts.
