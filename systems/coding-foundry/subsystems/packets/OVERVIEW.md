---
title: coding-foundry/packets Overview
status: frozen
tags:
  - subsystem
  - overview
  - coding-foundry
  - child-subsystem
  - frozen
  - coding-foundry-packets
  - packets
---

# coding-foundry/packets Overview

## Who
- packet builders
- route controllers
- validation and merge actors

## What

Canonical packet family and packet-boundary discipline for coding work.

## Why

The coding lane must move through typed packets rather than prompt sludge.

## Where

- Path: `systems/coding-foundry/subsystems/packets`
- Kind: `child-subsystem`
- Status: `frozen`
- Parent: `coding-foundry`
- Depends on: `none`
- Allowed dependencies: `coding-foundry/deterministic-truth, coding-foundry/working-memory`
- Child subsystems: `none`

## How

- Canonical schema: [FOUNDRY_SCHEMA.md](../../../../docs/schemas/FOUNDRY_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when packet families, packet invariants, or packet lineage rules change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [FOUNDRY_SCHEMA.md](../../../../docs/schemas/FOUNDRY_SCHEMA.md)
