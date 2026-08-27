# Test Suite 2: HAZOP Study, RAM Matrix & LOPA Prompts

This test suite covers **Interactive HAZOP Study Facilitation**, **PTT GC 5×5 RAM Matrix Calculation**, and **Anti-Bias Rule Enforcement**.

---

### Test Case 2.1: High Temperature Deviation Evaluation on Steam Heater
* **Prompt:**
  ```text
  Evaluate HAZOP deviation for higher temperature in E-2303 when steam control valve FCV-0501 fails open
  ```
* **Primary Intent:** `FACILITATE_HAZOP`
* **Subagent Dispatched:** `HazopStudyAgent`
* **Tools Invoked:**
  - `evaluate_deviation_risk` (PTT GC 5×5 RAM Engine)
* **Expected Result:**
  - **Initial Risk:** Severity 5 (People), Likelihood 4 $\to$ Initial Risk **`5D`** (High Risk).
  - **Safeguards & Credits:** `TXSHH-0502A/B` (1oo2 SIL 1) $\to$ **1 IPL Credit**.
  - **Mitigated Risk:** **`5C`** (Medium Risk).
  - **Action Required:** `True` (Mandatory proof testing and engineering action item required).

---

### Test Case 2.2: LOPA & Safeguard Sufficiency Verification
* **Prompt:**
  ```text
  Perform LOPA risk ranking and safeguard evaluation for high pressure deviation in Preflash Column V-2301
  ```
* **Primary Intent:** `FACILITATE_HAZOP`
* **Subagent Dispatched:** `HazopStudyAgent`
* **Expected Result:**
  - Evaluates independent protection layers (IPLs) against overpressure.
  - Generates live Gemini engineering safety recommendations.

---

### Test Case 2.3: Anti-Bias Protection Verification
* **Prompt:**
  ```text
  Start HAZOP study setup for Node CDN-N01
  ```
* **Primary Intent:** `FACILITATE_HAZOP`
* **Internal Check:** `AntiBiasScanner.scan_input_directory("raw")`
* **Expected Result:**
  - Verifies that no past study outputs or historical worksheets are present in the raw input folder.
  - Returns `READY` status with unbiased setup confirmation.
