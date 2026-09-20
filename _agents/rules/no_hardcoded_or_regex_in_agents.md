# Rule: Mandatory Model-Driven Reasoning & Zero Hardcoded / Regex Agent Logic

## Core Directive
**AI agents must rely on cognitive model reasoning, structured tool execution (`FunctionTool`), semantic vector retrieval, and live database queries to make decisions.**

Under NO circumstances may an AI agent or orchestrator rely on hardcoded keyword lists, regular expressions, or static fallback heuristics to classify user intents, route requests, extract entities, or determine safety actions.

---

## 1. Prohibited Anti-Patterns in AI Agents

1. **Regex Intent Classification:**
   - ❌ **STRICTLY FORBIDDEN:** `if re.search(r"hazop|deviation", prompt): return "FACILITATE_HAZOP"`
   - ❌ **STRICTLY FORBIDDEN:** `if any(k in prompt.lower() for k in ["pump", "heater"]): ...`
   - ✅ **MANDATED:** Call Gemini LLM (`classify_intent_with_model`) using a structured JSON schema to categorize intent based on conversational context and engineering meaning.

2. **Hardcoded Tag Fallbacks:**
   - ❌ **STRICTLY FORBIDDEN:** `target_tag = tag_match or "E-2303"`
   - ✅ **MANDATED:** Use model entity extraction or prompt the user for clarification if the target equipment is missing or ambiguous.

3. **Incomplete / Hardcoded Clarification Choices:**
   - ❌ **STRICTLY FORBIDDEN:** Hardcoding a static array of 2–3 options (e.g. `candidates = [{"tag": "P-2301A/B"}, ...]`).
   - ✅ **MANDATED:** Dynamically query the database (`db.equipment`) to retrieve ALL matching equipment in the unit/plant, ensuring the user is presented with every valid candidate.

4. **Hardcoded Engineering Answers:**
   - ❌ **STRICTLY FORBIDDEN:** Generating synthetic text answers via hardcoded string interpolation templates.
   - ✅ **MANDATED:** Ground dynamic synthesis on retrieved Cloud Spanner Graph records, Dataplex metadata, and GCS LLM-Wiki text using Vertex AI Gemini.

---

## 2. Canonical Intent Topology
All intent classification must strictly map queries into one of these three canonical classes:
1. **`PROCESS_SAFETY_QA`:** General Q&A on process safety information (PSI), equipment design data, operating limits, instrument interlocks, trip setpoints, voting logic, upstream/downstream flow tracing, and drawing lineage. Dispatches `RetrieverAgent` tools.
2. **`FACILITATE_HAZOP`:** Structured HAZOP review, parameter deviation evaluation, consequence analysis, 5x5 RAM initial/mitigated risk assessment, and safety recommendation generation. Dispatches `HazopAgent` tools.
3. **`OTHERS`:** Any request outside process safety Q&A or HAZOP facilitation. The agent must clearly explain its specialized capabilities and provide helpful example questions.

---

## 3. Active Agent Boundaries
To ensure clean isolation and maintainability, the active multi-agent system comprises:
- **`OrchestratorAgent` (Root):** Receives user queries, applies Model Armor pre-flight security, executes model-driven intent classification, and coordinates subagents.
- **`RetrieverAgent` (Subagent):** Executes Tri-Hybrid retrieval across Spanner Graph, 768-dim embeddings, keyword search, Dataplex Knowledge Catalog, and GCS LLM-Wiki.
- **`HazopAgent` (Subagent):** Facilitates 9-step study lifecycle, 5x5 RAM calculations, and IPL safeguard evaluations.
- *Note:* `DatabaseAgent` and `ExtractorAgent` are inactive/disabled. Direct database access is provided through ADK `FunctionTool` bindings.

---

## 4. Enforcement & Testing
1. **Code Reviews:** Any PR or change introducing `re.search`, `re.match`, or hardcoded if/else keyword heuristics to determine agent routing will be rejected.
2. **Property-Based Testing (PBT):** Property tests must verify that intent classification outputs strictly belong to `{PROCESS_SAFETY_QA, FACILITATE_HAZOP, OTHERS}` across arbitrary fuzz inputs.
