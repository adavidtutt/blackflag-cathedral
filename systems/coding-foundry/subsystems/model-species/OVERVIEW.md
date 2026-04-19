---
title: coding-foundry/model-species Overview
status: frozen
tags:
  - subsystem
  - overview
  - coding-foundry
  - child-subsystem
  - frozen
  - coding-foundry-model-species
  - model-species
---

# coding-foundry/model-species Overview

## Who
- coding model planners
- lane designers
- critic designers

## What

Scouts, judges, packet builders, route controllers, synthesis models, critics, and consolidators for the coding lane.

## Why

The coding lane itself is a model society, not one model plus prompts.

## Where

- Path: `systems/coding-foundry/subsystems/model-species`
- Kind: `child-subsystem`
- Status: `frozen`
- Parent: `coding-foundry`
- Depends on: `cathedral/models`
- Allowed dependencies: `cathedral/models, coding-foundry/packets, coding-foundry/memory, coding-foundry/promotion`
- Child subsystems: `none`

## How

- Canonical schema: [FOUNDRY_SCHEMA.md](../../../../docs/schemas/FOUNDRY_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when coding-lane species or role assignments change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [FOUNDRY_SCHEMA.md](../../../../docs/schemas/FOUNDRY_SCHEMA.md)
