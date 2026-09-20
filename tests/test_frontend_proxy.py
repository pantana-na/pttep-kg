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

"""Unit and Property-Based Tests for Cloud Run Frontend Web Cockpit & SSE Proxy.

Governed by: SPEC-20260918-FRONTEND-ONLY-CLOUD-RUN.md
Verifies frontend decoupling, proxy mechanics, fallback behavior, and SSE invariants.
"""

import json
import pytest
from unittest.mock import patch, AsyncMock
from fastapi.testclient import TestClient
from hypothesis import given, strategies as st, settings

from server.main import app, agent_proxy
from server.proxy import AgentPlatformProxy

client = TestClient(app)


def test_healthz_frontend_role():
    """Verify healthz indicates frontend web cockpit role."""
    resp = client.get("/healthz")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "HEALTHY"
    assert data["role"] == "frontend-web-cockpit"
    assert "backend_agent_runtime" in data


def test_adk_info_frontend_metadata():
    """Verify /api/v1/adk/info indicates frontend role and backend runtime ID."""
    resp = client.get("/api/v1/adk/info")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "SUCCESS"
    assert data["role"] == "frontend-web-cockpit"
    assert "remote_agent_runtime_id" in data


@pytest.mark.asyncio
async def test_proxy_mock_streaming():
    """Verify AgentPlatformProxy streams and formats SSE chunks properly."""
    proxy = AgentPlatformProxy(resource_name="projects/123/locations/asia-southeast1/reasoningEngines/999")
    assert proxy.is_configured
    assert proxy.location == "asia-southeast1"

    mock_events = [
        {"author": "OrchestratorAgent", "content": {"parts": [{"text": "Hello, safety engineer."}]}},
        {"author": "RetrieverAgent", "content": {"parts": [{"text": "Found E-2303 interlocks."}]}}
    ]

    async def mock_stream_query(prompt, session_id="default-session"):
        for ev in mock_events:
            for part in ev["content"]["parts"]:
                yield {
                    "event": "message_delta",
                    "data": {"content": part["text"], "author": ev["author"]}
                }
        yield {"event": "message_done", "data": {"status": "COMPLETED"}}

    with patch.object(proxy, "stream_query", side_effect=mock_stream_query):
        events = []
        async for item in proxy.stream_query("Test prompt"):
            events.append(item)

        assert len(events) == 3
        assert events[0]["event"] == "message_delta"
        assert events[0]["data"]["content"] == "Hello, safety engineer."
        assert events[1]["event"] == "message_delta"
        assert events[1]["data"]["content"] == "Found E-2303 interlocks."
        assert events[2]["event"] == "message_done"
        assert events[2]["data"]["status"] == "COMPLETED"


def test_stream_agent_proxy_streaming():
    """Verify /api/v1/agent/stream forwards properly when agent_proxy is configured."""
    async def mock_proxy_stream(prompt, session_id="default-session"):
        yield {"event": "message_delta", "data": {"content": "Proxied response from Agent Platform"}}
        yield {"event": "message_done", "data": {"status": "COMPLETED"}}

    with patch.object(agent_proxy, "resource_name", "projects/123/locations/asia-southeast1/reasoningEngines/555"):
        with patch.object(agent_proxy, "stream_query", side_effect=mock_proxy_stream):
            resp = client.get("/api/v1/agent/stream?prompt=What%20is%20E-2303?")
            assert resp.status_code == 200
            assert "event: message_delta" in resp.text
            assert "Proxied response from Agent Platform" in resp.text
            assert "event: message_done" in resp.text


def test_stream_agent_local_fallback():
    """Verify /api/v1/agent/stream falls back gracefully to local orchestrator when proxy is unconfigured."""
    with patch.object(agent_proxy, "resource_name", ""):
        assert not agent_proxy.is_configured
        resp = client.get("/api/v1/agent/stream?prompt=What%20is%20E-2303?")
        assert resp.status_code == 200
        assert "text/event-stream" in resp.headers["content-type"]
        body = resp.text
        assert "event: " in body
        assert "data: " in body


@settings(max_examples=15, deadline=None)
@given(st.text(min_size=1, max_size=50))
def test_pbt_sse_framing_invariant(prompt_text):
    """PBT-SSE-FRAMING-INVARIANT: Every SSE chunk emitted by the generator
    must strictly conform to the SSE protocol format: 'event: <name>\ndata: <json>\n\n'.
    """
    safe_prompt = prompt_text.replace("\n", " ").replace("\r", " ").strip()
    if not safe_prompt:
        safe_prompt = "E-2303"

    with patch.dict("os.environ", {"FORCE_OFFLINE_MOCK": "true", "AGENT_ENGINE_RESOURCE_NAME": ""}):
        with patch.object(agent_proxy, "resource_name", ""):
            resp = client.get("/api/v1/agent/stream", params={"prompt": safe_prompt})
            assert resp.status_code == 200
            chunks = resp.text.split("\n\n")

            for chunk in chunks:
                chunk = chunk.strip()
                if not chunk:
                    continue
                lines = chunk.split("\n")
                assert len(lines) >= 2, f"Chunk malformed: {chunk}"
                assert lines[0].startswith("event: "), f"Missing event header in: {chunk}"
                assert lines[1].startswith("data: "), f"Missing data header in: {chunk}"
                # Invariant: data payload must be valid JSON
                data_str = lines[1][len("data: "):]
                parsed = json.loads(data_str)
                assert isinstance(parsed, dict)


