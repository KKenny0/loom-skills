# Vault Migration Workflow

Use this reference when scanning or migrating a legacy Markdown writing vault into the Loom schema.

## Default Behavior

Migration starts read-only. Generate a report before changing files.

Run:

```bash
python3 shared/scripts/scan_vault.py <vault-root>
```

Report:

- Directory presence: `00_Index`, `01_Daily_Notes`, `02_Topic_Notes`, `03_Content_Output`.
- Daily Note count by year and status directory.
- Topic Note count by category.
- Assets count and likely asset directories.
- Files missing YAML frontmatter.
- Status values found.
- Topic Notes that are link-only transclusions.
- Broken or unresolved local markdown links and Obsidian transclusions.
- Whether index files exist.

## Migration Plan

After scanning, propose a staged plan:

1. Initialize indexes without modifying notes.
2. Add missing frontmatter to high-confidence files.
3. Normalize status values only if requested.
4. Convert selected link-only Topic Notes into synthesis notes.
5. Validate links and index consistency.

## Apply Rules

Only apply migration when the user explicitly says to write or apply changes.

Before writing, summarize:

- Files to create.
- Files to update.
- Fields to add.
- Files intentionally left unchanged.

During migration:

- Do not delete content.
- Do not reorder frontmatter unless rewriting the whole file was requested.
- Do not move assets unless requested.
- Keep original Topic Notes if generating synthesis replacements unless the user asks to overwrite them.
- Prefer adding `00_Index` first, because it is reversible and low-risk.

## Loom Vault Notes

The sample vault at `/Users/kennywu/Documents/knowledge-vaults/loom-vault` currently behaves like a writing vault:

- `01_Daily_Notes/2026/inbox`
- `01_Daily_Notes/2026/published`
- `01_Daily_Notes/assets`
- `02_Topic_Notes/<Category>`

It may not yet contain `00_Index` or `03_Content_Output`. Treat this as expected before migration.
