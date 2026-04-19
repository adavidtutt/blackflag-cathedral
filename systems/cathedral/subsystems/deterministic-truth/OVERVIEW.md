---
title: cathedral/deterministic-truth Overview
status: bounded
tags:
  - subsystem
  - overview
  - cathedral
  - child-subsystem
  - bounded
  - cathedral-deterministic-truth
  - deterministic-truth
---

# cathedral/deterministic-truth Overview

## Who
- truth-plane designers
- fact-store designers
- validation designers

## What

Exact-truth doctrine for the Cathedral.

## Why

Exact truth should live in exact systems whenever possible.

## Where

- Path: `systems/cathedral/subsystems/deterministic-truth`
- Kind: `child-subsystem`
- Status: `bounded`
- Parent: `cathedral`
- Depends on: `none`
- Allowed dependencies: `cathedral/memory, cathedral/query-path`
- Child subsystems: `none`

## How

- Canonical schema: [CATHEDRAL_SCHEMA.md](../../../../docs/schemas/CATHEDRAL_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when deterministic truth boundaries or exact-store responsibilities change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [CATHEDRAL_SCHEMA.md](../../../../docs/schemas/CATHEDRAL_SCHEMA.md)
