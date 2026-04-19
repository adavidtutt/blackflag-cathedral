---
title: harness/telemetry Overview
status: frozen
tags:
  - subsystem
  - overview
  - harness
  - child-subsystem
  - frozen
  - harness-telemetry
  - telemetry
---

# harness/telemetry Overview

## Who
- operators
- debuggers
- performance observers

## What

Observability boundary for logs, traces, and metrics.

## Why

Observability must exist without becoming the hidden workflow authority.

## Where

- Path: `systems/harness/subsystems/telemetry`
- Kind: `child-subsystem`
- Status: `frozen`
- Parent: `harness`
- Depends on: `none`
- Allowed dependencies: `none`
- Child subsystems: `none`

## How

- Canonical schema: [HARNESS_SCHEMA.md](../../../../docs/schemas/HARNESS_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when telemetry surfaces, trace shape, or operational visibility changes.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [HARNESS_SCHEMA.md](../../../../docs/schemas/HARNESS_SCHEMA.md)
