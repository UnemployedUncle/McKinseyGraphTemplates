# Consulting Graph Template | 2026-11-19 (Asia/Seoul)

## Preparation and review boundary
- Started **03:12:25 KST**; finished preparation **03:29:45 KST**.
- Newly added **3 / target 3**: Bain 1, BCG 1, McKinsey 1.
- Cumulative **Bronze 69 / Silver 0 / Gold 0**.
- Source-reproduction self-verified before run **15**, new **1 (Bain)**, cumulative **16**. Source fidelity is independent of successful Python execution and explicit human review.
- All 3 records have **human_review=pending**; no Silver/Gold promotion, no approved training data.
- Main Bronze commit: [794d541ef84b7e17c3d9f3b6ea497e91b0567037](https://github.com/UnemployedUncle/McKinseyGraphTemplates/commit/794d541ef84b7e17c3d9f3b6ea497e91b0567037).
- GitHub Actions [run 44369857675](https://github.com/UnemployedUncle/McKinseyGraphTemplates/actions/runs/44369857675) completed **success** for unit tests, medallion integrity, all-chart render and artifact upload. [Image and log artifact](https://github.com/UnemployedUncle/McKinseyGraphTemplates/actions/runs/44369857675/artifacts/14457189416).

## 01 — Bain: banking market leadership and profitability

**Source:** [https://www.bain.com/insights/future-of-banking-strategy-for-ai-era/](https://www.bain.com/insights/future-of-banking-strategy-for-ai-era/), published **2026-11-12**, Figure 2; official source chart image actually opened and visually inspected.

**Three-sentence gist:** Bain analyzes strategic differentiation across leading banks in an AI-era competitive environment. In its top-30-bank analysis, strong market leadership is associated with higher returns on equity. The observed difference does not establish a causal effect.

**Single So what:** Prioritize leadership in bank businesses whose economics justify it; do not interpret correlation as causation.

| Segment | ROE | Provenance |
|---|---:|---|
| Weak positions | 9% | reported |
| Leading positions | 15% | reported |

The relevant difference is **6 percentage points**, a derived value. Denominator is banks/business areas among the top 30 listed banks by 2025 assets, across 18 areas; exact individual-bank observations and calculation weights are not publicly available. Chart type: original two-bar vertical comparison faithfully reproduced in high-level structure. Gray=weak, red=leading, x=leadership class, y=ROE %, shared baseline 0, direct labels 9% and 15%, no legend needed. **Self-assessment 4.57/5** over seven original comparison dimensions; text spacing and typography differ. Use same sampling frame, position threshold, ROE calculation, and time basis to reuse for bank business portfolios. This is descriptive association, not evidence that becoming a leader by itself raises ROE.

**Immutable Bronze:** [chart.py, data.csv, config.json, card, record and manifest](https://github.com/UnemployedUncle/McKinseyGraphTemplates/tree/main/bronze/2026-11-19/bain_future_banking_leadership_roe_fig2), payload `1e1a5309a013c68ba19f2a61d925005d6816bec558f5a57aaef747775c939b21`.

## 02 — BCG: OECD energy import reliance

**Source:** [https://www.bcg.com/publications/2026/countries-strengthen-energy-security](https://www.bcg.com/publications/2026/countries-strengthen-energy-security), published **2026-11-18**; numerical statement associated with Exhibit 2, **original image not visually verified**.

**Three-sentence gist:** BCG examines how energy-security policy should respond to import dependence and strategic exposures. The article reports that approximately 60% of OECD countries rely on imports for more than half their energy. Country-level observations and the exact measurement year are not supplied in the inspected passage.

**Single So what:** Prioritize domestic-energy and diversification initiatives with country-specific dependency measurement rather than treating the OECD average as a country's risk profile.

The value **~60%** is reported and approximate; **~40%** is a derived *approximate* complement and is not separately observed. Denominator is the count of OECD countries, not energy consumption volume; no precise sample count/time basis was released in the passage. Our 100%-stacked bar is **an editorial comparison, not the original Exhibit 2**: x=0–100% aggregate share, teal=above-half import dependence, gray=other, approximate direct labels, two-color legend. Reuse by defining consistent country membership, period, energy-balance formula and threshold, then counting actual countries. Do not infer detailed country values or confidence intervals from the rounded statistic. **Original fidelity: unverified/null.**

**Immutable Bronze:** [source, reusable code, full methods and caveats](https://github.com/UnemployedUncle/McKinseyGraphTemplates/tree/main/bronze/2026-11-19/bcg_oecd_energy_import_ex2_editorial), payload `17be91295723a295555013dd4a511640b071838a06d484f55895f167aab91fa7`.

## 03 — McKinsey: observed and modeled global bank ROE uplift

**Source:** [https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/global-banking-annual-review](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/global-banking-annual-review), published **2026-11-17**, Exhibit 5 numerical values; original exhibit visualization **not directly inspected**.

**Three-sentence gist:** McKinsey describes shifts in global bank profitability and capital allocation. It models passive tailwinds and active strategic actions as distinct sources of ROE improvement between 2025 and 2028. These values are prospective estimates, not realized 2028 profits.

**Single So what:** Separate exogenous tailwinds from the active capital-management premium when setting bank strategy targets.

| Component | Value | Unit | Provenance |
|---|---:|---|---|
| 2025 global bank ROE baseline | 13 | % ROE | reported |
| Passive tailwind | +2.3 | percentage points | reported scenario |
| Active initiative premium | +1.4 | percentage points | reported scenario |
| Modeled 2028 outcome | 16.7 | % ROE | derived (13+2.3+1.4) |

Waterfall chart x=baseline/passive/active/final, y=ROE %, neutral baseline, accented forecast increments, dark final bar, connectors and direct numeric labels. The layout is an **editorial redesign**, not a verified pixel match to Exhibit 5. Reuse via consistent ROE denominators, explicitly separate observed and forecast/model components, and ensure percentage-point arithmetic. Rounding and model inputs remain a limitation; do not generalize to individual banks. **Original fidelity: unverified/null.**

**Immutable Bronze:** [source, code, data, config and validation](https://github.com/UnemployedUncle/McKinseyGraphTemplates/tree/main/bronze/2026-11-19/mckinsey_banking_roe_uplift_ex5_editorial), payload `1a7f8c566b0add66799eab783a3fd383622183898cef156828e924bc9ae7f3e2`.

## Execution and storage evidence

Python **3.13.5**, matplotlib **3.10.8**; code successfully rendered each theme for each of three charts (six PNGs, **2200×1240 px, 200 dpi**); all six visually inspected. Local semantic checks included signed values, ROE % versus percentage-point differences, categorical ordering, approximate complement, rounding and missing/unknown denominators. The GitHub Action for the Bronze commit also passed its unit tests, `scripts/medallion.py validate`, full `scripts/render_all.py` and artifact upload. The current main's 69 Bronze bundles were preserved; catalog/index.json, catalog/README.md and dataset JSONL were updated; only 3 new Bronze bundles were added.

Generated PNGs are **not** part of the immutable Bronze bundle. Download new image files in the locally created preview ZIP in the conversation or in [Actions artifact 14457189416](https://github.com/UnemployedUncle/McKinseyGraphTemplates/actions/runs/44369857675/artifacts/14457189416).

**Storage and approvals:** Individual file SHA256 and payload SHA256 are in each manifest; `human_review=pending` and `training_eligible=false`. No company logo/report image/font, internal file ID, private client data or credentials added. Neither a successful render nor a self-fidelity score is human approval. Silver and Gold remain empty. No model retraining or extra schedule.

## Morning handoff

Read [prepared.json](https://github.com/UnemployedUncle/McKinseyGraphTemplates/blob/main/runs/2026-11-19/prepared.json) and the immutable Bronze records before user delivery. `prepared_complete=true`, `delivered=false`. Deliver the exact prepared material and real CI status once; do not initiate a second research topic, second package or duplicate commit. Re-check GitHub `main` and newest CI status for the handoff if helpful.
