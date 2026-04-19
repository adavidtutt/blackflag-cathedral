---
title: cathedral/fractal-cognitive-substrate/runtime-routing Overview
status: bounded
tags:
  - subsystem
  - overview
  - cathedral
  - child-subsystem
  - bounded
  - cathedral-fractal-cognitive-substrate-runtime-routing
  - fractal-cognitive-substrate
  - runtime-routing
---

# cathedral/fractal-cognitive-substrate/runtime-routing Overview

## Who
- runtime designers
- router builders
- execution-plane operators

## What

Hot route sketch, hydration pipeline, and live execution loop for the substrate.

## Why

The substrate needs an explicit lowering from durable structure into compact live execution state.

## Where

- Path: `systems/cathedral/subsystems/fractal-cognitive-substrate/subsystems/runtime-routing`
- Kind: `child-subsystem`
- Status: `bounded`
- Parent: `cathedral/fractal-cognitive-substrate`
- Depends on: `cathedral/fractal-cognitive-substrate/ontology, cathedral/fractal-cognitive-substrate/memory-topology, cathedral/fractal-cognitive-substrate/graph-topology, cathedral/fractal-cognitive-substrate/model-interface`
- Allowed dependencies: `cathedral/query-path, cathedral/models, cathedral/deterministic-truth, cathedral/fractal-cognitive-substrate/ontology, cathedral/fractal-cognitive-substrate/memory-topology, cathedral/fractal-cognitive-substrate/graph-topology, cathedral/fractal-cognitive-substrate/model-interface, cathedral/fractal-cognitive-substrate/compiler-learning, cathedral/fractal-cognitive-substrate/mapflow`
- Child subsystems: `none`

## Contract Node

- Class: `route-execution-law`
- Owns: `route sketch, hydration pipeline, turn arbitration, execution budgets, traversal stop rules`
- Requires: `cathedral/fractal-cognitive-substrate/ontology, cathedral/fractal-cognitive-substrate/memory-topology, cathedral/fractal-cognitive-substrate/graph-topology, cathedral/fractal-cognitive-substrate/model-interface`
- Emits to: `cathedral/fractal-cognitive-substrate/compiler-learning, cathedral/fractal-cognitive-substrate/mapflow`
- Forbids: `primary fact ownership, ontology redefinition, unbounded graph traversal`

## How

- Canonical schema: [FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)
- Local readme: [README.md](README.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
- Contracts surface: [contracts](contracts/README.md)
- Tests surface: [tests](tests/README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when route-sketch fields, hydration behavior, or turn-loop arbitration changes.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
