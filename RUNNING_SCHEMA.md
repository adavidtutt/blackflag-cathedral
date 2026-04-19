---
title: Running Schema
status: bounded
authority: canonical-ledger
tags:
  - running-schema
  - canonical
  - cathedral
  - coding-foundry
  - architecture
  - frozen
  - bounded
  - reconciliation
  - training
  - harness
  - structural-ir
  - parameter-lineage
---

# Running Schema

This file is the canonical running schema ledger for the Cathedral project family.

It exists to prevent drift across:
- live conversation context
- frozen architectural decisions
- reconciled outside-chat results
- future subsystem additions

## Authority Order

When conflicts appear, use this precedence:

1. Direct user truth in this thread
2. Explicitly frozen decisions acknowledged in this thread
3. Reconciled outside-chat outputs that were accepted here
4. Working notes and provisional drafts

Nothing below is allowed to silently override anything above it.

## Update Rule

Every material architectural change should do all of the following:

1. Update this file
2. Update `running_schema.yaml` if the change affects canonical entities or schema surfaces
3. Mark the changed section as either `frozen`, `bounded`, or `provisional`
4. Record what the change does not alter

If a future note is not reflected here, it is not canonical.

## Current State

Status: `bounded`
Scope: `Cathedral-adjacent architecture and Coding Foundry subsystem`

## Core Truth

The final system is **The Cathedral**.

The earlier multi-model coding architecture is **not** the final system. It is a bounded subsystem, referred to here as the **Coding Foundry**, that will:
- help build the larger system
- later live inside the larger system
- remain compatible with Cathedral principles rather than forcing the Cathedral to inherit accidental design shortcuts

The Cathedral treats intelligence as distributed across:
- static trunk weights
- hot-swappable adapters and deltas
- graph structure
- deterministic stores
- caches
- recurrent or working state
- retrieval
- routing
- consolidation over time

It does not assume intelligence lives mainly in one dense parameter blob.

## Cathedral Principles

Status: `frozen`

The Cathedral is organized around these principles:

- Memory is split into species rather than treated as one thing.
- Graphs are layered rather than collapsed into one graph.
- Models form a society of specialized species rather than one top model with tools.
- Exact truth should live in deterministic systems whenever possible.
- Query handling is staged:
  - preclassification
  - distributed scouting
  - packet shaping
  - execution assembly
  - synthesis
  - critique
  - answer plus memory write
- Learning occurs at multiple speeds:
  - immediate writes
  - session-level promotion
  - medium-loop adaptation
  - slow-loop consolidation

## Memory Species

Status: `frozen`

- Symbol memory
- Semantic memory
- Relational memory
- Deterministic memory
- Episodic memory
- Parameter memory
- Working memory

## Graph Hierarchy

Status: `frozen`

- Token graph
- Span graph
- Entity graph
- Concept graph
- Epistemic graph
- Parameter graph

## Model Species

Status: `frozen`

- Lane scouts
- Lane judges
- Packet builders
- Route controllers
- Synthesis models
- Critic models
- Consolidation models

## Coding Foundry

Status: `frozen`
Role: `Cathedral-compatible coding lane`

The Coding Foundry is a bounded subsystem responsible for:
- generating code artifacts
- testing and validating them
- repairing failures
- assembling mergeable outputs
- emitting traces and lineage that can later integrate into the Cathedral

It is not the full Cathedral.

### Coding Foundry Memory Mapping

Status: `frozen`

- Symbol memory: prompts, token traces, code spans, patch fragments, failure motifs
- Semantic memory: coding concepts such as contracts, migrations, retries, auth boundaries
- Relational memory: imports, test coverage relations, patch touches, error causality
- Deterministic memory: exact rows for jobs, files, hashes, tests, dependencies, validators, checkpoints
- Episodic memory: prior runs, routes, patches, failures, validations, escalations
- Parameter memory: trunks, role checkpoints, runtime variants, lineage metadata
- Working memory: current objective, active packets, repo slice, patch stack, unresolved ambiguities, route plan

