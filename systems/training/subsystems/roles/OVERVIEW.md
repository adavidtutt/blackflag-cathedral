---
title: training/roles Overview
status: frozen
tags:
  - subsystem
  - overview
  - training
  - child-subsystem
  - frozen
  - training-roles
  - roles
---

# training/roles Overview

## Who
- role planners
- training owners
- model-family maintainers

## What

Per-role model family and role separation rule.

## Why

Each role keeps its own training lane and checkpoint family.

## Where

- Path: `systems/training/subsystems/roles`
- Kind: `child-subsystem`
- Status: `frozen`
- Parent: `training`
- Depends on: `none`
- Allowed dependencies: `training/datasets, training/hardware`
- Child subsystems: `none`

## How

- Canonical schema: [TRAINING_SCHEMA.md](../../../../docs/schemas/TRAINING_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when role count, role identity, or base model assignment changes.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [TRAINING_SCHEMA.md](../../../../docs/schemas/TRAINING_SCHEMA.md)
