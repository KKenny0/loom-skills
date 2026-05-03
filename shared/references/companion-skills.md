# Required Companion Skills

The Loom skill pack assumes these companion skill packs are installed.

## Install

```bash
npx skills add jimliu/baoyu-skills
npx skills add lijigang/ljg-skills#md -g --all
```

If a required skill is missing, stop and show the relevant install command. Do not silently fall back to a weaker workflow.

## Responsibility Split

- **baoyu-skills**: URL/X/YouTube capture, Markdown conversion, formatting, visual assets, HTML, and publishing helpers.
- **ljg-skills**: reading, paper analysis, plain explanation, deep thinking, rank reduction, roundtable synthesis, writing, and cards.
- **loom-skills**: workflow orchestration, schemas, vault paths, index maintenance, migration, validation, and lifecycle boundaries.

## Stage Mapping

| Stage | Required or preferred companion skills |
| --- | --- |
| Intake | none required beyond Loom; use companion only after source type is known |
| Capture | `baoyu-url-to-markdown`, `baoyu-youtube-transcript`, `baoyu-danger-x-to-markdown` |
| Read | `ljg-read`, `ljg-paper`, `ljg-paper-river`, `ljg-plain`, `ljg-learn`, `ljg-think` |
| Synthesis Pack | `ljg-rank`, `ljg-roundtable`, `ljg-think`, `ljg-learn` |
| Draft / Final | `ljg-writes`, `baoyu-format-markdown`, `ljg-plain` |
| Topic | `ljg-rank`, `ljg-think`, `ljg-learn` |
| Connect | `ljg-roundtable`, `ljg-rank` |
| Evolve | `ljg-rank`, `ljg-writes` |

## Danger Skills

`baoyu-danger-*` skills use reverse-engineered or riskier access paths. Use them only when the user explicitly asks for that source type or confirms use.

Do not let flow skills silently call:

- `baoyu-danger-x-to-markdown`
- `baoyu-danger-gemini-web`

## Deferred Extensions

These capabilities are available through companion skills but are not first-round Loom stages:

- visual assets: `baoyu-cover-image`, `baoyu-diagram`, `baoyu-infographic`, `baoyu-image-cards`, `ljg-card`
- publishing: `baoyu-markdown-to-html`, `baoyu-post-to-wechat`, `baoyu-post-to-x`, `baoyu-post-to-weibo`
