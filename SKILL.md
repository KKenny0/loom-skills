# Knowledge Compiler — Claude Code Skill

> Turn Claude Code into an autonomous knowledge compiler.
> Give it a URL, text, or file → get a structured Daily Note or Topic Note + auto-updated index.

---

## When This Skill Activates

This skill activates when you (Claude Code) receive any of these inputs:

1. **A URL** — Compile it into a Daily Note.
2. **Raw text or a pasted article** — Compile it into a Daily Note.
3. **A path to a markdown file** — Compile it into a Daily Note.
4. **A request to compile Topic Notes from existing Daily Notes** — Aggregate into a Topic Note.
5. **A topic name with instruction to create/compile** — Create a Topic Note from specified sources.

### How to Detect the Operation

| User Input | Operation | Output |
|------------|-----------|--------|
| URL, raw text, or file path | **Daily Note Compile** | `01_Daily_Notes/YYYY/inbox/YYYY-MM-DD_title.md` |
| "compile topic [name]" or "create topic note from [sources]" | **Topic Note Compile** | `02_Topic_Notes/[Category]/YYYY-MM-DD_Title.md` |

If the user's intent is ambiguous, default to **Daily Note Compile** (most common operation).

---

## Prerequisites

Before compiling, you need to know the **vault root path**. Check in this order:

1. User specified it explicitly → use that path.
2. Check if a file `.knowledge-compiler-vault` exists in the current working directory → read the path from it.
3. Ask the user: "What is the path to your knowledge vault?"

All paths below are relative to the vault root.

You also need to have **SCHEMA.md** available. Read it once at the start of each compilation to ensure you follow the exact templates.

---

## Workflow 1: Daily Note Compile

### Step 1: Ingest the Source

- **URL**: Fetch the content using your web tools. Extract the main article text, stripping navigation, ads, and boilerplate.
- **Text**: Use the provided text directly.
- **File**: Read the file from the given path.

If the source cannot be fetched or is empty, respond with: `"Error: Could not extract content from the source. Please provide a valid URL, text, or file path."` and stop.

### Step 2: Determine Metadata

From the ingested content, determine:

- **title**: A descriptive title in the source's original language. Keep it concise (5-10 words).
- **source_url**: The original URL, or `"local"` if text/file.
- **source_type**: `"web-clip"` for URLs, `"text"` for pasted text, `"file"` for file paths.
- **tags**: 2-6 lowercase tags with hyphens. Prefer tags that already exist in recent Daily Notes in the vault.

### Step 3: Generate Content

Using your LLM capabilities, generate the three required sections:

1. **Summary**: 3-5 sentences capturing the essence of the source.
2. **Key Points**: 3-8 bullet points. Each must be a concrete assertion, not a topic label.
3. **Details**: Full content organized with `###` sub-headers. Preserve the source's structure and key information.

### Step 4: Write the Daily Note

Create the file at:
```
01_Daily_Notes/YYYY/inbox/YYYY-MM-DD_short-kebab-title.md
```

Use the **Daily Note Template** from SCHEMA.md verbatim. Fill in all frontmatter fields. Do not add or remove any fields.

Example output file:
```markdown
---
title: "Hermes Agent Messaging Gateway 深度解析"
date: "2026-04-17"
status: "inbox"
source_url: "https://example.com/hermes-messaging"
source_type: "web-clip"
tags: [hermes, messaging, gateway, ai-agent]
---

## Summary
Hermes Agent 的消息网关是一个统一的多平台桥接层...
（3-5 sentences）

## Key Points
- 消息网关通过单一后台进程连接所有配置的消息平台
- 会话持久化策略支持 daily 和 idle 两种重置模式
（3-8 bullets）

## Details
### 核心架构
...
### 配置与使用
...
```

**If the file already exists**, append a number: `YYYY-MM-DD_short-kebab-title-2.md`.

### Step 5: Report Completion

Tell the user:
- The file path of the created Daily Note.
- The title.
- The number of Key Points generated.

**Do NOT auto-compile a Topic Note** — that is a separate explicit operation.

---

