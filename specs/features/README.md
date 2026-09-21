# Feature Specifications Directory

This directory contains the authoritative feature and architectural specifications for the **Refinery Phenol Process Safety Expert & Multi-Agent Platform**.

All historical feature designs and specifications (August 24, 2026 – September 21, 2026) have been consolidated into the unified master specification document below:

## Authoritative System Specification

| Document ID | Title | Status | Scope |
|---|---|---|---|
| [`SPEC-CONSOLIDATED-20260921-SYSTEM-ARCHITECTURE`](./CONSOLIDATED_FEATURE_SPECIFICATION.md) | **Consolidated Feature Specification & System Architecture** | Approved & Implemented | Decoupled cloud architecture (Gemini Enterprise Agent Platform backend + Cloud Run frontend), single orchestrator with zero regex intent dispatch, Tri-Tier knowledge layer (Spanner, Dataplex, GCS), inline Model Armor guardrails, Tri-Pane Mission Control Cockpit, automated 14-parameter HAZOP facilitation with 7-tab Excel export, and Neutral Refinery data sanitization. |

---

## SDD Governance & Extension Protocol

Any future feature proposals, modifications, or API changes must be drafted in this directory following [`specs/templates/sdd-template.md`](../templates/sdd-template.md) and synchronized with this master specification and the implementation plan in [`specs/plan/`](../plan/).
