# SCHEMA.md — Knowledge Compiler Output Formats & Directory Structure

> This file defines the contract between SKILL.md instructions and output files.
> All templates must be followed verbatim. Do not add, remove, or rename fields.

---

## 1. Vault Directory Structure

Every knowledge vault managed by Knowledge Compiler must follow this layout:

```
<vault-root>/
├── 00_Index/
│   └── TOPIC_INDEX.md           # Master metadata index (auto-updated)
│
├── 01_Daily_Notes/
│   └── YYYY/
│       ├── inbox/               # Freshly compiled Daily Notes
│       ├── working/             # Notes being refined
│       ├── published/           # Finalized Daily Notes
│       └── archived/            # Deprecated Daily Notes
│
├── 02_Topic_Notes/
│   └── [Category]/              # One subdirectory per category
│       └── YYYY-MM-DD_Title.md  # Topic Note files
│
└── 03_Content_Output/
    ├── Longform/                # Long-form articles
    └── Social_Posts/            # Short-form social content
```

### Category Naming Convention

Category directory names use `Pascal_Case` with underscores replacing spaces. Examples:

- `AI_Agent`
- `Claude_Code`
- `Coding_Agent`
- `LLM_Models`
- `OpenClaw`
- `Video_Generation`

### File Naming Convention

- **Daily Notes**: `YYYY-MM-DD_short-kebab-title.md` in `01_Daily_Notes/YYYY/inbox/`
- **Topic Notes**: `YYYY-MM-DD_Title-With-Words.md` in `02_Topic_Notes/[Category]/`

---

## 2. Daily Note Template

Every Daily Note **must** contain exactly these fields and sections. No more, no less.

```markdown
---
title: "[Title]"
date: "YYYY-MM-DD"
status: "inbox"
source_url: "[原始 URL]"
source_type: "[web-clip|text|file]"
tags: [tag1, tag2]
---

## Summary
[3-5 句摘要]

## Key Points
- [关键点 1]
- [关键点 2]

## Details
[详细内容]
```

### Field Specifications

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | ✅ | Descriptive title in the source's original language |
| `date` | date | ✅ | ISO date `YYYY-MM-DD` of compilation |
| `status` | enum | ✅ | One of: `inbox`, `working`, `published`, `archived`. Default: `inbox` |
| `source_url` | string | ✅ | Original URL, or `"local"` if no URL |
| `source_type` | enum | ✅ | One of: `web-clip`, `text`, `file` |
| `tags` | array | ✅ | 2-6 lowercase tags. Use hyphens for multi-word tags (e.g., `multi-agent`) |

### Section Specifications

| Section | Required | Length Guidance |
|---------|----------|-----------------|
| `## Summary` | ✅ | 3-5 sentences capturing the essence |
| `## Key Points` | ✅ | 3-8 bullet points, each a single assertion |
| `## Details` | ✅ | Full content, organized with sub-headers as needed |

---

## 3. Topic Note Template

Every Topic Note **must** contain exactly these fields and sections. No more, no less.

```markdown
---
title: "[Title]"
category: "[Category Name]"
date: "YYYY-MM-DD"
version: "1.0.0"
compiled_from: "[来源 Daily Notes / Topic Notes]"
tags: [tag1, tag2]
related_topics:
  - "[[Topic Name 1]]"
  - "[[Topic Name 2]]"
summary:
  core_idea: "[一句话核心观点]"
  key_mechanism: "[关键机制/方法]"
  applicable_to: "[适用于什么场景]"
  unique_insight: "[独特见解]"
---

## Summary
[自动生成的摘要]

## Key Points
- [关键点 1]
- [关键点 2]

## Detailed Explanation
[LLM 生成的详细解释]

## Related Work
[相关工作或参考]

## Questions
[待探索的问题]
```

