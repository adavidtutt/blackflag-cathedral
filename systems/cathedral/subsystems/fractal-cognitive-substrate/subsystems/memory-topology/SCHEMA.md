# FCS Memory Topology Contract Node

Canonical source:
- [../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)

Contract node class:
- `memory-plane-law`

Owns:
- cold plane
- warm plane
- hot plane
- speculative plane
- residency law
- staging law
- object granularity law

Requires:
- `cathedral/fractal-cognitive-substrate/ontology`

Emits to:
- `cathedral/fractal-cognitive-substrate/graph-topology`
- `cathedral/fractal-cognitive-substrate/runtime-routing`
- `cathedral/fractal-cognitive-substrate/mapflow`

Forbids:
- graph contradiction semantics
- model role boundaries
- payload identity rules outside ontology

Insertion rule:
- put plane roles, residency classes, staging rules, and object sizing law here
