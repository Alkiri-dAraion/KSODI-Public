# KSODI IK_rel - Dyadic Relational Coherence Compatibility v3.50

This file defines the carrier-neutral IK_rel method after
the exact compatible R0 gate. Schemas, pseudocode, migration and test fixtures
belong in the separate companion:

- [`KSODI_Dyadic-Relational-Coherence-IK_rel_Implementation-Companion_V350.md`](./KSODI_Dyadic-Relational-Coherence-IK_rel_Implementation-Companion_V350.md)

## 0. What IK_rel is and what it does

IK_rel asks one narrow relational question:

> After an open numeric canonical complete dyadic R0 gate under the exact
> required profile has admitted two distinguishable trajectories, how
> compatible is their observable movement along one shared, declared monadic
> IK axis?

The v3.50 primary profile compares paired first differences:

```text
Delta IK_A(k_A(j))
Delta IK_B(k_B(j))
```

under an explicit relational pairing

```text
pi(j) = (k_A(j), k_B(j)).
```

IK_rel is therefore not inferred from two isolated IK values. It requires two
separately valid monadic trajectories, comparable projection profiles,
source-local predecessors, an explicit pairing and an open numeric canonical
complete dyadic R0 result under the exact required profile.

The essential distinction is:

```text
parallel monadic observation may occur before R0
relational interpretation begins only after its exact compatible open R0 gate
primary IK_rel compares paired IK movement under one shared axis
extended relational axes use one fixed declared component set N
automatic active-component renormalization is not permitted
```

IK_rel is not agreement, truth, alignment, causation, coupling, resonance,
shared meaning, shared consciousness or a control instruction.

### 0.1 Minimal practical reading

1. Preserve distinguishable trajectories A and B.
2. Resolve one explicit pairing `pi(j)`.
3. Require a canonical numeric dyadic `R0_AB(j)` for the same ordered dyad,
   pairing and relational step, at or above the declared threshold and with
   stored gate state `open`. Reduced or n-adic R0 does not open this method.
4. Require comparable canonical IK profiles and valid source-local first
   differences on both sides.
5. Apply the declared zero-movement policy.
6. Compute the primary movement-compatibility value only when all gates pass.
7. Keep extended component status typed; never silently drop unavailable
   components and move the relational axis.
8. Aggregate only within one stable pairing, gate, axis and component contract.

### 0.2 How to read this file

Sections 1-3 establish examples, identity and gates. Sections 4-6 define the
primary profile and typed extended components. Sections 7-9 define dynamics,
windows and Hangar. Sections 10-12 fix downstream, privacy and formal
boundaries.

## 1. Bounded application examples

### 1.1 Human-chatbot interaction

Let A be the human trajectory and B the chatbot trajectory. Each side first
receives its own Layer-1, Z and IK records. An observer may display both
monadic curves before R0, but may not call their proximity relational
coherence.

At relational step `j`, `pi(j)` pairs one declared A event with one declared
B event. If the exact canonical complete dyadic R0 gate for that same pairing
is open and both canonical IK movements use the same axis, IK_rel may report
whether those movements are compatible. It does not prove
that either side understood, acknowledged or internally represented the other.

### 1.2 Unknown Morse-like signal

An observed signal and a responding system may have partial Z or reduced
`IK^[M]` views. Those views remain diagnostically useful, but they do not
qualify for the v3.50 primary IK_rel profile, which requires comparable
canonical IK trajectories.

A future reduced relational profile would have to declare the same fixed
monadic coordinate set M on both sides, a fixed relational component set N and
its own validation. It must be named separately and is not silently substituted
for canonical IK_rel.

## 2. Architectural position and relational identity

### 2.1 Position after R0

```text
A: K/S/O/D/I -> Z_A -> IK_A
B: K/S/O/D/I -> Z_B -> IK_B

Delta Z_A --\
              +--> R0_AB(j)
Delta Z_B --/

IK_A trajectory ----------------\
IK_B trajectory -----------------+--> IK_rel_AB(j)
exact compatible open dyadic R0 gate -/
```

