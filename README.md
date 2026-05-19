<p align="center">
  <img src="assets/loom-logo-transparent.png" alt="Loom logo" width="180">
</p>

<h1 align="center">Loom</h1>

<p align="center">Weave scattered research threads into traceable, evolving knowledge.</p>

<p align="center">
  <a href="README.zh.md">中文</a>
</p>

## Why

Loom is a Claude Code skill pack for personal knowledge vaults. It treats AI-assisted research as a staged pipeline rather than a one-shot chat: sources become threads, the workflow is the loom, and the vault is the fabric.

AI can summarize quickly and draft fluent prose. Without stages, schemas, and write boundaries, research drifts: sources blur into opinions, drafts overwrite evidence, indexes depend on memory, and older claims become hard to trace. The result: three months later, you find a claim in your notes and can't tell whether it came from a peer-reviewed paper, a blog post, or your own speculation.

Loom keeps the work structured: inventory material, capture sources, read deeply, synthesize across sources, draft prose, consolidate Topic Notes, maintain indexes, discover cross-topic links, and report knowledge evolution.

Loom weaves research into knowledge.

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
Input: three URLs on emergence theory
  → loom intake         → Material List (3 sources)
  → loom-research       → 3 Raw Captures + 3 Source Briefs + 1 Synthesis Pack
  → loom-write          → Draft article + 2 Topic Notes + Index update
```

<details>
<summary>Sample Synthesis Pack (excerpt)</summary>

```markdown
## Working Thesis
Emergence is not a single phenomenon but a family of pattern-level
behaviors that appear when simple components interact under constraints.

## Conflicts
- Source 1 (physicist): emergence requires irreducibility
- Source 2 (complexity scientist): emergence is just computational
  compression — no new physics needed
- Source 3 (philosopher): both views collapse the phenomenological
  experience of "something new"

## Evidence Weight
| Claim | Sources | Weight |
|-------|---------|--------|
| Emergence is irreducible | S1, S3 | Moderate (2/3, S2 disputes) |
| Computational compression suffices | S2 | Weak (single source, disputed) |
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
