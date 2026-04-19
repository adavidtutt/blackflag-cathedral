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
- Allowed dependencies: `cathedral/models, cathedral/learning, cathedral/fractal-cognitive-substrate/ontology, cathedral/fractal-cognitive-substrate/runtime-routing`
- Child subsystems: `none`

## How

- Canonical schema: [FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when translator rules, model roles, or parameter-artifact boundaries change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md](../../../../../../docs/schemas/FRACTAL_COGNITIVE_SUBSTRATE_SCHEMA.md)
