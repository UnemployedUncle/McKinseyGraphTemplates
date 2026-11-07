# McKinsey · Airline economic profit: top vs middle vs bottom (Exhibit 2 text)

**Publication:** 2026-11-06. **Collected:** 2026-11-08 Asia/Seoul. **Underlying observations:** 2025, 97 airlines. **Source:** https://www.mckinsey.com/industries/travel/our-insights/could-aviation-at-last-be-close-to-earning-its-wings, Exhibit 2 / discussion immediately below. **Original image:** McKinsey SVGZ inaccessible for visual comparison; article narrative verified.

## Article in three original sentences
The 2025 airline sector still failed to cover its cost of capital despite profitability improvements versus the prepandemic period. Individual airline outcomes are highly unequal: twenty top performers generated a large net economic profit while twenty bottom performers destroyed much more value. Improvements at the top do not offset severe underperformance elsewhere.

## So what — one decision
**Assess airline portfolio investments and operating transformation by the dispersion of firm-level economic profit, not the industry average alone.**

## Context → metric → judgment
- **Context:** Do airline industry aggregates conceal winners and losers?
- **Metric:** 2025 cohort sum of economic profit, in **USD billions**, as distinct from revenue, net income or economic-profit margin. Economic profit = (ROIC–WACC) × invested capital under McKinsey's disclosed conceptual definition.
- **Denominator:** 97 sampled airlines, split 20 top, 57 middle and 20 bottom by economic profit performance, not equal-sized groups of airlines across middle aggregated three quintiles.
- **Compare:** +14.0 / −2.3 / −22.9; group sizes differ, so sum of dollar amounts is not per-airline performance.
- **Decision:** Investigate the business model and unit economics of carriers at both tails rather than extrapolating average profitability.

## Observed source vs edited visualization
The original Exhibit 2 is an industry **power curve**, not a 3-bar chart. SVGZ source media could not be rendered in the analysis environment, so neither original layout nor detailed curve points are claimed reproduced. Our **editorial** horizontal diverging bar chart deliberately compresses the reported quintile aggregates and marks the zero line; teal = aggregate economic profit positive, dark blue = negative, labels show +/- USD billion; name includes `airline_count`.

## Sources, calculations and audit concern
- Original exact article-stated values: top 20 airlines **+$14.0bn**, middle 57 **−$2.3bn**, bottom 20 **−$22.9bn**; all `reported`.
- **Group total = −$11.2bn**, whereas the article says the 2025 **entire airline industry economic loss is −$12.8bn**, a difference of **$1.6bn**. The sample of 97 airlines and sector-level estimate may represent different coverage, adjustments or methods; the source does not explain the reconciliation here. DO NOT force or assign the discrepancy; no invented residual group.
- Survey/date: 2025 annual company economic profit, not a consumer sample. Currency is USD nominal? **Price adjustment not specified in source**, leave as unspecified nominal/real rather than asserting.

## Data recipe for reuse
1. Gather ROIC, WACC and invested capital for a consistently defined airline universe and observation year.
2. Calculate economic profit in common currency/scale and rank firms descending by chosen metric.
3. Define cohort boundaries; aggregate dollar economic profit per group and count firms.
4. Check all group counts sum to full sample; report total-of-sample and separate any sector benchmark if coverage differs.
5. Plot diverging bars against zero and label monetary units explicitly; exclude percentages unless separately defined.
6. Replace data.csv / CONTEXT / THEME and run both display themes.

## Conditions, counterexamples, limitations
Group dollar totals reflect group sizes and invested capital; group profitability per airline, ROIC and cost of capital cannot be inferred. Changing cohort size or definition can alter results. Outliers may dominate a group sum. These three aggregate values are suitable for *editorial data storytelling*, not exact reconstruction of Exhibit 2's curve. Human review pending. No external model training performed.

## Run
`python chart.py --data data.csv --config config.json --theme source --output source.png`; repeat with `--theme neutral`.
