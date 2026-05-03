---
name: loom-connect
description: Maintain Loom cross-topic connections in CONNECTION_INDEX.md. Use when the user asks to find cross-topic connections, compile structured topic-pair insights, or update connection entries of type 迁移, 混搭, or 反转.
---

# Loom Connect

Compile structured connections between Topic Notes.

## Read First

- `../shared/references/schema.md`
- `../shared/references/companion-skills.md`

## Inputs

- `00_Index/TOPIC_INDEX.md`
- Existing Topic Notes with summary frontmatter.
- Existing `00_Index/CONNECTION_INDEX.md` if present.

## Output

- New or updated `CONNECTION_INDEX.md` entries.

## Companion Skills

- Use `ljg-roundtable` for multi-perspective contrast.
- Use `ljg-rank` for cross-domain generators.

## Rules

- Produce only structured topic-pair insights, not generic inspiration prose.
- Valid types: `迁移`, `混搭`, `反转`.
- Every connection must be concrete and actionable.
- Do not duplicate existing topic pairs in either direction.
