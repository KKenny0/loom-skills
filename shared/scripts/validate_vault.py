#!/usr/bin/env python3
"""Validate Loom vault structure and common consistency issues."""

from __future__ import annotations

import argparse
from pathlib import Path

from vault_utils import classify_note, iter_markdown, markdown_links, read_note, resolve_link


VALID_STATUSES = {"inbox", "working", "reviewed", "done", "published", "archived", ""}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vault_root", type=Path)
    args = parser.parse_args()

    root = args.vault_root.expanduser().resolve()
    if not root.exists():
        raise SystemExit(f"Vault root does not exist: {root}")

    errors: list[str] = []
    warnings: list[str] = []

    if not (root / "01_Daily_Notes").exists():
        errors.append("Missing required directory: 01_Daily_Notes")
    if not (root / "02_Topic_Notes").exists():
        errors.append("Missing required directory: 02_Topic_Notes")
    if not (root / "00_Index").exists():
        warnings.append("Missing optional initialized index directory: 00_Index")

    for path in iter_markdown(root):
        note = read_note(path, root)
        kind = classify_note(path)
        if kind in {"daily", "topic"} and not note.has_frontmatter:
            warnings.append(f"Missing frontmatter: {note.rel_path}")
        if kind == "daily" and note.status not in VALID_STATUSES:
            warnings.append(f"Unknown status `{note.status}`: {note.rel_path}")
        for link in markdown_links(note.text):
            if link.startswith(("http://", "https://", "mailto:")):
                continue
            if resolve_link(root, path, link) is None:
                warnings.append(f"Unresolved markdown/wiki link `{link}` in {note.rel_path}")

    print("# Loom Vault Validation")
    print()
    print(f"Vault: `{root}`")
    print()
    if errors:
        print("## Errors")
        for item in errors:
            print(f"- {item}")
        print()
    else:
        print("## Errors")
        print("- none")
        print()
    if warnings:
        print("## Warnings")
        for item in warnings:
            print(f"- {item}")
    else:
        print("## Warnings")
        print("- none")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
