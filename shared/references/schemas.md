# Loom Schemas

Single reference for all Loom artifact schemas, vault layout, and index formats.

## Directory Layout

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

## Status Values

`inbox` | `working` | `reviewed` | `published` | `archived`

Legacy `done` is preserved during migration. New files use the five values above.

---

## Vault Config

Path: `<vault-root>/.loom/config.yaml`

Created by cold-start interview on first `loom` invocation. Read by all sub-skills to apply user preferences.

```yaml
vault_path: "/absolute/path/to/vault"
language: "zh"           # zh | en | auto
categories:              # Initial topic categories for 02_Topic_Notes/
  - "AI_Agent"
  - "Software_Architecture"
output_depth: "standard" # quick | standard | deep
created: "2026-05-19"
```

Rules: all sub-skills read config if it exists. Config values are defaults — user can override per query. Editing `.loom/config.yaml` directly is supported; re-running cold-start is also supported by saying "reconfigure" during `loom` intake.

---

## Material List

Created during intake before any reading or drafting.

```markdown
# Material List — [Task Title]

> Created: YYYY-MM-DD
> Task type: single-source deep dive | multi-source synthesis | theme research | draft rewrite

| ID | Title | Author | Date | Type | Source Tier | Relevance | Citation Usability | Risk Level | Raw Path | Capture Status |
|----|-------|--------|------|------|-------------|-----------|--------------------|------------|----------|----------------|
| S1 | ... | ... | ... | article | primary | high | direct | low | https://... | pending |
```

Fields: `ID` (S1, S2, …), `Title`, `Author`, `Date`, `Type` (article|paper|docs|x-thread|youtube|book|file|text|other), `Source Tier` (primary|secondary|commentary|social|unknown), `Relevance` (high|medium|low), `Citation Usability` (direct|background|not-citable|unknown), `Risk Level` (low|medium|high), `Raw Path` (real URL/file/marker), `Capture Status` (pending|captured|failed|skipped).

---

## Raw Capture

Preserves source material before analysis.

```markdown
---
source_id: "S1"
title: "[Source Title]"
source_url: "[URL or local]"
source_type: "[web-clip|x-thread|youtube|paper|file|text]"
retrieved_at: "YYYY-MM-DD"
capture_tool: "[tool name or manual]"
raw_path: "[path or URL]"
extraction_notes: "[brief notes]"
---
```

Rules: preserve source wording. No rhetorical framing or title optimization. `raw_path` must resolve to a real source.

---

## Daily Note

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

Rules: source language for title/body. Lowercase English hyphenated tags (2-8). Filename: `YYYY-MM-DD_short-kebab-title.md`. Default: `01_Daily_Notes/YYYY/inbox/`. If no `source_url`, use `"local"`. `raw_path` must point to a real source. Preserve source semantics; do not rewrite with publication voice.

Legacy: preserve `source` field if present; preserve unknown frontmatter fields (`aliases`, `author`, `assets_dir`, `identifier`, `venue`, `cssclasses`, `platform`).

---

## Source Brief

Result of deep-reading one source.

```markdown
# Source Brief — [Source Title]

source_id: S1
raw_path: [raw path]
brief_date: YYYY-MM-DD

## Core Conclusion
[The source's main conclusion.]

## Source Claims
- [Claim made by the source]

## Key Evidence
- [Evidence supporting claims]

## Argument Path
1. [How the source gets from premise to conclusion]

## Limits
- [Scope, assumptions, caveats, missing evidence]

## Quotable Lines
- "[Short quote or paraphrasable expression]" — [context]

## Disputes / Tensions
- [Internal tension or conflict with other known sources]

## Claims To Verify
- [High-impact claim needing verification]
```

Rules: keep source claims separate from your thesis. Preserve uncertainty. One source per brief.

---

## Synthesis Pack

Combines multiple Source Briefs into an article-ready research package.

