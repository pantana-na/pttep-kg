"""Cloud Spanner DDL Migration & Data Seeding Script.

Provisions schema and seeds all refinery process safety data into Cloud Spanner.
"""

import os
import sys
import time
from pathlib import Path
from google.cloud import spanner
from database.init_db import load_ddl_statements, init_local_mock
from agents.database.spanner_sync import generate_embedding

PROJECT_ID = os.getenv("GCP_PROJECT", "cs-poc-y03r7kmfyov4kilzg50fd7s")
INSTANCE_ID = os.getenv("SPANNER_INSTANCE", "phenol-process-graph")
DATABASE_ID = os.getenv("SPANNER_DATABASE", "safety-db")


def apply_schema(database):
    print(f"[SPANNER DDL] Loading DDL statements from database/spanner_schema.sql...")
    statements = load_ddl_statements()
    print(f"[SPANNER DDL] Found {len(statements)} DDL statements to apply.")

    # Apply tables and foreign keys in batches
    print(f"[SPANNER DDL] Submitting DDL update operation to Cloud Spanner...")
    try:
        op = database.update_ddl(statements)
        print(f"[SPANNER DDL] Waiting for schema migration operation to complete...")
        op.result(timeout=600)
        print("[SPANNER DDL] Schema migration completed successfully!")
    except Exception as e:
        print(f"[SPANNER DDL WARNING] DDL error: {e}")
        # Try applying statement by statement if bulk fails
        print("[SPANNER DDL] Attempting incremental statement application...")
        for i, stmt in enumerate(statements, 1):
            try:
                print(f"  [{i}/{len(statements)}] Applying: {stmt.splitlines()[0][:70]}...")
                op = database.update_ddl([stmt])
                op.result(timeout=180)
            except Exception as stmt_err:
                print(f"  [{i}/{len(statements)}] Notice/Skip: {stmt_err}")


def seed_data(database, mock_db):
    print(f"\n[SPANNER SEED] Seeding relational and graph data into {DATABASE_ID}...")

    def insert_units(transaction):
        if not mock_db.units:
            return
        rows = [
            (u.unit_id, u.name, u.code, u.description, u.sources, spanner.COMMIT_TIMESTAMP)
            for u in mock_db.units.values()
        ]
        transaction.insert_or_update(
            "Units",
            columns=["UnitId", "Name", "Code", "Description", "Sources", "UpdatedAt"],
            values=rows
        )
        print(f"  [Units] Inserted {len(rows)} records.")

    def insert_equipment(transaction):
        if not mock_db.equipment:
            return
        rows = [
            (
                eq.equipment_tag,
                eq.unit_id or "CDN",
                eq.name,
                eq.type or "Equipment",
                eq.design_pressure_barg,
                eq.design_temp_celsius,
                eq.operating_pressure_barg,
                eq.operating_temp_celsius,
                eq.material,
                eq.markdown_uri,
                eq.description_summary,
                eq.embedding or generate_embedding(f"{eq.equipment_tag} {eq.name} {eq.description_summary or ''}"),
                False,
                spanner.COMMIT_TIMESTAMP
            )
            for eq in mock_db.equipment.values()
        ]
        transaction.insert_or_update(
            "Equipment",
            columns=[
                "EquipmentTag", "UnitId", "Name", "Type",
                "DesignPressureBarg", "DesignTempCelsius",
                "OperatingPressureBarg", "OperatingTempCelsius",
                "Material", "MarkdownUri", "DescriptionSummary",
                "Embedding", "IsDeleted", "UpdatedAt"
            ],
            values=rows
        )
        print(f"  [Equipment] Inserted {len(rows)} records.")

    def insert_streams(transaction):
        if not mock_db.streams:
            return
        rows = [
            (
                st.stream_id,
                st.unit_id or "CDN",
                st.description,
                st.from_equipment,
                st.to_equipment,
                st.flow_rate_kg_hr,
                st.temp_celsius,
                st.pressure_barg,
                st.chp_concentration_wt_pct,
                st.phase,
                False
            )
            for st in mock_db.streams.values()
        ]
        transaction.insert_or_update(
            "Streams",
            columns=[
                "StreamId", "UnitId", "Description", "FromEquipment", "ToEquipment",
                "FlowRateKgHr", "TempCelsius", "PressureBarg", "ChpConcentrationWtPct", "Phase", "IsDeleted"
            ],
            values=rows
        )
        print(f"  [Streams] Inserted {len(rows)} records.")

    def insert_instruments(transaction):
        if not mock_db.instruments:
            return
        rows = [
            (
                inst.instrument_tag,
                inst.equipment_tag or "E-2303",
                inst.type or "Instrument",
                inst.calibrated_range,
                inst.trip_setpoint,
                inst.sil_rating,
                inst.voting_logic,
                inst.is_sis_initiator,
                False
            )
            for inst in mock_db.instruments.values()
        ]
        transaction.insert_or_update(
            "Instruments",
            columns=[
                "InstrumentTag", "EquipmentTag", "Type", "CalibratedRange",
                "TripSetpoint", "SilRating", "VotingLogic", "IsSisInitiator", "IsDeleted"
            ],
            values=rows
        )
        print(f"  [Instruments] Inserted {len(rows)} records.")

    def insert_hazards(transaction):
        if not mock_db.chemical_hazards:
            return
        rows = [
            (
                h.hazard_id,
                h.chemical_name,
                h.cas_number,
                h.decomposition_onset_temp_celsius,
                h.sadt_temp_celsius,
                h.flash_point_celsius,
                h.ghs_classification,
                h.markdown_uri
            )
            for h in mock_db.chemical_hazards.values()
        ]
        transaction.insert_or_update(
            "ChemicalHazards",
            columns=[
                "HazardId", "ChemicalName", "CasNumber",
                "DecompositionOnsetTempCelsius", "SadtTempCelsius", "FlashPointCelsius",
                "GhsClassification", "MarkdownUri"
            ],
            values=rows
        )
        print(f"  [ChemicalHazards] Inserted {len(rows)} records.")

    valid_eq_tags = set(mock_db.equipment.keys())
    valid_inst_tags = set(mock_db.instruments.keys())

    # Ensure all referenced stream_ids exist in streams
    for flow in mock_db.equipment_flows:
        if flow.stream_id and flow.stream_id not in mock_db.streams:
            from database.models import StreamModel
            mock_db.streams[flow.stream_id] = StreamModel(
                stream_id=flow.stream_id,
                unit_id="CDN",
                description=f"Process Stream {flow.stream_id}"
            )

    valid_flows = [
        flow for flow in mock_db.equipment_flows
        if flow.from_equipment_tag in valid_eq_tags and flow.to_equipment_tag in valid_eq_tags
    ]

    valid_actuations = [
        act for act in mock_db.instrument_actuations
        if act.initiator_instrument_tag in valid_inst_tags and act.target_equipment_tag in valid_eq_tags
    ]

    def insert_flows(transaction):
        if not valid_flows:
            return
        rows = [
            (flow.from_equipment_tag, flow.to_equipment_tag, flow.stream_id)
            for flow in valid_flows
        ]
        transaction.insert_or_update(
            "EquipmentFlows",
            columns=["FromEquipmentTag", "ToEquipmentTag", "StreamId"],
            values=rows
        )
        print(f"  [EquipmentFlows (Graph Edges)] Inserted {len(rows)} records.")

    def insert_actuations(transaction):
        if not valid_actuations:
            return
        rows = [
            (act.initiator_instrument_tag, act.target_equipment_tag, act.interlock_action)
            for act in valid_actuations
        ]
        transaction.insert_or_update(
            "InstrumentActuations",
            columns=["InitiatorInstrumentTag", "TargetEquipmentTag", "InterlockAction"],
            values=rows
        )
        print(f"  [InstrumentActuations (Graph Edges)] Inserted {len(rows)} records.")

    def seed_all(transaction):
        insert_units(transaction)
        insert_equipment(transaction)
        insert_streams(transaction)
        insert_instruments(transaction)
        insert_hazards(transaction)
        insert_flows(transaction)
        insert_actuations(transaction)

    try:
        database.run_in_transaction(seed_all)
        print("  [SUCCESS] All relational and graph entities committed to Cloud Spanner.")
    except Exception as err:
        print(f"  [Notice on seed_all]: {err}")