## Workflow 2: Topic Note Compile

### Step 1: Identify Sources

The user must specify one of:
- A list of Daily Note file paths or titles.
- A topic name (you will search for relevant Daily Notes).
- A combination of Daily Notes and existing Topic Notes.

**If a topic name is given without specific files:**
1. Read `00_Index/TOPIC_INDEX.md` to check if a Topic Note for this topic already exists.
2. Search `01_Daily_Notes/YYYY/inbox/` for Daily Notes whose titles or tags are relevant to the topic.
3. List the candidate source files and confirm with the user before proceeding.

### Step 2: Read All Source Material

Read every source file completely. For each file, extract:
- The key assertions and insights.
- The structured content (summaries, details, key points).
- The tags and metadata.

### Step 3: Determine Category

From the aggregated content, determine the most appropriate category:
- Check existing category directories in `02_Topic_Notes/` for matches.
- If no existing category fits, create a new one using Pascal_Case (e.g., `New_Category`).
- Common categories: `AI_Agent`, `Claude_Code`, `Coding_Agent`, `LLM_Models`, `OpenClaw`, `Video_Generation`.

### Step 4: Determine Metadata

- **title**: Descriptive title for the synthesized knowledge.
- **category**: The category chosen in Step 3.
- **compiled_from**: List the filenames of all source Daily Notes and/or Topic Note titles.
- **tags**: 2-8 tags synthesized from source tags. Keep existing tags where relevant, add new ones for novel concepts.
- **related_topics**: Check TOPIC_INDEX for related Topic Notes. Use wiki-link format `[[Topic Name]]`.

### Step 5: Generate Structured Summary

Fill all 4 mandatory fields:
- **core_idea**: One sentence. The single most important takeaway.
- **key_mechanism**: The primary mechanism, method, or technique.
- **applicable_to**: Concrete scenarios where this applies.
- **unique_insight**: What makes this different from conventional approaches.

### Step 6: Generate Content Sections

1. **Summary**: 3-5 sentences synthesizing all sources.
2. **Key Points**: 5-12 bullet points. Deduplicate overlapping points from multiple sources.
3. **Detailed Explanation**: Comprehensive synthesis with `###` sub-headers. Go deeper than any single source.
4. **Related Work**: References, alternatives, prior art mentioned in sources.
5. **Questions**: 2-5 genuine open questions for future exploration.

### Step 7: Write the Topic Note

Create the file at:
```
02_Topic_Notes/[Category]/YYYY-MM-DD_Title-With-Words.md
```

Use the **Topic Note Template** from SCHEMA.md verbatim. Fill in all frontmatter fields including the nested `summary` object.

**If a Topic Note with the same title already exists in the category:**
1. Read the existing Topic Note.
2. Merge: update content, increment `version` (minor bump, e.g., `1.0.0` → `1.1.0`), add new sources to `compiled_from`.
3. Overwrite the existing file.

### Step 8: Update TOPIC_INDEX

After writing the Topic Note, update `00_Index/TOPIC_INDEX.md`:

1. **Read** the existing TOPIC_INDEX.md.
2. **Check** if an entry with the same title already exists in the table.
3. **If exists**: Update that row's Category, Core Idea, Tags, and Date columns. Do NOT change its position.
4. **If new**: Append a new row at the end of the table.
5. **Update** the `Last updated: YYYY-MM-DD` in the blockquote to today's date.

Use the format from SCHEMA.md TOPIC_INDEX Template verbatim.

### Step 9: Update TIMELINE_INDEX

After updating TOPIC_INDEX, update `00_Index/TIMELINE_INDEX.md`:

