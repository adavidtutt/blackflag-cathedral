---
title: coding-foundry/memory Overview
status: frozen
tags:
  - subsystem
  - overview
  - coding-foundry
  - child-subsystem
  - frozen
  - coding-foundry-memory
  - memory
---

# coding-foundry/memory Overview

## Who
- coding-memory designers
- trace and artifact designers
- future lane operators

## What

Coding-lane mapping of memory species.

## Why

The Foundry needs its own memory mapping while staying Cathedral-compatible.

## Where

- Path: `systems/coding-foundry/subsystems/memory`
- Kind: `child-subsystem`
- Status: `frozen`
- Parent: `coding-foundry`
- Depends on: `cathedral/memory`
- Allowed dependencies: `cathedral/memory, coding-foundry/deterministic-truth, coding-foundry/working-memory, coding-foundry/parameter-lineage`
- Child subsystems: `none`

## How

- Canonical schema: [FOUNDRY_SCHEMA.md](../../../../docs/schemas/FOUNDRY_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when coding-memory responsibilities or boundaries change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [FOUNDRY_SCHEMA.md](../../../../docs/schemas/FOUNDRY_SCHEMA.md)
