---
title: cathedral/fractal-cognitive-substrate/mapflow Overview
status: bounded
tags:
  - subsystem
  - overview
  - cathedral
  - child-subsystem
  - bounded
  - cathedral-fractal-cognitive-substrate-mapflow
  - fractal-cognitive-substrate
  - mapflow
---

# cathedral/fractal-cognitive-substrate/mapflow Overview

## Who
- DSL designers
- compiler engineers
- runtime-lowering designers

## What

Language and compiler surface for expressing and lowering FCS semantics.

## Why

FCS needs a first-class authoring and lowering surface that preserves substrate semantics while lowering only regular dense work into fast kernels.

## Where

- Path: `systems/cathedral/subsystems/fractal-cognitive-substrate/subsystems/mapflow`
- Kind: `child-subsystem`
- Status: `bounded`
- Parent: `cathedral/fractal-cognitive-substrate`
- Depends on: `cathedral/fractal-cognitive-substrate/ontology, cathedral/fractal-cognitive-substrate/memory-topology, cathedral/fractal-cognitive-substrate/graph-topology, cathedral/fractal-cognitive-substrate/runtime-routing, cathedral/fractal-cognitive-substrate/compiler-learning, cathedral/fractal-cognitive-substrate/model-interface`
- Allowed dependencies: `cathedral/memory, cathedral/models, cathedral/query-path, cathedral/learning, cathedral/fractal-cognitive-substrate/ontology, cathedral/fractal-cognitive-substrate/memory-topology, cathedral/fractal-cognitive-substrate/graph-topology, cathedral/fractal-cognitive-substrate/runtime-routing, cathedral/fractal-cognitive-substrate/compiler-learning, cathedral/fractal-cognitive-substrate/model-interface`
- Child subsystems: `none`

## Contract Node

- Class: `authoring-lowering-law`
- Owns: `DSL grammar, MapIR and later IR surfaces, legality rules, lowering rules, execution-class declarations, page and kernel lowering interfaces`
- Requires: `cathedral/fractal-cognitive-substrate/ontology, cathedral/fractal-cognitive-substrate/memory-topology, cathedral/fractal-cognitive-substrate/graph-topology, cathedral/fractal-cognitive-substrate/runtime-routing, cathedral/fractal-cognitive-substrate/compiler-learning, cathedral/fractal-cognitive-substrate/model-interface`
- Emits to: `none`
- Forbids: `a second ontology, arbitrary graph wandering in the hot path, lowering meaning-heavy irregular logic into kernels`

## How

- Canonical schema: [MAPFLOW_SCHEMA.md](../../../../../../docs/schemas/MAPFLOW_SCHEMA.md)
- Local readme: [README.md](README.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
- Contracts surface: [contracts](contracts/README.md)
- Tests surface: [tests](tests/README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when DSL constructs, IR layers, legality rules, scheduling doctrine, or backend-lowering boundaries change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [MAPFLOW_SCHEMA.md](../../../../../../docs/schemas/MAPFLOW_SCHEMA.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
