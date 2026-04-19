---
title: visual-implementation/structural-compiler Overview
status: bounded
tags:
  - subsystem
  - overview
  - visual-implementation
  - child-subsystem
  - bounded
  - visual-implementation-structural-compiler
  - structural-compiler
---

# visual-implementation/structural-compiler Overview

## Who
- compiler designers
- projection designers
- validation designers

## What

Compiler passes from authored truth into IR and projections.

## Why

The visual system only gains leverage if its authored truth can be compiled and regenerated systematically.

## Where

- Path: `systems/visual-implementation/subsystems/structural-compiler`
- Kind: `child-subsystem`
- Status: `bounded`
- Parent: `visual-implementation`
- Depends on: `none`
- Allowed dependencies: `visual-implementation/structural-ir, visual-implementation/projections, visual-implementation/package-ownership, visual-implementation/gui-views`
- Child subsystems: `none`

## How

- Canonical schema: [STRUCTURAL_COMPILER_SCHEMA.md](../../../../docs/schemas/STRUCTURAL_COMPILER_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when compiler stages, extraction rules, or validation passes change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [STRUCTURAL_COMPILER_SCHEMA.md](../../../../docs/schemas/STRUCTURAL_COMPILER_SCHEMA.md)
