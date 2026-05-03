---
name: loom-evolve
description: Generate Loom monthly, quarterly, or annual knowledge evolution summaries. Use when the user asks for 知识演进, monthly summary, quarterly summary, annual review, or evolution reports based on TIMELINE_INDEX, TOPIC_INDEX, CONNECTION_INDEX, and selected Topic Notes.
---

# Loom Evolve

Generate evolution summaries from existing indexes.

## Read First

- `../shared/references/evolution-template.md`
- `../shared/references/schema.md`

## Inputs

- `00_Index/TIMELINE_INDEX.md`
- `00_Index/TOPIC_INDEX.md`
- `00_Index/CONNECTION_INDEX.md`
- Full Topic Notes only when needed.

## Output

- `03_Content_Output/Longform/Evolution_YYYY-MM.md`
- `03_Content_Output/Longform/Evolution_YYYY-QN.md`
- `03_Content_Output/Longform/Evolution_YYYY.md`

## Rules

- Do not rerun connection discovery in this stage.
- Use existing `CONNECTION_INDEX.md` entries for cross-domain sections.
- For quarterly or annual summaries, prefer existing lower-period summaries when available.
