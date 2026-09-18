"""Unit and Integration Tests for FastAPI Server & Streaming Endpoints (Step 7.0).

Verifies Cloud Run healthz, UI serving, SSE event streams, and clarification endpoints.
"""

import pytest
from fastapi.testclient import TestClient
from server.main import app

client = TestClient(app)


def test_healthz_endpoint():
    """Verify Cloud Run liveness probe."""
    resp = client.get("/healthz")
    assert resp.status_code == 200
    assert resp.json()["status"] == "HEALTHY"


def test_ui_root_endpoint():
    """Verify UI HTML is served at root."""
    resp = client.get("/")
    assert resp.status_code == 200
    assert "Refinery Phenol Process Safety" in resp.text



def test_query_endpoint():
    """Verify direct POST /api/v1/agent/query."""
    resp = client.post("/api/v1/agent/query", json={"prompt": "What trips protect E-2303?"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "SUCCESS"
    assert len(data["events"]) > 0


def test_clarify_endpoint():
    """Verify POST /api/v1/agent/clarify."""
    resp = client.post("/api/v1/agent/clarify", json={
        "session_id": "test-sess",
        "selected_option_id": "P-2301A/B",
        "target_tag": "P-2301A/B"
    })
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "RESUMED"
    assert data["resolved_tag"] == "P-2301A/B"


def test_graph_topology_endpoint():
    """Verify GET /api/v1/graph/topology returns valid Spanner graph nodes and edges."""
    resp = client.get("/api/v1/graph/topology")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "SUCCESS"
    assert "nodes" in data and len(data["nodes"]) > 0
    assert "edges" in data and len(data["edges"]) > 0
    assert "stats" in data
    assert data["stats"]["equipment_count"] > 0
    assert data["stats"]["feed_edges_count"] > 0

    # Ensure both equipment and instruments are present
    types = {n["type"] for n in data["nodes"]}
    assert "equipment" in types
    assert "instrument" in types

    # Ensure edge types include FEEDS and TRIPS
    edge_types = {e["type"] for e in data["edges"]}
    assert "FEEDS" in edge_types
    assert "TRIPS" in edge_types


from hypothesis import given, strategies as st

@given(st.sampled_from(["equipment", "instrument"]))
def test_pbt_graph_topology_validity(node_type):
    """PBT-GRAPH-TOPOLOGY-VALIDITY: Ensure all edges connect valid declared nodes in the topology."""
    resp = client.get("/api/v1/graph/topology")
    assert resp.status_code == 200
    data = resp.json()
    node_ids = {n["id"] for n in data["nodes"]}

    for edge in data["edges"]:
        assert edge["source"] in node_ids, f"Edge source {edge['source']} not found in nodes"
        assert edge["target"] in node_ids, f"Edge target {edge['target']} not found in nodes"
        assert edge["type"] in ["FEEDS", "TRIPS"]

