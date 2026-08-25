---
name: CDN Pump Motor Control Types and Tag Table
unit: CDN
tags: [instruments, pumps, motor-control, CDN, DCS]
sources: [14780-8120-25-23-0001F_Z1.pdf, 14780-8120-25-23-0001G_Z1.pdf, 14780-8120-25-23-0001H_Z1.pdf]
last_updated: 2026-06-06
---

# CDN Pump Motor Control Types and Tag Table

**Source:** Drawings 0001F (schematics), 0001G (tag table), 0001H (vibration monitoring) — Rev Z1 As-Built

---

## Motor Control Types

Twelve control types (A through L) are defined for CDN pumps. Key differences:

| Type | READY | Motor Power (XP) | Temp Switch (TS) | Typical Service | SIS Connected |
|------|-------|-----------------|-----------------|-----------------|---------------|
| A | No | No | No | Basic HV pump | No |
| B | No | No | No | Standard centrifugal (most acid pumps) | No |
| C | Yes (XR) | No | No | Auto-start capable | No |
| D | Yes (XR) | No | No | Auto-start + DCS permissive | Some |
| E | Yes (XR) | No | No | Auto-start | No |
| F | Yes (XR) | No | No | Auto-start, SIS connected | Yes (UC-2303) |
| G | No | No | Yes (TS) | Magnetic pump with temp monitor | No |
| H | No | No | Yes (TS) | Magnetic pump + auto-start | No |
| I | No | Yes (XP) | No | With motor power monitoring | No |
| J | Yes (XR) | Yes (XP) | No | Auto-start + power monitoring | No |
| K | Yes (XR) | Yes (XP) | Yes (TS) | Full monitoring | No |
| L | Yes (XR) | Yes (XP) | Yes (TS) | Full monitoring + SIS | Yes (UC-2301) |

**Notes from drawing:**
- High and Low motor power alarms and shutdowns are provided for **magnetic sealless pumps only**
- Shutdown circuitry stops the operating pump for any abnormal condition listed in the shutdown variables
- XY (permissive) can be FY, LY, PY, or UY (any function variable)
- Low-Low motor power alarm and shutdown specifically apply to P-2102A/B and P-2203A/B (OXI section — referenced for cross-unit awareness)
- READY signal is applied only to auto-start pumps
- Permissive signal for LV motor: combined with DCS STOP; process control logic also connected
- Permissive signal for HV motor: hardwired to MCC; process control logic also connected
- Temperature switch (TS) is provided by the magnetic pump vendor; High signal trips the pump

---

## Complete Motor Control Tag Table — CDN Unit 2300

**Drawing:** 0001G (Motor Control Details)

