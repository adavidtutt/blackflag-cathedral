---
title: harness/runtime-planes Overview
status: bounded
tags:
  - subsystem
  - overview
  - harness
  - child-subsystem
  - bounded
  - harness-runtime-planes
  - runtime-planes
---

# harness/runtime-planes Overview

## Who
- runtime planners
- scheduler owners
- model-loading operators

## What

Hot, warm, and cold runtime-plane distinctions for serving economics.

## Why

Not all model tiers should stay loaded the same way all the time.

## Where

- Path: `systems/harness/subsystems/runtime-planes`
- Kind: `child-subsystem`
- Status: `bounded`
- Parent: `harness`
- Depends on: `none`
- Allowed dependencies: `harness/scheduler, training/runtime-planes`
- Child subsystems: `none`

## How

- Canonical schema: [HARNESS_SCHEMA.md](../../../../docs/schemas/HARNESS_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when plane definitions or loading economics change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [HARNESS_SCHEMA.md](../../../../docs/schemas/HARNESS_SCHEMA.md)
