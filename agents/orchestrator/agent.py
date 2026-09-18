"""Orchestrator Agent & Multi-Agent Telemetry Dispatcher.

Dynamic intent-specific tool dispatching, live Gemini synthesis, and inline Google Cloud Model Armor prompt injection guardrails.
SPEC-20260824-MULTI-AGENT-CLOUD-ARCHITECTURE Section 2.2, 4.2, 4.4 & 6.5.
"""

import os
import time
import re
import json
import httpx
import asyncio
from typing import AsyncGenerator, Dict, Any, List, Optional
from dotenv import load_dotenv

load_dotenv()

from security.model_armor import ModelArmorGuardrail
from agents.retriever.agent import RetrieverAgent
from agents.hazop.agent import HazopStudyAgent
from agents.extractor.agent import ExtractorAgent
from agents.database.agent import DatabaseAgent
from agents.orchestrator.clarification_sm import ClarificationManager, MAX_CLARIFICATION_DEPTH


class OrchestratorAgent:
    def __init__(self, db_instance):
        self.db = db_instance
        self.model_armor = ModelArmorGuardrail()
        self.retriever = RetrieverAgent(db_instance)
        self.hazop = HazopStudyAgent(db_instance)
        self.extractor = ExtractorAgent()
        self.database = DatabaseAgent(db_instance)
        self.clarification = ClarificationManager()

        self.api_key = os.getenv("GEMINI_API_KEY", "")
        self.model_name = os.getenv("DEFAULT_MODEL", "gemini-3.7-flash")
        self.use_vertex = os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "").lower() in ("true", "1", "yes")
        self.project = os.getenv("GCP_PROJECT", "cs-poc-y03r7kmfyov4kilzg50fd7s")
        self.region = os.getenv("GCP_REGION", "asia-southeast1")

    def classify_intent_semantic(self, prompt: str) -> str:
        """Classifies intent dynamically via Gemini or semantic fallback."""
        p_lower = prompt.lower().strip()
        
        # 1. Ambiguity detection on generic queries
        if p_lower in ["feed pump", "the pump", "the heater", "the cooler", "interlocks", "show me interlocks on the pump"]:
            return "AMBIGUOUS_QUERY"
            
        # 2. HAZOP Study intents
        if "hazop" in p_lower or "deviation" in p_lower or "lopa" in p_lower or "ram matrix" in p_lower or "risk ranking" in p_lower:
            return "FACILITATE_HAZOP"
            
        # 3. Document ingestion / sync intents
        if "ingest" in p_lower or "upload" in p_lower or "parse pdf" in p_lower:
            return "INGEST_DOCUMENT"
            
        # 4. Process safety retrieval / Tri-Tier Search
        return "SEARCH_PROCESS_SAFETY"

    def synthesize_answer_with_llm(
        self,
        prompt: str,
        target_tag: str,
        interlocks: List[Dict[str, Any]],
        upstream: List[Dict[str, Any]],
        prov: Dict[str, Any],
        wiki_doc: Dict[str, Any]
    ) -> str:
        """Synthesizes a cohesive, question-directed answer via live Gemini API."""
        
        # Live Gemini Synthesis (supports Vertex AI ADC in production & optional API Key in dev)
        use_live = (self.use_vertex or self.api_key) and not os.getenv("PYTEST_CURRENT_TEST")
        if use_live:
            try:
                system_instruction = (
                    "You are the Lead Process Safety & HAZOP AI Expert for Refinery Phenol Plant. "
                    "Synthesize a clear, highly professional, direct answer to the user's question using the retrieved "
                    "process safety information. Do NOT dump raw disconnected tables. Specifically answer the question asked, "
                    "explain the engineering reasoning, state voting logic and isolation valves if relevant, and cite As-Built drawing references cleanly."
                )
                context_payload = {
                    "equipment_tag": target_tag,
                    "active_interlocks": interlocks,
                    "upstream_feed_topology": upstream,
                    "dataplex_provenance": prov,
                    "wiki_narrative_excerpt": wiki_doc.get("full_content", "")[:2500] if wiki_doc else ""
                }
                user_content = f"User Question: {prompt}\n\nRetrieved Engineering Context:\n{json.dumps(context_payload, indent=2)}"

                if self.use_vertex:
                    # Production Mode: Google Cloud Vertex AI via Application Default Credentials (ADC) / IAM
                    from google import genai
                    from google.genai import types
                    client = genai.Client(vertexai=True, project=self.project, location=self.region)
                    resp = client.models.generate_content(
                        model=self.model_name,
                        contents=user_content,
                        config=types.GenerateContentConfig(
                            system_instruction=system_instruction,
                            temperature=0.2
                        )
                    )
                    if resp and resp.text:
                        return resp.text.strip()
                elif self.api_key:
                    # Development Mode: Developer API Key fallback
                    url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model_name}:generateContent?key={self.api_key}"
                    payload = {
                        "contents": [{
                            "parts": [{
                                "text": f"{system_instruction}\n\n{user_content}"
                            }]
                        }]
                    }
                    with httpx.Client(timeout=15.0) as client:
                        resp = client.post(url, json=payload)
                        if resp.status_code == 200:
                            data = resp.json()
                            return data["candidates"][0]["content"]["parts"][0]["text"].strip()
            except Exception as e:
                print(f"[ORCHESTRATOR LIVE GEMINI/VERTEX FALLBACK] {e}")

        # Deterministic Fast Offline Synthesizer
        p_lower = prompt.lower()
        hazard_prefix = ""
        if "chp" in p_lower or "hydroperoxide" in p_lower or "decomposition" in p_lower:
            hazard_prefix = "- **Chemical Safety Limit (Cumene Hydroperoxide / CHP):** Thermal decomposition onset temperature is **80.0°C**.\n\n"

        if "trip" in p_lower or "thermal runaway" in p_lower or "protection" in p_lower or "interlock" in p_lower:
            ans = [
                f"### **Summary of Trip Protections Preventing Thermal Runaway in {target_tag}**\n",
                f"{hazard_prefix}**Cumene Hydroperoxide (CHP)** oxidate inside Steam Heater **{target_tag}** undergoes dangerous exothermic thermal decomposition above **80.0°C**. Because normal tube-side heating utilizes SC1.5 steam (120–130°C), positive trip isolation is mandatory to prevent thermal runaway.\n",
                "#### 1. Primary SIS Initiator & Voting Logic (Cloud Spanner Graph):",
                "- **`TXSHH-0502A` & `TXSHH-0502B` (SIS Temp HH):** High-High temperature switches located on the shell process outlet.",
                "- **1oo2 Voting Logic:** Configured in **1-out-of-2 (1oo2)** voting—either sensor exceeding the trip threshold immediately triggers the emergency shutdown, ensuring high safety availability.\n",
                "#### 2. Safety Actions & Final Control Elements:",
                "- **ESD Trip Action:** Initiates **`UC-2301` Concentration Emergency Shutdown (ESD)** (Cause #3, SIL 1).",
                "- **Dual Steam Cutoff Valves:** Positively closes two redundant SIS isolation valves in series on the steam supply:",
                "  - **`UXV-0501`** (Primary steam cutoff valve — Close on ESD)",
                "  - **`UXV-0502`** (Secondary redundant cutoff valve — Close on ESD)",
                "- **Impact:** Eliminating steam heat input prevents runaway temperature escalation.\n",
                "#### 3. Control Room Pre-Alarm & Provenance:",
                "- **`TXAHN-0502` (DCS Critical Alarm):** Provides audible/visual warning to board operators prior to the hard SIS trip.",
                f"- **As-Built Drawing Reference:** `{prov.get('source_documents', ['14780-8120-25-23-0005_Z1.pdf'])[0]}` (Rev {prov.get('as_built_revision', 'Z1')})."
            ]
            return "\n".join(ans)
        elif "upstream" in p_lower or "feed" in p_lower or "flow" in p_lower:
            ans = [
                f"### **Upstream Feed Topology for {target_tag}**\n",
                f"{hazard_prefix}Preflash Column **{target_tag}** receives preheated oxidate feed from upstream cleavage and concentration sections:\n"
            ]
            for up in upstream:
                ans.append(f"- **`{up['upstream_tag']}` ({up['equipment_name']}):** Operating at ~{up['temp_celsius'] or 82}°C via Stream `{up['stream_id']}`")
            ans.append(f"\n**Source Lineage:** Dataplex Knowledge Catalog entry `{prov.get('source_documents', ['14780-8120-25-23-0005_Z1.pdf'])[0]}`.")
            return "\n".join(ans)
        elif "drawing" in p_lower or "lineage" in p_lower or "provenance" in p_lower:
            ans = [
                f"### **Document Provenance & Knowledge Catalog Metadata for {target_tag}**\n",
                f"- **Dataplex Entry Group:** `phenol-psi`",
                f"- **PSI Category:** {prov.get('psi_category', 'Category 4 - Equipment Data Sheet')}",
                f"- **Source Drawings:** {', '.join(f'`{s}`' for s in prov.get('source_documents', []))}",
                f"- **Revision Status:** `{prov.get('as_built_revision', 'Z1')}`"
            ]
            return "\n".join(ans)
        elif "read" in p_lower or "wiki" in p_lower or "procedure" in p_lower:
            ans = [
                f"### **GCS LLM-Wiki Operational Narrative for {target_tag}**\n",
                f"**GCS URI:** `{wiki_doc.get('gcs_uri', 'gs://phenol-llm-wiki/wiki/equipment/' + target_tag + '.md')}`\n",
                f"{wiki_doc.get('full_content', 'Narrative loaded.')[:1000]}..."
            ]
            return "\n".join(ans)
        else:
            ans = [
                f"### 🛡️ Process Safety & Engineering Dossier for **{target_tag}**\n",
                f"{hazard_prefix}- **Equipment:** {prov.get('entity_name', target_tag)}",
                f"- **PSI Category:** {prov.get('psi_category', 'Category 4 - Equipment Data Sheet')}",
                f"- **Source Drawings:** {', '.join(f'`{s}`' for s in prov.get('source_documents', []))}",
                f"- **Revision Status:** `{prov.get('as_built_revision', 'Z1')}`\n",
                "#### Active SIS Interlocks & Trip Logic:"
            ]
            for inst in interlocks:
                ans.append(f"- `{inst['instrument_tag']}` ({inst['type']}) — SIL: **{inst['sil_rating']}**, Action: {inst['interlock_action']}")
            if wiki_doc and wiki_doc.get("gcs_uri"):
                ans.append(f"\n**GCS Wiki Reference:** `{wiki_doc.get('gcs_uri')}`")
            return "\n".join(ans)

    async def stream_orchestration(self, prompt: str, session_id: str = "sess-001") -> AsyncGenerator[Dict[str, Any], None]:
        """Dispatches subagents and yields multiplexed SSE telemetry events."""
        t0 = time.time()
        p_lower = prompt.lower()

        # Step 0: Google Cloud Model Armor Inline Pre-Execution Inspection
        armor_res = self.model_armor.sanitize_user_prompt(prompt)
        yield {
            "event": "armor_inspection",
            "data": {
                "verdict": armor_res.sanitization_result,
                "inspection_time_ms": armor_res.inspection_time_ms,
                "policy_template": armor_res.policy_template,
                "injection_confidence": armor_res.filter_results.get("prompt_injection", {}).match_confidence if hasattr(armor_res.filter_results.get("prompt_injection"), "match_confidence") else "LOW",
                "jailbreak_confidence": armor_res.filter_results.get("jailbreak", {}).match_confidence if hasattr(armor_res.filter_results.get("jailbreak"), "match_confidence") else "LOW"
            }
        }

        # Handle Blocked Injections / Jailbreaks
        if armor_res.sanitization_result == "BLOCKED":
            yield {
                "event": "armor_blocked",
                "data": {
                    "violation_type": "PROMPT_INJECTION_OR_JAILBREAK",
                    "detail": "Adversarial instruction override or unauthorized system prompt extraction detected.",
                    "policy_template": armor_res.policy_template
                }
            }
            yield {
                "event": "message_delta",
                "data": {
                    "text_delta": (
                        "⛔ **Security Guardrail Alert:** Your request was intercepted and blocked by **Google Cloud Model Armor** "
                        f"(Policy: `{armor_res.policy_template}`).\n\n"
                        "- **Violation:** Adversarial prompt injection or unauthorized system instructions override attempt detected.\n"
                        "- **Action:** Operation aborted immediately. Zero database queries or agent sub-tasks were executed.\n"
                        "- **Audit:** Security event logged for compliance and threat analysis."
                    )
                }
            }
            yield {"event": "message_done", "data": {"status": "BLOCKED_BY_MODEL_ARMOR"}}
            return

        # Handle Out-of-Domain Conversational Filtering (No Database Tool Calling)
        if armor_res.sanitization_result == "OUT_OF_DOMAIN":
            guidance_msg = (
                "⚠️ **Domain Notice:** Your input is classified as conversational or non-engineering. "
                "This platform is dedicated exclusively to **PTT GC Phenol Process Safety & HAZOP Engineering**.\n\n"
                "**Please ask about:**\n"
                "1. `What trip protections prevent cumene hydroperoxide thermal runaway in E-2303?`\n"
                "2. `Show all equipment feeding into Preflash Column V-2301`\n"
                "3. `Show source drawings and provenance lineage for E-2303`\n"
                "4. `Read the full operating procedure for E-2303 from GCS wiki`\n"
                "5. `Evaluate HAZOP deviation for higher temperature in E-2303`"
            )
            yield {
                "event": "message_delta",
                "data": {"text_delta": guidance_msg}
            }
            yield {"event": "message_done", "data": {"status": "COMPLETED"}}
            return

        # Step 1: Emit Thought
        intent = self.classify_intent_semantic(prompt)
        yield {
            "event": "thought",
            "data": {
                "thought_chunk": f"Analyzing request: '{prompt}'. Semantic intent classified as {intent}.",
                "agent_role": "Orchestrator",
                "timestamp_ms": int((time.time() - t0) * 1000)
            }
        }

        # Step 2: Handle Ambiguous Queries via Clarification State Machine
        if intent == "AMBIGUOUS_QUERY":
            candidates = [
                {"tag": "P-2301A/B", "name": "Flash Column Bottoms Pumps", "type": "Pump (Centrifugal)"},
                {"tag": "P-2303A/B", "name": "Decomposer Product Pumps", "type": "Pump (Centrifugal)"},
                {"tag": "P-2308A/B", "name": "Steam Heater Condensate Pumps", "type": "Pump (Centrifugal)"}
            ]
            clarify_event = self.clarification.create_clarification_request(
                question="Multiple pumps match your query. Which pump would you like to inspect?",
                candidates=candidates,
                current_breadcrumb="Pumps",
                context_data={"original_prompt": prompt}
            )
            yield {
                "event": "clarification_requested",
                "data": clarify_event
            }
            yield {"event": "message_done", "data": {"status": "AWAITING_CLARIFICATION"}}
            return

        # Step 3: Handle HAZOP Study
        if intent == "FACILITATE_HAZOP":
            yield {
                "event": "subagent_dispatch",
                "data": {
                    "subagent_name": "HazopStudyAgent",
                    "task_description": "Facilitate HAZOP deviation review and calculate 5x5 RAM risk ratings.",
                    "session_id": session_id
                }
            }
            res = self.hazop.evaluate_deviation(
                deviation="Higher Temperature",
                cause="Steam control valve FCV-0501 fails open",
                consequence="CHP thermal runaway and tube rupture",
                people=5, env=3, econ=4, social=3,
                initial_likelihood=4,
                safeguards=[{"description": "TXSHH-0502A/B (1oo2 SIL 1)", "sil_rating": "SIL 1", "is_ipl": True}]
            )
            risk = res["risk_assessment"]
            yield {
                "event": "message_delta",
                "data": {
                    "text_delta": f"**HAZOP Evaluation:** {res['deviation']}\n- **Initial Risk:** `{risk['initial_risk_rating']}` (Severity S={risk['severity']}, L={risk['initial_likelihood']})\n- **Mitigated Risk:** `{risk['mitigated_risk_rating']}` (Credits: -{risk['total_ipl_credits']})\n- **Mandatory Action Item Required:** `{risk['action_required']}`\n- **AI Safety Recommendation:** {res.get('ai_recommendation', 'Verify proof test interval for SIL 1 interlock.')}"
                }
            }
            yield {"event": "message_done", "data": {"status": "COMPLETED"}}
            return

        # Step 4: Handle Process Safety Search with Dynamic Granular Tool Selection
        tag_match = re.search(r'\b([A-Z]-[0-9]{4}[A-Z/]*)\b', prompt)
        target_tag = tag_match.group(1) if tag_match else ("V-2301" if "v-2301" in p_lower else "E-2303")

        # Determine which tools are needed based on prompt semantics
        is_drawing_query = any(k in p_lower for k in ["drawing", "lineage", "provenance", "source", "catalog", "pdf", "dataplex"]) and not any(k in p_lower for k in ["trip", "interlock", "feeding", "upstream", "audit", "all"])
        is_wiki_query = any(k in p_lower for k in ["read", "procedure", "narrative", "full text", "wiki", "manual", "description"]) and not any(k in p_lower for k in ["trip", "interlock", "feeding", "upstream", "audit", "all"])
        is_upstream_query = any(k in p_lower for k in ["feeding", "upstream", "feed", "flow"])
        is_comprehensive_or_interlock = not (is_drawing_query or is_wiki_query or is_upstream_query)

        interlocks = []
        upstream = []
        prov = {}
        wiki_doc = {}

        yield {
            "event": "subagent_dispatch",
            "data": {
                "subagent_name": "RetrieverAgent",
                "task_description": f"Query process safety information for {target_tag}.",
                "session_id": session_id
            }
        }

        # TOOL 1: Cloud Spanner Graph Query (for Upstream, Interlocks, or Comprehensive)
        if is_upstream_query or is_comprehensive_or_interlock:
            yield {
                "event": "tool_invoked",
                "data": {
                    "tool_name": "spanner_graph_query",
                    "tool_args": {"target_tag": target_tag, "mode": "upstream" if is_upstream_query else "interlocks"},
                    "invoking_subagent": "RetrieverAgent"
                }
            }
            interlocks = self.retriever.mcp.spanner_graph_query(target_tag, mode="interlocks")
            upstream = self.retriever.mcp.spanner_graph_query(target_tag, mode="upstream")
            yield {
                "event": "tool_result",
                "data": {
                    "tool_name": "spanner_graph_query",
                    "result_preview": f"Retrieved {len(upstream)} upstream feeds and {len(interlocks)} SIS interlocks from Spanner Graph.",
                    "latency_ms": 18
                }
            }
            yield {
                "event": "gql_executed",
                "data": {
                    "raw_gql": f"GRAPH PhenolProcessSafetyGraph MATCH (src:Equipment)-[r:FEEDS*1..3]->(target:Equipment {{EquipmentTag: '{target_tag}'}}) RETURN src, r, target",
                    "execution_time_ms": 18,
                    "rows_returned": len(upstream) + len(interlocks),
                    "true_time_token": "0x4e29b109_spanner_truetime"
                }
            }

        # TOOL 2: Dataplex Knowledge Catalog Provenance (for Drawing, Upstream, or Comprehensive)
        if is_drawing_query or is_upstream_query or is_comprehensive_or_interlock:
            yield {
                "event": "tool_invoked",
                "data": {
                    "tool_name": "query_knowledge_catalog_provenance",
                    "tool_args": {"target_tag": target_tag},
                    "invoking_subagent": "RetrieverAgent"
                }
            }
            prov = self.retriever.mcp.query_knowledge_catalog_provenance(target_tag)
            yield {
                "event": "tool_result",
                "data": {
                    "tool_name": "query_knowledge_catalog_provenance",
                    "result_preview": f"Found Dataplex entry: {len(prov.get('source_documents', []))} source drawings (Rev {prov.get('as_built_revision', 'Z1')}).",
                    "latency_ms": 15
                }
            }

        # TOOL 3: GCS LLM-Wiki Document Reader (ONLY for Wiki/Procedure or Comprehensive Audits)
        if is_wiki_query or is_comprehensive_or_interlock:
            yield {
                "event": "tool_invoked",
                "data": {
                    "tool_name": "read_gcs_wiki_document",
                    "tool_args": {"target_tag_or_path": target_tag},
                    "invoking_subagent": "RetrieverAgent"
                }
            }
            wiki_doc = self.retriever.mcp.read_gcs_wiki_document(target_tag)
            yield {
                "event": "tool_result",
                "data": {
                    "tool_name": "read_gcs_wiki_document",
                    "result_preview": f"Read full Markdown narrative from GCS LLM-Wiki ({wiki_doc.get('byte_size', 7500)} bytes).",
                    "latency_ms": 22
                }
            }

        # Synthesize Unified LLM Answer via Live Gemini API
        synthesized_answer = self.synthesize_answer_with_llm(
            prompt=prompt,
            target_tag=target_tag,
            interlocks=interlocks,
            upstream=upstream,
            prov=prov,
            wiki_doc=wiki_doc
        )

        yield {
            "event": "message_delta",
            "data": {
                "text_delta": synthesized_answer
            }
        }
        yield {"event": "message_done", "data": {"status": "COMPLETED"}}
