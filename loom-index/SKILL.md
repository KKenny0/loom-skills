---
name: loom-index
description: Initialize, rebuild, validate, or repair Loom index files. Use when the user asks to create, update, refresh, dry-run, rebuild, validate, or repair TOPIC_INDEX.md, TIMELINE_INDEX.md, CONNECTION_INDEX.md, or the 00_Index directory.
---

# Loom Index

Maintain deterministic vault indexes.

## Read First

- `../shared/references/schema.md`

## Inputs

- Existing Daily Notes, Topic Notes, Connection Index, and vault root.

## Outputs

- `00_Index/TOPIC_INDEX.md`
- `00_Index/TIMELINE_INDEX.md`
- `00_Index/CONNECTION_INDEX.md`

## Scripts

- Dry run: `python3 ../shared/scripts/build_indexes.py <vault-root>`
- Write when explicitly requested: `python3 ../shared/scripts/build_indexes.py <vault-root> --write`

## Rules

- Do not generate new knowledge insights.
- Do not run connection analysis; use `loom-connect`.
- Prefer dry-run before writing.
- Match topics by exact title and preserve existing row order where required by schema.
