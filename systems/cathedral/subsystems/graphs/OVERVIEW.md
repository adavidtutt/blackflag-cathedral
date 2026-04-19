---
title: cathedral/graphs Overview
status: frozen
tags:
  - subsystem
  - overview
  - cathedral
  - child-subsystem
  - frozen
  - cathedral-graphs
  - graphs
---

# cathedral/graphs Overview

## Who
- graph designers
- knowledge-layer builders
- parameter-graph consumers

## What

Layered graph hierarchy for the Cathedral.

## Why

The system needs multiple graph layers because one graph is not enough.

## Where

- Path: `systems/cathedral/subsystems/graphs`
- Kind: `child-subsystem`
- Status: `frozen`
- Parent: `cathedral`
- Depends on: `none`
- Allowed dependencies: `cathedral/memory, cathedral/models`
- Child subsystems: `none`

## How

- Canonical schema: [CATHEDRAL_SCHEMA.md](../../../../docs/schemas/CATHEDRAL_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when graph layers, graph boundaries, or graph-to-memory relationships change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [CATHEDRAL_SCHEMA.md](../../../../docs/schemas/CATHEDRAL_SCHEMA.md)
