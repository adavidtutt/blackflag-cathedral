---
title: harness/gateway Overview
status: frozen
tags:
  - subsystem
  - overview
  - harness
  - child-subsystem
  - frozen
  - harness-gateway
  - gateway
---

# harness/gateway Overview

## Who
- external callers
- admission logic
- API boundary maintainers

## What

Ingress and egress boundary for the harness.

## Why

The gateway owns client-facing admission and should stay separate from scheduling and execution.

## Where

- Path: `systems/harness/subsystems/gateway`
- Kind: `child-subsystem`
- Status: `frozen`
- Parent: `harness`
- Depends on: `none`
- Allowed dependencies: `harness/scheduler`
- Child subsystems: `none`

## How

- Canonical schema: [HARNESS_SCHEMA.md](../../../../docs/schemas/HARNESS_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when ingress contracts, admission checks, or outward API shaping changes.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [HARNESS_SCHEMA.md](../../../../docs/schemas/HARNESS_SCHEMA.md)