R0 and monadic IK are parallel prerequisites. R0 is not calculated from IK.
IK_rel consumes the open canonical gate decision plus declared monadic
projection trajectories.

### 2.2 Atomic relational evaluation unit

The atomic dyadic unit is:

```text
rho_AB(j | pi(j))
pi(j) = (k_A(j), k_B(j))
```

where the `source_entity_id` of A and B may be stable or explicitly
provisional, each attribution status remains explicit, `k_A` and `k_B` remain
source-local trajectory indices, and `j` is the relational evaluation index.

The record must preserve:

- for each paired event: `target_event_id_E`, stable or provisional
  `source_entity_id_E`, explicit `source_attribution_status_E`, and
  `emitting_entity_id_E` only when established;
- for each monadic trajectory: `trajectory_id_E`, global event index `n_E`
  and source-local position `k_E`;
- both source-local predecessor event/position references and the resulting
  `Delta IK_E` record IDs;
- pairing-map ID and directionality;
- context and comparison scope;
- R0 result, ordered-dyad/pairing identity, profile and threshold;
- both IK result/profile references;
- IK_rel profile, component contract and zero-movement policy.

A global event index or timestamp may be mapped to these identities but may
not replace them.

### 2.3 Dyadic scope

This v3.50 method is dyadic. N-adic extension requires an explicit
constellation, pairing/hyperedge policy, aggregation rule and comparability
contract. Pairwise averaging is not an automatic n-adic definition.

## 3. Gate and typed result contract

### 3.1 R0 gate

Primary IK_rel is eligible only when:

```text
R0_AB(j).comparison_kind = dyad
R0_AB(j).ordered_dyad_id = IK_rel.ordered_dyad_id
R0_AB(j).pairing_or_constellation_map_id = IK_rel.pairing_map_id
R0_AB(j).relational_eval_id = j
R0_AB(j).status = numeric
R0_AB(j).projection_kind = complete
R0_AB(j).active_coordinate_set_M = {K,S,O,D,I}
R0_AB(j).value >= theta_R0_stable
R0_AB(j).gate_state = open
```

The R0 record must describe the same ordered dyad, paired events, pairing-map
semantics and relational step as the attempted IK_rel result. Its stored gate
state, value, finite threshold in `[0,1]`, method/profile version and complete
dyadic projection contract must be mutually consistent and match the IK_rel
profile exactly.

If R0 is numeric but below threshold, has a valid non-open gate state or is a
reduced or n-adic result, the current dyadic relational projection is
`not_applicable`. If R0 or another required observable gate input is
`not_observable`, the IK_rel result is `not_observable`; the scalar branch
status must not erase the underlying typed reason. Other valid non-numeric R0
results follow the precedence below. If R0 produced an `incomparable`
processing record, malformed identity/profile evidence or another processing
failure, no valid R0 result exists: IK_rel records a downstream processing
block and must not manufacture `not_applicable`, zero or any other valid
IK_rel result.

Canonical IK movement already requires complete comparable Z movement, so a
reduced gate must not be selected to open the canonical primary branch. A
future reduced relational profile requires its own matched `R0^[M]`,
`IK^[M]`, component and validation contract.

An exact compatible open canonical complete dyadic R0 gate admits evaluation;
it does not guarantee a high IK_rel value.

### 3.2 Required monadic input

The primary profile requires:

```text
canonical numeric IK_A(k_A(j) | p_IK)
canonical numeric IK_B(k_B(j) | p_IK)
canonical numeric Delta IK_A(k_A(j) | p_IK)
canonical numeric Delta IK_B(k_B(j) | p_IK)
```

Both sides use the same named IK profile, weight vector, coordinate order and
complete-Z contract. Each first difference uses its own source-local
predecessor. Chronological adjacency across A and B is not a monadic
predecessor.

Reduced `IK^[M]`, changing M or different monadic axes do not qualify for the
primary profile.

### 3.3 IK_rel result type

The external result domain is:

```text
numeric(value in [0,1])
not_selected
not_observable
not_applicable
```

Recommended precedence:

