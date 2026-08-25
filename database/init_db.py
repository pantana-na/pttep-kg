"""Database initialization and schema management for Cloud Spanner Graph & Local Seeding.

Supports live Cloud Spanner provisioning and in-memory mock initialization.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = os.getenv("GCP_PROJECT", "cs-poc-y03r7kmfyov4kilzg50fd7s")
INSTANCE_ID = os.getenv("SPANNER_INSTANCE", "phenol-process-graph")
DATABASE_ID = os.getenv("SPANNER_DATABASE", "safety-db")


def load_ddl_statements(schema_path: str = "database/spanner_schema.sql") -> list:
    content = Path(schema_path).read_text(encoding="utf-8")
    # Split on semicolon while ignoring comments
    statements = []
    current = []
    for line in content.splitlines():
        clean = line.strip()
        if not clean or clean.startswith("--"):
            continue
        current.append(line)
        if clean.endswith(";"):
            stmt = "\n".join(current).rstrip(";").strip()
            if stmt:
                statements.append(stmt)
            current = []
    return statements


def init_live_spanner():
    """Initializes Cloud Spanner instance, database, and DDL tables on GCP."""
    try:
        from google.cloud import spanner
        client = spanner.Client(project=PROJECT_ID)
        instance = client.instance(INSTANCE_ID)
        
        if not instance.exists():
            print(f"[LIVE SPANNER] Creating Spanner Instance '{INSTANCE_ID}' in project '{PROJECT_ID}'...")
            config_name = f"{client.project_name}/instanceConfigs/regional-asia-southeast1"
            op = instance.create(
                configuration_name=config_name,
                node_count=1,
                display_name="Phenol Process Safety Graph Instance"
            )
            op.result(timeout=300)
            print(f"[LIVE SPANNER] Instance '{INSTANCE_ID}' created successfully.")

        database = instance.database(DATABASE_ID)
        if not database.exists():
            print(f"[LIVE SPANNER] Creating Database '{DATABASE_ID}' with DDL schema...")
            ddl_statements = load_ddl_statements()
            op = database.create(ddl_statements=ddl_statements)
            op.result(timeout=300)
            print(f"[LIVE SPANNER] Database '{DATABASE_ID}' and Property Graph created successfully.")
        else:
            print(f"[LIVE SPANNER] Database '{DATABASE_ID}' already exists.")
            
        return database
    except Exception as e:
        print(f"[LIVE SPANNER NOTICE] Could not connect to live Cloud Spanner: {e}")
        print("[LIVE SPANNER NOTICE] Running in Local Mock / Test Mode.")
        return None


def init_local_mock(wiki_dir: str = "wiki"):
    """Initializes and seeds an in-memory Spanner property graph mock from local wiki."""
    from database.mock_spanner import MockSpannerDatabase
    db = MockSpannerDatabase()
    db.seed_from_wiki(wiki_dir)
    print(f"[MOCK SPANNER] Seeded {len(db.equipment)} equipment, {len(db.units)} units, {len(db.chemical_hazards)} hazards, {len(db.equipment_flows)} flow edges.")
    return db


if __name__ == "__main__":
    print(f"Initializing Phenol Process Safety Database for project {PROJECT_ID}...")
    db = init_local_mock()
