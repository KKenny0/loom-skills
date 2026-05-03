---
name: loom-topic
description: Create or update Loom Topic Notes from trusted research artifacts. Use when the user asks to compile a topic note, synthesize long-lived knowledge, or convert reviewed notes, a Synthesis Pack, Final article, or published article into a structured reusable Topic Note.
---

# Loom Topic

Convert trusted research into durable knowledge structure.

## Read First

- `../shared/references/writing-pipeline.md`
- `../shared/references/schema.md`
- `../shared/references/companion-skills.md`

## Input Priority

1. Synthesis Pack.
2. `reviewed` Daily Notes.
3. Final or Published Article.

## Output

- Synthesis Topic Note in `02_Topic_Notes/<Category>/`.

## Companion Skills

- Use `ljg-rank`, `ljg-think`, or `ljg-learn` to extract reusable mechanisms and boundaries.

## Rules

- Do not default to unreviewed Draft input. If the user insists, mark source confidence explicitly.
- Topic Note must use calm knowledge-base voice, not article rhetoric or platform tone.
- Focus on structure, mechanisms, applicability, boundaries, related work, and reusable insights.
- Update indexes only if `00_Index` exists or the user asks to update indexes.
