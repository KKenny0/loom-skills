# Loom Shared

Canonical source for schemas, references, and scripts shared across the Loom skill suite.

## Layout

```
shared/
├── README.md           # This file
├── references/
│   └── schemas.md      # Canonical vault schema, artifact formats, index formats
└── scripts/
    ├── scan_vault.py     # Vault inventory scanner
    ├── validate_vault.py # Blocking error and migration warning detection
    ├── vault_utils.py    # Shared utilities
    └── build_indexes.py  # INDEX rebuild (TOPIC_INDEX, TIMELINE_INDEX)
```

## Synchronization

Each Loom skill maintains its own copy of the shared files it needs:

| Shared File | loom | loom-research | loom-write | loom-maintain |
|-------------|------|---------------|------------|---------------|
| references/schemas.md | copy | copy | copy | copy |
| references/reading-variants.md | — | copy (canonical) | — | — |
| scripts/*.py | — | — | build_indexes.py | copy (all) |

**Edit here first**, then run the sync script to propagate changes:

```bash
python3 shared/sync.py
```

## Why copies, not symlinks?

Claude Code installs skills by copying individual skill directories. Sibling directories like `shared/` are not installed alongside skills, so `../shared/references/schemas.md` references break at runtime. Each skill must be self-contained.
