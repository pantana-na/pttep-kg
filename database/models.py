"""Data models for Cloud Spanner Graph & Relational Entities.

Corresponds to SPEC-20260824-MULTI-AGENT-CLOUD-ARCHITECTURE Section 3.2.
"""

from typing import List, Optional, Any, Dict
from datetime import date, datetime
from pydantic import BaseModel, Field


class UnitModel(BaseModel):
    unit_id: str = Field(..., max_length=64, description="Unique Unit Identifier, e.g. U-2300")
    name: str = Field(..., max_length=128, description="Unit Name, e.g. Cumene Cleavage & Decomposition Unit")
    code: str = Field(..., max_length=32, description="Unit Code, e.g. CDN")
    description: Optional[str] = None
    sources: List[str] = Field(default_factory=list)
    updated_at: Optional[datetime] = None


class EquipmentModel(BaseModel):
    equipment_tag: str = Field(..., max_length=64, description="Primary Key, e.g. E-2303, D-2304")
    unit_id: str = Field(..., max_length=64)
    name: str = Field(..., max_length=128)
    type: str = Field(..., max_length=64, description="Vessel, HeatExchanger, Pump, Column, Reactor, Filter, Package")
    design_pressure_barg: Optional[float] = None
    design_temp_celsius: Optional[float] = None
    operating_pressure_barg: Optional[float] = None
    operating_temp_celsius: Optional[float] = None
    material: Optional[str] = Field(None, max_length=128)
    markdown_uri: Optional[str] = Field(None, max_length=256)
    description_summary: Optional[str] = None
    embedding: Optional[List[float]] = None
    is_deleted: bool = False
    updated_at: Optional[datetime] = None


class StreamModel(BaseModel):
    stream_id: str = Field(..., max_length=64, description="Stream tag or number, e.g. S-2301")
    unit_id: str = Field(..., max_length=64)
    description: Optional[str] = Field(None, max_length=256)
    from_equipment: Optional[str] = Field(None, max_length=64)
    to_equipment: Optional[str] = Field(None, max_length=64)
    flow_rate_kg_hr: Optional[float] = None
    temp_celsius: Optional[float] = None
    pressure_barg: Optional[float] = None
    chp_concentration_wt_pct: Optional[float] = None
    phase: Optional[str] = Field(None, max_length=64)
    is_deleted: bool = False


class InstrumentModel(BaseModel):
    instrument_tag: str = Field(..., max_length=64, description="Instrument Tag, e.g. TXSHH-0502A")
    equipment_tag: str = Field(..., max_length=64)
    type: str = Field(..., max_length=64, description="PT, TT, FT, LT, PSV, CV, Analyzer")
    calibrated_range: Optional[str] = Field(None, max_length=64)
    trip_setpoint: Optional[str] = Field(None, max_length=64)
    sil_rating: Optional[str] = Field("None", max_length=32, description="None, SIL 1, SIL 2, SIL 3")
    voting_logic: Optional[str] = Field("1oo1", max_length=32, description="1oo1, 1oo2, 2oo3")
    is_sis_initiator: bool = False
    is_deleted: bool = False


class ChemicalHazardModel(BaseModel):
    hazard_id: str = Field(..., max_length=64)
    chemical_name: str = Field(..., max_length=128)
    cas_number: Optional[str] = Field(None, max_length=64)
    decomposition_onset_temp_celsius: Optional[float] = None
    sadt_temp_celsius: Optional[str] = Field(None, max_length=64)
    flash_point_celsius: Optional[float] = None
    ghs_classification: List[str] = Field(default_factory=list)
    markdown_uri: Optional[str] = Field(None, max_length=256)


class HazopNodeModel(BaseModel):
    node_id: str = Field(..., max_length=64, description="Node Identifier, e.g. CDN-N02")
    name: str = Field(..., max_length=128)
    unit_id: str = Field(..., max_length=64)
    pid_sheet: Optional[str] = Field(None, max_length=128)
    status: Optional[str] = Field("Active", max_length=32)
    is_deleted: bool = False