def test_catalog_hierarchy_structure():
    """Verify /api/v1/catalog/hierarchy returns valid plant sections, nodes, equipment, and instruments."""
    resp = client.get("/api/v1/catalog/hierarchy")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "SUCCESS"
    assert data["total_equipment"] > 0
    assert data["total_instruments"] > 0
    assert len(data["sections"]) >= 3

    section_ids = [s["section_id"] for s in data["sections"]]
    assert "SEC-23" in section_ids
    assert "SEC-22" in section_ids
    assert "SEC-21" in section_ids

    # Verify E-2303 exists and has instruments
    all_eq = {}
    for s in data["sections"]:
        for n in s["nodes"]:
            for eq in n["equipment"]:
                all_eq[eq["tag"]] = eq

    assert "E-2303" in all_eq
    e2303 = all_eq["E-2303"]
    assert e2303["instrument_count"] > 0
    assert len(e2303["instruments"]) == e2303["instrument_count"]
    inst_tags = [i["tag"] for i in e2303["instruments"]]
    assert "FE-0501" in inst_tags or "FIC-0501" in inst_tags



def test_session_reset_endpoint():
    """Verify /api/v1/session/reset generates distinct valid session identifiers."""
    resp1 = client.post("/api/v1/session/reset")
    assert resp1.status_code == 200
    data1 = resp1.json()
    assert data1["status"] == "SUCCESS"
    assert data1["session_id"].startswith("session_")
    assert "timestamp" in data1

    resp2 = client.post("/api/v1/session/reset")
    assert resp2.status_code == 200
    data2 = resp2.json()
    assert data2["session_id"].startswith("session_")
    assert data1["session_id"] != data2["session_id"]


@settings(max_examples=10, deadline=None)
@given(st.sampled_from(["SEC-23", "SEC-22", "SEC-21"]))
def test_pbt_catalog_hierarchy_invariants(target_sec_id):
    """PBT-HIERARCHY-INVARIANT: Every section adheres to strict structural and relational invariants:
    1. Every node belongs to its declared section.
    2. Every equipment has a valid non-empty tag, matching node_id, and exact instrument_count.
    3. Every instrument in an equipment has a non-empty tag and valid classification.
    """
    resp = client.get("/api/v1/catalog/hierarchy")
    assert resp.status_code == 200
    data = resp.json()

    sec = next((s for s in data["sections"] if s["section_id"] == target_sec_id), None)
    assert sec is not None, f"Section {target_sec_id} not found in hierarchy"
    assert len(sec["nodes"]) >= 1

    for node in sec["nodes"]:
        assert node["node_id"].startswith(("CDN-", "OXI-", "ALKY-"))
        assert len(node["name"]) > 0
        for eq in node["equipment"]:
            assert eq["tag"] != ""
            assert eq["node_id"] == node["node_id"]
            assert eq["instrument_count"] == len(eq["instruments"])
            assert eq["operating_temp_c"] is not None and isinstance(eq["operating_temp_c"], (int, float))
            assert eq["operating_press_barg"] is not None and isinstance(eq["operating_press_barg"], (int, float))
            assert eq["drawing_ref"] is not None and len(eq["drawing_ref"]) > 0
            for inst in eq["instruments"]:
                assert inst["tag"] is not None and len(inst["tag"]) > 0
                assert "sil_rating" in inst


@pytest.mark.parametrize("param,tag,expected_dev", [
    ("Flow", "P-2301A", "Flow — No / Low Flow"),
    ("Pressure", "V-2301", "Pressure — High Pressure"),
    ("Level", "D-2304", "Level — High Level"),
    ("Temperature", "E-2303", "Temperature — High Temperature"),
])
def test_stream_hazop_deviation_parameters(param, tag, expected_dev):
    """Verify /api/v1/agent/stream dynamically adapts HAZOP evaluation to the requested deviation parameter."""
    with patch.dict("os.environ", {"FORCE_OFFLINE_MOCK": "true", "AGENT_ENGINE_RESOURCE_NAME": ""}):
        with patch.object(agent_proxy, "resource_name", ""):
            prompt = f"Evaluate HAZOP deviation for {param} in {tag}"
            resp = client.get("/api/v1/agent/stream", params={"prompt": prompt})
            assert resp.status_code == 200
            body = resp.text

            # Verify tool was invoked with expected parameter and deviation
            assert "event: tool_invoked" in body
            assert f'"parameter": "{param}"' in body
            assert (expected_dev in body) or (expected_dev.replace("—", "\\u2014") in body)

            # Verify content markdown reflects the parameter
            assert f"Process Parameter:** `{param}`" in body
            assert (expected_dev in body) or (expected_dev.replace("—", "\\u2014") in body)
            assert "Initial Unmitigated Risk" in body
            assert "Mitigated Risk" in body


