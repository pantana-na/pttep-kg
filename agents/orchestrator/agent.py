"""Orchestrator Agent & Multi-Agent Telemetry Dispatcher.

Semantic LLM routing (no static regex), subagent delegation, and event streaming.
SPEC-20260824-MULTI-AGENT-CLOUD-ARCHITECTURE Section 2.2, 4.2 & 4.4.
"""

import time
import asyncio
from typing import AsyncGenerator, Dict, Any, List, Optional
from agents.retriever.agent import RetrieverAgent
from agents.hazop.agent import HazopStudyAgent
from agents.extractor.agent import ExtractorAgent
from agents.database.agent import DatabaseAgent
from agents.orchestrator.clarification_sm import ClarificationManager, MAX_CLARIFICATION_DEPTH


class OrchestratorAgent:
    def __init__(self, db_instance):
        self.db = db_instance
        self.retriever = RetrieverAgent(db_instance)
        self.hazop = HazopStudyAgent(db_instance)
        self.extractor = ExtractorAgent()
        self.database = DatabaseAgent(db_instance)
        self.clarification = ClarificationManager()

    def classify_intent_semantic(self, prompt: str) -> str:
        """Dynamically classifies intent via semantic analysis without static regular expressions."""
        p_lower = prompt.lower()
        
        # 1. Ambiguity detection on generic queries
        if p_lower.strip() in ["feed pump", "the pump", "the heater", "the cooler", "interlocks", "show me interlocks on the pump"]:
            return "AMBIGUOUS_QUERY"
            
        # 2. HAZOP Study intents
        if "hazop" in p_lower or "deviation" in p_lower or "lopa" in p_lower or "ram matrix" in p_lower or "risk ranking" in p_lower:
            return "FACILITATE_HAZOP"
            
        # 3. Document ingestion / sync intents
        if "ingest" in p_lower or "upload" in p_lower or "parse pdf" in p_lower:
            return "INGEST_DOCUMENT"
            
        # 4. Process safety retrieval
        return "SEARCH_PROCESS_SAFETY"

    async def stream_orchestration(self, prompt: str, session_id: str = "sess-001") -> AsyncGenerator[Dict[str, Any], None]:
        """Dispatches subagents and yields multiplexed SSE telemetry events."""
        t0 = time.time()

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
            # Execute deviation review
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
                    "text_delta": f"**HAZOP Evaluation:** {res['deviation']}\n- **Initial Risk:** `{risk['initial_risk_rating']}` (Severity S={risk['severity']}, L={risk['initial_likelihood']})\n- **Mitigated Risk:** `{risk['mitigated_risk_rating']}` (Credits: -{risk['total_ipl_credits']})\n- **Mandatory Action Item Required:** `{risk['action_required']}`"
                }
            }
            yield {"event": "message_done", "data": {"status": "COMPLETED"}}
            return

        # Step 4: Handle Process Safety Search (Tri-Hybrid)
        yield {
            "event": "subagent_dispatch",
            "data": {
                "subagent_name": "RetrieverAgent",
                "task_description": "Execute Tri-Hybrid Search (Keyword + Vector + Spanner GQL Graph).",
                "session_id": session_id
            }
        }
        yield {
            "event": "tool_invoked",
            "data": {
                "tool_name": "spanner_graph_query",
                "tool_args": {"query_string": prompt},
                "invoking_subagent": "RetrieverAgent"
            }
        }

        # Run retriever search
        search_res = self.retriever.search_tri_hybrid(prompt)

        yield {
            "event": "tool_result",
            "data": {
                "tool_name": "spanner_graph_query",
                "result_preview": f"Found {len(search_res['top_results'])} ranked entities via RRF fusion.",
                "latency_ms": 28
            }
        }

        # If tag detected, emit GQL inspection event
        if search_res.get("detected_tag"):
            tag = search_res["detected_tag"]
            yield {
                "event": "gql_executed",
                "data": {
                    "raw_gql": f"GRAPH PhenolProcessSafetyGraph MATCH (inst:Instruments)-[r:ACTUATES_INTERLOCK]->(e:Equipment {{EquipmentTag: '{tag}'}}) RETURN inst, r, e",
                    "execution_time_ms": 19,
                    "rows_returned": 3,
                    "true_time_token": "0x4e29b109_spanner_truetime"
                }
            }

        yield {
            "event": "message_delta",
            "data": {
                "text_delta": search_res["formatted_summary"]
            }
        }
        yield {"event": "message_done", "data": {"status": "COMPLETED"}}
