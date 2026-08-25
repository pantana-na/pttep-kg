"""FastAPI Application Server for Multi-Agent Phenol Process Safety Platform.

Supports Cloud Run Liveness Probes, SSE event streaming, interactive clarification, and UI static serving.
SPEC-20260824-MULTI-AGENT-CLOUD-ARCHITECTURE Section 4.4 & 6.1.
"""

import json
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database.init_db import init_local_mock
from agents.orchestrator.agent import OrchestratorAgent

app = FastAPI(title="Phenol Process Safety AI Platform", version="2.0.0")

# CORS middleware for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global in-memory DB and Orchestrator
db = init_local_mock("wiki")
orchestrator = OrchestratorAgent(db)


class ClarificationPayload(BaseModel):
    session_id: str
    selected_option_id: str
    target_tag: str
    custom_write_in: str = ""


class QueryPayload(BaseModel):
    prompt: str
    session_id: str = "default-session"


@app.get("/")
async def serve_ui():
    """Serves the Multi-Agent Process Safety UI."""
    index_file = Path("server/static/index.html")
    if index_file.exists():
        return FileResponse(str(index_file))
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
    """Handles user selection from <ClarificationCard /> and resumes execution."""
    tag = payload.target_tag or payload.selected_option_id
    res = orchestrator.clarification.resolve_clarification(tag)
    
    # Run targeted retrieval with resolved tag
    search_res = orchestrator.retriever.search_tri_hybrid(f"Show interlocks and equipment data for {tag}")
    return {
        "status": "RESUMED",
        "resolved_tag": tag,
        "search_results": search_res
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
