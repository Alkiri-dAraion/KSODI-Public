# KSODI-Standard-Eval / KSODI-Full Transition V350

**Status:** public structural and method-boundary orientation for KSODI v3.5 / v3.50

**Filename marker:** `_V350` denotes KSODI v3.5 / v3.50. It is a path-safe
version marker, not a separate release or method variant.

## Purpose of This Note

This note records the transition from the former `KSODI-Eval-Variants`
container to two directly named public method scopes:

- [KSODI-Standard-Eval](./KSODI-Standard-Eval/README.md)
- [KSODI-Full](./KSODI-Full/README.md)

The former container was useful during development but introduced an
unnecessary parent category. It could make KSODI-Standard-Eval and KSODI-Full
look like independent alternative methods or make versioned subfolders look
like additional products. The root-level structure now lets the path carry the
canonical product name directly.

No method material was removed through this transition. Canonical method
definitions remain in the linked, versioned layer files.

## One KSODI Method, Three Public Scopes

[KSODI-Light](./KSODI-Light/README.md), KSODI-Standard-Eval and KSODI-Full
belong to the same KSODI method. They are neither competing methodologies nor
interchangeable implementations.

KSODI-Light is the compact, human-facing entry layer. It uses practical
K/S/O/D/I working questions for reflection within an interaction and does not
require an external Observer.

From KSODI-Standard-Eval onward, an external Observer evaluates observable,
source-attributed events through declared measurement profiles and preserves
event, entity, trajectory and provenance identities. This requires
corresponding observation infrastructure but does not prescribe one software
stack.

## Operator Names at the Observer Boundary

The formal Observer line begins with the ordered tuple `(K, S, O, D, I)`:

- `K` — **Observable Context Completeness**
- `S` — **Observable Structural Coherence**
- `O` — **Observable Grounded Objectivity**
- `D` — **Observable Clarity**
- `I` — **Observable Information Impulse**

KSODI-Light may use shorter human-facing labels for local reflection. This is
a viewpoint distinction, not a competing operator definition. Formal Observer
files must use the observer-facing names above or map their terms explicitly.

## Product Boundary

### KSODI-Standard-Eval: monadic trajectory observation

KSODI-Standard-Eval contains the complete monadic Observer line:

```text
source-attributed event
  -> K/S/O/D/I
  -> Z_A(k)
  -> IK_A(k)
```

Every value remains attached to one identified event in one declared
trajectory. KSODI-Standard-Eval ends with the monadic interaction-coherence
projection `IK_A(k)`.

### KSODI-Full: dyadic observation from R_0

KSODI-Full begins with dyadic observation at the Layer 4 gate `R_0`. The gate
evaluates whether two distinguishable monadic `Z`-trajectories support
relational observation. It does not merge them and is not calculated from
monadic `IK`.

Only after a stable `R_0` does the Layer 5 relational projection `IK_rel`
open. Both `R_0` and `IK_rel` belong to KSODI-Full, not
KSODI-Standard-Eval. Further application-specific R-family and signal-media
extensions occupy Layers 6–8 and remain separately staged in the current
public release.

The existence of an interaction, shared channel or exchange identifier does
not itself establish `R_0`, relational coherence, coupling, meaning or
causality.

## Shared Observer References

The following root-level references span KSODI-Standard-Eval and KSODI-Full:

- [Conceptual Note](./Conceptual-Note.md)
- [KSODI Architecture V350](./KSODI-Architecture_V350.md)
- [KSODI Hangar V350](./KSODI-Hangar_V350.md)
- [KSODI Implementation Guardrails](./IMPLEMENTATION_GUARDRAILS.md)
- [Public implementation-transfer examples](./implementation-examples/README.md)

The Hangar is the shared observer-side comparison space for attributable
states, trajectories, windows, distributions and point clouds. It is not a
merged internal state and not an additional main layer.

## Publication and Historical Boundary

The current public KSODI v3.5 release contains all five Layer-1 operator
definitions, the Layer-2 monadic state vector `Z_A(k)`, the Layer-3 monadic
projection `IK_A(k)`, the KSODI-Full Layer 4 gate `R_0` and the KSODI-Full
Layer 5 relational projection `IK_rel`.

Later R-family and signal-media elements remain staged until their own release
status says otherwise. Repository visibility alone is not a release marker.

Earlier v3.3 documents and the v3.42 implementation line are retained for
provenance, not as current implementation guidance:

- [Historical method material](./archive/method-history-v33/README.md)
- [Historical Observer visualizations](./archive/assets-archive/historical-observer-v342/README.md)

The visualizations remain important evidence of the implementation path and
help explain the later separation of monadic coherence, relational
comparability and further R-family observation.

## Licence Transition

KSODI-Standard-Eval and KSODI-Full were initially held under an
all-rights-reserved status and were later released as method documentation
under CC BY 4.0. Their mirrored transition notes point to the authoritative
repository licence and history:

- [KSODI-Standard-Eval licence transition](./KSODI-Standard-Eval/LICENCE_TRANSITION_NOTE.md)
- [KSODI-Full licence transition](./KSODI-Full/LICENCE_TRANSITION_NOTE.md)
- [Repository licence](./LICENSE.md)
- [Licence decision history](./LICENSE_HISTORY.md)

Separately published software implementations are distinct works and retain
the licence declared in their own repositories.

---

© 2026 Anne Steinacker-Folkerts & Heiko Folkerts
Licensed under CC BY 4.0
