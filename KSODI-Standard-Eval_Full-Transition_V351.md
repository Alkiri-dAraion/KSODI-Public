# KSODI-Standard-Eval / KSODI-Full Transition V351

**Authority:** Anne Steinacker. This cumulative Public boundary does not change
the fixed v3.5.0 DOI snapshot and does not authorize implementation,
Controller action or a new relational branch.

**Filename marker:** `_V351` denotes the KSODI v3.51 method line.
It is a path-safe version marker, not a separate method or product.

## Purpose of This Note and Succession

This note explains the structural and method boundary between:

- [KSODI-Light](./KSODI-Light/README.md);
- [KSODI-Standard-Eval](./KSODI-Standard-Eval/README.md); and
- [KSODI-Full](./KSODI-Full/README.md).

It cumulatively retains the released v3.50 transition and adds the reviewed
v3.51 identity, granularity, typed-result, IK, window, view,
reconstruction and authority boundaries. Canonical calculations remain in
their versioned layer files; this note connects scopes and handoffs rather than
creating another calculation layer.

The former `KSODI-Eval-Variants` container was useful during development but
introduced an unnecessary parent category. It could make Standard-Eval and
Full look like competing methods or versioned folders look like additional
products. Root-level scope names now carry the intended product boundary
directly. No valid method material is discarded by that structural transition.

The unchanged
[v3.50 predecessor](./archive/document-snapshots/standard-eval-full-transition/v350-replaced-by-v351/KSODI-Standard-Eval_Full-Transition_V350.md)
is preserved as historical evidence.

## One KSODI Method, Three Public Scopes

KSODI-Light, KSODI-Standard-Eval and KSODI-Full belong to one related KSODI
Method family. They are not competing methodologies, interchangeable
implementations or progressively more truthful views.

### KSODI-Light

KSODI-Light is the compact human-facing entry into communication reflection
and the Method's K/S/O/D/I question families. It may use practical working
questions and optional `0..5` orientation values inside an interaction. It
does not require an external Observer and does not calculate formal Layer-1–5
results.

### KSODI-Standard-Eval

From Standard-Eval onward, an external Observer evaluates observable,
source-attributed events through declared measurement profiles. It preserves
event, entity, observation-unit, trajectory, profile, status and provenance
identity. This requires suitable observation infrastructure but does not
prescribe one software stack.

### KSODI-Full

KSODI-Full begins only when a relational question, relation identity and
candidate distinguishable monadic trajectories have been declared. `R_0`
then tests eligibility under its exact profile. Full does not merge
participants or convert a shared channel into proof of relation.

## Operator Names at the Observer Boundary

The formal Observer line begins with the ordered tuple `(K, S, O, D, I)`:

- `K` — **Observable Context Completeness**;
- `S` — **Observable Structural Coherence**;
- `O` — **Observable Grounded Objectivity**;
- `D` — **Observable Clarity**;
- `I` — **Observable Information Impulse**.

Light may use shorter human-facing labels for local reflection. This is a
viewpoint and interface distinction, not a competing operator definition.
Formal Observer files use the versioned Observer names or declare an explicit
mapping. Results from different profiles or domain instantiations are not made
comparable by sharing one letter.

## Product Boundary

### KSODI-Standard-Eval: monadic trajectory observation

Standard-Eval contains the formal monadic Observer line:

```text
source-attributed event
  -> K/S/O/D/I under declared profiles
  -> complete typed Z_A(k_A)
  -> monadic IK views for A at k_A
```

Every result remains attached to one identified event and observation unit in
one declared trajectory. Complete typed `Z` retains all five coordinate
values or typed non-numeric states, component identities, profiles and
provenance. Missing, inapplicable, failed or incomparable evidence is not
silently converted to numeric zero.

The v3.51 monadic evaluation basis is not one scalar replacement for `Z`. It
keeps at least:

- `IK_w` — the declared weighted axis projection;
- `IK_M2` — normalized vector magnitude;
- `IK_ref` — the declared reference-axis view;
- `AxisDev_ref` — deviation from that reference axis; and
- the return path to complete typed `Z` and its provenance.

Their human-facing joint view is the **IK-Gesamtbild**; the technical
identifier is `ik_joint_evaluation_view`. It is a navigable multi-view, not a
new total score or replacement truth. Standard-Eval ends at monadic
trajectory observation and these monadic views. It does not establish a
relation between trajectories.

### Applicability and expected numeric coverage

The upper numeric layers speak only where all five required operator
coordinates are numeric under the same declared event, basis and profile
contract. If an operator is `not_applicable`, `not_observable`, failed or
otherwise nonnumeric, the complete typed record preserves that state; it does
not fabricate a canonical complete numeric `Z`, `IK`, `R_0` or `IK_rel`
result. This is an applicability boundary, not a judgement that the event or
interaction lacks value.

