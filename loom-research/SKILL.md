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

### Reading variants

Select variant based on source type:

**Article/essay** — 4-phase reading:
1. Global Map: one-paragraph summary; classify paragraphs as 骨 (structural), 肌 (substantive), 筋 (connective); draw ASCII structure map.
2. Three-layer translation (for non-Chinese or dense text): 直译 → 意译 → 点睛.
3. Annotation: mark claims, evidence, assumptions, gaps; generate Socratic collision questions.
4. Pace: apply appropriate depth based on source importance (fast scan → medium read → slow deep-read).

**Academic paper** — 9-step extraction:
1. Problem framing: 亲历 (personal experience) → 旧路 (prior approaches) → 新口 (new angle).
2. Method translation in plain language.
3. Core concepts (minimum 3) with definitions.
4. Key insight extraction.
5. Advisor review: what would a domain expert question?
6. Personal takeaways.
7. Red line check: what must be true for the claims to hold.

**Concept/term** — 8-dimension anatomy:
History → Dialectics → Phenomenology → Linguistics → Formalization → Existentialism → Aesthetics → Meta-philosophy.
Output: anchor → 8 cuts → introspection → compression (formula + one-liner + ASCII structure).

**Any source needing depth** — vertical drilling:
Drill layers: 表象 → 机理 → 原理 → 公理 (surface → mechanism → principle → axiom). Name each layer. Identify cracks where reasoning jumps. Stop at irreducible truth.

### Output

- Source Brief per core source, following schemas.md.

### Read rules

- Separate source claims, evidence, limits, disputes, quotable lines, and claims to verify.
- Preserve source meaning and uncertainty.
- One source per Source Brief. Do not merge across sources.

### Quality check — 9 red lines

Apply as final pass on each Source Brief:
1. 口语测试: if you can't say it aloud naturally, rewrite.
2. 零术语: no unexplained jargon.
3. 短词优先: prefer short words.
4. 一句一事: one idea per sentence.
5. 具象优先: concrete over abstract.
6. 理由先行: give reason before conclusion.
7. 不说废话: no filler phrases.
8. 信任读者: trust the reader's intelligence.
9. 诚实: be honest about uncertainty.

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

Generator criteria: 独立性 (not derivable from others), 必要性 (removing breaks explanation), 生成力 (explains multiple phenomena), 简洁性 (no unnecessary complexity), 可证伪 (makes testable predictions).

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