### Coding Foundry Graph Mapping

Status: `frozen`

- Token graph for code-token and failure-token motifs
- Span graph for functions, classes, config blocks, traces, diffs
- Entity graph for repos, files, symbols, validators, roles, checkpoints
- Concept graph for software-engineering abstractions
- Epistemic graph for support, contradiction, inference, unresolved state
- Parameter graph for checkpoint and runtime-artifact lineage

### Coding Foundry Model Species Mapping

Status: `frozen`

- Scouts:
  - repo scout
  - symbol scout
  - test scout
  - traceback scout
  - dependency scout
  - patch-history scout
  - validator-history scout
  - checkpoint scout
- Judges:
  - evidence relevance judge
  - deterministic sufficiency judge
  - route necessity judge
  - patch-risk judge
- Packet builders
- Route controllers
- Synthesis models:
  - scaffolder
  - logic worker
  - tester
  - documenter
  - fixer
  - manager
  - architect
- Critics:
  - linter/security
  - validator arbitration
  - unsupported-claim checker
  - merge critic
- Consolidation models:
  - initially can be procedural rather than model-heavy

## Frozen Harness Architecture

Status: `frozen`

The current harness baseline is:
- Rust control plane
- `vLLM` as primary serving backend
- hot / warm / cold runtime planes
- NATS JetStream
- Postgres
- sandbox runner
- strict JSON role contracts
- packet-based orchestration
- deterministic truth as a first-class design rule
- compression as a configurable serving-layer interface

### Harness Services

Status: `frozen`

- gateway
- scheduler
- broker
- sandbox-runner
- artifact-store
- telemetry

### Harness Service Boundary Rule

Status: `frozen`

Service boundaries follow the reconciled external result:
- ChatGPT 5.4 service-boundary answer is the canonical base
- plus one merged rule from Gemini:
  - large blobs must not travel through the broker
  - use artifact references or URIs instead

## Structural Compiler Track

Status: `bounded`

This is adjacent to, but distinct from, the Coding Foundry.

Purpose:
- visual-first structural authoring
- compile to semantic or structural IR
- generate downstream projections

Relationship to main system:
- this track helps describe and manage the Coding Foundry
- later it helps describe and manage broader Cathedral subsystems

### Structural Authoring Truth

Status: `frozen`

The visual system is allowed to be a truth-bearing authoring surface.

The correct shape is:
- visual schematic or harness authoring
- bound subdocumentation attached to authored structures
- intermediate representation compiled from that authoring truth
- compiled projections downstream

Python and Rust are downstream targets of the same canonical IR, not parents of each other.

## Visual To Implementation System

Status: `frozen`

The visual-to-implementation tangent is now treated as a first-class architectural subsystem.

Core rules:
- the system must be buildable visually at depth
- the visual artifact is required for human topology thinking
- the visual system plus its bound subdocumentation can change truth
- the correct path is:
  - visual schematic or harness authoring
  - bound subdocumentation
  - canonical IR
  - compiled projections

Further rules:
- layout is not logic
- the compiler should consume symbols, IDs, ports, boundaries, and typed relations rather than pixels
- Python and Rust are sibling targets of the same IR
- generated structure should prefer owned zones over mutating arbitrary handwritten code
- GUI/control surfaces are compiled views of the same canonical model
- the system should preserve at least:
  - topology graph
  - semantic or relation graph

Canonical detail lives in:
- `docs/schemas/VISUAL_IMPLEMENTATION_SCHEMA.md`

## Structural IR Boundary

Status: `frozen`
Canonical source: `outside-chat reconciliation -> ChatGPT 5.4`

