---
title: Visual To Implementation Schema
status: bounded
authority: thread-frozen
tags:
  - visual-to-implementation
  - schematic
  - harness
  - compiler
  - ir
  - projections
  - python
  - rust
  - gui
  - control-plane
---

# Visual To Implementation Schema

## Status

`bounded`

This file captures the visual-authoring-to-implementation tangent as a first-class subsystem of the architecture corpus.

It is not the Cathedral itself.
It is not the Coding Foundry itself.
It is the structural authoring and compilation system that helps externalize, formalize, and regenerate both.

## Core Truth

The system must be buildable visually at depth.

The visual artifact is required because the architecture is too structurally dense to be managed as prose or raw code alone.

The visual artifact is **not** the final semantic truth.

The correct shape is:

1. visual schematic or harness authoring
2. canonical IR
3. compiled projections

This is not a compromise. It is the correct architecture for the problem.

## Mental Category

The correct metaphor is not a mind map.

The correct category is closer to:
- industrial harness logic
- plant-scale engineered systems
- loomed machine nervous systems
- hierarchical schematic systems

That matters because the system needs:
- trunks
- branches
- typed interfaces
- control loops
- feedback returns
- cross-boundaries
- monitoring points
- hierarchical decomposition

## Source Of Truth Rule

The authoring stack has three distinct layers:

### Visual Layer

Purpose:
- human topology thinking
- layout
- visible boundaries
- subsystem navigation

The visual layer is for human cognition, not final machine authority.

### IR Layer

Purpose:
- canonical machine-readable truth
- structure without drawing trivia
- identity, boundaries, interfaces, topology, and projection intent

This is the authoritative layer.

### Projection Layer

Purpose:
- generate executable and navigable outputs from the IR

Examples:
- Python package scaffolds
- Rust runtime scaffolds
- docs
- GUIs
- inventories
- validation outputs
- wiki pages

## Layout Is Not Logic

The system must preserve the distinction between:

- where something sits on a page
- what that thing structurally is

The compiler should consume:
- symbols
- labels
- IDs
- ports
- sheets
- boundaries
- structured metadata

It should not consume pixels or aesthetic trivia as semantic authority.

## Structural Frontend Rule

The schematic is a frontend, not the truth layer.

It should visually author:
- nodes
- ports
- buses
- branches
- feedback loops
- monitors
- policy gates
- storage layers
- compute layers
- trust boundaries
- subsystem boundaries

The compiler should then extract:
- typed nodes
- typed edges
- hierarchy
- directionality
- multiplicity
- trust boundaries
- stateful vs stateless declarations where structurally relevant
- failure domains
- observability hooks
- control loops
- cost classes where structurally declared

## IR To Code Rule

Do not compile Python into Rust.

Do not let Python become the semantic source of truth by accident.

Python and Rust must compile from the same canonical IR.

That means:
- Python is a downstream target
- Rust is a downstream target
- GUI/control views are downstream targets
- docs are downstream targets

They are siblings, not parents of each other.

## Portable Execution Model

The schematic should not compile directly into language-specific code structures as its first semantic target.

It should first compile into a portable execution model containing:
- subsystems
- nodes
- ports
- contracts
- channels
- control domains
- memory domains
- schedulers
- policies as structural references
- observability points
- failure boundaries

That portable execution model can then be lowered into:
- Python packages
- Rust crates or services
- control-plane surfaces
- wiki projections

## Package And Ownership Rule

The compiler should prefer generating packages and owned zones rather than mutating arbitrary handwritten code.

Safe pattern:
- compiler owns generated structure
- humans own custom behavior

Recommended ownership split:
- generated files or directories for compiler-owned structure
- custom files or directories for human-owned behavior

This avoids future regeneration fights.

## Regeneration Rule

Every projection should be regenerable from the same IR.

That includes:
- docs
- code scaffolds
- GUI views
- inventories
- validation views
- wiki pages

If a projection cannot be regenerated cleanly, it should not silently become the real source of truth.

## GUI Rule

The GUI is not an afterthought.

It is another compiled view of the same canonical structural model.

The intended view family includes:
- authoring schematic views
- operator/control-plane views
- observability views
- system-self-visibility views

That means the system should be able to see its own structure through the same canonical model the human uses.

## Two Graphs Rule

The visual-to-implementation system should not assume one flat graph is sufficient.

At minimum it needs:

### Topology Graph

What connects to what.

### Semantic Or Relation Graph

What the connection means.

Because the same two things may be connected by different relation types:
- data flow
- control flow
- feedback
- policy approval
- telemetry
- training exhaust
- memory update
- human override

These relations must not be flattened into one untyped edge model.

## Compiler Passes

The tangent established an intended compiler shape:

1. ingest pass
2. resolution pass
3. typing pass
4. validation pass
5. projection pass

These passes remain bounded architectural intent, not an implementation mandate.

## What This Does Not Change

- This does not replace the Structural IR boundary rules.
- This does not collapse the Coding Foundry into a generic code generator.
- This does not make the visual schematic itself authoritative.
- This does not make Python the parent of Rust.
- This does not force arbitrary in-place editing of handwritten code.