A distinct later O-profile is needed for interaction-internal residual and
reference reconstruction when observable participants or systems appear to
exchange logically structured signals although the Observer cannot yet decode
their language, code or semantics. This route does not begin with
undifferentiated visible material: attributable contributions from known
sources are first retained and accounted for and, where a valid common
representation permits it, subtracted. The remaining visible residual can
then be examined for recurrence, sequence, transformation or response
patterns. Current O may already admit visible interaction elements as
reference material; what remains undefined is this controlled residualization
and the construction and validation of an interaction-internal reference
basis. This is a methodically necessary research direction for cross-species
and cross-protocol observation, not part of v3.51. It must distinguish
source-local evidence from
relational contingencies and must not turn pattern regularity into a claim of
an unknown source, meaning, shared understanding, intent or successful
communication.

A later, separately identified O-profile for checking external sources not
present in the observed interaction is a methodically necessary research
direction for KSODI's broader reconstruction ambition. It is planned research,
not part of v3.51, and would require its own basis, source-access boundary,
identity, instrument and validation. Whether it should be developed before
v3.6 or in parallel remains open and depends in particular on reproducible
evidence from the preceding implementation line. It would address “a source
is required but is not visible
here”, not silently convert “no source is expected for this question” into a
numeric O result.

### Future cross-layer identity of raw and residual views

Any later known-source residualization occurs at the evidence-object level,
before operator calculation. K/S/O/D/I results must identify whether they were
calculated from the admitted raw material or from a separately constructed
residual view; score subtraction is not a substitute. Raw and residual `Z`
states are distinct tagged objects, and every IK view inherits that identity.
`R_0` may compare movements only under the same or an explicitly compatible
residualization contract. Current `IK_rel` would additionally require both
compatible `IK_w` operands and the exact matching `R_0` handoff. This is a
research guard for a later profile, not a v3.51 calculation change.

### KSODI-Full: dyadic observation from R_0

After complete typed `Z`, the architecture branches. Monadically derived IK
views and Layer-4 `R_0` answer different questions:

```text
complete typed Z trajectories
  +--> monadic IK views
  +--> R_0 relational eligibility under declared pairing/profile
```

`R_0` receives distinguishable, comparable source-local movements plus an
explicit ordered pairing or constellation identity. It is not calculated from
monadic IK. Numeric result status and categorical gate state remain separate:

```text
valid numeric R_0 at/above its declared threshold -> open
valid numeric R_0 below its declared threshold    -> closed
non-numeric R_0                                   -> not_evaluable
incomparable or invalid input                      -> no valid R_0 result
```

An open gate admits only the exact compatible downstream calculation. It is
not proof of relation, acknowledgement, shared meaning, coupling, resonance,
agreement, alignment, success or permission to act.

Current primary dyadic Layer-5 `IK_rel` additionally requires the same ordered
dyad, paired event/predecessor identities, relational step and an open numeric
canonical-complete dyadic `R_0` under the exact required profile. Reduced or
n-adic `R_0` does not silently open that branch. Its components such as
`C_gap`, `C_move` and `C_accel` remain distinguishable questions; their
selected profile, operands, weights, status precedence and provenance remain
part of the result.

Monadically coherent, dyadically coherent and dyadically resonant are not
synonyms. Later `R_geom`, `R_pace`, voice/signal-media and other R-family
branches remain separately staged for their own contracts and release
decisions.

The joint v3.51 Phase-H review is a cross-layer protection package rather than
another calculation layer. Its 52 synthetic cases test R₀ metric/profile
sensitivity, optional coordinate-extreme compression, IK_rel projection
collisions, epsilon provenance and the complete R₀-to-IK_rel route. Expected
profile sensitivity and diagnostic information loss remain distinct from a
contract contradiction; no tested contradiction was observed. The review
changes no canonical formula or profile and does not establish runtime
conformance.

### v3.51 observation-unit boundary

Source entity, observed unit, event and observation granularity are separate.
A person, subsystem, component, composite event, dyad or ensemble may be
selected only under a declared profile that preserves applicable parent,
membership, composition and source provenance.

Changing the observed unit or granularity changes the question. It does not
silently convert one trajectory or result into another. Provisional identity,
legacy reconstruction and `reconstruction_pending` states may preserve useful
material without manufacturing missing provenance or v3.51 comparability.

## Time, Movement and Derived Window Objects

Comparable `Delta Z` and `Delta2 Z` remain directed, time-qualified movement
objects. Their start/target states, predecessor relation, interval or event
step, component profiles and provenance remain explicit. A scalar movement
magnitude does not replace the directed vector.

A window aggregate has its own derived identity. It must preserve exact
members or reconstructible membership, coverage, status partitions,
aggregator and version, window kind and provenance. It must not pose as a
participant event or be written back as a participant state.

At minimum, distinguish:

```text
derive_then_aggregate
aggregate_then_derive
```

These orders may answer different questions and need not produce the same
result. Event-level `Delta`, `Delta2`, path length, window-to-window difference
and a difference between window summaries remain separate operations.

