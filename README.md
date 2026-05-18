<p align="center">
  <img src="assets/loom-logo-transparent.png" alt="Loom logo" width="180">
</p>

<h1 align="center">Loom</h1>

<p align="center">把散落的研究线头，织成可追溯的知识布匹。</p>

<p align="center">
  <a href="README.en.md">English</a>
</p>

## Why

Loom（织）是一组面向 Claude Code 的个人知识库 skills。它不把 AI 研究当成一次性问答，而是把 URL、PDF、视频、论文、摘录和旧文章放进一条有边界的织机：来源是线，流程是织机，知识库是最终织出的布。

AI 很擅长快速读材料，也很擅长写一段看起来完整的文字。问题是，如果没有阶段、schema 和写入边界，研究很快会变成一团难以追溯的线：来源混在观点里，草稿污染原始材料，索引靠记忆维护，几个月后已经不知道某个判断从哪里来。

Loom 做的事情很朴素：先登记材料，再保存来源，再精读压缩，再综合成包，再写作、沉淀 Topic、维护索引、发现连接、观察演进。每一步都留下明确产物，每个产物都有自己的位置和责任。

它和已有工具形成一组工作流隐喻：[Taku](https://github.com/KKenny0/Taku)（琢）build with intent，[Lode](https://github.com/KKenny0/Lode)（矿脉）remember what matters，Loom（织）weave research into knowledge.

## Skills

4 个 skill，每个都是独立目录，包含 `SKILL.md` 和 `agents/openai.yaml`。

| Skill | 何时使用 | 产物或动作 |
| --- | --- | --- |
| `loom` | 不确定该走哪个流程，或需要创建 Material List | 路由 + Material List |
| `loom-research` | 研究材料：从 URL/文件/文本到 Synthesis Pack | Raw Capture + Daily Note + Source Brief + Synthesis Pack |
| `loom-write` | 从研究到文章到知识沉淀 | Draft/Final + Topic Note + Index 更新 |
| `loom-maintain` | Vault 治理：验证、迁移、连接发现、演进报告、索引重建 | Validation report / migration / CONNECTION_INDEX / Evolution Summary |

## Chaining

- **研究到成文**：`loom`（intake）→ `loom-research`（capture + read + synthesis）→ `loom-write`（draft + topic + index）
- **只做研究**：`loom` → `loom-research`
- **从已有研究写文章**：`loom-write`
- **Vault 治理**：`loom-maintain`

## Vault Contract

- Raw Capture、Daily Note、Source Brief、Synthesis Pack、Topic Note、Draft / Final 不能互相覆盖。
- Material List 的 `raw_path` 必须指向真实来源、本地文件、原始 URL 或明确占位标记。
- Draft / Final 可以有个人表达，但不能反向改写上游材料。
- Topic Note 使用冷静知识库语气，不继承文章标题、平台语气或营销修辞。
- 索引、扫描和校验由 `shared/scripts` 执行，默认 dry-run 或只读。

## Install

```bash
npx skills add KKenny0/loom-skills
```

本地开发时，也可以直接把 `loom`、`loom-research`、`loom-write`、`loom-maintain` 目录复制到 skills 目录。

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
├── loom-write/
├── loom-maintain/
└── shared/
    ├── references/
    │   ├── schemas.md          # all artifact schemas
    │   └── writing-pipeline.md # pipeline reference
    └── scripts/
```

Loom 是给长期知识库用的，不是内容包装工具箱。它不依赖外部 companion skill packs——所有核心阅读、分析和写作 patterns 已经内嵌到 `loom-research` 和 `loom-write` 中。

## License

MIT