The structural IR must include:
- stable identity and addressability
- node kinds and structural roles
- containment and composition
- ports, interfaces, and connection topology
- explicit boundary declarations
- structural contracts and compatibility constraints
- typed interface-level artifacts where needed for composition
- instantiation and reuse semantics
- minimal projection metadata needed for downstream generation
- source mapping and provenance
- structural validation markers
- disciplined extension points

The structural IR must not include:
- executable logic
- target-language idioms
- UI-only drawing trivia
- runtime state
- optimization policy
- human-process prose as authority
- environment-specific deployment facts
- domain behavior disguised as structure

## Coding Foundry Packet Family

Status: `frozen`
Canonical source: `outside-chat reconciliation -> ChatGPT 5.4`

Canonical packet family:
- RepoPacket
- TaskPacket
- FailurePacket
- PatchPacket
- ValidationPacket
- MergePacket

Important packet requirements:
- explicit repository anchoring
- explicit task scope and out-of-scope boundaries
- explicit base revision anchoring
- patch lineage via parent refs where needed
- validation basis revision anchoring
- merge disposition as a typed outcome
- explicit supersession chains
- artifact refs separated from packet bodies

## Deterministic Truth

Status: `bounded`

The Coding Foundry must preserve deterministic truth for exact coding facts.

Current canonical deterministic domains:
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

Detailed deterministic-truth schema is not yet frozen in this file.

## Working Memory

Status: `bounded`

Each active coding run should maintain a bounded working-memory object containing:
- current objective
- active task ids
- active packet ids
- active repo slice
- open ambiguities
- pending validators
- current route plan
- current patch stack
- escalation state

Detailed working-memory schema is not yet frozen in this file.

## Parameter Lineage

Status: `frozen`
Canonical source: `outside-chat reconciliation -> ChatGPT 5.4`

Every checkpoint and runtime artifact should carry lineage metadata sufficient for the future Cathedral parameter graph.

Core required lineage fields include:
- parameter artifact identity
- lineage record identity
- artifact class
- model family reference
- role reference
- creation event reference
- parent artifact references
- derivation kind
- parameter-state fingerprint
- architecture compatibility reference
- tensor manifest reference
- storage artifact reference
- validity status
- supersession references
- provenance chain reference

## Training Roles

Status: `frozen`

Each original role requires its own custom training job.

Do not collapse role checkpoints into fewer models for the purposes of the frozen training plan.

Current role family:
- Router: Dolphin 2.9.3 Qwen2 0.5B
- Six coding workers: Dolphin 3.0 Qwen2.5 3B
- Manager: Dolphin 3.0 Qwen2.5 32B
- Architect: Dolphin 3.0 Qwen2.5 72B

## Hardware Policy

Status: `frozen`
Canonical source: `outside-chat reconciliation -> ChatGPT 5.4`

Hardware policy principle:
- choose the cheapest acceptable hardware class for each role
- do not sacrifice planned quality to fit cheaper hardware
- independent jobs may run on arbitrary hosts
- one training job should stay on one host or a tightly coupled machine

Escalation should be triggered by:
- memory fit failure
- quality-preservation failure
- cost crossover
- interconnect bottleneck
- reliability failure

## Outside-Chat Reconciliation Rule

Status: `frozen`

For bounded external deep-thinking prompts:
- ChatGPT 5.4 is the primary external reference
- Gemini is secondary and useful for contradiction checking or simplification
- Grok is not a trusted source for core architectural decisions unless the question is trivial and narrow

## Open Items

Status: `bounded`

Not yet frozen here:
- detailed deterministic-truth schema
- detailed working-memory schema
- promotion and consolidation hook schema
- structural IR to packet-boundary mapping
- visual harness authoring grammar to IR mapping

## Non-Changes

Status: `frozen`

This ledger does not:
- redesign the Cathedral
- collapse the Coding Foundry into a simple agent toolchain
- replace packet-based orchestration with prompt chaining
- move source of truth from IR back into Python or Rust
- make the Coding Foundry the final system
