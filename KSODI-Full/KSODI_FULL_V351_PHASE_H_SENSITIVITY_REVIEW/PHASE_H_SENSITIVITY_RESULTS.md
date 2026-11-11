# Phase H — Joint R₀ / IK_rel Sensitivity Results

Status: `PUBLIC_SYNTHETIC_REFERENCE_RESULT / CONTRACTS_CONFIRMED /
EXPECTED_PROFILE_SENSITIVITY_AND_PROJECTION_LOSS_OBSERVED`

## 1. Result at a glance

The runtime-independent generator produced 52 synthetic reference rows,
including one declared baseline reuse (`H-E-07`) for its adjacent profile
control (`H-E-08`):

| Block | Rows | Principal result |
| --- | ---: | --- |
| H-A | 12 | canonical threshold behavior confirmed; norm and coordinate-metric profiles can change the gate as expected |
| H-B | 7 | ties remain representable, but an extrema record compresses sign and nonmaximal movement unless complete `Delta Z` is retained |
| H-C | 7 | five raw scalar projection collisions observed—three numeric and two typed projected-zero cases; complete movement vectors distinguish them |
| H-D | 16 | exact zero, all three positive-epsilon kinds, their boundaries and calibration-provenance failures remain typed and separable |
| H-E | 10 | complete R₀ → IK_rel route preserves the declared gate, profile, epsilon and reverse-evidence boundaries |

Observed finding families across their applicable blocks:

- `contract_confirmed`;
- `profile_sensitive_expected`;
- `diagnostic_information_loss`;
- no independently adjudicated `contract_contradiction` finding; the generator
  does not perform that separate method-to-fixture reconciliation.

No formula, threshold, gate rule, epsilon value or canonical profile was
changed by this review.

## 2. H-A — R₀ profile sensitivity

The canonical normalized L1 boundary behaves inclusively:

```text
uniform drift 0.19 -> R₀ 0.81 -> open
uniform drift 0.20 -> R₀ 0.80 -> open
uniform drift 0.21 -> R₀ 0.79 -> closed
```

The same single-axis movement yields `R₀ = 0.8` under the canonical normalized
L1 reference and approximately `0.552786404500042` under the separate L2 test
control. This is expected profile sensitivity, not arithmetic disagreement.

Equal L1 magnitude does not imply equal L2 magnitude. Conversely, vectors
with equal L2 magnitude may have different L1 distributions. Fixed
coordinate-weight controls additionally make coordinate identity consequential:
the K-focused control closes the K-axis case at `R₀ = 0.7` while opening the
same-magnitude S-axis case at `R₀ = 0.95`.

These controls show why profile identity is part of the result identity. They
do not support replacing the canonical equal-coordinate L1 profile.

## 3. H-B — coordinate-extreme candidate

The candidate retains:

- one unique extreme coordinate;
- every coordinate in a tied maximum;
- an empty coordinate-ID set for the all-zero vector.

It does not retain the sign, complete distribution or all secondary movement
by itself. Two vectors may share the same magnitude and extreme IDs while
having different signs or remaining coordinates. Therefore:

```text
max_abs_coordinate_delta_E
!= complete Delta Z_E
```

The diagnostic may be useful for a narrow question, but the current result
does not justify making it a required v3.51 record field.

## 4. H-C — IK_rel projection collisions

Five of seven deliberately selected rows produce a raw projected compatibility
expression of `1` although their complete movement vectors differ. Three are
numeric `C_move` collisions. Two have both projected operands at exact zero and
therefore correctly return `not_applicable_joint_projected_zero`, not numeric
`IK_rel = 1`. Examples include:

- equal projected movement on different coordinates;
- projected zero for a full transfer versus actual rest;
- concentrated versus uniformly distributed movement with the same `IK_w`;
- disjoint zero-sum transfers.

This is the mathematically expected consequence of projecting five dimensions
onto one scalar and then applying the separately typed zero policy. It does not
mean `IK_rel` claims that the complete movements are identical. The current
v3.51 reverse route to both full `Delta Z` vectors is therefore essential, not
optional explanatory decoration.

One identical full-movement case correctly produces `C_move = 1` without a
collision. One opposite-projection case produces `C_move = 0.9`, confirming
that the scalar remains sensitive to its declared projected question.

## 5. H-D — epsilon and calibration provenance

The fixtures distinguish all three positive-epsilon kinds:

- `epsilon_numeric_tolerance`;
- `epsilon_observation_resolution`;
- `epsilon_question_relevance`.

Across the exact and positive-epsilon cases they produce:

- one exact joint projected-zero result;
- four positive-band non-applicable results;
- three `not_observable` results for observation-resolution cases;
- four numeric results;
- four processing errors for missing origin, missing calibration status,
  unsupported calibration claim or negative epsilon.

Boundary equality uses `<= epsilon`. A positive epsilon can therefore change
the typed status without changing the raw `C_move` operand or formula.

The structurally complete calibration-record fixture validates only that an
evidence-reference field is present. The review makes no empirical calibration
claim.

## 6. H-E — complete joint route

The combined cases confirm:

1. an open R₀ gate does not force a numeric `IK_rel` result when the projected
   movement lies in the exact-zero or selected epsilon band;
2. a closed R₀ test profile blocks the current primary downstream branch;
3. an alternative IK-weight profile changes `C_move` only under its own named
   identity;
4. complete `Delta Z` retains distinctions hidden by equal scalar
   projections;
5. profile and status changes remain reconstructible through the record.

All ten declared row expectations matched the generated classifications. This
is an internal generator assertion, not an independent contract audit.

## 7. Four post-review decision candidates

These candidates follow from the generated evidence but remain subject to
separate method, governance and version review.

### 7.1 Coordinate-extreme schema

Candidate: defer to v3.52. Phase H supports keeping the diagnostic available
for a narrow question, but not requiring it in every controlled record.

### 7.2 Human and machine presentation

Candidate: future views should expose profile changes and projection collisions without
presenting them as defects. Machine records need exact operands and identities;
human views need a drill-down from scalar result to the complete movement
bundle.

### 7.3 Calibration research

Candidate: positive epsilon and threshold values require question-, material-,
population-, resolution- and infrastructure-specific evidence. No synthetic
fixture becomes an empirical default.

### 7.4 v3.51 correction decision

Candidate: no formula correction is indicated. The most material standard-question loss
is the known scalar projection collision, and v3.51 already addresses it
through the mandatory reverse route and diagnostic bundle. Removing that loss
would require a different question or richer result object, not a silent
change to `IK_rel`.

## 8. Future Work boundary

Whether a loss is tolerable depends on at least:

- investigation context and question;
- chosen resolution and observation window;
- available infrastructure and storage;
- intended human or machine consumer;
- expected decision or follow-up;
- privacy, sensitivity and governance constraints.

This tolerability work remains open unless a common standard question exposes
a material, safely repairable omission. Phase H supplies evidence for that
later review; it does not close it.

## 9. Bounded conclusion

The corrected fixtures are consistent with the frozen v3.51 contracts under
the tested sensitivity pass. The observed losses are visible and reproducible;
the separate reconciliation records whether they remain compatible with the
declared non-total nature of `R_0` and `IK_rel`. Any v3.52 schema decision and
any runtime-conformance claim remain separate review steps.
