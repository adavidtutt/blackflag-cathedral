---
title: coding-foundry/working-memory Overview
status: bounded
tags:
  - subsystem
  - overview
  - coding-foundry
  - child-subsystem
  - bounded
  - coding-foundry-working-memory
  - working-memory
---

# coding-foundry/working-memory Overview

## Who
- route controllers
- lane workers
- failure/repair actors

## What

Active run state for one coding attempt or route.

## Why

The lane needs bounded hot state for what is currently being worked.

## Where

- Path: `systems/coding-foundry/subsystems/working-memory`
- Kind: `child-subsystem`
- Status: `bounded`
- Parent: `coding-foundry`
- Depends on: `coding-foundry/packets`
- Allowed dependencies: `coding-foundry/packets, coding-foundry/deterministic-truth, coding-foundry/model-species`
- Child subsystems: `none`

## How

- Canonical schema: [FOUNDRY_SCHEMA.md](../../../../docs/schemas/FOUNDRY_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when active run state, ambiguity handling, or route-state shape changes.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [FOUNDRY_SCHEMA.md](../../../../docs/schemas/FOUNDRY_SCHEMA.md)
