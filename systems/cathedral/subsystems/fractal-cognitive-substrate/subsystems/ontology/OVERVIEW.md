---
title: cathedral/fractal-cognitive-substrate/ontology Overview
status: bounded
tags:
  - subsystem
  - overview
  - cathedral
  - child-subsystem
  - bounded
  - cathedral-fractal-cognitive-substrate-ontology
  - fractal-cognitive-substrate
  - ontology
---

# cathedral/fractal-cognitive-substrate/ontology Overview

## Who
- ontology designers
- schema maintainers
- artifact-identity builders

## What

Universal artifact, node, payload, and contract law for the substrate.

## Why

The substrate needs one reusable shell law so all later layers compose instead of drifting into incompatible object families.

## Where

- Path: `systems/cathedral/subsystems/fractal-cognitive-substrate/subsystems/ontology`
- Kind: `child-subsystem`
- Status: `bounded`
- Parent: `cathedral/fractal-cognitive-substrate`
- Depends on: `none`
- Allowed dependencies: `cathedral/memory, cathedral/graphs, cathedral/deterministic-truth, cathedral/fractal-cognitive-substrate/memory-topology, cathedral/fractal-cognitive-substrate/graph-topology, cathedral/fractal-cognitive-substrate/runtime-routing, cathedral/fractal-cognitive-substrate/compiler-learning, cathedral/fractal-cognitive-substrate/model-interface, cathedral/fractal-cognitive-substrate/mapflow`
- Child subsystems: `none`

## Contract Node

- Class: `substrate-law`
- Owns: `artifact classes, node contract, payload classes, identity rules, lineage surfaces, universal verbs`
- Requires: `none`
- Emits to: `cathedral/fractal-cognitive-substrate/memory-topology, cathedral/fractal-cognitive-substrate/graph-topology, cathedral/fractal-cognitive-substrate/runtime-routing, cathedral/fractal-cognitive-substrate/compiler-learning, cathedral/fractal-cognitive-substrate/model-interface, cathedral/fractal-cognitive-substrate/mapflow`
- Forbids: `duplicate node law outside ontology, mutable identity semantics in downstream layers, payload custody rules embedded in child layers without ontology updates`

## How

- Canonical schema: [FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)
- Local readme: [README.md](README.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
- Contracts surface: [contracts](contracts/README.md)
- Tests surface: [tests](tests/README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when node fields, artifact classes, universal verbs, or identity semantics change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
