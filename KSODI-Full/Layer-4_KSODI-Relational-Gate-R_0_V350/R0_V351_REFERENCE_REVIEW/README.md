# R₀ v3.51 reference review

This package gives humans and machines one small reproducible route through
the Layer-4 v3.51 reference contract. It is subordinate evidence, not another
method definition.

## Reading and reproduction order

1. [Phase 0 frozen basis](./PHASE_0_FROZEN_BASIS.md)
2. [Bounded results](./R0_V351_REFERENCE_RESULTS.md)
3. [Generator](./calculate_r0_v351_reference.py)
4. [Numeric fixture](./r0_v351_numeric_reference.csv)
5. [Status-precedence fixture](./r0_v351_status_precedence.csv)
6. [SHA-256 manifest](./R0_V351_REFERENCE_SHA256SUMS.txt)

Run from this directory or repository root:

```text
python3 -B calculate_r0_v351_reference.py
```

Expected fixture hashes:

```text
r0_v351_numeric_reference.csv
7cd12c4e27ebcde528bd44c81815397a1087d3a260122c7f9ab0a4d46295d1fe

r0_v351_status_precedence.csv
b3c927e4ad260d37a3b9ee66a5d0b81ed045ae42f3e977c114f2a28ad1c2017e
```

## Claim boundary

The package verifies the printed synthetic formulas, profile separation and
status cases. It does not establish empirical calibration, runtime
conformance, relation, coupling, resonance, safety, action authority or
universal profile choice. Alternative coordinate weights remain outside this
package for the later joint R₀/IK_rel sensitivity review.
