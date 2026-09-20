"""Syncs all refinery equipment into Google Cloud Dataplex Knowledge Catalog (Entry Group: phenol-psi).

Uses Dataplex REST API v1 with Application Default Credentials (ADC).
"""

import os
import sys
import re
import time
from pathlib import Path

# Ensure project root is in sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import httpx
import google.auth
from google.auth.transport.requests import Request
from database.init_db import get_database

PROJECT_ID = os.getenv("GCP_PROJECT", "cs-poc-y03r7kmfyov4kilzg50fd7s")
LOCATION = os.getenv("GCP_REGION", "asia-southeast1")
ENTRY_GROUP = "phenol-psi"
ENTRY_TYPE = f"projects/{PROJECT_ID}/locations/{LOCATION}/entryTypes/process-safety-equipment"


def sanitize_entry_id(tag: str) -> str:
    """Dataplex entry IDs must be lowercase, alphanumeric, or hyphen."""
    clean = tag.lower().replace("/", "-").replace("_", "-")
    return re.sub(r'[^a-z0-9-]', '', clean)


def get_auth_token() -> str:
    credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
    if not credentials.valid:
        credentials.refresh(Request())
    return credentials.token


def sync_dataplex_entries():
    token = get_auth_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "X-Goog-User-Project": PROJECT_ID,
        "Content-Type": "application/json"
    }

    db = get_database()
    equipment_items = list(db.equipment.values())
    print(f"[DATAPLEX SYNC] Found {len(equipment_items)} equipment items to sync to Dataplex '{ENTRY_GROUP}'...")

    base_url = f"https://dataplex.googleapis.com/v1/projects/{PROJECT_ID}/locations/{LOCATION}/entryGroups/{ENTRY_GROUP}/entries"
    created = 0
    existing = 0

    with httpx.Client(timeout=15.0) as client:
        for idx, eq in enumerate(equipment_items):
            entry_id = sanitize_entry_id(eq.equipment_tag)
            entry_url = f"{base_url}/{entry_id}"

            # Check if exists
            check_resp = client.get(entry_url, headers=headers)
            if check_resp.status_code == 200:
                existing += 1
                continue

            # Create entry
            create_url = f"{base_url}?entryId={entry_id}"
            payload = {
                "entryType": ENTRY_TYPE,
                "entrySource": {
                    "system": "Refinery PSI System",
                    "displayName": f"{eq.equipment_tag} — {eq.name[:100]}",
                    "description": (eq.description_summary or eq.name)[:400],
                    "updateTime": "2026-06-16T00:00:00Z",
                    "location": LOCATION
                }
            }
            create_resp = client.post(create_url, headers=headers, json=payload)
            if create_resp.status_code in (200, 201):
                created += 1
                print(f"  [{idx+1}/{len(equipment_items)}] Created Dataplex entry: {entry_id}")
            else:
                print(f"  [{idx+1}/{len(equipment_items)}] Notice for {entry_id}: {create_resp.status_code} - {create_resp.text[:120]}")

    print(f"[DATAPLEX SYNC COMPLETE] {created} created, {existing} already present in Dataplex Entry Group '{ENTRY_GROUP}'.")


if __name__ == "__main__":
    sync_dataplex_entries()
