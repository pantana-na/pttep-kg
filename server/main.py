"""FastAPI Application Server for Multi-Agent Phenol Process Safety Platform.

Supports Cloud Run Liveness Probes, SSE event streaming, interactive clarification,
P&ID markup ingestion, 3-gate HITL HAZOP study facilitation, and 7-tab Excel exports.
SPEC-20260831-HAZOP-MARKUP-INGESTION-AND-STUDY-LIFECYCLE.
"""

import json
from pathlib import Path
from typing import Dict, Any, List, Optional
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from database.init_db import get_database
from agents.orchestrator.agent import OrchestratorAgent

app = FastAPI(title="Phenol Process Safety AI Platform", version="2.1.0")

# CORS middleware for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global DB and Orchestrator (live Cloud Spanner in cloud, mock in local tests)
db = get_database()
orchestrator = OrchestratorAgent(db)


# ==========================================
# Pydantic Request Models
# ==========================================

class ClarificationPayload(BaseModel):
    session_id: str
    selected_option_id: str
    target_tag: str
    custom_write_in: str = ""


class QueryPayload(BaseModel):
    prompt: str
    session_id: str = "default-session"


class FirstRiskPayload(BaseModel):
    people: int = 5
    env: int = 4
    econ: int = 5
    social: int = 4
    initial_likelihood: int = 4


class SafeguardsProposalPayload(BaseModel):
    equipment_tag: str
    deviation_type: str = "Flow"


class SecondRiskPayload(BaseModel):
    deviation: str
    cause: str
    consequence: str
    first_risk: Dict[str, Any]
    confirmed_safeguards: List[Dict[str, Any]]
    override_mitigated_likelihood: Optional[int] = None


class ExportExcelPayload(BaseModel):
    study_metadata: Dict[str, Any]
    worksheet_rows: List[Dict[str, Any]]


class DiscoverRisksPayload(BaseModel):
    node_id: str = "CDN-N02"
    equipment_tags: Optional[List[str]] = None


class RowEvaluationPayload(BaseModel):
    ref: str = "1.1.1"
    parameter: Optional[str] = None
    deviation: str = "Flow — No / Low Flow"
    cause: str = ""
    consequence: str = ""
    wo_p: int = 5
    wo_en: int = 4
    wo_ec: int = 5
    wo_s: int = 4
    wo_l: int = 4
    available_safeguards: Optional[List[Dict[str, Any]]] = None
    safeguards: Optional[List[Dict[str, Any]]] = None
    recommendation: Optional[str] = ""
    override_mitigated_likelihood: Optional[int] = None


class ScenarioGenerationPayload(BaseModel):
    node_id: str = "CDN-N02"
    equipment_tags: Optional[List[str]] = None
    scenario_text: str
    existing_rows_count: int = 5


# ==========================================
# Core Platform Endpoints
# ==========================================

@app.get("/")
async def serve_ui():
    """Serves the Multi-Agent Process Safety UI."""
    index_file = Path("server/static/index.html")
    if index_file.exists():
        return FileResponse(
            str(index_file),
            headers={
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0",
            },
        )
    return {"message": "Phenol Process Safety Platform API"}


@app.get("/healthz")
def healthz():
    """Liveness probe for Google Cloud Run."""
    return {"status": "HEALTHY", "service": "phenol-process-safety-agent"}


@app.post("/api/v1/agent/query")
async def handle_query(payload: QueryPayload):
    """Direct query endpoint returning aggregated answer."""
    events = []
    async for event in orchestrator.stream_orchestration(payload.prompt, payload.session_id):
        events.append(event)
    return {"status": "SUCCESS", "events": events}


@app.get("/api/v1/agent/stream")
async def stream_agent(prompt: str, session_id: str = "default-session"):
    """Server-Sent Events (SSE) streaming multiplexer endpoint."""
    async def event_generator():
        async for item in orchestrator.stream_orchestration(prompt, session_id):
            ev_name = item.get("event", "message_delta")
            data_json = json.dumps(item.get("data", {}))
            yield f"event: {ev_name}\ndata: {data_json}\n\n"
    return StreamingResponse(event_generator(), media_type="text/event-stream")


