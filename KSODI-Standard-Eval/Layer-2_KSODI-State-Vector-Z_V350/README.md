# Layer 2 — Complete Typed State Vector Z

Layer 2 assembles five already evaluated, source-attributed Layer-1 coordinate
records into one typed monadic state record. `Z` is not a sixth score and does
not merge participants:

```text
one attributable target event of A
  → K_A, S_A, O_A, D_A, I_A
  → typed record R_Z,A(k_A)
  → complete numeric Z_A(k_A) only when all five statuses are numeric
```

## Active v3.51 files on Public main

- [State Vector Z method](./KSODI_State-Vector-Z_V351.md) — controlling,
  carrier-neutral definition;
- [Z implementation companion](./KSODI_State-Vector-Z_Implementation-Companion_V351.md) —
  subordinate schemas, validation, migration, pseudocode and tests.

The v3.50 method and companion are retained in the repository archive as the
released predecessor evidence. Public `main` may contain later layers still
under their v3.50 names during the layerwise v3.51 publication run; this does
not imply a completed tagged v3.51 release.

## Human reading route

Start with four distinctions:

1. A typed Z record can be valid without containing a complete numeric vector.
2. `T_Z` preserves why a coordinate is non-numeric; the binary `A_Z` mask only
   says whether a numeric value exists.
3. A partial `Z^[M]` is a named diagnostic projection, never silent completion
   of canonical Z.
4. A graph, rounded vector or short explanation is a view of the recoverable
   typed object, not a replacement for it.

The method then explains identity, complete and partial states, comparability,
`Delta Z`, `Delta2 Z`, movement norms, windows, Hangar and the transition to
IK. The companion shows how an implementation can preserve those boundaries.

## Machine and assistive reading route

Keep three linked channels distinguishable:

```text
recoverable machine-readable typed Z object
assistive-model interpretation over governed inputs, if selected
human/governance display
```

The machine object retains the five coordinate records, source and trajectory
identity, statuses, concrete basis instances, profiles, transformations, raw
results and provenance. An assistive model may describe a pattern or suggest a
drill-down. It may not change status, fill a coordinate, certify meaning or
create action authority. Display rounding never changes the stored operand.

## Dynamics, windows and Hangar

Keep these objects separately reconstructible:

```text
Z_k
Delta Z_k
Delta2 Z_k
movement norms under named metrics
one derived aggregate Z over an exact eligible member set
window identity, order, overlap, coverage, partitions and exclusions
```

A derived window object has its own identity and is never written back as a
participant state. `derive_then_aggregate` and `aggregate_then_derive` answer
different questions even where a linear special case produces the same
number. The v3.51 reference route uses `strict_integrity_v351`; later robust,
semantic, change-point or `PPWA-bounded` profiles remain separately named
research routes.

Hangar views preserve point identity and provenance. Complete points,
partial-mask strata and window aggregates must not be silently mixed.

## Transition to IK

Complete typed Z remains the return object for the jointly reviewed v3.51 IK
views:

```text
complete typed Z
  ├── IK_w
  ├── IK_M2
  ├── IK_ref
  └── AxisDev_ref
```

Layer 3 controls the formulas and interpretation. No scalar, magnitude,
deviation or visualization replaces Z. Reduced projections require separately
named profiles.

## Governing public anchors

- [Layer-1 measurement-basis discipline](../Layer-1_KSODI-Operators_V350/LAYER_1_MEASUREMENT_BASIS_AND_REFERENCE_DISCIPLINE_V351.md)
- [State Vector Z method](./KSODI_State-Vector-Z_V351.md)
- [Z implementation companion](./KSODI_State-Vector-Z_Implementation-Companion_V351.md)

## Release boundary

The method and companion are published on Public `main` as v3.51 reference
method and implementation guidance. This does not establish independent
runtime conformance, approve a specific product architecture or authorize an
intervention. Selection for the complete release, tag, GitHub Release and DOI
remain separate human decisions.
