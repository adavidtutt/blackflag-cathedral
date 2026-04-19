---
title: coding-foundry/deterministic-truth Overview
status: bounded
tags:
  - subsystem
  - overview
  - coding-foundry
  - child-subsystem
  - bounded
  - coding-foundry-deterministic-truth
  - deterministic-truth
---

# coding-foundry/deterministic-truth Overview

## Who
- coding truth-plane designers
- repo-fact designers
- validator designers

## What

Exact coding-fact domains and boundaries for the Foundry.

## Why

The coding lane must not ask models to hallucinate exact repo facts that can be stored exactly.

## Where

- Path: `systems/coding-foundry/subsystems/deterministic-truth`
- Kind: `child-subsystem`
- Status: `bounded`
- Parent: `coding-foundry`
- Depends on: `cathedral/deterministic-truth`
- Allowed dependencies: `cathedral/deterministic-truth, coding-foundry/packets, coding-foundry/working-memory`
- Child subsystems: `none`

## How

- Canonical schema: [FOUNDRY_SCHEMA.md](../../../../docs/schemas/FOUNDRY_SCHEMA.md)
- Local readme: [README.md](README.md)
- Validator: `python3 scripts/validate_subsystems.py`

## When

Touch this when deterministic coding domains, keys, or exact-fact ownership changes.

## Truth Surfaces

- Manifest: [manifest.yaml](manifest.yaml)
- Canonical schema: [FOUNDRY_SCHEMA.md](../../../../docs/schemas/FOUNDRY_SCHEMA.md)
