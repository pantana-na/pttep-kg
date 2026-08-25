# Input Drop Zone

Drop any plant document here — PFD, P&ID, Data Sheet, Operating Manual, SOP, or any other process document.

Then tell the assistant:

```
Sort input folder
```

The assistant will:
1. Read each file's name and content
2. Classify it to the correct category
3. Move it to the appropriate `raw/` subfolder
4. Ingest it into the wiki automatically

---

## Supported Document Types

| What you drop | Where it goes |
|---------------|--------------|
| Process Flow Diagram | `raw/pfd/` |
| Piping & Instrumentation Diagram | `raw/pid/` |
| Equipment Data Sheet / Process Data Sheet | `raw/data_sheets/` |
| Operating Manual / SOP / Procedure | `raw/operating_manuals/` |
| Images / Attachments | `raw/assets/` |

If the assistant cannot confidently classify a file, it will ask you before moving it.
