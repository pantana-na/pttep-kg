"""Cloud Spanner Database HAZOP Seeder & Migration Script.

Migrates all authoritative process safety deviations, initiating causes,
5x5 RAM consequences, SIS safeguards, and action items directly into
Google Cloud Spanner (safety-db).
Governed by: SPEC-20260920-ZERO-HARDCODED-DATA-AND-DB-DRIVEN-ARCHITECTURE.md.
"""

import json
import os
import sys
from pathlib import Path
from google.cloud import spanner

PROJECT_ID = os.getenv("GCP_PROJECT", "cs-poc-y03r7kmfyov4kilzg50fd7s")
INSTANCE_ID = os.getenv("SPANNER_INSTANCE", "phenol-process-graph")
DATABASE_ID = os.getenv("SPANNER_DATABASE", "safety-db")

SEED_FILE = Path(__file__).parent.parent / "database" / "seeds" / "spanner_hazop.json"


def seed_spanner_hazop():
    print(f"Connecting to Cloud Spanner: {PROJECT_ID} / {INSTANCE_ID} / {DATABASE_ID}...")
    if not SEED_FILE.exists():
        raise FileNotFoundError(f"HAZOP seed file not found: {SEED_FILE}")

    data = json.loads(SEED_FILE.read_text(encoding="utf-8"))
    deviations = data.get("deviations", [])
    causes = data.get("causes", [])
    consequences = data.get("consequences", [])
    safeguards = data.get("safeguards", [])
    action_items = data.get("action_items", [])

    client = spanner.Client(project=PROJECT_ID)
    instance = client.instance(INSTANCE_ID)
    db = instance.database(DATABASE_ID)

    # 1. Seed Deviations
    print(f"\n[1/5] Seeding Deviations table ({len(deviations)} records)...")
    def write_deviations(transaction):
        rows = [
            (
                d["deviation_id"],
                d["node_id"],
                d["parameter"],
                d["guideword"],
                d["deviation_label"],
                d["sequence_number"],
                d.get("embedding")
            )
            for d in deviations
        ]
        transaction.insert_or_update(
            "Deviations",
            columns=["DeviationId", "NodeId", "Parameter", "Guideword", "DeviationLabel", "SequenceNumber", "Embedding"],
            values=rows
        )
    db.run_in_transaction(write_deviations)
    print(f"  ✓ Seeded {len(deviations)} Deviations successfully.")

    # 2. Seed Causes
    print(f"\n[2/5] Seeding Causes table ({len(causes)} records)...")
    def write_causes(transaction):
        rows = [
            (
                c["cause_id"],
                c["deviation_id"],
                c.get("equipment_tag"),
                c["description"]
            )
            for c in causes
        ]
        transaction.insert_or_update(
            "Causes",
            columns=["CauseId", "DeviationId", "EquipmentTag", "Description"],
            values=rows
        )
    db.run_in_transaction(write_causes)
    print(f"  ✓ Seeded {len(causes)} Causes successfully.")

    # 3. Seed Consequences
    print(f"\n[3/5] Seeding Consequences table ({len(consequences)} records)...")
    def write_consequences(transaction):
        rows = [
            (
                c["consequence_id"],
                c["cause_id"],
                c["causal_chain"],
                c["severity_people"],
                c["severity_environment"],
                c["severity_economic"],
                c["severity_social"],
                c["initial_likelihood"],
                c["initial_risk_rating"]
            )
            for c in consequences
        ]
        transaction.insert_or_update(
            "Consequences",
            columns=[
                "ConsequenceId", "CauseId", "CausalChain",
                "SeverityPeople", "SeverityEnvironment", "SeverityEconomic", "SeveritySocial",
                "InitialLikelihood", "InitialRiskRating"
            ],
            values=rows
        )
    db.run_in_transaction(write_consequences)
    print(f"  ✓ Seeded {len(consequences)} Consequences successfully.")

    # 4. Seed Safeguards
    print(f"\n[4/5] Seeding Safeguards table ({len(safeguards)} records)...")
    def write_safeguards(transaction):
        rows = [
            (
                s["safeguard_id"],
                s["consequence_id"],
                s.get("instrument_tag"),
                s["description"],
                s.get("is_interlock_esd", False),
                s.get("ipl_credit_level", 0)
            )
            for s in safeguards
        ]
        transaction.insert_or_update(
            "Safeguards",
            columns=["SafeguardId", "ConsequenceId", "InstrumentTag", "Description", "IsInterlockEsd", "IplCreditLevel"],
            values=rows
        )
    db.run_in_transaction(write_safeguards)
    print(f"  ✓ Seeded {len(safeguards)} Safeguards successfully.")

    # 5. Seed ActionItems
    print(f"\n[5/5] Seeding ActionItems table ({len(action_items)} records)...")
    def write_action_items(transaction):
        rows = [
            (
                a["action_id"],
                a["consequence_id"],
                a["node_id"],
                a["recommendation_text"],
                a["risk_rank"],
                a.get("discipline"),
                a.get("owner_type"),
                a.get("owner"),
                a.get("due_date"),
                a.get("status", "Open"),
                a.get("mitigated_likelihood"),
                a.get("mitigated_risk_rating"),
                a.get("residual_likelihood"),
                a.get("residual_risk_rating")
            )
            for a in action_items
        ]
        transaction.insert_or_update(
            "ActionItems",
            columns=[
                "ActionId", "ConsequenceId", "NodeId", "RecommendationText", "RiskRank",
                "Discipline", "OwnerType", "Owner", "DueDate", "Status",
                "MitigatedLikelihood", "MitigatedRiskRating", "ResidualLikelihood", "ResidualRiskRating"
            ],
            values=rows
        )
    db.run_in_transaction(write_action_items)
    print(f"  ✓ Seeded {len(action_items)} ActionItems successfully.")

    # Verification snapshot
    print("\n[VERIFICATION] Verifying records directly in Cloud Spanner SQL...")
    for tbl in ["Deviations", "Causes", "Consequences", "Safeguards", "ActionItems"]:
        with db.snapshot() as s:
            cnt = list(s.execute_sql(f"SELECT COUNT(1) FROM {tbl}"))[0][0]
            print(f"  - {tbl}: {cnt} rows")

    print("\n=======================================================")
    print("  CLOUD SPANNER HAZOP TABLES SEEDED SUCCESSFULLY!      ")
    print("=======================================================")


if __name__ == "__main__":
    seed_spanner_hazop()