class DeviationModel(BaseModel):
    deviation_id: str = Field(..., max_length=64)
    node_id: str = Field(..., max_length=64)
    parameter: str = Field(..., max_length=32, description="Flow, Temperature, Pressure, Level, Composition")
    guideword: str = Field(..., max_length=32, description="More, Less, None, Reverse, Higher, Lower")
    deviation_label: str = Field(..., max_length=64, description="e.g. Higher Temperature")
    sequence_number: int
    embedding: Optional[List[float]] = None


class CauseModel(BaseModel):
    cause_id: str = Field(..., max_length=64)
    deviation_id: str = Field(..., max_length=64)
    equipment_tag: Optional[str] = Field(None, max_length=64)
    description: str


class ConsequenceModel(BaseModel):
    consequence_id: str = Field(..., max_length=64)
    cause_id: str = Field(..., max_length=64)
    causal_chain: str
    severity_people: int = Field(..., ge=1, le=5)
    severity_environment: int = Field(..., ge=1, le=5)
    severity_economic: int = Field(..., ge=1, le=5)
    severity_social: int = Field(..., ge=1, le=5)
    initial_likelihood: int = Field(..., ge=1, le=5)
    initial_risk_rating: str = Field(..., max_length=16)


class SafeguardModel(BaseModel):
    safeguard_id: str = Field(..., max_length=64)
    consequence_id: str = Field(..., max_length=64)
    instrument_tag: Optional[str] = Field(None, max_length=64)
    description: str
    is_interlock_esd: bool = False
    ipl_credit_level: int = Field(0, ge=0, le=3)


class ActionItemModel(BaseModel):
    action_id: str = Field(..., max_length=32, description="Action/Recommendation ID, e.g. R-001")
    consequence_id: str = Field(..., max_length=64)
    node_id: str = Field(..., max_length=64)
    recommendation_text: str
    risk_rank: str = Field(..., max_length=16)
    discipline: Optional[str] = Field(None, max_length=64)
    owner_type: Optional[str] = Field(None, max_length=16)
    owner: Optional[str] = Field(None, max_length=128)
    due_date: Optional[date] = None
    status: str = Field("Open", max_length=16)
    mitigated_likelihood: Optional[int] = Field(None, ge=1, le=5)
    mitigated_risk_rating: Optional[str] = Field(None, max_length=16)
    residual_likelihood: Optional[int] = Field(None, ge=1, le=5)
    residual_risk_rating: Optional[str] = Field(None, max_length=16)


# Edge Representations
class EquipmentFlowEdge(BaseModel):
    from_equipment_tag: str
    to_equipment_tag: str
    stream_id: str


class NodeEquipmentEdge(BaseModel):
    node_id: str
    equipment_tag: str


class InstrumentActuationEdge(BaseModel):
    initiator_instrument_tag: str
    target_equipment_tag: str
    interlock_action: str


# Search Result container
class HybridSearchResult(BaseModel):
    entity_tag: str
    entity_type: str
    name: str
    keyword_score: float = 0.0
    vector_score: float = 0.0
    graph_score: float = 0.0
    rrf_score: float = 0.0
    summary: str = ""
    metadata: Dict[str, Any] = Field(default_factory=dict)


class KnowledgeCatalogEntryModel(BaseModel):
    entry_id: str
    entry_group: str = "projects/cs-poc-y03r7kmfyov4kilzg50fd7s/locations/asia-southeast1/entryGroups/phenol-psi"
    display_name: str
    description: Optional[str] = None
    psi_category: int = 6  # Category 6: Process Hazard Analysis & HAZOP
    aspects: Dict[str, Any] = Field(default_factory=dict)
    linked_drawings: List[str] = Field(default_factory=list)
    linked_equipment: List[str] = Field(default_factory=list)
    deliverable_uri: Optional[str] = None
    status: str = "COMPLETE"
    last_updated: Optional[str] = None
