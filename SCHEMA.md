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

---

## 6. TIMELINE_INDEX.md Template

The TIMELINE_INDEX tracks when topics are created, updated, and archived over time. It lives at `00_Index/TIMELINE_INDEX.md`.

```markdown
# Timeline Index

> Auto-generated. Last updated: YYYY-MM-DD

## 2026-04
### New Topics
- [[Topic 1]] (2026-04-10) - OpenClaw
- [[Topic 2]] (2026-04-09) - Claude_Code

### Updated Topics
- [[Topic 3]] (2026-04-08) - AI_Agent

### Archived
- [[Topic 4]] (2026-04-05) - Video_Generation
```

### Field Specifications

| Element | Required | Description |
|---------|----------|-------------|
| Month header (`## YYYY-MM`) | ✅ | One per month that has activity |
| `### New Topics` | ✅ | Topics first compiled this month |
| `### Updated Topics` | ✅ | Existing topics re-compiled with new sources this month |
| `### Archived` | ✅ | Topics moved to archived status this month |
| Entry format | ✅ | `- [[Title]] (YYYY-MM-DD) - Category` |

### Update Rules

1. **Idempotent**: A topic must appear at most **once per section per month**. If the same topic is compiled multiple times in the same month:
   - First compile → add to `### New Topics`
   - Subsequent compiles in the same month → **do not duplicate** (skip silently)
   - If the topic already existed in a prior month → add to `### Updated Topics` instead of `### New Topics`
2. **New vs Updated**: Check TOPIC_INDEX or TIMELINE_INDEX history. If the topic title exists in a prior month's entries, it is an **Updated** topic. If it is brand new (never appeared before), it is a **New** topic.
3. **Match by title**: Use exact string match on the `title` field.
4. **Category**: Use the Topic Note's `category` field.
5. **Date**: Use the Topic Note's `date` field (compilation date).
6. **Month header**: Create a new `## YYYY-MM` header if one does not already exist for the current month. Months are ordered chronologically (newest first).
7. **Archived**: When a Daily Note's status changes to `archived` and that Daily Note is referenced by a Topic Note's `compiled_from`, add the Topic Note to the `### Archived` section for that month.
8. **Last updated**: Update the `YYYY-MM-DD` in the blockquote to today's date.
9. **Entry order within a section**: Chronological by date, newest first.
10. **Empty sections**: Keep section headers even if empty (they signal the structure is maintained).

### What NOT to include

- Do not include Daily Notes in TIMELINE_INDEX — only Topic Notes.
- Do not include reasons or summaries — use the wiki-link format for quick reference.

---

## 7. Evolution Summary Output Format

The evolution summary is generated on demand (user-triggered) and written to `03_Content_Output/Longform/`. The format is defined in `EVOLUTION_TEMPLATE.md`.

### Summary Types

| Type | Period | Filename Pattern |
|------|--------|------------------|
| Monthly | Single month | `Evolution_YYYY-MM.md` |
| Quarterly | 3 months | `Evolution_YYYY-QN.md` |
| Annual | Full year | `Evolution_YYYY.md` |

### Source Selection Strategy

To keep token usage efficient:
1. Read TIMELINE_INDEX for the target period.
2. Read TOPIC_INDEX for topic metadata.
3. Only read full Topic Notes that are listed as **New Topics** or **Updated Topics** in the target period.
4. Skip reading Topic Notes that are only listed as **Archived** (use TIMELINE_INDEX entry only).
5. For quarterly/annual summaries, read monthly evolution summaries if they exist (instead of re-reading all Topic Notes).

---

## 8. CONNECTION_INDEX.md Template

The CONNECTION_INDEX tracks cross-domain connections discovered by the Inspire Analysis (Workflow 4). It lives at `00_Index/CONNECTION_INDEX.md`.

```markdown
# Connection Index

> Auto-generated. Last updated: YYYY-MM-DD

## [Topic A] ↔ [Topic B]
- **连接类型**: 迁移
- **启发**: 这意味着你可以用 [X] 来替代/增强 [你体系中的 Y]
- **发现日期**: 2026-04-10

## [Topic C] ↔ [Topic D]
- **连接类型**: 混搭
- **启发**: 将 [A] 和 [你已有的 B] 结合，可以产生 [C]
- **发现日期**: 2026-04-10
```

### Field Specifications

| Element | Required | Description |
|---------|----------|-------------|
| Section header (`## [A] ↔ [B]`) | ✅ | Wiki-links for both topics, connected by `↔` |
| `连接类型` | ✅ | One of: `迁移`, `混搭`, `反转` |
| `启发` | ✅ | Specific actionable insight following the sentence pattern for the connection type |
| `发现日期` | ✅ | ISO date `YYYY-MM-DD` when the connection was discovered |

