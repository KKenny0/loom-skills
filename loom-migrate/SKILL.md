---
name: loom-migrate
description: Scan and migrate a legacy Markdown writing vault into the Loom schema. Use when the user asks to inspect, report on, dry-run, normalize, or migrate an existing Loom vault while preserving content and frontmatter.
---

# Loom Migrate

Plan and apply legacy vault migration.

## Read First

- `../shared/references/vault-migration.md`
- `../shared/references/schema.md`

## Inputs

- Legacy vault root. Default sample: `/Users/kennywu/Documents/knowledge-vaults/loom-vault`.

## Outputs

- Migration report.
- Dry-run patch plan.
- Explicit migration writes only when requested.

## Scripts

- Scan: `python3 ../shared/scripts/scan_vault.py <vault-root>`
- Validate: `python3 ../shared/scripts/validate_vault.py <vault-root>`
- Index preview: `python3 ../shared/scripts/build_indexes.py <vault-root>`

## Rules

- Default is read-only.
- Preserve content and unknown frontmatter.
- Prefer additive changes.
- Do not move assets unless explicitly requested.
