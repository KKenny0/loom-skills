#!/usr/bin/env python3
"""Shared helpers for Loom vault scripts."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
WIKI_LINK_RE = re.compile(r"!?\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+\.md(?:#[^)]+)?)\)")


@dataclass
class Note:
    path: Path
    rel_path: str
    text: str
    frontmatter: dict[str, object]
    body: str

    @property
    def has_frontmatter(self) -> bool:
        return bool(self.frontmatter)

    @property
    def title(self) -> str:
        value = self.frontmatter.get("title")
        if isinstance(value, str) and value.strip():
            return strip_quotes(value.strip())
        match = re.search(r"^#\s+(.+)$", self.body, re.MULTILINE)
        if match:
            return match.group(1).strip()
        return self.path.stem

    @property
    def date(self) -> str:
        value = self.frontmatter.get("date")
        if isinstance(value, str) and value.strip():
            return strip_quotes(value.strip()).split()[0]
        match = re.match(r"(\d{4}-\d{2}-\d{2})", self.path.name)
        return match.group(1) if match else ""

    @property
    def status(self) -> str:
        value = self.frontmatter.get("status")
        if isinstance(value, str) and value.strip():
            return strip_quotes(value.strip())
        parts = set(self.path.parts)
        for status in ("inbox", "working", "reviewed", "published", "archived"):
            if status in parts:
                return status
        return ""

    @property
    def tags(self) -> list[str]:
        value = self.frontmatter.get("tags")
        if isinstance(value, list):
            return [str(v).strip() for v in value if str(v).strip()]
        if isinstance(value, str):
            raw = strip_quotes(value.strip())
            if raw.startswith("[") and raw.endswith("]"):
                return [strip_quotes(v.strip()) for v in raw[1:-1].split(",") if v.strip()]
            return [raw] if raw else []
        return []


def strip_quotes(value: str) -> str:
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def read_note(path: Path, vault_root: Path) -> Note:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    frontmatter: dict[str, object] = {}
    body = text
    if match:
        frontmatter = parse_simple_yaml(match.group(1))
        body = text[match.end() :]
    return Note(
        path=path,
        rel_path=path.relative_to(vault_root).as_posix(),
        text=text,
        frontmatter=frontmatter,
        body=body,
    )


def parse_simple_yaml(raw: str) -> dict[str, object]:
    data: dict[str, object] = {}
    current_key: str | None = None
    current_list: list[str] | None = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") and current_key and current_list is not None:
            current_list.append(strip_quotes(line[4:].strip()))
            continue
        if line.startswith("- ") and current_key and current_list is not None:
            current_list.append(strip_quotes(line[2:].strip()))
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        current_key = key
        current_list = None
        if value == "":
            current_list = []
            data[key] = current_list
        elif value.startswith("[") and value.endswith("]"):
            data[key] = [strip_quotes(v.strip()) for v in value[1:-1].split(",") if v.strip()]
        else:
            data[key] = strip_quotes(value)
    return data


def iter_markdown(vault_root: Path) -> list[Path]:
    ignored_parts = {".git"}
    return sorted(
        p
        for p in vault_root.rglob("*.md")
        if not ignored_parts.intersection(p.relative_to(vault_root).parts)
    )


def classify_note(path: Path) -> str:
    parts = path.parts
    if "assets" in parts:
        return "asset"
    if "01_Daily_Notes" in parts:
        return "daily"
    if "02_Topic_Notes" in parts:
        return "topic"
    if "00_Index" in parts:
        return "index"
    if "03_Content_Output" in parts:
        return "output"
    return "other"


def category_from_topic_path(path: Path) -> str:
    parts = list(path.parts)
    if "02_Topic_Notes" not in parts:
        return ""
    idx = parts.index("02_Topic_Notes")
    if idx + 1 < len(parts):
        return parts[idx + 1]
    return ""


def first_wiki_links(text: str) -> list[str]:
    return [m.group(1).strip() for m in WIKI_LINK_RE.finditer(text)]


def markdown_links(text: str) -> list[str]:
    links = [m.group(1).split("#", 1)[0] for m in MD_LINK_RE.finditer(text)]
    links.extend(
        link
        for link in first_wiki_links(text)
        if "/" in link or "." in Path(link).name
    )
    return links


def resolve_link(vault_root: Path, source_path: Path, target: str) -> Path | None:
    target = target.strip()
    if not target or target.startswith(("http://", "https://", "mailto:")):
        return None
    candidates = []
    raw = target
    if Path(raw).suffix == "":
        raw = f"{raw}.md"
    raw_path = Path(raw)
    if raw_path.is_absolute():
        candidates.append(raw_path)
    else:
        candidates.append((source_path.parent / raw_path).resolve())
        candidates.append((vault_root / raw_path).resolve())
        candidates.extend(vault_root.rglob(raw_path.name))
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None
