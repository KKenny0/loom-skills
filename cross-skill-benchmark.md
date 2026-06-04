# Loom Cross-Skill Benchmark — Iteration 1

Date: 2026-06-03

## Aggregate

| Metric | With Skill | Baseline | Delta |
|--------|-----------|----------|-------|
| **Pass Rate** | 98.1% (210/214) | 57.0% (122/214) | **+41.1%** |

## Per-Skill Breakdown

| Skill | With Skill | Baseline | Delta | Notes |
|-------|-----------|----------|-------|-------|
| **deep-read** | 100% (37/37) | 75.7% (28/37) | +24.3% | Gate validated: 0/4 → 4/4 |
| **debate** | 100% (33/33) | 51.5% (17/33) | +48.5% | Gate validated: 0/3 → 3/3 |
| **forge** | 88.6% (31/35) | 71.4% (25/35) | +17.1% | Gate works (4/4). Fixes applied post-iteration-1 |
| **excavate** | 100% (39/39) | 33.3% (13/39) | **+66.7%** | Largest delta. Structure is the differentiator |
| **survey** | 100% (37/37) | 56.8% (21/37) | **+43.2%** | Gate works (4/4). Lakatos/IBIS frameworks key |
| **source-dive** | 100% (33/33) | 54.5% (18/33) | **+45.5%** | Gate works (3/3). Source code reading is the differentiator |

## Per-Eval Detail

### deep-read
| Eval | With Skill | Baseline | Delta |
|------|-----------|----------|-------|
| 1. single-paper-analysis | 100% (12/12) | 83.3% (10/12) | +16.7% |
| 2. multi-source-synthesis | 100% (11/11) | 90.9% (10/11) | +9.1% |
| 3. non-ai-interview | 100% (10/10) | 80.0% (8/10) | +20.0% |
| 4. edge-case-no-sources | 100% (4/4) | 0% (0/4) | +100% |

### debate
| Eval | With Skill | Baseline | Delta |
|------|-----------|----------|-------|
| 1. concrete-claim-debate | 100% (12/12) | 66.7% (8/12) | +33.3% |
| 2. non-ai-value-debate | 100% (10/10) | 40.0% (4/10) | +60.0% |
| 3. text-based-evidence-debate | 100% (8/8) | 62.5% (5/8) | +37.5% |
| 4. edge-case-vague-thesis | 100% (3/3) | 0% (0/3) | +100% |

### forge
| Eval | With Skill | Baseline | Delta |
|------|-----------|----------|-------|
| 1. cross-domain-structural-similarity | 83.3% (10/12) | 50.0% (6/12) | +33.3% |
| 2. non-ai-cross-domain | 90.0% (9/10) | 90.0% (9/10) | 0% |
| 3. hard-pair-forge | 88.9% (8/9) | 77.8% (7/9) | +11.1% |
| 4. edge-case-single-source | 100% (4/4) | 75.0% (3/4) | +25.0% |

### excavate
| Eval | With Skill | Baseline | Delta |
|------|-----------|----------|-------|
| 1. non-ai-common-claim | 100% (13/13) | 15.4% (2/13) | +84.6% |
| 2. academic-analogy-excavation | 100% (10/10) | 40.0% (4/10) | +60.0% |
| 3. text-based-social-science | 100% (10/10) | 40.0% (4/10) | +60.0% |
| 4. edge-case-pure-fact | 100% (6/6) | 50.0% (3/6) | +50.0% |

### survey
| Eval | With Skill | Baseline | Delta |
|------|-----------|----------|-------|
| 1. non-ai-established-domain | 100% (13/13) | 38.5% (5/13) | +61.5% |
| 2. ai-agent-emerging-field | 100% (10/10) | 70.0% (7/10) | +30.0% |
| 3. non-ai-narrow-comparison | 100% (10/10) | 70.0% (7/10) | +30.0% |
| 4. edge-case-domain-too-broad | 100% (4/4) | 50.0% (2/4) | +50.0% |

### source-dive
| Eval | With Skill | Baseline | Delta |
|------|-----------|----------|-------|
| 1. single-repo-analysis | 100% (10/10) | 40.0% (4/10) | +60.0% |
| 2. multi-source-synthesis | 100% (10/10) | 50.0% (5/10) | +50.0% |
| 3. non-github-analysis | 100% (10/10) | 60.0% (6/10) | +40.0% |
| 4. edge-case-no-topic | 100% (3/3) | 100% (3/3) | 0% |

## Key Findings

### 1. Structure > Knowledge
The skill's value is structural, not informational. Baseline models produce analytically sound content but don't follow the required output format (frontmatter, section hierarchy, rating systems, coverage statements). The skill turns "a good essay" into "a compliant report."

This is most dramatic in **excavate** (+66.7%) and **survey** (+43.2%) where the structured methodology (Mohist three-tables, Lakatos research programs, IBIS controversies) is the entire differentiator.

### 2. Gate Effectiveness — Fully Validated
Hard gates work across all 6 skills. The pattern: explicit "入口门控" section before the pipeline, with a hard stop instruction.

- **deep-read eval-4**: 0/4 → 4/4 (gate validated)
- **debate eval-4**: 0/3 → 3/3 (gate validated)
- **forge eval-4**: 4/4 (worked from iteration-1)
- **excavate eval-4**: 6/6 (pure fact edge case, handled by methodology itself)
- **survey eval-4**: 4/4 (worked from iteration-1)
- **source-dive eval-4**: 3/3 (worked from iteration-1)

### 3. Non-discriminating Evals
- **forge eval-2** (90% vs 90%): Well-paired domains (ecological succession × org lifecycle) where even baseline naturally follows a decomposition approach. The skill adds no value for "easy" domain pairs.

### 4. Cross-cutting Issues
- **Hedge language**: Forge iteration-1 showed both configs using banned hedge words (可能、也许、有趣). Fix applied (rule 5 in 锻造硬规则). Needs iteration-2 validation.
- **[锻造产物] markers**: Template/output mismatch in forge. Fix applied. Needs iteration-2 validation.

### 5. Token Cost is Modest
Skills that add the most value (excavate, survey) don't dramatically increase token usage. Excavate uses ~2x tokens but achieves 3x the pass rate. Survey token delta is negligible (+3.5%).

## Recommendations

1. ~~**Re-run deep-read eval-4 and debate eval-4**~~ Done — gates validated
2. **Re-run forge iteration-2** to validate hedge-language fix and [锻造产物] marker fix (API was overloaded, retry later)
3. **Consider replacing non-discriminating eval** for forge eval-2 — it doesn't test what it's meant to test
4. **5 of 6 skills at 100%** — only forge at 88.6% (iteration-1, fixes pending validation)
