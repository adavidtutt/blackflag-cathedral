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

Use `../scripts/validate_subsystems.py` to validate the subsystem graph.

