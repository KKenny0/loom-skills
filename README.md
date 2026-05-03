<p align="center">
  <img src="assets/loom-logo-transparent.png" alt="Loom logo" width="180">
</p>

<h1 align="center">Loom</h1>

<p align="center">把散落的研究线头，织成可追溯的知识布匹。</p>

<p align="center">
  <a href="README.en.md">English</a>
</p>

## Why

Loom（织）是一组面向 Claude Code / Codex 的个人知识库 skills。它不把 AI 研究当成一次性问答，而是把 URL、PDF、视频、论文、摘录和旧文章放进一条有边界的织机：来源是线，流程是织机，知识库是最终织出的布。

AI 很擅长快速读材料，也很擅长写一段看起来完整的文字。问题是，如果没有阶段、schema 和写入边界，研究很快会变成一团难以追溯的线：来源混在观点里，草稿污染原始材料，索引靠记忆维护，几个月后已经不知道某个判断从哪里来。

Loom 做的事情很朴素：先登记材料，再保存来源，再精读压缩，再综合成包，再写作、沉淀 Topic、维护索引、发现连接、观察演进。每一步都留下明确产物，每个产物都有自己的位置和责任。

它和已有工具形成一组工作流隐喻：[Taku](https://github.com/KKenny0/Taku)（琢）build with intent，[Lode](https://github.com/KKenny0/Lode)（矿脉）remember what matters，Loom（织）weave research into knowledge.

## Skills

每个 skill 都是独立目录，包含 `SKILL.md` 和 `agents/openai.yaml`。可以单独触发，也可以手动按 flow 串联。

| Skill | 何时使用 | 产物或动作 |
| --- | --- | --- |
| `loom` | 不确定该走哪个阶段 | 路由到合适的 Loom skill |
| `loom-intake` | 刚拿到一批 URL、文件、主题或粘贴材料 | Material List |
| `loom-capture` | 材料需要落到 vault | Raw Capture + inbox Daily Note |
| `loom-read` | 需要精读单篇材料 | Source Brief |
| `loom-synthesis-pack` | 多篇材料读完，需要综合 | Synthesis Pack |
| `loom-draft` | 研究充分，需要成文 | Draft / Final |
| `loom-topic` | 文章或研究需要沉淀为长期知识 | Topic Note |
| `loom-index` | vault 内容变化，需要维护索引 | `00_Index` |
| `loom-connect` | 想发现跨主题关系 | `CONNECTION_INDEX` |
| `loom-evolve` | 想看知识随时间如何演进 | Evolution Summary |
| `loom-migrate` | 有旧 Markdown vault 需要迁入 | migration report / dry-run |
| `loom-validate` | 需要检查 vault 健康度 | validation report |
| `loom-research-flow` | 只做研究，暂时不写文章 | intake -> capture -> read -> synthesis-pack |
| `loom-article-flow` | 从材料一路研究到文章草稿 | intake -> capture -> read -> synthesis-pack -> draft |
| `loom-topic-flow` | 把可信研究或文章沉淀回知识库 | topic -> index |
| `loom-maintenance-flow` | 做 vault 治理 | validate -> migrate scan -> index preview |
| `loom-evolution-flow` | 做阶段性知识演进报告 | validate -> index -> connect -> evolve |

## Chaining Skills

Loom 的 skills 不会自动互相触发。flow skill 只是给 agent 一个明确的执行顺序，真正执行时仍然要按阶段读取输入、产出文件、确认写入边界。

常用链路：

- 研究材料：`loom-intake` -> `loom-capture` -> `loom-read` -> `loom-synthesis-pack`
- 研究到成文：`loom-intake` -> `loom-capture` -> `loom-read` -> `loom-synthesis-pack` -> `loom-draft`
- 沉淀知识：`loom-topic` -> `loom-index`
- Vault 治理：`loom-validate` -> `loom-migrate scan` -> `loom-index dry-run / rebuild`
- 演进报告：`loom-validate` -> `loom-index` -> `loom-connect` -> `loom-evolve`

每个箭头都代表一次手动决策。Loom 默认不从未 review 的 Draft 生成 Topic Note；如果已经有可信的 Synthesis Pack，可以直接从 `loom-draft` 或 `loom-topic` 开始。

## Vault Contract

- Raw Capture、Daily Note、Source Brief、Synthesis Pack、Topic Note、Draft / Final 不能互相覆盖。
- Material List 的 `raw_path` 必须指向真实来源、本地文件、原始 URL 或明确占位标记。
- Draft / Final 可以有个人表达，但不能反向改写上游材料。
- Topic Note 使用冷静知识库语气，不继承文章标题、平台语气或营销修辞。
- 索引、扫描和校验由 `shared/scripts` 执行，默认 dry-run 或只读。
- migration、index rebuild、connection update 需要用户明确要求才写入。

## Install

先安装 companion skills：

```bash
npx skills add jimliu/baoyu-skills
npx skills add lijigang/ljg-skills#md -g --all
```

然后安装 Loom。仓库推荐命名为 `loom-skills`：

```bash
npx skills add KKenny0/loom-skills
```

本地开发时，也可以直接把需要的 `loom-*` 目录复制到 skills 目录。每个目录都是一个独立 skill。

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

The companion skills provide general capabilities such as URL-to-Markdown conversion, YouTube transcripts, paper reading, article handling, and content cards. Loom owns the workflow boundary: artifact schemas, vault paths, index maintenance, migration, validation, and lifecycle rules.

## Background

推荐仓库布局：

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

Loom 是给长期知识库用的，不是内容包装工具箱。视觉资产、平台发布、社媒改写可以由 companion skills 承担；Loom 只关心研究如何被保存、验证、综合、沉淀和演进。

## License

MIT
