#!/usr/bin/env python3
"""Preview or build Loom index files from existing Topic Notes."""

from __future__ import annotations

import argparse
from collections import defaultdict
from datetime import date
from pathlib import Path

from vault_utils import (
    category_from_topic_path,
    classify_note,
    first_wiki_links,
    iter_markdown,
    read_note,
    resolve_link,
)


def topic_row(note, root: Path) -> dict[str, str]:
    category = note.frontmatter.get("category") if note.frontmatter else ""
    if not isinstance(category, str) or not category:
        category = category_from_topic_path(note.path)
    mode = note.frontmatter.get("mode") if note.frontmatter else ""
    if not isinstance(mode, str) or not mode:
        links = first_wiki_links(note.body)
        mode = "link-only" if links and len(note.body.strip().splitlines()) <= 3 else "synthesis"
    links = first_wiki_links(note.body)
    linked_note = None
    if links:
        resolved = resolve_link(root, note.path, links[0])
        if resolved and resolved.suffix == ".md":
            linked_note = read_note(resolved, root)
    title = note.title
    if not note.has_frontmatter and linked_note:
        title = linked_note.title
    tags = ", ".join(note.tags or (linked_note.tags if linked_note else []))
    core = ""
    if "summary:" in note.text and "core_idea:" in note.text:
        for line in note.text.splitlines():
            stripped = line.strip()
            if stripped.startswith("core_idea:"):
                core = stripped.split(":", 1)[1].strip().strip('"')
                break
    if not core and mode == "link-only":
        core = f"Links to {links[0]}" if links else "Link-only topic entry"
    return {
        "title": title,
        "category": category,
        "mode": mode,
        "file": note.rel_path,
        "core": core,
        "tags": tags,
        "date": note.date,
    }


def render_topic_index(rows: list[dict[str, str]]) -> str:
    today = date.today().isoformat()
    lines = [
        "# Topic Index",
        "",
        f"> Auto-generated. Last updated: {today}",
        "",
        "| Title | Category | Mode | File | Core Idea | Tags | Date |",
        "|-------|----------|------|------|-----------|------|------|",
    ]
    for row in rows:
        lines.append(
            f"| [[{row['title']}]] | {row['category']} | {row['mode']} | {row['file']} | {row['core']} | {row['tags']} | {row['date']} |"
        )
    return "\n".join(lines) + "\n"


def render_timeline(rows: list[dict[str, str]]) -> str:
    today = date.today().isoformat()
    months: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        month = row["date"][:7] if row["date"] else today[:7]
        months[month].append(row)
    lines = ["# Timeline Index", "", f"> Auto-generated. Last updated: {today}", ""]
    for month in sorted(months, reverse=True):
        lines.append(f"## {month}")
        lines.append("### New Topics")
        for row in sorted(months[month], key=lambda item: item["date"], reverse=True):
            entry_date = row["date"] or today
            lines.append(f"- [[{row['title']}]] ({entry_date}) - {row['category']}")
        lines.extend(["", "### Updated Topics", "", "### Archived", ""])
    return "\n".join(lines).rstrip() + "\n"


def render_connections() -> str:
    today = date.today().isoformat()
    return "\n".join(["# Connection Index", "", f"> Auto-generated. Last updated: {today}", ""]) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vault_root", type=Path)
    parser.add_argument("--write", action="store_true", help="write 00_Index files")
    args = parser.parse_args()

    root = args.vault_root.expanduser().resolve()
    if not root.exists():
        raise SystemExit(f"Vault root does not exist: {root}")

    topic_notes = [
        read_note(path, root)
        for path in iter_markdown(root)
        if classify_note(path) == "topic"
    ]
    rows = [topic_row(note, root) for note in topic_notes]
    topic_index = render_topic_index(rows)
    timeline_index = render_timeline(rows)
    connection_index = render_connections()

    if args.write:
        index_dir = root / "00_Index"
        index_dir.mkdir(parents=True, exist_ok=True)
        (index_dir / "TOPIC_INDEX.md").write_text(topic_index, encoding="utf-8")
        (index_dir / "TIMELINE_INDEX.md").write_text(timeline_index, encoding="utf-8")
        connection_path = index_dir / "CONNECTION_INDEX.md"
        if not connection_path.exists():
            connection_path.write_text(connection_index, encoding="utf-8")
        print(f"Wrote indexes to {index_dir}")
    else:
        print("# Dry Run: TOPIC_INDEX.md")
        print(topic_index)
        print("# Dry Run: TIMELINE_INDEX.md")
        print(timeline_index)
        print("# Dry Run: CONNECTION_INDEX.md")
        print(connection_index)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
