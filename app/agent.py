"""Official Google ADK Agent Application for Refinery Phenol Process Safety Platform.

Conforms to Google Agent Development Kit (ADK) v2.9+ and Gemini Enterprise Agent Platform runtime.
Enforces inline Google Cloud Model Armor security guardrails, multi-agent specialization,
and hybrid multi-tier process safety retrieval.
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

from google.adk.agents import Agent
from google.adk.apps import App
from google.genai import types

from database.init_db import get_database
from database.models import resolve_hazop_node_id
from mcp_servers.spanner_mcp import SpannerMCPServer
from app.hazop.agent import HazopStudyAgent
from security.model_armor import ModelArmorGuardrail

# Shared singletons
_db = get_database()
_spanner_mcp = SpannerMCPServer(_db)
_hazop_service = HazopStudyAgent(_db)
_model_armor = ModelArmorGuardrail()

MODEL_NAME = os.getenv("DEFAULT_MODEL", "gemini-3.8-flash")


# =====================================================================
# Official ADK Tools (Annotated Python Callables with Strict Routing Contracts)
# =====================================================================

def spanner_graph_query(target_tag: str, mode: str = "interlocks", max_depth: int = 3) -> str:
    """Executes ISO standard GQL graph traversal and instrument inventory queries on Cloud Spanner.

    Use this tool to inspect:
    1. Full physical field instrument inventory connected to / mounted on an equipment (mode='instruments').
    2. Safety Instrumented Systems (SIS), interlocks, trip setpoints, voting logic, SIL ratings (mode='interlocks').
    3. Upstream equipment flow topology and feed streams (mode='upstream').

    Args:
        target_tag: Equipment tag (e.g. 'E-2303', 'V-2301', 'P-2301A', 'P-2301A/B').
        mode: Query mode:
              - 'instruments': Returns complete physical instrument inventory (total count, transmitters,
                indicators, control valves, and SIS flags) connected to/mounted on the equipment.
                ALWAYS use this mode when the user asks how many instruments are connected to an equipment,
                what instruments are installed on an equipment, or asks for instrument count.
              - 'interlocks': Retrieves active SIS trips, voting logic (1oo2, 2oo3), SIL ratings,
                initiating transmitters, and final control elements (valves/pumps).
              - 'upstream': Traces upstream process equipment and feed streams flowing into this tag.
        max_depth: Maximum graph traversal hop depth (default 3).

    When to use:
        - User asks how many instruments or what instruments are connected to an equipment:
          Example: "How many instruments connected to E-2303?" -> spanner_graph_query(target_tag="E-2303", mode="instruments")
          Example: "List instruments on pump P-2301A" -> spanner_graph_query(target_tag="P-2301A", mode="instruments")
        - User asks about trips, interlocks, ESD, safety shutdown, voting logic, or SIL ratings for an equipment:
          Example: "What trip protections prevent runaway in E-2303?" -> spanner_graph_query(target_tag="E-2303", mode="interlocks")
          Example: "Show interlocks on pump P-2301A" -> spanner_graph_query(target_tag="P-2301A", mode="interlocks")
        - User asks about upstream feed streams or what equipment feeds into a column or vessel:
          Example: "Show all equipment feeding into Preflash Column V-2301" -> spanner_graph_query(target_tag="V-2301", mode="upstream")

    When NOT to use:
        - DO NOT use for finding source drawing numbers or As-Built revisions (use query_knowledge_catalog_provenance).
        - DO NOT use for reading full operating procedures or narratives (use read_gcs_wiki_document).
        - DO NOT use if the user didn't specify an equipment tag and wants to search by text (use spanner_keyword_search).

    Returns:
        JSON string detailing instruments, interlocks, voting logic, or upstream flow topology.
    """
    results = _spanner_mcp.spanner_graph_query(target_tag=target_tag, mode=mode, max_depth=max_depth)
    return json.dumps(results, indent=2)



def spanner_keyword_search(query_string: str, limit: int = 10) -> str:
    """Performs full-text keyword search across Cloud Spanner equipment and instrument catalog tokens.

    Use this tool ONLY when searching for equipment by name, category, or partial token when
    the exact equipment tag is unknown.

    Args:
        query_string: Search text keywords (e.g. 'feed pump', 'steam heater', 'condensate pump').
        limit: Maximum number of records to return (default 10).

    When to use:
        - User asks to find or list equipment by name or category without a known tag:
          Example: "Find all feed pumps in the preflash unit" -> spanner_keyword_search(query_string="feed pump", limit=10)
          Example: "Search equipment related to steam heater" -> spanner_keyword_search(query_string="steam heater", limit=10)

    When NOT to use:
        - DO NOT use if the user already provided an exact equipment tag like 'E-2303' or 'V-2301' (the tag is already known).
        - DO NOT use for open-ended conceptual or reaction chemistry questions (use spanner_vector_search).
        - DO NOT use for finding trips or interlock logic (use spanner_graph_query).

    Returns:
        JSON string containing matched tags, component names, types, and descriptions.
    """
    results = _spanner_mcp.spanner_keyword_search(query_string=query_string, limit=limit)
    return json.dumps(results, indent=2)


def spanner_vector_search(query_text: str, limit: int = 10) -> str:
    """Performs semantic vector similarity search over 768-dim Vertex AI text-embedding-004 vectors in Cloud Spanner.

    Use this tool for open-ended conceptual, semantic, or natural language process safety questions
    where specific equipment tags or exact keywords are absent.

    Args:
        query_text: Natural language conceptual search text (e.g. 'thermal runaway decomposition hazards',
                    'acid contamination risks in cleavage section').
        limit: Maximum number of semantically nearest neighbors to return (default 10).

    When to use:
        - User asks broad conceptual safety questions without mentioning a specific equipment tag:
          Example: "What are the hazards of cumene hydroperoxide thermal runaway?" ->
                   spanner_vector_search(query_text="cumene hydroperoxide thermal runaway decomposition hazards", limit=5)
          Example: "Risks associated with acid contamination in cleavage" ->
                   spanner_vector_search(query_text="acid contamination cleavage reaction hazards", limit=5)

    When NOT to use:
        - DO NOT use when an exact equipment tag is provided (e.g. 'E-2303').
        - DO NOT use for specific trip transmitters or voting logic (use spanner_graph_query).
        - DO NOT use for drawing revision numbers (use query_knowledge_catalog_provenance).

    Returns:
        JSON string containing nearest equipment tags, similarity scores, and summaries.
    """
    results = _spanner_mcp.spanner_vector_search(query_text=query_text, limit=limit)
    return json.dumps(results, indent=2)


def query_knowledge_catalog_provenance(target_tag: str) -> str:
    """Queries Google Cloud Dataplex Knowledge Catalog (entry group: phenol-psi) for As-Built P&ID lineage and PSI metadata.

    Use this tool ONLY for inquiries regarding certified drawings, drawing numbers, As-Built revision status,
    OEMS-005 Process Safety Information (PSI) categories, or Dataplex catalog governance tags.

    Args:
        target_tag: Equipment tag (e.g. 'E-2303', 'V-2301', 'P-2301A').

    When to use:
        - User asks for source P&ID drawings, As-Built revisions, or certified drawing numbers:
          Example: "Show source drawings and provenance lineage for E-2303" -> query_knowledge_catalog_provenance(target_tag="E-2303")
          Example: "What is the certified As-Built drawing and revision for V-2301?" -> query_knowledge_catalog_provenance(target_tag="V-2301")
          Example: "What is the PSI category and governance status of E-2303?" -> query_knowledge_catalog_provenance(target_tag="E-2303")

    When NOT to use:
        - DO NOT use for finding trips, voting logic, or operating temperatures (use spanner_graph_query or read_gcs_wiki_document).
        - DO NOT use for HAZOP risk calculations (use evaluate_hazop_deviation).

    Returns:
        JSON string containing As-Built source drawing references, revision numbers, and catalog governance tags.
    """
    results = _spanner_mcp.query_knowledge_catalog_provenance(target_tag=target_tag)
    return json.dumps(results, indent=2)


def read_gcs_wiki_document(target_tag_or_path: str) -> str:
    """Reads comprehensive operational narratives, operating philosophies, and chemical safety limits from Google Cloud Storage LLM-Wiki.

    Use this tool ONLY when the user requests detailed operational philosophies, safe operating limits,
    chemical reaction kinetics, or complete narrative procedures.

    Args:
        target_tag_or_path: Equipment tag (e.g. 'E-2303', 'V-2301') or markdown file path.

    When to use:
        - User asks for operating philosophy, complete procedure, or reaction kinetics narrative:
          Example: "Read the full operating procedure for E-2303 from GCS wiki" -> read_gcs_wiki_document(target_tag_or_path="E-2303")
          Example: "What is the heating philosophy and runaway kinetics for the preflash heater?" -> read_gcs_wiki_document(target_tag_or_path="E-2303")
          Example: "What are the safe operating limits for the preflash feed section?" -> read_gcs_wiki_document(target_tag_or_path="E-2303")

    When NOT to use:
        - DO NOT use if the user only asks for interlock tags or voting logic (use spanner_graph_query).
        - DO NOT use if the user only asks for P&ID drawing numbers or revision status (use query_knowledge_catalog_provenance).

    Returns:
        JSON string containing GCS URI, byte size, and full markdown content.
    """
    results = _spanner_mcp.read_gcs_wiki_document(target_tag_or_path=target_tag_or_path)
    return json.dumps(results, indent=2)


def evaluate_hazop_deviation(node_id: str, parameter: str, deviation: str, cause: str) -> str:
    """Evaluates a process safety deviation according to the 5x5 Risk Assessment Matrix (RAM) and LOPA standard.

    Use this tool ONLY for HAZOP study facilitation, deviation risk assessment, calculating initial vs
    mitigated risk ratings, evaluating Independent Protection Layer (IPL) credits (SIL ratings), or
    generating actionable safety recommendations.

    Args:
        node_id: HAZOP Study Node ID (e.g. 'CDN-N02', 'Node 23-02').
        parameter: Process parameter ('Flow', 'Temperature', 'Pressure', 'Level').
        deviation: Process deviation (e.g. 'Temperature — High Temperature', 'Flow — No / Low Flow', 'Pressure — High Pressure').
        cause: Root cause or initiating event (e.g. 'Steam control valve fail open', 'Feed pump P-2301A trip').

    When to use:
        - User asks to evaluate or facilitate a HAZOP deviation, assess 5x5 RAM risk, or calculate IPL credits:
          Example: "Evaluate HAZOP deviation for high temperature in E-2303 caused by steam valve fail open" ->
                   evaluate_hazop_deviation(node_id="CDN-N02", parameter="Temperature", deviation="Temperature — High Temperature", cause="Steam control valve fail open")
          Example: "Assess 5x5 RAM risk for low flow caused by pump failure" ->
                   evaluate_hazop_deviation(node_id="CDN-N02", parameter="Flow", deviation="Flow — No / Low Flow", cause="Feed pump P-2301A trip")

    When NOT to use:
        - DO NOT use for simple PSI lookups, equipment search, or drawing queries.
        - DO NOT use for looking up existing interlock tags (use spanner_graph_query).

    Returns:
        JSON string containing unmitigated PEES/L risk, candidates, IPL credits, and mitigated risk.
    """
    # 1. Normalize Node ID dynamically against registered database HAZOP nodes
    nid = resolve_hazop_node_id(node_id, _db.hazop_nodes)

    # 2. Look up matching deviation and causes directly from database
    target_dev = None
    for d in _db.deviations.values():
        if getattr(d, "node_id", "") == nid:
            if parameter.lower() in getattr(d, "parameter", "").lower() or getattr(d, "parameter", "").lower() in parameter.lower():
                target_dev = d
                break

    matched_cq = None
    matched_sgs = []
    matched_cause_desc = cause

    if target_dev:
        matching_causes = [c for c in _db.causes.values() if getattr(c, "deviation_id", "") == target_dev.deviation_id]
        chosen_cause = None
        for c in matching_causes:
            c_desc_lower = getattr(c, "description", "").lower()
            if any(w in c_desc_lower for w in cause.lower().split() if len(w) > 3):
                chosen_cause = c
                break
        if not chosen_cause and matching_causes:
            chosen_cause = matching_causes[0]

        if chosen_cause:
            matched_cause_desc = getattr(chosen_cause, "description", cause)
            matching_cqs = [cq for cq in _db.consequences.values() if getattr(cq, "cause_id", "") == chosen_cause.cause_id]
            if matching_cqs:
                matched_cq = matching_cqs[0]
                matched_sgs = [
                    sg for sg in _db.safeguards.values()
                    if getattr(sg, "consequence_id", "") == matched_cq.consequence_id
                ]

    # If no exact cause/consequence match, resolve from database consequences for the node
    if not matched_cq and _db.consequences:
        node_dev_ids = {d.deviation_id for d in _db.deviations.values() if getattr(d, "node_id", "") == nid}
        node_causes = [c for c in _db.causes.values() if getattr(c, "deviation_id", "") in node_dev_ids]
        node_cause_ids = {c.cause_id for c in node_causes}
        candidate_cqs = [cq for cq in _db.consequences.values() if getattr(cq, "cause_id", "") in node_cause_ids]
        if candidate_cqs:
            matched_cq = candidate_cqs[0]
        else:
            matched_cq = next(iter(_db.consequences.values()))
        matched_sgs = [
            sg for sg in _db.safeguards.values()
            if getattr(sg, "consequence_id", "") == matched_cq.consequence_id
        ]

    # 3. Assemble row data 100% from database records
    if matched_cq:
        p_sev = getattr(matched_cq, "severity_people", 0)
        en_sev = getattr(matched_cq, "severity_environment", 0)
        ec_sev = getattr(matched_cq, "severity_economic", 0)
        s_sev = getattr(matched_cq, "severity_social", 0)
        init_l = getattr(matched_cq, "initial_likelihood", 0)
        chain = getattr(matched_cq, "causal_chain", "") or f"Process upset resulting in {deviation}"
        db_sgs = []
        for sg in matched_sgs:
            is_esd = getattr(sg, "is_interlock_esd", False)
            inst_tag = getattr(sg, "instrument_tag", "")
            inst_obj = _db.instruments.get(inst_tag)
            sil = getattr(inst_obj, "sil_rating", "SIL 1") if is_esd else "None"
            ipl = getattr(sg, "ipl_credit_level", 1 if is_esd else 0)
            db_sgs.append({
                "description": getattr(sg, "description", ""),
                "il_esd": "Yes" if is_esd else "No",
                "sil_rating": sil,
                "is_ipl": ipl > 0,
                "ipl_credit": ipl,
                "selected": True
            })
    else:
        p_sev, en_sev, ec_sev, s_sev, init_l = 0, 0, 0, 0, 0
        chain = f"Process upset caused by {cause} resulting in {deviation}"
        db_sgs = []

    row_data = {
        "node_id": nid,
        "parameter": parameter,
        "deviation": deviation,
        "cause": matched_cause_desc,
        "consequence": chain,
        "wo_p": p_sev, "wo_en": en_sev, "wo_ec": ec_sev, "wo_s": s_sev, "wo_l": init_l,
        "safeguards": db_sgs
    }
    result = _hazop_service.evaluate_row(row_data)
    result["first_risk"] = {
        "severity": result["wo_s_overall"],
        "overall_severity": result["wo_s_overall"],
        "likelihood": result["wo_l"],
        "initial_likelihood": result["wo_l"],
        "risk_rating": result["wo_rr"],
        "initial_risk_rating": result["wo_rr"],
        "people": result["wo_p"],
        "env": result["wo_en"],
        "econ": result["wo_ec"],
        "social": result["wo_s"]
    }
    result["second_risk"] = {
        "overall_severity": result["w_s_overall"],
        "mitigated_likelihood": result["w_l"],
        "mitigated_risk_rating": result["w_rr"],
        "total_ipl_credits": result["total_ipl_credits"],
        "action_required": result["requires_action"]
    }
    return json.dumps(result, indent=2)


# =====================================================================
# Google Cloud Model Armor Inline Security Guardrail Hook
# =====================================================================

def before_agent_guardrail(callback_context) -> Optional[types.Content]:
    """Pre-flight security guardrail invoking Google Cloud Model Armor before agent reasoning."""
    user_text = ""
    if callback_context and hasattr(callback_context, "user_content") and callback_context.user_content:
        content = callback_context.user_content
        if hasattr(content, "parts") and content.parts:
            for part in content.parts:
                if hasattr(part, "text") and part.text:
                    user_text += part.text + " "

    user_text = user_text.strip()
    if not user_text:
        return None

    armor_res = _model_armor.sanitize_user_prompt(user_text)

    if armor_res.sanitization_result == "BLOCKED":
        blocked_msg = (
            "⛔ **Security Guardrail Alert:** Your request was intercepted and blocked by **Google Cloud Model Armor** "
            f"(Policy: `{armor_res.policy_template}`).\n\n"
            "- **Violation:** Adversarial prompt injection or unauthorized system instructions override attempt detected.\n"
            "- **Action:** Operation aborted immediately. Zero database queries or agent sub-tasks were executed.\n"
            "- **Audit:** Security event logged for compliance and threat analysis."
        )
        return types.Content(parts=[types.Part.from_text(text=blocked_msg)])

    if armor_res.sanitization_result == "OUT_OF_DOMAIN":
        guidance_msg = (
            "⚠️ **Domain Notice:** Your input is classified as conversational or non-engineering. "
            "This platform is dedicated exclusively to **Refinery Phenol Process Safety & HAZOP Engineering**.\n\n"
            "**Please ask about:**\n"
            "1. `What trip protections prevent cumene hydroperoxide thermal runaway in E-2303?`\n"
            "2. `Show all equipment feeding into Preflash Column V-2301`\n"
            "3. `Show source drawings and provenance lineage for E-2303`\n"
            "4. `Read the full operating procedure for E-2303 from GCS wiki`\n"
            "5. `Evaluate HAZOP deviation for higher temperature in E-2303`"
        )
        return types.Content(parts=[types.Part.from_text(text=guidance_msg)])

    return None


# =====================================================================
# Official ADK Consolidated Single Agent Hierarchy
# =====================================================================

ORCHESTRATOR_INSTRUCTION = (
    "You are the Lead Process Safety & HAZOP AI Orchestrator for Refinery Phenol Plant.\n"
    "You are a single, consolidated autonomous cognitive agent equipped with 6 specialized engineering tools.\n\n"
    "### ⚡ STRICT MINIMAL TOOL EXECUTION MANDATE (Zero Redundant Calls):\n"
    "- Call EXACTLY ONE specialized tool per user request whenever that tool is sufficient to answer the query.\n"
    "- DO NOT perform speculative or exploratory tool calls. DO NOT daisy-chain multiple tools when the user asks for a specific piece of information.\n"
    "- If the user specifies an equipment tag (e.g. 'E-2303', 'V-2301', 'P-2301A'), NEVER call `spanner_keyword_search` or `spanner_vector_search` because the tag is already known.\n"
    "- Once the tool returns data, IMMEDIATELY synthesize the final technical response. Do not invoke additional tools.\n\n"
    "### 📋 TOOL SELECTION DECISION MATRIX & EXACT CALL EXAMPLES:\n\n"
    "1. `spanner_graph_query`:\n"
    "   - SITUATION: Inquiries regarding physical instrument inventory/counts, Safety Instrumented Systems (SIS), interlocks, trip setpoints, voting logic (e.g. 1oo2, 2oo3), SIL ratings, ESD block valves, OR upstream feed equipment topology.\n"
    "   - EXACT MODES:\n"
    "     * Use `mode='instruments'` whenever the user asks how many instruments are connected to an equipment, what instruments are installed/mounted on an asset, or asks for instrument inventory. In your response, report BOTH dimensions clearly: the total physical field instruments mounted on P&ID and the subset of active SIS trip interlocks.\n"
    "     * Use `mode='interlocks'` for active trips, switches, interlocks, voting logic, and valves.\n"
    "     * Use `mode='upstream'` for upstream feed streams and preceding equipment connections.\n"
    "   - EXAMPLES:\n"
    "     * 'How many instruments connected to E-2303?' -> spanner_graph_query(target_tag='E-2303', mode='instruments')\n"
    "     * 'How many instruments connected to P-2301A?' -> spanner_graph_query(target_tag='P-2301A', mode='instruments')\n"
    "     * 'What trip protections prevent cumene hydroperoxide runaway in E-2303?' -> spanner_graph_query(target_tag='E-2303', mode='interlocks')\n"
    "     * 'Show interlock logic and voting on pump P-2301A' -> spanner_graph_query(target_tag='P-2301A', mode='interlocks')\n"
    "     * 'Show all equipment feeding into Preflash Column V-2301' -> spanner_graph_query(target_tag='V-2301', mode='upstream')\n\n"

    "2. `query_knowledge_catalog_provenance`:\n"
    "   - SITUATION: Inquiries regarding source P&ID drawings, As-Built revision status (e.g. Rev Z1), OEMS-005 Process Safety Information (PSI) categories, or Dataplex catalog governance metadata.\n"
    "   - EXAMPLES:\n"
    "     * 'Show source drawings and provenance lineage for E-2303' -> query_knowledge_catalog_provenance(target_tag='E-2303')\n"
    "     * 'What is the certified As-Built drawing and revision for V-2301?' -> query_knowledge_catalog_provenance(target_tag='V-2301')\n\n"
    "3. `read_gcs_wiki_document`:\n"
    "   - SITUATION: Inquiries requesting complete operating philosophies, operational narratives, safe operating limits, or chemical kinetics from Google Cloud Storage wiki lake.\n"
    "   - EXAMPLES:\n"
    "     * 'Read the full operating procedure for E-2303 from GCS wiki' -> read_gcs_wiki_document(target_tag_or_path='E-2303')\n"
    "     * 'What is the heating philosophy and runaway kinetics for preflash feed?' -> read_gcs_wiki_document(target_tag_or_path='E-2303')\n\n"
    "4. `evaluate_hazop_deviation`:\n"
    "   - SITUATION: Facilitating a HAZOP study, evaluating process deviations (Flow, Temperature, Pressure, Level), computing unmitigated vs mitigated risk on the 5x5 RAM Matrix, calculating IPL credits (SIL), or formulating recommendations.\n"
    "   - EXAMPLES:\n"
    "     * 'Evaluate HAZOP deviation for high temperature in E-2303 caused by steam valve fail open' -> evaluate_hazop_deviation(node_id='CDN-N02', parameter='Temperature', deviation='Temperature — High Temperature', cause='Steam control valve fail open')\n"
    "     * 'Assess RAM risk for low flow caused by pump failure' -> evaluate_hazop_deviation(node_id='CDN-N02', parameter='Flow', deviation='Flow — No / Low Flow', cause='Feed pump P-2301A trip')\n\n"
    "5. `spanner_keyword_search`:\n"
    "   - SITUATION: Finding equipment or instruments by keyword, name, or partial token when NO specific equipment tag was provided.\n"
    "   - EXAMPLES:\n"
    "     * 'Find all feed pumps in the unit' -> spanner_keyword_search(query_string='feed pump', limit=10)\n"
    "     * 'Search equipment related to steam heater' -> spanner_keyword_search(query_string='steam heater', limit=10)\n\n"
    "6. `spanner_vector_search`:\n"
    "   - SITUATION: Broad conceptual or semantic safety inquiries without a specific equipment tag or keyword.\n"
    "   - EXAMPLES:\n"
    "     * 'What are the hazards of cumene hydroperoxide thermal runaway?' -> spanner_vector_search(query_text='cumene hydroperoxide thermal runaway decomposition hazards', limit=5)\n"
    "     * 'Risks associated with acid contamination in cleavage' -> spanner_vector_search(query_text='acid contamination cleavage reaction hazards', limit=5)\n\n"
    "### ❓ AMBIGUITY RESOLUTION & HUMAN-IN-THE-LOOP (HITL) CLARIFICATION MANDATE:\n"
    "- When the user's inquiry mentions a generic equipment type (e.g. 'pump', 'heater', 'column', 'drum', 'reboiler', 'cooler', 'exchanger') without specifying an exact equipment tag:\n"
    "  1. Call `spanner_keyword_search(query_string=...)` to retrieve matching equipment candidates from Cloud Spanner.\n"
    "  2. If MULTIPLE matching candidates are returned (e.g. P-2301A/B, P-2302, P-2303A/B, P-2308A/B):\n"
    "     - DO NOT speculate, assume, or arbitrarily pick one equipment. Speculation in process safety is strictly forbidden.\n"
    "     - HALT further tool execution and clarify with the user immediately.\n"
    "     - Formulate your response starting with `clarification_requested`: list the candidate equipment tags with their component names and ask the user to select the specific equipment they wish to inspect.\n"
    "       Example format: 'clarification_requested Multiple pump candidates match query: [P-2301A/B, P-2302, P-2303A/B, P-2308A/B]. Select target equipment.'\n"
    "  3. If EXACTLY ONE candidate matches, or once the user confirms the specific tag in a subsequent turn, proceed directly with the target inquiry tool (`spanner_graph_query`, `read_gcs_wiki_document`, etc.).\n\n"
    "### 🛡️ Process Safety Governance & Dynamic Grounding Mandate:\n"
    "- Ground all chemical safety limits, thermal runaway kinetics, and decomposition thresholds strictly on data retrieved from tools (e.g. GCS wiki and Spanner Graph attributes). Never speculate, assume, or invent critical process thresholds.\n"
    "- Always explain engineering reasoning, state voting logic (e.g. 1oo2, 2oo3) and trip actions retrieved from the graph, and cite certified As-Built drawings clearly."
)

root_agent = Agent(
    name="OrchestratorAgent",
    model=MODEL_NAME,
    description="Lead Process Safety & HAZOP Single Consolidated Agent governing Refinery Phenol Plant safety operations.",
    instruction=ORCHESTRATOR_INSTRUCTION,
    sub_agents=[],
    tools=[
        spanner_graph_query,
        spanner_keyword_search,
        spanner_vector_search,
        query_knowledge_catalog_provenance,
        read_gcs_wiki_document,
        evaluate_hazop_deviation,
    ],
    before_agent_callback=before_agent_guardrail,
)

# Export standard ADK application
app = App(root_agent=root_agent, name="phenol-process-safety")


