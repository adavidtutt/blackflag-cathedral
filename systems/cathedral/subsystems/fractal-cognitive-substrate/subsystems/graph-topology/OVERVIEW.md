---
title: cathedral/fractal-cognitive-substrate/graph-topology Overview
status: bounded
tags:
  - subsystem
  - overview
  - cathedral
  - child-subsystem
  - bounded
  - cathedral-fractal-cognitive-substrate-graph-topology
  - fractal-cognitive-substrate
  - graph-topology
---

# cathedral/fractal-cognitive-substrate/graph-topology Overview

## Who
- graph designers
- epistemic-state designers
- refutation-system builders

## What

Typed graph stack, confidence lattice, and contradiction/refutation surfaces.

## Why

The map is not one graph; it is a stack of typed graph surfaces with attached trust and contradiction state.

## Where

- Path: `systems/cathedral/subsystems/fractal-cognitive-substrate/subsystems/graph-topology`
- Kind: `child-subsystem`
- Status: `bounded`
- Parent: `cathedral/fractal-cognitive-substrate`
- Depends on: `cathedral/fractal-cognitive-substrate/ontology`
- Allowed dependencies: `cathedral/graphs, cathedral/deterministic-truth, cathedral/fractal-cognitive-substrate/ontology, cathedral/fractal-cognitive-substrate/memory-topology, cathedral/fractal-cognitive-substrate/runtime-routing, cathedral/fractal-cognitive-substrate/compiler-learning, cathedral/fractal-cognitive-substrate/mapflow`
- Child subsystems: `none`

## Contract Node

- Class: `graph-law`
- Owns: `typed graph families, confidence lattice, contradiction semantics, refutation semantics, supersession semantics`
- Requires: `cathedral/fractal-cognitive-substrate/ontology`
- Emits to: `cathedral/fractal-cognitive-substrate/runtime-routing, cathedral/fractal-cognitive-substrate/compiler-learning, cathedral/fractal-cognitive-substrate/mapflow`
- Forbids: `residency policy ownership, dense-model translator law, untyped contradiction handling`

## How

- Canonical schema: [FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)
- Local readme: [README.md](README.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
- Contracts surface: [contracts](contracts/README.md)
- Tests surface: [tests](tests/README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when graph families, edge semantics, confidence vectors, or contradiction handling changes.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
