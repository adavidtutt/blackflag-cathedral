---
title: Subsystem Layout
status: canonical
authority: modular-structure
tags:
  - systems
  - modularity
  - subsystem-graph
  - manifests
  - validation
---

# Subsystem Layout

This directory is the modular execution and ownership layout for the schema corpus.

Each top-level subsystem has:
- `README.md`
- `OVERVIEW.md`
- `SCHEMA.md`
- `manifest.yaml`
- `contracts/`
- `tests/`
- `subsystems/`

Each subsystem may own child subsystems recursively through its local `subsystems/REGISTRY.yaml`.

The goal is simple:
- work one subsystem at a time
- preserve clean boundaries
- keep dependencies explicit
- allow each subsystem to grow its own internal structure without flattening the whole repo

Human-readable navigation surfaces:
- `../meta/exports/subsystem_human_index.md`
- each subsystem-local `OVERVIEW.md`

Use:
- `python3 ../scripts/sync_subsystem_surfaces.py` to regenerate the human-readable subsystem surfaces
- `python3 ../scripts/validate_subsystems.py` to validate the subsystem graph