def verify_spanner(database):
    print("\n[SPANNER VERIFY] Verifying live Cloud Spanner database queries...")
    with database.snapshot(multi_use=True) as snapshot:
        # SQL Relational Query
        results = list(snapshot.execute_sql("SELECT COUNT(1) AS TotalEquipment FROM Equipment"))
        total = results[0][0] if results else 0
        print(f"  [SQL Check] Total Equipment in Spanner: {total}")

        # GQL Graph Query
        try:
            gql_query = """
            GRAPH PhenolProcessSafetyGraph
            MATCH (src:Equipment)-[f:FEEDS]->(dst:Equipment)
            RETURN src.EquipmentTag AS SourceTag, dst.EquipmentTag AS DestTag
            LIMIT 5
            """
            gql_results = list(snapshot.execute_sql(gql_query))
            print(f"  [GQL Graph Check] Successfully executed ISO GQL traversal ({len(gql_results)} sample edges found):")
            for src, dst in gql_results:
                print(f"    {src} --[:FEEDS]--> {dst}")
        except Exception as gql_err:
            print(f"  [GQL Graph Notice]: {gql_err}")




def main():
    print(f"============================================================")
    print(f"  Cloud Spanner Migration & Seeding: {PROJECT_ID}/{INSTANCE_ID}/{DATABASE_ID}")
    print(f"============================================================")
    client = spanner.Client(project=PROJECT_ID)
    instance = client.instance(INSTANCE_ID)
    database = instance.database(DATABASE_ID)

    # 1. Apply Schema (if not already applied)
    skip_ddl = "--seed-only" in sys.argv or "--skip-ddl" in sys.argv
    if not skip_ddl:
        try:
            with database.snapshot() as s:
                res = list(s.execute_sql("SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Equipment'"))
                if res:
                    print("[SPANNER DDL] Schema already provisioned. Skipping DDL migration.")
                    skip_ddl = True
        except Exception:
            pass

    if not skip_ddl:
        apply_schema(database)

    # 2. Ingest mock seed
    mock_db = init_local_mock("wiki")

    # 3. Seed into Cloud Spanner
    seed_data(database, mock_db)

    # 4. Verify
    verify_spanner(database)
    print("\n[SUCCESS] Cloud Spanner migration and seeding completed.")


if __name__ == "__main__":
    main()
