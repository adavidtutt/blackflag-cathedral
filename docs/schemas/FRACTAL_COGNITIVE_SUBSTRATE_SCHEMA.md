---
title: Fractal Cognitive Substrate Schema
status: bounded
authority: direct-user-architecture
tags:
  - cathedral
  - fractal-cognitive-substrate
  - map-first
  - mapflow
  - node-contract
  - routing
  - hydration
  - contradiction
  - lineage
  - compiler
---

# Fractal Cognitive Substrate Schema

## Status

`bounded`

This file is the canonical deep schema for the Fractal Cognitive Substrate, the current bounded doctrine for how the Cathedral's persistent intelligence substrate is structured.

## One-Sentence Law

Build a cryptographically addressed, self-compiling memory fabric in which the map is the persistent cognitive topology, dense models are subordinate language-and-abstraction organs, and hot execution runs on a compressed route sketch that continuously rehydrates, reasons, and recompiles itself.

## Core Posture

- The map is the primary intelligence substrate.
- Dense models are subordinate organs for language, synthesis, abstraction, ambiguity resolution, creativity, and route proposal.
- Deterministic systems own exact records whenever the world is knowable.
- Probabilistic systems operate where abstraction, compression, interpretation, or novelty are required.
- Identity, lineage, contradiction, route history, and provenance are first-class intelligence surfaces rather than side metadata.
- Runtime state is a lowering of the larger substrate, not a replacement ontology.

## Compiler Surface

Status: `bounded`

The current bounded language and compiler surface for FCS is **MapFlow**.

MapFlow is the authoring and lowering interface used to:
- express substrate semantics in a human-readable and machine-lowerable form
- preserve node, route, lineage, trust, staging, and hydration semantics in IR
- schedule control, retrieval, dense math, and background compile work explicitly
- lower only dense regular transforms into Triton or CUDA class kernels

Canonical deep schema:
- [MAPFLOW_SCHEMA.md](./MAPFLOW_SCHEMA.md)

## Design Laws

- Everything becomes an artifact.
- Every artifact has lineage.
- Every artifact lives in a typed neighborhood.
- Every neighborhood is sparsely traversable.
- Every traversal leaves exhaust.
- Exhaust recompiles the map.
- One node shell. One small verb set. Many payload classes.
- Hot holds direction. Warm holds readiness. Cold holds truth.
- Do not lower meaning into kernels; lower regular transforms into kernels.
- Ingest wide. Stage narrow. Compile aggressively.
- No node exists only because data exists; a node exists because the system needs a stable executable contract around the data.
- The fractal repeats in contract and behavior, not necessarily in byte size.

## Universal Structure

### Core Abstractions

- `artifact`: any addressable thing in the system
- `node`: universal shell that wraps or points to an artifact
- `payload`: typed data behind a node
- `contract`: stable lifecycle and execution surface around a node
- `route_sketch`: compact hot execution form of the active frontier
- `hydration`: expansion of compact route choices into working sets
- `exhaust`: reusable byproducts of retrieval, routing, inference, correction, and interaction

### Universal Node Contract

Every stable substrate object should be expressible through one node contract.

Required fields:
- `id`
- `kind`
- `payload_ref`
- `state`
- `lineage`
- `links`
- `summary`
- `stats`

Optional fields:
- `permissions`
- `compression_class`
- `execution_hooks`
- `route_signature`
- `page_refs`
- `expansion_recipe`
- `trust_vector`
- `refutation_refs`

### Universal Operations

All node kinds should support the same small verb set:
- `attach`
- `retrieve`
- `score`
- `link`
- `promote`
- `demote`
- `refute`
- `compress`
- `stage`
- `archive`

Execution classes:
- pure control ops
- retrieval ops
- dense math ops
- background compile ops

## Layer Map

The FCS subsystem is organized into six semantic layers plus one cross-cutting compiler surface. Additions should land in one or more of these layers or explicitly target the compiler surface rather than appearing as free-floating doctrine.

### 1. Ontology

Owns:
- artifact classes
- node contract
- payload classes
- identity rules
- lineage surfaces
- universal verbs

Key invariants:
- immutable artifact identity must be distinct from mutable adjudication state
- payload custody must be separated from contract metadata
- a node contract must be executable, not merely descriptive

### 2. Memory Topology

Owns:
- cold plane
- warm plane
- hot plane
- speculative plane
- sizing and granularity law
- staging and residency policy

Key invariants:
- hot stores direction, not archive bulk
- warm stores hydration-ready structure
- cold stores exact or safely compressed durable truth
- object size follows function class rather than a global default

### 3. Graph Topology

Owns:
- identity graph
- provenance graph
- semantic adjacency graph
- contradiction graph
- temporal graph
- task graph
- parameter affinity graph
- route frequency graph
- compression graph
- confidence lattice
- refutation and supersession semantics

Key invariants:
- contradiction must remain attached, not discarded
- edge types are typed, confidence-bearing, and lineage-bearing
- contradiction is scoped by task, time, source regime, or interpretation frame

### 4. Runtime Routing

Owns:
- durable map to warm map lowering
- warm map to hot route sketch lowering
- route-sketch structure
- hydration pipeline
- deterministic and probabilistic arbitration during one turn
- hot execution budgets and traversal stop rules

