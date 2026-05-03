---
name: loom-capture
description: Capture source material for Loom by preserving raw/source content and creating an inbox Daily Note entry. Use when the user asks to save a URL, X/Twitter source, YouTube transcript, PDF, markdown file, pasted text, or other raw material into the vault with traceable source metadata.
---

# Loom Capture

Preserve source material before analysis.

## Read First

- `../shared/references/writing-pipeline.md`
- `../shared/references/companion-skills.md`
- `../shared/references/raw-capture-schema.md`
- `../shared/references/schema.md`

## Inputs

- Source URL, X/Twitter URL, YouTube URL, PDF/paper URL, local file, pasted text, or Material List row.

## Outputs

- Raw Capture: original or converted source material, with source identity and retrieval metadata.
- Inbox Daily Note: `01_Daily_Notes/YYYY/inbox/YYYY-MM-DD_slug.md`, acting as the research entry point.

## Companion Skills

- Use `baoyu-url-to-markdown` for ordinary URLs.
- Use `baoyu-youtube-transcript` for YouTube.
- Use `baoyu-danger-x-to-markdown` only when the user explicitly asks to capture X/Twitter.

## Rules

- Distinguish Raw Capture from Daily Note. Raw Capture preserves the source; Daily Note references it.
- Daily Note must preserve source semantics and avoid publication-style rewriting.
- Material List `raw_path` must point to the real raw file, converted Markdown, URL, or explicit local text marker.
- Do not run deep reading, synthesis, drafting, topic generation, or index updates in this stage.
