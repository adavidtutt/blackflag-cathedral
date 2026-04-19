---
title: Harness Schema
status: bounded
authority: thread-plus-reconciled
tags:
  - harness
  - rust
  - vllm
  - nats
  - postgres
  - sandbox
  - service-boundaries
  - packets
  - runtime-planes
---

# Harness Schema

## Status

`bounded`

This file consolidates the frozen harness baseline plus the reconciled service-boundary result.

## Harness Baseline

Status: `frozen`

- Rust control plane
- `vLLM` primary serving backend
- hot / warm / cold runtime planes
- NATS JetStream
- Postgres
- sandbox runner
- strict JSON role contracts
- packet-based orchestration
- deterministic truth as first-class rule
- compression as a configurable serving-layer interface

## Services

Status: `frozen`

- gateway
- scheduler
- broker
- sandbox-runner
- artifact-store
- telemetry

## Service Boundaries

Status: `frozen`
Canonical source: `outside-chat reconciliation -> ChatGPT 5.4`

### Gateway

External ingress/egress boundary:
- client-facing API admission
- request normalization into strict JSON contracts
- auth and response shaping

### Scheduler

Decision boundary:
- job classification
- runtime-plane selection
- queue placement
- priority
- reservation logic
- retries and lifecycle routing

### Broker

Execution mediation boundary:
- backend invocation mediation
- backend call correlation
- response normalization
- abstraction over `vLLM` and similar serving backends

### Sandbox-Runner

Isolated tool/process execution boundary:
- repo and workspace execution
- isolated tool runs
- bounded process lifecycle
- structured output emission

### Artifact-Store

Durable artifact custody:
- immutable or versioned artifacts
- content fingerprints
- manifests
- retrieval handles

### Telemetry

Observability boundary:
- logs
- traces
- metrics
- replayable operational records

## Forbidden Couplings

Status: `frozen`

- Gateway must not call serving backends directly.
- Scheduler must not invoke `vLLM` or tool runtimes directly.
- Broker must not self-assign or reprioritize work outside scheduler authority.
- Sandbox-runner must not own model-serving orchestration that belongs to broker.
- Artifact-store must not become a workflow engine.
- Telemetry must not become authoritative workflow truth.
- No service may rely on another service’s private DB schema or in-memory structures.
- No service should infer control truth from another service’s logs.
- No large blobs should be sent through the broker. Use artifact refs or URIs instead.

## Runtime Planes

Status: `bounded`

### Hot

- router
- 3B worker pool
- cheap always-on capacity

### Warm

- manager
- prewarm when backlog or difficulty justifies it

### Cold

- architect
- load for blueprinting, synthesis, escalation, arbitration

## Packet Rule

Status: `frozen`

The harness remains packet-based. It does not regress into freeform prompt chaining.

## What This Does Not Change

- Rust remains the control-plane assumption.
- `vLLM` remains the primary serving backend assumption.
- The six-service harness shape remains intact.

