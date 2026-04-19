---
title: visual-implementation Overview
status: frozen
tags:
  - subsystem
  - overview
  - visual-implementation
  - top-level-subsystem
  - frozen
---

# visual-implementation Overview

## Who
- visual architects
- compiler designers
- GUI/control-plane designers

## What

Truth-bearing visual authoring and compilation system.

## Why

The system must be buildable visually at depth, and the visual system plus bound subdocumentation must be able to change truth.

## Where

- Path: `systems/visual-implementation`
- Kind: `top-level-subsystem`
- Status: `frozen`
- Parent: `none`
- Depends on: `cathedral, coding-foundry`
- Allowed dependencies: `cathedral, coding-foundry`
- Child subsystems: `visual-implementation/authoring-surface, visual-implementation/bound-subdocumentation, visual-implementation/structural-ir, visual-implementation/structural-compiler, visual-implementation/projections, visual-implementation/package-ownership, visual-implementation/gui-views`

## How

- Canonical schema: [VISUAL_IMPLEMENTATION_SCHEMA.md](../../docs/schemas/VISUAL_IMPLEMENTATION_SCHEMA.md)
- Local readme: [README.md](README.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
- Contracts surface: [contracts](contracts/README.md)
- Tests surface: [tests](tests/README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when the visual authoring system, truth flow, or projection strategy changes.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [VISUAL_IMPLEMENTATION_SCHEMA.md](../../docs/schemas/VISUAL_IMPLEMENTATION_SCHEMA.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
