---
title: harness/scheduler Overview
status: frozen
tags:
  - subsystem
  - overview
  - harness
  - child-subsystem
  - frozen
  - harness-scheduler
  - scheduler
---

# harness/scheduler Overview

## Who
- route planners
- queue managers
- runtime-plane selectors

## What

Placement and lifecycle decision boundary for the harness.

## Why

The scheduler owns work classification, queue placement, and runtime-plane decisions.

## Where

- Path: `systems/harness/subsystems/scheduler`
- Kind: `child-subsystem`
- Status: `frozen`
- Parent: `harness`
- Depends on: `none`
- Allowed dependencies: `harness/broker, harness/runtime-planes`
- Child subsystems: `none`

## How

- Canonical schema: [HARNESS_SCHEMA.md](../../../../docs/schemas/HARNESS_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when scheduling authority, leases, retries, or plane selection changes.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [HARNESS_SCHEMA.md](../../../../docs/schemas/HARNESS_SCHEMA.md)
