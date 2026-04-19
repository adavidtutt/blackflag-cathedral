# Fractal Cognitive Substrate Surface

Canonical source:
- [../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)

Layer and compiler surfaces:
- `ontology`
- `memory-topology`
- `graph-topology`
- `runtime-routing`
- `compiler-learning`
- `model-interface`
- `mapflow`

Insertion rule:
- add new doctrine to the smallest coherent layer that can own it
- if the doctrine is a cross-cutting authoring or lowering surface, place it in `mapflow`
- if a new concept spans layers, update the deep schema first, then attach layer-local consequences
- do not create parallel vocabulary when an existing layer can own the addition