| Condition | IK_rel status |
| --- | --- |
| no IK_rel profile selected | `not_selected` |
| R0 has an incomparable/processing record and therefore no valid result | no valid IK_rel result; downstream processing block |
| R0 or another required observable gate input is `not_observable` | `not_observable` |
| valid R0 closed/non-open, wrong cardinality/projection, absent comparable movement or static-step policy | `not_applicable` |
| a required observable monadic input is `not_observable` after R0 is open | `not_observable` |
| every gate and the selected component policy pass | `numeric` |
| malformed identity, weights or arithmetic | no valid result; processing error |

Retain all underlying R0, IK and typed Z reasons. A scalar relational status
must not erase why one side was unavailable.

## 4. Primary v3.50 movement profile

### 4.1 Raw and normalized movement gap

Since canonical `Delta IK` lies in `[-1,1]`:

```text
g_move,AB(j)
= |Delta IK_A(k_A(j)) - Delta IK_B(k_B(j))|
in [0,2]

C_move,AB(j)
= clip(1 - g_move,AB(j) / 2, 0, 1)
in [0,1]
```

The v3.50 primary profile is:

```text
IK_rel,AB(j | p_rel_move) := C_move,AB(j)
```

Clipping is defensive numerical containment, not permission to accept invalid
inputs.

### 4.2 Zero-movement policy

Under the v3.50 default:

```text
if |Delta IK_A| <= epsilon_move
and |Delta IK_B| <= epsilon_move:
    IK_rel = not_applicable
    static_step = true
```

Joint stillness is absence of directed movement to compare, not relational
failure and not positive compatibility evidence. `epsilon_move` and the policy
ID are versioned. For this normalized first-difference input,
`epsilon_move` must be finite and satisfy `0 <= epsilon_move < 1`.

### 4.3 Bounded interpretation

| Result | Meaning under the primary profile |
| --- | --- |
| near 1 | paired monadic projections move similarly |
| middle | partial movement compatibility |
| near 0 | paired projection movements diverge strongly |
| non-numeric | the declared relational question was not numerically evaluable |

The result says nothing by itself about geometric coupling, pacing, shared
meaning or causation.

## 5. Typed extended relational components

Every current v3.50 extended component uses the same exact canonical complete
dyadic R0 gate from Section 3.1. Reduced or n-adic R0 belongs only to a future
separately named compatible downstream contract.

An extended diagnostic may define:

```text
C_gap(j)   = 1 - |IK_A - IK_B|
C_move(j)  = 1 - |Delta IK_A - Delta IK_B| / 2
C_accel(j) = 1 - |Delta2 IK_A - Delta2 IK_B| / 4
```

after the common gate and each component's own comparability checks.

Zero-input handling is component-local and preserves derivative order:

```text
if |Delta IK_A| <= epsilon_move
and |Delta IK_B| <= epsilon_move:
    C_move = not_applicable
    static_step = true

if |Delta2 IK_A| <= epsilon_accel
and |Delta2 IK_B| <= epsilon_accel:
    C_accel = not_applicable
    zero_accel_step = true
```

`C_gap` remains a static comparison and is not blocked by either rule. Joint
zero movement at the current step does not imply joint zero acceleration: when
both trajectories have just slowed to rest, their second differences may be
numeric and informative. Conversely, equal nonzero constant movement can make
`C_move` numeric while `C_accel` is non-applicable. If only one side is
within the relevant epsilon, the component remains numeric and records genuine
one-sided difference.

`epsilon_move`, `epsilon_accel` and both policy IDs are versioned. For the
normalized ranges used here, require finite `0 <= epsilon_move < 1` and finite
`0 <= epsilon_accel < 2`. A non-numeric movement- or acceleration-based
component is retained in `T_G` and therefore blocks every fixed-N profile that
requires it; it is never silently removed or renormalized.

The complete typed component record is:

```text
T_G,AB(j)
= [status_gap, status_move, status_accel, status_shared]
```

using the common result states. `C_shared` remains reserved and `not_selected`
in v3.50 until a separate definition and profile are accepted. It is retained
in `T_G` for explicit status visibility but is not selectable in a released
v3.50 component axis.

No implementation may construct an unlabeled active vector by removing
non-numeric components event by event. The old `G_rel_active(t)` behavior is
retired because it creates a moving relational basis.

