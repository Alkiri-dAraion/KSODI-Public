# KSODI R_0 - Typed Monadic-to-Relational Comparability Gate v3.50

> **Status:** public v3.50 reference release - strictly reviewed and released on 2026-08-26.

Status: authoritative reader-first Layer-4 method, strictly reviewed and released 2026-08-26. Mathematical prose
uses `R_0`; path-safe and implementation notation may use `R0`. This file
defines the carrier-neutral gate method. Schemas, pseudocode, migration and
test fixtures belong in the separate companion:

- [`KSODI_Relational-Gate-R_0_Implementation-Companion_V350.md`](./KSODI_Relational-Gate-R_0_Implementation-Companion_V350.md)

## 0. What R_0 is and what it does

`R_0` asks one narrow gate question:

> Do the separately observed, explicitly paired trajectories satisfy one
> declared availability and bounded-drift contract strongly enough for a
> relational comparison to be opened?

`R_0` uses source-local Z movement. It does not compare semantic direction,
movement direction, projection agreement or coupling. The v3.50 reference
profile summarizes the normalized movement magnitudes of the declared
trajectories by their arithmetic mean.

The essential distinction is:

```text
declared pair or constellation comes before R_0
complete comparable Delta Z on every trajectory -> canonical R_0
one fixed explicit coordinate set M -> named R_0^[M]
numeric R_0 result -> gate may be open or closed
non-numeric R_0 result -> gate is not evaluable
incompatible identity/profile/predecessor contracts -> no valid R_0 result
```

An open gate is necessary for downstream relational interpretation but is not
evidence of relation, agreement, shared meaning, coupling or resonance.

### 0.1 Minimal practical reading

1. Preserve distinguishable monadic trajectories.
2. Declare an explicit dyadic pairing `pi(j)` or n-adic constellation map.
3. Resolve each trajectory's source-local predecessor independently.
4. Preserve typed Z and movement availability; do not zero-fill.
5. Use all five coordinates for canonical R0.
6. If a reduced gate is justified, declare one non-empty fixed M and report
   `R0^[M]`.
7. Compute normalized per-trajectory drift and then the declared gate profile.
8. Separate the numeric result status from the derived open/closed gate state.
9. Compare or aggregate only under one stable identity, M, norm and profile.

### 0.2 How to read this file

Sections 1-3 establish examples, identity and typed input. Sections 4-8 define
result state, normalization, canonical and reduced gates. Sections 9-11 cover
n-adic use, dynamics and boundaries. Section 12 gives the compact contract and
tests.

## 1. Bounded application examples

### 1.1 Horse and rider

Horse A and rider B are two distinguishable participants in one declared
observation episode. Their presence together does not establish coupling.

At relational step `j`, the observer pairs one declared position from each
trajectory. R0 asks only whether their separately observed movements meet the
selected stability and availability contract. If the gate opens, later
branches may ask about movement compatibility, geometry or pacing. The horse
and rider may still be moving in unrelated directions—or be perfectly stable
while doing nothing together.

### 1.2 Human-chatbot interaction

Human and chatbot events retain separate source identities and source-local
predecessors. Chronological adjacency in a chat does not create one shared
Delta Z.

If both complete Z trajectories provide comparable complete movement at the
paired step, canonical R0 may be evaluated. If only a fixed subset such as
`M={K,S,D,I}` is admissible on both sides, the result is explicitly
`R0^[K,S,D,I]`, not canonical R0.

## 2. Architectural position and identity

### 2.1 Position

```text
A: K/S/O/D/I -> Z_A -> Delta Z_A --\
                                       R0_AB(j)
B: K/S/O/D/I -> Z_B -> Delta Z_B --/
                                          |
                                          +-> IK_rel and parallel R branches
```

Monadic IK is a parallel branch after Z and is not an input to R0.

### 2.2 Atomic dyadic gate unit

```text
rho_AB(j | pi(j))
pi(j) = (k_A(j), k_B(j))
```

`k_A(j)` and `k_B(j)` identify the paired current positions. Their monadic
predecessors are `k_A(j)-1` and `k_B(j)-1` within their own declared
trajectories, or another explicitly declared source-local predecessor map.

Required identity includes:

