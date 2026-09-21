---
name: Process Data Sheet — CDN Flow Instruments (2026-06-16)
description: Source summary for the 50-page CDN flow instrument process data sheet covering DP transmitters, orifice plates, Coriolis meters, thermal mass flow switches, restriction orifices, and a rotameter
metadata:
  type: source
tags: [source, instrument, data-sheet, flow, CDN]
sources: ["14780-8120-PS-0031_FLOW INSTRUMENT (CDN)_Z1.pdf"]
last_updated: 2026-06-16
---

# Source: Process Data Sheet — CDN Flow Instruments (2026-06-16)

## Purpose

50-page AS-BUILT (Rev Z1) Flow Instrument process data sheet for the CDN unit, prepared by POSCO Engineering for Refinery Phenol Train II under UOP licence. Covers 53 instrument data sheets across 6 device families: DP transmitters, primary flow elements (orifice plates), Coriolis mass flow meters, thermal mass flow instruments/switches, restriction orifices, and one rotameter.

Full extraction is at [[instruments/flow-instruments-cdn]] — this page summarizes findings only.

## Coverage

Instrumentation clusters around: Preflash Column (V-2301) and Flash Column (V-2302) overhead/bottoms/reflux services; the Decomposer feed/circulation/calorimeter loop (including duplicate FT/FXT pairs feeding the two calorimeters); steam services to the Preflash/Flash vaporizers and Dehydrators; and the Acid Aromatics/Direct Neutralizer static-mixer injection points (sulfuric acid and diamine metering).

## Key Findings

1. **Two internal tag-naming inconsistencies** found in the source document itself (not wiki errors): (a) the document index lists "FSL-23-1207" for the Process Water to Decomposer Feed switch while the data-sheet body shows "FSL-23-1202" for the identical service; (b) FXT-23-1501/1601/1602 (sulfuric acid injection Coriolis meters) were renamed from FT- per a P&ID clarification meeting, but the data-sheet body text was not updated to match the renamed index entries.
2. Nearly all DP-transmitter and orifice-type instruments are 316SS wetted, consistent with CHP/cumene/phenol service.
3. FE-23-1701 (Reliable CW to Decomposer Cooler) is an insertion-type Annubar, not an orifice plate — the only insertion-type primary element among the orifice plates.
4. Restriction orifices RO-23-0501/0701/0801/0901 were revised per a hydraulic study (Rev F2); RO-23-2001 flow was revised from 6.72 to 3.3 m³/h per vendor information (Rev F1).

## Equipment Touched

No equipment pages required correction from this batch — all flow instrument data is consistent with existing wiki entries. New consolidated reference page created: [[instruments/flow-instruments-cdn]].

## References

- [[instruments/flow-instruments-cdn]] — full register (primary reference)
- [[instruments/cause-effect-cdn]] — SIS-side flow tags (FXSLL series)