@app.post("/api/v1/agent/clarify")
async def handle_clarification(payload: ClarificationPayload):
    """Handles user selection from <ClarificationCard /> and resumes execution with LLM synthesis."""
    tag = payload.target_tag or payload.selected_option_id
    res = orchestrator.clarification.resolve_clarification(tag)
    
    # Run targeted retrieval across all 3 storage tiers
    interlocks = orchestrator.retriever.mcp.spanner_graph_query(tag, mode="interlocks")
    upstream = orchestrator.retriever.mcp.spanner_graph_query(tag, mode="upstream")
    prov = orchestrator.retriever.mcp.query_knowledge_catalog_provenance(tag)
    wiki_doc = orchestrator.retriever.mcp.read_gcs_wiki_document(tag)
    
    # Synthesize unified engineering answer via live Gemini
    synthesized_answer = orchestrator.synthesize_answer_with_llm(
        prompt=f"Show interlocks, trip actions, and process safety information for {tag}",
        target_tag=tag,
        interlocks=interlocks,
        upstream=upstream,
        prov=prov,
        wiki_doc=wiki_doc
    )
    
    return {
        "status": "RESUMED",
        "resolved_tag": tag,
        "synthesized_answer": synthesized_answer,
        "interlocks": interlocks,
        "provenance": prov,
        "wiki_doc": wiki_doc
    }


@app.get("/api/v1/graph/topology")
def get_graph_topology():
    """Returns full topological nodes and directed edges for the interactive Spanner Graph Cockpit.
    
    Includes equipment nodes, instrument interlock nodes, process flow edges (FEEDS),
    and instrument actuation edges (TRIPS).
    """
    nodes = []
    node_ids = set()

    for tag, eq in db.equipment.items():
        nodes.append({
            "id": tag,
            "label": tag,
            "type": "equipment",
            "sub_type": eq.type,
            "name": eq.name,
            "unit": eq.unit_id,
            "design_temp": eq.design_temp_celsius,
            "operating_temp": eq.operating_temp_celsius,
            "design_pressure": eq.design_pressure_barg,
            "operating_pressure": eq.operating_pressure_barg
        })
        node_ids.add(tag)

    for tag, inst in db.instruments.items():
        nodes.append({
            "id": tag,
            "label": tag,
            "type": "instrument",
            "sub_type": inst.type,
            "sil": inst.sil_rating,
            "voting": inst.voting_logic,
            "setpoint": inst.trip_setpoint,
            "target_equipment": inst.equipment_tag
        })
        node_ids.add(tag)

    edges = []
    for flow in db.equipment_flows:
        for t in (flow.from_equipment_tag, flow.to_equipment_tag):
            if t not in node_ids:
                nodes.append({
                    "id": t,
                    "label": t,
                    "type": "equipment",
                    "sub_type": "Connected Equipment",
                    "name": f"Process Equipment {t}",
                    "unit": "CDN"
                })
                node_ids.add(t)

        edges.append({
            "source": flow.from_equipment_tag,
            "target": flow.to_equipment_tag,
            "type": "FEEDS",
            "label": flow.stream_id,
            "stream": flow.stream_id
        })

    for act in db.instrument_actuations:
        for t in (act.initiator_instrument_tag, act.target_equipment_tag):
            if t not in node_ids:
                is_inst = not t.startswith(("E-", "V-", "P-", "D-", "UXV-"))
                nodes.append({
                    "id": t,
                    "label": t,
                    "type": "instrument" if is_inst else "equipment",
                    "sub_type": "Actuated Target" if not is_inst else "Initiator",
                    "name": f"Safety Component {t}",
                    "unit": "CDN"
                })
                node_ids.add(t)

        edges.append({
            "source": act.initiator_instrument_tag,
            "target": act.target_equipment_tag,
            "type": "TRIPS",
            "label": act.interlock_action,
            "action": act.interlock_action
        })

    return {
        "status": "SUCCESS",
        "nodes": nodes,
        "edges": edges,
        "stats": {
            "equipment_count": len(db.equipment),
            "instrument_count": len(db.instruments),
            "feed_edges_count": len(db.equipment_flows),
            "trip_edges_count": len(db.instrument_actuations)
        }
    }


# ==========================================
# HAZOP Study & HITL Endpoints
# ==========================================

@app.post("/api/v1/hazop/upload-markup")
async def upload_markup_pdf(request: Request):
    """Ingests engineer-marked P&ID PDF and returns hydrated NodeDefinition for confirmation."""
    content_bytes = await request.body()
    filename = request.headers.get("x-filename", "Node 23-02.pdf")
    
    # Also support JSON payload with base64/text if passed as JSON
    if request.headers.get("content-type", "").startswith("application/json"):
        try:
            json_body = json.loads(content_bytes)
            filename = json_body.get("filename", filename)
            content_bytes = json_body.get("content", "").encode("latin-1")
        except Exception:
            pass

    node_def = orchestrator.hazop.parse_markup_and_hydrate(content_bytes, filename=filename)
    return {
        "status": "AWAITING_CONFIRMATION",
        "node_definition": node_def
    }


