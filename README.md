<p align="center">
  <img src="assets/loom-logo-transparent.png" alt="Loom logo" width="180">
</p>

<h1 align="center">Loom</h1>

<p align="center">Weave scattered research threads into traceable, evolving knowledge.</p>

<p align="center">
  <a href="README.zh.md">中文</a>
</p>

## Why

Three months from now, you find a claim in your notes. Can you tell whether it came from a peer-reviewed paper, a blog post, or your own speculation?

AI chat frontends are great for quick answers. But they're ephemeral — each conversation is an island. If you research across multiple sessions, your insights scatter across chat logs, and provenance fades. You end up with a pile of plausible-sounding text and no way to trace it.

Loom is for building a durable, cumulative knowledge base. Every source is captured verbatim. Every claim traces back to its origin. Every synthesis is a separate artifact that drafts can read but never mutate. The vault compounds: your second research topic builds on the first, and over time you have something a chat log can't give you — a searchable, indexed, cross-referenced personal knowledge fabric.

Loom weaves research into knowledge.

## When NOT to use Loom

Loom is the wrong tool for one-off quick lookups. If you just want to understand a single article or get a fast answer, use a chat frontend — it'll be faster and cheaper.

Loom is the right tool when you're building knowledge that compounds. If you expect to revisit a topic, connect it to other topics, or write from it later, the structure pays for itself.

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