| Pump Tag | P&ID No. | Type | DCS Signal | XI (Running) | XA (Fault) | XR (Ready) | XL (Permissive) | II (Current) | XP (Power) | HS Start | HS Stop | HS(HOA) | TS |
|----------|---------|------|-----------|------|------|------|------|------|------|------|------|------|---|
| P-2301A | 0009 | B | — | 23-0901A | 23-0901A | — | — | 23-0901A | — | 23-0901AST | 23-0901ASP | 23-0901AHA | — |
| P-2301B | 0009 | B | — | 23-0901B | 23-0901B | — | — | 23-0901B | — | 23-0901BST | 23-0901BSP | 23-0901BHA | — |
| P-2302A | 0017 | D | FY-23-1702 | 23-1701A | 23-1701A | 23-1701A | 23-1701A | 23-1701A | — | 23-1701AST | 23-1701ASP | 23-1701AHA | — |
| P-2302B | 0017 | D | FY-23-1702 | 23-1701B | 23-1701B | 23-1701B | 23-1701B | 23-1701B | — | 23-1701BST | 23-1701BSP | 23-1701BHA | — |
| P-2303A | 0013 | B | — | 23-1301A | 23-1301A | — | — | 23-1301A | — | 23-1301AST | 23-1301ASP | 23-1301AHA | — |
| P-2303B | 0013 | B | — | 23-1301B | 23-1301B | — | — | 23-1301B | — | 23-1301BST | 23-1301BSP | 23-1301BHA | — |
| P-2304A | 0020A | D | LY-23-2001 | 23-2001A | 23-2001A | — | — | 23-2001A | — | 23-2001AST | 23-2001ASP | 23-2001AHA | — |
| P-2305A | 0015 | B | — | 23-1501A | 23-1501A | — | — | 23-1501A | — | 23-1501AST | 23-1501ASP | 23-1501AHA | — |
| P-2305B | 0015 | B | — | 23-1501B | 23-1501B | — | — | 23-1501B | — | 23-1501BST | 23-1501BSP | 23-1501BHA | — |
| P-2305C | 0016 | B | — | 23-1601A | 23-1601A | — | — | 23-1601A | — | 23-1601AST | 23-1601ASP | 23-1601AHA | — |
| P-2305D | 0016 | B | — | 23-1601B | 23-1601B | — | — | 23-1601B | — | 23-1601BST | 23-1601BSP | 23-1601BHA | — |
| P-2305E | 0016 | B | — | 23-1602A | 23-1602A | — | — | 23-1602A | — | 23-1602AST | 23-1602ASP | 23-1602AHA | — |
| P-2305F | 0016 | B | — | 23-1602B | 23-1602B | — | — | 23-1602B | — | 23-1602BST | 23-1602BSP | 23-1602BHA | — |
| P-2306A | 0019 | B | — | 23-1901A | 23-1901A | — | — | 23-1901A | — | 23-1901AST | 23-1901ASP | 23-1901AHA | — |
| P-2306B | 0019 | B | — | 23-1901B | 23-1901B | — | — | 23-1901B | — | 23-1901BST | 23-1901BSP | 23-1901BHA | — |
| P-2307A | 0008B | D | FY-23-0802 | 23-0801A | 23-0801A | 23-0801A | 23-0801A | 23-0801A | — | 23-0801AST | 23-0801ASP | 23-0801AHA | — |
| P-2307B | 0008B | D | FY-23-0802 | 23-0801B | 23-0801B | 23-0801B | 23-0801B | 23-0801B | — | 23-0801BST | 23-0801BSP | 23-0801BHA | — |
| P-2308A | 0005A | L | FY-23-0502 | 23-0501A | 23-0501A | 23-0501A | 23-0501A | 23-0501A | 23-0501A | 23-0501AST | 23-0501ASP | 23-0501AHA | TSH-23-0508 |
| P-2308B | 0005A | L | FY-23-0502 | 23-0501B | 23-0501B | 23-0501B | 23-0501B | 23-0501B | 23-0501B | 23-0501BST | 23-0501BSP | 23-0501BHA | TSH-23-0509 |
| P-2309A | 0007A | L | FY-23-0703 | 23-0701A | 23-0701A | 23-0701A | 23-0701A | 23-0701A | 23-0701A | 23-0701AST | 23-0701ASP | 23-0701AHA | TSH-23-0704 |
| P-2309B | 0007A | L | FY-23-0703 | 23-0701B | 23-0701B | 23-0701B | 23-0701B | 23-0701B | 23-0701B | 23-0701BST | 23-0701BSP | 23-0701BHA | TSH-23-0705 |
| P-2320A | 0020A | D | LS-23-2005 | 23-2001 | 23-2001 | — | — | 23-2001 | — | 23-2001ST | 23-2001SP | 23-2001HA | — |
| P-2316A | 0010A | F | UC-2303 | 23-1001A | 23-1001A | — | — | 23-1001A | — | 23-1001AST | 23-1001ASP | 23-1001AHA | — |
| P-2316B | 0010A | F | UC-2303 | 23-1001B | 23-1001B | — | — | 23-1001B | — | 23-1001BST | 23-1001BSP | 23-1001BHA | — |
| P-2317A | 0010A | F | UC-2303 | 23-1002A | 23-1002A | — | — | 23-1002A | — | 23-1002AST | 23-1002ASP | 23-1002AHA | — |
| P-2317B | 0010A | F | UC-2303 | 23-1002B | 23-1002B | — | — | 23-1002B | — | 23-1002BST | 23-1002BSP | 23-1002BHA | — |

