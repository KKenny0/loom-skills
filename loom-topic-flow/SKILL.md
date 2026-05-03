---
name: loom-topic-flow
description: Run the Loom topic handoff workflow from trusted research or articles to Topic Note and index update. Use when the user asks to turn reviewed notes, a Synthesis Pack, Final article, or published article into a Topic Note and update indexes.
---

# Loom Topic Flow

Run topic handoff.

## Pipeline

1. `loom-topic`
2. `loom-index`

## Read First

- `../shared/references/schema.md`
- `../shared/references/writing-pipeline.md`

## Inputs

- Synthesis Pack.
- Reviewed Daily Notes.
- Final or Published Article.

## Outputs

- Synthesis Topic Note.
- Updated or dry-run indexes, depending on user request and whether `00_Index` exists.

## Rules

- Do not use unreviewed Draft by default.
- Topic Note must shed article rhetoric and return to knowledge structure.
- Ask before writing index files if the user did not explicitly request writes.
