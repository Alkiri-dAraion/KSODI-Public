# KSODI-Full

## Public orientation note

This folder is the public orientation entry for the KSODI-Full v350 research
structure. It supports conceptual review, discussion and version traceability.

The shared structural and method boundary with KSODI-Standard-Eval is
documented in the root
[KSODI-Standard-Eval / KSODI-Full Transition V350](../KSODI-Standard-Eval_Full-Transition_V350.md).

The current architecture separates the following layers:

- interaction state observation
- interaction coherence
- relational comparability
- resonance-family observation

This public folder should not be treated as an implementation reference.

## Relation to KSODI-Standard-Eval

KSODI-Full builds on KSODI-Standard-Eval. The complete monadic KSODI-Standard-Eval
line is `K/S/O/D/I -> Z -> IK` and ends with `IK`.

After `Z`, the architecture branches. `R_0` is the relational gate
evaluated from distinguishable `Z`-trajectories in parallel to monadic `IK`.
Only after a stable `R_0` does `IK_rel` open the relational projection branch,
followed by the further R-family. `R_0`, `IK_rel` and the further R-family are
not part of KSODI-Standard-Eval.

Without such a gate, relational or resonance-family observations can become
misleading, because a system may show apparent resonance while losing
coherence, direction or comparability.

## Current research direction

The revised private reference line distinguishes monadic observation layers
from dyadic and n-adic relational observation layers.

KSODI-Full extends the method toward dynamic interaction patterns, transitions
and relational observation over time. Method material and large parts of the
mathematics for `R_geom` and `R_pace` exist in the private canonical workbench.
They still require complete public review and renewed validation on the
restructured infrastructure before they can become current public reference
releases. Layer 8 signal-media work remains a staged research direction without
a defined architecture.

KSODI-Full is intended to support explainability, observability and
auditability. Its observations may inform separately governed steering or
action, but KSODI-Full does not itself decide, steer or replace human
responsibility and must not be used as an automated decision system.

## Status

Public KSODI 3.3 materials and the later v3.42 working / implementation line
contain or reveal known structural issues and unresolved separations between
`Z`, `IK`, `R_0`, `IK_rel` and the broader R-family. In the current public v3.5
release, the complete monadic KSODI-Standard-Eval line through `IK` is published.
`R_0` is also published separately as the KSODI-Full Layer 4 gate, and `IK_rel`
is published separately as KSODI-Full Layer 5. `R_geom`, `R_pace` and later
R-family layers are not current public reference releases. `R_geom` and
`R_pace` await complete public review and infrastructure revalidation; Layer 8
remains staged research.

Current public v3.5 release boundary:

[`KSODI-Full-Release_V350.md`](./KSODI-Full-Release_V350.md)

The historical Observer images are preserved as important transition evidence
for both KSODI-Standard-Eval and KSODI-Full:

[`historical-observer-v342`](../archive/assets-archive/historical-observer-v342/README.md)

Thanks for your understanding.