- ordered or otherwise explicitly symmetric dyad ID;
- for each paired event: `target_event_id_E`, stable or provisional
  `source_entity_id_E`, explicit `source_attribution_status_E`, and
  `emitting_entity_id_E` only when established;
- for each monadic trajectory: `trajectory_id_E`, global event index `n_E`
  and source-local position `k_E`;
- pairing-map ID and directionality;
- context/comparison scope;
- Z, norm, R0 and threshold profile IDs.

R0 does not discover a pair. The Observer declares it.

### 2.3 Coordinate order

```text
(K,S,O,D,I)
```

is the fixed reporting order. It is not a causal chain and does not merge the
two trajectories.

## 3. Typed Z-movement input

### 3.1 Complete movement

Canonical R0 requires, on both sides:

```text
complete comparable Z at the current source-local position
complete comparable Z at its source-local predecessor
complete numeric Delta Z in [-1,1]^5
```

Each numeric coordinate difference exists only if both static coordinate
records are numeric and comparable. Typed `T_Z`, categorical `Delta T_Z`,
profiles, reasons and provenance remain attached.

### 3.2 Movement-result status

For each coordinate X and trajectory E, an implementation must be able to
distinguish:

```text
numeric(Delta X_E)
not_selected
not_observable
not_applicable
incomparable
```

`incomparable` is a comparison-processing state that blocks a numeric delta;
it does not overwrite either stored static coordinate result and is not an
external R0 result status. A required incomparable movement record blocks the
R0 calculation and produces no valid R0 result; it must not be recoded as
`not_applicable` or numeric zero.

### 3.3 Fixed partial movement

For one explicit non-empty

```text
M subset of {K,S,O,D,I}
```

`Delta Z_E^[M]` exists only when every coordinate in M is numeric and
comparable on trajectory E. Dyadic `R0^[M]` requires the same M for A and B.

M is selected by a versioned analytic profile, not generated as “whatever is
numeric at this event.”

## 4. R0 result and gate state

### 4.1 Result type

The external R0 result domain is:

```text
numeric(value in [0,1])
not_selected
not_observable
not_applicable
```

Recommended propagation:

| Condition | R0 result status |
| --- | --- |
| no R0 profile selected | `not_selected` |
| required movement cannot be observed | `not_observable` |
| a valid declared pair/constellation, predecessor, scope or required fixed-M contract is substantively inapplicable | `not_applicable` |
| all gates and calculations pass | `numeric` |
| required records exist but identity, profile, axis or predecessor contracts are incompatible | no valid result; `incomparable` processing record |
| identity, range, threshold, weight or arithmetic failure | no valid result; processing error |

Retain the typed input reasons from every trajectory.

### 4.2 Derived gate state

Gate state is separate:

```text
if R0.status != numeric:
    gate_state = not_evaluable
else if R0.value >= theta_R0_stable:
    gate_state = open
else:
    gate_state = closed
```

`theta_R0_stable` must be finite and lie in `[0,1]`. The threshold is a
versioned gate-policy parameter, not an empirical fact, a coupling threshold
or action authority.

A numeric value below threshold is a valid numeric R0 result with a closed
gate. It is not `not_applicable`.

## 5. Normalized trajectory drift

Let E denote A or B.

### 5.1 Complete L1 reference norm

```text
d_E,L1(j)
= (1/5) * sum_(X in {K,S,O,D,I}) |Delta X_E(k_E(j))|
in [0,1]
```

L1 is the v3.50 reference norm because every coordinate contribution remains
directly readable and equally bounded under the complete profile.

### 5.2 Complete L2 profile

```text
d_E,L2(j)
= sqrt(sum_X Delta X_E(k_E(j))^2) / sqrt(5)
in [0,1]
```

L2 is a separate versioned profile and is more sensitive to concentrated
movement.

### 5.3 Fixed partial norms

```text
d_E,L1^[M](j)
= (1/|M|) * sum_(X in M) |Delta X_E(k_E(j))|

d_E,L2^[M](j)
= sqrt(sum_(X in M) Delta X_E(k_E(j))^2) / sqrt(|M|)
```

The denominator is the size of the fixed declared M, never an event-wise
availability count.

## 6. Canonical dyadic R0

