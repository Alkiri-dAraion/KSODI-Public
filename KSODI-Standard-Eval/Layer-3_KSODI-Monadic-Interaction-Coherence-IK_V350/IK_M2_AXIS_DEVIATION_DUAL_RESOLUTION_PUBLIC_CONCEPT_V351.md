# IK magnitude, fixed-reference deviation and dual-resolution views — v3.51 public concept companion

## 1. Purpose

This companion explains why KSODI v3.51 does not reduce a complete typed
state vector to one monadic scalar. It introduces the public reasoning behind
the joint use of:

```text
complete typed Z
├── IK_w             active weighted-axis position
├── IK_M2            normalized complete-vector magnitude
├── IK_ref           fixed-reference-axis position
├── AxisDev_ref      deviation from the fixed reference diagonal
└── identities, profiles, statuses and provenance
```

The authoritative formulas, result identities and conformance conditions are
defined in the
[v3.51 IK method](./KSODI_Monadic-Interaction-Coherence-IK_V351.md).
This file is an explanatory concept companion. It does not replace that
method, select empirical thresholds, authorize implementation changes or turn
an observation into a decision.

The current architecture begins with bounded examples and test cases arising
from pedagogical and communication settings, software-development questions,
safety-oriented review and general method-understanding problems. Some cases
are synthetic. They support explanation and counterchecking; they do not by
themselves validate a domain, population, intervention or long-term effect.

## 2. Why one projection is not enough

For a complete numerical state

```text
Z = (K, S, O, D, I) in [0,1]^5
```

the weighted projection

```text
IK_w(Z) = w dot Z
```

answers a useful question: where is the state located on one declared and
versioned weighting functional?

It cannot, by itself, show whether the same projected value arose from a
balanced coordinate profile or from a strongly uneven one. It also does not
preserve the complete labelled state. Two different Z vectors may therefore
share the same `IK_w` value.

KSODI v3.51 retains `IK_w` and adds a fixed reference geometry. The resulting
views answer different questions and must not be treated as independent votes
for one conclusion:

- `IK_w` — position under the active declared weighting profile;
- `IK_M2` — normalized magnitude of the complete numerical vector;
- `IK_ref` — position on the fixed equal-coordinate reference diagonal;
- `AxisDev_ref` — distance from that diagonal;
- complete typed `Z` — the labelled coordinates, statuses and return path to
  evidence.

No uncalibrated sum or generic “overall coherence” value follows from these
readings.

## 3. Fixed-reference mathematics

For complete numerical `Z`, the normalized Euclidean magnitude is:

```text
IK_M2(Z) = ||Z||_2 / sqrt(5)
```

The fixed reference direction is the equal-coordinate diagonal:

```text
u_ref = (1,1,1,1,1) / sqrt(5)
```

The normalized reference-axis position is:

```text
IK_ref(Z)
  = (u_ref dot Z) / sqrt(5)
  = (K + S + O + D + I) / 5
```

The normalized deviation from that diagonal is:

```text
AxisDev_ref(Z)
  = ||Z - (u_ref dot Z)u_ref||_2 / sqrt(5)
```

The three fixed-reference quantities satisfy:

```text
IK_M2(Z)^2 = IK_ref(Z)^2 + AxisDev_ref(Z)^2
```

For this exact five-coordinate representation, `AxisDev_ref` is also the
population standard deviation of the five coordinate values. This is a
descriptive property inside the declared representation. It does not prove
that the five operators have equal empirical reliability, uncertainty,
semantic scale meaning or domain relevance.

`IK_ref` is identical to the complete-state equal-weight mean and therefore
does not add an independent measurement. It remains useful as an explicit or
reproducibly derived support coordinate for the fixed geometry.

## 4. Fixed reference versus active weighting

The active weighted projection and the fixed reference diagonal serve
different purposes:

```text
IK_w    -> question-specific weighted position
IK_ref  -> stable equal-coordinate reference position
```

A non-equal weight vector defines a linear functional whose equal-score sets
are hyperplanes. Reusing that vector as a geometric reference ray would be an
additional method choice. KSODI v3.51 therefore does not silently interpret
every active weight profile as the reference geometry.

The fixed diagonal remains available when active weights change. This makes
profile changes visible instead of allowing an adaptive or learned axis to
become its own unexamined reference.

Question-specific corridors, learned axes and other geometric references
remain possible research directions. They require their own identities,
estimation evidence, metrics, uncertainty, comparison rules and validation.
They do not redefine `AxisDev_ref`.

## 5. The IK-Gesamtbild

**IK-Gesamtbild** is the human-facing name for the jointly navigable view. Its
technical view identifier is:

```text
ik_joint_evaluation_view
```

It is not a fourth calculation and not a total score. A conforming view keeps
the following distinctions available:

```text
IK-Gesamtbild
├── active IK_w and weighting-profile identity
├── IK_M2
├── IK_ref
├── AxisDev_ref
├── complete typed Z
├── comparison and window identity
└── provenance and evidence return path
```

A visual interface may show a line, point, distance, ring, profile or time
trace. Every such surface remains a projection of a richer retained object.

## 6. Dual-resolution contract

