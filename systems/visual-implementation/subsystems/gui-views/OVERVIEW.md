---
title: visual-implementation/gui-views Overview
status: bounded
tags:
  - subsystem
  - overview
  - visual-implementation
  - child-subsystem
  - bounded
  - visual-implementation-gui-views
  - gui-views
---

# visual-implementation/gui-views Overview

## Who
- GUI designers
- operators
- future self-observing system layers

## What

Operator, observability, and self-visibility GUI projections.

## Why

The GUI is another compiled view of the same canonical structural model.

## Where

- Path: `systems/visual-implementation/subsystems/gui-views`
- Kind: `child-subsystem`
- Status: `bounded`
- Parent: `visual-implementation`
- Depends on: `none`
- Allowed dependencies: `visual-implementation/projections, visual-implementation/structural-ir`
- Child subsystems: `none`

## How

- Canonical schema: [VISUAL_IMPLEMENTATION_SCHEMA.md](../../../../docs/schemas/VISUAL_IMPLEMENTATION_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when GUI/control-plane projection boundaries or view families change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [VISUAL_IMPLEMENTATION_SCHEMA.md](../../../../docs/schemas/VISUAL_IMPLEMENTATION_SCHEMA.md)
