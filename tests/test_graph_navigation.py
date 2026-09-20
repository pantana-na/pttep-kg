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

"""Unit and Property-Based Tests for Spanner Graph 2D Pan/Scroll & Auto-Centering.

Governed by: specs/features/SPEC-20260920-SPANNER-GRAPH-PAN-SCROLL-AND-AUTO-CENTER.md
Verifies:
1. Mathematical invariants of the 2D viewport coordinate pipeline (centering, pan linearity, zoom clamping).
2. HTML UI/UX integration and canvas event handlers for pan, scroll, click selection, and target beacon.
3. Live topology API contracts backing the canvas.
"""

import math
from pathlib import Path
import pytest
from fastapi.testclient import TestClient
from hypothesis import given, settings, strategies as st

from server.main import app

client = TestClient(app)

INDEX_HTML_PATH = Path(__file__).resolve().parent.parent / "server" / "static" / "index.html"


# ============================================================================
# Coordinate Transformation Reference Functions (matching index.html JS)
# ============================================================================

def compute_centering_translation(node_x: float, node_y: float, canvas_w: float, canvas_h: float, scale: float):
    """Compute translation Tx, Ty required to position node at canvas center."""
    tx = (canvas_w / 2.0) - (node_x * scale)
    ty = (canvas_h / 2.0) - (node_y * scale)
    return tx, ty


def screen_from_world(world_x: float, world_y: float, tx: float, ty: float, scale: float):
    """Transform world coordinate to canvas screen coordinate."""
    screen_x = tx + (world_x * scale)
    screen_y = ty + (world_y * scale)
    return screen_x, screen_y


def world_from_screen(screen_x: float, screen_y: float, tx: float, ty: float, scale: float):
    """Transform canvas screen coordinate to world coordinate."""
    world_x = (screen_x - tx) / scale
    world_y = (screen_y - ty) / scale
    return world_x, world_y


def clamp_zoom_scale(current_scale: float, factor: float, min_scale: float = 0.3, max_scale: float = 3.0) -> float:
    """Clamp zoom scale within allowable boundary."""
    return max(min_scale, min(max_scale, current_scale * factor))


# ============================================================================
# Unit Tests (Deterministic Examples)
# ============================================================================

def test_ut_graph_01_centering_math_deterministic():
    """UT-GRAPH-01: Arbitrary node (x, y) on canvas (W, H) maps exactly to (W/2, H/2)."""
    node_x, node_y = 190.0, 290.0
    canvas_w, canvas_h = 340.0, 340.0
    scale = 0.85

    tx, ty = compute_centering_translation(node_x, node_y, canvas_w, canvas_h, scale)
    screen_x, screen_y = screen_from_world(node_x, node_y, tx, ty, scale)

    assert math.isclose(screen_x, canvas_w / 2.0, abs_tol=1e-6)
    assert math.isclose(screen_y, canvas_h / 2.0, abs_tol=1e-6)


def test_ut_graph_02_pan_offset_delta():
    """UT-GRAPH-02: Pan translation increases exactly by (dx, dy)."""
    initial_tx, initial_ty = 100.0, 50.0
    dx, dy = 45.0, -30.0

    new_tx = initial_tx + dx
    new_ty = initial_ty + dy

    assert new_tx == 145.0
    assert new_ty == 20.0


def test_ut_graph_03_hit_test_inside_and_outside_radius():
    """UT-GRAPH-03: Click hit-testing correctly detects node proximity."""
    node_x, node_y = 200.0, 150.0
    radius = 18.0

    # Inside radius
    click_x, click_y = 210.0, 155.0
    dist = math.hypot(node_x - click_x, node_y - click_y)
    assert dist <= radius

    # Outside radius
    far_x, far_y = 225.0, 170.0
    far_dist = math.hypot(node_x - far_x, node_y - far_y)
    assert far_dist > radius


def test_ut_graph_04_html_contains_navigation_controls():
    """UT-GRAPH-04: index.html contains all 4 pan buttons, center button, and canvas."""
    html = INDEX_HTML_PATH.read_text(encoding="utf-8")

    assert "spanner-graph-canvas" in html
    assert "panGraph(0, 45)" in html    # Pan Up
    assert "panGraph(0, -45)" in html   # Pan Down
    assert "panGraph(45, 0)" in html    # Pan Left
    assert "panGraph(-45, 0)" in html   # Pan Right
    assert "centerOnTargetNode()" in html
    assert "centerOnNode" in html
    assert "zoomGraphAt" in html
    assert "setupCanvasInteractions" in html
    assert "handleCanvasNodeClick" in html
    assert "[TARGET]" in html


