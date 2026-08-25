"""Automated Agent Evaluation Test Suite (Step 8.0).

Runs the Golden Process Safety Benchmark and asserts 100% safety invariant compliance.
"""

import pytest
import asyncio
from evals.run_evals import run_all_evals


@pytest.mark.asyncio
async def test_agent_eval_golden_benchmarks():
    """Verify all golden process safety benchmark scenarios pass with Groundedness >= 0.90."""
    result = await run_all_evals("evals/datasets/phenol_safety_bench.jsonl")
    assert result["status"] == "PASSED"
    assert result["passed"] == result["total"]
    assert result["average_groundedness"] >= 0.90
