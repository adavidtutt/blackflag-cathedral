---
title: training/hardware Overview
status: frozen
tags:
  - subsystem
  - overview
  - training
  - child-subsystem
  - frozen
  - training-hardware
  - hardware
---

# training/hardware Overview

## Who
- hardware planners
- cost planners
- training operators

## What

Cheapest-acceptable-hardware policy and escalation triggers.

## Why

Quality must be preserved while still exploiting favorable compute economics.

## Where

- Path: `systems/training/subsystems/hardware`
- Kind: `child-subsystem`
- Status: `frozen`
- Parent: `training`
- Depends on: `none`
- Allowed dependencies: `training/roles, training/runtime-planes`
- Child subsystems: `none`

## How

- Canonical schema: [TRAINING_SCHEMA.md](../../../../docs/schemas/TRAINING_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when hardware classes, escalation triggers, or economic assumptions change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [TRAINING_SCHEMA.md](../../../../docs/schemas/TRAINING_SCHEMA.md)
