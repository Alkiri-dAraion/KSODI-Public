# Work Notes - Canonical v350 Operators

Status: public work guidance for canonical operator review

Purpose: keep the v350 operator definitions architecture-independent before
they are adapted into the Observer infrastructure.

Rules:

- define the operator meaning first
- name the observable unit, reference space and comparability conditions
- avoid Kubernetes, Docker, database, vector-store, graph-store or monitoring
  assumptions
- avoid Observer-layer aggregation details unless they are explicitly marked as
  non-normative orientation
- preserve the sender / receiver boundary, especially for `I0`
- use `Ref_t` for the turn-specific reference space
- do not reintroduce active v350 terms such as `R_takt`, `R_phase`,
  `R_struc`, `R_struct`, `R_freq`, voice overlay or takt overlay

Workflow:

1. Review the canonical operator here.
2. Only after review, adapt it into `../Standard-Eval_v350/layer-1-operators`.
3. If the Observer adaptation needs implementation-specific wording, keep that
   wording in the `Standard-Eval_v350` layer structure, not in the canonical
   operator file.
