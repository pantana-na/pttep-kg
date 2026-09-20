# Specification: 100% Database-Driven Architecture & Zero Hardcoded Data

**Document ID:** `SPEC-20260920-ZERO-HARDCODED-DATA-AND-DB-DRIVEN-ARCHITECTURE`  
**Author:** Lead AI Engineering Team & User Pair  
**Status:** Approved for Implementation  
**Created:** September 20, 2026  
**Governed by:** `GEMINI.md` & `_agents/rules/spec_driven_development.md`

---

## 1. Problem Statement & Motivation

An architectural audit of the codebase revealed that despite the presence of Google Cloud Spanner (`safety-db`), Dataplex Knowledge Catalog (`phenol-psi`), and GCS LLM-Wiki, multiple critical operational datasets and safety logic structures were hardcoded in application code:
1. **Frontend UI (`server/static/index.html`):** Lines 881–918 stored a hardcoded JavaScript dictionary (`docMap`) of drawing numbers and wiki HTML snippets for 5 assets, and lines 846–854 hardcoded a 54-item `knownTags` array.
2. **Backend API (`server/main.py`):** Lines 213–271 hardcoded a static `sections` dictionary defining plant sections and nodes instead of querying `Units` and `HazopNodes` tables from Cloud Spanner. Line 199 hardcoded `"E-2303"` fallback queries.
3. **HAZOP Facilitator (`app/hazop/agent.py`):** Lines 258–450 contained ~200 lines of hardcoded deviation, cause, consequence, initial risk, and safeguard dictionaries (`discover_node_risks`), while lines 76–129 and 204–248 hardcoded equipment condition strings and safeguards.
4. **P&ID Markup Parser (`app/hazop/markup_parser.py`):** Lines 18–45 hardcoded `KNOWN_NODE_METADATA` for Node 23-02 and Node 23-03.
5. **ADK Agent Tool (`app/agent.py`):** Lines 220–231 hardcoded initial risk ratings and safeguards in `evaluate_hazop_deviation`.

### Core Goals:
1. **100% Database-Driven Single Source of Truth:** Populate all HAZOP study entities (`Deviations`, `Causes`, `Consequences`, `Safeguards`, `ActionItems`) and node definitions into Google Cloud Spanner.
2. **Eliminate All Hardcoded Dictionaries:** Delete `docMap`, `knownTags`, `KNOWN_NODE_METADATA`, hardcoded risk worksheets in `app/hazop/agent.py`, and hardcoded sections in `server/main.py`.
3. **Dynamic API & UI Integration:**
   - `GET /api/v1/catalog/hierarchy` queries `Units`, `HazopNodes`, `NodeEquipmentMap`, `Equipment`, and `Instruments` 100% dynamically from Spanner.
   - Add `GET /api/v1/catalog/lineage?tag=...` returning live Dataplex Knowledge Catalog provenance and GCS Wiki content so the UI Right Pane is completely dynamic.
   - Frontend `server/static/index.html` fetches lineage and docs live via API with zero client-side dictionary.
4. **Agent Tools & Prompts Alignment:** Update ADK agent tools to query live Spanner HAZOP tables for deviation risk analysis.
5. **Mandatory Testing:** Deliver Unit Tests and Property-Based Tests (PBT) verifying universal non-null invariants, dynamic queries, and zero hardcoded fallbacks.

---

## 2. Target Architecture & Storage Tier Alignment



---

## 3. Step-by-Step Implementation Plan

### Step 1: Cloud Spanner HAZOP Entities Migration
- Create `scripts/seed_spanner_hazop.py` to seed complete HAZOP relational tables in live Cloud Spanner:
  - `Deviations` (parameters: Flow, Temperature, Pressure, Level, Composition)
  - `Causes` (initiating causes linked to equipment and nodes)
  - `Consequences` (severity across People, Environment, Economic, Social; initial likelihood; risk rating)
  - `Safeguards` (SIS interlocks, SIL ratings, IPL credit levels, BPCS alarms)
  - `ActionItems` (recommendations, risk rank, disciplines, owner types)
- Run script and verify in live Spanner database (`safety-db`).
- Synchronize `database/seeds/spanner_hazop.json` and update `MockSpannerDatabase` for offline test parity.

### Step 2: Dynamic Plant Hierarchy in `server/main.py`
- In `get_catalog_hierarchy()`:
  - Query `db.units` to construct dynamic sections (`UnitId`, `Name`, `Description`).
  - Query `db.hazop_nodes` to nest nodes under their respective units.
  - Query `db.node_equipment_map` to place equipment under their respective nodes.
  - Query `db.equipment` and `db.instruments` for equipment specs and nested instruments.
  - Remove static `sections = [...]’ dictionary.
- Add `GET /api/v1/catalog/lineage` endpoint returning:
  - Certified drawing reference and As-Built revision status from Dataplex / Spanner.
  - Safe narrative wiki snippet from `read_gcs_wiki_document`.
  - Equipment operating conditions and active SIS interlock count.

### Step 3: Eliminate Hardcoded Data in Frontend (`server/static/index.html`)
- Delete hardcoded `docMap` dictionary (lines 881–918).
- Replace `updateLineageDocsForTag(tag)` with asynchronous API call to `/api/v1/catalog/lineage?tag=${encodeURIComponent(tag)}`.
- Delete hardcoded `knownTags` array (lines 846–854); derive known tags dynamically from `window.catalogHierarchyData`.
- Remove hardcoded `"E-2303"` initial selections; initialize with first equipment node returned by catalog API.

### Step 4: Refactor HAZOP Facilitator (`app/hazop/agent.py` & `app/hazop/markup_parser.py`)
- In `app/hazop/agent.py`:
  - Refactor `discover_node_risks(node_id)` to query `db.deviations`, `db.causes`, `db.consequences`, and `db.safeguards` from Cloud Spanner. Delete hardcoded risk lists.
  - Refactor `parse_markup_and_hydrate()` to read stream parameters and operating conditions from `db.equipment` and `db.streams`.
  - Refactor `propose_safeguards_hitl()` to query `db.graph_find_interlocks()` and `db.safeguards`.
- In `app/hazop/markup_parser.py`:
  - Delete `KNOWN_NODE_METADATA`. Query node metadata from `db.hazop_nodes` and `db.node_equipment_map`.

### Step 5: Refactor ADK Agent Tools (`app/agent.py`)
- In `evaluate_hazop_deviation`:
  - Query Spanner `Deviations`, `Causes`, `Safeguards` for the target node and deviation parameter.
  - Calculate unmitigated and mitigated risks using official `HazopStudyAgent` and live database safeguards with zero hardcoded placeholder numbers.

### Step 6: Unit & Property-Based Testing
- Author tests in `tests/test_frontend_proxy.py` and `tests/test_adk_agents.py`:
  - Unit tests: verify `/api/v1/catalog/hierarchy` generates sections and nodes dynamically from `db.units` and `db.hazop_nodes`.
  - Unit tests: verify `/api/v1/catalog/lineage` returns live provenance and wiki content for any equipment tag.
  - Property tests: assert universal validity of deviations, causes, and safeguards fetched from database across all 6 nodes.
  - Invariant tests: assert zero static fallback dictionaries in code.

### Step 7: Build, Deploy & Live Verification
- Build container via Google Cloud Build.
- Deploy to Cloud Run production (`phenol-process-safety-prod`).
- Probe live endpoints across multiple equipment tags to verify 100% database-driven responses.
