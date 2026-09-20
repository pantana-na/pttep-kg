# Specification: Database-First Equipment Catalog & Live Spanner Synchronization

**Document ID:** `SPEC-20260920-DATABASE-FIRST-EQUIPMENT-CATALOG`  
**Author:** AI Engineering Team & User Pair  
**Status:** Approved for Implementation  
**Created:** September 20, 2026  
**Governed by:** `GEMINI.md` & `_agents/rules/spec_driven_development.md`

---

## 1. Problem Statement & Motivation

Previously, equipment operating parameters (`OperatingTempCelsius`, `OperatingPressureBarg`), design envelopes (`DesignTempCelsius`, `DesignPressureBarg`), and certified drawing references were stored in a 732-line hardcoded Python dictionary (`server/equipment_catalog.py`). 

### Critical Architecture Flaws of the Previous Design:
1. **Database Drift:** The Cloud Spanner database table `Equipment` contained `NULL` values for `OperatingTempCelsius`, `OperatingPressureBarg`, `DesignTempCelsius`, and `DesignPressureBarg` across all 54 assets. Table `HazopNodes` and `NodeEquipmentMap` were completely empty.
2. **Dual Source of Truth:** The UI queried an API endpoint that masked the empty database columns by falling back to the hardcoded dictionary in code.
3. **Violates DevOps & SDD Standards:** Plant process parameters must reside in the centralized, ACID-compliant database (Cloud Spanner), queryable via standard SQL and ISO GQL property graph traversals by agents, humans, and analytics services.

---

## 2. Target Architecture: Database-First Single Source of Truth

```
┌────────────────────────────────────────────────────────┐
│         Google Cloud Spanner (safety-db)               │
│                                                        │
│  ┌───────────────────────┐  ┌───────────────────────┐  │
│  │   Equipment Table     │  │   HazopNodes Table    │  │
│  │  - EquipmentTag (PK)  │  │  - NodeId (PK)        │  │
│  │  - Name, Type         │  │  - Name, UnitId       │  │
│  │  - OperatingTempC     │  │  - PidSheet           │  │
│  │  - OperatingPressBarg │  └───────────┬───────────┘  │
│  │  - DesignTempC        │              │              │
│  │  - DesignPressBarg    │  ┌───────────▼───────────┐  │
│  │  - MarkdownUri (P&ID) │  │  NodeEquipmentMap     │  │
│  └───────────▲───────────┘  │  - NodeId             │  │
│              │              │  - EquipmentTag       │  │
│              └──────────────┴───────────────────────┘  │
└───────────────────────────▲────────────────────────────┘
                            │ Live SQL / GQL Queries
┌───────────────────────────┴────────────────────────────┐
│      Cloud Run Web Cockpit / FastAPI Server             │
│      (server/main.py: /api/v1/catalog/hierarchy)       │
│                                                        │
│  * Live Database Queries: db.equipment, db.hazop_nodes │
│  * Zero hardcoded dictionaries in code                 │
└────────────────────────────────────────────────────────┘
```

---

## 3. Data Schema & Invariants

### 3.1 Cloud Spanner Table `Equipment` (Target State)
All 54 equipment rows in `Equipment` must be populated with:
- `OperatingTempCelsius` (FLOAT64, NOT NULL): Operating temperature in °C from certified Process Data Sheets.
- `OperatingPressureBarg` (FLOAT64, NOT NULL): Operating pressure in barg from certified Process Data Sheets.
- `DesignTempCelsius` (FLOAT64, NOT NULL): Design maximum temperature in °C.
- `DesignPressureBarg` (FLOAT64, NOT NULL): Design maximum pressure in barg.
- `MarkdownUri` (STRING(256)): Certified As-Built P&ID Drawing reference (e.g. `14780-8120-25-23-0005`).

### 3.2 Cloud Spanner Table `HazopNodes` (Target State)
Populated with 6 nodes across 3 units:
- `CDN-N01`: Cumene Quench Tank & Feed System (Unit: `CDN`)
- `CDN-N02`: Preflash Column & Vaporizer Section (Unit: `CDN`)
- `CDN-N03`: Decomposer Drum & Acid Cleavage Section (Unit: `CDN`)
- `CDN-N04`: Vacuum Producing & Flare System (Unit: `CDN`)
- `OXI-N01`: Oxidation Reactor Loop & Vent Gas Separation (Unit: `OXI`)
- `ALKY-N01`: Feed Fractionation & Alkylation Section (Unit: `ALKY`)

### 3.3 Cloud Spanner Table `NodeEquipmentMap`
Maps every equipment tag to its designated HAZOP node in Cloud Spanner.

---

## 4. Step-by-Step Implementation Plan

### Step 1: Cloud Spanner Seeding & Migration Script (`scripts/seed_spanner_catalog.py`)
- Reads authoritative process specifications and updates live Cloud Spanner tables:
  - `Equipment` (Operating and Design conditions, Drawing refs)
  - `HazopNodes` (6 nodes)
  - `NodeEquipmentMap` (54 mappings)
- Idempotent transaction execution (`insert_or_update`).

### Step 2: Mock Spanner Parity (`database/mock_spanner.py`)
- Synchronize `MockSpannerDatabase` with the exact same seed data for 100% deterministic test parity in offline/unit testing modes.

### Step 3: Refactor Backend API (`server/main.py`)
- Remove hardcoded dictionary dependency (`EQUIPMENT_SPECS` / `server/equipment_catalog.py`).
- Modify `/api/v1/catalog/hierarchy` to construct sections, nodes, and equipment directly from `db.equipment`, `db.hazop_nodes`, and `db.node_equipment_map`.
- Delete `server/equipment_catalog.py`.

### Step 4: Unit & Property-Based Test Verification
- Unit test: verify Cloud Spanner SQL returns non-null operating conditions for all 54 assets.
- Property test: verify universal non-null invariant across all equipment items in database.
- Integration test: verify `/api/v1/catalog/hierarchy` returns live database values.

### Step 5: Production Deployment & Live Cloud Run Probe
- Build and deploy updated container to Cloud Run production (`phenol-process-safety-prod`).
- Verify live endpoint returns database values directly.
