---
name: loom
description: Route ambiguous or multi-step Loom requests and create Material Lists. Use when the user provides mixed source material and needs help starting, when the request spans research and writing, or when unsure which loom-* skill applies. For clear single-intent requests, the sub-skills (loom-research, loom-write, loom-maintain) handle intake directly.
---

# Loom Router + Intake

Route ambiguous requests and create the Material List before any research begins.

## Read First

- `../shared/references/schemas.md`

## Cold Start

Before routing, check whether the vault is configured.

If `<vault-root>/.loom/config.yaml` does not exist, run a one-time setup interview:

1. **Vault location** — Where should the vault live? Suggest `~/loom-vault`. Create the directory if needed.
2. **Working language** — `zh`, `en`, or `auto` (detect per query).
3. **Interest areas** — What topics is the user currently working on? (e.g. "AI Agent, Software Architecture"). These become the initial Category directories under `02_Topic_Notes/`.
4. **Default research depth** — `quick` (Source Brief only), `standard` (through Synthesis Pack), or `deep` (full pipeline through Topic Note + Index).

Write `.loom/config.yaml` to the vault root:

```yaml
vault_path: <absolute-path>
language: <zh|en|auto>
categories:
  - <Category>
output_depth: <quick|standard|deep>
created: YYYY-MM-DD
```

If config already exists, read it. Use stored preferences as defaults — user can override per query.

To change settings later, the user can say "reconfigure" or edit `.loom/config.yaml` directly.

## Routing

When the user's intent is clear, route directly:

- **Research materials** (URLs, PDFs, text → synthesis pack): use `loom-research`.
- **Write or draft** (from synthesis or notes → article → topic → index): use `loom-write`.
- **Vault maintenance** (validate, migrate, evolve, connect, index rebuild): use `loom-maintain`.

When intent is ambiguous, ask one question: "Research, write, or maintain?"

## Intake

Before routing to `loom-research` or `loom-write`, create a Material List:

1. Classify task type: single-source deep dive, multi-source synthesis, theme research, or draft rewrite.
2. For each source, record: ID (S1, S2…), Title, Author, Date, Type, Source Tier, Relevance, Citation Usability, Risk Level, Raw Path, Capture Status.
3. Every source row must include a `raw_path`. If no local capture exists, use the original URL/path or `pasted-local-text` and mark capture status as pending.
4. Record source tier, relevance, citation usability, and risk level conservatively.
5. Suggest next step: `loom-research` or `loom-write`.

## Rules

- Do not deep-read, synthesize, or draft in this stage.
- Do not let Draft or Final wording overwrite Raw Capture, Daily Note, Source Brief, Synthesis Pack, or Topic Note content.
- Detect user query language. All generated artifacts (Source Brief, Synthesis Pack, Draft, Topic Note) use the user's language. Raw Captures always preserve source language.