```markdown
# Synthesis Pack — [Working Title]

created: YYYY-MM-DD
source_ids: [S1, S2]

## Key Findings
- [3-5 most important discoveries across all sources]

## Working Thesis
[User/article thesis.]

## Analysis Summary
[3-5 sentences. Which generators survived decomposition, which criteria were
weakest. No step-by-step transcript.]

## Stress Test Summary
[3-5 sentences. Which perspectives converged, where they disagreed, what the
evidence best supports. Include ASCII framework diagram only if it adds clarity.]

## Merged Conclusions
- [Conclusion supported by multiple sources]

## Conflicts
| Issue | Source A | Source B | Resolution / Treatment |
|-------|----------|----------|------------------------|
| ... | ... | ... | ... |

## Evidence Weight
| Claim | Evidence Strength | Sources | Notes |
|-------|-------------------|---------|-------|
| ... | strong/medium/weak | S1, S2 | ... |

## Consensus And Disagreement
### Consensus
- [...]

### Disagreement
- [...]

## Article Spine
1. [Main section]

## High-Risk Claims
- [Claim] — risk: [why] — action: verify | soften | exclude | mark uncertainty

## Source Coverage Checklist
| Source ID | Used In Thesis | Used In Evidence | Needs More Review | Notes |
|-----------|----------------|------------------|-------------------|-------|
| S1 | yes/no | yes/no | yes/no | ... |
```

Rules: distinguish source consensus from user thesis. Do not hide conflicts. Mark high-risk claims. Drafts can read this but must not mutate it. Key Findings: 3-5 bullets max, single-line each, no methodology. Analysis Summary and Stress Test Summary: 3-5 sentences each, no reasoning transcript.

---

## Topic Note

### Link-Only Mode

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

Rules: Category directories use Pascal_Case. Filename: `YYYY-MM-DD_Title-With-Words.md`. Update → increment minor version. Preserve link-only notes. Input priority: Synthesis Pack > reviewed Daily Notes > Final/Published Article. Do not create from unreviewed Drafts by default. Use calm knowledge-base voice.

---

## TOPIC_INDEX

Path: `00_Index/TOPIC_INDEX.md`

```markdown
# Topic Index

> Auto-generated. Last updated: YYYY-MM-DD

| Title | Category | Mode | File | Core Idea | Tags | Date |
|-------|----------|------|------|-----------|------|------|
| [[Topic 1]] | Claude_Code | synthesis | 02_Topic_Notes/Claude_Code/2026-01-01_Topic-1.md | ... | tag1, tag2 | 2026-01-01 |
```

Rules: match by exact title, update in place, append new rows. `Core Idea` from `summary.core_idea`.

---

## TIMELINE_INDEX

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

Rules: months newest first. All three section headers present. One appearance per section per month. Newest first within sections. Daily Notes excluded.

---

## CONNECTION_INDEX

Path: `00_Index/CONNECTION_INDEX.md`

```markdown
# Connection Index

> Auto-generated. Last updated: YYYY-MM-DD

## [[Topic A]] ↔ [[Topic B]]
- **连接类型**: 迁移
- **启发**: 这意味着你可以用 [X] 来替代/增强 [Y]
- **发现日期**: YYYY-MM-DD
```

Rules: append after blockquote, newest first. No duplicate pairs. Types: `迁移`, `混搭`, `反转`. Every insight must be concrete and actionable.

---

## Evolution Summary

Output: `03_Content_Output/Longform/Evolution_YYYY-MM.md` (monthly), `Evolution_YYYY-QN.md` (quarterly), `Evolution_YYYY.md` (annual).

Frontmatter: `type: "evolution-summary"`, `period`, `period_type`, `generated_at`, `source_topics_new`, `source_topics_updated`, `source_topics_archived`.

Sections: 本期新增主题 → 本期关键发现 → 知识演进趋势 → 跨领域连接发现 → 附录数据.

Token efficiency: monthly reads TIMELINE + TOPIC + new/updated Topic Notes; quarterly reads 3 monthly sections or existing monthly summaries; annual reads quarterly summaries. CONNECTION_INDEX filtered by period. Do not re-run connection analysis.

---

## Migration Compatibility

When migrating existing vaults:

1. Preserve all existing content.
2. Preserve unknown frontmatter fields.
3. Add missing fields only with high-confidence inference.
4. Do not rewrite bodies to fit templates.
5. Do not move assets unless requested.
6. Prefer additive changes.
7. Path location is a status hint — do not silently overwrite conflicting frontmatter.
