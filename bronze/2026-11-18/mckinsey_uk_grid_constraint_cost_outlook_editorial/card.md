# Solving Britain's energy bottlenecks: The £78 billion-a-year opportunity for cleaner, more affordable power

## Article gist (three sentences)
McKinsey frames six bottleneck-related UK energy value pools totaling about £78bn annual commercial opportunity in 2030. It separately cites the National Audit Office's observation of £1.9bn transmission constraint costs in 2025/26. Absent coordinated grid action the cited outlook could reach £7.8bn per year by 2030.

## So what (one)
Prioritize transmission-grid bottlenecks by potential annual system cost, while keeping conditional outcomes separate from committed spending.

## Business context → metric → decision
**Source fact:** Without concerted upgrades, annual UK transmission constraint costs could rise from £1.9 billion in FY2025/26 to £7.8 billion by 2030, a conditional £5.9 billion increase.

**Metric specification:** GBP bn per year; FY2025/26 and conditional 2030; observation unit and per-row denominator are in data.csv. The relevant comparator is the conditional 2030 scenario relative to annual FY2025/26 constraint costs. **Interpretation:** Prioritize transmission-grid bottlenecks by potential annual system cost, while keeping conditional outcomes separate from committed spending.

**Source vs observation vs inference:** Source-reported numbers are tagged in CSV; differences are derived only as explicit arithmetic. The takeaway is managerial interpretation, not a measured causal effect. Reuse in another industry is a proposal, not a source finding.

## Source and research method
Published: 2026-11-16. Collected/check date: 2026-11-18. Underlying data: FY2025/26 and conditional 2030. UK National Audit Office / McKinsey citation; modeled assumptions for 2030 scenario not provided in article. McKinsey article dated Nov 16 2026; UK National Audit Office forecast dated Sep 11 2026. Source exhibit SVG fetch unsupported. Textual numbers accessible.

## Chart encoding and design
- Original chart: Six energy value-pool exhibit (SVG, inaccessible to graphic comparison)
- Editorial encoding: x=period/status, y=annual GBP billions, fill+hatching=observed versus conditional forecast, direct labels and computed £5.9bn difference.
- Axes, title, labels, colors, emphasis, layout, and notes use config.json (THEME/CONTEXT); computed positions derive from CSV; displayed labels use input values.
- Caution: Original article's six-value-pool SVG exhibit could not be viewed; this is an editorial chart from a separate sourced paragraph, not exhibit reproduction. Do not compare £78bn market revenues against £7.8bn grid costs as additive.

## Reusable data recipe
1. Define annual network constraint costs as the comparable metric.
2. Use FY2025/26 reported cost and 2030 conditional scenario only.
3. Keep forecast status explicit and preserve undisclosed price-basis.
4. Calculate annual difference by subtracting reported values.
5. Do not confuse costs with the article's distinct £78bn commercial opportunity.

## Conditions and counterexamples
- The £7.8bn estimate is conditional on insufficient grid upgrades.
- Each number is an annual amount, not a cumulative multi-year amount.
- Inflation basis for the National Audit Office constraint-cost comparison is not stated in this article.
- Counterexample: Grid reinforcement or improved dispatch could prevent the high-cost 2030 scenario.
- Undisclosed sample, formula parameters, and assumptions are not invented.

## Reproduction and reuse
```bash
python chart.py --theme source --output artifacts/mckinsey_uk_grid_constraint_cost_outlook_editorial/source.png
python chart.py --theme neutral --output artifacts/mckinsey_uk_grid_constraint_cost_outlook_editorial/neutral.png
```
Change data.csv, THEME.source/neutral and CONTEXT for comparable datasets; do not edit the original Bronze snapshot. Images are generated under artifacts outside the snapshot. This is not approved training data.

Official source: https://www.mckinsey.com/uk/our-insights/solving-britains-energy-bottlenecks-the-78-billion-pounds-a-year-opportunity-for-cleaner-more-affordable-power
