# Synthesis Pack Schema

Synthesis Pack combines multiple Source Briefs into an article-ready research package.

## Format

```markdown
# Synthesis Pack — [Working Title]

created: YYYY-MM-DD
source_ids: [S1, S2]

## Working Thesis
[User/article thesis, not necessarily identical to any source claim.]

## Merged Conclusions
- [Conclusion supported by multiple sources]

## Conflicts
| Issue | Source A | Source B | Resolution / Treatment |
|-------|----------|----------|------------------------|
| ... | ... | ... | ... |

## Evidence Weight
| Claim | Evidence Strength | Sources | Notes |
|-------|-------------------|---------|-------|
| ... | strong/medium/weak | S1, S2 | ... |

## Consensus And Disagreement
### Consensus
- [...]

### Disagreement
- [...]

## Article Spine
1. [Main section]
2. [Main section]

## High-Risk Claims
- [Claim] — risk: [why] — action: verify | soften | exclude | mark uncertainty

## Source Coverage Checklist
| Source ID | Used In Thesis | Used In Evidence | Needs More Review | Notes |
|-----------|----------------|------------------|-------------------|-------|
| S1 | yes/no | yes/no | yes/no | ... |
```

## Rules

- Distinguish source consensus from user thesis.
- Do not hide unresolved conflicts.
- Mark high-risk claims before drafting.
- Drafts can use this pack; they must not mutate it.