### Field Specifications

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | ✅ | Descriptive title |
| `category` | string | ✅ | Must match an existing category directory name (Pascal_Case) |
| `date` | date | ✅ | ISO date of compilation or last update |
| `version` | semver | ✅ | Semantic version, starts at `"1.0.0"`. Increment minor on re-compile |
| `compiled_from` | string | ✅ | List of source Daily Note filenames and/or Topic Note titles |
| `tags` | array | ✅ | 2-8 lowercase tags with hyphens |
| `related_topics` | array | ✅ | Wiki-link references to related Topic Notes. Empty array `[]` if none |
| `summary.core_idea` | string | ✅ | One sentence capturing the essential point |
| `summary.key_mechanism` | string | ✅ | The primary mechanism, method, or technique described |
| `summary.applicable_to` | string | ✅ | Concrete scenarios where this knowledge applies |
| `summary.unique_insight` | string | ✅ | What makes this different from conventional wisdom |

### Section Specifications

| Section | Required | Length Guidance |
|---------|----------|-----------------|
| `## Summary` | ✅ | 3-5 sentences, synthesized from all source material |
| `## Key Points` | ✅ | 5-12 bullet points, each a single distilled assertion |
| `## Detailed Explanation` | ✅ | Comprehensive explanation with sub-headers, examples, and nuance |
| `## Related Work` | ✅ | References, prior art, alternatives. Can be bullet list or prose |
| `## Questions` | ✅ | 2-5 open questions for future exploration. Bullet list |

### Structured Summary Design

The `summary` frontmatter block serves as the **machine-readable digest** of the Topic Note. It is:

- Used by TOPIC_INDEX for quick lookup (avoids reading full Topic Notes)
- Used by future modules (启发分析, CONNECTION_INDEX) for cross-topic analysis
- Designed to fit in ~100 tokens per Topic Note

All 4 fields (`core_idea`, `key_mechanism`, `applicable_to`, `unique_insight`) are mandatory. Do not leave any field as an empty string.

---

## 4. TOPIC_INDEX.md Template

The TOPIC_INDEX is the master lookup table for all Topic Notes. It lives at `00_Index/TOPIC_INDEX.md`.

```markdown
# Topic Index

> Auto-generated. Last updated: YYYY-MM-DD

| Title | Category | Core Idea | Tags | Date |
|-------|----------|-----------|------|------|
| [[Topic 1]] | OpenClaw | ... | tag1, tag2 | 2026-04-10 |
| [[Topic 2]] | Claude_Code | ... | tag3, tag4 | 2026-04-09 |
```

### Update Rules

1. **Idempotent**: If a Topic Note with the same title already exists in the index, **update the existing row** (category, core_idea, tags, date). Do **not** insert a duplicate row.
2. **Match by title**: Use the `title` field (exact string match) to determine if an entry already exists.
3. **Core Idea**: Copy verbatim from the Topic Note's `summary.core_idea` field.
4. **Tags**: Join the Topic Note's `tags` array with `, ` (comma-space).
5. **Date**: Use the Topic Note's `date` field.
6. **Order**: New entries are appended at the end. Updated entries stay in their original position.
7. **Last updated**: Update the `YYYY-MM-DD` in the blockquote to today's date.

### What NOT to include

- Do not include Daily Notes in TOPIC_INDEX — only Topic Notes.
- Do not include full summaries — that's what the `core_idea` column is for.

---

## 5. Behavioral Constraints

These rules govern how the compiler agent generates output.

### 5.1 Language

- Use the source material's original language for the title and content.
- Tags are always lowercase English with hyphens.
- Category names are always Pascal_Case English.

### 5.2 Tags

- Each tag should represent a concept, not a proper noun (use categories for proper nouns).
- Aim for 2-6 tags on Daily Notes, 2-8 tags on Topic Notes.
- Prefer existing tags over inventing new ones. Check recent notes in the vault for tag conventions.

### 5.3 Quality

- Summary must be substantive, not generic ("This article discusses...").
- Key Points must be assertions, not topic labels ("Agent uses progressive disclosure" not "Disclosure section").
- Questions must be genuine open questions, not rhetorical devices.

### 5.4 No Raw Sources Directory

URL sources are recorded in Daily Note frontmatter (`source_url`). Do not create a `01_Raw_Sources/` directory or save raw HTML/text separately.

### 5.5 No Obsidian-Specific Features

Wiki-links (`[[Topic Name]]`) are used in TOPIC_INDEX and Topic Note `related_topics` for human readability in editors that support them. They are **not** Obsidian-specific features — they are simple text markers that any editor can read. Do not use Obsidian-specific features like Dataview queries, callouts, or embedded queries.
