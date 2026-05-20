<p align="center">
  <img src="assets/loom-logo-transparent.png" alt="Loom logo" width="180">
</p>

<h1 align="center">Loom</h1>

<p align="center">把散落的来源，织成能看出"哪里站得住、哪里站不住"的研究。</p>

<p align="center">
  <a href="README.md">English</a>
</p>

## Why

让 AI 聊天机器人研究一个主题写篇文章——它会给你一个流畅、自信的答案。但真正的研究不流畅。来源之间有分歧，证据质量参差不齐，有些判断下面只是薄薄一层冰。AI 把它知道的东西平均了一下。分歧被抹平，弱主张听起来和强证据一样笃定。你得到一篇读起来很顺的文章，却看不出哪里地基是实的、哪里是虚的。

Loom 的做法不同。它读的是你给的来源，不是训练数据。它原样捕获、独立分析、再跨源综合——但不抹平冲突。它告诉你来源之间共识在哪、分歧在哪、哪些判断只靠弱证据撑着。

结果：一篇扎根于你来源的研究文章，附带一份证据地图——让你一眼看清哪里是共识、哪里有争议、哪里还没被充分验证。三个月后回头看，每个判断仍然能追溯到出处。

持续使用，研究会复利增长。Topic Notes 跨项目连接，索引自动建立。你积累的不是聊天记录，而是一块耐久的知识织物——不会丢失，永远可追溯。

Loom（织）weave research into knowledge.

## 什么时候不用 Loom

Loom 不适合这些场景：
- **一次性快速查询。** 贴到聊天前端——更快更省。
- **不需要溯源的内容。** SEO 文章、社媒更新、通用科普——Loom 的 overhead 不值得。
- **量产写作。** 如果你一天要出五篇，这不是你的工具。

Loom 适用于研究结果有后果的场景：技术决策、分析报告、文献综述，或者任何"搞错了代价比 token 大"的事。

## 谁适合用 Loom

- **技术负责人** 做架构或工具选型决策。
- **分析师和记者** 处理文档、报告或专家观点。
- **研究者** 做跨论文和预印本的文献综述。
- **认真的自学者** 想搞懂一个领域的完整版图，而不只是最流行的说法。

如果你的决策取决于"真正已知的是什么"而不仅仅是"大家常说的是什么"——Loom 适合你。

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
