---
title: Black Flag Cathedral Schema Corpus
status: bounded
authority: canonical-index
tags:
  - cathedral
  - coding-foundry
  - architecture
  - schema
  - training
  - harness
  - structural-ir
  - deterministic-truth
  - parameter-lineage
  - wiki
  - github
---

# Black Flag Cathedral Schema Corpus

This repository is the running architecture ledger for the Cathedral project family.

It is designed to do four jobs at once:
- preserve canonical truth from the working thread
- prevent context drift across long design cycles
- provide human-readable architecture documentation
- support wiki-style browsing and GitHub publishing

## Canonical Entry Points

- [RUNNING_SCHEMA.md](./RUNNING_SCHEMA.md)
- [docs/INDEX.md](./docs/INDEX.md)
- [docs/schemas/CATHEDRAL_SCHEMA.md](./docs/schemas/CATHEDRAL_SCHEMA.md)
- [docs/schemas/FOUNDRY_SCHEMA.md](./docs/schemas/FOUNDRY_SCHEMA.md)
- [docs/schemas/TRAINING_SCHEMA.md](./docs/schemas/TRAINING_SCHEMA.md)
- [docs/schemas/HARNESS_SCHEMA.md](./docs/schemas/HARNESS_SCHEMA.md)
- [docs/schemas/STRUCTURAL_COMPILER_SCHEMA.md](./docs/schemas/STRUCTURAL_COMPILER_SCHEMA.md)
- [docs/schemas/VISUAL_IMPLEMENTATION_SCHEMA.md](./docs/schemas/VISUAL_IMPLEMENTATION_SCHEMA.md)
- [docs/reconciliations/OUTSIDE_CHAT_RECONCILIATIONS.md](./docs/reconciliations/OUTSIDE_CHAT_RECONCILIATIONS.md)
- [docs/reconciliations/THREAD_TRUTH_CHECKLIST.md](./docs/reconciliations/THREAD_TRUTH_CHECKLIST.md)

## Authority Order

When conflicts appear, use this precedence:

1. Direct user truth in the source thread
2. Explicitly frozen decisions acknowledged in the source thread
3. Reconciled outside-chat outputs accepted in the source thread
4. Provisional notes and local expansions

If a future note is not reflected in the canonical schema corpus, it is not authoritative.

## Human-Readable Surfaces

For narrative browsing:
- [docs/wiki/Home.md](./docs/wiki/Home.md)
- [docs/wiki/_Sidebar.md](./docs/wiki/_Sidebar.md)

For machine-readable summaries:
- [running_schema.yaml](./running_schema.yaml)
- [meta/tags/tag_index.yaml](./meta/tags/tag_index.yaml)
- [meta/exports/wiki_manifest.yaml](./meta/exports/wiki_manifest.yaml)

## Update Rule

Every material architectural change should:

1. update `RUNNING_SCHEMA.md`
2. update `running_schema.yaml` if canonical entities or schema surfaces changed
3. update the relevant deep schema file under `docs/schemas/`
4. update reconciliation files if the change came from outside-chat analysis
5. preserve explicit status markers: `frozen`, `bounded`, or `provisional`

## Scope

This repo does **not** claim that the Coding Foundry is the final system.

The final system is **The Cathedral**.

The Coding Foundry is a bounded, Cathedral-compatible coding lane that:
- helps build the larger system
- later lives inside the larger system
- preserves structural compatibility with Cathedral principles