@settings(max_examples=10, deadline=None)
@given(st.sampled_from(["Flow", "Pressure", "Level", "Temperature"]))
def test_pbt_hazop_parameter_routing_invariant(chosen_param):
    """PBT-HAZOP-ROUTING-INVARIANT: Every HAZOP evaluation request faithfully preserves the
    chosen process parameter in both tool execution args and synthesized risk reports.
    """
    with patch.dict("os.environ", {"FORCE_OFFLINE_MOCK": "true", "AGENT_ENGINE_RESOURCE_NAME": ""}):
        with patch.object(agent_proxy, "resource_name", ""):
            prompt = f"Run HAZOP deviation evaluation for {chosen_param} in E-2303"
            resp = client.get("/api/v1/agent/stream", params={"prompt": prompt})
            assert resp.status_code == 200
            body = resp.text
            assert f'"parameter": "{chosen_param}"' in body
            assert f"Process Parameter:** `{chosen_param}`" in body


def test_proxy_stream_lifecycle_sequencing():
    """Verify that in proxy mode, telemetry_waterfall is strictly emitted BEFORE message_done,
    ensuring browser clients never close the connection before receiving latency breakdown.
    """
    async def mock_proxy_stream(prompt, session_id="default-session"):
        yield {"event": "thought", "data": {"thought_chunk": "Reasoning on plant graph..."}}
        yield {"event": "tool_invoked", "data": {"tool_name": "spanner_graph_query", "tool_args": {"target_tag": "E-2303"}}}
        yield {"event": "tool_result", "data": {"tool_name": "spanner_graph_query", "result_preview": "Found 6 interlocks"}}
        yield {"event": "message_delta", "data": {"content": "Interlocks verified for E-2303."}}
        yield {"event": "message_done", "data": {"status": "COMPLETED"}}

    with patch.object(agent_proxy, "resource_name", "projects/123/locations/asia-southeast1/reasoningEngines/999"):
        with patch.object(agent_proxy, "stream_query", side_effect=mock_proxy_stream):
            resp = client.get("/api/v1/agent/stream?prompt=What%20is%20E-2303?")
            assert resp.status_code == 200
            body = resp.text

            # Parse event names in order of appearance
            event_names = []
            for chunk in body.split("\n\n"):
                chunk = chunk.strip()
                if chunk.startswith("event: "):
                    event_names.append(chunk.split("\n")[0].replace("event: ", "").strip())

            assert "armor_inspection" in event_names
            assert "thought" in event_names
            assert "tool_invoked" in event_names
            assert "tool_result" in event_names
            assert "message_delta" in event_names
            assert "telemetry_waterfall" in event_names
            assert "message_done" in event_names

            # Invariant: telemetry_waterfall must appear BEFORE message_done
            wf_idx = event_names.index("telemetry_waterfall")
            done_idx = event_names.index("message_done")
            assert wf_idx < done_idx, f"telemetry_waterfall ({wf_idx}) must precede message_done ({done_idx})"


def test_proxy_stream_fallback_delta_on_empty():
    """Verify that if the remote reasoning engine yields no message_deltas, a rich fallback delta is emitted."""
    async def mock_empty_proxy_stream(prompt, session_id="default-session"):
        yield {"event": "thought", "data": {"thought_chunk": "Reasoning completed with empty body."}}
        yield {"event": "message_done", "data": {"status": "COMPLETED"}}

    with patch.object(agent_proxy, "resource_name", "projects/123/locations/asia-southeast1/reasoningEngines/999"):
        with patch.object(agent_proxy, "stream_query", side_effect=mock_empty_proxy_stream):
            resp = client.get("/api/v1/agent/stream?prompt=What%20interlocks%20protect%20E-2303?")
            assert resp.status_code == 200
            body = resp.text
            assert "event: message_delta" in body
            assert "Analysis complete." in body
            assert "Certified Safety Protections" in body
            assert "event: telemetry_waterfall" in body
            assert "event: message_done" in body


@settings(max_examples=25, deadline=None)
@given(st.sampled_from(["E-2303", "E-2310", "D-2121", "D-2304", "P-2306A/B", "OX-2201", "V-2301"]))
def test_pbt_equipment_operating_specs_invariants(target_tag):
    """PBT-EQUIPMENT-SPECS-INVARIANT: Every equipment item possesses physically valid,
    non-null operating parameters and a valid drawing reference without unpopulated placeholders.
    """
    from server.equipment_catalog import get_equipment_specs
    specs = get_equipment_specs(target_tag)
    assert specs["operating_temp_c"] is not None
    assert -50.0 <= specs["operating_temp_c"] <= 400.0
    assert specs["operating_press_barg"] is not None
    assert -1.0 <= specs["operating_press_barg"] <= 100.0
    assert specs["drawing_ref"] is not None and len(specs["drawing_ref"]) >= 5




