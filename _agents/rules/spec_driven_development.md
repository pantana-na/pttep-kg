---
trigger: always_on
description: "Strictly enforce Spec-Driven Development (SDD) with mandatory brownfield baseline, detailed implementation plans, and unit + property-based testing at every step."
---

# Rule: Spec-Driven Development (SDD) & Brownfield Protocol

## Core Mandate
This project operates strictly under the **Spec-Driven Development (SDD)** process.
**Code is a downstream artifact derived from specification documents.** No feature implementation, architectural change, major refactoring, or API modification may begin without:
1. An approved, up-to-date Specification Document (SDD) stored under `specs/`.
2. A detailed **Implementation Plan** breaking down changes into concrete steps.
3. Dedicated **Unit Tests** and **Property-Based Tests (PBT)** defined for every implementation step.

---

## 1. Brownfield Development Protocol (Mandatory Baseline First)

When working on an existing (brownfield) codebase or modifying any existing subsystem:

1. **Check for Baseline SDD:**
   - Before writing or modifying any code, verify if a comprehensive Baseline SDD exists in `specs/baseline/` for the targeted component/system.
2. **Reverse-Engineer / Generate Baseline SDD First:**
   - If no Baseline SDD exists (or if it is out-of-date), you **MUST** inspect the existing code, dependencies, data contracts, and APIs to generate a complete Baseline SDD first.
   - The Baseline SDD must accurately document the "as-is" state:
     - Architecture and subsystem boundaries
     - Data models and TypeScript types / schemas
     - API endpoints, payloads, headers, and error behaviors
     - Business logic, algorithms, and domain constraints
     - UI/UX workflows and component hierarchy
     - External service integrations (e.g., Gemini API, Vertex AI, Google Cloud)
     - Core system invariants to be protected by property tests
3. **Establish Baseline Before Delta:**
   - Only after the baseline state is codified into `specs/baseline/` can feature specs or modification plans (`specs/features/`) be drafted against it.

---

## 2. SDD Workflow Lifecycle

Every development task must progress through these sequential phases:

```
[Phase 0: Baseline Discovery (Brownfield only)]
               │
               ▼
[Phase 1: Specification Authoring (SDD)]
               │
               ▼
[Phase 2: Detailed Implementation Plan + Test Strategy]
               │
               ▼
[Phase 3: Review & Alignment]
               │
               ▼
[Phase 4: Step-by-Step Implementation + Unit & Property Tests]
               │
               ▼
[Phase 5: Verification, Full Test Suite & Living Spec Sync]
```

### Phase 0: Baseline Discovery (Brownfield only)
- Inspect existing files, configuration, models, and tests.
- Document current behavior, contracts, and invariants in `specs/baseline/`.

### Phase 1: Specification Authoring
- Create or update the relevant spec under `specs/features/` or `specs/` using `specs/templates/sdd-template.md`.
- Required sections:
  1. Problem Statement & Goals / Non-Goals
  2. System Architecture & Component Interactions
  3. Data Models & Schema Definitions (Single source of truth)
  4. API Contracts & Integrations (Request/Response, status codes, error shapes)
  5. UI/UX & Behavioral Specifications (State machines, edge cases, validation)
  6. Security, Privacy & Non-Functional Requirements

### Phase 2: Detailed Implementation Plan & Test Design
Before writing production code, author a granular **Implementation Plan** in the SDD with:
- **Sequential Step Breakdown:** Clear, manageable steps from foundational models/types to backend APIs, UI components, and integrations.
- **Unit Tests for Every Step:** Specific, deterministic test cases covering expected behavior, edge cases, and error paths.
- **Property-Based Tests (PBT) for Every Step:** Formal mathematical/logical invariants tested across randomized, fuzzed, or generative inputs (e.g. with `fast-check` in TS/JS or `hypothesis` in Python).
- **Completion Criteria:** Definition of Done for each individual step.

### Phase 3: Review & Alignment
- Review the proposed specification, step-by-step implementation plan, and test designs with the user/stakeholders.
- Resolve ambiguities, edge cases, and design trade-offs *in the document* before writing code.

### Phase 4: Step-by-Step Implementation
- Execute the implementation plan step-by-step.
- For each step:
  1. Implement the step code and its required types/contracts.
  2. Implement the accompanying Unit Tests.
  3. Implement the accompanying Property-Based Tests.
  4. Run and verify that all tests pass before proceeding to the next step.

### Phase 5: Verification & Living Spec Synchronization
- Run the complete test suite (all unit tests and property tests).
- Verify against every Acceptance Criterion in the SDD.
- If necessary refinements arise during implementation, update the SDD immediately to prevent spec drift.

---

## 3. Mandatory Testing Standards for Every Step

For **every step** in the implementation plan:

### 3.1 Unit Testing Requirements
- **Deterministic Examples:** Test concrete inputs and verified expected outputs.
- **Boundary & Edge Conditions:** Empty sets, max limits (e.g., 20 images limit, exactly 6 digits), malformed payloads, network timeout errors.
- **Mocking & Isolation:** Isolate external services (e.g. mock Gemini API calls and network transport) to ensure fast, reliable test execution.

### 3.2 Property-Based Testing (PBT) Requirements
- **Universal Invariants:** Formulate properties that must hold true for *all* valid inputs (e.g., "Severity ordering is monotonic: grade(F) >= grade(E) >= ... >= grade(A)", "Summary grade is never better than any individual image grade", "Non-relevant/NA results never alter valid grade aggregation").
- **Generative Arbitraries:** Use generators (`fc.string()`, `fc.record()`, `fc.array()`) to produce hundreds of permutations.
- **Shrinking & Counterexamples:** Ensure failing properties produce minimal failing examples to quickly diagnose edge bugs.
- **Idempotence & Round-tripping:** Test serialization/deserialization, normalizer idempotence (`normalize(normalize(x)) === normalize(x)`).

---

## 4. Directory Structure & Spec Organization

All specifications must reside in the `specs/` directory:

```
specs/
├── README.md                      # Index of all specifications
├── templates/
│   └── sdd-template.md            # Standardized template with Implementation Plan & Testing sections
├── baseline/                      # Baseline SDDs for existing/brownfield code
│   └── system-overview.md         # Full system architecture, stack & invariants
└── features/                      # Feature specifications and enhancement proposals
    └── <feature-id>-<title>.md
```

---

## 5. Hard Enforcement Rules

1. **No Code Without Spec & Plan:** Reject or pause direct coding requests until the SDD, detailed implementation plan, and test designs are established.
2. **Unit & Property Tests Required at Every Step:** Code without corresponding unit tests and property-based tests is strictly prohibited.
3. **Strict Schema Fidelity:** API responses, frontend types, and backend validation schemas must be exact matches to the SDD contracts.
4. **Zero Spec Drift:** If code changes behavior, the SDD must be updated in the same commit/change.
5. **Preserve Domain Invariants:** Ensure core domain properties (container number format, grading severity order, upload caps, credential boundaries) are strictly validated by property tests.
