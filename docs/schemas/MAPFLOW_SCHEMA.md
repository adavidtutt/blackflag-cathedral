---
title: MapFlow Schema
status: bounded
authority: direct-user-architecture
tags:
  - cathedral
  - fractal-cognitive-substrate
  - mapflow
  - dsl
  - compiler
  - lowering
  - kernels
  - runtime
---

# MapFlow Schema

## Status

`bounded`

MapFlow is the current maximalist-alpha cognitive systems DSL and compiler stack for the Fractal Cognitive Substrate.

## Purpose

MapFlow exists to express nodes, routes, confidence, lineage, staging, hydration, and parameter compilation as substrate-native semantics, then lower only regular dense work into fast GPU kernels.

## Design Goal

Primary goal:
- express the map as the primary intelligence substrate while keeping the hot execution path compatible with fast existing GPU execution models

Non-goals:
- do not replace CUDA as a hardware language
- do not force meaning itself into GPU kernels
- do not make raw transformer ontology the final ontology
- do not allow arbitrary graph wandering in the hot path

## Grounding

Execution foundations:
- CUDA kernel model
- CUDA memory hierarchy
- Triton blocked program model
- MLIR-style progressive lowering
- KV-page runtime patterns

Rationale:
- CUDA is the right lower bound for dense hot-path execution because it exposes kernels and memory spaces directly.
- Triton is the fast iteration surface for blocked dense kernels.
- MLIR-style thinking fits dialects, legality, and progressive lowering.
- KV-page runtime patterns match route-sketch paging, prefetch, and continuous batching.

## Worldview

Core claim:
- the map is the persistent cognitive topology
- the embedded LLM is a subordinate organ for language, ambiguity resolution, abstraction, and creative synthesis

Architectural split:
- deterministic layer: truth, lineage, refutation, exact retrieval, symbolic joins
- probabilistic layer: language, abstraction, novelty, ambiguity resolution
- compiler layer: map rewriting, summary generation, route prior updates, compaction

## Language Shape

Category:
- declarative plus execution-aware DSL

Authoring requirements:
- human-readable
- machine-readable
- schedulable
- lowerable

Philosophy:
- one node shell
- one small verb set
- many payload classes
- strict traversal budgets
- hot path must be pageable
- everything important leaves exhaust
- exhaust must compile downward into denser structure

## Root Concepts

- `artifact`: any addressable thing in the system
- `node`: universal shell placed around an artifact
- `payload`: typed material behind a node
- `contract`: stable executable law around a node
- `route_sketch`: compressed hot routing surface
- `page`: hydratable warm or hot execution unit
- `snapshot`: time-bound captured state
- `parameter_artifact`: compiled executable region synthesized from model behavior or promoted structure
- `exhaust`: reusable byproduct of execution
- `hydration`: turning compact route decisions into execution-ready pages

## Node Contract Alignment

MapFlow node declarations must preserve canonical FCS node law.

Canonical fields:
- `id`
- `kind`
- `payload_ref`
- `state`
- `lineage`
- `links`
- `summary`
- `stats`

Optional fields:
- `route_signature`
- `trust_vector`
- `page_manifest`
- `expansion_recipe`
- `execution_hooks`
- `permissions`
- `compression_class`

## Types

Primitive scalar families:
- bool
- signed and unsigned integers from 8 to 64 bit
- `f16`, `bf16`, `f32`, `f64`

Identity families:
- `id64` for local handles only
- `id128` for compact preferred identity handles
- `id256` for full content identity when needed

Structural families:
- `ref`
- `range`
- `tuple`
- `vec[dtype, length]`
- `page_ref`
- `manifest_ref`
- `recipe_ref`
- `lineage_ref`
- `summary_ref`

Map-specific families:
- `route_code`
- `trust_vec`
- `stats`
- `edge`
- `edge_set`
- `state`

## Truth And Confidence

Truth-state enum:
- asserted
- supported
- provisional
- conflicting
- falsified
- superseded
- unresolved

Confidence-band enum:
- low
- medium
- high
- near_certain

Trust-vector layout:
- source confidence
- structural confidence
- cross-source agreement
- recency
- replay consistency
- task contribution
- human reviewed
- contradiction pressure

## Memory Model

Spaces:
- `cold_archive`: raw truth, large objects, lineage-complete history
- `warm_hydration`: operational pages, summaries, route tables, replay capsules
- `hot_route`: route sketch and active decision surface
- `hot_exec`: execution-ready pages and dense active compute