The v3.51 strict-integrity reference route does not drop required failures or
non-numeric partitions to manufacture a number. Later
`partition_preserving_window_aggregation` (`PPWA`) and bounded-tolerance
profiles remain named Future Work until their own rules are validated.

## Machine Object, Assistive Interpretation and Human View

For every displayed or machine-consumed result, distinguish:

```text
retained operands and provenance
  -> raw typed result
  -> numeric policy / transformation
  -> machine calculation value
  -> rounded display value and rendered mark
```

Formal values may lie in the real numbers permitted by their contract; a
human display may round them. The unrounded stored value remains authoritative
for calculation. A display value is not fed back as an operand.

Deterministic Observer calculation, assistive LLM interpretation and human or
domain-expert decision are separate channels. An assistive model receives a
bounded attributable package, exposes uncertainty and alternatives, and may
propose explanations or follow-up questions. It does not overwrite the method
result, invent evidence or inherit action authority.

Every simplified view keeps a drill-down route to the complete retained
machine object and, within declared access and retention limits, its evidence.

## Interaction, Hangar and Controller Boundary

Four spaces remain distinguishable:

1. participant-specific processing/library/archive space;
2. transient interaction/work space;
3. qualified Observer-side Hangar; and
4. separately authorized Controller/action space.

Shared availability does not merge identities, archives, understanding or
responsibility. The Hangar stores qualified observation and reconstruction
views; it is not the interaction itself, a participant's hidden state or an
additional main layer.

Observer findings, corridors and alerts may open diagnostic questions. They
do not select a target or action. Controller decisions, execution and feedback
require a separate policy, authority, evidence envelope and audit trail. See
the cumulative
[Observability and Separate Controlled-Action Boundary v3.51](./KSODI-Full/KSODI_Observability-and-Controlled-Action-Boundary_V351.md).

## Shared Cross-Scope References

The following current Public references span Standard-Eval and Full. Their
own v3.51 successor review remains separately governed where applicable:

- [Conceptual Note v3.51](./Conceptual-Note_V351.md);
- [KSODI Architecture](./KSODI-Architecture_V351.md);
- [KSODI Hangar](./KSODI-Hangar_V351.md);
- [Implementation Guardrails](./IMPLEMENTATION_GUARDRAILS_V351.md); and
- [Ethics](./Ethics_V351.md).

Canonical layer definitions and companions remain authoritative for their own
calculations. Cross-scope notes explain boundaries and navigation; they do not
silently modify formulas.

## Compatibility and Migration Boundary

The released v3.50 structure remains valid and unchanged. V3.51 sharpens
identity, status, provenance, IK views, windows, result/display channels and
relational handoffs. A v3.50 or earlier record may be classified as:

- `v351_conformant`;
- `legacy_reconstructible`;
- `legacy_partially_reconstructible`;
- `legacy_noncomparable`; or
- where genuine alternatives remain unresolved, `reconstruction_pending`.

`not v3.51 conformant` does not mean worthless or invalid. Missing provenance
must not be reconstructed as fact. Implementers declare gaps rather than
guessing identities, profiles, operands or statuses.

## Publication and Historical Boundary

The fixed Public KSODI v3.5 release and DOI snapshot remain unchanged. Public
`main` now contains reviewed cumulative v3.51 method and reference material
through Layer 5 plus the joint Phase-H sensitivity package. These files may be
`published_to_public_main_verified` and `release_selected` without yet being
`released_verified`. This transition is published on Public `main`; other
Root/reader successors, the final commit set, tag, GitHub Release and
citation/DOI treatment remain separately authorized stages.

Later R-family and signal-media material remains staged. Repository visibility
alone is not a release marker. Earlier v3.3 and v3.42 implementation material
remains provenance, not current implementation authority:

- [Historical method material](./archive/method-history-v33/README.md);
- [Historical Observer visualizations](./archive/assets-archive/historical-observer-v342/README.md); and
- [Public implementation-transfer examples](./implementation-examples/README.md).

Public implementation examples remain examples rather than method canon.

Reference methods and reproducible tests may be released before independent
runtime conformance exists, provided that boundary is stated explicitly.

## Licence Transition

Standard-Eval and Full were initially held under an all-rights-reserved status
and were later released as method documentation under CC BY 4.0. The central
transition note points to the authoritative repository licence and history:

- [KSODI licence transition from V342 to V350](./KSODI-License-Transition-Note_V342-to-V350.md);
- [Repository licence](https://github.com/Alkiri-dAraion/KSODI-Public/blob/main/LICENSE.md); and
- [Licence decision history](https://github.com/Alkiri-dAraion/KSODI-Public/blob/main/LICENSE_HISTORY.md).

Separately published software implementations are distinct works and retain
the licence declared in their own repositories.

---

© 2026 Anne Steinacker-Folkerts & Heiko Folkerts
Licensed under CC BY 4.0
