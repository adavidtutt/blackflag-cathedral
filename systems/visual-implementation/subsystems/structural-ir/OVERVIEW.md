---
title: visual-implementation/structural-ir Overview
status: frozen
tags:
  - subsystem
  - overview
  - visual-implementation
  - child-subsystem
  - frozen
  - visual-implementation-structural-ir
  - structural-ir
---

# visual-implementation/structural-ir Overview

## Who
- IR designers
- compiler designers
- projection generators

## What

Machine-canonical structural layer compiled from authored truth.

## Why

The system needs a machine-stable truth layer for regeneration and downstream targets.

## Where

- Path: `systems/visual-implementation/subsystems/structural-ir`
- Kind: `child-subsystem`
- Status: `frozen`
- Parent: `visual-implementation`
- Depends on: `none`
- Allowed dependencies: `visual-implementation/bound-subdocumentation, visual-implementation/structural-compiler, visual-implementation/projections`
- Child subsystems: `none`

## How

- Canonical schema: [STRUCTURAL_COMPILER_SCHEMA.md](../../../../docs/schemas/STRUCTURAL_COMPILER_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when structural IR fields, boundaries, or authority rules change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [STRUCTURAL_COMPILER_SCHEMA.md](../../../../docs/schemas/STRUCTURAL_COMPILER_SCHEMA.md)
