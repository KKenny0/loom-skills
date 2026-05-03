#!/usr/bin/env python3
"""Read-only inventory and migration report for a Loom vault."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from pathlib import Path

from vault_utils import classify_note, first_wiki_links, iter_markdown, read_note


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vault_root", type=Path)
    args = parser.parse_args()

    root = args.vault_root.expanduser().resolve()
    if not root.exists():
        raise SystemExit(f"Vault root does not exist: {root}")

    md_paths = iter_markdown(root)
    notes = [read_note(path, root) for path in md_paths]

    by_kind = Counter(classify_note(path) for path in md_paths)
    status_counts = Counter(note.status or "(missing)" for note in notes if classify_note(note.path) == "daily")
    missing_fm = [note.rel_path for note in notes if classify_note(note.path) in {"daily", "topic"} and not note.has_frontmatter]
    topic_modes = Counter()
    link_only_topics = []

    daily_by_dir = Counter()
    topic_by_category = Counter()
    for note in notes:
        kind = classify_note(note.path)
        if kind == "daily":
            parts = note.path.relative_to(root).parts
            key = "/".join(parts[:3]) if len(parts) >= 3 else note.rel_path
            daily_by_dir[key] += 1
        elif kind == "topic":
            parts = note.path.relative_to(root).parts
            category = parts[1] if len(parts) > 1 else "(uncategorized)"
            topic_by_category[category] += 1
            mode = note.frontmatter.get("mode") if note.frontmatter else ""
            links = first_wiki_links(note.body)
            if not mode and links and len(note.body.strip().splitlines()) <= 3:
                topic_modes["link-only-inferred"] += 1
                link_only_topics.append(note.rel_path)
            elif isinstance(mode, str) and mode:
                topic_modes[mode] += 1
            else:
                topic_modes["unknown"] += 1

    asset_files = []
    assets_root = root / "01_Daily_Notes" / "assets"
    if assets_root.exists():
        asset_files = [p for p in assets_root.rglob("*") if p.is_file()]

    print("# Loom Vault Scan Report")
    print()
    print(f"Vault: `{root}`")
    print()
    print("## Structure")
    for dirname in ("00_Index", "01_Daily_Notes", "02_Topic_Notes", "03_Content_Output"):
        exists = "yes" if (root / dirname).exists() else "no"
        print(f"- `{dirname}`: {exists}")
    print()
    print("## Counts")
    print(f"- Markdown files: {len(md_paths)}")
    print(f"- Daily Notes: {by_kind['daily']}")
    print(f"- Topic Notes: {by_kind['topic']}")
    print(f"- Index files: {by_kind['index']}")
    print(f"- Output files: {by_kind['output']}")
    print(f"- Asset files: {len(asset_files)}")
    print()
    print("## Daily Notes By Directory")
    for key, count in sorted(daily_by_dir.items()):
        print(f"- `{key}`: {count}")
    print()
    print("## Topic Notes By Category")
    for key, count in sorted(topic_by_category.items()):
        print(f"- `{key}`: {count}")
    print()
    print("## Status Values")
    for status, count in sorted(status_counts.items()):
        print(f"- `{status}`: {count}")
    print()
    print("## Topic Modes")
    for mode, count in sorted(topic_modes.items()):
        print(f"- `{mode}`: {count}")
    print()
    print("## Files Missing Frontmatter")
    if missing_fm:
        for rel in missing_fm:
            print(f"- `{rel}`")
    else:
        print("- none")
    print()
    print("## Link-Only Topic Notes")
    if link_only_topics:
        for rel in link_only_topics:
            print(f"- `{rel}`")
    else:
        print("- none")
    print()
    print("## Recommended Next Steps")
    if not (root / "00_Index").exists():
        print("- Initialize indexes with `shared/scripts/build_indexes.py <vault-root> --write` after reviewing a dry run.")
    if missing_fm:
        print("- Add frontmatter to high-confidence files before strict validation.")
    if link_only_topics:
        print("- Keep link-only Topic Notes as-is or selectively upgrade important topics to synthesis mode.")
    if not missing_fm and (root / "00_Index").exists():
        print("- Run `shared/scripts/validate_vault.py <vault-root>` for consistency checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