### Connection Type Sentence Patterns

Each connection type has a **mandatory sentence pattern** that must be followed:

| 连接类型 | 问题 | 句式模板 |
|----------|------|----------|
| 迁移 (Transfer) | 某机制能否移植升级你的体系？ | "这意味着你可以用 [X] 来替代/增强 [你体系中的 Y]" |
| 混搭 (Mix) | 某组件和你已有的东西组合能产生什么？ | "将 [A] 和 [你已有的 B] 结合，可以产生 [C]" |
| 反转 (Reverse) | 某做法和你的默认假设相反吗？ | "这提醒你：你可能需要停下 [X]，开始做 [Y]" |

**Key rule**: Every insight must be **specific and actionable** ("能用"，不是"能想"). Vague observations like "这两个主题都很有趣" or "可以考虑它们的关系" are NOT acceptable.

### Update Rules

1. **Append only**: New connections are appended at the end of the file, before the blockquote.
2. **No duplicates**: Before adding, scan existing entries for the same topic pair (in either direction). If `[A] ↔ [B]` or `[B] ↔ [A]` already exists, skip.
3. **Last updated**: Update the `YYYY-MM-DD` in the blockquote to today's date.
4. **Order**: Connections are ordered by discovery date, newest first.

### What NOT to include

- Do not include connections between topics in the same category (these are filtered out during pre-filtering).
- Do not include connections without a specific, actionable insight.

---

## 9. Inspire Analysis Rules

These rules govern the cross-domain connection discovery process (Workflow 4 in SKILL.md).

### 9.1 Pre-Filter Rules (Rule-Based, No LLM)

Pre-filtering operates **exclusively** on TOPIC_INDEX metadata (the table rows). Do NOT read full Topic Note files during this step.

| Rule | Logic | Rationale |
|------|-------|-----------|
| Skip same-category | If `Category(A) == Category(B)`, skip | Cross-domain connections require different domains |
| Skip high tag overlap | If `overlap(tags_A, tags_B) / min(len(tags_A), len(tags_B)) >= 0.6`, skip | Too similar → likely obvious connection, not insightful |
| Skip already connected | If `[A] ↔ [B]` exists in CONNECTION_INDEX, skip | Avoid duplicate analysis |

**Tag overlap formula**: `intersection(tags_A, tags_B).length / min(tags_A.length, tags_B.length)`

**Edge case**: If a topic has 0 tags, skip it (cannot compute meaningful overlap).

### 9.2 Candidate Selection

After pre-filtering, select candidate pairs for LLM analysis:

1. Sort remaining pairs by tag overlap (ascending) — lower overlap means more cross-domain potential.
2. Take the **top 3-5 pairs** (configurable, default 5, max 5).
3. If fewer than 3 pairs pass pre-filtering, proceed with however many are available (even 1).

### 9.3 Token Budget

| Stage | Token Budget | Source |
|-------|-------------|--------|
| Pre-filter | 0 tokens | TOPIC_INDEX table only (already in context) |
| Read structured summaries | ~100 tokens × N candidates | Topic Note `summary` frontmatter |
| LLM analysis | < 1,000 tokens (input) | Per DESIGN.md Section 5 |
| Output (insights + CONNECTION_INDEX) | Not counted | Generated by LLM |

**Total budget per run**: < 1,000 tokens input (excluding output). Target ~500-800 tokens for 3-5 candidate pairs.

### 9.4 Insight Quality Rules

1. **Specific, not vague**: Each insight must reference concrete mechanisms, tools, or concepts from both topics.
2. **Actionable, not observational**: "你可以用 X 来做 Y" not "X 和 Y 有相似之处".
3. **One insight per perspective per pair**: For each candidate pair, attempt to generate at most one insight per perspective (迁移, 混搭, 反转). Not every perspective will yield a valid insight — that's fine.
4. **Skip forced insights**: If no genuine, actionable connection exists for a perspective, do NOT fabricate one. Only record connections that pass a "would I actually act on this?" test.

### 9.5 Insight Output Format

For each discovered connection, output follows the exact patterns defined in Section 8 (CONNECTION_INDEX Template):

- 迁移: `"这意味着你可以用 [X] 来替代/增强 [你体系中的 Y]"`
- 混搭: `"将 [A] 和 [你已有的 B] 结合，可以产生 [C]"`
- 反转: `"这提醒你：你可能需要停下 [X]，开始做 [Y]"`

Where `[X]`, `[Y]`, `[A]`, `[B]`, `[C]` are **concrete mechanisms, tools, patterns, or practices** extracted from the Topic Notes — not abstract labels.