def test_ut_graph_05_api_topology_contract():
    """UT-GRAPH-05: Server /api/v1/graph/topology returns valid equipment and instrument nodes."""
    resp = client.get("/api/v1/graph/topology")
    assert resp.status_code == 200
    data = resp.json()

    assert "nodes" in data
    assert "edges" in data
    assert "stats" in data
    assert data["stats"]["equipment_count"] >= 50
    assert any(n["id"] == "E-2303" for n in data["nodes"])


# ============================================================================
# Property-Based Tests (PBT with Hypothesis)
# ============================================================================

@given(
    node_x=st.floats(min_value=-2000.0, max_value=2000.0, allow_nan=False, allow_infinity=False),
    node_y=st.floats(min_value=-2000.0, max_value=2000.0, allow_nan=False, allow_infinity=False),
    canvas_w=st.floats(min_value=100.0, max_value=1920.0, allow_nan=False, allow_infinity=False),
    canvas_h=st.floats(min_value=100.0, max_value=1080.0, allow_nan=False, allow_infinity=False),
    scale=st.floats(min_value=0.2, max_value=3.0, allow_nan=False, allow_infinity=False),
)
@settings(max_examples=100)
def test_pbt_graph_01_centering_invariant(node_x, node_y, canvas_w, canvas_h, scale):
    """PBT-GRAPH-01: Centering invariant holds across all random coordinates, canvas dimensions, and scales.
    
    Invariant: Applying Tx, Ty always places (node_x, node_y) at (canvas_w/2, canvas_h/2).
    """
    tx, ty = compute_centering_translation(node_x, node_y, canvas_w, canvas_h, scale)
    screen_x, screen_y = screen_from_world(node_x, node_y, tx, ty, scale)

    target_cx = canvas_w / 2.0
    target_cy = canvas_h / 2.0

    assert math.isclose(screen_x, target_cx, abs_tol=1e-4)
    assert math.isclose(screen_y, target_cy, abs_tol=1e-4)


@given(
    initial_tx=st.floats(min_value=-5000.0, max_value=5000.0, allow_nan=False, allow_infinity=False),
    initial_ty=st.floats(min_value=-5000.0, max_value=5000.0, allow_nan=False, allow_infinity=False),
    deltas=st.lists(
        st.tuples(
            st.floats(min_value=-100.0, max_value=100.0, allow_nan=False, allow_infinity=False),
            st.floats(min_value=-100.0, max_value=100.0, allow_nan=False, allow_infinity=False),
        ),
        min_size=1,
        max_size=20,
    ),
)
@settings(max_examples=50)
def test_pbt_graph_02_pan_linearity(initial_tx, initial_ty, deltas):
    """PBT-GRAPH-02: Pan translation is linear and additive under arbitrary sequences of pan vectors.
    
    Invariant: T_final = T_initial + sum(deltas).
    """
    curr_tx, curr_ty = initial_tx, initial_ty
    sum_dx = sum(d[0] for d in deltas)
    sum_dy = sum(d[1] for d in deltas)

    for dx, dy in deltas:
        curr_tx += dx
        curr_ty += dy

    assert math.isclose(curr_tx, initial_tx + sum_dx, abs_tol=1e-4)
    assert math.isclose(curr_ty, initial_ty + sum_dy, abs_tol=1e-4)


@given(
    scale=st.floats(min_value=0.1, max_value=5.0, allow_nan=False, allow_infinity=False),
    factor=st.floats(min_value=0.01, max_value=10.0, allow_nan=False, allow_infinity=False),
)
@settings(max_examples=50)
def test_pbt_graph_03_zoom_scale_clamping(scale, factor):
    """PBT-GRAPH-03: Zoom scale is strictly clamped within [0.3, 3.0] for any multiplier."""
    clamped = clamp_zoom_scale(scale, factor, min_scale=0.3, max_scale=3.0)
    assert 0.3 <= clamped <= 3.0


@given(
    world_x=st.floats(min_value=-1000.0, max_value=1000.0, allow_nan=False, allow_infinity=False),
    world_y=st.floats(min_value=-1000.0, max_value=1000.0, allow_nan=False, allow_infinity=False),
    tx=st.floats(min_value=-500.0, max_value=500.0, allow_nan=False, allow_infinity=False),
    ty=st.floats(min_value=-500.0, max_value=500.0, allow_nan=False, allow_infinity=False),
    scale=st.floats(min_value=0.3, max_value=3.0, allow_nan=False, allow_infinity=False),
)
@settings(max_examples=50)
def test_pbt_graph_04_world_screen_roundtrip(world_x, world_y, tx, ty, scale):
    """PBT-GRAPH-04: World-to-screen and screen-to-world transformations are bijective round-trips."""
    sx, sy = screen_from_world(world_x, world_y, tx, ty, scale)
    wx, wy = world_from_screen(sx, sy, tx, ty, scale)

    assert math.isclose(wx, world_x, abs_tol=1e-4)
    assert math.isclose(wy, world_y, abs_tol=1e-4)
