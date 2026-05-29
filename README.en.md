<p align="center">
  <img src="assets/loom-logo-transparent.png" alt="Loom logo" width="180">
</p>

<h1 align="center">Loom</h1>

<p align="center">Weave scattered sources into research that tells you what holds and what doesn't.</p>

<p align="center">
  <a href="README.md">中文</a>
</p>

## Why

Ask an AI chatbot to research a topic and write an article. It'll give you a smooth, confident answer. But real research isn't smooth — sources disagree, evidence varies in quality, some claims are built on thin ice. The AI averages what it knows. Disagreements get smoothed. Weak claims sound as solid as strong ones. You get an article that reads well but you can't tell where the ground is firm and where it isn't.

Loom works differently. It reads your specific sources, not its training data. It captures them verbatim, analyzes each one independently, then synthesizes across them — but it doesn't smooth over conflicts. It tells you what the sources agree on, where they disagree, and which claims rest on weak evidence.

The result: a research article grounded in your sources, backed by an evidence map that shows you the shape of what's known, what's contested, and what's unproven. Three months later, every claim still traces to its origin. Over time, Topic Notes connect across projects and research compounds.

Loom weaves research into knowledge.

For situations where research results carry stakes: technical decisions, analytical reports, literature reviews — anything where getting it wrong costs more than the tokens.

## When NOT to use Loom

Loom is the wrong tool for:
- **One-off quick lookups.** Paste into a chat frontend — faster and cheaper.
- **Content that doesn't need source verification.** SEO posts, social media updates, generic explainers — Loom's overhead isn't worth it.
- **Volume writing.** If you need five articles a day, this isn't your tool.

## Architecture

Three research skills, three thinking lenses, one vault tool. Each skill is standalone — no vault required.

```
Research layer (sources → complete article, each standalone):
  deep-read       Papers, articles, reports → research article    [this repo]
  source-dive     Technical source code → deep analysis article   [KKenny0/source-dive]
  survey          Domain name/direction → structured domain map   [this repo]

Thinking lenses (apply to any Loom artifact or raw input):
  excavate        Assumption archaeology — dig beneath the surface
  debate          Dialectical reasoning — thesis → antithesis → aufhebung
  forge           Conceptual forging — cross-domain synthesis and new ideas

Optional vault infrastructure (personal use, open-source users can ignore):
  loom-maintain   Vault health + Topic Notes + index maintenance  [this repo]
```

## Skills

| Skill | When to use | Output |
| --- | --- | --- |
| `deep-read` | Deep-read papers, articles, reports, interviews → research article | Raw Capture + Source Brief + Synthesis Pack + Research Article |
| `survey` | Want to understand a domain's landscape, enter a new direction, or find a survey-style domain map | Domain map (research programmes → debates → evolution → open problems → entry points) |
| `excavate` | Want to understand why a claim holds, or dig into hidden premises | Excavation report (assumption archaeology) |
| `debate` | Dialectical analysis of a controversy or opposing positions | 辩证记录 (dialectical reasoning with aufhebung) |
| `forge` | Forge new concepts from cross-domain sources | 锻造图 (atomic concepts → cross-domain mapping → new ideas) |
| `loom-maintain` | Vault governance: validate, migrate, connect, evolve, Topic Notes, index | Validation report / Topic Note / CONNECTION_INDEX / Evolution Summary |

## Quick look

```
Input: three articles on AI agent architecture
  → deep-read           → 3 Source Briefs + 1 Synthesis Pack + 1 Research Article
  → excavate (opt)      → assumption report on key claims
  → debate (opt)        → dialectical resolution of conflicting findings
  → forge (opt)         → cross-domain concept map from Topic Notes
  → loom-maintain (opt) → 2 Topic Notes + Index update

Input: a new research direction
  → survey              → domain map (programmes, debates, evolution, open problems, entry points)
  → deep-read (opt)     → deep-read key papers from the entry recommendations
  → excavate (opt)      → excavate core assumptions of a programme
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

## Install

```bash
# Install all skills
npx skills add KKenny0/loom-skills -a claude-code -g -y

# Install a single skill
npx skills add KKenny0/loom-skills --skill deep-read -a claude-code -g -y
```

For local development, copy `deep-read`, `survey`, `excavate`, `debate`, `forge`, and `loom-maintain` directories into your skills directory.

## Quick Start

Prerequisite: [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed.

Minimal usage — read a paper:

```bash
/deep-read https://arxiv.org/abs/xxxx.xxxxx
```

Multi-source + thinking lens combo:

```bash
/deep-read paper1.pdf paper2.pdf paper3.pdf
→ /excavate    # dig hidden assumptions
→ /debate      # dialectical analysis of conflicts
→ /forge       # cross-domain concept forging
```

No vault needed. All outputs appear directly in the conversation.

<details>
<summary>Developer reference: Vault Contract & Validation</summary>

## Vault Contract

- Raw Capture, Source Brief, Synthesis Pack, Research Article, and Topic Note are separate artifacts. They cannot overwrite each other.
- Every Material List `raw_path` points to a real source, local file, original URL, or explicit placeholder.
- Research Articles may use personal voice, but must not rewrite upstream evidence.
- Topic Notes use a calm vault voice, not article rhetoric or platform tone.
- Scanning, validation, and indexing live in `shared/scripts` and default to dry-run or read-only.

## Validate

```bash
for d in deep-read loom-maintain survey excavate debate forge; do
  python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$PWD/$d"
done
```

```bash
python3 shared/scripts/scan_vault.py <vault-path>
python3 shared/scripts/validate_vault.py <vault-path>
python3 shared/scripts/build_indexes.py <vault-path>
```

</details>

## Directory Structure

```text
loom-skills/
├── deep-read/
│   └── references/
│       ├── reading-variants.md   # reading methodology variants
│       └── schemas.md
├── survey/
│   ├── Workflows/
│   │   ├── 01-scout.md
│   │   ├── 02-map.md
│   │   └── 03-compose.md
│   └── references/
│       └── schemas.md
├── excavate/
│   └── references/
│       └── schemas.md
├── debate/
│   └── references/
│       └── schemas.md
├── forge/
│   └── references/
│       └── schemas.md
├── loom-maintain/
│   ├── scripts/
│   └── references/
│       └── schemas.md
└── shared/
    ├── references/
    │   ├── schemas.md             # canonical artifact schemas
    │   └── writing-pipeline.md    # pipeline + lens composition reference
    └── scripts/
        ├── scan_vault.py
        ├── validate_vault.py
        ├── vault_utils.py
        └── build_indexes.py
```

## Acknowledgments

Loom's analysis and writing patterns build on ideas from:

- [ljg-skills](https://github.com/lijigang/ljg-skills) — deep reading, concept anatomy, domain decomposition, multi-perspective debate, critical writing, clarity checks
- [baoyu-skills](https://github.com/JimLiu/baoyu-skills) — content detection, markdown formatting
- [Karpathy's LLM knowledge base workflow](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — vault structure inspiration

## License

MIT
