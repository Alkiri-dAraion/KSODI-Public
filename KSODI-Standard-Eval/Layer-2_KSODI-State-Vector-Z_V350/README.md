# Layer 2 - State Vector Z

Status: public KSODI v3.50 Layer-2 reference package, strictly reviewed and
released on 2026-08-26; method, companion and README are byte-identical between
Private and Public at this checkpoint.

Layer 2 composes five already evaluated, source-attributed Layer-1 coordinate
records. Z is not a sixth score:

```text
e_A(k_A)
  -> K_A, S_A, O_A, D_A, I_A
  -> typed Z record R_Z,A(k_A)
  -> complete Z_A(k_A) only when all five statuses are numeric
```

Active files:

- [State Vector Z method](./KSODI_State-Vector-Z_V350.md) — authoritative,
  carrier-neutral public reference method;
- [Z implementation companion](./KSODI_State-Vector-Z_Implementation-Companion_V350.md) —
  subordinate conditional storage, validation, migration, pseudocode and test
  guidance.

The method requires the typed coordinate-status vector:

```text
T_Z,A(k_A)
= (tau_K, tau_S, tau_O, tau_D, tau_I)
```

with each status in:

```text
numeric
not_selected
not_observable
not_applicable
```

The binary `A_Z` mask is derived from `T_Z`. It records numeric availability
only and cannot replace the typed status vector.

Canonical `Z_A(k_A) in [0,1]^5` exists only when all five aligned coordinate
records are numeric. Every reduced view must display its coordinate set and
remain visibly distinct from complete Z and canonical IK.

Potential derived views include complete or explicitly partial `Delta Z`,
`Delta2 Z`, drift norms, `Z_Σ(W)` and `Z_Σ(Hangar)`. Complete dynamics use
same-source comparable complete states. Partial dynamics require one fixed
declared coordinate set.

Human-readable scalar, vector and drift displays are projections of the same
typed records used by richer machine-readable trajectory, distribution and
point-cloud views. Presentation complexity does not create another state-space
branch and must not erase identity, status, profile or provenance.

The shared Hangar method note is maintained at the repository root:

- [KSODI Hangar](../../KSODI-Hangar_V350.md)

Cross-layer implementation identity and storage are controlled by:

- [KSODI Implementation Guardrails](../../IMPLEMENTATION_GUARDRAILS.md)

## Release boundary

This release covers the Layer-2 Z method, its conditional implementation
companion and this adjacent README. It does not release the newer private
Layer-3 IK revision, authorize downstream implementation alignment, or create
a GitHub tag, GitHub Release, DOI or Zenodo artifact.
