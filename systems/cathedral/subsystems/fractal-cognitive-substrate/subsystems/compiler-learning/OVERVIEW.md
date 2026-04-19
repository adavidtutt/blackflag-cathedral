---
title: cathedral/fractal-cognitive-substrate/compiler-learning Overview
status: bounded
tags:
  - subsystem
  - overview
  - cathedral
  - child-subsystem
  - bounded
  - cathedral-fractal-cognitive-substrate-compiler-learning
  - fractal-cognitive-substrate
  - compiler-learning
---

# cathedral/fractal-cognitive-substrate/compiler-learning Overview

## Who
- compiler designers
- promotion designers
- consolidation operators

## What

Background compilation, exhaust reuse, compression, and self-rewrite loops.

## Why

The substrate only becomes self-compiling if runtime exhaust is turned into better route priors, summaries, and durable structure.

## Where

- Path: `systems/cathedral/subsystems/fractal-cognitive-substrate/subsystems/compiler-learning`
- Kind: `child-subsystem`
- Status: `bounded`
- Parent: `cathedral/fractal-cognitive-substrate`
- Depends on: `cathedral/fractal-cognitive-substrate/runtime-routing, cathedral/fractal-cognitive-substrate/model-interface, cathedral/fractal-cognitive-substrate/graph-topology`
- Allowed dependencies: `cathedral/learning, cathedral/fractal-cognitive-substrate/ontology, cathedral/fractal-cognitive-substrate/graph-topology, cathedral/fractal-cognitive-substrate/runtime-routing, cathedral/fractal-cognitive-substrate/model-interface, cathedral/fractal-cognitive-substrate/mapflow`
- Child subsystems: `none`

## Contract Node

- Class: `rewrite-learning-law`
- Owns: `exhaust capture, route-prior rewrite, summary generation, promotion and demotion, replay-capsule generation, compression families, speculative prestaging`
- Requires: `cathedral/fractal-cognitive-substrate/runtime-routing, cathedral/fractal-cognitive-substrate/model-interface, cathedral/fractal-cognitive-substrate/graph-topology`
- Emits to: `cathedral/fractal-cognitive-substrate/runtime-routing, cathedral/fractal-cognitive-substrate/mapflow`
- Forbids: `sovereign hot execution ownership, direct world-fact storage, untagged exhaust classes`

## How

- Canonical schema: [FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)
- Local readme: [README.md](README.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
- Contracts surface: [contracts](contracts/README.md)
- Tests surface: [tests](tests/README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when compiler jobs, compression families, promotion logic, or consolidation loops change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
