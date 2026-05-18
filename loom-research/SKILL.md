---
name: loom-research
description: Capture, read, and synthesize source material into a Synthesis Pack. Use when the user asks to research a topic, process materials, read sources, or build a research package from URLs, PDFs, files, pasted text, or topic keywords.
---

# Loom Research

One skill for the full research pipeline: capture → read → synthesize.

## Read First

- `../shared/references/schemas.md` (all artifact formats)

## Pipeline

```
Input (URLs, files, text, Material List)
  → Capture: preserve source + create inbox Daily Note
  → Read: deep-read each source into a Source Brief
  → Synthesize: combine Source Briefs into a Synthesis Pack
```

## Stage 1 — Capture

Preserve source material before analysis.

### Capture flow

1. Fetch source content using AI web tools (not external companion skills).
2. Detect content type: article, paper, tutorial, documentation, social thread, transcript.
3. Analyze structural elements: headings, lists, code blocks, tables, quotes.
4. Generate YAML frontmatter with type-appropriate fields (source_url, title, author, date_captured, capture_method).
5. Create descriptive title from content if missing.
6. Apply formatting: consistent heading hierarchy, proper list formatting, preserve code blocks.
7. Save as Raw Capture + create inbox Daily Note pointing to it.

### Output

- Raw Capture with source identity and retrieval metadata.
- Inbox Daily Note: `01_Daily_Notes/YYYY/inbox/YYYY-MM-DD_slug.md`.

### Capture rules

- Preserve source wording and source meaning. No AI commentary, rhetorical framing, or title optimization.
- Distinguish Raw Capture (source) from Daily Note (reference).
- `raw_path` must resolve to a real file, original URL, or explicit local text marker.

## Stage 2 — Read

Deep-read one source into a Source Brief.

### Select reading variant

| Source Type | Variant | When |
|-------------|---------|------|
| Article / essay | 4-phase reading | Narrative prose with argument structure |
| Academic paper | 9-step extraction | Peer-reviewed, methodology-heavy |
| Concept / term | 8-dimension anatomy | Single concept needing full decomposition |
| Any source needing depth | Vertical drilling | Follow a thread to its root |

Read the detailed methodology in `references/reading-variants.md` for the selected variant.

### Output

- Source Brief per core source, following schemas.md.

### Read rules

- Separate source claims, evidence, limits, disputes, quotable lines, and claims to verify.
- Preserve source meaning and uncertainty.
- One source per Source Brief. Do not merge across sources.
- Each Source Brief is quarantined: reference only its own source. No cross-references to other sources' claims, frameworks, or terminology. Cross-source analysis belongs in the Synthesis Pack, never in Source Briefs.
- Apply 9 red lines quality check (in `references/reading-variants.md`) as final pass.

## Stage 3 — Synthesize

Combine Source Briefs into a Synthesis Pack.

### Synthesis flow

**First pass — decomposition to generators:**
1. 铺现象: lay out observed phenomena from all sources.
2. 列候选: list candidate generators that could explain patterns.
3. 递归追问: recursively ask "why?" of each candidate.
4. 合并同源: merge candidates sharing the same root cause.
5. 砍: cut candidates derived from deeper ones.
6. 反生成: verify remaining generators can re-generate the phenomena.
7. 预测+变更双测: predict what would change if each generator were altered.

Generator criteria: 独立性 (not derivable from others), 必要性 (removing breaks explanation), 生成力 (explains multiple phenomena), 简洁性 (no unnecessary complexity), 可证伪 (makes testable predictions). Explicitly evaluate each surviving generator against all 5 criteria in the output — do not apply them implicitly.

**Second pass — multi-perspective stress test:**
- Moderator is truth-seeking (not balanced — seeks best-supported position).
- Invite 3-5 perspectives (real traditions or named frameworks).
- Each perspective responds to evidence and to other perspectives.
- Moderator synthesis: identify convergence, remaining disagreements, ASCII framework diagrams.

### Output

- Synthesis Pack following schemas.md: Working Thesis, Merged Conclusions, Conflicts, Evidence Weight, Consensus/Disagreement, Article Spine, High-Risk Claims, Source Coverage Checklist.

### Synthesis rules

- Distinguish source consensus from user thesis.
- Do not hide unresolved conflicts or collapse them into false consensus.
- Mark high-risk claims before any drafting.
- Drafts can read this pack; they must not mutate it.

## Full Pipeline Rules

- Do not draft publication prose except as outline or thesis notes in the Synthesis Pack.
- If the user provides a Material List from `loom` intake, use it as the source ledger.
- If no Material List exists, create one before starting capture.
- Every Daily Note must point to a real source via `raw_path`.
