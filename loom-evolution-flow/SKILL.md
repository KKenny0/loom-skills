---
name: loom-evolution-flow
description: Run Loom evolution reporting by validating indexes, updating topic connections, and generating an evolution summary. Use when the user asks for an evolution report that may need fresh indexes or connection discovery before monthly, quarterly, or annual summary generation.
---

# Loom Evolution Flow

Run the full evolution reporting pipeline.

## Pipeline

1. `loom-validate`
2. `loom-index`
3. `loom-connect`
4. `loom-evolve`

## Read First

- `../shared/references/evolution-template.md`
- `../shared/references/schema.md`

## Outputs

- Validation report.
- Index dry-run or update.
- `CONNECTION_INDEX.md` entries when requested or required.
- Evolution Summary.

## Rules

- If the user asks only for a summary from existing data, use `loom-evolve` directly.
- Ask before writing index or connection updates unless the request explicitly asks for updates.
- Evolution summary consumes connections; it does not invent them inline.
