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
    assert "PTT GC Phenol Process Safety" in resp.text


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
