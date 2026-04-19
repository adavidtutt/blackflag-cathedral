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

Layer contract-node law:
- every FCS layer is treated as a contract node
- every layer must declare:
  - what it owns
  - what it requires
  - what it may emit to
  - what it explicitly forbids
- layer contract law lives in:
  - layer `manifest.yaml`
  - layer `SCHEMA.md`
  - layer `contracts/README.md`
  - layer `tests/README.md`

Canonical dependency law:
- `ontology` is the root law surface
- `memory-topology` depends on `ontology`
- `graph-topology` depends on `ontology`
- `model-interface` depends on `ontology`
- `runtime-routing` depends on `ontology`, `memory-topology`, `graph-topology`, and `model-interface`
- `compiler-learning` depends on `runtime-routing`, `model-interface`, and `graph-topology`
- `mapflow` depends on `ontology`, `memory-topology`, `graph-topology`, `runtime-routing`, `compiler-learning`, and `model-interface`

Rule:
- if a layer requires another layer structurally, that edge must appear in both `depends_on` and the layer's contract-node `requires`
- if a layer emits doctrine or compiled consequences into another layer, that edge must appear in the layer's contract-node `emits_to`

Insertion rule:
- add new doctrine to the smallest coherent layer that can own it
- if the doctrine is a cross-cutting authoring or lowering surface, place it in `mapflow`
- if a new concept spans layers, update the deep schema first, then attach layer-local consequences
- do not create parallel vocabulary when an existing layer can own the addition
