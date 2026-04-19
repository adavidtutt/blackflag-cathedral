---
title: visual-implementation/authoring-surface Overview
status: frozen
tags:
  - subsystem
  - overview
  - visual-implementation
  - child-subsystem
  - frozen
  - visual-implementation-authoring-surface
  - authoring-surface
---

# visual-implementation/authoring-surface Overview

## Who
- visual authors
- system designers
- future operator-authors

## What

Schematic or harness authoring surface for topology construction.

## Why

The machine must be drawable and navigable at depth.

## Where

- Path: `systems/visual-implementation/subsystems/authoring-surface`
- Kind: `child-subsystem`
- Status: `frozen`
- Parent: `visual-implementation`
- Depends on: `none`
- Allowed dependencies: `visual-implementation/bound-subdocumentation, visual-implementation/structural-ir`
- Child subsystems: `none`

## How

- Canonical schema: [VISUAL_IMPLEMENTATION_SCHEMA.md](../../../../docs/schemas/VISUAL_IMPLEMENTATION_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when authoring-surface assumptions or topology authoring rules change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [VISUAL_IMPLEMENTATION_SCHEMA.md](../../../../docs/schemas/VISUAL_IMPLEMENTATION_SCHEMA.md)
