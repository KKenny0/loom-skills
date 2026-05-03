# Material List Schema

Material List is the source ledger for a research task. It is created before deep reading or drafting.

## Format

```markdown
# Material List — [Task Title]

> Created: YYYY-MM-DD
> Task type: single-source deep dive | multi-source synthesis | theme research | draft rewrite

| ID | Title | Author | Date | Type | Source Tier | Relevance | Citation Usability | Risk Level | Raw Path | Capture Status |
|----|-------|--------|------|------|-------------|-----------|--------------------|------------|----------|----------------|
| S1 | ... | ... | ... | article | primary | high | direct | low | https://... | pending |
```

## Fields

- `ID`: stable source id, for example `S1`, `S2`.
- `Title`: source title or inferred title.
- `Author`: author, org, channel, or `unknown`.
- `Date`: source publication date or retrieval date.
- `Type`: article, paper, docs, X thread, YouTube, book, local file, pasted text, other.
- `Source Tier`: primary, secondary, commentary, social, unknown.
- `Relevance`: high, medium, low.
- `Citation Usability`: direct, background, not-citable, unknown.
- `Risk Level`: low, medium, high.
- `Raw Path`: must point to a real source: URL, local raw file, converted Markdown, original file path, or `pasted-local-text`.
- `Capture Status`: pending, captured, failed, skipped.

## Rules

- Every row must have `Raw Path`.
- If capture has not happened, `Raw Path` can be the original URL/path and `Capture Status` is `pending`.
- Do not remove low-relevance sources if they explain discarded context; mark relevance instead.
- High-risk sources need later verification or exclusion.
