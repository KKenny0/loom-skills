<p align="center">
  <img src="assets/loom-logo-transparent.png" alt="Loom logo" width="180">
</p>

<h1 align="center">Loom</h1>

<p align="center">把散落的研究线头，织成可追溯的知识布匹。</p>

<p align="center">
  <a href="README.md">English</a>
</p>

## Why

三个月后，你在笔记里翻到一个判断。你还能分清它来自一篇论文、一篇博文、还是你自己的推测吗？

AI 聊天前端很适合快速问答。但它们是短暂的——每次对话都是一座孤岛。如果你跨多次研究同一个领域，洞察散落在不同的聊天记录里，出处逐渐模糊。最后你得到的是一堆看起来合理的文字，却无法追溯。

Loom 为累积性知识库而设计。每份来源原样保存。每条判断可以追溯到出处。每次综合是独立产物，草稿可以读取但绝不能改写。知识库会复利增长：第二个研究主题建立在第一个之上，最终你拥有的是聊天记录无法提供的东西——一个可搜索、可索引、可交叉引用的个人知识织物。

Loom（织）weave research into knowledge.

## 什么时候不用 Loom

一次性快速查询不是 Loom 的场景。如果你只是想搞懂一篇文章或得到一个快速答案，直接用聊天前端——更快更省。

Loom 适用于会复利增长的知识工作。如果你预期会重访一个主题、把它和其他主题连接、或以后基于它写作，这种结构就值得投入。

## Skills

4 个 skill，每个都是独立目录，包含 `SKILL.md` 和 `agents/openai.yaml`。

| Skill | 何时使用 | 产物或动作 |
| --- | --- | --- |
| `loom` | 不确定该走哪个流程，或需要创建 Material List | 路由 + Material List |
| `loom-research` | 研究材料：从 URL/文件/文本到 Synthesis Pack | Raw Capture + Daily Note + Source Brief + Synthesis Pack |
| `loom-write` | 从研究到文章到知识沉淀 | Draft/Final + Topic Note + Index 更新 |
| `loom-maintain` | Vault 治理：验证、迁移、连接发现、演进报告、索引重建 | Validation report / migration / CONNECTION_INDEX / Evolution Summary |

## Quick look

```
Input: three articles on AI agent architecture
  → loom intake         → Material List (3 sources)
  → loom-research       → 3 Raw Captures + 3 Source Briefs + 1 Synthesis Pack
  → loom-write          → Draft article + 2 Topic Notes + Index update
```

<details>
<summary>Synthesis Pack 示例（节选）</summary>

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

- **研究到成文**：`loom`（intake）→ `loom-research`（capture + read + synthesis）→ `loom-write`（draft + topic + index）
- **只做研究**：`loom` → `loom-research`
- **从已有研究写文章**：`loom-write`
- **Vault 治理**：`loom-maintain`

## Install

```bash
npx skills add KKenny0/loom
```

本地开发时，也可以直接把 `loom`、`loom-research`、`loom-write`、`loom-maintain` 目录复制到 skills 目录。

## Vault Contract

- Raw Capture、Daily Note、Source Brief、Synthesis Pack、Topic Note、Draft / Final 不能互相覆盖。
- Material List 的 `raw_path` 必须指向真实来源、本地文件、原始 URL 或明确占位标记。
- Draft / Final 可以有个人表达，但不能反向改写上游材料。
- Topic Note 使用冷静知识库语气，不继承文章标题、平台语气或营销修辞。
- 索引、扫描和校验由 `shared/scripts` 执行，默认 dry-run 或只读。

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

Loom 是给长期知识库用的，不是内容包装工具箱。所有核心阅读、分析和写作 patterns 已经内嵌到 `loom-research` 和 `loom-write` 中——运行时不依赖外部 companion skill packs。

## Acknowledgments

Loom 的分析和写作模式借鉴了以下来源的思想：

- [ljg-skills](https://github.com/lijigang/ljg-skills) — 深度阅读、概念解剖、领域分解、多视角辩论、批判性写作、清晰度检查
- [baoyu-skills](https://github.com/JimLiu/baoyu-skills) — 内容检测、Markdown 格式化
- [Karpathy 的 LLM 知识库工作流](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — 知识库结构灵感

## License

MIT
