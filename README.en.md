<p align="center">
  <img src="assets/loom-logo-transparent.png" alt="Loom logo" width="180">
</p>

<h1 align="center">Loom</h1>

<p align="center">Weave scattered research threads into traceable, evolving knowledge.</p>

<p align="center">
  <a href="README.md">中文</a>
</p>

## Why

Loom is a Claude Code / Codex skill pack for personal knowledge vaults. It treats AI-assisted research as a staged pipeline rather than a one-shot chat: sources become threads, the workflow is the loom, and the vault is the fabric.

AI can summarize quickly and draft fluent prose. Without stages, schemas, and write boundaries, research drifts: sources blur into opinions, drafts overwrite evidence, indexes depend on memory, and older claims become hard to trace.

Loom keeps the work structured. It inventories material, captures source content, reads deeply, synthesizes across sources, drafts prose, consolidates Topic Notes, maintains indexes, discovers cross-topic links, and reports knowledge evolution.

The tool identity sits alongside the existing workflow tools: [Taku](https://github.com/KKenny0/Taku) builds with intent, [Lode](https://github.com/KKenny0/Lode) remembers what matters, and Loom weaves research into knowledge.

## Skills

Each skill is a standalone directory with `SKILL.md` and `agents/openai.yaml`. Trigger one skill directly, or use a flow skill to give the agent an explicit chain.

| Skill | When to use | Output or action |
| --- | --- | --- |
| `loom` | The request is broad or ambiguous | Routes to the right Loom skill |
| `loom-intake` | You have URLs, files, topics, or pasted source material | Material List |
| `loom-capture` | Source material needs to land in the vault | Raw Capture + inbox Daily Note |
| `loom-read` | One source needs deep reading | Source Brief |
| `loom-synthesis-pack` | Multiple sources need synthesis | Synthesis Pack |
| `loom-draft` | Research is ready for prose | Draft / Final |
| `loom-topic` | Trusted research should become long-lived knowledge | Topic Note |
| `loom-index` | Vault content changed | `00_Index` |
| `loom-connect` | Cross-topic links should be discovered or maintained | `CONNECTION_INDEX` |
| `loom-evolve` | You need monthly, quarterly, or annual knowledge evolution | Evolution Summary |
| `loom-migrate` | A legacy Markdown vault needs migration planning | migration report / dry-run |
| `loom-validate` | The vault needs a health check | validation report |
| `loom-research-flow` | Research only, no article draft | intake -> capture -> read -> synthesis-pack |
| `loom-article-flow` | Source material should become an article draft | intake -> capture -> read -> synthesis-pack -> draft |
| `loom-topic-flow` | Trusted research or articles should return to the vault | topic -> index |
| `loom-maintenance-flow` | Vault governance is needed | validate -> migrate scan -> index preview |
| `loom-evolution-flow` | An evolution report needs fresh indexes or links | validate -> index -> connect -> evolve |

## Chaining Skills

Loom skills do not auto-trigger each other. Flow skills define the intended order, but each stage must still read its inputs, produce its own artifact, and respect write boundaries.

Common workflows:

- Research materials: `loom-intake` -> `loom-capture` -> `loom-read` -> `loom-synthesis-pack`
- Research to prose: `loom-intake` -> `loom-capture` -> `loom-read` -> `loom-synthesis-pack` -> `loom-draft`
- Consolidate knowledge: `loom-topic` -> `loom-index`
- Vault maintenance: `loom-validate` -> `loom-migrate scan` -> `loom-index dry-run / rebuild`
- Evolution report: `loom-validate` -> `loom-index` -> `loom-connect` -> `loom-evolve`

Each arrow is a manual user decision. Loom does not generate Topic Notes from unreviewed Drafts by default; if a trusted Synthesis Pack already exists, start directly at `loom-draft` or `loom-topic`.

## Vault Contract

- Raw Capture, Daily Note, Source Brief, Synthesis Pack, Topic Note, Draft, and Final are separate artifacts.
- Every Material List `raw_path` points to a real source, local file, original URL, or explicit placeholder.
- Draft and Final may use personal voice, but must not rewrite upstream evidence.
- Topic Notes use a calm vault voice, not article rhetoric or platform tone.
- Scanning, validation, and index work live in `shared/scripts` and default to dry-run or read-only behavior.
- Migration, index rebuilds, and connection updates require explicit write intent.

## Install

Install companion skills first:

```bash
npx skills add jimliu/baoyu-skills
npx skills add lijigang/ljg-skills#md -g --all
```

Then install Loom. The recommended repository slug is `loom-skills`:

```bash
npx skills add KKenny0/loom-skills
```

For local development, copy the needed `loom-*` directories into your skills directory. Each directory is standalone.

## Validate

```bash
for d in loom loom-intake loom-capture loom-read loom-synthesis-pack \
         loom-draft loom-topic loom-index loom-connect loom-evolve \
         loom-migrate loom-validate loom-research-flow loom-article-flow \
         loom-topic-flow loom-maintenance-flow loom-evolution-flow; do
  python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$PWD/$d"
done
```

```bash
python3 shared/scripts/scan_vault.py <vault-path>
python3 shared/scripts/validate_vault.py <vault-path>
python3 shared/scripts/build_indexes.py <vault-path>
```

## Compatibility

Loom hard-cuts the old `ai-wiki-*` names. Install and invoke the `loom-*` skills directly.

Companion skills provide general capabilities such as URL-to-Markdown conversion, YouTube transcripts, paper reading, article handling, and content cards. Loom owns the workflow boundary: artifact schemas, vault paths, index maintenance, migration, validation, and lifecycle rules.

## Background

Recommended repository layout:

```text
loom-skills/
├── loom/
├── loom-intake/
├── loom-capture/
├── loom-read/
├── loom-synthesis-pack/
├── loom-draft/
├── loom-topic/
├── loom-index/
├── loom-connect/
├── loom-evolve/
├── loom-migrate/
├── loom-validate/
├── loom-*-flow/
└── shared/
```

Loom is for long-lived knowledge vaults, not a content packaging toolbox. Visual assets, publishing, and social rewrites can belong to companion skills; Loom cares about how research is preserved, verified, synthesized, consolidated, and evolved.

## License

MIT
