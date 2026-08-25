---
name: CDN Pre-commissioning and Commissioning Procedure
type: Startup
unit: CDN
tags: [procedure, startup, precommissioning, commissioning, CDN, concentration, decomposition, neutralization]
sources: [OM-Phenol Unit UOP-2015.pdf]
last_updated: 2026-06-16
---

# CDN Pre-commissioning and Commissioning Procedure

**Authority:** UOP General Operating Manual, Rev 8, Section V — Pre-commissioning.

> Section V is written generically for the whole UOP Phenol unit (oxidizers, reactors, columns, compressors). This page extracts the items applicable to CDN equipment: vessels (V-2301/V-2302/D-2301–D-2312), pumps (P-2301–P-2320), the concentration vacuum package (X-2301), and CDN instrumentation. Generic guidance not relevant to CDN (fired heaters, reciprocating compressors, MSHP catalyst reduction) is omitted — see source for full text.

---

## Scope

Pre-commissioning and commissioning activities required before [[procedures/startup-cdn]] can begin. Three purposes per UOP GOM: (1) verify by inspection/testing that the unit is safe, operable, and built as specified; (2) prepare equipment for operation (flushing, pump/vacuum run-in); (3) familiarize operators with the unit. Order of activities may be adapted to construction progress, but all items must be completed before introducing hydrocarbon or CHP.

---

## Prerequisites / Pre-checks

- [ ] Construction mechanically complete for the CDN equipment group being commissioned
- [ ] Vendor data sheets and nameplates available for cross-check against design (see [[equipment]] pages for design data)
- [ ] Vessel entry safety procedures in place (toxic vapor / O₂ sampling, harness, attendant) — **never enter an unattended vessel**

---

## Steps

### 1. Equipment Inspection

**Vessels** (V-2301, V-2302, D-2301 through D-2312, X-2320, X-2321): compare actual installation to Project Specification drawings —
- Temperature/pressure/vacuum rating
- Wall thickness and metallurgy (note: D-2304 Decomposer Drum uses Alloy 20 acid injection distributor — verify against [[equipment/D-2304]])
- Elevation and support (D-2304 requires 3000mm clearance above platform equipment within 15m radius)
- Trays/packing (V-2301 Sulzer Mellapak 250X — verify level, orientation, support)
- Nozzles, distributors, vortex breakers, demisters
- Thermowells and level instrument nozzles
- Insulation and fireproofing
- Cleanliness — no construction debris

**Heat exchangers** (E-2301, E-2302A/B, E-2303, E-2304, E-2306, E-2307A/B, E-2308A/B, E-2309, E-2310): metallurgy, tube/tubesheet/baffle condition, manufacturer P/T/ΔP ratings, nozzle and flange condition.

**Pumps** (all CDN pumps P-2301A/B through P-2320): metallurgy, suction/discharge block valves, suction strainers, discharge pressure gauges, check valves, lubrication and seal flush systems, piping expansion provisions, steam tracing/insulation where required. Cross-check vendor rating (head, capacity, temperature, pressure) against [[equipment]] design data pages.

**Piping and Instrumentation:** verify against P&ID — line sizes/metallurgy, flanges/gaskets, bolting, drains/vents, relief valve settings, piping supports, utility tie-ins, general safety requirements.

### 2. Strength and Leak Testing (Hydrostatic Test)

- Test pressure: **1.5× design pressure for piping, 1.3× design pressure for equipment**.
- Fill completely with water (treated water if plant water chloride content is high — risk of stress corrosion cracking on austenitic SS, used extensively in OXI/CDN vessels).
- Remove or blind/gag all relief valves and rupture discs (including X-2311 rupture disc on D-2304) before testing — they must not open during test.
- Remove level instruments, orifice plates, and other internals not rated for test pressure.
- Divide the CDN section into test groups by design pressure rating; isolate with blinds per ANSI B31.3.
- Bench test and set all PSVs before final installation (PSV set pressures for V-2301/V-2302 — see [[hazop/study-info]] open item).
- Install temporary fine-mesh screens in pump suction lines before testing to protect impellers from debris.

