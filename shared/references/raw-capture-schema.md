# Raw Capture Schema

Raw Capture preserves source material before analysis or rewriting.

## Raw Capture Metadata

Use this metadata in the raw file when possible, or in the corresponding inbox Daily Note when the raw format cannot store frontmatter.

```markdown
---
source_id: "S1"
title: "[Source Title]"
source_url: "[URL or local]"
source_type: "[web-clip|x-thread|youtube|paper|file|text]"
retrieved_at: "YYYY-MM-DD"
capture_tool: "[baoyu-url-to-markdown|baoyu-youtube-transcript|manual|other]"
raw_path: "[path or URL]"
extraction_notes: "[brief notes]"
---
```

## Inbox Daily Note Entry

```markdown
---
title: "[Title]"
date: "YYYY-MM-DD"
status: "inbox"
source_url: "[URL or local]"
source_type: "[web-clip|x-thread|youtube|paper|file|text]"
raw_path: "[raw source path]"
tags: [tag1, tag2]
topic: "[topic-slug]"
---

## Source
[Traceable source identity and raw path.]

## Capture Notes
[Faithful short note about what was captured.]

## Next Step
[read | synthesis | draft | skip]
```

## Rules

- Raw Capture is not article prose.
- Preserve source meaning and source wording as much as the capture medium allows.
- Do not add rhetorical framing, title optimization, or publication polish.
- `raw_path` must resolve to a real file, original URL, or explicit local text marker.
