---
title: cathedral Overview
status: frozen
tags:
  - subsystem
  - overview
  - cathedral
  - top-level-subsystem
  - frozen
---

# cathedral Overview

## Who
- human architect
- future cathedral controllers
- all downstream subsystem owners

## What

Final-system architecture that frames the whole project as a distributed cognition machine rather than a single model.

## Why

This is the highest-level authority surface for what the final machine is supposed to be.

## Where

- Path: `systems/cathedral`
- Kind: `top-level-subsystem`
- Status: `frozen`
- Parent: `none`
- Depends on: `none`
- Allowed dependencies: `none`
- Child subsystems: `cathedral/memory, cathedral/graphs, cathedral/models, cathedral/query-path, cathedral/learning, cathedral/deterministic-truth`

## How

- Canonical schema: [CATHEDRAL_SCHEMA.md](../../docs/schemas/CATHEDRAL_SCHEMA.md)
- Local readme: [README.md](README.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
- Contracts surface: [contracts](contracts/README.md)
- Tests surface: [tests](tests/README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when the final-system shape, first principles, or top-level cognitive strata change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [CATHEDRAL_SCHEMA.md](../../docs/schemas/CATHEDRAL_SCHEMA.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
