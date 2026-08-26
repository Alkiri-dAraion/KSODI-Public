# Work Notes - KSODI Standard-Eval v3.50

Purpose: state the current public Standard-Eval package without replacing the
versioned method files.

## Public monadic line

KSODI Standard-Eval contains:

- Layer 1: the five source-attributed operators K, S, O, D and I;
- Layer 2: the source-attributed state vector `Z_A(k_A)`;
- Layer 3: the source-attributed monadic projection `IK_A(k_A)`.

Standard-Eval ends at monadic IK. R0, IK_rel and the R-family belong to
KSODI-Full.

## Current release checkpoint

The current five Layer-1 method/companion packages are released. O additionally
includes the Source-Need Gate.

The reader-first Layer-2 package released on 2026-08-26 contains:

- `KSODI_State-Vector-Z_V350.md` — authoritative carrier-neutral method;
- `KSODI_State-Vector-Z_Implementation-Companion_V350.md` — subordinate
  conditional implementation guidance;
- the adjacent Layer-2 README.

The Layer-2 package preserves the four valid Layer-1 result statuses
`numeric`, `not_selected`, `not_observable` and `not_applicable` in mandatory
`T_Z`. Its binary `A_Z` is derived numeric availability only. Processing
failures produce no valid coordinate result and are never converted into a
fifth status or numeric zero. Complete canonical `Z_A(k_A) in [0,1]^5` exists
only when all five aligned coordinate records are numeric.

The reader-first Layer-3 package released on 2026-08-26 contains:

- `KSODI_Monadic-Interaction-Coherence-IK_V350.md` — authoritative monadic
  projection method;
- `KSODI_Monadic-Interaction-Coherence-IK_Implementation-Companion_V350.md` —
  subordinate conditional implementation guidance;
- the adjacent Layer-3 README.

Canonical IK consumes only complete canonical numeric Z under one named,
versioned axis. Any fixed reduced view remains visibly `IK^[M]`. IK is monadic:
neither one nor two IK values opens relation. Current dyadic `IK_rel` requires
explicit dyadic pairing and open numeric canonical complete dyadic R0 under the
exact required profile.

## Release guardrail

Method files remain authoritative and carrier-neutral. Companions are
conditional implementation guidance. Neither a companion nor an Observer
profile may invent evidence, impute unavailable coordinates, merge source
trajectories or assign decision, steering or intervention authority.

This checkpoint creates no GitHub tag, GitHub Release, DOI or Zenodo artifact
and does not authorize a later private revision.
