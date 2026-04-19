---
title: Thread Truth Checklist
status: bounded
authority: verification
tags:
  - verification
  - truth-check
  - user-truth
  - boundedness
  - cathedral
  - foundry
  - training
  - compiler
---

# Thread Truth Checklist

This file is the explicit self-check against the thread’s user-provided truth.

## Core Truth Checks

- [x] The final system is The Cathedral.
- [x] The Coding Foundry is not the final system.
- [x] The Coding Foundry is treated as a bounded subsystem that later lives inside the larger system.
- [x] Intelligence is treated as distributed rather than concentrated in one dense model blob.
- [x] Memory is split into species.
- [x] Graphs are layered rather than singular.
- [x] Deterministic truth remains first-class.
- [x] Packet shaping remains canonical.
- [x] The model stack is a society of specialized species.

## Structural Compiler Checks

- [x] The visual artifact is not treated as semantic truth.
- [x] A canonical IR remains between visual authoring and downstream code.
- [x] Python and Rust are treated as sibling targets of the same IR.
- [x] The structural compiler track is not collapsed into the Coding Foundry.

## Training Checks

- [x] The original role set remains separate.
- [x] Each role gets custom training.
- [x] Dolphin variants of Qwen remain the base family for the role plan.
- [x] Independent jobs may fan out.
- [x] Single training jobs stay local to one host or tightly coupled machine.
- [x] Hardware policy still optimizes for cheapest acceptable hardware.

## Harness Checks

- [x] Rust control plane preserved
- [x] `vLLM` primary serving backend preserved
- [x] packet-based harness preserved
- [x] strict JSON role contracts preserved
- [x] six-service boundary preserved
- [x] broker is not used for large inline blobs

## Non-Drift Checks

- [x] The architecture is not reduced to an MVP agent harness
- [x] The coding lane is not treated as the entire system
- [x] The outside-chat results did not override direct user truth
- [x] Provisional open items remain clearly bounded

## Current Gaps

- [ ] Deterministic-truth schema not fully frozen
- [ ] Working-memory schema not fully frozen
- [ ] Promotion/consolidation hook schema not fully frozen
- [ ] Visual-harness-to-IR mapping not fully frozen
- [ ] Structural-IR-to-packet-boundary mapping not fully frozen

