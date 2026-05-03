---
name: loom-intake
description: Classify a Loom research or writing request and create a Material List. Use when the user provides URLs, files, pasted text, topic keywords, or mixed source material and needs the task typed, sources inventoried, and a traceable material ledger before capture, reading, synthesis, or drafting.
---

# Loom Intake

Create the Material List for a Loom research pipeline.

## Read First

- `../shared/references/writing-pipeline.md`
- `../shared/references/companion-skills.md`
- `../shared/references/material-list-schema.md`

## Inputs

- URL, X/Twitter link, YouTube link, paper link, local file path, pasted text, topic keyword, folder, or mixed source bundle.

## Output

- A Material List using `../shared/references/material-list-schema.md`.
- Task type: single-source deep dive, multi-source synthesis, theme research, or draft rewrite.
- Recommended next stage: `loom-capture`, `loom-read`, `loom-synthesis-pack`, or `loom-draft`.

## Rules

- Every source row must include a `raw_path` value. If no local capture exists yet, use the original URL/path or `pasted-local-text` and mark capture status as pending.
- Record source tier, relevance, citation usability, and risk level conservatively.
- Do not deep-read, synthesize, or draft in this stage.
