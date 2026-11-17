# Consulting Graph Template | 2026-11-18 (Asia/Seoul)

## Execution and review boundary

Preparation started **03:19:52 KST** and completed **2026-11-18T03:37:03.813+09:00**. The target was **3 quantitative firm figures**; **2 newly added**, one per BCG and McKinsey. Cumulative catalog counts: **Bronze 66 / Silver 0 / Gold 0**. Previously source-faithful self-verified **15**; today **0**. The two new charts are editorial rather than original graphics, `validation_status=unverified`, `fidelity_score=null`, `human_review=pending`. No human review, Gold/Silver promotion, or model training was performed.

## 01 — BCG, growth-vector strategies and annualized shareholder return

**Source:** [To Find Growth in Today's Market, CEOs Need a New Compass](https://www.bcg.com/publications/2026/how-ceos-build-growth-strategy), published **2026-11-17**; Exhibit 2, visually inspected original radial graphic. The five-year measure covers **September 2021–September 2026**; source BCG ValueScience and S&P Capital IQ.

**Article gist (three sentences).** BCG advocates mutually reinforcing growth vectors instead of a universal growth formula. Exhibit 2 examines three illustrative companies with five-year annualized shareholder returns (TSR). The exhibit discloses numeric industry comparisons for two companies, but not a numeric Aurobindo benchmark.

**Single So what:** Evaluate company-specific strategic choices against aligned industry benchmarks without treating observed return differences as causal proof.

| Company | Annualized company TSR | Industry median | Status |
|---|---:|---:|---|
| Trane Technologies | 23% | 5% | reported / reported |
| Brinker International | 32% | 0% | reported / reported |
| Aurobindo Pharma | 13% | not disclosed | reported / missing |

**Business context → metric → decision.** Five-year annualized TSR (%) is the y-independent numeric x position, companies occupy the y-axis in source order; sector medians are displayed as paired dots and line connectors wherever numeric information exists. Missing peer comparison is intentionally not shown as a zero. Use it to rank benchmarking opportunities, not to identify a causal explanation for outperformance.

**Design:** Paired dot plot; x=annualized TSR, y=company, company dot saturated, available peer dots neutral, direct labels, shared zero reference. This **replaces** the source's radial growth-compass panels and is **not** a source-faithful reproduction.

**Data recipe:** Align the period and sector comparison; calculate dividend-inclusive annualized TSR; obtain peer median with disclosed methodology; separate reported, derived, and missing measurements; display connectors only for actual matched data; acknowledge market and sector confounders. **Key limitations:** Aurobindo's comparator and full sample methods are not disclosed. A return gap does not establish the causal value of a growth tactic.

**Bundle:** [bronze/2026-11-18/bcg_growth_compass_tsr_ex2_editorial](https://github.com/UnemployedUncle/McKinseyGraphTemplates/tree/main/bronze/2026-11-18/bcg_growth_compass_tsr_ex2_editorial); **payload SHA256:** `d6b101831413992a15a049a1e942e95cf36b3c072f97ddf7df6cac39e783c757`.

## 02 — McKinsey, UK energy transmission constraint costs

**Source:** [Solving Britain's energy bottlenecks](https://www.mckinsey.com/uk/our-insights/solving-britains-energy-bottlenecks-the-78-billion-pounds-a-year-opportunity-for-cleaner-more-affordable-power), published **2026-11-16**. The cost figures cite a **National Audit Office assessment dated 2026-09-11**. The original article's six-value-pool SVG figure was not visually inspectable; the chart here is an **editorial bar chart from a separate quantitative paragraph**.

**Article gist (three sentences).** McKinsey studies several UK clean-energy bottlenecks and the opportunities associated with addressing them. Transmission constraints cost **£1.9bn per year in FY2025/26**. With insufficient coordinated grid investment they **could** cost **£7.8bn per year by 2030**.

**Single So what:** Use future network-cost exposure to prioritize energy interventions, without confusing a conditional forecast with already incurred or committed expenditure.

| Period | GBP billion per year | Status | Provenance |
|---|---:|---|---|
| FY2025/26 | 1.9 | Observed | reported |
| 2030 | 7.8 | Conditional projection | reported forecast |
| Difference | +5.9 | Calculated change | derived = 7.8 − 1.9 |

**Business context → metric → decision.** Both figures use annual UK transmission constraint costs as the denominator and £bn/year as the unit. Bar height encodes amounts, hatching and color distinguish historical observation from conditional scenario, direct labels show amounts. This is **not** the report's separate **£78bn annual commercial opportunity**, and those unlike quantities must not be summed. No undisclosed inflation base or probability distribution was invented.

**Data recipe:** Define comparable annual cost; separate actual and forecast periods; preserve the scenario's conditional assumptions; calculate the disclosed-value difference; distinguish units, price basis, and uncertainty; evaluate alternative grid-upgrade assumptions. **Key limitation:** Model inputs and inflation basis for the 2030 cost scenario are not fully disclosed.

**Bundle:** [bronze/2026-11-18/mckinsey_uk_grid_constraint_cost_outlook_editorial](https://github.com/UnemployedUncle/McKinseyGraphTemplates/tree/main/bronze/2026-11-18/mckinsey_uk_grid_constraint_cost_outlook_editorial); **payload SHA256:** `ff751b76d8086641dd233776ece5c81c457c06778182e4827f357f766900d1ed`.

## Bain — excluded rather than invented

Official Bain search was prioritized for **2026-11-11–18**, then widened to **2026-10-19–11-18**. A nonduplicate recently published quantitative chart with accessible original and dated numeric evidence could not be firmly established. No 3rd template or synthetic data was fabricated.

## Code, tests, images, verification

Both bundles contain `chart.py`, `data.csv`, `config.json`, `requirements.txt`, `card.md`, `record.json`, `validation.json`, `manifest.json`. Each implements `render(data, theme, context)->fig`; adjustable `THEME.source`, `THEME.neutral`, `CONTEXT`, and CSV. Generated Source and Neutral PNGs: **4**, **200dpi**, **2200×1240**, visually inspected. The four portable code/data/config/requirements files of each local preview were SHA256-matched with GitHub and can be downloaded together separately; GitHub remains canonical for full exact payload.

Local commands executed for both: `python chart.py --theme source --output artifacts/source.png`; `python chart.py --theme neutral --output artifacts/neutral.png`. Local Python **3.13.5**, matplotlib **3.10.8**, and 8 semantic checks passed. GitHub Actions Python **3.11** passed unit tests, full medallion checks, all **132 previews for 66 Bronze bundles**, and artifact upload, as verified for commit `a7270abb9bc66dea4c939ffd3914e66f8605bb18`.

**Important correction history:** the first upload contained incorrect SHA256 envelopes. They were recomputed from actual committed bytes and corrected in commit [2cae761](https://github.com/UnemployedUncle/McKinseyGraphTemplates/commit/2cae761deb8638dd57b148a2872c78f890d75ebb). The existing runner assumed CLI `--data`/`--config` accepted everywhere; a non-destructive retry for explicitly rejected flags was validated locally and published as [a7270ab](https://github.com/UnemployedUncle/McKinseyGraphTemplates/commit/a7270abb9bc66dea4c939ffd3914e66f8605bb18). Existing immutable Bronze snapshots were not edited and no Silver/Gold files were touched. Earlier failing Actions runs were not represented as successes.

**GitHub Actions result:** [Run 44149292190](https://github.com/UnemployedUncle/McKinseyGraphTemplates/actions/runs/44149292190) — `completed/success`; [132 generated previews and smoke-test artifact](https://github.com/UnemployedUncle/McKinseyGraphTemplates/actions/runs/44149292190/artifacts/14359140159). User review is still **pending**. A passing Python or CI check is neither source-faithful reproduction nor human approval.

## Morning single-delivery instruction

At 07:15 read `runs/2026-11-18/prepared.json` and this report **first**. Deliver the prepared material only once; do not restart discovery, create further chart files, or duplicate Git commits. Never describe these editorial figures as original-chart certified. Retain all safety and review boundaries.
