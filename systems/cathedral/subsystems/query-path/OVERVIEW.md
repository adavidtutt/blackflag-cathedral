---
title: cathedral/query-path Overview
status: frozen
tags:
  - subsystem
  - overview
  - cathedral
  - child-subsystem
  - frozen
  - cathedral-query-path
  - query-path
---

# cathedral/query-path Overview

## Who
- route designers
- packet designers
- execution planners

## What

Canonical staged query path for the Cathedral.

## Why

The system must move through staged retrieval, shaping, synthesis, and critique rather than one-pass guessing.

## Where

- Path: `systems/cathedral/subsystems/query-path`
- Kind: `child-subsystem`
- Status: `frozen`
- Parent: `cathedral`
- Depends on: `none`
- Allowed dependencies: `cathedral/models, cathedral/graphs, cathedral/deterministic-truth`
- Child subsystems: `none`

## How

- Canonical schema: [CATHEDRAL_SCHEMA.md](../../../../docs/schemas/CATHEDRAL_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when the end-to-end query stages or their boundaries change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [CATHEDRAL_SCHEMA.md](../../../../docs/schemas/CATHEDRAL_SCHEMA.md)
