---
title: cathedral/fractal-cognitive-substrate/memory-topology Overview
status: bounded
tags:
  - subsystem
  - overview
  - cathedral
  - child-subsystem
  - bounded
  - cathedral-fractal-cognitive-substrate-memory-topology
  - fractal-cognitive-substrate
  - memory-topology
---

# cathedral/fractal-cognitive-substrate/memory-topology Overview

## Who
- memory-plane designers
- hydration planners
- residency-policy builders

## What

Cold, warm, hot, and speculative memory-plane structure for the substrate.

## Why

The substrate only works if different memory planes have explicit roles, representations, and transfer rules.

## Where

- Path: `systems/cathedral/subsystems/fractal-cognitive-substrate/subsystems/memory-topology`
- Kind: `child-subsystem`
- Status: `bounded`
- Parent: `cathedral/fractal-cognitive-substrate`
- Depends on: `cathedral/fractal-cognitive-substrate/ontology`
- Allowed dependencies: `cathedral/memory, cathedral/fractal-cognitive-substrate/ontology, cathedral/fractal-cognitive-substrate/graph-topology, cathedral/fractal-cognitive-substrate/runtime-routing, cathedral/fractal-cognitive-substrate/mapflow`
- Child subsystems: `none`

## Contract Node

- Class: `memory-plane-law`
- Owns: `cold plane, warm plane, hot plane, speculative plane, residency law, staging law, object granularity law`
- Requires: `cathedral/fractal-cognitive-substrate/ontology`
- Emits to: `cathedral/fractal-cognitive-substrate/graph-topology, cathedral/fractal-cognitive-substrate/runtime-routing, cathedral/fractal-cognitive-substrate/mapflow`
- Forbids: `graph contradiction semantics, model role boundaries, payload identity rules outside ontology`

## How

- Canonical schema: [FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)
- Local readme: [README.md](README.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
- Contracts surface: [contracts](contracts/README.md)
- Tests surface: [tests](tests/README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when memory planes, staging rules, or object-granularity policies change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
