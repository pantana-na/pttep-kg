# Test Suite 1: Process Safety & Tri-Tier Retrieval Prompts

This test suite covers **Cloud Spanner Graph (ISO GQL)**, **Dataplex Knowledge Catalog**, and **GCS LLM-Wiki** tool invocations.

---

### Test Case 1.1: SIS Trip Protections & Interlock Voting
* **Prompt:**
  ```text
  What trip protections prevent cumene hydroperoxide thermal runaway in E-2303?
  ```
* **Primary Intent:** `SEARCH_PROCESS_SAFETY`
* **Tools Invoked:**
  - `spanner_graph_query` (Cloud Spanner Graph)
  - `query_knowledge_catalog_provenance` (Dataplex Knowledge Catalog)
  - `read_gcs_wiki_document` (GCS LLM-Wiki)
* **Expected Result:**
  - **Spanner Interlocks:** `TXSHH-0502A/B` (1oo2 SIL 1) actuating `UXV-0501` and `UXV-0502` steam isolation valves in series.
  - **Chemical Limit:** Cumene hydroperoxide decomposition onset temperature (80.0°C).
  - **Drawing Reference:** As-Built P&ID `14780-8120-25-23-0005` Rev Z1.

---

### Test Case 1.2: Upstream Flow & Piping Feed Tracing
* **Prompt:**
  ```text
  Show all equipment feeding into Preflash Column V-2301
  ```
* **Primary Intent:** `SEARCH_PROCESS_SAFETY`
* **Tools Invoked:**
  - `spanner_graph_query` (`mode="upstream"`)
  - `query_knowledge_catalog_provenance`
* **Expected Result:**
  - **GQL Graph Traversal:** Identifies upstream units (`E-2302A/B`, `E-2303`, `X-2302A/B`, `P-2308A/B`, `D-2308`).
  - **TrueTime Token:** Emits `0x4e29b109_spanner_truetime` with query latency < 25ms.

---

### Test Case 1.3: Dataplex Knowledge Catalog Provenance & As-Built Status
* **Prompt:**
  ```text
  Show source drawings, provenance lineage, and Knowledge Catalog metadata for E-2303
  ```
* **Primary Intent:** `SEARCH_PROCESS_SAFETY`
* **Tools Invoked:**
  - `query_knowledge_catalog_provenance`
* **Expected Result:**
  - **Dataplex Entry Group:** `phenol-psi`
  - **PSI Category:** Category 4 (Equipment & Process Data Sheets)
  - **Source Drawings:** `14780-8120-25-23-0005_Z1.pdf` and `14780-8120-PS-E2303_..._Z1.pdf`
  - **Revision Status:** `Z1 (As-Built Certified)`

---

### Test Case 1.4: GCS LLM-Wiki Full Operational Narrative Reading
* **Prompt:**
  ```text
  Read the full operating procedure and control philosophy for E-2303 from GCS wiki
  ```
* **Primary Intent:** `SEARCH_PROCESS_SAFETY`
* **Tools Invoked:**
  - `read_gcs_wiki_document`
* **Expected Result:**
  - **GCS URI Badge:** `gs://phenol-llm-wiki-.../wiki/equipment/E-2303.md` (7.5 KB)
  - **Control Narrative:** Feed-forward control strategy from Oxidation Section (`FIC-0501`) and steam heating duty.

---

### Test Case 1.5: Full Safety Audit & MOC Comprehensive Review (Simultaneous 3-Tool Execution)
* **Prompt:**
  ```text
  Perform a full safety audit on Steam Heater E-2303: trace its interlock trip logic, identify its As-Built P&ID drawing provenance, and retrieve its operating narrative.
  ```
* **Primary Intent:** `SEARCH_PROCESS_SAFETY`
* **Tools Invoked Simultaneously:**
  1. `spanner_graph_query`
  2. `query_knowledge_catalog_provenance`
  3. `read_gcs_wiki_document`
* **Expected Result:**
  - All 3 tool execution cards render in parallel in the Observability Drawer.
  - Live Gemini synthesizes a comprehensive process safety dossier covering interlocks, drawing provenance, and operating limits.
