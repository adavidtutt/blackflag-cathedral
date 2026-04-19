---
title: training/datasets Overview
status: bounded
tags:
  - subsystem
  - overview
  - training
  - child-subsystem
  - bounded
  - training-datasets
  - datasets
---

# training/datasets Overview

## Who
- dataset curators
- training pipeline owners
- evaluation designers

## What

Dataset directions and role-specific training data mappings.

## Why

Role-specific training only works if the dataset boundaries are explicit.

## Where

- Path: `systems/training/subsystems/datasets`
- Kind: `child-subsystem`
- Status: `bounded`
- Parent: `training`
- Depends on: `none`
- Allowed dependencies: `training/roles`
- Child subsystems: `none`

## How

- Canonical schema: [TRAINING_SCHEMA.md](../../../../docs/schemas/TRAINING_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when dataset mappings, corpus directions, or role-data relationships change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [TRAINING_SCHEMA.md](../../../../docs/schemas/TRAINING_SCHEMA.md)
