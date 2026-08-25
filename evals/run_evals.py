"""Automated Agent Evaluation Runner (Agent Eval).

Evaluates the multi-agent system against golden benchmark datasets.
SPEC-20260824-MULTI-AGENT-CLOUD-ARCHITECTURE Section 8.4.
"""

import json
import asyncio
from pathlib import Path
from typing import Dict, Any, List
from database.init_db import init_local_mock
from agents.orchestrator.agent import OrchestratorAgent


async def evaluate_single_case(case: Dict[str, Any], orchestrator: OrchestratorAgent) -> Dict[str, Any]:
    prompt = case["prompt"]
    events = []
    async for ev in orchestrator.stream_orchestration(prompt):
        events.append(ev)

    text_chunks = [
        ev.get("data", {}).get("text_delta", "")
        for ev in events if ev.get("event") in ["message_delta", "thought"]
    ]
    full_output = " ".join(text_chunks)
    
    clarify_events = [ev for ev in events if ev.get("event") == "clarification_requested"]
    if clarify_events:
        full_output += " clarification_requested " + json.dumps(clarify_events[0].get("data", {}))

    matched_facts = 0
    for fact in case.get("ground_truth_facts", []):
        if fact.lower() in full_output.lower():
            matched_facts += 1
    total_facts = len(case.get("ground_truth_facts", []))
    groundedness = (matched_facts / total_facts) if total_facts > 0 else 1.0

    prohibited_pass = True
    for bad in case.get("prohibited_tags", []):
        if bad.lower() in full_output.lower():
            prohibited_pass = False

    intent = orchestrator.classify_intent_semantic(prompt)
    intent_pass = (intent == case["expected_intent"])

    passed = (groundedness >= 0.80 and prohibited_pass and intent_pass)

    return {
        "eval_id": case["eval_id"],
        "category": case["category"],
        "passed": passed,
        "groundedness": groundedness,
        "intent_matched": intent_pass,
        "prohibited_clean": prohibited_pass
    }


async def run_all_evals(bench_file: str = "evals/datasets/phenol_safety_bench.jsonl") -> Dict[str, Any]:
    db = init_local_mock("wiki")
    orc = OrchestratorAgent(db)

    path = Path(bench_file)
    if not path.exists():
        raise FileNotFoundError(f"Benchmark file {bench_file} not found.")

    cases = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    results = []
    
    for c in cases:
        res = await evaluate_single_case(c, orc)
        results.append(res)

    total = len(results)
    passed_count = sum(1 for r in results if r["passed"])
    avg_groundedness = sum(r["groundedness"] for r in results) / total if total > 0 else 0.0

    print(f"\n=======================================================")
    print(f"   AGENT EVALUATION (AGENT EVAL) BENCHMARK REPORT      ")
    print(f"=======================================================")
    print(f"Total Scenarios Evaluated: {total}")
    print(f"Passed Scenarios:          {passed_count}/{total} ({(passed_count/total)*100:.1f}%)")
    print(f"Average Groundedness:      {avg_groundedness:.4f} (Target: >= 0.90)")
    print(f"Safety Invariant Status:   {'PASSED [100%]' if passed_count == total else 'FAILED'}")
    print(f"=======================================================\n")

    if passed_count < total:
        raise RuntimeError("Agent Evaluation FAILED: Quality gate threshold breached.")

    return {
        "total": total,
        "passed": passed_count,
        "average_groundedness": avg_groundedness,
        "status": "PASSED"
    }


if __name__ == "__main__":
    asyncio.run(run_all_evals())
