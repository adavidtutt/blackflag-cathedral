---
title: training Overview
status: frozen
tags:
  - subsystem
  - overview
  - training
  - top-level-subsystem
  - frozen
---

# training Overview

## Who
- training designers
- dataset planners
- hardware planners

## What

Role-specific model and hardware training plan for the coding lane.

## Why

The training system preserves separate role training and its cost-aware hardware logic.

## Where

- Path: `systems/training`
- Kind: `top-level-subsystem`
- Status: `frozen`
- Parent: `none`
- Depends on: `coding-foundry`
- Allowed dependencies: `coding-foundry`
- Child subsystems: `training/roles, training/datasets, training/hardware, training/runtime-planes`

## How

- Canonical schema: [TRAINING_SCHEMA.md](../../docs/schemas/TRAINING_SCHEMA.md)
- Local readme: [README.md](README.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
- Contracts surface: [contracts](contracts/README.md)
- Tests surface: [tests](tests/README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when role training, datasets, or hardware policy changes.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [TRAINING_SCHEMA.md](../../docs/schemas/TRAINING_SCHEMA.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
