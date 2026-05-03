# Loom Vault Schema

This reference defines the target schema for new Loom outputs and compatibility rules for migrating existing Markdown writing vaults.

## Directory Layout

Target vault layout:

```text
<vault-root>/
├── 00_Index/
│   ├── TOPIC_INDEX.md
│   ├── TIMELINE_INDEX.md
│   └── CONNECTION_INDEX.md
├── 01_Daily_Notes/
│   ├── YYYY/
│   │   ├── inbox/
│   │   ├── working/
│   │   ├── reviewed/
│   │   ├── published/
│   │   └── archived/
│   └── assets/
├── 02_Topic_Notes/
│   └── <Category>/
└── 03_Content_Output/
    ├── Longform/
    └── Social_Posts/
```

Legacy vaults may omit `00_Index`, `03_Content_Output`, or intermediate status directories. Do not create missing directories unless the user asks to initialize indexes, write a new note, or apply migration.

## Status Values

Supported status values:

- `inbox`: newly captured or unprocessed material
- `working`: actively being developed
- `reviewed`: checked but not final
- `done`: legacy value meaning reviewed or complete
- `published`: stable public-facing article
- `archived`: deprecated or inactive material

For new files, prefer `inbox`, `working`, `reviewed`, `published`, or `archived`. Preserve legacy `done` during migration unless the user asks to normalize statuses.

## Daily Note

New Daily Notes should use this frontmatter:

```markdown
---
title: "[Title]"
date: "YYYY-MM-DD"
status: "inbox"
source_url: "[URL or local]"
source_type: "[web-clip|text|file]"
raw_path: "[raw file path, source URL, or pasted-local-text]"
tags: [tag1, tag2]
topic: "[topic-slug]"
---

## Summary
[3-5 sentences]

## Key Points
- [Concrete assertion]

## Details
[Full organized content]
```

Rules:

- Use the source language for title and body.
- Use lowercase English tags with hyphens for new files.
- Use 2-8 tags.
- Filename: `YYYY-MM-DD_short-kebab-title.md`.
- Default destination: `01_Daily_Notes/YYYY/inbox/`.
- If `source_url` is not available, use `"local"`.
- `raw_path` must point to a real raw source, converted Markdown file, original URL, or explicit local text marker.
- Daily Notes preserve source semantics and must not be rewritten with publication-style voice.

Legacy compatibility:

- Some existing notes may use `source` instead of `source_url`; preserve it.
- Some notes may omit frontmatter; infer title/date from filename and H1 during scans.
- Some notes may contain Obsidian callouts or transclusions; preserve them.
- Do not remove unknown fields such as `aliases`, `author`, `assets_dir`, `identifier`, `venue`, `cssclasses`, or `platform`.

## Topic Note

Topic Notes support two modes.

### Link-Only Mode

Use for legacy-style topic entries that point to one or more Daily Notes.

```markdown
---
title: "[Title]"
category: "[Category]"
date: "YYYY-MM-DD"
mode: "link-only"
status: "published"
tags: [tag1, tag2]
linked_notes:
  - "01_Daily_Notes/YYYY/published/example.md"
---

![[01_Daily_Notes/YYYY/published/example.md]]
```

### Synthesis Mode

Use for new long-lived knowledge synthesis.

```markdown
---
title: "[Title]"
category: "[Category]"
date: "YYYY-MM-DD"
version: "1.0.0"
mode: "synthesis"
compiled_from:
  - "01_Daily_Notes/YYYY/inbox/source.md"
tags: [tag1, tag2]
related_topics:
  - "[[Topic Name]]"
summary:
  core_idea: "[One-sentence core idea]"
  key_mechanism: "[Primary mechanism]"
  applicable_to: "[Concrete scenarios]"
  unique_insight: "[Distinctive insight]"
---

## Summary
[3-5 sentences]

## Key Points
- [Distilled assertion]

## Detailed Explanation
[Synthesis with subheadings]

## Related Work
[References, alternatives, prior art]

## Questions
- [Open question]
```

Rules:

- Category directory names use Pascal_Case, for example `AI_Agent`, `Claude_Code`, `Coding_Agent`, `LLM_Models`, `OpenClaw`.
- Filename: `YYYY-MM-DD_Title-With-Words.md`.
- When updating a synthesis note, increment minor version, for example `1.0.0` to `1.1.0`.
- Preserve link-only Topic Notes unless the user requests synthesis.
- Prefer Topic Note inputs in this order: Synthesis Pack, `reviewed` Daily Notes, Final/Published Article.
- Do not create Topic Notes from unreviewed Drafts by default. If forced by the user, record source confidence explicitly.
- Topic Notes use knowledge-base voice and must not inherit article rhetoric or platform-specific wording.

## TOPIC_INDEX.md

Path: `00_Index/TOPIC_INDEX.md`

```markdown
# Topic Index

> Auto-generated. Last updated: YYYY-MM-DD

| Title | Category | Mode | File | Core Idea | Tags | Date |
|-------|----------|------|------|-----------|------|------|
| [[Topic 1]] | Claude_Code | synthesis | 02_Topic_Notes/Claude_Code/2026-01-01_Topic-1.md | ... | tag1, tag2 | 2026-01-01 |
```

Update rules:

- Match existing rows by exact title.
- Update existing rows in place.
- Append new rows at the end.
- `Core Idea` comes from `summary.core_idea` for synthesis notes.
- For link-only notes without a summary, use the first linked note title or a short inferred description.
- Include `File` so later workflows do not guess paths.

## TIMELINE_INDEX.md

Path: `00_Index/TIMELINE_INDEX.md`

```markdown
# Timeline Index

> Auto-generated. Last updated: YYYY-MM-DD

## 2026-04
### New Topics
- [[Topic 1]] (2026-04-10) - Claude_Code

### Updated Topics
- [[Topic 2]] (2026-04-08) - AI_Agent

### Archived
- [[Topic 3]] (2026-04-05) - OpenClaw
```

Rules:

- Keep months newest first.
- Keep all three section headers in each month.
- A topic appears at most once per section per month.
- New entries within a section are newest first.
- Do not include Daily Notes directly.

## CONNECTION_INDEX.md

Path: `00_Index/CONNECTION_INDEX.md`

```markdown
# Connection Index

> Auto-generated. Last updated: YYYY-MM-DD

## [[Topic A]] ↔ [[Topic B]]
- **连接类型**: 迁移
- **启发**: 这意味着你可以用 [X] 来替代/增强 [Y]
- **发现日期**: YYYY-MM-DD
```

Rules:

- Append new connection sections after the blockquote.
- Keep newest connections first.
- Do not duplicate topic pairs in either direction.
- Valid types: `迁移`, `混搭`, `反转`.
- Every insight must be concrete and actionable.

## Migration Compatibility Rules

When migrating an existing vault:

1. Preserve all existing content.
2. Preserve unknown frontmatter fields.
3. Add missing fields only when high-confidence inference is possible.
4. Do not rewrite article bodies just to fit section templates.
5. Do not move assets unless explicitly requested.
6. Prefer additive changes: reports, indexes, topic syntheses, and optional normalized copies.
7. Treat path location as a useful status hint, but do not silently overwrite frontmatter status when it conflicts.
