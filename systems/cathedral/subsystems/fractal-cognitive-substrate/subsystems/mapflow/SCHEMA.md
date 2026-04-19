# MapFlow Contract Node

Canonical source:
- [../../../../../../docs/schemas/MAPFLOW_SCHEMA.md](../../../../../../docs/schemas/MAPFLOW_SCHEMA.md)
- [../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)

Contract node class:
- `authoring-lowering-law`

Owns:
- DSL grammar
- MapIR and later IR surfaces
- legality rules
- lowering rules
- execution-class declarations
- page and kernel lowering interfaces

Requires:
- `cathedral/fractal-cognitive-substrate/ontology`
- `cathedral/fractal-cognitive-substrate/memory-topology`
- `cathedral/fractal-cognitive-substrate/graph-topology`
- `cathedral/fractal-cognitive-substrate/runtime-routing`
- `cathedral/fractal-cognitive-substrate/compiler-learning`
- `cathedral/fractal-cognitive-substrate/model-interface`

Emits to:
- none

Forbids:
- a second ontology
- arbitrary graph wandering in the hot path
- lowering meaning-heavy irregular logic into kernels

Insertion rule:
- put grammar, IR, legality, lowering, and backend target doctrine here
