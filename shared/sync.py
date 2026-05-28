#!/usr/bin/env python3
"""Sync shared files from shared/ to each Loom skill directory."""

import shutil
from pathlib import Path

SHARED = Path(__file__).resolve().parent
REPO = SHARED.parent

SYNC_MAP = {
    "deep-read": {
        "files": ["references/schemas.md"],
    },
    "loom-maintain": {
        "files": ["references/schemas.md"],
        "scripts": ["scan_vault.py", "validate_vault.py", "vault_utils.py", "build_indexes.py"],
    },
}


def sync():
    for skill, targets in SYNC_MAP.items():
        for f in targets.get("files", []):
            src = SHARED / f
            dst = REPO / skill / f
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            print(f"  {skill}/{f}")

        for s in targets.get("scripts", []):
            src = SHARED / "scripts" / s
            dst_dir = REPO / skill / "scripts"
            dst_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst_dir / s)
            print(f"  {skill}/scripts/{s}")

    print("\nSync complete.")


if __name__ == "__main__":
    sync()
