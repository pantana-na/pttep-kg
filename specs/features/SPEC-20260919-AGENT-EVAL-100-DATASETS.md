# SPEC-20260919-AGENT-EVAL-100-DATASETS: Comprehensive 100+ Agent Evaluation Benchmark Suite

**Document ID:** `SPEC-20260919-AGENT-EVAL-100-DATASETS`  
**Status:** APPROVED  
**Author(s):** Antigravity Agent & Core Architecture Team  
**Governed by:** `GEMINI.md` (Rules 1, 3, 4, 11, 12), `_agents/rules/spec_driven_development.md`, `_agents/rules/google_adk_and_agent_runtime.md`  
**Target Environment:** Non-Prod (`development`) & Prod (`production`)  
**Date:** September 19, 2026  

---

## 1. Problem Statement & Goals

### 1.1 Context & Background
The platform provides multi-tier process safety retrieval, 5x5 RAM risk evaluations, and Model Armor security guardrails for a Refinery Phenol Unit. Previously, the automated Agent Evaluation (`evals/datasets/phenol_safety_bench.jsonl` and `tests/eval/datasets/basic-dataset.json`) contained only 5 basic test scenarios. 

To ensure continuous regression testing, safety grounding, and production readiness across all engineering scenarios, the platform requires an exhaustive benchmark suite of at least 100 golden test cases directly derived from the **Master Test Prompts Suite** (`test_prompt/`).

### 1.2 Problem Statement
How do we generate, structure, and automate a comprehensive $\ge 100$ scenario evaluation dataset that rigorously validates:
1. Tri-tier process safety retrieval (Spanner Property Graph SIS trips, Dataplex P&ID drawing lineage, GCS LLM-Wiki operational procedures),
2. HAZOP study facilitation, 5x5 RAM risk rankings, and LOPA independent protection layer (IPL) credits across all process parameters (Flow, Temperature, Pressure, Level),
3. Human-in-the-loop (HITL) ambiguity resolution and candidate disambiguation across plant equipment,
4. Google Cloud Model Armor security guardrails (prompt injection, jailbreak, safety rating override defense, out-of-domain filtering), and
5. Multimodal document provenance and drawing revision tracking?

### 1.3 Goals
- **$\ge 100$ Test Scenarios:** Author 105 distinct, production-grade test cases categorized across the 5 Golden Prompt Suites.
- **Dual Format Support:**
  - `evals/datasets/phenol_safety_bench.jsonl` (used by `evals/run_evals.py` and `tests/test_agent_eval.py`).
  - `tests/eval/datasets/basic-dataset.json` (official Google ADK Agent Evaluation format).
- **Automated Multi-Tier Execution:** Enhance `evals/run_evals.py` to execute official ADK tools (`spanner_graph_query`, `spanner_keyword_search`, `spanner_vector_search`, `query_knowledge_catalog_provenance`, `read_gcs_wiki_document`, `evaluate_hazop_deviation`) and security guardrails (`before_agent_guardrail`).
- **Quality Gates:** 100% pass rate with average Groundedness score $\ge 0.90$ and 0 prohibited/hallucinated tags.

---

## 2. Benchmark Suite Category Distribution (105 Total Cases)

| Suite | Category Code | Description | Case Count |
|---|---|---|---|
| **Suite 1** | `PROCESS_SAFETY_TRI_TIER` | SIS trips, voting logic (1oo2, 2oo3), upstream feed flows, Dataplex certified drawings, GCS wiki narratives, and chemical kinetics. | **35** |
| **Suite 2** | `HAZOP_LOPA_RAM` | 5x5 RAM severity/likelihood evaluations across Flow, Temp, Press, and Level; IPL credits (SIL 1/2). | **25** |
| **Suite 3** | `HITL_CLARIFICATION` | Ambiguous equipment queries triggering token candidate searches (pumps, heaters, drums, columns, exchangers). | **15** |
| **Suite 4** | `SECURITY_MODEL_ARMOR` | Direct prompt injection, jailbreaks, developer prompt leaks, safety rating overrides, and out-of-domain filtering. | **15** |
| **Suite 5** | `DOC_PROVENANCE_MOC` | OEMS-005 PSI classification (P&ID, PFD, Data Sheet), revision control (`Rev Z1`), and drawing lineage. | **15** |
| **Total** | | | **105** |

---

## 3. Implementation Plan

- **Step 1:** Generate `evals/datasets/phenol_safety_bench.jsonl` with 105 structured JSONL records containing `eval_id`, `category`, `prompt`, `expected_intent`, `required_entities`, `prohibited_tags`, `ground_truth_facts`, and metadata.
- **Step 2:** Generate `tests/eval/datasets/basic-dataset.json` mirroring the 105 eval cases in Google ADK conversational schema.
- **Step 3:** Enhance `evals/run_evals.py` to route all categories to production ADK tools and Model Armor guardrails.
- **Step 4:** Execute `python evals/run_evals.py` and `pytest tests/test_agent_eval.py` to verify 100% pass rate.
- **Step 5:** Generate living progress report under `specs/plan/PROGRESS_REPORT_20260919_AGENT_EVAL_100_DATASETS.md`.
- **Step 6:** Ambiguity Clarification Prompt Directive in ADK Agent Instructions (`app/agent.py`):
  - Formalize human-in-the-loop (HITL) ambiguity resolution mandate in `ORCHESTRATOR_INSTRUCTION`.
  - When a query references generic equipment terms without exact tags, call `spanner_keyword_search`.
  - If multiple candidate equipment items match, immediately halt further tool execution, output `clarification_requested`, present candidate tags/names, and prompt the user to specify the target equipment.
  - Assert compliance in unit and evaluation tests.

