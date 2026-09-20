# Rule: Google Agent Development Kit (ADK) & Gemini Enterprise Agent Platform Mandate

## Core Mandate
All conversational AI agents, autonomous decision systems, and tool registries developed in this repository **MUST strictly adhere to the official Google Agent Development Kit (`google-adk`) standards** and execute on the **Gemini Enterprise Agent Platform (Agent Runtime)**.

Direct, unmanaged LLM orchestration scripts without ADK agent encapsulation are prohibited for production runtime.

---

## 1. Google ADK Architectural Directives

1. **Standard Agent Hierarchy:**
   - **Root Agent:** A root `google.adk.agents.Agent` or `LlmAgent` must serve as the primary conversational coordinator and router.
   - **Specialized Subagents:** Functional capabilities (e.g. Retrieval, HAZOP Analysis, Database Mutation, Document Parsing) must be modularized into discrete ADK `Agent` instances declared as `sub_agents` or invoked via `AgentTool` / `transfer_to_agent`.
   - **ADK App Container:** All agents must be registered within a `google.adk.apps.App(root_agent=..., name=...)` exported in the standard agent package (`app/agent.py`).

2. **Strongly Typed ADK FunctionTools:**
   - All tools interacting with external systems (Cloud Spanner, Dataplex, Cloud Storage, APIs) must be registered as ADK tools using type-annotated Python callables with Google-style docstrings, or wrapped using `google.adk.tools.FunctionTool`.
   - Tool arguments and return types must use Python type hints and Pydantic models.

3. **Inline Security via ADK Callbacks:**
   - Security guardrails (Google Cloud Model Armor) must be wired into the ADK lifecycle via `before_agent_callback` or `before_model_callback`.
   - Any prompt flagged by Model Armor (`filterMatchState == "MATCH_FOUND"`) must abort model reasoning immediately with zero tool invocations.

4. **Session & Memory Management:**
   - Production session state must use managed storage (`--session_service_uri agentengine://...` or standard ADK in-memory/database session stores).
   - Clarification states and user working memory must be preserved within the ADK Context / Session State.

---

## 2. Gemini Enterprise Agent Platform & `agents-cli` Lifecycle

All agent projects must support the complete **Agents CLI (`agents-cli`)** lifecycle:

1. **Project Manifest (`agents-cli-manifest.yaml`):**
   - The repository root must maintain an accurate `agents-cli-manifest.yaml` specifying:
     - `name`: Normalized lowercase hyphenated agent name.
     - `agent_directory`: Directory containing `agent.py` and `app`.
     - `region`: Google Cloud region (`asia-southeast1`).
     - `deployment_target`: `agent_runtime` (Gemini Enterprise Agent Platform) or `cloud_run`.
     - `base_template`: `adk`.

2. **Evaluation via `agents-cli eval`:**
   - Agent quality, safety, and trajectory adherence must be evaluated using `agents-cli eval run` or `adk eval`.
   - Evaluation datasets (`evals/datasets/*.jsonl`) must test groundedness, safety compliance, and tool precision ($\ge 90\%$).

3. **Deployment via `agents-cli deploy`:**
   - Production deployments must be executable via:
     ```bash
     agents-cli deploy --deployment-target agent_runtime --region asia-southeast1
     ```
     or containerized Cloud Run:
     ```bash
     agents-cli deploy --deployment-target cloud_run --region asia-southeast1
     ```
   - Automated deployment scripts (`scripts/deploy.sh`) must integrate with `agents-cli`.

4. **Local Development & Interactive Debugging:**
   - Support `adk run app "query"` for single-turn testing.
   - Support `agents-cli playground` or `adk web` for local graphical inspection.

---

## 3. Enforcement & Verification

- Pull requests introducing agent logic without ADK `Agent` encapsulation will be rejected.
- All new tools must have unit tests verifying tool schema reflection and deterministic execution.
- Property-based tests must verify that ADK agents maintain safety invariants across fuzzed inputs.
