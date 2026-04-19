---
title: training/runtime-planes Overview
status: bounded
tags:
  - subsystem
  - overview
  - training
  - child-subsystem
  - bounded
  - training-runtime-planes
  - runtime-planes
---

# training/runtime-planes Overview

## Who
- runtime planners
- serving planners
- training planners

## What

Training-linked hot, warm, and cold runtime economics.

## Why

Training and serving economics are linked through which models stay loaded and when.

## Where

- Path: `systems/training/subsystems/runtime-planes`
- Kind: `child-subsystem`
- Status: `bounded`
- Parent: `training`
- Depends on: `none`
- Allowed dependencies: `training/hardware`
- Child subsystems: `none`

## How

- Canonical schema: [TRAINING_SCHEMA.md](../../../../docs/schemas/TRAINING_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when training-driven runtime-plane assumptions change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [TRAINING_SCHEMA.md](../../../../docs/schemas/TRAINING_SCHEMA.md)