## 6. Declared relational component-axis profiles

For one fixed, non-empty component set

```text
N subset of {gap, move, accel}
```

and a named profile:

```text
v_rel(N) = [v_c | c in N]
each v_c is finite and v_c >= 0
sum_(c in N) v_c = 1
```

the extended projection is:

```text
IK_rel,AB^[N](j | p_rel^[N])
= sum_(c in N) v_c C_c,AB(j)
```

only when every component in N is numeric. Each weight is bound to its named
component identity; positional reordering must not reassign weights.

`IK_rel^[N]` is explicitly profile-bound. Different N, weights, zero-movement
policies or component definitions are not directly comparable. A non-numeric
component is never silently removed and the remaining weights are never
automatically renormalized.

The primary profile is the fixed one-component special case:

```text
N = {move}
IK_rel^[move] = IK_rel
```

## 7. Comparability and relational dynamics

Two primary IK_rel results are comparable only with:

- the same ordered dyad and pairing-map semantics;
- compatible relational context and evaluation granularity;
- the same R0 method/profile/threshold;
- the same canonical monadic IK profile on both sides and across time;
- the same primary IK_rel and zero-movement profiles;
- numeric results at every required relational step.

Extended results additionally require the same fixed N, component definitions
and weights.

For comparable numeric results:

```text
Delta IK_rel,AB(j)
= IK_rel,AB(j) - IK_rel,AB(j-1)
in [-1,1]

Delta2 IK_rel,AB(j)
= Delta IK_rel,AB(j) - Delta IK_rel,AB(j-1)
in [-2,2]
```

These are relational-result dynamics over j. They are not monadic source-local
dynamics and not generic R-family deltas. Gate closure or a typed status
transition is categorical; it is not numeric `Delta IK_rel`.

## 8. Windows and Sigma

Let `W_AB` be one declared non-empty window of relational opportunities under
one fixed dyad, pairing semantics and profile contract. Define:

```text
W_AB^gate
= {j in W_AB | a valid numeric canonical complete dyadic R0 result exists
                 under the exact required profile}

W_AB^open
= {j in W_AB^gate | the R0 gate state is open}

W_AB^move
= {j in W_AB^open | comparable canonical numeric Delta IK inputs on both
                     sides reach the zero-movement policy decision}

W_AB^rel
= {j in W_AB^move | IK_rel,AB(j) is numeric and comparable}

coverage_rel(W_AB) = |W_AB^rel| / |W_AB|
gate_open_rate(W_AB) = |W_AB^open| / |W_AB^gate|
static_rate(W_AB) = count(static_step=true in W_AB^move) / |W_AB^move|
```

Require `|W_AB| > 0` before computing coverage. `gate_open_rate` is numeric
only when `|W_AB^gate| > 0`; `static_rate` is numeric only when
`|W_AB^move| > 0`. An empty denominator is non-evaluable, not zero. Store each
numerator, denominator and eligibility rule explicitly.

`static_step` is a typed first-order observation seed, not a numeric movement
compatibility value. Run lengths, joint versus one-sided stillness,
co-silence opportunities and possible orthogonal or complex-valued
representations remain separately registered Future Work; they do not imply
intent, acknowledgement or successful communication.

For a declared aggregator:

```text
IK_rel_Sigma,AB(W_AB)
= Agg_rel({IK_rel,AB(j) | j in W_AB^rel})
```

Store the aggregator, positive minimum count, coverage threshold, typed status
counts, gate counts and the explicit rate denominators. Emit a numeric
aggregate only when `W_AB^rel` meets the declared positive minimum count and
coverage rule. A high aggregate over sparse eligible steps is not equivalent
to sustained relational coherence.

Extended windows require one fixed N and profile. Deltas between windows
require identical pairing, gate, profile, component and coverage policies.

## 9. Point clouds and Sigma(Hangar)

The richer observer view stores typed relational components beside the scalar:

```text
P_rel,AB(j) = (T_G, numeric components, IK_rel result, gate record)
```

A Hangar view may distribute comparable point records and window summaries.
It is not a shared inner Hangar of A and B.

