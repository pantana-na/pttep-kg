"""Cloud Spanner Database Catalog Seeder & Migration Script.

Migrates all authoritative equipment operating conditions, design envelopes,
certified drawing references, HazopNodes, and NodeEquipmentMap directly
into Google Cloud Spanner (safety-db).
Governed by: SPEC-20260920-DATABASE-FIRST-EQUIPMENT-CATALOG.md.
"""

import json
import os
import sys
from pathlib import Path
from google.cloud import spanner

PROJECT_ID = os.getenv("GCP_PROJECT", "cs-poc-y03r7kmfyov4kilzg50fd7s")
INSTANCE_ID = os.getenv("SPANNER_INSTANCE", "phenol-process-graph")
DATABASE_ID = os.getenv("SPANNER_DATABASE", "safety-db")

SEED_FILE = Path(__file__).parent.parent / "database" / "seeds" / "spanner_catalog.json"


def seed_spanner_catalog():
    print(f"Connecting to Cloud Spanner: {PROJECT_ID} / {INSTANCE_ID} / {DATABASE_ID}...")
    if not SEED_FILE.exists():
        raise FileNotFoundError(f"Catalog seed file not found: {SEED_FILE}")

    data = json.loads(SEED_FILE.read_text(encoding="utf-8"))
    hazop_nodes = data.get("hazop_nodes", [])
    node_equip_map = data.get("node_equipment_map", [])
    equipment_list = data.get("equipment", [])

    client = spanner.Client(project=PROJECT_ID)
    instance = client.instance(INSTANCE_ID)
    db = instance.database(DATABASE_ID)

    # 1. Seed HazopNodes
    print("\n[1/3] Seeding HazopNodes table in Cloud Spanner...")
    def write_hazop_nodes(transaction):
        rows = [
            (
                n["node_id"],
                n["name"],
                n["unit_id"],
                n.get("pid_sheet", ""),
                n.get("status", "APPROVED"),
                False
            )
            for n in hazop_nodes
        ]
        transaction.insert_or_update(
            "HazopNodes",
            columns=["NodeId", "Name", "UnitId", "PidSheet", "Status", "IsDeleted"],
            values=rows
        )
    db.run_in_transaction(write_hazop_nodes)
    print(f"  ✓ Seeded {len(hazop_nodes)} HazopNodes successfully.")

    # 2. Seed NodeEquipmentMap
    print("\n[2/3] Seeding NodeEquipmentMap table in Cloud Spanner...")
    def write_node_equipment_map(transaction):
        node_equip_rows = [(m["node_id"], m["equipment_tag"]) for m in node_equip_map]
        transaction.insert_or_update(
            "NodeEquipmentMap",
            columns=["NodeId", "EquipmentTag"],
            values=node_equip_rows
        )
    db.run_in_transaction(write_node_equipment_map)
    print(f"  ✓ Seeded {len(node_equip_map)} NodeEquipmentMap mappings successfully.")

    # 3. Update Equipment with operating/design conditions and drawings
    print("\n[3/3] Updating Equipment table with certified conditions in Cloud Spanner...")
    def update_equipment(transaction):
        existing_rows = list(transaction.execute_sql(
            "SELECT EquipmentTag, UnitId, Name, Type, Material, DescriptionSummary FROM Equipment"
        ))
        existing_map = {r[0]: r for r in existing_rows}

        equip_update_rows = []
        for eq in equipment_list:
            tag = eq["equipment_tag"]
            existing = existing_map.get(tag)
            unit_id = eq.get("unit_id") or (existing[1] if existing else "CDN")
            name = eq.get("name") or (existing[2] if existing else tag)
            eq_type = eq.get("type") or (existing[3] if existing else "Equipment")
            material = eq.get("material") or (existing[4] if existing else None)
            desc = eq.get("description_summary") or (existing[5] if existing else name)

            oper_temp = float(eq["operating_temp_celsius"]) if eq.get("operating_temp_celsius") is not None else None
            oper_press = float(eq["operating_pressure_barg"]) if eq.get("operating_pressure_barg") is not None else None
            design_temp = float(eq["design_temp_celsius"]) if eq.get("design_temp_celsius") is not None else None
            design_press = float(eq["design_pressure_barg"]) if eq.get("design_pressure_barg") is not None else None
            drawing_ref = eq.get("markdown_uri")

            equip_update_rows.append((
                tag,
                unit_id,
                name,
                eq_type,
                design_press,
                design_temp,
                oper_press,
                oper_temp,
                material,
                drawing_ref,
                desc,
                False,
                spanner.COMMIT_TIMESTAMP
            ))

        transaction.insert_or_update(
            "Equipment",
            columns=[
                "EquipmentTag", "UnitId", "Name", "Type",
                "DesignPressureBarg", "DesignTempCelsius",
                "OperatingPressureBarg", "OperatingTempCelsius",
                "Material", "MarkdownUri", "DescriptionSummary",
                "IsDeleted", "UpdatedAt"
            ],
            values=equip_update_rows
        )
    db.run_in_transaction(update_equipment)
    print(f"  ✓ Updated {len(equipment_list)} Equipment records with live operating & design conditions.")

    # 4. Verify live Spanner contents
    print("\n[VERIFICATION] Verifying 5 Sample Assets directly in Cloud Spanner SQL...")
    sample_tags = ["E-2303", "V-2301", "D-2121", "D-2304", "P-2301A/B"]
    with db.snapshot() as s:
        results = list(s.execute_sql("""
            SELECT e.EquipmentTag, e.Name, e.OperatingTempCelsius, e.OperatingPressureBarg, e.DesignTempCelsius, e.DesignPressureBarg, e.MarkdownUri, m.NodeId
            FROM Equipment e
            LEFT JOIN NodeEquipmentMap m ON e.EquipmentTag = m.EquipmentTag
            WHERE e.EquipmentTag IN UNNEST(@tags)
        """, params={"tags": sample_tags}, param_types={"tags": spanner.param_types.Array(spanner.param_types.STRING)}))

        for r in results:
            print(f"  - Tag: {r[0]} ({r[1]}) | Node: {r[7]}")
            print(f"    Operating: {r[2]} °C | {r[3]} barg")
            print(f"    Design:    {r[4]} °C | {r[5]} barg")
            print(f"    P&ID Ref:  {r[6]}")
            assert r[2] is not None, f"OperatingTempCelsius must not be NULL for {r[0]}"
            assert r[3] is not None, f"OperatingPressureBarg must not be NULL for {r[0]}"

    print("\n=======================================================")
    print("  CLOUD SPANNER DATABASE CATALOG MIGRATION SUCCESSFUL! ")
    print("=======================================================")


if __name__ == "__main__":
    seed_spanner_catalog()
