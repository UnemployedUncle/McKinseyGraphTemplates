# The Future of Banking: Strategy for the AI Era — Figure 2 — Banks with leadership positions have measurably better returns

## Article gist (3 sentences)
Bain compares return on equity across business areas in major global banks classified by market leadership. Leading positions are associated with 15% ROE versus 9% for weaker positions. The exhibit is an association, not an experiment identifying a causal effect.

**So what:** Prioritize defending or building defensible leadership where economics justify it; do not assume the 6pp ROE association is causal.

## Business context → metric → decision
Business-area market leadership correlates with higher ROE: 15% versus 9% among the surveyed top 30 banks. Unit is % ROE; source publication 2026-11-12; underlying data Bank assets at 2025 year-end; return analysis 2025. Denominator: Top 30 banks by 2025 year-end assets. Compare observations only where definitions and periods align. This supports resource prioritization, not causal attribution.

## Data and provenance
| Category | Value | Unit | Provenance |
|---|---:|---|---|
| Weak | 9 | % ROE | reported |
| Leading | 15 | % ROE | reported |

Original chart: Two-category vertical bar, weak gray and leading red. Created: comparison_bar. Visual encoding: x=leadership group, y=ROE %, two vertical bars; weak in gray and leading in red; sorted in original weak→leading order, shared zero and direct labels; no legend needed. Layout, colors, labels, font and chart title are set in config.json THEME/CONTEXT; derived locations use values in data.csv.

## Published data and method
Source: https://www.bain.com/insights/future-of-banking-strategy-for-ai-era/ (published 2026-11-12, checked 2026-11-19). Underlying source context: Bank assets at 2025 year-end; return analysis 2025. Top 30 publicly traded banks ranked by 2025 assets; the sample is not all banks. Weak and leading refer to market-position classes across 18 business areas. Reported returns are averages/benchmark comparisons; underlying bank-level estimates and weighting were not disclosed. Explicit unpublished data, weights and sample details remain undisclosed.

## Reusable data_recipe
1. Select a consistent population of large banks and define business-area leadership using disclosed ranks.
2. Assign each comparable business area to weak or leading based on rank thresholds.
3. Compute ROE with the same measurement date, weighting policy and profitability definition.
4. Plot both values against a shared zero baseline, with exact direct labels.
5. Test composition, survivorship and endogeneity before claiming causal effects.

## Message conditions and counterexamples
- Top 30 publicly traded banks ranked by 2025 assets; the sample is not all banks.
- Weak and leading refer to market-position classes across 18 business areas.
- Reported returns are averages/benchmark comparisons; underlying bank-level estimates and weighting were not disclosed.

**Counterexample:** A higher displayed value alone does not establish causation, eliminate composition bias or apply to different populations. Decisions require matched definitions and external operational evidence.

## Reuse and verification
Edit data.csv, config.json THEME.source / THEME.neutral and CONTEXT; run `python chart.py --theme source --output artifacts/source.png` and neutral analog. Render success, original fidelity and human review are separate statuses. **Status:** verified (agent self-assessment 4.57/5); human_review=pending. Opened actual Flourish Figure 2 thumbnail; shape, ordering, colors, labels and two reported values reproduced. Font and vertical whitespace are not pixel-identical.
