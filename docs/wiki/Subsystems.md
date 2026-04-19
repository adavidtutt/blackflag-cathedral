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
- a schema surface
- contracts and tests surfaces
- its own child subsystem registry

For canonical detail, see:
- [../../systems/README.md](../../systems/README.md)
- [../../systems/REGISTRY.yaml](../../systems/REGISTRY.yaml)
