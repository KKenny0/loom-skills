# Phase 2: Read

精读每个素材，产出结构化笔记（Source Brief）。

## Step 1: 选择阅读方法

根据素材类型，从 `references/reading-variants.md` 中选择对应方法：

| 素材类型 | 方法 | 适用场景 |
|----------|------|----------|
| 文章/散文 | 4-Phase Reading | 有论证结构的叙事文本 |
| 学术论文 | 9-Step Extraction | 同行评审、方法论重 |
| 概念/术语 | 8-Dimension Anatomy | 需要完整拆解的单个概念 |
| 任何需要深度的素材 | Vertical Drilling | 超越表面理解 |

## Step 2: 执行精读

对每个素材执行精读，产出 Source Brief。

### 单素材精读流程

1. **骨/肌/筋分类**：给素材每个段落标注 `[骨]`、`[肌]`、`[筋]`
2. **选择并执行对应方法**：按 reading-variants.md 中的步骤执行
3. **问题节**：核心叙事用亲历→旧路→新口结构整理
4. **质量检查**：过 9 Red Lines

### Source Brief 结构

Source Brief 的完整字段和规则见 [schemas.md](../references/schemas.md) 的 Source Brief section。以下只列操作要点：

- 骨/肌/筋分类：给每个段落标注 `[骨]`、`[肌]` 或 `[筋]`
- 问题节：用亲历→旧路→新口结构整理核心叙事
- 质量检查：过 9 Red Lines（见 [reading-variants.md](../references/reading-variants.md)）

### 多素材并行精读

如果有 3 个以上素材，使用 background agent 并行精读：

给每个 agent 的 prompt 模板：

```
精读以下素材，产出 Source Brief。

素材内容：{素材全文或关键段落}

执行步骤：
1. 骨/肌/筋分类：给每个段落标注 [骨]、[肌] 或 [筋]
2. 选择阅读方法：{根据类型指定方法}
3. 按该方法论执行精读
4. 核心叙事用亲历→旧路→新口结构整理
5. 过 9 Red Lines 质量检查

Source Brief 结构（完整 schema 见 references/schemas.md）：
- source_id, raw_path, brief_date, type
- 核心观点（一句话）
- 骨架段 [骨]（核心论证）
- 证据段 [肌]（支撑数据）
- 问题节（亲历→旧路→新口）
- 关键引述
- 争议与张力（与其他来源的冲突或素材内部的张力）
- 待验证论断
- 不确定处

输出要求：
- 中文
- 每个点 2-3 句话说清楚
- 保留原文关键术语
- 不合并不同素材的内容
```

**关键**：多个 background agent 必须在一次消息中并行启动。

## Step 3: Source Brief 隔离原则

- 一个素材一个 Source Brief，不跨素材合并
- Source Brief 只引用自己的素材，不引入其他素材的论点或框架
- 跨素材分析属于 Phase 3 Synthesize，不属于 Source Brief

## Step 4: 完成 Read 阶段

所有 Source Brief 完成后，进入 [Phase 3: Synthesize](03-synthesize.md)。
