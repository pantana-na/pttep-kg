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

"""Agent Platform Proxy Client for Cloud Run Frontend.

Routes frontend queries and streaming requests to the deployed Gemini Enterprise
Agent Platform (Vertex AI Reasoning Engine backend) via Application Default Credentials.
Governed by: SPEC-20260918-FRONTEND-ONLY-CLOUD-RUN.md
"""

import json
import logging
import os
import re
import time
from typing import AsyncGenerator, Dict, Any, Optional
import httpx
import google.auth
from google.auth.transport.requests import Request as AuthRequest

logger = logging.getLogger("phenol.proxy")


class AgentPlatformProxy:
    """Client proxy for communicating with Gemini Enterprise Agent Platform runtime."""

    def __init__(self, resource_name: Optional[str] = None):
        self.resource_name = resource_name or os.getenv("AGENT_ENGINE_RESOURCE_NAME", "").strip()
        if not self.resource_name and os.path.exists("deployment_metadata.json"):
            try:
                with open("deployment_metadata.json", "r", encoding="utf-8") as f:
                    meta = json.load(f)
                    self.resource_name = meta.get("remote_agent_runtime_id", "").strip()
            except Exception as e:
                logger.warning(f"Failed to read deployment_metadata.json: {e}")

        self.location = os.getenv("GCP_REGION", "asia-southeast1")
        if self.resource_name and "/locations/" in self.resource_name:
            match = re.search(r"/locations/([^/]+)/", self.resource_name)
            if match:
                self.location = match.group(1)

        self._credentials = None
        self._project = None

    @property
    def is_configured(self) -> bool:
        """Returns True if a valid Agent Engine resource name is configured."""
        return bool(self.resource_name)

    def _get_access_token(self) -> str:
        """Retrieves or refreshes Google OAuth2 access token via ADC."""
        if self._credentials is None:
            self._credentials, self._project = google.auth.default(
                scopes=["https://www.googleapis.com/auth/cloud-platform"]
            )
        if not self._credentials.valid:
            self._credentials.refresh(AuthRequest())
        return self._credentials.token

    def _build_endpoint_url(self, method_name: str) -> str:
        """Builds regional Vertex AI Reasoning Engine URL."""
        return f"https://{self.location}-aiplatform.googleapis.com/v1/{self.resource_name}:{method_name}"

    async def stream_query(
        self, prompt: str, session_id: str = "default-session"
    ) -> AsyncGenerator[Dict[str, Any], None]:
        """Streams query execution from deployed Agent Platform backend, yielding formatted SSE events."""
        if not self.is_configured:
            raise RuntimeError("AgentPlatformProxy is not configured with AGENT_ENGINE_RESOURCE_NAME")

        token = self._get_access_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        url = self._build_endpoint_url("streamQuery")
        # Vertex AI Reasoning Engine requires hyphenated alphanumeric session IDs (rejects underscores)
        clean_session_id = (session_id or "default-session").replace("_", "-")
        if not clean_session_id.startswith("session-") and not clean_session_id.startswith("default"):
            clean_session_id = f"session-{clean_session_id}"

        payload = {
            "class_method": "async_stream_query",
            "input": {
                "user_id": "web-cockpit-user",
                "session_id": clean_session_id,
                "message": prompt,
            },
        }

        t_proxy_start = time.perf_counter()
        t_tool_call_start = None
        total_tool_duration_ms = 0.0
        first_cognitive_event_time = None
        t_synthesis_start = None

        async with httpx.AsyncClient(timeout=120.0) as client:
            async with client.stream("POST", url, headers=headers, json=payload) as response:
                if response.status_code != 200:
                    error_text = await response.aread()
                    logger.error(
                        f"Agent Platform streamQuery returned {response.status_code}: "
                        f"{error_text.decode('utf-8', errors='ignore')}"
                    )
                    yield {
                        "event": "message_delta",
                        "data": {
                            "content": f"⚠️ **Backend Error ({response.status_code}):** Could not reach Agent Platform runtime."
                        },
                    }
                    yield {"event": "message_done", "data": {"status": "ERROR"}}
                    return

                async for line in response.aiter_lines():
                    if not line or not line.strip():
                        continue
                    
                    raw = line.strip()
                    if raw.startswith("event:"):
                        continue
                    if raw.startswith("data:"):
                        raw = raw[5:].strip()
                    if not raw or raw == "[DONE]":
                        continue

                    try:
                        event_data = json.loads(raw)
                    except json.JSONDecodeError:
                        logger.warning(f"Failed to parse JSON from stream line: {raw[:100]}")
                        continue

                    now_ts = time.perf_counter()
                    if first_cognitive_event_time is None:
                        first_cognitive_event_time = now_ts

                    # ADK native event format
                    if "content" in event_data or "author" in event_data:
                        author = event_data.get("author", "OrchestratorAgent")
                        if author == "AgentPlatform":
                            author = "OrchestratorAgent"
                        content = event_data.get("content", {})
                        if isinstance(content, dict):
                            for part in content.get("parts", []):
                                if isinstance(part, dict):
                                    if "text" in part:
                                        text = part["text"]
                                        if part.get("thought"):
                                            yield {
                                                "event": "thought",
                                                "data": {
                                                    "thought_chunk": text,
                                                    "agent_role": author,
                                                    "timestamp_ms": round(now_ts * 1000),
                                                },
                                            }
                                        else:
                                            if t_synthesis_start is None:
                                                t_synthesis_start = now_ts
                                            yield {
                                                "event": "message_delta",
                                                "data": {
                                                    "content": text,
                                                    "text_delta": text,
                                                    "author": author,
                                                },
                                            }
                                    elif "function_call" in part:
                                        t_tool_call_start = time.perf_counter()
                                        fc = part["function_call"]
                                        tool_name = fc.get("name", "tool")
                                        args = fc.get("args", {})
                                        yield {
                                            "event": "tool_invoked",
                                            "data": {
                                                "tool_name": tool_name,
                                                "tool": tool_name,
                                                "tool_args": args,
                                                "arguments": args,
                                                "invoking_subagent": author,
                                            },
                                        }
                                        yield {
                                            "event": "tool_start",
                                            "data": {
                                                "tool_name": tool_name,
                                                "tool": tool_name,
                                                "arguments": args,
                                                "invoking_subagent": author,
                                            },
                                        }
                                    elif "function_response" in part:
                                        t_resp_now = time.perf_counter()
                                        if t_tool_call_start is not None:
                                            tool_dur = max(1.0, (t_resp_now - t_tool_call_start) * 1000.0)
                                            total_tool_duration_ms += tool_dur
                                            t_tool_call_start = None
                                        else:
                                            tool_dur = 25.0
                                        t_synthesis_start = t_resp_now

                                        fr = part["function_response"]
                                        tool_name = fr.get("name", "tool")
                                        resp = fr.get("response", {})
                                        resp_str = json.dumps(resp) if isinstance(resp, (dict, list)) else str(resp)
                                        yield {
                                            "event": "tool_result",
                                            "data": {
                                                "tool_name": tool_name,
                                                "tool": tool_name,
                                                "latency_ms": round(tool_dur, 1),
                                                "result_preview": resp_str[:300] if resp_str else "Success",
                                                "response": resp,
                                                "invoking_subagent": author,
                                            },
                                        }
                        elif isinstance(content, str) and content.strip():
                            if t_synthesis_start is None:
                                t_synthesis_start = now_ts
                            yield {
                                "event": "message_delta",
                                "data": {
                                    "content": content,
                                    "text_delta": content,
                                    "author": author,
                                },
                            }
                    elif "candidates" in event_data:
                        if t_synthesis_start is None:
                            t_synthesis_start = now_ts
                        for cand in event_data.get("candidates", []):
                            cand_content = cand.get("content", {})
                            if isinstance(cand_content, dict):
                                for part in cand_content.get("parts", []):
                                    if isinstance(part, dict) and "text" in part:
                                        text = part["text"]
                                        yield {
                                            "event": "message_delta",
                                            "data": {
                                                "content": text,
                                                "text_delta": text,
                                                "author": "OrchestratorAgent",
                                            },
                                        }
                    elif "event" in event_data and "data" in event_data:
                        ev = event_data["event"]
                        d = event_data["data"]
                        if ev in ("tool_invoked", "tool_start"):
                            t_tool_call_start = time.perf_counter()
                            if "tool_name" not in d and "tool" in d:
                                d["tool_name"] = d["tool"]
                            if "invoking_subagent" not in d:
                                d["invoking_subagent"] = "OrchestratorAgent"
                        elif ev == "tool_result":
                            t_resp_now = time.perf_counter()
                            if t_tool_call_start is not None:
                                tool_dur = max(1.0, (t_resp_now - t_tool_call_start) * 1000.0)
                                total_tool_duration_ms += tool_dur
                                t_tool_call_start = None
                                if "latency_ms" not in d:
                                    d["latency_ms"] = round(tool_dur, 1)
                            t_synthesis_start = t_resp_now
                        elif ev == "message_delta":
                            if t_synthesis_start is None:
                                t_synthesis_start = now_ts
                            if "text_delta" not in d and "content" in d:
                                d["text_delta"] = d["content"]
                        yield event_data
                    elif "text" in event_data:
                        if t_synthesis_start is None:
                            t_synthesis_start = now_ts
                        yield {
                            "event": "message_delta",
                            "data": {"content": event_data["text"], "text_delta": event_data["text"], "author": "OrchestratorAgent"},
                        }
                    elif "error" in event_data:
                        yield {
                            "event": "message_delta",
                            "data": {"content": f"⚠️ **Error:** {event_data['error']}", "text_delta": f"⚠️ **Error:** {event_data['error']}"},
                        }

                t_stream_end = time.perf_counter()
                if first_cognitive_event_time is None:
                    first_cognitive_event_time = t_stream_end
                if t_synthesis_start is None:
                    t_synthesis_start = first_cognitive_event_time

                p2_ms = max(5.0, (first_cognitive_event_time - t_proxy_start) * 1000.0)
                p3_ms = total_tool_duration_ms
                p4_ms = max(5.0, (t_stream_end - t_synthesis_start) * 1000.0)

                yield {
                    "event": "execution_timings",
                    "data": {
                        "phase2_ms": round(p2_ms, 1),
                        "phase3_ms": round(p3_ms, 1),
                        "phase4_ms": round(p4_ms, 1),
                    },
                }

                yield {"event": "message_done", "data": {"status": "COMPLETED"}}

    async def direct_query(
        self, prompt: str, session_id: str = "default-session"
    ) -> Dict[str, Any]:
        """Performs a direct query by aggregating stream events from the Agent Platform."""
        events = []
        async for event in self.stream_query(prompt, session_id):
            events.append(event)
        return {"status": "SUCCESS", "events": events}
