# Consulting Graph Template | 2026-11-20 (Asia/Seoul)

## Execution boundary and status
- Preparation started at **03:14:05 KST**; local rendering and published Bronze integrity verification completed **03:33:38 KST**. Publication of this report is a separate final step.
- **2/3 new quantitative charts**: BCG 1 / McKinsey 1 / Bain 0. Cumulative **Bronze 71, Silver 0, Gold 0**.
- Cumulative self-verified original-fidelity chart count remains **16**, new source-faithful verified **0** (both new charts editorial/unverified). This is separate from successful Python execution and human approval.
- Python **3.13.5**, matplotlib **3.10.8**, numpy **2.3.5**; Source and Neutral themes rendered to **4 PNGs at 200dpi (2200×1240)**, all visually inspected. Two semantic unit tests passed after correcting test expectations for UTF-8 São Paulo and per-field provenance columns; chart aesthetics were adjusted and rendered again.
- Remote SHA256 check: **14/14 immutable payload files match manifest.json** and both recomputed payload_sha256 values match; manifest human_review=pending, training_eligible=false.
- GitHub Bronze commit: [0396eda2](https://github.com/UnemployedUncle/McKinseyGraphTemplates/commit/0396eda2b4365a18e18a5cef9e0d9eef46a87d16). GitHub Actions status for this commit was **not confirmed by the available PR-only workflow-run lookup**; do not treat workflow presence as a successful run.
- This stage prepared the daily material; **delivered=false**. No user review, Silver/Gold promotion, model training, or new scheduled task.

## 1. BCG — distributional income effects around startup ecosystems

**Source:** [https://www.bcg.com/publications/2026/cities-build-startup-ecosystems-faster](https://www.bcg.com/publications/2026/cities-build-startup-ecosystems-faster), published **2026-11-19**; source checked **2026-11-20**. **Exhibit 7 related passage** (original image itself not opened). Source data span **2013–2024**.

**Three-sentence gist:** BCG examines how entrepreneurial ecosystems create new businesses and may spread prosperity across population groups. In São Paulo and Singapore, reported lower-income groups achieved greater cumulative real-income percentage growth than the top decile. These differences do not causally establish that startups alone generated the change.

**Single So what:** Measure ecosystem results using real-income distribution, not only investment and valuation indicators.

| City | Low-income cohort | Low cohort real income growth | Top 10% real income growth | Within-city gap |
|---|---|---:|---:|---:|
| São Paulo | Bottom 40% | **9%** | **7%** | **+2pp derived** |
| Singapore | Bottom 10% | **36%** | **32%** | **+4pp derived** |

These 4 income-growth values are **reported**, not digitized estimates. The 2pp and 4pp gaps are **derived** and do not go into the raw observation CSV as reported. The denominator is each city's named income cohort, not the same cross-city group; real-income inflation adjustment and sample weights are not disclosed in the inspected article section. All values are cumulative percent changes, **not annual growth rates**, so do not mix % and percentage points.

**Design and why:** The source mentions a bar chart but its picture was not directly opened. The reusable **editorial grouped bar** uses x=city and group, y=real-income % change, bar height=value, paired low/high category colors, shared 0 baseline, direct top labels and a cohort-definition annotation. Bars are sorted São Paulo → Singapore and the category pair is low → high. This design shows the relative distribution within each city while explicitly warning the low-cohort denominator differs across cities.

**Reuse data_recipe:** Define comparable populations and real-income basis → source or calculate cumulative changes → attach value-level provenance and denominators → compute within-city %p gap → render 0-axis paired bars with a clear cohort caveat → investigate policy/cycle counterfactuals. Counterexample: transfer payments or wage regulation could raise low-income earnings independently of startup ecosystem maturity. **Validation: code executed; source fidelity unverified, score=null, original visual not confirmed.**

**Immutable Git bundle:** [bronze/2026-11-20/bcg_startup_income_distribution_ex7](https://github.com/UnemployedUncle/McKinseyGraphTemplates/tree/main/bronze/2026-11-20/bcg_startup_income_distribution_ex7), manifest SHA256 payload `2fb2924cb5059be617bef73a3e4c098553660faad529543228d9c3944de6fb50`.

## 2. McKinsey — labor productivity and workforce participation in Belgium

**Source:** [https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/a-bold-vision-for-belgium](https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/a-bold-vision-for-belgium), published **2026-11-19**; source checked **2026-11-20**. **Exhibit 1 official alt text and numeric table**, original graphic not directly opened. Underlying figures are **2024** national statistics; OECD/Eurostat source updates occurred during **2026 July–October**.

**Three-sentence gist:** Belgium has high GDP produced per hour worked but relatively lower workforce participation. National GDP per working-age person must be interpreted through employment, working hours and hourly productivity jointly. Greater labor-market participation without matching productivity and hours changes need not raise output mechanically at an unchanged rate.

**Single So what:** Decompose output per working-age person into employment, hours, and hourly productivity when selecting growth-policy priorities.

| Economy | GDP/working-age (€k) | Employment % | GDP/hour (€) | Hours/worker/year |
|---|---:|---:|---:|---:|
| United States | 96 | 76 | 71 | 1,775 |
| Belgium | **88** | **72** | **77** | 1,583 |
| Netherlands | 88 | 84 | 72 | 1,452 |
| Denmark | 87 | 80 | 79 | 1,372 |
| European Union | 70 | 76 | 57 | 1,661 |

All **20 values** are **reported**; GDP/working-age is per resident aged 20–64 in 2024 euros adjusted to **Belgium 2024 purchasing power**. This is not nominal GDP at market exchange rates. Employment % × GDP/hour × hours/worker gives an approximate decomposition because rounded components and source methodologies may differ. Belgium 0.72 × 77 × 1583 = €87,767 ≈ €88k, but discrepancies across all economies need not be solely attributable to rounding; verify exact OECD measurement methods before causal or accounting claims.

**Design and why:** Original official HTML alt describes integrated bar+table; exact image layout was unavailable. This **editorial bar/table** uses x=economy, y=GDP/working-age €k with 0 baseline, Belgium accent, and 3 aligned driver rows for employment, GDP/hour and annual hours. Countries retain the original narrative order and individual bars have €k value labels. Fixed bar width and configurable source/neutral theme allow peer-country/business-unit reuse.

**Reuse data_recipe:** Fix age population and PPP/real-price basis → gather matched-year employment, hours and productivity → retain provenance for each metric → sanity-check decomposed total with explicit tolerance → plot KPI bars and driver table → check industrial composition and country age-structure before interpreting policy causation. **Validation: code executed; source fidelity unverified, score=null.**

**Immutable Git bundle:** [bronze/2026-11-20/mckinsey_belgium_productivity_ex1_bar_table](https://github.com/UnemployedUncle/McKinseyGraphTemplates/tree/main/bronze/2026-11-20/mckinsey_belgium_productivity_ex1_bar_table), manifest SHA256 payload `8783cf8cf68e127636f7c4aeff7d7d54eadad0ce60eb903466c9cd2e37c11b79`.

## 3. Bain — exclusion
Primary recent candidate within 7 days was Bain's 2026-11-18 luxury-market analysis carried by a third-party press release, but no accessible **Bain-hosted original numerical figure** matching the source/figure/date conditions could be confirmed. The expanded 30-day search did not yield an accessible and nonduplicate confirmed original chart. Do **not** invent a Bain item or equate third-party narrative statistics with an original Bain quantitative figure.

## Source reuse and limitations
- Original copyrighted figures, logos, proprietary fonts, complete report text, private data and credentials were **not** stored in Git or the preview ZIP.
- Theme colors represent an independently constructed source-style palette, not a verified pixel-exact reproduction of the consulting firm's original design.
- The PNG previews and local reproducibility tests are generated outputs, not part of the immutable Bronze bundle. The **GitHub manifest and file SHA** identify the immutable versions; do not use a separately generated local preview package as an exact hash reference.
- Chart execution, source visual fidelity and human approval remain separate evidence states. Both new items are **human_review=pending**, **training_eligible=false**.
- At 07:15, read runs/2026-11-20/prepared.json and this exact report, verify current GitHub status, and deliver **once only** without running new research or duplicate commits.
