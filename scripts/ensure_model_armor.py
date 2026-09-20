#!/usr/bin/env python3
"""Idempotently ensures Google Cloud Model Armor Template has Responsible AI filters set to LOW_AND_ABOVE.

Governed by SPEC-20260918-MODEL-INTENT-DISPATCH-AND-CLEANUP and GEMINI.md.
"""

import os
import sys
import json
import httpx
from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.getenv("GCP_PROJECT", "cs-poc-y03r7kmfyov4kilzg50fd7s")
REGION = os.getenv("GCP_REGION", "asia-southeast1")
TEMPLATE_ID = os.getenv("PROD_MODEL_ARMOR_TEMPLATE", "phenol-safety-armor-template").split("/")[-1]

BASE_URL = f"https://modelarmor.{REGION}.rep.googleapis.com/v1/projects/{PROJECT_ID}/locations/{REGION}/templates"


def get_auth_token():
    try:
        import google.auth
        from google.auth.transport.requests import Request

        creds, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
        if not creds.valid:
            creds.refresh(Request())
        return creds.token
    except Exception as e:
        print(f"[MODEL ARMOR SCRIPT] Warning: Unable to get ADC credentials: {e}")
        return None


def ensure_model_armor_template():
    token = get_auth_token()
    if not token:
        print("[MODEL ARMOR SCRIPT] Skipping Model Armor configuration (no ADC token available).")
        return

    headers = {
        "Authorization": f"Bearer {token}",
        "X-Goog-User-Project": PROJECT_ID,
        "Content-Type": "application/json"
    }

    template_url = f"{BASE_URL}/{TEMPLATE_ID}"

    target_rai_filters = [
        {"filterType": "HATE_SPEECH", "confidenceLevel": "LOW_AND_ABOVE"},
        {"filterType": "DANGEROUS", "confidenceLevel": "LOW_AND_ABOVE"},
        {"filterType": "SEXUALLY_EXPLICIT", "confidenceLevel": "LOW_AND_ABOVE"},
        {"filterType": "HARASSMENT", "confidenceLevel": "LOW_AND_ABOVE"}
    ]

    target_filter_config = {
        "raiSettings": {
            "raiFilters": target_rai_filters
        },
        "piAndJailbreakFilterSettings": {
            "filterEnforcement": "ENABLED",
            "confidenceLevel": "MEDIUM_AND_ABOVE"
        }
    }

    with httpx.Client(timeout=10.0) as client:
        # Check if template exists
        resp = client.get(template_url, headers=headers)
        if resp.status_code == 200:
            existing = resp.json()
            print(f"[MODEL ARMOR SCRIPT] Found existing template: {TEMPLATE_ID}")
            current_filters = existing.get("filterConfig", {}).get("raiSettings", {}).get("raiFilters", [])
            
            # Check if update is required
            all_low = all(f.get("confidenceLevel") == "LOW_AND_ABOVE" for f in current_filters) and len(current_filters) >= 4
            if all_low:
                print("[MODEL ARMOR SCRIPT] Responsible AI filters are already verified as 'LOW_AND_ABOVE' for all categories.")
                return

            print("[MODEL ARMOR SCRIPT] Updating Responsible AI filters to 'LOW_AND_ABOVE' across all categories...")
            patch_payload = {
                "filterConfig": target_filter_config
            }
            patch_url = f"{template_url}?updateMask=filterConfig.raiSettings,filterConfig.piAndJailbreakFilterSettings"
            patch_resp = client.patch(patch_url, headers=headers, json=patch_payload)
            if patch_resp.status_code in (200, 201):
                print("[MODEL ARMOR SCRIPT] Successfully updated Model Armor Responsible AI filters to 'LOW_AND_ABOVE'.")
            else:
                print(f"[MODEL ARMOR SCRIPT] Warning: Patch returned status {patch_resp.status_code}: {patch_resp.text}")
        elif resp.status_code == 404:
            print(f"[MODEL ARMOR SCRIPT] Template {TEMPLATE_ID} not found. Creating new template with LOW_AND_ABOVE RAI filters...")
            create_payload = {
                "filterConfig": target_filter_config,
                "templateMetadata": {
                    "filterVersionSelector": {
                        "alias": "FILTER_VERSION_ALIAS_STABLE"
                    },
                    "dataResidencyCompliant": True
                }
            }
            create_url = f"{BASE_URL}?templateId={TEMPLATE_ID}"
            create_resp = client.post(create_url, headers=headers, json=create_payload)
            if create_resp.status_code in (200, 201):
                print("[MODEL ARMOR SCRIPT] Successfully created Model Armor template with LOW_AND_ABOVE RAI filters.")
            else:
                print(f"[MODEL ARMOR SCRIPT] Error creating template: {create_resp.status_code} - {create_resp.text}")
        else:
            print(f"[MODEL ARMOR SCRIPT] Unexpected response querying template: {resp.status_code} - {resp.text}")


if __name__ == "__main__":
    ensure_model_armor_template()
