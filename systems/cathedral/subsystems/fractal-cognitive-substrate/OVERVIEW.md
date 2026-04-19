---
title: cathedral/fractal-cognitive-substrate Overview
status: bounded
tags:
  - subsystem
  - overview
  - cathedral
  - child-subsystem
  - bounded
  - cathedral-fractal-cognitive-substrate
  - fractal-cognitive-substrate
---

# cathedral/fractal-cognitive-substrate Overview

## Who
- system architects
- memory and routing designers
- future compiler operators

## What

Persistent cognitive-topology substrate for the Cathedral.

## Why

The Cathedral needs a canonical structure for the map-first substrate that binds memory, routing, contradiction, lineage, and recompilation into one executable doctrine.

## Where

- Path: `systems/cathedral/subsystems/fractal-cognitive-substrate`
- Kind: `child-subsystem`
- Status: `bounded`
- Parent: `cathedral`
- Depends on: `cathedral/memory, cathedral/graphs, cathedral/models, cathedral/query-path, cathedral/learning, cathedral/deterministic-truth`
- Allowed dependencies: `cathedral/memory, cathedral/graphs, cathedral/models, cathedral/query-path, cathedral/learning, cathedral/deterministic-truth, cathedral/fractal-cognitive-substrate/ontology, cathedral/fractal-cognitive-substrate/memory-topology, cathedral/fractal-cognitive-substrate/graph-topology, cathedral/fractal-cognitive-substrate/runtime-routing, cathedral/fractal-cognitive-substrate/compiler-learning, cathedral/fractal-cognitive-substrate/model-interface, cathedral/fractal-cognitive-substrate/mapflow`
- Child subsystems: `cathedral/fractal-cognitive-substrate/ontology, cathedral/fractal-cognitive-substrate/memory-topology, cathedral/fractal-cognitive-substrate/graph-topology, cathedral/fractal-cognitive-substrate/runtime-routing, cathedral/fractal-cognitive-substrate/compiler-learning, cathedral/fractal-cognitive-substrate/model-interface, cathedral/fractal-cognitive-substrate/mapflow`

## How

- Canonical schema: [FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)
- Local readme: [README.md](README.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
- Contracts surface: [contracts](contracts/README.md)
- Tests surface: [tests](tests/README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when the substrate doctrine, layer map, or cross-layer invariants change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
