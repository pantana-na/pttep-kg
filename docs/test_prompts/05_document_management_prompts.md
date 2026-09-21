# Test Suite 5: Document Management, Classification & Ingestion Prompts

This test suite covers **Multimodal PSI Classification (OEMS-005)**, **PDF Ingestion & Graph Synchronization**, and **Cascading Deletion**.

---

### Test Case 5.1: Process Flow Diagram (PFD) Ingestion
* **Prompt / File:**
  ```text
  14780-8120-25-01-0001_PFD_CONCENTRATION.pdf
  ```
* **Subagent Dispatched:** `ExtractorAgent` + `DatabaseAgent`
* **Expected Result:**
  - **PSI Classification:** `pfd` (Confidence: 0.98, Target Unit: `CDN`).
  - **Graph Sync:** Ingests mass & energy balances and links unit `CDN` in Spanner Graph.

---

### Test Case 5.2: Equipment Process Data Sheet Classification
* **Prompt / File:**
  ```text
  14780-8120-PS-E2303_E-2303 PROCESS DATA SHEET_Z1.pdf
  ```
* **Subagent Dispatched:** `ExtractorAgent`
* **Expected Result:**
  - **PSI Classification:** `data_sheets` (Confidence: 0.96).
  - **Wiki Markdown:** Extracted to `equipment/E-2303.md` with full frontmatter metadata.

---

### Test Case 5.3: Cascading Document Deletion
* **Target Drawing / Document:**
  ```text
  14780-8120-PS-0018
  ```
* **Subagent Dispatched:** `DatabaseAgent`
* **Tool Invoked:** `cascade_delete_document`
* **Expected Result:**
  - **Tombstone Records:** Marks graph nodes with `_tombstoned = true`.
  - **Sever Edges:** Removes flow and interlock connections associated with the superseded drawing.
  - **Audit Log:** Writes entry to `wiki/log.md` with TrueTime timestamp.
