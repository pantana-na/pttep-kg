# Rule: Google Agent Development Kit (ADK) & Gemini Enterprise Agent Platform Standard

## Core Mandate
All conversational AI agents, autonomous decision systems, and tool registries developed in this repository **MUST strictly adhere to the official Google Agent Development Kit (`google-adk`) standards** and execute on the **Gemini Enterprise Agent Platform (`agent_runtime`)**.

Direct, unmanaged LLM orchestration scripts without ADK agent encapsulation are strictly prohibited for production runtime. All agent reasoning must be decoupled from the frontend, deploying to the managed Agent Platform runtime while the web application serves as a thin streaming proxy.

---

## 1. Google ADK Architectural Directives

1. **Standard Agent Hierarchy:**
   - **Root Agent:** A root `google.adk.agents.Agent` or `LlmAgent` must serve as the primary conversational coordinator and router.
   - **Specialized Subagents & Tools:** Functional capabilities (Retrieval, Safety Facilitation, Database Mutations, Document Ingestion) must be modularized into discrete ADK `Agent` instances or declared as typed `FunctionTool` callables.
   - **ADK App Container:** All agents must be registered within a `google.adk.apps.App(root_agent=..., name=...)` exported in the standard agent package (`app/agent.py`).

2. **Strongly Typed ADK FunctionTools:**
   - All tools interacting with external systems (Databases, Knowledge Catalogs, Object Storage, External APIs) must be registered as ADK tools using type-annotated Python callables with comprehensive Google-style docstrings, or wrapped using `google.adk.tools.FunctionTool`.
   - Tool docstrings must explicitly define:
     - Clear parameter descriptions and types.
     - **"When to use"** scenarios with concrete example queries.
     - **"When NOT to use"** negative constraints to prevent tool miscalling and overlapping scope.
   - Tool arguments and return types must use Python type hints and Pydantic models.

3. **Inline Security via ADK Callbacks:**
   - Security guardrails (e.g. Google Cloud Model Armor) must be wired into the ADK lifecycle via `before_agent_callback` or `before_model_callback`.
   - Any prompt flagged by Model Armor (`filterMatchState == "MATCH_FOUND"`) must abort model reasoning immediately with zero tool invocations.

4. **Session & Memory Management:**
   - Production session state must use managed storage (`--session_service_uri agentengine://...` or standard ADK in-memory/database session stores).
   - Clarification states and user working memory must be preserved within the ADK Context / Session State across multi-turn dialogues.

---

## 2. Live Environment Agent Evaluation (`agents-cli eval`)

Agent quality, reasoning fidelity, and trajectory correctness must be continuously verified using the official **Google Agents CLI (`agents-cli eval`)**.

### 2.1 Live Environment Evaluation Mandate
- When initiating agent evaluations, tests **MUST run against the live environment** (`agents-cli eval run` connecting to live database instances, knowledge catalogs, and live agent runtime backends).
- Offline mocks, synthetic hardcoded stubs, or simulated shortcuts are prohibited during formal agent evaluation, ensuring that trajectory execution, latency, and tool contracts reflect real-world operational truth.

### 2.2 Recommended Comprehensive Evaluation Criteria & Metrics
All evaluation suites must assess agent trajectories across the following six core dimensions:

1. **Tool Trajectory & Selection Accuracy (Target: $\ge 95\%$):**
   - **Precision & Recall:** Did the agent select the precise tool(s) required by the inquiry without calling extraneous tools?
   - **Parameter Fidelity:** Were tool arguments correctly extracted, typed, and normalized against live database identifiers?
   - **Trajectory Exact Match:** In multi-step workflows, did tool execution follow the required engineering sequence?

2. **Groundedness & Context Faithfulness (Target: 1.000 / 100%):**
   - Verifies that 100% of facts, parameters, operating limits, and citations in the agent's synthesized output are strictly derived from the tool responses retrieved from live databases.
   - **Zero Hallucination / Zero Speculation:** Any claim not substantiated by retrieved tool data fails the evaluation.

3. **Negative Constraint Adherence (Target: 100%):**
   - Explicitly evaluates that prohibited tools are **NEVER** called for excluded inquiry types (e.g., verifying that unstructured document readers are never called for structured inventory counts, and vice versa).

4. **Security & Guardrail Efficacy (Target: 100%):**
   - Interception of adversarial attacks, prompt injections, and jailbreaks at the pre-flight callback, verifying 100% block rate and zero downstream tool execution on unsafe prompts.

5. **Ambiguity Resolution & Human-in-the-Loop (HITL) Clarification Rate (Target: 100%):**
   - Verifies that ambiguous or generic queries (e.g. "pump", "heater") consistently trigger `clarification_requested` with live candidate options rather than arbitrary guesses.

6. **Trajectory Efficiency & Step Bounds:**
   - Step count must not exceed optimal bounds (e.g. maximum 1–2 tool hops for single-entity inquiries).
   - End-to-end wall-clock latency must remain within production SLA limits.

### 2.3 Comprehensive Evaluation Dataset Standard
Evaluation datasets (`evals/datasets/*.jsonl`) must be comprehensive and representative across all operational domains:
- **Broad Entity Coverage:** Golden datasets must cover all plant sections, equipment categories, and instrument types (not just a single example asset).
- **Diverse Query Types:** Must test happy paths, edge cases, multi-hop traversals, boundary violations, negative constraints, ambiguous prompts, and adversarial security attacks.
- **Golden Trajectories:** Each test case must specify expected tool calls, required arguments, and reference grounded outputs.

### 2.4 Strict Prohibition: Zero Hardcoded Logic on Failed Evals
- **IF AGENT EVALUATION FAILS, NEVER ATTEMPT TO PASS IT BY HARDCODING AGENT LOGIC.**
- Strictly prohibited:
  - Adding `if prompt == "..."` or regex heuristics to force the expected tool or answer.
  - Hardcoding static candidate lists or fallback values into tool functions.
  - Weakening eval criteria or deleting failing test cases to artificially inflate metrics.
- **Mandated Action on Eval Failure:**
  - Investigate the root cause in prompt instructions, tool docstrings, database records, or model temperature.
  - Follow the **Root Cause Investigation & Zero Quick-Patch Rule** (`_agents/rules/root_cause_investigation_and_zero_quick_patch.md`).

---

## 3. Deployment & Lifecycle Management

1. **Project Manifest (`agents-cli-manifest.yaml`):**
   - The repository root must maintain an accurate `agents-cli-manifest.yaml` specifying:
     - `name`: Normalized lowercase hyphenated agent name.
     - `agent_directory`: Directory containing `agent.py` and `app`.
     - `region`: Google Cloud region (`asia-southeast1`).
     - `deployment_target`: `agent_runtime` (Gemini Enterprise Agent Platform) or `cloud_run`.
     - `base_template`: `adk`.

2. **Deployment via `agents-cli deploy`:**
   - Production deployments must be executable via:
     ```bash
     agents-cli deploy --deployment-target agent_runtime --region asia-southeast1
     ```
   - Automated deployment scripts (`scripts/deploy.sh`) must integrate with `agents-cli`.

---

## 4. Enforcement & Verification

- Pull requests introducing agent logic without ADK `Agent` encapsulation will be rejected.
- All new tools must have unit tests verifying tool schema reflection and deterministic execution.
- Property-based tests must verify that ADK agents maintain safety invariants across fuzzed inputs.
- Agent evaluations must run against the live environment and achieve $\ge 95\%$ trajectory precision and 1.000 groundedness.
