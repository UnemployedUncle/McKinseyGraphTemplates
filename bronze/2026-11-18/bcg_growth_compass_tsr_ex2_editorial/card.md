# To Find Growth in Today's Market, CEOs Need a New Compass

## Article gist (three sentences)
BCG argues companies should combine reinforcing growth vectors rather than follow one universal growth playbook. Exhibit 2 illustrates three companies' growth-vector combinations alongside five-year shareholder returns. The published panel makes the sector comparison explicit for Trane and Brinker but not numerically for Aurobindo.

## So what (one)
Compare growth-path choices against comparable industry baselines, without treating observed TSR outperformance as causal proof.

## Business context → metric → decision
**Source fact:** Trane Technologies (23% vs 5% median) and Brinker International (32% vs 0% median) outperformed their respective sector medians in five-year annualized TSR; Aurobindo Pharma delivered 13% but its numerical sector comparator was not disclosed.

**Metric specification:** % annualized TSR; Sep 2021–Sep 2026; observation unit and per-row denominator are in data.csv. The relevant comparator is the S&P 500 industry median for the same five-year window. **Interpretation:** Compare growth-path choices against comparable industry baselines, without treating observed TSR outperformance as causal proof.

**Source vs observation vs inference:** Source-reported numbers are tagged in CSV; differences are derived only as explicit arithmetic. The takeaway is managerial interpretation, not a measured causal effect. Reuse in another industry is a proposal, not a source finding.

## Source and research method
Published: 2026-11-17. Collected/check date: 2026-11-18. Underlying data: Sep 2021–Sep 2026. BCG ValueScience / S&P Capital IQ; sample count not disclosed for this exhibit; company and sector returns include reinvested dividends. Article published Nov 17 2026. Official Exhibit 2 opened and visually inspected. Brinker 32%/0% and Trane 23%/5% can be read in the caption; Aurobindo 13% with unknown numeric median.

## Chart encoding and design
- Original chart: Three circular growth-vector compass panels with annualized TSR captions
- Editorial encoding: x=annualized TSR, y=company in exhibit order, dots=company versus sector median, connector=percentage-point gap, direct labels; one missing benchmark plotted only as a single dot.
- Axes, title, labels, colors, emphasis, layout, and notes use config.json (THEME/CONTEXT); computed positions derive from CSV; displayed labels use input values.
- Caution: Original six-vector radial graphics are not reproduced; the new quantitative dot chart is a deliberate editorial redesign. Aurobindo median not disclosed.

## Reusable data recipe
1. Fix consistent five-year TSR period and peer selection.
2. Calculate annualized dividend-reinvested TSR for company and industry median.
3. Mark unavailable comparator as missing, never zero.
4. Use paired dots for known company–median pairs and one unpaired dot for unknown benchmark.
5. Check whether external factors could explain TSR outperformance.

## Conditions and counterexamples
- Same return measure, period, and currency are used for comparison.
- S&P 500 industry median is not an individually matched competitor.
- Observed outperformance is descriptive, not a causal estimate.
- Counterexample: One-off sector shocks can lift shareholder returns without validating the stated growth-vector strategy.
- Undisclosed sample, formula parameters, and assumptions are not invented.

## Reproduction and reuse
```bash
python chart.py --theme source --output artifacts/bcg_growth_compass_tsr_ex2_editorial/source.png
python chart.py --theme neutral --output artifacts/bcg_growth_compass_tsr_ex2_editorial/neutral.png
```
Change data.csv, THEME.source/neutral and CONTEXT for comparable datasets; do not edit the original Bronze snapshot. Images are generated under artifacts outside the snapshot. This is not approved training data.

Official source: https://www.bcg.com/publications/2026/how-ceos-build-growth-strategy
