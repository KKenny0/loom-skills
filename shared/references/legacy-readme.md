# Knowledge Compiler — Claude Code Skill

A Claude Code skill that turns any URL, text, or file into structured knowledge notes with automatic indexing. Inspired by [Karpathy's LLM knowledge base workflow](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## What It Does

Knowledge Compiler gives Claude Code two compile operations:

1. **Daily Note Compile** — Feed it a URL, pasted text, or file → get a structured Daily Note with frontmatter, summary, key points, and details.
2. **Topic Note Compile** — Specify source Daily Notes or a topic name → get a synthesized Topic Note with structured summary, detailed explanation, and auto-updated TOPIC_INDEX.

All output follows strict schemas defined in `SCHEMA.md`. No code dependencies — pure Markdown.

## Installation

### Option A: Claude Code Custom Commands (Recommended)

1. Copy this directory to your Claude Code commands location:
   ```bash
   cp -r llm-wiki-skills/ ~/.claude/commands/knowledge-compiler/
   ```

2. In your project's `CLAUDE.md` (or global `~/.claude/CLAUDE.md`), add:
   ```markdown
   ## Knowledge Compiler
   
   When the user asks to compile a URL, article, or text into a knowledge note, read and follow:
   - `~/.claude/commands/knowledge-compiler/SKILL.md`
   - `~/.claude/commands/knowledge-compiler/SCHEMA.md`
   
   Knowledge vault path: /path/to/your/KnowledgeBase-AI/
   ```

### Option B: Project-Level Setup

1. Place `SKILL.md` and `SCHEMA.md` in your project directory (e.g., `docs/knowledge-compiler/`).
2. Reference them in your project's `CLAUDE.md`:
   ```markdown
   ## Knowledge Compiler
   Read and follow `docs/knowledge-compiler/SKILL.md` and `docs/knowledge-compiler/SCHEMA.md` when compiling knowledge.
   ```

### Option C: Direct Usage

Simply tell Claude Code:
> "Read SKILL.md and SCHEMA.md from this directory, then compile this URL: https://..."

## Usage

### Compile a URL into a Daily Note

```
> Compile this URL into a Daily Note: https://example.com/article-about-agents
```

Claude Code will:
1. Fetch and extract the article content
2. Generate a structured Daily Note with frontmatter, summary, key points, and details
3. Save it to `01_Daily_Notes/YYYY/inbox/`

### Compile text into a Daily Note

```
> Compile this text into a Daily Note:
> [paste your text here]
```

### Compile a Topic Note from Daily Notes

```
> Compile a Topic Note about "Multi-Agent Systems" from these Daily Notes:
> - 2026-04-10_multi-agent-patterns.md
> - 2026-04-12_agent-orchestration.md
```

Or let Claude Code find relevant sources:

```
> Create a Topic Note about "Prompt Engineering" — find relevant Daily Notes in my vault
```

Claude Code will:
1. Read source Daily Notes
2. Synthesize into a Topic Note with structured summary
3. Save to `02_Topic_Notes/[Category]/`
4. Auto-update `00_Index/TOPIC_INDEX.md`

## File Structure

```
llm-wiki-skills/
├── SKILL.md      # Main skill instructions (trigger conditions + workflows)
├── SCHEMA.md     # Output templates and behavioral constraints
└── README.md     # This file
```

## Vault Structure

Knowledge Compiler expects (and creates if missing) this vault layout:

```
<vault-root>/
├── 00_Index/
│   └── TOPIC_INDEX.md
├── 01_Daily_Notes/
│   └── YYYY/
│       ├── inbox/
│       ├── working/
│       ├── published/
│       └── archived/
├── 02_Topic_Notes/
│   └── [Category]/
└── 03_Content_Output/
    ├── Longform/
    └── Social_Posts/
```

## Design Principles

- **Zero code dependencies** — Pure Markdown skill files, no Python/TypeScript/JS.
- **Self-contained** — Claude Code reads SKILL.md + SCHEMA.md and knows exactly what to do.
- **Schema-first** — SCHEMA.md defines exact output formats; SKILL.md defines workflows.
- **Idempotent indexing** — Compiling the same topic twice updates, never duplicates.
- **Token-efficient** — TOPIC_INDEX as primary lookup; structured summaries at ~100 tokens/topic.

## Credits

Inspired by Andrej Karpathy's [LLM knowledge base workflow](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## License

MIT