For complete comparable movement and the L1 reference profile:

```text
R0_raw,AB(j)
= 1 - (d_A,L1(j) + d_B,L1(j)) / 2

R0_AB(j)
= clip(R0_raw,AB(j), 0, 1)
in [0,1]
```

With valid inputs, clipping should not bind; it is a numerical guard.

Interpretation:

| Result | Bounded meaning |
| --- | --- |
| near 1 | low average normalized movement under the declared profile |
| middle | moderate average normalized movement |
| near 0 | high average normalized movement |
| gate open | selected stability threshold is met |
| gate closed | numeric result exists but threshold is not met |

If both trajectories are static, R0 is 1. This confirms only minimal movement,
not connection or compatibility.

## 7. Fixed partial dyadic gate

For the same fixed M on both trajectories:

```text
R0_AB^[M](j)
= clip(1 - (d_A^[M](j) + d_B^[M](j)) / 2, 0, 1)
```

`R0^[M]` is a reduced gate view. It is not canonical R0 and is not comparable
with another `R0^[N]` or complete R0 unless a separate method explicitly
defines that comparison.

The former event-wise shared-active-set construction is retired. It may be
migrated only when its exact M can be recovered. Otherwise the legacy result
remains non-comparable.

## 8. Mean limitation, weights and asymmetry

### 8.1 Mean limitation

The arithmetic mean can mask one-sided movement:

```text
d_A = 0.0
d_B = 0.8
R0 = 0.6
```

Whether the gate opens depends on the threshold profile. Therefore every R0
record retains both per-trajectory drift magnitudes.

### 8.2 Weighted profile

```text
R0_w,AB(j)
= clip(1 - (w_A d_A(j) + w_B d_B(j)), 0, 1)

w_A >= 0
w_B >= 0
w_A + w_B = 1
```

This is a separately named profile. Weights declare how each trajectory's
movement contributes to the gate; they are not empirical facts about either
entity and require justification and versioning.

### 8.3 Asymmetry diagnostic

An optional companion diagnostic is:

```text
a_AB(j) = |d_A(j) - d_B(j)| in [0,1]
```

It exposes one-sided movement but does not alter canonical R0. A later strict
profile may use `1-max(d_A,d_B)`; it is not active canonical v3.50 behavior.

## 9. N-adic extension

Let one declared constellation at relational step q be:

```text
C(q) = {E_1, ..., E_n}
Pi(q) = {k_E(q) | E in C(q)}
n >= 2
```

Every trajectory keeps its own source-local predecessor.

For complete comparable movement under one common norm profile:

```text
R0_C(q)
= clip(1 - (1/n) * sum_(E in C(q)) d_E(q), 0, 1)
```

A separately named weighted constellation profile may use fixed weights:

```text
R0_w,C(q)
= clip(1 - sum_(E in C(q)) w_E d_E(q), 0, 1)

w_E >= 0 for every E
sum_(E in C(q)) w_E = 1
```

Membership order or stable member identity must bind every weight. Weights are
governed analytic configuration choices, not observed facts about members.

For a reduced view, the same fixed M applies to every member:

```text
R0_C^[M](q)
= clip(1 - (1/n) * sum_(E in C(q)) d_E^[M](q), 0, 1)
```

Constellation membership, mapping, symmetry, norm, M and threshold are
versioned. The entity summation variable is not the relational index.

The mean limitation grows with n; store all individual drifts and optional
dispersion/asymmetry diagnostics.

## 10. Comparability, dynamics, windows and Hangar

### 10.1 Comparability

R0 results require the same:

- ordered dyad or constellation semantics;
- pairing/map and relational granularity;
- source-local predecessor policy;
- Layer-1 and Z definitions/versions;
- projection kind: complete or reduced;
- fixed M where reduced;
- norm, aggregation, weights, clipping and threshold profiles.

### 10.2 Relational-index dynamics

For consecutive comparable numeric dyadic results:

```text
Delta R0_AB(j)
= R0_AB(j) - R0_AB(j-1)
in [-1,1]

Delta2 R0_AB(j)
= Delta R0_AB(j) - Delta R0_AB(j-1)
in [-2,2]
```