@app.post("/api/v1/hazop/confirm-node")
async def confirm_node_endpoint(node_def: Dict[str, Any]):
    """Confirms Node Boundaries and registers node in wiki knowledge base."""
    res = orchestrator.hazop.confirm_node_definition(node_def)
    return res


@app.post("/api/v1/hazop/discover-risks")
def discover_risks_endpoint(payload: DiscoverRisksPayload):
    """Discovers all credible deviations, causes, consequences, initial PEES, and candidate safeguards for a confirmed node."""
    rows = orchestrator.hazop.discover_node_risks(
        node_id=payload.node_id,
        equipment_tags=payload.equipment_tags
    )
    return {"status": "SUCCESS", "node_id": payload.node_id, "discovered_rows": rows}


@app.post("/api/v1/hazop/evaluate-row")
def evaluate_row_endpoint(payload: RowEvaluationPayload):
    """Evaluates a single row with adjusted initial risk (PEES/L), selected safeguards IPLs, mitigated risk, and recommendation."""
    evaluated = orchestrator.hazop.evaluate_row(payload.model_dump())
    return {"status": "SUCCESS", "row": evaluated}


@app.post("/api/v1/hazop/generate-scenario-row")
def generate_scenario_row_endpoint(payload: ScenarioGenerationPayload):
    """Generates a complete structured HAZOP row from a natural language scenario using AI process knowledge."""
    row = orchestrator.hazop.generate_scenario_row(
        node_id=payload.node_id,
        equipment_tags=payload.equipment_tags,
        scenario_text=payload.scenario_text,
        existing_rows_count=payload.existing_rows_count
    )
    return {"status": "SUCCESS", "row": row}


@app.post("/api/v1/hazop/deviation/1st-risk")
def calculate_1st_risk(payload: FirstRiskPayload):
    """HITL Gate 1: Proposes unmitigated 1st risk assessment for human adjustment."""
    res = orchestrator.hazop.evaluate_1st_risk_hitl(
        people=payload.people,
        env=payload.env,
        econ=payload.econ,
        social=payload.social,
        initial_likelihood=payload.initial_likelihood
    )
    return {"status": "SUCCESS", "first_risk": res}


@app.post("/api/v1/hazop/deviation/safeguards")
def get_safeguard_proposals(payload: SafeguardsProposalPayload):
    """HITL Gate 2: Retrieves existing safeguards and calculated IPL credits."""
    safeguards = orchestrator.hazop.propose_safeguards_hitl(
        equipment_tag=payload.equipment_tag,
        deviation_type=payload.deviation_type
    )
    return {"status": "SUCCESS", "safeguards": safeguards}


@app.post("/api/v1/hazop/deviation/2nd-risk")
def calculate_2nd_risk(payload: SecondRiskPayload):
    """HITL Gate 3: Calculates Mitigated Risk and generates live Gemini recommendation."""
    res = orchestrator.hazop.evaluate_2nd_risk_and_recommendation_hitl(
        deviation=payload.deviation,
        cause=payload.cause,
        consequence=payload.consequence,
        first_risk=payload.first_risk,
        confirmed_safeguards=payload.confirmed_safeguards,
        override_mitigated_likelihood=payload.override_mitigated_likelihood
    )
    return {"status": "SUCCESS", "result": res}


@app.post("/api/v1/hazop/export-excel")
def export_excel_endpoint(payload: ExportExcelPayload):
    """Generates 7-tab Refinery audit-compliant Excel deliverable matching hazop-example/*.xlsx."""
    output_path = f"output/exports/{payload.study_metadata.get('node_id', 'CDN-N02')}_HAZOP-worksheet.xlsx"
    file_saved = orchestrator.hazop.export_study_workbook(
        study_metadata=payload.study_metadata,
        worksheet_rows=payload.worksheet_rows,
        output_filepath=output_path
    )
    return FileResponse(
        file_saved,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=Path(file_saved).name
    )


@app.post("/api/v1/hazop/finalize-study")
def finalize_study_endpoint(payload: ExportExcelPayload):
    """Finalizes study: synchronizes Wiki markdown, Cloud Spanner Graph, and Dataplex Knowledge Catalog."""
    output_path = f"output/exports/{payload.study_metadata.get('node_id', 'CDN-N02')}_HAZOP-worksheet.xlsx"
    sync_report = orchestrator.hazop.finalize_study_and_sync(
        study_metadata=payload.study_metadata,
        worksheet_rows=payload.worksheet_rows,
        output_filepath=output_path
    )
    return sync_report


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