### 3. Line Flushing

- Flush all CDN piping with water (or steam/air for gas lines) at maximum safe volume and velocity.
- Remove control valves before flushing where practical — do not flush through them (debris can damage valve seats, especially tight-shutoff on/off valves such as the SIS isolation valves UXV-1201A/B/C).
- Flush instrument lines with transmitters removed.
- Flush sequence: main header → lateral headers → branch lines, each from source to end.
- Always flush through equipment bypass to an open end before flushing through the equipment itself.
- Reconnect all temporary breaks, replace control valves, and re-check pump alignment after flushing.

### 4. Run-In of Pumps (all CDN pumps)

- Rotate pump/driver by hand to verify free rotation before starting.
- Run uncoupled motor for a minimum of **4 hours** to verify motor operation.
- Circulate water through new equipment with temporary suction strainers installed.
- Centrifugal pumps: throttle discharge valve during run-in to prevent overload (run-in fluid is denser than process fluid — risk of motor overload) and to prevent cavitation as strainers foul.
- Positive displacement pumps (P-2305A–F acid injection, P-2306A/B diamine injection): **never close the discharge valve while running** — these can overpressure themselves and downstream piping.
- Sealless mag-drive pumps (P-2308A/B, P-2309A/B, API 685): verify flush/cooling circuit cleanliness — loss of flush or dirty flush causes seal/bearing failure (no mechanical seal to fall back on).
- Mechanical-seal pumps: verify all flush system components (strainers, separators, restriction orifices, coolers) installed correctly and clean.
- Check shaft sealing after start: mechanical seals should show no leakage after a few start/stop cycles; packed stuffing boxes must be permitted to leak slightly.
- Shut down sequence: close discharge valve first (protects against backflow through a leaking check valve and gives wearing rings a final flush).
- Remove temporary suction screens only after two successive debris-free inspections.

### 5. Instrument Servicing and Calibration

- Visual inspection of all instruments against specification (range, pressure rating, materials, electrical characteristics).
- Pressure-test instrument piping with instrument air; soap-test joints.
- Calibrate transmitters, control board equipment, local controllers; adjust control valves and positioners.
- Verify control valve fail-action on air failure — **critical for CDN SIS valves** (UXV series) and split-range control (e.g., TIC-1302 on E-2307A/B).
- Loop-check every control loop: simulate signal at transmitter, verify response at controller and at the field control valve.
- Bench test and set all relief valves if not already done during hydrostatic testing.
- Special attention to complex trip systems — UC-2301/UC-2302/UC-2303 SIS architecture (see [[instruments/sis-cdn]] and [[instruments/cause-effect-cdn]]).

### 6. Commissioning of Plant Services (CDN-relevant)

Commission in this order: plant/treated water → electrical/emergency power → plant and instrument air → nitrogen system → steam/condensate (excluding tracing) → tempered/refrigerated water (flush and leak test now; do not commission live until start-up is imminent).

**Drain and effluent systems — leak test before commissioning:**
- CHP drains and pumps (CHD header → [[equipment/D-2206]] CHP Sump, OXI section)
- Acid aromatics drains and sump (AD header → [[equipment/D-2307]] → [[equipment/P-2304A]])
- Sulfuric acid drains and neutralizing pit ([[equipment/X-2320]])

Leak test method: blind/block all drain lines at the collection vessel, fill to the brim of drain funnels, watch for level loss. Verify correct routing by hosing each point individually and confirming appearance at the correct collection vessel — **do not assume drain routing matches the P&ID without this check**, given the strict separation required between CHP drains and acid aromatics drains (H₂SO₄ + CHP reaction hazard, per Drawing 0023 Note).

### 7. Commissioning of the Concentration Vacuum System (X-2301)

> This is the CDN-specific application of GOM Section V.N–P (Commissioning of Additional Plant Services, Ejector Systems, Vacuum Testing).

