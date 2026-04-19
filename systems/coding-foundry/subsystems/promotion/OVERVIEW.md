---
title: coding-foundry/promotion Overview
status: bounded
tags:
  - subsystem
  - overview
  - coding-foundry
  - child-subsystem
  - bounded
  - coding-foundry-promotion
  - promotion
---

# coding-foundry/promotion Overview

## Who
- promotion logic
- consolidators
- future trainer loops

## What

Promotion and consolidation hooks across fast, medium, and slow loops in the coding lane.

## Why

Successful repeated behavior must have a path to become durable structure.

## Where

- Path: `systems/coding-foundry/subsystems/promotion`
- Kind: `child-subsystem`
- Status: `bounded`
- Parent: `coding-foundry`
- Depends on: `cathedral/learning`
- Allowed dependencies: `cathedral/learning, coding-foundry/model-species, coding-foundry/parameter-lineage, coding-foundry/deterministic-truth`
- Child subsystems: `none`

## How

- Canonical schema: [FOUNDRY_SCHEMA.md](../../../../docs/schemas/FOUNDRY_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when promotion rules, consolidation triggers, or loop boundaries change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [FOUNDRY_SCHEMA.md](../../../../docs/schemas/FOUNDRY_SCHEMA.md)
