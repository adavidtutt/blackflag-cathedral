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
- Depends on: `cathedral/fractal-cognitive-substrate/ontology, cathedral/fractal-cognitive-substrate/memory-topology, cathedral/fractal-cognitive-substrate/graph-topology`
- Allowed dependencies: `cathedral/query-path, cathedral/models, cathedral/deterministic-truth, cathedral/fractal-cognitive-substrate/ontology, cathedral/fractal-cognitive-substrate/memory-topology, cathedral/fractal-cognitive-substrate/graph-topology, cathedral/fractal-cognitive-substrate/model-interface`
- Child subsystems: `none`

## How

- Canonical schema: [FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when route-sketch fields, hydration behavior, or turn-loop arbitration changes.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)
