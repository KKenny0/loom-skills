---
name: loom-validate
description: Validate a Loom vault for schema, frontmatter, paths, links, index consistency, and legacy compatibility. Use when the user asks to check, audit, validate, lint, or inspect a Loom vault without changing it.
---

# Loom Validate

Run read-only vault validation.

## Read First

- `../shared/references/schema.md`
- `../shared/references/vault-migration.md`

## Input

- Vault root.

## Output

- Validation report with errors and warnings.

## Scripts

- `python3 ../shared/scripts/validate_vault.py <vault-root>`
- Optional inventory: `python3 ../shared/scripts/scan_vault.py <vault-root>`

## Rules

- Never write files.
- Separate blocking errors from migration warnings.
- Treat legacy compatibility warnings as migration candidates, not failures.