1. **Read** the existing TIMELINE_INDEX.md (create if it doesn't exist, using the template from SCHEMA.md Section 6).
2. **Determine** whether this is a New Topic or Updated Topic:
   - Search TIMELINE_INDEX for any prior month's entry with the same title.
   - If found in a prior month → **Updated Topic**.
   - If not found anywhere → **New Topic**.
3. **Check idempotency**: If an entry for this topic already exists in the current month's section (same title, same section), **skip** — do not duplicate.
4. **Add entry**: Under the current month's `## YYYY-MM` header, add to the appropriate section:
   - New Topic → `### New Topics`
   - Updated Topic → `### Updated Topics`
   - Format: `- [[Title]] (YYYY-MM-DD) - Category`
5. **Create month header** if `## YYYY-MM` for the current month does not exist. Insert in chronological order (newest first, before older months).
6. **Update** the `Last updated: YYYY-MM-DD` in the blockquote to today's date.

Use the format from SCHEMA.md TIMELINE_INDEX Template verbatim.

### Step 10: Report Completion

Tell the user:
- The file path of the created/updated Topic Note.
- The title and category.
- Whether it was a new note or an update.
- The number of source notes compiled.
- Confirmation that TOPIC_INDEX was updated.
- Confirmation that TIMELINE_INDEX was updated.

---

### Status Transitions and TIMELINE_INDEX

When a Daily Note changes status (inbox → working → published → archived):
1. Check if the Daily Note's filename appears in any Topic Note's `compiled_from` field.
2. If yes, and the status changes to `archived`, add the Topic Note to the current month's `### Archived` section in TIMELINE_INDEX.
3. Status transitions other than `archived` do not trigger TIMELINE_INDEX updates.

---

## Workflow 3: Evolution Summary

### Trigger Conditions

This workflow activates when the user explicitly requests an evolution summary. Recognizable patterns:
- "generate monthly summary" / "generate evolution for YYYY-MM"
- "quarterly summary" / "evolution for YYYY-QN"
- "annual summary" / "yearly evolution for YYYY"
- "知识演进" / "演进总结"

### Step 1: Determine the Summary Period

Parse the user's request to determine:
- **Period type**: Monthly, Quarterly, or Annual.
- **Period value**: e.g., `2026-04`, `2026-Q2`, `2026`.

If the user doesn't specify a period, default to **monthly for the current month**.

### Step 2: Read TIMELINE_INDEX

Read `00_Index/TIMELINE_INDEX.md` and extract entries for the target period:
- **Monthly**: Read the `## YYYY-MM` section.
- **Quarterly**: Read the three `## YYYY-MM` sections for the quarter.
- **Annual**: Read all `## YYYY-MM` sections for the year.

Collect all New Topics, Updated Topics, and Archived entries.

### Step 3: Read TOPIC_INDEX

Read `00_Index/TOPIC_INDEX.md` for metadata (Core Idea, Tags) of the topics found in Step 2.

### Step 4: Read Selected Topic Notes

For token efficiency, only read full Topic Notes that are:
- Listed as **New Topics** in the target period.
- Listed as **Updated Topics** in the target period.

**Skip** reading Topic Notes that are only listed as **Archived**.

For **quarterly and annual** summaries: check if monthly evolution summaries already exist in `03_Content_Output/Longform/`. If they do, read those instead of re-reading individual Topic Notes.

### Step 5: Generate the Evolution Summary

Use the EVOLUTION_TEMPLATE.md template to generate the summary. Fill in each section:

1. **本期新增主题** — Summarize new topics added in the period.
2. **本期关键发现** — Highlight the most impactful insights across all topics.
3. **知识演进趋势** — Identify trends: what areas are growing, what themes emerge.
4. **跨领域连接发现** — Placeholder for Phase 3 (note as "pending CONNECTION_INDEX implementation").

### Step 6: Write the Evolution Summary

Write to:
```
03_Content_Output/Longform/Evolution_YYYY-MM.md      (monthly)
03_Content_Output/Longform/Evolution_YYYY-QN.md      (quarterly)
03_Content_Output/Longform/Evolution_YYYY.md          (annual)
```

Use the template from EVOLUTION_TEMPLATE.md verbatim.

### Step 7: Report Completion

Tell the user:
- The file path of the generated evolution summary.
- The period covered.
- Number of new topics, updated topics, and archived topics.
- Key trends identified.

---

## Workflow 4: Inspire Analysis

### Trigger Conditions

This workflow activates when the user explicitly requests an inspire analysis or cross-domain connection discovery. Recognizable patterns:
- "find connections" / "discover connections" / "inspire analysis"
- "启发分析" / "跨领域连接" / "发现连接"
- "run inspire" / "inspire me"

### Overview

The Inspire Analysis discovers cross-domain connections between Topic Notes and generates actionable insights. It uses a 3-step pipeline optimized for token efficiency:

```
TOPIC_INDEX metadata
       ↓
Step 1: Rule pre-filter (0 tokens)
       ↓  (skip same-category, skip high tag overlap)
Candidate pairs (3-5)
       ↓
Step 2: Read structured summaries (~100 tokens each)
       ↓
Step 3: LLM semantic analysis (< 1,000 tokens input)
       ↓
Insights (迁移/混搭/反转)
       ↓
Update CONNECTION_INDEX.md
```

### Step 1: Rule Pre-Filter

Read `00_Index/TOPIC_INDEX.md` and extract the metadata table. Using **only** the table data (do NOT read full Topic Note files):

1. **Collect all topics**: Extract title, category, tags for every row in TOPIC_INDEX.
2. **Generate all possible pairs**: For every combination of two topics (A, B) where A ≠ B.
3. **Apply pre-filter rules** (per SCHEMA.md Section 9.1):
   - **Skip same-category**: If `Category(A) == Category(B)`, discard this pair.
   - **Skip high tag overlap**: Compute `intersection(tags_A, tags_B).length / min(tags_A.length, tags_B.length)`. If ≥ 0.6, discard this pair.
   - **Skip already connected**: If `[A] ↔ [B]` or `[B] ↔ [A]` already exists in `00_Index/CONNECTION_INDEX.md`, discard this pair.
   - **Skip topics with 0 tags**: If either topic has an empty tags field, discard.
4. **Sort remaining pairs** by tag overlap ascending (lower overlap first = more cross-domain potential).
5. **Select top 3-5 pairs** (default 5, max 5) for analysis.

**If fewer than 3 pairs remain**, proceed with however many are available (even 1).
**If 0 pairs remain**, report to the user: "No suitable cross-domain candidate pairs found. Consider adding more topics or reducing tag overlap threshold."

### Step 2: Read Structured Summaries

For each selected candidate pair, read the **`summary` frontmatter block** from both Topic Note files:

```
00_Index/TOPIC_INDEX.md → identify Topic Note paths
02_Topic_Notes/[Category]/[Topic Note file] → read only the summary block
```

Read **only** the `summary` field from the frontmatter (core_idea, key_mechanism, applicable_to, unique_insight). Do NOT read the full body of the Topic Note. This keeps each topic at ~100 tokens.

If a Topic Note file referenced in TOPIC_INDEX cannot be found, skip that pair and move to the next candidate.

### Step 3: LLM Semantic Analysis

For each candidate pair, analyze the two structured summaries and attempt to generate actionable insights in three perspectives:

| 视角 | 问题 | 输出句式 |
|------|------|----------|
| 迁移 (Transfer) | 某机制能否移植升级你的体系？ | "这意味着你可以用 [X] 来替代/增强 [你体系中的 Y]" |
| 混搭 (Mix) | 某组件和你已有的东西组合能产生什么？ | "将 [A] 和 [你已有的 B] 结合，可以产生 [C]" |
| 反转 (Reverse) | 某做法和你的默认假设相反吗？ | "这提醒你：你可能需要停下 [X]，开始做 [Y]" |

**Rules for insight generation** (per SCHEMA.md Section 9.4):
- Each insight must reference **concrete** mechanisms, tools, or concepts from both topics.
- Each insight must be **actionable** — "能用"，不是"能想"。"You can use X to do Y" not "X and Y are related".
- Not every perspective will yield a valid insight. **Skip forced insights** — if no genuine actionable connection exists, do NOT fabricate one.
- At most **one insight per perspective per pair**.

### Step 4: Update CONNECTION_INDEX

For each discovered connection (each insight that passed the quality check):

1. **Read** `00_Index/CONNECTION_INDEX.md` (create if it doesn't exist, using the template from SCHEMA.md Section 8).
2. **Check for duplicates**: Verify `[Topic A] ↔ [Topic B]` or `[Topic B] ↔ [Topic A]` does not already exist.
3. **Append** the new connection entry at the end of the file:
   ```markdown
   ## [[Topic A]] ↔ [[Topic B]]
   - **连接类型**: [迁移|混搭|反转]
   - **启发**: [exact insight following the sentence pattern]
   - **发现日期**: YYYY-MM-DD
   ```
4. **Update** the `Last updated: YYYY-MM-DD` in the blockquote to today's date.

### Step 5: Report Completion

Tell the user:
- Number of candidate pairs analyzed.
- Number of connections discovered (broken down by type: 迁移, 混搭, 反转).
- A brief summary of the most impactful insight.
- Confirmation that CONNECTION_INDEX was updated.

If no connections were discovered, explain why and suggest:
- Adding more topics across different categories.
- Reducing the tag overlap threshold.
- Checking if topics have sufficient tag metadata.

---

## Edge Cases

### Empty Input
If the user provides an empty string or a URL that returns no content, respond:
> "Could not extract any content. Please provide a valid URL, non-empty text, or an existing file path."

### Malformed Content
If the source content is garbled, incomplete, or appears to be an error page:
- Attempt to extract whatever useful content exists.
- If nothing useful can be extracted, respond: "The source appears to be empty or malformed. Please check and try again."

### Existing Files
- Daily Notes: Append a number suffix if the filename exists.
- Topic Notes: Merge and overwrite if the title matches (see Step 7 of Workflow 2).

### Category Detection
- First check existing category directories for a match.
- If uncertain between two categories, pick the more specific one.
- If the content spans multiple categories, use the one most central to the content.

### TOPIC_INDEX Does Not Exist
If `00_Index/TOPIC_INDEX.md` does not exist, create it with the header and table header from the template, then add the first entry.

### TIMELINE_INDEX Does Not Exist
If `00_Index/TIMELINE_INDEX.md` does not exist, create it with the header from the TIMELINE_INDEX template in SCHEMA.md Section 6, then add the current month's section and entry.

### Vault Directory Does Not Exist
If any required directory (`01_Daily_Notes/YYYY/inbox/`, `02_Topic_Notes/[Category]/`, `00_Index/`) does not exist, create it before writing.

---

## Token Efficiency Notes

- **TOPIC_INDEX is the primary lookup mechanism.** Always read it before scanning directories.
- When searching for relevant Daily Notes, use tags and titles rather than reading every file.
- For Topic Note compilation, read source files completely — there is no shortcut for quality synthesis.
- The structured summary in Topic Notes is designed to be ~100 tokens — this enables future cross-topic analysis without reading full notes.

---

## Quick Reference

```
Input: URL / text / file
         ↓
    Daily Note Compile
         ↓
    01_Daily_Notes/YYYY/inbox/YYYY-MM-DD_title.md

Input: "compile topic [X]" or "create topic note from [sources]"
         ↓
    Topic Note Compile
         ↓
    02_Topic_Notes/[Category]/YYYY-MM-DD_Title.md
         ↓
    Update 00_Index/TOPIC_INDEX.md
         ↓
    Update 00_Index/TIMELINE_INDEX.md

Input: "generate monthly summary" or "compile evolution for 2026-04"
         ↓
    Evolution Summary (Workflow 3)
         ↓
    Read TIMELINE_INDEX + TOPIC_INDEX + select Topic Notes
         ↓
    03_Content_Output/Longform/Evolution_YYYY-MM.md

Input: "inspire analysis" / "find connections" / "启发分析"
         ↓
    Inspire Analysis (Workflow 4)
         ↓
    Read TOPIC_INDEX → Rule pre-filter (0 tokens)
         ↓
    Select 3-5 candidate pairs (cross-category, low tag overlap)
         ↓
    Read structured summaries (~100 tokens each)
         ↓
    LLM analyze: 迁移/混搭/反转 (< 1,000 tokens)
         ↓
    Update 00_Index/CONNECTION_INDEX.md
```
