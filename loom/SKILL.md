---
name: loom
description: Route ambiguous Loom research, writing, vault maintenance, migration, and evolution requests to the appropriate Loom stage or flow skill. Use when the user asks broadly to run a Loom workflow, maintain a Loom vault, or is unsure which loom-* skill applies.
---

# Loom Router

Use this fallback skill only for broad or ambiguous requests. Prefer a specific stage or flow skill whenever the user's intent is clear.

## Routing

- Source intake or material ledger: use `loom-intake`.
- Save raw source material or create an inbox source entry: use `loom-capture`.
- Deep-read one source: use `loom-read`.
- Combine multiple sources into a research synthesis: use `loom-synthesis-pack`.
- Write Draft or Final from a Synthesis Pack: use `loom-draft`.
- Convert trusted research outputs into Topic Notes: use `loom-topic`.
- Rebuild or repair indexes: use `loom-index`.
- Maintain cross-topic connections: use `loom-connect`.
- Generate evolution summaries: use `loom-evolve`.
- Scan or migrate a legacy vault: use `loom-migrate`.
- Validate a vault: use `loom-validate`.
- Run end-to-end research: use `loom-research-flow`.
- Run end-to-end article writing: use `loom-article-flow`.
- Run topic/index handoff: use `loom-topic-flow`.
- Run maintenance: use `loom-maintenance-flow`.
- Run index/connect/evolution summary: use `loom-evolution-flow`.

## Shared Resources

Read shared references only after choosing a stage:

- `../shared/references/writing-pipeline.md`
- `../shared/references/companion-skills.md`
- `../shared/references/schema.md`
- `../shared/references/vault-migration.md`
- `../shared/references/evolution-template.md`

Deterministic scripts live in `../shared/scripts/`.

## Rules

- Treat `/Users/kennywu/Documents/knowledge-vaults/loom-vault` as read-only unless the user explicitly requests writes.
- `baoyu-skills` and `ljg-skills` are required companion skill packs. If missing, tell the user the install commands from `../shared/references/companion-skills.md`.
- Do not let Draft or Final wording overwrite Raw Capture, Daily Note, Source Brief, Synthesis Pack, or Topic Note content.
