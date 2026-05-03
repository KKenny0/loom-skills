---
name: loom-maintenance-flow
description: Run Loom vault maintenance by validating, scanning migration issues, and previewing or rebuilding indexes. Use when the user asks to maintain, audit, clean up, migrate-check, validate, or refresh a Loom vault.
---

# Loom Maintenance Flow

Run operational maintenance.

## Pipeline

1. `loom-validate`
2. `loom-migrate` scan
3. `loom-index` dry-run or rebuild

## Read First

- `../shared/references/vault-migration.md`
- `../shared/references/schema.md`

## Outputs

- Validation report.
- Migration report.
- Index preview or rebuilt `00_Index` when requested.

## Rules

- Default is read-only.
- Write indexes only when explicitly requested.
- Do not normalize frontmatter or migrate files unless the user asks for an apply step.
