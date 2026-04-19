---
title: Subsystems
status: wiki
tags:
  - wiki
  - subsystems
  - modularity
  - manifests
  - validation
---

# Subsystems

The repo now has a true subsystem graph under `systems/`.

Top-level subsystems:
- `cathedral`
- `coding-foundry`
- `harness`
- `training`
- `visual-implementation`

Each top-level subsystem has:
- a manifest
- a local overview
- a schema surface
- contracts and tests surfaces
- its own child subsystem registry

For canonical detail, see:
- [../../systems/README.md](../../systems/README.md)
- [../../systems/REGISTRY.yaml](../../systems/REGISTRY.yaml)
- [../../meta/exports/subsystem_human_index.md](../../meta/exports/subsystem_human_index.md)

For local explanation, open the `OVERVIEW.md` inside any subsystem directory. Every subsystem and child subsystem now has one.
