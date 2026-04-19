---
title: harness/artifact-store Overview
status: frozen
tags:
  - subsystem
  - overview
  - harness
  - child-subsystem
  - frozen
  - harness-artifact-store
  - artifact-store
---

# harness/artifact-store Overview

## Who
- artifact registries
- storage maintainers
- retrieval users

## What

Durable custody layer for artifacts and retrieval handles.

## Why

Artifacts need durable, content-addressable custody separate from workflow logic.

## Where

- Path: `systems/harness/subsystems/artifact-store`
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

Touch this when artifact persistence, manifests, or retrieval surfaces change.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [HARNESS_SCHEMA.md](../../../../docs/schemas/HARNESS_SCHEMA.md)