Required stratification includes ordered dyad, pairing policy, R0 profile,
monadic IK profile, IK_rel profile, fixed N where extended, gate/status counts,
coverage and distribution-distance policy.

Do not pool changing N, weights, pairing policies or typed failures into one
numeric cloud. A distribution distance is non-negative Hangar movement, not
signed `Delta IK_rel`.

## 10. Shared-set and theoretical boundaries

The former notation

```text
H_AB = {Z_A, Z_B}
```

may be used only as a transient observer-side display set. It is not a Hangar,
not a merged state and not an additional relational signal. With complete Z
and one shared linear IK axis, projecting the pair mean equals the mean of the
two monadic IK values and adds no independent relational information.

KSODI does not decide whether communication constitutes an emergent social
process in a Luhmannian sense. It states only that the observer does not access
a merged inner state. The method compares visible or reconstructable
contributions, trajectories, statuses, projections and distributions under
declared contracts.

## 11. Relation to other branches, fairness and retention

An open numeric canonical complete dyadic R0 gate for the same ordered dyad,
pairing and exact required profile records eligibility. IK_rel then asks about
compatibility of monadic coherence-axis movement. `R_geom`, staged `R_pace`
and future signal-media work remain parallel post-R0 questions with separate
bases and profiles.

IK_rel neither replaces those branches nor becomes a generic resonance scalar.
No IK_rel value authorizes steering or intervention.

Pairing rules, thresholds, axes and missingness policies can materially alter
results. They are configuration choices and require disclosure and validation.
Relational records may identify both parties and reveal behavioral patterns;
pseudonymization is not anonymity. Retain the minimum needed and protect
pairing maps, trajectory IDs and provenance.

The method is authoritative. The companion is subordinate implementation
guidance.

## 12. Formal summary and consistency tests

### 12.1 Compact contract

```text
pi(j) = (k_A(j), k_B(j))

open numeric canonical complete dyadic R0 for the same ordered dyad, pairing
and relational step under the exact required profile
+ comparable canonical IK trajectories under one shared axis
+ valid source-local Delta IK on both sides
+ non-static movement under declared policy
-> IK_rel may be numeric

g_move = |Delta IK_A - Delta IK_B|
IK_rel = 1 - g_move / 2

T_G = typed statuses for gap / move / accel / shared

fixed N and all N numeric
-> IK_rel^[N] = sum_(c in N) v_c C_c

changing or hidden N
-> no comparable extended projection, dynamic or window
```

### 12.2 Consistency tests

1. no IK_rel evaluation before an open numeric canonical complete dyadic R0
   gate for the same ordered dyad, pairing, relational step and exact profile;
2. no implicit pairing or shared predecessor;
3. both sides retain distinct source and monadic trajectory identities;
4. the primary profile requires the same canonical IK axis;
5. reduced monadic IK does not enter the primary profile;
6. reduced or n-adic R0 does not open the primary or a current v3.50 extended profile;
7. joint zero first-order movement makes `C_move` `not_applicable`, not zero or one;
8. joint zero second-order movement makes `C_accel` `not_applicable`, while a transition to rest may retain numeric acceleration;
9. `C_gap` remains a static comparison under stillness;
10. movement and acceleration normalization map their full gap ranges to `[0,1]`;
11. all extended component statuses remain in `T_G`;
12. every extended projection declares fixed N from `{gap,move,accel}` and
    finite component-bound weights;
13. no automatic removal and renormalization of non-numeric components;
14. gate/status changes are not numeric deltas;
15. windows reject empty denominators and report coverage, gate, static and
    typed-status numerators and denominators;
16. shared-set notation never becomes a merged state or independent signal;
17. IK_rel remains separate from R_geom, R_pace, resonance and control;
18. upstream incomparable/processing records block a valid IK_rel result and
    are never recoded as a method status or zero;
19. thresholds and zero-input epsilons are finite and lie in their declared
    normalized domains.

## 13. Separate implementation companion

The adjacent companion supplies conditional schemas, pseudocode, migration,
fixtures and acceptance tests. It must preserve the gate, identity, typed
component-set and branch boundaries defined here.
