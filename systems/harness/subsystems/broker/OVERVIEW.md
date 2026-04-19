---
title: harness/broker Overview
status: frozen
tags:
  - subsystem
  - overview
  - harness
  - child-subsystem
  - frozen
  - harness-broker
  - broker
---

# harness/broker Overview

## Who
- backend mediators
- serving integrators
- response normalizers

## What

Backend invocation mediation boundary for model-serving calls.

## Why

The broker isolates backend-specific semantics from the rest of the harness.

## Where

- Path: `systems/harness/subsystems/broker`
- Kind: `child-subsystem`
- Status: `frozen`
- Parent: `harness`
- Depends on: `none`
- Allowed dependencies: `harness/sandbox-runner, harness/artifact-store`
- Child subsystems: `none`

## How

- Canonical schema: [HARNESS_SCHEMA.md](../../../../docs/schemas/HARNESS_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when backend mediation, invocation envelopes, or large-payload rules change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [HARNESS_SCHEMA.md](../../../../docs/schemas/HARNESS_SCHEMA.md)
