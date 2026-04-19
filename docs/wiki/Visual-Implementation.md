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

The system must be buildable visually at depth, but the visual artifact is not the final semantic truth.

The canonical path is:
- visual schematic or harness authoring
- canonical IR
- compiled projections

Python and Rust are sibling targets of that IR. The visual-to-implementation system also treats GUIs and operator views as compiled projections of the same canonical structure.

For canonical detail, see:
- [../schemas/VISUAL_IMPLEMENTATION_SCHEMA.md](../schemas/VISUAL_IMPLEMENTATION_SCHEMA.md)
- [../schemas/STRUCTURAL_COMPILER_SCHEMA.md](../schemas/STRUCTURAL_COMPILER_SCHEMA.md)

