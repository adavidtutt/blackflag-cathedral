---
title: Coding Foundry Schema
status: frozen
authority: thread-frozen
tags:
  - coding-foundry
  - cathedral-compatible
  - coding-lane
  - packets
  - working-memory
  - deterministic-truth
  - parameter-lineage
  - model-species
---

# Coding Foundry Schema

## Status

`frozen`

The Coding Foundry is a Cathedral-compatible coding lane. It is not the full Cathedral.

## Scope

The Coding Foundry exists to:
- generate code artifacts
- test and validate them
- repair failures
- assemble mergeable outputs
- emit traces and lineage that later integrate into the Cathedral

## Species Mapping

### Scouts

- repo scout
- symbol scout
- test scout
- traceback scout
- dependency scout
- patch-history scout
- validator-history scout
- checkpoint scout

### Judges

- evidence relevance judge
- deterministic sufficiency judge
- route necessity judge
- patch-risk judge

### Packet Builders

These assemble typed evidence packets rather than raw prompt sludge.

### Route Controllers

These decide lane routing, escalation, and packet-to-role assembly.

### Synthesis Models

- scaffolder
- logic worker
- tester
- documenter
- fixer
- manager
- architect

### Critics

- linter/security
- validator arbitration
- unsupported-claim checker
- merge critic

### Consolidators

Initially these may be procedural rather than model-heavy.

## Memory Mapping

### Symbol Memory

- prompts
- token traces
- code spans
- patch fragments
- failure motifs

### Semantic Memory

- API contract
- migration
- retry policy
- auth boundary
- serialization
- async correctness

### Relational Memory

- file imports file
- test covers function
- patch touches file
- error caused by dependency
- module belongs to service
- change contradicts contract
- fix derived from traceback

### Deterministic Memory

Exact coding facts in durable stores:
- jobs
- files
- hashes
- tests
- dependencies
- validators
- checkpoints

### Episodic Memory

- prior runs
- routes
- patches
- failures
- validations
- escalations

### Parameter Memory

- base trunks
- role checkpoints
- runtime variants
- lineage metadata

### Working Memory

- current objective
- active packets
- active repo slice
- current patch stack
- unresolved ambiguities
- active route plan

## Packet Family

Canonical packet family:
- `RepoPacket`
- `TaskPacket`
- `FailurePacket`
- `PatchPacket`
- `ValidationPacket`
- `MergePacket`

These are the canonical coding-lane packets. Their detailed field surfaces are governed by the reconciled packet spec.

## Packet Invariants

- explicit repository anchoring
- explicit task scope and exclusions
- explicit base revision anchoring
- patch lineage
- validation basis revision anchoring
- merge disposition as a typed state
- explicit supersession chains
- artifact references separated from large payload custody

## Deterministic Truth Domains

Current exact domains:
- repositories
- commits
- files
- symbols
- jobs
- job_edges
- patches
- validation_runs
- tests
- dependencies
- role_runs
- checkpoint_registry
- runtime_variants
- route_outcomes

Detailed deterministic-truth schema remains bounded, not fully frozen.

## Working Memory Fields

Current bounded fields:
- objective
- active_task_ids
- active_packet_ids
- active_repo_slice
- open_ambiguities
- pending_validators
- current_route_plan
- current_patch_stack
- escalation_state

Detailed working-memory schema remains bounded, not fully frozen.

## Parameter Lineage

Every checkpoint and runtime artifact must emit lineage metadata sufficient for later ingestion into the Cathedral parameter graph.

Core required fields:
- `parameter_artifact_id`
- `lineage_record_id`
- `artifact_class`
- `model_family_ref`
- `role_ref`
- `creation_event_ref`
- `parent_artifact_refs`
- `derivation_kind`
- `parameter_state_fingerprint`
- `architecture_compatibility_ref`
- `tensor_manifest_ref`
- `storage_artifact_ref`
- `validity_status`
- `supersedes_artifact_refs`
- `provenance_chain_ref`

## Promotion Hooks

Current bounded, not yet fully frozen:
- route outcomes
- validator outcomes
- patch success/failure
- evidence packet usefulness
- role latency/cost metrics
- recurring failure families
- recurring repair motifs
- route-win clusters
- checkpoint supersession proposals

## What This Does Not Change

- The Coding Foundry is not promoted to the final system.
- Packet-based execution is not replaced with prompt chaining.
- This file does not fully freeze deterministic-truth or working-memory detail yet.

