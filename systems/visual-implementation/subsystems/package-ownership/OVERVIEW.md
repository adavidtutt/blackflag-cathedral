---
title: visual-implementation/package-ownership Overview
status: bounded
tags:
  - subsystem
  - overview
  - visual-implementation
  - child-subsystem
  - bounded
  - visual-implementation-package-ownership
  - package-ownership
---

# visual-implementation/package-ownership Overview

## Who
- codegen designers
- human implementers
- boundary maintainers

## What

Owned-zone rule for generated structure versus custom behavior.

## Why

Regeneration becomes a fistfight if compiler-owned and human-owned zones are not separated.

## Where

- Path: `systems/visual-implementation/subsystems/package-ownership`
- Kind: `child-subsystem`
- Status: `bounded`
- Parent: `visual-implementation`
- Depends on: `none`
- Allowed dependencies: `visual-implementation/projections`
- Child subsystems: `none`

## How

- Canonical schema: [VISUAL_IMPLEMENTATION_SCHEMA.md](../../../../docs/schemas/VISUAL_IMPLEMENTATION_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when package ownership rules or regeneration boundaries change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [VISUAL_IMPLEMENTATION_SCHEMA.md](../../../../docs/schemas/VISUAL_IMPLEMENTATION_SCHEMA.md)
