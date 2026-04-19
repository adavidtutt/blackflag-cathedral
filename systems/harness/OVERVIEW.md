---
title: harness Overview
status: frozen
tags:
  - subsystem
  - overview
  - harness
  - top-level-subsystem
  - frozen
---

# harness Overview

## Who
- control-plane engineers
- backend mediators
- sandbox operators

## What

Rust control-plane harness for the coding lane.

## Why

The harness is the operational spine that runs the coding lane safely and economically.

## Where

- Path: `systems/harness`
- Kind: `top-level-subsystem`
- Status: `frozen`
- Parent: `none`
- Depends on: `coding-foundry`
- Allowed dependencies: `coding-foundry`
- Child subsystems: `harness/gateway, harness/scheduler, harness/broker, harness/sandbox-runner, harness/artifact-store, harness/telemetry, harness/runtime-planes`

## How

- Canonical schema: [HARNESS_SCHEMA.md](../../docs/schemas/HARNESS_SCHEMA.md)
- Local readme: [README.md](README.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
- Contracts surface: [contracts](contracts/README.md)
- Tests surface: [tests](tests/README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when the harness service set, boundaries, or control-plane assumptions change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [HARNESS_SCHEMA.md](../../docs/schemas/HARNESS_SCHEMA.md)
- Local schema surface: [SCHEMA.md](SCHEMA.md)
