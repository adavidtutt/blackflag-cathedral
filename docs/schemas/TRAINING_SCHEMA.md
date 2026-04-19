---
title: Training Schema
status: bounded
authority: thread-plus-reconciled
tags:
  - training
  - models
  - dolphin
  - qwen
  - hardware
  - role-training
  - dataset-mapping
  - custom-training
  - hot-warm-cold
---

# Training Schema

## Status

`bounded`

This file consolidates the training and model plan discussed from the beginning of the thread through the later reconciliations.

## Non-Negotiables

Status: `frozen`

- Each original role gets its own custom training job.
- Do not collapse the role set into fewer checkpoints for the frozen plan.
- Use Dolphin variants of Qwen for the planned role family.
- Training and runtime economics matter.
- Independent jobs may fan out globally.
- A single training job should stay on one host or a tightly coupled machine.

## Role Family

Status: `frozen`

- Router: `Dolphin 2.9.3 Qwen2 0.5B`
- Scaffolder: `Dolphin 3.0 Qwen2.5 3B`
- Logic Worker: `Dolphin 3.0 Qwen2.5 3B`
- Pedantic Tester: `Dolphin 3.0 Qwen2.5 3B`
- Linter / Security: `Dolphin 3.0 Qwen2.5 3B`
- Documenter: `Dolphin 3.0 Qwen2.5 3B`
- Fixer: `Dolphin 3.0 Qwen2.5 3B`
- Manager: `Dolphin 3.0 Qwen2.5 32B`
- Architect: `Dolphin 3.0 Qwen2.5 72B`

## Dataset Mapping

Status: `bounded`

These mappings were established earlier in-thread and retained because the user explicitly asked to preserve the training discussion from the beginning.

### Router

- Base: `Dolphin 2.9.3 Qwen2 0.5B`
- Dataset direction:
  - `NousResearch/hermes-function-calling-v1`
  - plus remapped routing labels for this system
- Objective:
  - strict queue routing
  - structured output compliance

### Scaffolder

- Base: `Dolphin 3.0 Qwen2.5 3B`
- Dataset direction:
  - `OpenCoder-LLM` stage-1 style slices
- Objective:
  - boilerplate
  - schema stubs
  - file layout

### Logic Worker

- Base: `Dolphin 3.0 Qwen2.5 3B`
- Dataset direction:
  - `CodeFeedback` filtered for implementation-heavy tasks
- Objective:
  - function internals
  - algorithmic edits

### Pedantic Tester

- Base: `Dolphin 3.0 Qwen2.5 3B`
- Dataset direction:
  - `NuminaMath-CoT`
  - plus real code-test corpora
- Objective:
  - test generation
  - rigorous reasoning

### Linter / Security

- Base: `Dolphin 3.0 Qwen2.5 3B`
- Dataset direction:
  - security/lint corpus in addition to general coding data
- Objective:
  - static review
  - vuln flags
  - syntax/import issues

### Documenter

- Base: `Dolphin 3.0 Qwen2.5 3B`
- Dataset direction:
  - `smoltalk`
  - plus code-doc pairs
- Objective:
  - README
  - inline comments
  - setup docs

### Fixer

- Base: `Dolphin 3.0 Qwen2.5 3B`
- Dataset direction:
  - traceback/log -> patch corpus
- Objective:
  - repair from failing traces
  - repair from test logs

### Manager

- Base: `Dolphin 3.0 Qwen2.5 32B`
- Dataset direction:
  - task-graph
  - review
  - merge data
- Objective:
  - decomposition
  - routing
  - review
  - escalation

### Architect

- Base: `Dolphin 3.0 Qwen2.5 72B`
- Dataset direction:
  - planning
  - synthesis
  - system design corpora
- Objective:
  - blueprinting
  - synthesis
  - high-level arbitration

## Hardware Classes

Status: `bounded`

Earlier working classes:

- `C1`: cheap single consumer GPU
- `C2`: cheap tightly coupled consumer multi-GPU host
- `E1`: premium enterprise multi-GPU node
- `E2`: highest-end premium enterprise node

These are abstract policy classes, not locked vendor/SKU choices.

## Hardware Assignment Policy

Status: `frozen`
Canonical source: `outside-chat reconciliation -> ChatGPT 5.4`

Principle:
- choose the cheapest acceptable hardware class
- do not sacrifice planned quality to stay cheap

### Router

- default: cheapest acceptable single consumer class

### 3B Workers

- default: cheapest acceptable consumer class
- escalate to tightly coupled consumer multi-GPU when the recipe cannot complete acceptably on smaller hardware

### Manager

- default: premium enterprise node
- cheaper consumer multi-GPU only if a dry-run proves the full intended recipe fits without quality compromise and still wins economically

### Architect

- default: highest-end premium enterprise node
- do not route actual architect training through cheap hardware experimentation

## Escalation Triggers

Status: `frozen`

- memory fit failure
- quality-preservation failure
- cost crossover
- interconnect bottleneck
- reliability failure

## Parallelization Rules

Status: `frozen`

- Independent small-role jobs can fan out globally.
- Do not split one training job across random distant hosts.
- Parallelize the six 3B workers horizontally when cheap capacity exists.
- Keep single large-role jobs local to one host or tightly coupled machine.

## Runtime Planes

Status: `bounded`

From the earlier harness/training discussion:

### Hot Plane

- router
- 3B workers
- always on
- cheap GPUs

### Warm Plane

- manager
- loaded or prewarmed when queue depth or difficulty justifies it

### Cold Plane

- architect
- invoked only for blueprinting, synthesis, escalation, or arbitration

## What This Does Not Change

- This file does not downgrade the custom-per-role training plan.
- This file does not replace the reconciled hardware policy with a new philosophy.
- This file does not fully freeze concrete SKU choices.

