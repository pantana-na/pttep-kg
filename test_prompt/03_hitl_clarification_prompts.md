# Test Suite 3: Human-in-the-Loop (HITL) Clarification Prompts

This test suite covers **Ambiguous / Under-specified Queries** that trigger the **Clarification State Machine** and interactive `<ClarificationCard />` in the UI.

---

### Test Case 3.1: Ambiguous Generic Pump Query
* **Prompt:**
  ```text
  show me interlocks on the pump
  ```
* **Primary Intent:** `AMBIGUOUS_QUERY`
* **State Machine Dispatched:** `ClarificationManager`
* **Event Emitted:** `event: clarification_requested`
* **Expected UI Behavior:**
  - Halts automatic search to prevent hallucination.
  - Renders `<ClarificationCard />` presenting selectable candidate pills:
    1. **`P-2301A/B`**: Flash Column Bottoms Pumps
    2. **`P-2303A/B`**: Decomposer Product Pumps
    3. **`P-2308A/B`**: Steam Heater Condensate Pumps
  - Context trail shows breadcrumb: `Pumps (Step 1 of 3)`.

---

### Test Case 3.2: Ambiguous Heater / Exchanger Query
* **Prompt:**
  ```text
  the heater
  ```
* **Primary Intent:** `AMBIGUOUS_QUERY`
* **Expected UI Behavior:**
  - Displays clarification card prompting the engineer to disambiguate between `E-2302A/B` (Feed-Oxidate Exchanger) and `E-2303` (Steam Heater).
