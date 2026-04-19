---
title: Structural Compiler Schema
status: bounded
authority: thread-frozen
tags:
  - structural-compiler
  - visual-authoring
  - harness
  - ir
  - schema
  - python
  - rust
  - projections
  - wiki
---

# Structural Compiler Schema

## Status

`bounded`

This track is adjacent to, but distinct from, the Coding Foundry.

## Purpose

The structural compiler track exists because the system must be authored visually at depth, but the visual artifact is not the final semantic truth.

Correct shape:
- visual schematic or harness authoring
- canonical intermediate representation
- generated downstream projections

## Core Rule

Python and Rust are downstream targets of the same semantic or structural IR.

Rust is not compiled from Python.
Python is not the semantic parent of Rust.

They are sibling targets of the same canonical truth layer.

## Structural IR Boundary

Status: `frozen`
Canonical source: `outside-chat reconciliation -> ChatGPT 5.4`

### Must Exist In The Structural IR

- stable identity and addressability
- node kinds and structural roles
- containment and composition
- ports, interfaces, and connection topology
- boundary declarations
- structural contracts
- typed interface-level artifacts where required for composition
- instantiation and reuse semantics
- minimal projection metadata
- provenance and source mapping
- structural validation markers
- disciplined extension points

### Must Not Exist In The Structural IR

- executable logic
- target-language idioms
- UI-only drawing trivia
- runtime state
- optimization policy
- human-process prose as authority
- environment-specific deployment facts
- behavior smuggled in as structure

## Projection Philosophy

The visual artifact is for human legibility.
The IR is for compiler legibility.
Generated code, docs, GUIs, and control surfaces are projections.

## Intended Projections

- Python runtime scaffolds
- Rust runtime scaffolds
- docs
- GUI/control-plane views
- wiki pages
- inventories
- validation reports

## What This Does Not Change

- This does not replace the visual-first authoring approach.
- This does not make Python the semantic source of truth.
- This does not collapse the Structural Compiler track into the Coding Foundry.

