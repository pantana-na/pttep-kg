"""Live Cloud Spanner Property Graph & Relational Database Client.

Implements ISO GQL graph traversal, full-text token search, and vector cosine distance
directly against Google Cloud Spanner (PhenolProcessSafetyGraph).
"""

import os
from typing import List, Dict, Any, Optional, Tuple
from google.cloud import spanner
from google.cloud.spanner_v1.param_types import Array, FLOAT64, STRING, INT64
from database.models import (
    EquipmentModel, UnitModel, InstrumentModel, ChemicalHazardModel,
    EquipmentFlowEdge, InstrumentActuationEdge
)


class SpannerDatabaseClient:
    """Client for querying live Google Cloud Spanner Property Graph and tables."""

    def __init__(
        self,
        project_id: Optional[str] = None,
        instance_id: Optional[str] = None,
        database_id: Optional[str] = None
    ):
        self.project_id = project_id or os.getenv("GCP_PROJECT", "cs-poc-y03r7kmfyov4kilzg50fd7s")
        self.instance_id = instance_id or os.getenv("SPANNER_INSTANCE", "phenol-process-graph")
        self.database_id = database_id or os.getenv("SPANNER_DATABASE", "safety-db")

        self.client = spanner.Client(project=self.project_id)
        self.instance = self.client.instance(self.instance_id)
        self.database = self.instance.database(self.database_id)

        # In-memory cached lookup dictionaries
        self.equipment: Dict[str, EquipmentModel] = {}
        self.units: Dict[str, UnitModel] = {}
        self.instruments: Dict[str, InstrumentModel] = {}
        self.chemical_hazards: Dict[str, ChemicalHazardModel] = {}
        self.streams: Dict[str, Any] = {}
        self.hazop_nodes: Dict[str, Any] = {}
        self.deviations: Dict[str, Any] = {}
        self.causes: Dict[str, Any] = {}
        self.consequences: Dict[str, Any] = {}
        self.safeguards: Dict[str, Any] = {}
        self.action_items: Dict[str, Any] = {}
        self.node_equipment_map: List[Any] = []
        self.equipment_flows: List[EquipmentFlowEdge] = []
        self.instrument_actuations: List[InstrumentActuationEdge] = []
        self.knowledge_catalog: Dict[str, Any] = {}

        # Warm up cache from Spanner
        self.refresh_cache()

    def clear(self):
        self.equipment.clear()
        self.units.clear()
        self.instruments.clear()
        self.chemical_hazards.clear()
        self.streams.clear()
        self.hazop_nodes.clear()
        self.deviations.clear()
        self.causes.clear()
        self.consequences.clear()
        self.safeguards.clear()
        self.action_items.clear()
        self.node_equipment_map.clear()
        self.equipment_flows.clear()
        self.instrument_actuations.clear()
        self.knowledge_catalog.clear()

    def refresh_cache(self):
        """Loads cached models from Cloud Spanner into memory for sub-millisecond local reads."""
        try:
            # 1. Units
            with self.database.snapshot() as snapshot:
                unit_rows = list(snapshot.execute_sql("SELECT UnitId, Name, Code, Description, Sources FROM Units"))
            for row in unit_rows:
                self.units[row[0]] = UnitModel(
                    unit_id=row[0], name=row[1], code=row[2],
                    description=row[3], sources=row[4] or []
                )

            # 2. Equipment
            with self.database.snapshot() as snapshot:
                eq_rows = list(snapshot.execute_sql(
                    "SELECT EquipmentTag, UnitId, Name, Type, DesignPressureBarg, DesignTempCelsius, "
                    "OperatingPressureBarg, OperatingTempCelsius, Material, MarkdownUri, DescriptionSummary, Embedding "
                    "FROM Equipment WHERE IsDeleted = false"
                ))
            for row in eq_rows:
                self.equipment[row[0]] = EquipmentModel(
                    equipment_tag=row[0], unit_id=row[1], name=row[2], type=row[3],
                    design_pressure_barg=row[4], design_temp_celsius=row[5],
                    operating_pressure_barg=row[6], operating_temp_celsius=row[7],
                    material=row[8], markdown_uri=row[9], description_summary=row[10],
                    embedding=row[11] or []
                )

            # 3. Instruments
            with self.database.snapshot() as snapshot:
                inst_rows = list(snapshot.execute_sql(
                    "SELECT InstrumentTag, EquipmentTag, Type, CalibratedRange, TripSetpoint, SilRating, VotingLogic, IsSisInitiator "
                    "FROM Instruments WHERE IsDeleted = false"
                ))
            for row in inst_rows:
                self.instruments[row[0]] = InstrumentModel(
                    instrument_tag=row[0], equipment_tag=row[1], type=row[2],
                    calibrated_range=row[3], trip_setpoint=row[4], sil_rating=row[5],
                    voting_logic=row[6], is_sis_initiator=row[7]
                )

            # 4. Chemical Hazards
            with self.database.snapshot() as snapshot:
                haz_rows = list(snapshot.execute_sql(
                    "SELECT HazardId, ChemicalName, CasNumber, DecompositionOnsetTempCelsius, SadtTempCelsius, "
                    "FlashPointCelsius, GhsClassification, MarkdownUri FROM ChemicalHazards"
                ))
            for row in haz_rows:
                self.chemical_hazards[row[0]] = ChemicalHazardModel(
                    hazard_id=row[0], chemical_name=row[1], cas_number=row[2],
                    decomposition_onset_temp_celsius=row[3], sadt_temp_celsius=row[4],
                    flash_point_celsius=row[5], ghs_classification=row[6] or [],
                    markdown_uri=row[7]
                )

            # 5. Graph Edges
            with self.database.snapshot() as snapshot:
                flow_rows = list(snapshot.execute_sql("SELECT FromEquipmentTag, ToEquipmentTag, StreamId FROM EquipmentFlows"))
            self.equipment_flows = [
                EquipmentFlowEdge(from_equipment_tag=r[0], to_equipment_tag=r[1], stream_id=r[2])
                for r in flow_rows
            ]

            with self.database.snapshot() as snapshot:
                act_rows = list(snapshot.execute_sql("SELECT InitiatorInstrumentTag, TargetEquipmentTag, InterlockAction FROM InstrumentActuations"))
            self.instrument_actuations = [
                InstrumentActuationEdge(initiator_instrument_tag=r[0], target_equipment_tag=r[1], interlock_action=r[2])
                for r in act_rows
            ]

            print(f"[SPANNER CLIENT] Cache initialized from live Spanner: {len(self.equipment)} equipment, {len(self.instruments)} instruments, {len(self.equipment_flows)} flow edges.")
        except Exception as e:
            print(f"[SPANNER CLIENT NOTICE] Failed to cache from Spanner: {e}")

    def keyword_search(self, query: str, limit: int = 10) -> List[Tuple[str, float, EquipmentModel]]:
        """Executes full-text search directly on Spanner using SEARCH function."""
        try:
            with self.database.snapshot() as snapshot:
                sql = """
                SELECT EquipmentTag, Name, Type, DescriptionSummary, MarkdownUri,
                       SCORE(EquipmentTokens, @query) AS relevance_score
                FROM Equipment
                WHERE SEARCH(EquipmentTokens, @query) AND IsDeleted = false
                ORDER BY relevance_score DESC
                LIMIT @limit
                """
                params = {"query": query, "limit": limit}
                param_types = {"query": STRING, "limit": INT64}
                rows = list(snapshot.execute_sql(sql, params=params, param_types=param_types))
                results = []
                for row in rows:
                    tag = row[0]
                    score = float(row[5]) if row[5] is not None else 1.0
                    eq = self.equipment.get(tag) or EquipmentModel(
                        equipment_tag=row[0], name=row[1], type=row[2],
                        description_summary=row[3], markdown_uri=row[4]
                    )
                    results.append((tag, score, eq))
                if results:
                    return results
        except Exception as err:
            print(f"[SPANNER SEARCH NOTICE] Full-text search fallback: {err}")

        # Fallback to in-memory keyword matching if index still building
        query_tokens = query.lower().split()
        fallback_results = []
        for tag, eq in self.equipment.items():
            text = f"{eq.equipment_tag} {eq.name} {eq.description_summary or ''}".lower()
            score = sum(5.0 if t == eq.equipment_tag.lower() else 1.0 for t in query_tokens if t in text)
            if score > 0:
                fallback_results.append((tag, score, eq))
        fallback_results.sort(key=lambda x: x[1], reverse=True)
        return fallback_results[:limit]

    def vector_search(self, query_embedding: List[float], limit: int = 10) -> List[Tuple[str, float, EquipmentModel]]:
        """Executes vector cosine distance query directly in Cloud Spanner."""
        try:
            with self.database.snapshot() as snapshot:
                sql = """
                SELECT EquipmentTag,
                       1.0 - COSINE_DISTANCE(Embedding, @query_vec) AS cosine_sim
                FROM Equipment
                WHERE Embedding IS NOT NULL AND IsDeleted = false
                ORDER BY cosine_sim DESC
                LIMIT @limit
                """
                params = {"query_vec": query_embedding, "limit": limit}
                param_types = {"query_vec": Array(FLOAT64), "limit": INT64}
                rows = list(snapshot.execute_sql(sql, params=params, param_types=param_types))
                results = []
                for row in rows:
                    tag = row[0]
                    sim = float(row[1]) if row[1] is not None else 0.0
                    eq = self.equipment.get(tag)
                    if eq:
                        results.append((tag, sim, eq))
                if results:
                    return results
        except Exception as err:
            print(f"[SPANNER VECTOR NOTICE] Vector search fallback: {err}")

        # Fallback in-memory cosine similarity
        results = []
        for tag, eq in self.equipment.items():
            if eq.embedding:
                dot = sum(a * b for a, b in zip(query_embedding, eq.embedding))
                norm1 = sum(a * a for a in query_embedding) ** 0.5
                norm2 = sum(b * b for b in eq.embedding) ** 0.5
                sim = dot / (norm1 * norm2) if norm1 > 0 and norm2 > 0 else 0.0
                if sim > 0:
                    results.append((tag, sim, eq))
        results.sort(key=lambda x: x[1], reverse=True)
        return results[:limit]

    def graph_traverse_upstream(self, target_tag: str, max_depth: int = 3) -> List[Dict[str, Any]]:
        """Executes ISO GQL graph traversal on PhenolProcessSafetyGraph in Cloud Spanner."""
        try:
            with self.database.snapshot() as snapshot:
                gql = f"""
                GRAPH PhenolProcessSafetyGraph
                MATCH (src:Equipment) -[:FEEDS]->{{1,{max_depth}}} (dst:Equipment {{EquipmentTag: @target_tag}})
                RETURN DISTINCT src.EquipmentTag AS upstream_tag,
                                src.Name AS equipment_name,
                                src.OperatingTempCelsius AS temp_celsius
                LIMIT 20
                """
                params = {"target_tag": target_tag}
                param_types = {"target_tag": STRING}
                rows = list(snapshot.execute_sql(gql, params=params, param_types=param_types))
                results = []
                for row in rows:
                    results.append({
                        "upstream_tag": row[0],
                        "equipment_name": row[1] or "",
                        "temp_celsius": float(row[2]) if row[2] is not None else None,
                        "depth": 1,
                        "stream_id": "PROCESS_STREAM"
                    })
                if results:
                    return results
        except Exception as err:
            print(f"[SPANNER GQL NOTICE] Graph upstream GQL fallback: {err}")

        # Fallback in-memory BFS
        visited = set()
        queue = [(target_tag, 0)]
        results = []
        while queue:
            curr, depth = queue.pop(0)
            if depth >= max_depth:
                continue
            for flow in self.equipment_flows:
                if flow.to_equipment_tag == curr and flow.from_equipment_tag not in visited:
                    visited.add(flow.from_equipment_tag)
                    eq = self.equipment.get(flow.from_equipment_tag)
                    results.append({
                        "upstream_tag": flow.from_equipment_tag,
                        "equipment_name": eq.name if eq else "",
                        "temp_celsius": eq.operating_temp_celsius if eq else None,
                        "depth": depth + 1,
                        "stream_id": flow.stream_id
                    })
                    queue.append((flow.from_equipment_tag, depth + 1))
        return results

    def graph_find_interlocks(self, target_equipment_tag: str) -> List[Dict[str, Any]]:
        """Executes ISO GQL interlock trip query in Cloud Spanner."""
        try:
            with self.database.snapshot() as snapshot:
                gql = """
                GRAPH PhenolProcessSafetyGraph
                MATCH (inst:Instruments)-[act:ACTUATES_INTERLOCK]->(eq:Equipment {EquipmentTag: @target_tag})
                RETURN inst.InstrumentTag AS instrument_tag,
                       inst.Type AS type,
                       inst.SilRating AS sil_rating,
                       inst.VotingLogic AS voting_logic,
                       inst.TripSetpoint AS trip_setpoint,
                       act.InterlockAction AS interlock_action
                """
                params = {"target_tag": target_equipment_tag}
                param_types = {"target_tag": STRING}
                rows = list(snapshot.execute_sql(gql, params=params, param_types=param_types))
                results = []
                for row in rows:
                    results.append({
                        "instrument_tag": row[0],
                        "type": row[1] or "Instrument",
                        "sil_rating": row[2] or "None",
                        "voting_logic": row[3] or "1oo1",
                        "trip_setpoint": row[4],
                        "interlock_action": row[5] or "TRIP_ACTION"
                    })
                if results:
                    return results
        except Exception as err:
            print(f"[SPANNER GQL NOTICE] Graph interlocks GQL fallback: {err}")

        # Fallback in-memory
        results = []
        for act in self.instrument_actuations:
            if act.target_equipment_tag == target_equipment_tag:
                inst = self.instruments.get(act.initiator_instrument_tag)
                results.append({
                    "instrument_tag": act.initiator_instrument_tag,
                    "type": inst.type if inst else "Unknown",
                    "sil_rating": inst.sil_rating if inst else "None",
                    "voting_logic": inst.voting_logic if inst else "1oo1",
                    "trip_setpoint": inst.trip_setpoint if inst else None,
                    "interlock_action": act.interlock_action
                })
        return results

    def register_knowledge_catalog_entry(self, entry_id: str, entry_data: Dict[str, Any]) -> Dict[str, Any]:
        self.knowledge_catalog[entry_id] = entry_data
        return entry_data

    def get_knowledge_catalog_entry(self, entry_id: str) -> Optional[Dict[str, Any]]:
        return self.knowledge_catalog.get(entry_id)
