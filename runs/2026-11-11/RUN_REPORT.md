# Consulting Graph Template | 2026-11-11 — Prepared

## Executive summary
- Completed 2 / target 3 (BCG Exhibit 2, McKinsey Exhibit 1 article-reported subset); Bain not selected.
- Bronze 52 / Silver 0 / Gold 0. Original reproduction agent-verified cumulative 14, newly 1.
- Python 3.13.5 / matplotlib 3.10.8. Six local unit tests passed; four source/neutral PNGs rendered at 200 dpi and visually checked. Images kept outside immutable Bronze.
- BCG source original Exhibit 2 inspected at https://www.bcg.com/publications/2026/how-industrial-companies-win-with-ai (published 2026-11-10). Partial card-type reproduction self-score 4.57/5; omits original descriptions. Local verified is **not** human approval.
- McKinsey original Figure 1 SVGZ could not be visually opened. Only two article-reported ranges, 34–71% and 29–69%, are plotted; edit-only, fidelity=null/unverified. Survey 2026-04-15–06-06, total n=50,744.
- Bain: unable to verify a new eligible dated chart from 7/30-day searches; no fabricated values.
- Each file has per-file SHA256 and payload SHA256, human_review=pending, training_eligible=false.
- Initial main head: 11945b834359cb4a9f136ff9d52b5efa3309effa. Commit head and GitHub Actions are checked post-publication and may differ from the values recorded when this immutable preparation record was created.
- This is a preparation package, not morning delivery; delivered=false.

## Charts
1. BCG: bronze/2026-11-11/bcg_industrials_ai_capability_gap_ex2 — KPI grid with industrial percentages 10,15,11,9,31 and differences -8,-5,-4,-4,-2 pp. Other-sector values are formula-derived.
2. McKinsey: bronze/2026-11-11/mckinsey_state_cx_service_ranges_ex1_editorial — state satisfaction range plot for retirement benefits (34–71%) and small business financial assistance (29–69%), an editorial redesign.

## Reproduction
python chart.py --data data.csv --config config.json --theme source --output source.png
python chart.py --data data.csv --config config.json --theme neutral --output neutral.png

## Original sources
BCG: https://www.bcg.com/publications/2026/how-industrial-companies-win-with-ai
McKinsey: https://www.mckinsey.com/industries/public-sector/our-insights/beyond-agency-boundaries-building-a-statewide-approach-to-customer-experience

## Review control
Human review never delegated or marked approved. Silver and Gold untouched. Never use Bronze as approved training data.
