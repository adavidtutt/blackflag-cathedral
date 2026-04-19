---
title: cathedral/fractal-cognitive-substrate/model-interface Overview
status: bounded
tags:
  - subsystem
  - overview
  - cathedral
  - child-subsystem
  - bounded
  - cathedral-fractal-cognitive-substrate-model-interface
  - fractal-cognitive-substrate
  - model-interface
---

# cathedral/fractal-cognitive-substrate/model-interface Overview

## Who
- model-interface designers
- translator builders
- parameterization planners

## What

Deterministic/probabilistic split, translators, and parameter-system interface to dense models.

## Why

The substrate needs a formal interface for what models do, what they do not own, and how model-adjacent artifacts enter the map.

## Where

- Path: `systems/cathedral/subsystems/fractal-cognitive-substrate/subsystems/model-interface`
- Kind: `child-subsystem`
- Status: `bounded`
- Parent: `cathedral/fractal-cognitive-substrate`
- Depends on: `cathedral/fractal-cognitive-substrate/ontology`
- Allowed dependencies: `cathedral/models, cathedral/learning, cathedral/fractal-cognitive-substrate/ontology, cathedral/fractal-cognitive-substrate/runtime-routing, cathedral/fractal-cognitive-substrate/compiler-learning, cathedral/fractal-cognitive-substrate/mapflow`
- Child subsystems: `none`

## Contract Node

- Class: `model-boundary-law`
- Owns: `deterministic/probabilistic split, translator law, parameter-artifact boundary, model-adjacent promotion boundaries`
- Requires: `cathedral/fractal-cognitive-substrate/ontology`
- Emits to: `cathedral/fractal-cognitive-substrate/runtime-routing, cathedral/fractal-cognitive-substrate/compiler-learning, cathedral/fractal-cognitive-substrate/mapflow`
- Forbids: `primary fact storage, contradiction ownership, world-truth authority`

## How

- Canonical schema: [FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)
- Local readme: [README.md](README.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
- Contracts surface: [contracts](contracts/README.md)
- Tests surface: [tests](tests/README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when translator rules, model roles, or parameter-artifact boundaries change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
