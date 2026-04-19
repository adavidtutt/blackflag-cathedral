---
title: Visual Implementation
status: wiki
tags:
  - wiki
  - visual-to-implementation
  - schematic
  - compiler
  - ir
  - projections
---

# Visual Implementation

The system must be buildable visually at depth, and the visual system is allowed to change truth.

The canonical path is:
- visual schematic or harness authoring
- bound subdocumentation
- canonical IR compiled from that authoring truth
- compiled projections

Python and Rust are sibling targets of that IR. The visual-to-implementation system also treats GUIs and operator views as compiled projections of the same canonical structure.

For canonical detail, see:
- [../schemas/VISUAL_IMPLEMENTATION_SCHEMA.md](../schemas/VISUAL_IMPLEMENTATION_SCHEMA.md)
- [../schemas/STRUCTURAL_COMPILER_SCHEMA.md](../schemas/STRUCTURAL_COMPILER_SCHEMA.md)