---

## Vibration and Temperature Monitoring (Drawing 0001H)

Only two pumps in CDN have **vibration monitoring** — this confirms their exceptional criticality:

### P-2302A — Decomposer Circulation Pump A (HV Motor, Type 2 monitoring)

| Point | Tag | Description |
|-------|-----|-------------|
| Pump VE (NDE) | VE-23-1740A | Pump vibration element — non-drive end |
| Pump VE (DE) | VE-23-1741A | Pump vibration element — drive end |
| Motor VE (NDE) | VI-23-1740A | Motor vibration indicator — NDE |
| Motor VE (DE) | VI-23-1741A | Motor vibration indicator — DE |
| Motor VE (NDE) | VI-23-1742A | Motor vibration indicator — additional NDE |
| Motor bearing TE (DE) | TE-23-1740A | Bearing temp element (drive end) |
| Motor bearing TT (DE) | TT-23-1740A | Bearing temp transmitter |
| Motor bearing TI (DE) | TI-23-1740A | Bearing temp indicator |
| Motor bearing TE (NDE) | TE-23-1743A | Bearing temp element (non-drive end) |
| Motor bearing TT (NDE) | TT-23-1743A | Bearing temp transmitter |
| Motor winding TE | TE-23-1744A | Stator winding temp |
| (Additional bearing points) | TE/TT/TI-23-1741A through 1749A | Full bearing temp monitoring suite |

### P-2302B — Decomposer Circulation Pump B (HV Motor, Type 2 monitoring)

Same monitoring structure as P-2302A, with tags in the 23-1740B through 23-1749B range:
- Pump vibration: VE-23-1740B, VE-23-1741B
- Motor vibration: VI-23-1740B, VI-23-1741B, VI-23-1742B
- All bearing temperatures: TE/TT/TI-23-1740B through 1749B

**Monitoring system:** Signals route to both MCC (Motor Control Center) and MMS (Machine Monitoring System).

**Process Engineering Note:** The presence of HV motors, full vibration, and bearing temperature monitoring confirms that P-2302A/B are the most mechanically and operationally critical pumps in CDN. These pumps maintain the 30.8:1 decomposer recirculation. MMS alarms should be configured with conservative setpoints given the consequence of pump failure on the running decomposer.

---

## DCS Auto-Start Logic

Pumps with READY signal (Type C/D/E/F/J/K/L) support standby auto-start. When the running pump trips:
1. Running pump XI signal drops
2. DCS logic checks: Is spare pump in AUTO (HOA in AUTO)?
3. If yes → auto-start signal sent to spare pump
4. FY (flow variable) or LY/PY provides permissive confirmation

Key auto-start pairs and their DCS permissive:
| Operating Pair | DCS Permissive | Auto-Start Logic |
|---------------|---------------|-----------------|
| P-2302A/B | FY-23-1702 | Decomposer Circulation — auto-start immediately |
| P-2307A/B | FY-23-0802 | Overhead pump — auto-start |
| P-2308A/B | FY-23-0502 | Condensate pump — auto-start (SIS also watches) |
| P-2309A/B | FY-23-0703 | Vaporizer condensate — auto-start (SIS also watches) |

**Acid injection pumps P-2305A–F do NOT have auto-start** (Type B). Manual restart is required after any P-2305 trip. This is operationally significant — acid flow can be interrupted if a pump trips and operator is slow to respond, triggering PXALL-23-1601 and potentially a decomposer ESD.

---

## References

- [[sources/pid-cdn]]
- [[equipment/P-2302]] — Decomposer Circulation Pumps
- [[instruments/sis-cdn]] — SIS connections
- [[instruments/pump-seal-plans]] — Seal plans per pump
- [[units/cdn]]
