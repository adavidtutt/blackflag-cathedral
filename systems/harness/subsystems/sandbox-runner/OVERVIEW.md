---
title: harness/sandbox-runner Overview
status: frozen
tags:
  - subsystem
  - overview
  - harness
  - child-subsystem
  - frozen
  - harness-sandbox-runner
  - sandbox-runner
---

# harness/sandbox-runner Overview

## Who
- tool runners
- workspace executors
- process isolation maintainers

## What

Isolated process and workspace execution boundary.

## Why

The harness needs a clean boundary for code execution and tool runs.

## Where

- Path: `systems/harness/subsystems/sandbox-runner`
- Kind: `child-subsystem`
- Status: `frozen`
- Parent: `harness`
- Depends on: `none`
- Allowed dependencies: `harness/artifact-store, harness/telemetry`
- Child subsystems: `none`

## How

- Canonical schema: [HARNESS_SCHEMA.md](../../../../docs/schemas/HARNESS_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when sandbox execution rules, isolation, or workspace lifecycle changes.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [HARNESS_SCHEMA.md](../../../../docs/schemas/HARNESS_SCHEMA.md)