The machine-readable result retains the information needed for reconstruction
and comparison:

- complete typed Z and coordinate order;
- source, event and evaluation-unit identities;
- active profile, reference geometry and formula versions;
- raw numerical components and typed non-numerical statuses;
- comparison, time and window identities;
- coverage, exclusions and provenance;
- reverse links to admissible operator evidence.

An assistive LLM may explain a governed selection from this object. It must
not fill missing evidence, infer hidden internal state or create a new IK
result.

A human/governance view may simplify and round values. The display policy must
remain identifiable, and the permitted route back to the richer object must
remain open.

The governing representation principle is:

> A governance line is not a simplified substitute truth but a navigable
> projection of the retained machine object. Every alert must keep the return
> path to complete Z and its provenance open.

## 7. Movement and time

State magnitude and movement magnitude are not interchangeable:

```text
Delta IK_M2
!= ||Delta Z||_2 / sqrt(5)       # in general
```

KSODI therefore keeps at least these objects distinguishable where the
question requires them:

```text
Z_start
directed complete Delta Z
||Delta Z||
Z_target
profile, time basis and provenance
```

Net displacement, path length, direction, pace, dwell time and second
difference answer different questions. Without a declared clock or interval,
`Delta2 Z` is an ordinal second difference rather than physical acceleration
or an R-family pacing result.

## 8. Windows and aggregation order

Two legitimate processing orders must be named separately:

```text
derive_then_aggregate:
  derive a result from each eligible complete Z,
  then aggregate the per-state results

aggregate_then_derive:
  aggregate one shared eligible set of complete Z vectors,
  then derive results from the aggregate Z
```

Linear `IK_w` and `IK_ref` commute with arithmetic averaging under one stable
contract. Nonlinear `IK_M2` and `AxisDev_ref` generally do not. The resulting
order gap may reveal structure compressed by an aggregate-state view; it is
not automatically a semantic difference, error, conflict or coherence
measure.

Every derived window object requires its own identity, member set, coverage,
aggregator, status partition and provenance. It must not be written back as a
participant state or presented as a target event.

The arithmetic mean is a transparent v3.51 reference case, not a universal
domain default. Event-based, clock-based, sliding, tumbling, robust,
distributional, semantic and change-point windows require separately named
profiles and validation.

## 9. Alerts and corridors

An alert is relative to a declared question, profile, reference, corridor or
compatibility condition. It opens investigation; it does not establish error,
harm, incoherence or required intervention.

Any later threshold or corridor must declare at least:

- the investigation question and observation claim;
- evaluation-unit and population identity where applicable;
- active weighting profile and geometric reference;
- axial position or position-conditioned reference;
- metric, window, coverage and uncertainty;
- estimation evidence and version;
- the route back to distributions, individual trajectories, complete Z and
  source evidence.

Long or dense observation settings may benefit from corridor-relative display
indices for navigation and triage. Such an index remains subordinate to the
IK-Gesamtbild and the retained distributions. It must not become an
unqualified score of persons, groups, communication quality or truth.

## 10. Cross-layer boundary

- Layer 1 operators do not automatically receive an `IK_M2` calculation.
- Layer 2 complete typed Z remains the primary geometric object.
- Layer 3 derives distinguishable monadic views from eligible Z.
- Layer 4 R₀ concerns comparable movement operands and relational eligibility;
  it is not static Z magnitude.
- Layer 5 IK_rel has its own pairing, gate, components and profiles; no monadic
  formula is copied into it automatically.
- Later R-family branches require their own geometry, pacing, signal and
  validation contracts.
- Hangar views retain typed objects and comparison routes; they are not a
  Controller.
- Observation and visualization do not authorize action.

Monadically coherent, dyadically compatible and relationally resonant remain
different claims. KSODI does not establish truth, intention, agreement or
causality without a separately declared question and evidence contract.

## 11. Public research questions

The following questions remain open and welcome attributed collaboration:

1. Which visualization preserves the fixed and active reference views without
   overwhelming non-specialist readers?
2. Under which questions are all fixed-reference components necessary, and
   when is a smaller reversible view sufficient?
3. Which window profiles reveal useful structure without hiding status
   partitions, multimodality or sparse coverage?
4. How should uncertainty from the Layer-1 operators propagate into the joint
   view?
5. Which domain-specific reference corridors can be estimated without
   circular self-confirmation or metric gaming?
6. How portable are the views across pedagogical, communication,
   development, safety-review and other declared settings?
7. Which machine-readable fields are necessary for reproducibility, and which
   human-facing details are necessary for responsible governance decisions?

Concrete use requires domain review, lawful and purpose-bound data handling,
declared instruments, counterexamples and validation against the exact
question. A successful synthetic example is not yet empirical validation.

## 12. Implementation and release boundary

The v3.51 method requires implementations to preserve result identity,
profiles, statuses, comparability, raw/display separation and provenance.
Reference mathematics can be published before an independent runtime
conformance demonstration, provided that the distinction remains explicit.

This explanatory companion does not authorize software merge, data
collection, monitoring, scoring, alert automation, intervention, a Git tag,
GitHub Release, DOI or other publication action.
