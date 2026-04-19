# FCS Runtime Routing Contract Node

Canonical source:
- [../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)

Contract node class:
- `route-execution-law`

Owns:
- route sketch
- hydration pipeline
- turn arbitration
- execution budgets
- traversal stop rules

Requires:
- `cathedral/fractal-cognitive-substrate/ontology`
- `cathedral/fractal-cognitive-substrate/memory-topology`
- `cathedral/fractal-cognitive-substrate/graph-topology`
- `cathedral/fractal-cognitive-substrate/model-interface`

Emits to:
- `cathedral/fractal-cognitive-substrate/compiler-learning`
- `cathedral/fractal-cognitive-substrate/mapflow`

Forbids:
- primary fact ownership
- ontology redefinition
- unbounded graph traversal

Insertion rule:
- put hot projection, hydration, arbitration, and traversal-budget law here
