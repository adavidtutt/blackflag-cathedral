---
title: coding-foundry/parameter-lineage Overview
status: frozen
tags:
  - subsystem
  - overview
  - coding-foundry
  - child-subsystem
  - frozen
  - coding-foundry-parameter-lineage
  - parameter-lineage
---

# coding-foundry/parameter-lineage Overview

## Who
- training pipeline
- artifact registry
- future parameter-graph consumers

## What

Lineage metadata for checkpoints and runtime artifacts used by the coding lane.

## Why

The coding lane must emit parameter lineage that can later attach to the Cathedral parameter graph.

## Where

- Path: `systems/coding-foundry/subsystems/parameter-lineage`
- Kind: `child-subsystem`
- Status: `frozen`
- Parent: `coding-foundry`
- Depends on: `cathedral/graphs`
- Allowed dependencies: `cathedral/graphs, coding-foundry/memory, coding-foundry/promotion`
- Child subsystems: `none`

## How

- Canonical schema: [FOUNDRY_SCHEMA.md](../../../../docs/schemas/FOUNDRY_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when artifact ancestry, validity, or compatibility metadata changes.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [FOUNDRY_SCHEMA.md](../../../../docs/schemas/FOUNDRY_SCHEMA.md)