These are gate-value dynamics over relational index j. Typed input transitions
or movement between open, closed and not-evaluable states are categorical
events, not numeric deltas.

### 10.3 Windows

For a declared non-empty relational window `W_AB`:

```text
W_AB^R0
= {j in W_AB | R0_AB(j) is numeric and comparable}

coverage_R0(W_AB) = |W_AB^R0| / |W_AB|
gate_open_rate(W_AB)
= count(gate_state=open) / |W_AB^R0|
```

`|W_AB|` must be positive before coverage is computed. `gate_open_rate` is
numeric only when `|W_AB^R0| > 0`; otherwise it is non-evaluable, not `0/0` or
zero. The aggregate additionally requires its declared positive minimum count
and coverage threshold.

`R0_Sigma` applies one declared aggregator to the eligible values. Store
minimum count, coverage threshold, result-status counts and gate-state counts.

### 10.4 Hangar

Hangar stores derived gate distributions, not a shared inner state. Partition
by dyad/constellation, pairing policy, complete versus fixed-M profile, norm,
aggregation, threshold and window policy.

Do not pool complete R0, different `R0^[M]` views or non-numeric statuses into
one unlabeled numeric distribution. Distribution distance is not signed
`Delta R0`.

## 11. Handshake and downstream boundaries

The SYN/ACK analogy is functional and bounded. R0 does not implement TCP,
prove receipt, acknowledgement, shared meaning or successful decoding.

R0 does not use IK and does not measure semantic or directional compatibility.
After a compatible open gate:

- current dyadic IK_rel may ask about paired canonical IK movement only after
  explicit dyadic pairing and an open numeric canonical complete dyadic R0
  under its exact required profile;
- R_geom may ask about geometric coupling;
- staged R_pace may ask about defined pacing;
- future signal-media branches may ask their own questions.

These are parallel post-R0 branches with their own cardinality, input and
profile contracts. Reduced `R0^[M]` and n-adic `R0_C` do not open the current
dyadic IK_rel branch. No single value establishes coupling, resonance,
alignment or a controller action.

Observer declaration and an open gate do not manufacture relation. R0 states
only that the selected comparison contract is numerically evaluable and meets
its declared stability threshold.

## 12. Formal summary, privacy and consistency tests

### 12.1 Compact contract

```text
pi(j) = (k_A(j), k_B(j))

complete numeric comparable Delta Z_A and Delta Z_B
-> canonical normalized d_A, d_B
-> canonical R0 = 1 - mean(d_A,d_B)

same fixed non-empty M on both sides
-> R0^[M] = 1 - mean(d_A^[M],d_B^[M])

R0.status = numeric and R0 >= theta
-> gate_state = open

R0.status = numeric and R0 < theta
-> gate_state = closed

R0.status != numeric
-> gate_state = not_evaluable
```

### 12.2 Privacy and retention

Z movements, pairing maps, constellations and gate trajectories may identify
participants or reveal behavioral patterns. Pseudonymization is not anonymity.
Store the minimum needed; protect identities, provenance and mapping records.
No raw text, embeddings, voice or timing data are required by R0.

### 12.3 Consistency tests

1. no R0 without a declared dyad or constellation;
2. no shared predecessor across distinct monadic trajectories;
3. canonical R0 requires complete movement on every trajectory;
4. every reduced R0 declares one fixed M;
5. no event-wise active-set intersection or renormalization;
6. L1 and L2 norms remain in `[0,1]`;
7. R0 remains in `[0,1]`;
8. numeric result and gate state remain distinct;
9. non-numeric reasons are preserved, not zero-filled;
10. complete and reduced gates are not mixed in dynamics or windows;
11. n-adic entity index and relational index remain distinct;
12. mean asymmetry limitation remains visible;
13. an open gate is not relation, coupling, resonance or alignment;
14. thresholds are finite, lie in `[0,1]` and remain separate policy choices;
15. empty windows produce no numeric coverage, open rate or aggregate;
16. `incomparable` blocks a valid R0 result and is not recoded as a result status;
17. R0 remains independent of IK and downstream branches.

## 13. Separate implementation companion

The adjacent companion supplies conditional schemas, pseudocode, migration,
fixtures and tests. The mathematical method remains authoritative.
