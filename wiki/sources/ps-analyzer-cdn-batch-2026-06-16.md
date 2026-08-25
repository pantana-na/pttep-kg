---
name: Process Data Sheet — CDN Analyzers (2026-06-16)
description: Source summary for the 12-page CDN analyzer process data sheet covering CHP density/concentration transmitters, sulfuric acid analyzers, and the vacuum-vent oxygen analyzer
metadata:
  type: source
tags: [source, instrument, data-sheet, analyzer, CDN]
sources: ["14780-8120-PS-0003_ANALYZER PROCESS DATA SHEET CDN SECTION_Z1.pdf"]
last_updated: 2026-06-16
---

# Source: Process Data Sheet — CDN Analyzers (2026-06-16)

## Purpose

12-page AS-BUILT (Rev Z1) Analyzer process data sheet for the CDN unit, prepared by POSCO Engineering for PTT Phenol Train II under UOP licence. Covers 5 analyzer systems: two density-based CHP concentration transmitters, two colorimetric sulfuric acid analyzers, and one paramagnetic oxygen analyzer.

Full extraction is at [[instruments/analyzers-cdn]] — this page summarizes findings only.

## Equipment Touched

| Tag | Page | Status |
|-----|------|--------|
| P-2307AB | [[equipment/P-2307AB]] | Confirmed — AI-0801A/B reconciled as the dual outputs of AT/AY-23-0801 |
| P-2301AB | [[equipment/P-2301AB]] | Confirmed — AI-0901A/B reconciled as the dual outputs of AT/AY-23-0901 |
| E-2307 | [[equipment/E-2307]] | Confirmed — AT-1701 matches AT/AY-23-1701; composition and start-up acid spike data added |
| X-2310AB | [[equipment/X-2310AB]] | Confirmed — AT-1901 matches AT/AY-23-1901; composition data added |
| X-2301 | [[equipment/X-2301]] | Confirmed — AI-1001 matches AT-23-1001; sample composition added |

## Key Findings

1. **No real tag conflicts** — initial review suggested the wiki's bare "AI-0801A/B" / "AI-0901A/B" tags might mismatch this document's "AT/AY-23-0801" / "AT/AY-23-0901" format, but the data sheets show each is a **single density transmitter with two simultaneous outputs** (density span + converted CHP wt%), exactly matching the wiki's existing A/B pair framing. Reconciled, not corrected.
2. **Inferential measurement caveat**: both CHP density/concentration transmitters carry an explicit source warning that the on-stream reading may differ from true CHP concentration and that routine lab analysis is required for verification — this on-stream signal should not be treated as a standalone safety measurement in HAZOP credit assessment.
3. **Start-up acid spike**: AT/AY-23-1701 (Decomposer circulating liquid) is designed for up to 300 wt ppm H₂SO₄ during start-up vs. 40 ppm normal — a ~7.5× transient, worth checking against corrosion/safeguard assumptions during startup-deviation HAZOP analysis.
4. **Material constraint**: both acid analyzers explicitly prohibit PTFE as the reaction-cup material.
5. New composition data captured for the Decomposer circulating liquid and the crude product to Fractionation — useful for future stream/parameter pages.

## References

- [[instruments/analyzers-cdn]] — full register (primary reference)
- [[hazards/cumene-hydroperoxide]] — CHP safety basis
