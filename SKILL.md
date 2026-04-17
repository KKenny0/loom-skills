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

### Step 9: Report Completion

Tell the user:
- The file path of the created/updated Topic Note.
- The title and category.
- Whether it was a new note or an update.
- The number of source notes compiled.
- Confirmation that TOPIC_INDEX was updated.

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
```
