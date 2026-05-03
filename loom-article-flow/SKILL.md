---
name: loom-article-flow
description: Run the Loom article writing workflow from sources or a Synthesis Pack to Draft and Final. Use when the user asks to research and write an article, turn materials into a draft, or produce Draft and Final versions from source material.
---

# Loom Article Flow

Run the full research-to-article pipeline.

## Pipeline

1. `loom-intake`
2. `loom-capture`
3. `loom-read`
4. `loom-synthesis-pack`
5. `loom-draft`

If a trusted Synthesis Pack already exists, start at `loom-draft`.

## Read First

- `../shared/references/writing-pipeline.md`
- `../shared/references/companion-skills.md`
- `../shared/references/synthesis-pack-schema.md`

## Outputs

- Material List, Raw Captures, Source Briefs, Synthesis Pack.
- Draft.
- Final when requested.

## Stop Points

- Draft is for user feedback.
- Final stays in `working/` by default.
- Do not move to `published/`, generate Topic Notes, or update indexes unless explicitly requested.

## Rules

- Draft/Final must not overwrite Raw Capture, Daily Note, Source Brief, Synthesis Pack, or Topic Note.
