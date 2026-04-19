---
title: cathedral/memory Overview
status: frozen
tags:
  - subsystem
  - overview
  - cathedral
  - child-subsystem
  - frozen
  - cathedral-memory
  - memory
---

# cathedral/memory Overview

## Who
- memory designers
- retrieval designers
- future memory operators

## What

Memory-species decomposition for the Cathedral.

## Why

The Cathedral depends on memory being split into species rather than collapsed into one store.

## Where

- Path: `systems/cathedral/subsystems/memory`
- Kind: `child-subsystem`
- Status: `frozen`
- Parent: `cathedral`
- Depends on: `none`
- Allowed dependencies: `cathedral/graphs, cathedral/deterministic-truth`
- Child subsystems: `none`

## How

- Canonical schema: [CATHEDRAL_SCHEMA.md](../../../../docs/schemas/CATHEDRAL_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when memory species, boundaries, or cross-memory responsibilities change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [CATHEDRAL_SCHEMA.md](../../../../docs/schemas/CATHEDRAL_SCHEMA.md)
