<p align="center">
  <img src="assets/loom-logo-transparent.png" alt="Loom logo" width="180">
</p>

<h1 align="center">Loom</h1>

<p align="center">Weave scattered sources into research that tells you what holds and what doesn't.</p>

<p align="center">
  <a href="README.zh.md">中文</a>
</p>

## Why

Ask an AI chatbot to research a topic and write an article. It'll give you a smooth, confident answer. But real research isn't smooth — sources disagree, evidence varies in quality, some claims are built on thin ice. The AI averages what it knows. Disagreements get smoothed. Weak claims sound as solid as strong ones. You get an article that reads well but you can't tell where the ground is firm and where it isn't.

Loom works differently. It reads your specific sources, not its training data. It captures them verbatim, analyzes each one independently, then synthesizes across them — but it doesn't smooth over conflicts. It tells you what the sources agree on, where they disagree, and which claims rest on weak evidence.

The result: a research article grounded in your sources, backed by an evidence map that shows you the shape of what's known, what's contested, and what's unproven. Three months later, every claim still traces to its origin.

Over time, your research compounds. Topic Notes connect across projects. Indexes build. You're not collecting chat logs — you're building a durable knowledge fabric where nothing gets lost and everything stays traceable.

Loom weaves research into knowledge.

## When NOT to use Loom

Loom is the wrong tool for:
- **One-off quick lookups.** Paste into a chat frontend — faster and cheaper.
- **Content that doesn't need source verification.** SEO posts, social media updates, generic explainers — Loom's overhead isn't worth it.
- **Volume writing.** If you need five articles a day, this isn't your tool.

Loom is the right tool when your research has stakes: a technical decision, a report, a literature review, or anything where getting it wrong costs more than the tokens.

## Who is Loom for

- **Technical leaders** evaluating architecture or tooling decisions.
- **Analysts and journalists** working with documents, reports, or expert views.
- **Researchers** doing literature review across papers and preprints.
- **Serious learners** who want to understand a domain's full landscape, not just the most popular take.

If your decision depends on knowing what's actually known — not just what's commonly said — Loom is for you.

## Skills

4 skills, each a standalone directory with `SKILL.md` and `agents/openai.yaml`.

| Skill | When to use | Output or action |
| --- | --- | --- |
| `loom` | Unsure which workflow, or need a Material List | Route + Material List |
| `loom-research` | Research: URLs/files/text to Synthesis Pack | Raw Capture + Daily Note + Source Brief + Synthesis Pack |
| `loom-write` | From research to article to knowledge consolidation | Draft/Final + Topic Note + Index update |
| `loom-maintain` | Vault governance: validate, migrate, connect, evolve, index | Validation report / migration / CONNECTION_INDEX / Evolution Summary |

## Quick look

```
Input: three articles on AI agent architecture
  → loom intake         → Material List (3 sources)
  → loom-research       → 3 Raw Captures + 3 Source Briefs + 1 Synthesis Pack
  → loom-write          → Draft article + 2 Topic Notes + Index update
```

<details>
<summary>Sample Synthesis Pack (excerpt)</summary>

```markdown
## Working Thesis
Building an effective AI agent isn't about the framework — it's about
designing the right boundary between model reasoning and tool execution.

## Conflicts
- Source 1 (Anthropic): keep agent architecture simple; augment LLM
  capabilities with clear tool interfaces
- Source 2 (OpenAI): delegate as much as possible to the platform
  (handoffs, guardrails, tracing)
- Source 3 (LangChain): compose agents as graphs with explicit state
  management

## Evidence Weight
| Claim | Sources | Weight |
|-------|---------|--------|
| Simple architectures outperform complex ones | S1, S3 | Moderate (2/3, S2 favors platform delegation) |
| Platform-managed delegation is the future | S2 | Weak (single source, newer approach) |
```
</details>

## Chaining

- **Research to article**: `loom` (intake) → `loom-research` (capture + read + synthesis) → `loom-write` (draft + topic + index)
- **Research only**: `loom` → `loom-research`
- **Write from existing research**: `loom-write`
- **Vault governance**: `loom-maintain`

## Install

```bash
npx skills add KKenny0/loom
```

For local development, copy `loom`, `loom-research`, `loom-write`, `loom-maintain` directories into your skills directory.

## Vault Contract

- Raw Capture, Daily Note, Source Brief, Synthesis Pack, Topic Note, Draft, and Final are separate artifacts. They cannot overwrite each other.
- Every Material List `raw_path` points to a real source, local file, original URL, or explicit placeholder.
- Draft and Final may use personal voice, but must not rewrite upstream evidence.
- Topic Notes use a calm vault voice, not article rhetoric or platform tone.
- Scanning, validation, and indexing live in `shared/scripts` and default to dry-run or read-only.

## Validate

```bash
for d in loom loom-research loom-write loom-maintain; do
  python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$PWD/$d"
done
```

```bash
python3 shared/scripts/scan_vault.py <vault-path>
python3 shared/scripts/validate_vault.py <vault-path>
python3 shared/scripts/build_indexes.py <vault-path>
```

## Background

```text
loom-skills/
├── loom/
├── loom-research/
│   └── references/
│       └── reading-variants.md  # reading methodology variants
├── loom-write/
├── loom-maintain/
└── shared/
    ├── references/
    │   ├── schemas.md            # all artifact schemas
    │   └── writing-pipeline.md   # pipeline reference
    └── scripts/
```

Loom is for long-lived knowledge vaults, not a content packaging toolbox. All core reading, analysis, and writing patterns are embedded directly into `loom-research` and `loom-write` — no runtime companion skill dependencies required.

## Acknowledgments

Loom's analysis and writing patterns build on ideas from:

- [ljg-skills](https://github.com/lijigang/ljg-skills) — deep reading, concept anatomy, domain decomposition, multi-perspective debate, critical writing, clarity checks
- [baoyu-skills](https://github.com/JimLiu/baoyu-skills) — content detection, markdown formatting
- [Karpathy's LLM knowledge base workflow](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — vault structure inspiration

## License

MIT
