---
title: coding-foundry Overview
status: frozen
tags:
  - subsystem
  - overview
  - coding-foundry
  - top-level-subsystem
  - frozen
---

# coding-foundry Overview

## Who
- coding-lane designers
- harness designers
- training designers

## What

Cathedral-compatible coding lane that builds and later lives inside the larger system.

## Why

The Coding Foundry is the bounded subsystem used to build and operationalize the coding species of the larger system.

## Where

- Path: `systems/coding-foundry`
- Kind: `top-level-subsystem`
- Status: `frozen`
- Parent: `none`
- Depends on: `cathedral, harness, training, visual-implementation`
- Allowed dependencies: `cathedral, harness, training, visual-implementation`
- Child subsystems: `coding-foundry/packets, coding-foundry/memory, coding-foundry/model-species, coding-foundry/deterministic-truth, coding-foundry/working-memory, coding-foundry/parameter-lineage, coding-foundry/promotion`

## How

- Canonical schema: [FOUNDRY_SCHEMA.md](../../docs/schemas/FOUNDRY_SCHEMA.md)
- Local readme: [README.md](README.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
- Contracts surface: [contracts](contracts/README.md)
- Tests surface: [tests](tests/README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when the coding lane’s purpose, scope, or top-level boundaries change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [FOUNDRY_SCHEMA.md](../../docs/schemas/FOUNDRY_SCHEMA.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