Residency classes:
- cold_only
- warm_resident
- hot_route_resident
- hot_exec_resident
- speculative_resident

Memory law:
- hot holds direction
- warm holds readiness
- cold holds truth

## Page Model

The hot path should operate on page-like units rather than arbitrary graph objects.

Page kinds:
- route_page
- summary_page
- evidence_page
- param_page
- context_page

Page header fields:
- `page_id`
- `page_kind`
- `codec`
- `version`
- `source_space`
- `byte_length`
- `logical_shape`
- `trust_band`
- `staleness_class`

Page footer fields:
- `checksum`
- `lineage_ref`
- `manifest_ref`

## KV Projection

Goal:
- compile the active map frontier into a KV-shaped execution form

Key contents:
- route signature
- node-kind bits
- confidence band
- neighborhood key
- time or context key

Value contents:
- payload ref
- page ref
- summary ref
- lineage ref
- permissions
- expansion recipe

Rules:
- hashes alone are insufficient for hot routing
- exact identity must remain separable from lossy route geometry
- only the active frontier lowers to hot KV pages

## Surface Syntax

MapFlow uses block-based declarative syntax with explicit operations.

Top-level constructs:
- `node`
- `payload`
- `route`
- `policy`
- `stage`
- `hydrate`
- `promote`
- `refute`
- `compile`
- `kernel`

Example node declaration:

```text
node user_fact_001:
  kind: belief
  payload_ref: ref("warm://beliefs/fact_001")
  state:
    truth_state: supported
    confidence_band: high
  summary: "user prefers route-first deterministic answers"
```

Example route declaration:

```text
route answer_path:
  from: discourse.current
  via:
    - semantic.neighborhood(top_k=8)
    - deterministic.known_facts(top_k=16)
    - context.replay(recent=4)
  budget:
    max_expansions: 32
    max_payload_pages: 8
```

Example policy declaration:

```text
policy promotion:
  if:
    source_confidence >= 0.95
    and cross_source_agreement >= 0.90
    and contradiction_pressure <= 0.10
  then:
    promote(to="supported")
```

Surface syntax is for authoring; runtime executes lowered IR.

## Grammar Outline

Module contents:
- imports
- type definitions
- node definitions
- route definitions
- policy definitions
- lowering hints
- kernel definitions

Node definitions require:
- name
- kind
- payload_ref

Route definitions require:
- source
- path
- budget

Policy definitions require:
- trigger
- action

Kernel definitions require:
- inputs
- outputs
- shape contract
- execution target

## Opcode Set

Core operations:
- attach
- retrieve
- score
- link
- promote
- demote
- refute
- compress
- stage
- archive

Extended operations:
- hydrate
- expand
- materialize
- compile
- speculate
- reconcile
- validate
- distill
- merge
- split
- pin
- evict

## IR Stack

- `SurfaceIR`: human-authored DSL form
- `MapIR`: canonical typed representation of nodes, edges, payload refs, trust state, route plans, manifests, and policies
- `ScheduleIR`: execution-aware plan with control, retrieval, dense-math, and background-compile classes
- `PageIR`: layout-ready representation for route, evidence, parameter, and context pages
- `KernelIR`: regularized dense transforms suitable for Triton or CUDA lowering
- `BackendIR`: target-specific representation after legality and lowering

MapIR invariants:
- all entities use universal node law
- no inline large payloads
- all routes have budgets

## Lowering Pipeline

Overview:
- keep meaning in MapIR
- lower the substrate progressively
- lower only regular transforms

Phases:
1. parse surface to MapIR
2. validate node contracts
3. validate route budgets
4. assign execution classes
5. derive page manifests
6. convert dense regions to KernelIR
7. lower KernelIR to BackendIR
8. emit runtime plan

Hot-path illegal forms:
- unbounded graph walk
- inline large payload
- unknown codec payload
- unresolved refutation for a high-confidence answer

Required before kernel lowering:
- known shape contract
- known data layout
- known staging manifest

Backend targets:
- CPU control plane
- GPU dense math
- future MLIR-style lowering pipeline

## Scheduler Model

Queues:
- control queue for state transitions, lineage updates, confidence updates, and policy checks
- retrieval queue for route expansion, page lookup, and manifest fetch
- hydration queue for decompression, warm-page assembly, and prefetch
- dense-math queue for similarity, ranking, projection, clustering, and compression transforms
- background-compile queue for replay capsules, summary merges, route-prior updates, expert split/merge, and parameter-artifact synthesis

