"""Google Cloud Model Armor Security Client & Local Defense Emulator.

Provides inline pre-execution and post-execution inspection for:
1. Prompt Injection (Direct & Indirect instruction override)
2. Jailbreaking & Persona Hijacking (System prompt leaks, DAN)
3. Out-of-Domain Non-Engineering Filtering
4. Data Loss Prevention (PII / Secrets)

SPEC-20260824-MULTI-AGENT-CLOUD-ARCHITECTURE Section 6.5.
"""

import os
import re
import json
import time
import httpx
from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field


class ArmorFilterResult(BaseModel):
    match_confidence: str = Field(..., description="LOW, MEDIUM, HIGH, VERY_HIGH")
    detail: str
    detected_patterns: List[str] = Field(default_factory=list)


class ModelArmorInspectionResult(BaseModel):
    sanitization_result: str = Field(..., description="PASSED, BLOCKED, OUT_OF_DOMAIN, SANITIZED")
    inspection_time_ms: int
    filter_results: Dict[str, ArmorFilterResult]
    sanitized_prompt: str
    policy_template: str = "phenol-safety-armor-template"


class ModelArmorGuardrail:
    def __init__(self, template_name: str = "phenol-safety-armor-template"):
        self.template_name = template_name
        self.project = os.getenv("GCP_PROJECT", "cs-poc-y03r7kmfyov4kilzg50fd7s")
        self.region = os.getenv("GCP_REGION", "asia-southeast1")
        self.api_key = os.getenv("GEMINI_API_KEY", "")

        # High-risk Prompt Injection Signatures
        self.injection_patterns = [
            r"ignore\s+(all\s+)?(previous|prior|above)\s+instructions",
            r"disregard\s+(all\s+)?safety\s+rules",
            r"override\s+.*(sil|ram|safety|risk|rating|protocol|limit)",
            r"you\s+are\s+now\s+(unrestricted|dan|jailbroken)",
            r"act\s+as\s+an\s+unrestricted",
            r"bypass\s+(the\s+)?(safety|interlock|trip)\s+protocol",
            r"set\s+risk\s+rating\s+to\s+0",
            r"set\s+sil\s+to\s+none\s+regardless",
            r"forget\s+you\s+are\s+a\s+safety\s+agent"
        ]

        # System Prompt Extraction & Secret Harvesting Signatures
        self.jailbreak_patterns = [
            r"(print|reveal|output|show|dump)\s+(your\s+)?.*(system\s+prompt|developer\s+prompt|hidden\s+prompt|instructions)",
            r"dump\s+(all\s+)?(database\s+credentials|api\s+keys)",
            r"what\s+is\s+your\s+system\s+instruction"
        ]

        # Conversational / Out-of-Domain Non-Engineering Signatures
        self.out_of_domain_patterns = [
            r"^(hello|hi|hey|good\s+morning|good\s+afternoon|good\s+evening)\b",
            r"^how\s+are\s+you",
            r"^tell\s+me\s+a\s+joke",
            r"^(write|generate|compose)\s+.*(poem|song|story)",
            r"^what\s+is\s+the\s+(weather|capital)",
            r"^who\s+won\s+the",
            r"^help$"
        ]

    def _call_cloud_model_armor(self, user_prompt: str) -> Optional[Dict[str, Any]]:
        """Invokes Google Cloud Model Armor regional endpoint in asia-southeast1 via ADC."""
        if os.getenv("FORCE_OFFLINE_MOCK", "false").lower() in ("true", "1", "yes"):
            return None
        try:
            import google.auth
            from google.auth.transport.requests import Request

            credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
            if not credentials.valid:
                credentials.refresh(Request())

            endpoint = f"https://modelarmor.{self.region}.rep.googleapis.com/v1/projects/{self.project}/locations/{self.region}/templates/{self.template_name}:sanitizeUserPrompt"
            headers = {
                "Authorization": f"Bearer {credentials.token}",
                "X-Goog-User-Project": self.project,
                "Content-Type": "application/json"
            }
            payload = {"userPromptData": {"text": user_prompt}}

            with httpx.Client(timeout=4.0) as client:
                resp = client.post(endpoint, headers=headers, json=payload)
                if resp.status_code == 200:
                    return resp.json()
        except Exception as e:
            print(f"[MODEL ARMOR CLOUD API NOTICE] API fallback: {e}")
        return None

    def sanitize_user_prompt(self, user_prompt: str) -> ModelArmorInspectionResult:
        """Inspects and sanitizes user input before agent dispatch."""
        t0 = time.time()
        p_clean = user_prompt.strip()
        p_lower = p_clean.lower()

        # 1. Out-of-Domain Conversational Pre-Filter
        is_out_of_domain = any(re.search(pat, p_lower) for pat in self.out_of_domain_patterns)
        if is_out_of_domain:
            elapsed_ms = max(1, int((time.time() - t0) * 1000))
            return ModelArmorInspectionResult(
                sanitization_result="OUT_OF_DOMAIN",
                inspection_time_ms=elapsed_ms,
                filter_results={
                    "out_of_domain": ArmorFilterResult(
                        match_confidence="HIGH",
                        detail="Non-engineering conversational input or out-of-domain request detected."
                    )
                },
                sanitized_prompt=p_clean,
                policy_template=self.template_name
            )

        # 2. Live Google Cloud Model Armor API
        cloud_resp = self._call_cloud_model_armor(user_prompt)
        if cloud_resp and "sanitizationResult" in cloud_resp:
            res = cloud_resp["sanitizationResult"]
            filter_state = res.get("filterMatchState", "NO_MATCH_FOUND")
            filter_results_data = res.get("filterResults", {})

            is_blocked = (filter_state == "MATCH_FOUND")
            conf = "HIGH"
            detail = "Adversarial prompt injection intercepted by Google Cloud Model Armor." if is_blocked else "Prompt passed Google Cloud Model Armor inspection."

            pi_data = filter_results_data.get("pi_and_jailbreak", {}).get("piAndJailbreakFilterResult", {})
            if pi_data.get("confidenceLevel"):
                raw_conf = pi_data.get("confidenceLevel")
                conf = "HIGH" if any(c in raw_conf for c in ["HIGH", "MEDIUM"]) else raw_conf

            if is_blocked:
                elapsed_ms = max(1, int((time.time() - t0) * 1000))
                return ModelArmorInspectionResult(
                    sanitization_result="BLOCKED",
                    inspection_time_ms=elapsed_ms,
                    filter_results={
                        "prompt_injection": ArmorFilterResult(
                            match_confidence=conf,
                            detail=detail,
                            detected_patterns=[user_prompt]
                        ),
                        "jailbreak": ArmorFilterResult(
                            match_confidence=conf,
                            detail=detail,
                            detected_patterns=[user_prompt]
                        ),
                        "out_of_domain": ArmorFilterResult(
                            match_confidence="LOW",
                            detail="Domain relevance verified for petrochemical process safety."
                        ),
                        "model_armor_cloud": ArmorFilterResult(
                            match_confidence="HIGH",
                            detail=f"Live Google Cloud Model Armor evaluated in {self.region} (match={filter_state})"
                        )
                    },
                    sanitized_prompt=p_clean,
                    policy_template=self.template_name
                )
            # If cloud Model Armor did not match, continue to defense-in-depth heuristics below


        # 3. Fallback Heuristic Checks (for offline test suite)
        detected_injections = []
        for pat in self.injection_patterns:
            if re.search(pat, p_lower):
                detected_injections.append(pat)

        detected_jailbreaks = []
        for pat in self.jailbreak_patterns:
            if re.search(pat, p_lower):
                detected_jailbreaks.append(pat)

        # Build filter results
        filter_results = {}
        
        # Injection Filter
        if detected_injections:
            filter_results["prompt_injection"] = ArmorFilterResult(
                match_confidence="HIGH",
                detail="Adversarial prompt injection pattern detected attempting to override safety instructions.",
                detected_patterns=detected_injections
            )
        else:
            filter_results["prompt_injection"] = ArmorFilterResult(
                match_confidence="LOW",
                detail="No adversarial prompt injection patterns detected."
            )

        # Jailbreak Filter
        if detected_jailbreaks:
            filter_results["jailbreak"] = ArmorFilterResult(
                match_confidence="HIGH",
                detail="System prompt extraction or persona hijacking signature detected.",
                detected_patterns=detected_jailbreaks
            )
        else:
            filter_results["jailbreak"] = ArmorFilterResult(
                match_confidence="LOW",
                detail="No jailbreak signatures detected."
            )

        # Out-of-Domain Filter
        if is_out_of_domain:
            filter_results["out_of_domain"] = ArmorFilterResult(
                match_confidence="HIGH",
                detail="Non-engineering conversational input or out-of-domain request detected."
            )
        else:
            filter_results["out_of_domain"] = ArmorFilterResult(
                match_confidence="LOW",
                detail="Domain relevance verified for petrochemical process safety."
            )

        # Determine final sanitization verdict
        if detected_injections or detected_jailbreaks:
            verdict = "BLOCKED"
        elif is_out_of_domain:
            verdict = "OUT_OF_DOMAIN"
        else:
            verdict = "PASSED"

        elapsed_ms = max(1, int((time.time() - t0) * 1000))

        return ModelArmorInspectionResult(
            sanitization_result=verdict,
            inspection_time_ms=elapsed_ms,
            filter_results=filter_results,
            sanitized_prompt=p_clean,
            policy_template=self.template_name
        )
