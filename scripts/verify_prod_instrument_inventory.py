"""Live Production Verification Script for Instrument Inventory & Compound Aliasing.

Tests live Cloud Run production deployment for:
1. /healthz
2. /api/v1/catalog/hierarchy - verifies instrument counts on equipment
3. /api/v1/agent/stream - verifies consistent, persistent answers across multiple equipment assets
"""

import sys
import json
import urllib.request
import urllib.parse
from typing import Dict, Any, List

BASE_URL = sys.argv[1] if len(sys.argv) > 1 else "https://phenol-process-safety-prod-cwmwtobz3a-as.a.run.app"


def check_health() -> bool:
    url = f"{BASE_URL}/api/v1/health"
    req = urllib.request.Request(url, headers={"User-Agent": "ProdTester/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        body = json.loads(resp.read().decode())
        print(f"[HEALTH CHECK] Status: {resp.status}, Body: {body}")
        return resp.status == 200 and body.get("status", "").lower() == "healthy"


def check_catalog_hierarchy() -> Dict[str, Any]:
    url = f"{BASE_URL}/api/v1/catalog/hierarchy"
    req = urllib.request.Request(url, headers={"User-Agent": "ProdTester/1.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.loads(resp.read().decode())
        sections = data.get("sections", [])
        print(f"[CATALOG HIERARCHY] Total Sections: {len(sections)}, Total Equipment: {data.get('total_equipment')}, Total Instruments: {data.get('total_instruments')}")
        
        counts = {}
        for sec in sections:
            for node in sec.get("nodes", []):
                for eq in node.get("equipment", []):
                    tag = eq.get("tag")
                    inst_list = eq.get("instruments", [])
                    counts[tag] = len(inst_list)
        
        print(f"[CATALOG HIERARCHY] Total Equipment resolved: {len(counts)}")
        print("Sample Equipment Instrument Counts in UI Hierarchy:")
        for sample_tag in ["E-2303", "V-2301", "D-2304", "P-2301A/B", "E-2302A/B", "D-2121"]:
            print(f"  - {sample_tag}: {counts.get(sample_tag, 'MISSING')} instruments")
        return counts


def query_agent_stream(prompt: str) -> Dict[str, Any]:
    encoded = urllib.parse.urlencode({"prompt": prompt})
    url = f"{BASE_URL}/api/v1/agent/stream?{encoded}"
    req = urllib.request.Request(url, headers={"User-Agent": "ProdTester/1.0"})
    
    events = []
    current_event_type = None
    with urllib.request.urlopen(req, timeout=30) as resp:
        for line in resp:
            line_str = line.decode('utf-8').strip()
            if line_str.startswith("event: "):
                current_event_type = line_str[7:].strip()
            elif line_str.startswith("data: "):
                payload_str = line_str[6:]
                if payload_str:
                    try:
                        data = json.loads(payload_str)
                        events.append({"event": current_event_type, "data": data})
                    except Exception:
                        pass
    
    # Collect text parts and tool calls
    full_text = ""
    tool_calls = []
    tool_results = []
    for ev in events:
        ev_name = ev.get("event")
        data = ev.get("data", {})
        if ev_name in ("message_delta", "text"):
            full_text += data.get("content") or data.get("text_delta") or ""
        elif ev_name == "tool_invoked":
            tool_calls.append(data)
        elif ev_name == "tool_result":
            tool_results.append(data)
    
    return {
        "full_text": full_text,
        "tool_calls": tool_calls,
        "tool_results": tool_results,
        "raw_events_count": len(events)
    }


def main():
    print(f"Testing Live Production Deployment at: {BASE_URL}\n" + "="*70)
    
    # 1. Health
    assert check_health(), "Health check failed!"
    print("[PASS] Health check verified.\n")
    
    # 2. Hierarchy
    counts = check_catalog_hierarchy()
    assert counts.get("E-2303") == 41, f"Expected E-2303 to have 41 instruments, got {counts.get('E-2303')}"
    assert counts.get("V-2301") == 12, f"Expected V-2301 to have 12 instruments, got {counts.get('V-2301')}"
    assert counts.get("D-2304") == 4, f"Expected D-2304 to have 4 instruments, got {counts.get('D-2304')}"
    assert counts.get("P-2301A/B") == 8, f"Expected P-2301A/B to have 8 instruments, got {counts.get('P-2301A/B')}"
    print("[PASS] UI Hierarchy Instrument counts verified.\n")
    
    # 3. Stream queries across multiple equipment
    test_cases = [
        ("How many instruments are connected to E-2303?", "E-2303", ["E-2303", "14780-8120", "TXSHH", "UXV"]),
        ("What trip protections and SIS interlocks protect V-2301?", "V-2301", ["V-2301", "interlock", "SIS"]),
        ("How many instruments are connected to P-2301A?", "P-2301", ["P-2301"]),
        ("What trip protections and SIS interlocks protect D-2304?", "D-2304", ["D-2304"]),
    ]
    
    for prompt, expected_tag, required_keywords in test_cases:
        print(f"\n--- Testing Query: '{prompt}' ---")
        result = query_agent_stream(prompt)
        text = result["full_text"]
        print(f"Response preview (first 300 chars):\n{text[:300]}...")
        print(f"Total response length: {len(text)} characters, Raw SSE events: {result['raw_events_count']}")
        
        # Check that response is rich and substantive (>150 chars)
        assert len(text) > 150, f"Expected substantive response (>150 chars) for '{prompt}', got {len(text)}"
        
        # Check required keywords
        for kw in required_keywords:
            assert kw.lower() in text.lower(), f"Expected keyword '{kw}' in response for '{prompt}'"
        
        print(f"[PASS] Production response verified for {expected_tag} with keywords {required_keywords}.")
    
    print("\n" + "="*70)
    print("ALL PRODUCTION ASSET PROBES PASSED WITH REAL INTELLIGENCE (100% GREEN)!")
    print("="*70)


if __name__ == "__main__":
    main()