Key invariants:
- hot projection is derived, never sovereign
- no live path touches an unbounded neighborhood
- no payload reaches VRAM without a manifest or explicit staging decision

### 5. Compiler Learning

Owns:
- exhaust capture
- background compiler loop
- summary generation
- route-prior rewrite
- promotion and demotion
- replay-capsule generation
- compression families
- speculative prestaging

Key invariants:
- exhaust must be typed by causal class
- background work must compile downward into fewer, denser structures over time
- false paths must become refutation assets that influence future routing

### 6. Model Interface

Owns:
- deterministic and probabilistic split
- model role boundaries
- static translator
- dynamic translator
- parameter system
- online parameterization rules
- model-adjacent artifacts and promotion boundaries

Key invariants:
- models do not own primary fact storage, provenance, or contradiction
- parameter promotion targets reusable transforms, priors, adapters, and gates before contingent world facts
- substrate update, route update, and parameter synthesis remain distinct learning modes

### 7. MapFlow

Owns:
- author-facing DSL constructs
- grammar and syntax model
- MapIR and later IR layers
- legality and lowering rules
- scheduler-visible execution classes
- page and kernel lowering interfaces
- backend target doctrine

Key invariants:
- meaning stays in substrate-level IR rather than kernel IR
- only dense regular transforms lower into GPU kernels
- hot-path legality requires explicit budgets, manifests, and known layouts
- compiler surfaces must preserve node law rather than invent a second ontology

## Memory Planes

### Cold

Role: world archive

Contains:
- raw source artifacts
- original documents
- checkpoints
- full lineage
- archived traces
- full refutation history

### Warm

Role: living map and hydration fabric

Contains:
- neighborhoods
- route tables
- summaries
- confidence structures
- chunk manifests
- semantic indices
- page manifests

### Hot

Role: control surface and execution frontier

Contains:
- active discourse state
- active route candidates
- active working set
- confidence frontier
- top neighborhoods
- active contract pages

### Speculative

Role: predictive prestaging workspace

Contains:
- likely next route branches
- likely next retrieval families
- likely next intent classes
- speculative summaries
- tentative promotions

## Runtime Doctrine

One user turn should execute as:

1. parse input into discourse state
2. query deterministic mind for exact knowns
3. query probabilistic mind for semantic neighborhoods
4. select route candidates and expert regions
5. stage only required payloads or pages
6. run dense math on staged material
7. reconcile deterministic evidence and probabilistic proposals
8. answer with confidence and provenance
9. emit exhaust

Required answer surfaces:
- user answer
- confidence breakdown
- provenance chain
- known versus inferred distinction
- route and context updates

## Deterministic / Probabilistic / Compiler Split

### Deterministic Mind

Owns:
- exact records
- structured facts
- provenance
- rules
- symbolic joins
- contradiction tracking
- time ordering

### Probabilistic Mind

Owns:
- language
- abstraction
- synthesis
- ambiguity resolution
- analogy
- novelty
- missing-link proposal

### Compiler Mind

Owns:
- map rewrites
- summary generation
- route prior updates
- compaction
- promotion and demotion
- failure analysis
- refutation synthesis
- speculative prestaging

## Parameter System

Parameters are broader than dense scalar weights.

Parameter classes:
- scalar parameters
- contract parameters
- route parameters
- reality parameters
- confidence parameters

Promotion rule:
- mutable world knowledge should stay in the map unless there is a strong reason to compile a reusable transform or control artifact from it

## MapFlow Binding

MapFlow binds to FCS through these rules:

- node contracts in MapFlow must remain structurally compatible with FCS node law
- route definitions in MapFlow must compile into explicit traversal budgets and staging manifests
- page and KV projection rules in MapFlow must preserve the hot/warm/cold memory law
- kernel lowering is permitted only after shapes, layouts, and execution targets are explicit
- compiler outputs must distinguish map updates, route updates, and parameter-artifact synthesis

## Open Questions

- What is the smallest stable useful leaf contract per memory class?
- What exact fields belong in the hot route sketch?
- How should parameter regions be grouped into coherent contract parameters?
- Which promotions become parameter artifacts versus map-only structure?
- What route-sketch representation gives the best bytes-per-decision?
- Which compression family best fits each artifact class?
- How much causal validation is needed before feature or circuit promotion?
- What quantization is safe for hot routing without destabilizing route quality?
- What scheduling split is best across CPU, DRAM, VRAM, and multi-device planes?
- Which surfaces should stay immutable versus fast-mutable?

## Integration Rule

Future passes should update this schema using these rules:

- Additions must land in an existing layer or explicitly declare a new layer and why it cannot fit an existing one.
- New fields must state whether they are immutable, mutable, derived, or speculative.
- New execution paths must declare their budget surface, provenance surface, and exhaust surface.
- New promotion logic must state what it does not permit, not only what it enables.
- New model-facing ideas must state whether they change map structure, route priors, or parameter artifacts.

## What This Does Not Change

- The Cathedral remains the final-system authority.
- The Coding Foundry remains a bounded Cathedral-compatible subsystem.
- This file does not freeze every implementation detail yet.
- This file does not license a second runtime ontology outside the node law.