1. Cannot commission ejectors (J-2301/J-2302A/B) until steam system is operating.
2. Open cooling water fully to inter-condensers and after-condensers before introducing steam.
3. Blow steam through the ejector steam lines near the ejector body to clear construction debris — **critical**: ejector jets are only a few mm in diameter; uncleaned lines cause repeated capacity loss or shutdowns during initial commissioning.
4. Start ejectors stage-by-stage from the last stage backward (last stage first, then preceding stage, etc.).
5. Confirm steam is dry and at nameplate pressure for each ejector.
6. Once vacuum stabilizes, put pressure controllers in service.
7. Commission liquid ring vacuum pumps P-2316A/B and sealant pumps P-2317A/B per vendor procedure (Gardner Denver Nash) — confirm sealant supply before starting P-2316A/B (loss of sealant = vacuum pump damage).
8. **Vacuum (leak) testing** — required for V-2301, V-2302, and all vacuum-service piping before hydrocarbon introduction:
   - Mask all flanges/fittings with tape; pull maximum vacuum; probe for leaks (soap solution or shaving cream drawn into a test hole indicates a leak).
   - After repairing leaks, isolate the test system and hold vacuum for **1 hour minimum** with no appreciable pressure change.
   - Break vacuum with nitrogen; leave at slight positive N₂ pressure.
9. Common ejector/vacuum troubleshooting checks if vacuum is poor or erratic: tighten all flanges/packing glands, check steam pressure vs. nameplate, check steam trap performance (wet steam causes back pressure), check for condenser fouling, check for plugged vents — see [[troubleshooting]] for CDN-specific recurring issues.

### 8. Air-Freeing

- Evacuate CDN equipment to minimum achievable pressure, then break with nitrogen to header pressure; repeat (typically 2 cycles).
- Target: **<0.5 vol% O₂** by sample analysis (0.3 vol% acceptable alternative; lower if process reasons require — relevant given CHP's sensitivity to oxygen-initiated side reactions).
- Leave all CHP-service and CDN equipment under slight positive N₂ pressure on completion.
- After this point, establish a permit system for vessel entry/work — equipment is now in a nitrogen atmosphere and must be treated accordingly for the life of the plant.

---

## Alarms to Watch

Not applicable during pre-commissioning (instrumentation is being calibrated, not yet in protective service). All SIS trip simulations during instrument loop-checking (Step 5) should be logged and verified against [[instruments/cause-effect-cdn]].

---

## Post-completion Verification

- [ ] All CDN vessels, exchangers, and piping hydrostatically tested per ANSI B31.3; results documented
- [ ] All CDN pumps run-in (uncoupled ≥4 hr, then coupled circulation) with no abnormal vibration, noise, or seal leakage
- [ ] All instrument loops checked; SIS trip simulations confirmed against C&E table
- [ ] PSVs bench tested and set (note: V-2301/V-2302 set pressures still TBC per [[hazop/study-info]] — confirm resolved before proceeding)
- [ ] CHP and acid aromatics drain systems leak tested and routing verified
- [ ] Concentration vacuum system (ejectors + P-2316A/B) commissioned and tuned to stable vacuum
- [ ] V-2301, V-2302, and vacuum piping vacuum-leak tested (1-hour hold, no pressure change)
- [ ] CDN equipment air-freed to <0.5 vol% O₂ and left under positive N₂
- [ ] Vessel entry permit system established

---

## References

- [[sources/om-phenol-uop-2015]] — UOP GOM §V (primary source)
- [[procedures/startup-cdn]] — next step after pre-commissioning is complete
- [[equipment/X-2301]] — Concentration Vacuum Producing Equipment
- [[equipment/D-2304]] — Decomposer Drum
- [[equipment/V-2301]] — Preflash Column
- [[equipment/V-2302]] — Flash Column
- [[instruments/sis-cdn]]
- [[instruments/cause-effect-cdn]]
- [[hazop/study-info]] — PSV set pressure open item
- [[hazards/cumene-hydroperoxide]]
