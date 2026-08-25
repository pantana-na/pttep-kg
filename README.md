# Phenol Process Expert

A persistent, LLM-maintained knowledge base for phenol plant process specialists.
Built on the LLM Wiki pattern — knowledge compounds with every document you add.

---

## Quick Start

### 1. Open this folder in Claude Code (VSCode Extension or CLI)

```
cd "Phenol Agent"
claude
```

The assistant reads `CLAUDE.md` at the start of every session and knows how to maintain the wiki.

### 2. Drop documents into the input folder

Drop **any** plant document into `input/` — no need to sort manually.

```
input/   ← drop anything here
```

Then tell the assistant:
```
Sort input folder
```

The assistant reads each file, classifies it, and moves it to the correct subfolder automatically:

| Destination | Document types |
|-------------|---------------|
| `raw/pfd/` | Process Flow Diagrams |
| `raw/pid/` | Piping & Instrumentation Diagrams |
| `raw/data_sheets/` | Equipment Data Sheets, Process Data Sheets |
| `raw/operating_manuals/` | Operating Manuals, SOPs, procedures |
| `raw/assets/` | Images, drawings, attachments |

If a file cannot be classified confidently, the assistant will ask you before moving it.

### 3. Ingest documents into the wiki

After sorting, tell the assistant:
```
Ingest them all
```
or for a specific file:
```
Ingest raw/data_sheets/E-201-datasheet.pdf
```

The assistant reads the document, extracts all process data, and integrates it into the wiki — creating and updating pages for equipment, streams, instruments, and procedures.

### 4. Ask questions

```
What is the normal operating temperature range for the cleavage reactor?
What are the critical interlocks for the oxidation section?
Walk me through the phenol column startup procedure.
What happens if CHP concentration in the oxidizer goes above 35 wt%?
```

Every answer cites specific wiki pages and source documents.

### 5. Periodic health check

```
Lint the wiki — find contradictions, gaps, and orphan pages.
```

---

## Directory Structure

```
Phenol Agent/
├── CLAUDE.md                    ← LLM schema (governs all behavior)
├── README.md                    ← This file
├── sort_input.py                ← Auto-classifier script (run by assistant)
├── input/                       ← DROP FILES HERE — assistant sorts them
├── raw/                         ← YOUR source documents (never modified by LLM)
│   ├── pfd/
│   ├── pid/
│   ├── data_sheets/
│   ├── operating_manuals/
│   └── assets/
└── wiki/                        ← LLM-maintained knowledge base
    ├── index.md                 ← Master catalog
    ├── log.md                   ← Activity history
    ├── overview.md              ← Process overview
    ├── units/                   ← Per-section pages (ALKY, OXI, CLP, DIST...)
    ├── equipment/               ← Per-equipment pages (R-201, T-301...)
    ├── streams/                 ← Key process streams
    ├── instruments/             ← Critical control loops and instruments
    ├── procedures/              ← Operating procedures and SOPs
    ├── parameters/              ← Operating windows and design basis
    ├── hazards/                 ← Chemical and process hazards
    └── troubleshooting/         ← Known problems and diagnostics
```

---

## Current Wiki Status

| Category | Status |
|----------|--------|
| Process Overview | Done |
| Unit pages (ALKY, OXI, CLP, DIST) | Skeleton — needs source documents |
| Equipment pages | Pending — add data sheets |
| Stream pages | Pending — add PFD |
| Instrument pages | Pending — add P&ID |
| Procedures | Pending — add operating manual |
| Hazard pages (CHP, Phenol) | Done |
| Troubleshooting | Pending — add operating manual |

---

## Philosophy

- The LLM writes the wiki; you read it
- Every source document added makes all future answers better
- The wiki accumulates knowledge — you never start from scratch
- The assistant never guesses on operating limits — it cites sources or says "data missing"
