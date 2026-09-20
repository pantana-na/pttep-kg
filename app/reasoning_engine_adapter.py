# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Reasoning Engine Adapter for Google Agent Development Kit (ADK) & Agent Runtime.

Exposes /api/stream_reasoning_engine and /api/reasoning_engine so that Vertex AI
Reasoning Engine (:streamQuery, :query, Console Playground, agents-cli run)
can execute queries directly against the ADK App runtime.
Governed by: SPEC-20260918-FRONTEND-ONLY-CLOUD-RUN.md
"""

import inspect
import json
from typing import Any, Optional
from fastapi import FastAPI, HTTPException, Request, encoders, responses

try:
    from vertexai.agent_engines.templates.adk import AdkApp
except ImportError:
    AdkApp = None  # Graceful fallback for environments without vertexai


def attach_reasoning_engine_routes(app: FastAPI) -> None:
    """Register reasoning_engine routes that dispatch to an AdkApp."""
    runtime: Optional[Any] = None
    streaming_methods: set[str] = set()
    sync_methods: set[str] = set()

    def get_runtime():
        nonlocal runtime, streaming_methods, sync_methods
        if runtime is None:
            if AdkApp is None:
                raise HTTPException(
                    status_code=500,
                    detail="vertexai.agent_engines.templates.adk is not installed."
                )
            from app.agent import app as adk_app
            runtime = AdkApp(app=adk_app)
            runtime.set_up()
            operations = runtime.register_operations()
            streaming_methods = set(operations.get("stream", [])) | set(
                operations.get("async_stream", [])
            )
            sync_methods = set(operations.get("", [])) | set(
                operations.get("async", [])
            )
        return runtime

    def resolve_method(class_method: str, *, streaming: bool):
        rt = get_runtime()
        allowed = streaming_methods if streaming else sync_methods
        if class_method not in allowed:
            raise HTTPException(
                status_code=404,
                detail=f"Unsupported reasoning_engine method: {class_method!r}",
            )
        return getattr(rt, class_method)

    @app.post("/api/stream_reasoning_engine")
    async def stream_reasoning_engine(request: Request) -> responses.StreamingResponse:
        body = await request.json()
        class_method = body.get("class_method", "async_stream_query")
        method = resolve_method(class_method, streaming=True)

        async def generator():
            kwargs = body.get("input") or {}
            # If user_id is missing, default to cli-user
            kwargs.setdefault("user_id", "default-user")
            async for event in method(**kwargs):
                yield json.dumps(event) + "\n"

        return responses.StreamingResponse(
            content=generator(), media_type="application/json"
        )

    @app.post("/api/reasoning_engine")
    async def reasoning_engine(request: Request) -> responses.JSONResponse:
        body = await request.json()
        class_method = body.get("class_method", "create_session")
        method = resolve_method(class_method, streaming=False)
        kwargs = body.get("input") or {}
        kwargs.setdefault("user_id", "default-user")
        output = (
            await method(**kwargs)
            if inspect.iscoroutinefunction(method)
            else method(**kwargs)
        )
        return responses.JSONResponse(
            content=encoders.jsonable_encoder({"output": output})
        )

    # A2A Agent Card endpoints
    @app.get("/api/a2a/{app_name}/.well-known/agent-card.json")
    @app.get("/a2a/{app_name}/.well-known/agent-card.json")
    async def get_agent_card(app_name: str):
        return {
            "name": "phenol-process-safety",
            "description": "Refinery Phenol Process Safety & HAZOP Multi-Agent Platform",
            "version": "1.0.0",
            "capabilities": ["PROCESS_SAFETY_QA", "FACILITATE_HAZOP", "OTHERS"],
            "protocol": "a2a",
            "runtime": "agent_runtime",
            "model": "gemini-3.8-flash"
        }
