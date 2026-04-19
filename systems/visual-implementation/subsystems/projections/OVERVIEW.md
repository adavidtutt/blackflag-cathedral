---
title: visual-implementation/projections Overview
status: bounded
tags:
  - subsystem
  - overview
  - visual-implementation
  - child-subsystem
  - bounded
  - visual-implementation-projections
  - projections
---

# visual-implementation/projections Overview

## Who
- code generators
- doc generators
- inventory generators

## What

Downstream projections to code, docs, inventories, and wiki surfaces.

## Why

One authored structural model must project outward into many useful surfaces.

## Where

- Path: `systems/visual-implementation/subsystems/projections`
- Kind: `child-subsystem`
- Status: `bounded`
- Parent: `visual-implementation`
- Depends on: `none`
- Allowed dependencies: `visual-implementation/structural-ir, visual-implementation/package-ownership, visual-implementation/gui-views`
- Child subsystems: `none`

## How

- Canonical schema: [VISUAL_IMPLEMENTATION_SCHEMA.md](../../../../docs/schemas/VISUAL_IMPLEMENTATION_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when generated outputs or projection boundaries change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [VISUAL_IMPLEMENTATION_SCHEMA.md](../../../../docs/schemas/VISUAL_IMPLEMENTATION_SCHEMA.md)
