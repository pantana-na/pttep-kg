# Rule: Mandatory Root Cause Investigation & Zero Quick-Patch Standard

## Core Mandate
When any test fails (**Agent Evaluation (`agents-cli eval`)**, **Property-Based Tests (PBT)**, **Unit Tests**, or **Integration Tests**), or when a user reports a defect or requests a bug fix:

**DEVELOPERS AND AI AGENTS ARE STRICTLY PROHIBITED FROM APPLYING QUICK FIXES, MOCKUP FALLBACK DATA, REGEX PATCHES, OR RULE-BASED CODE WORKAROUNDS.**

Under all circumstances, the developer/agent must:
1. **Investigate the actual root cause** across the live data, model reasoning, tool contracts, or system architecture.
2. **Transparently explain to the user** why the failure occurred, backed by technical evidence.
3. **Present viable architectural fix choices** along with their trade-offs.
4. **Await explicit user instruction** on which fix approach to implement before writing any modification.

---

## 1. Scope of Enforcement
This rule applies across the entire software lifecycle:
- **Agent Evaluations (`agents-cli eval run`):** Trajectory deviations, tool selection errors, hallucination, or safety guardrail failures.
- **Property-Based Testing (PBT / Hypothesis):** Invariant violations, shrinking counterexamples, or boundary crashes.
- **Deterministic Unit Testing:** Assertion mismatches, contract breaks, or unhandled exceptions.
- **Integration & Deployment Testing:** Cloud Run probe timeouts, API status errors, or database synchronization failures.
- **User Bug Reports & Fix Requests:** Any user prompt stating "Fix X", "Why did Y happen?", or requesting behavioral corrections.

---

## 2. Strictly Prohibited Anti-Patterns (The "Quick-Fix" Trap)

The following practices are **strictly prohibited** in this repository:

1. ❌ **Mockup Data & Fallback Dictionaries:**
   - Injecting synthetic fallback dictionaries or offline mockup data into application code to bypass missing or inconsistent database records.
   - *Example Prohibited:* `if not db_result: return {"tag": "E-2303", "temp": 180}`.

2. ❌ **Rule-Based Quick Patching & Special-Casing:**
   - Writing prompt-specific `if/else` checks or hardcoding special-case answers for specific test prompts.
   - *Example Prohibited:* `if "E-2303" in prompt and "instruments" in prompt: return 41`.

3. ❌ **Regex & Keyword Heuristics in Agents:**
   - Adding regex matching or substring heuristics to patch agent classification or routing errors (violating `no_hardcoded_or_regex_in_agents.md`).

4. ❌ **Assertion Weakening / Test Deletion:**
   - Modifying test assertions, deleting failing test cases, or widening tolerances simply to make a red test turn green without solving the defect.

5. ❌ **Hardcoding Domain Constants in Code:**
   - Storing equipment operating conditions, risk ratings, node mappings, or P&ID drawing numbers directly in Python/TypeScript code instead of querying systems of record (Cloud Spanner, Dataplex, GCS).

---

## 3. Mandatory 4-Step Root Cause Investigation Protocol

When a test fails or a fix is requested, the developer/agent **MUST** execute the following protocol sequentially:

### Step 1: Deep Root Cause Analysis (RCA)
- Thoroughly inspect the failure trajectory:
  - Examine database state (Cloud Spanner tables, Graph nodes/edges, Dataplex catalog entries).
  - Inspect Google ADK tool docstrings, parameter types, and negative constraints.
  - Review model cognitive prompts, reasoning context, and temperature settings.
  - Trace network logs, stack traces, and exact failing inputs.
- Isolate the true architectural or data root cause:
  - *Is data missing, incomplete, or corrupted in the database?*
  - *Is a tool docstring ambiguous, causing the model to misselect or skip it?*
  - *Are prompt instructions conflicting or lacking explicit negative constraints?*
  - *Is there a contract or schema mismatch between frontend and backend?*

### Step 2: Transparent Failure Explanation to User
Present a structured, factual diagnostic report to the user detailing:
- **The Exact Failure:** The failing prompt, test name, input arguments, and expected vs actual result.
- **Technical Root Cause:** Clear explanation of the mechanics that caused the failure (e.g. why the model chose Tool B instead of Tool A, or why the database query returned 0 rows).
- **Supporting Evidence:** Relevant log excerpts, database query results, or tool response payloads.

### Step 3: Present Architectural Fix Options & Trade-Offs
Formulate at least **two (2) viable, sustainable engineering options** that resolve the root cause without shortcuts:
- **Option A (e.g., Data Tier Resolution):** Populate or correct records in Cloud Spanner / Dataplex to ground the agent on accurate truth.
- **Option B (e.g., Cognitive Tool Prompt Refinement):** Clarify tool docstrings with explicit "When to use" vs "When NOT to use" negative rules and update orchestrator instructions.
- **Option C (e.g., Schema & Validation Hardening):** Adjust Pydantic models or database constraints to enforce invariants.
- **Provide Trade-Offs:** Outline the pros, cons, blast radius, and migration effort for each option.

### Step 4: Await Explicit User Instruction Before Coding
- **NEVER unilaterally jump into writing code or applying patches.**
- Present the options clearly to the user:
  > *"We have investigated the root cause of this failure. Here are the 2 viable approaches to resolve it cleanly. How would you like us to proceed?"*
- Wait for the user to select or instruct the desired resolution path before implementing any change.

---

## 4. Enforcement & Quality Gates

1. **Pre-Commit Verification:** Every change must prove that fixes were applied to the root cause (data, prompt design, schema, or system contract) rather than local heuristic patches.
2. **Zero-Mock Policy:** Code reviews must verify that no synthetic stubs or fallback dictionaries were introduced.
3. **Spec Synchronization:** Any structural change must be documented in the corresponding SDD in `specs/features/` and recorded in `specs/plan/`.