Scheduling laws:
- never send meaning-heavy irregular logic into dense-math queues
- never stage a payload without a manifest
- prefer coarse payload slabs over fine dust
- keep hot routing units compact so mistakes are cheap

## Translator Bindings

Static translator inputs:
- checkpoint
- tokenizer
- config

Static translator outputs:
- model nodes
- parameter-region nodes
- routeable-region nodes
- lineage records

Static rule:
- model internals are source material only; final ontology is always node plus payload plus typed links

Dynamic translator inputs:
- corpora
- tasks
- live feeds
- trusted API data

Dynamic translator outputs:
- activation maps
- co-usage maps
- route traces
- replay capsules
- candidate contract parameters

Dynamic rule:
- promote repeated, stable, causally useful behavior; never trust one-off activations as meaning

## Parameter Compilation

Premise:
- dense scalar parameters can be grouped into coherent functional bundles and compiled into contract parameters

Compiler targets:
- route_prior
- expert_mask
- adapter_delta
- parameter_artifact
- macro_parameter_page

Grouping requirements:
- shared function
- shared activation regime
- shared route behavior
- shared feature family
- coherent recovery under perturbation

Anti-pattern:
- never group by adjacency alone

## Performance Contract

Hot-path requirements:
- bounded route expansion
- pageable active frontier
- KV-native hot form
- coalesced payload fetch where possible
- runtime precision only when justified

Preferred optimizations:
- page reuse
- prefetch
- prefix or route caching
- fused dense transforms
- shape-stable kernels
- quantized route sketch

Anti-patterns:
- giant hot nodes
- arbitrary pointer chasing on GPU
- full graph materialization
- manifest-free fetches
- unconstrained cross-expert chatter

## Authoring Rules

- write substrate semantics at the DSL level
- declare budgets explicitly
- declare confidence and trust handling explicitly
- declare promotion and refutation laws explicitly
- separate route-time and execution-time objects
- prefer handles, manifests, and page refs over raw inline data
- tag everything with lineage
- treat false paths as first-class outputs
- make all expensive expansions explicit
- assume every repeated pattern should eventually compile downward

## Reference Runtime Layout

- frontend: author DSL, validate contracts, emit MapIR
- control plane: node store, graph ops, state machine, policy engine
- hydration plane: warm-page assembly, decompression, prefetch, residency
- GPU math plane: scoring, ranking, projection, compression, clustering
- compiler plane: replay-capsule generation, route-prior rewriting, distillation
- serving plane: request handling, continuous batching, answer assembly

## Example Programs

Deterministic answer program:
- route current discourse through deterministic knowns, semantic neighborhoods, and recent context
- stage summaries first
- hydrate evidence only when confidence is insufficient
- reconcile deterministic and probabilistic outputs

Ingestion program:
- ingest raw payload
- hash leaves
- create evidence nodes
- attach provenance and trust class
- summarize into routeable semantic pages
- promote if confidence policy passes

Parameter compilation program:
- scan dynamic traces
- cluster coherent functional bundles
- emit parameter-artifact pages
- hot-swap eligible artifacts into active route families

## Alpha Implementation Choice

Fastest path now:
- control plane language: Rust
- DSL frontend: YAML or custom text syntax parsed into Rust structs
- kernel iteration language: Triton
- stable hotspot backend: CUDA or CUTLASS
- IR strategy: custom MapIR now, MLIR-inspired lowering later

Why:
- Rust is the right systems runtime for orchestration and correctness
- Triton is the fastest path for dense-kernel iteration
- CUDA and CUTLASS are the stable sinks for proven hotspots
- MLIR-style lowering is useful immediately even before full MLIR adoption

## First Files To Build

- `mapflow_schema.yaml`
- `mapflow_parser.rs`
- `map_ir.rs`
- `schedule_ir.rs`
- `page_ir.rs`
- `node_store.rs`
- `policy_engine.rs`
- `hydration_manager.rs`
- `route_executor.rs`
- `triton_kernels/`
- `cuda_hotspots/`
- `compiler_loop.rs`

## Integration Rule

MapFlow changes must state:
- whether they affect node law, route law, page law, or kernel lowering
- what stays in MapIR versus what lowers into later IR
- what hot-path legality constraints they add or modify
- what manifest, lineage, or trust surfaces they require
- what repeated patterns are expected to compile downward later

## One-Sentence Summary

MapFlow is a cognitive systems DSL whose surface language expresses substrate law, whose IR preserves node, route, lineage, trust, staging, and hydration semantics, and whose compiler lowers only dense regular transforms into fast GPU kernels while the map remains the primary executable intelligence substrate.
