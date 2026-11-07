# BCG · Market leaders: Value capture × tenure (Exhibit 2)

**Publication:** 2026-11-06. **Collected:** 2026-11-08 Asia/Seoul. **Underlying study:** market capitalization of US-listed top 2,000 companies sampled five-yearly, 1990–2025 (S&P Capital IQ). **Canonical source:** https://www.bcg.com/publications/2026/market-leaders-staying-on-top-longer, Exhibit 2. **Source visual:** accessed; precision limited.

## Article in three original sentences
BCG observes that firms often stay market leaders longer now, but longevity alone does not guarantee defensible advantage. Exhibit 2 compares the share of newly created value captured by top five companies with the share of long-tenured incumbents in that group, by sector. Different quadrants demand different strategic responses, from exploiting reinforcing advantages to identifying vulnerabilities.

## So what — one decision
**Evaluate incumbent strength on BOTH leadership tenure and the capture of incremental value before assuming that durable rankings signal durable competitive advantage.**

## Context → metric → judgment
- **Context:** Which sectors exhibit stable market leaders that still capture new value?
- **Metric X:** Percent of each industry's value creation during **2015–2025** captured by its **five largest companies in 2025**. This is NOT market share of current sales.
- **Metric Y:** Percent of those five firms that have been in the top five **longer than the industry's 1990–2025 median leadership tenure**. Values occur on 20-point increments because denominator is five firms.
- **Compare:** same 0–100% scale with 50% crossing as *editorial* quadrant guides; BCG's original uses continuous scatter and does not establish this exact categorization.
- **Decision:** Low-X/high-Y can indicate incumbent value-capture risk; high-X/high-Y signals persistence plus growth capture. No causal inference follows.

## Observed original vs reconstructed encoding
- **Observed:** BCG Exhibit 2 is a labeled 2D scatter, with 14 discernible labels in the available 499×377 web image; original research mentions 15 industry groupings.
- **Estimate:** We use approximate visually read x/y positions rounded to whole percentage points, ±4 percentage points per coordinate. Labels near each other (communications infrastructure / utilities; energy / financials) are ambiguous. Original point-by-point dataset was not publicly provided.
- **Our edited design:** X=value capture %, Y=long-tenured top-five %, marker=sector, orange=selected examples, otherwise teal. 0–100 axes, 20-point ticks, 50% guidelines; both source-like and neutral palettes. Original layout and labels are **not** certified reproduced.
- **Annotations/labels:** Industry labels offset via CONTEXT.label_offsets for readability, positions derive from CSV values. Background guides are editorial, not original reference values.

## Data provenance and calculations
CSV fields: `industry`, `value_capture_pct`, `tenure_pct`, `uncertainty_pct`, `provenance`, `unit`, `measurement_year`, `value_capture_period`, `population`, `source_ref`. All numeric plotted coordinates have `digitized_estimate`; the 2025 observation date and definitions are reported context. We do not compute underlying market-cap weighted metrics without firm-level Capital IQ observations.

## Data recipe for reuse
1. List top five firms by industry at target date; define consistent universe and market capitalization adjustments.
2. Reconstruct each firm's preceding top-five tenure and compute industry median tenure across the long history.
3. Compute new industry value for base-to-target period and top-five contributions, honoring negative denominators/zero creation cases.
4. Calculate 0–100% top-five value capture and percentage above median tenure; disclose normalization/capping choices.
5. Validate denominator of five, industry coverage, dates and any excluded industries; propagate errors if digitized.
6. Replace CSV and CONTEXT title/axes; modify THEME colors/spacing; render both source and neutral.

## Conditions, counterexamples, limitations
A high share of new value captured by current leaders can coexist with weak real economic value creation; capital gains are not operating cash flows. Startup categories (digital platforms) can reflect cohort formation rather than longevity of existing firms. Non-US-only listings and private companies are outside the study. This is a deliberately **unverified approximate recreation**, not measured exact data or a certified pixel match. Human review pending; reuse only with these caveats.

## Run
`python chart.py --data data.csv --config config.json --theme source --output ../../artifacts/source.png` (or `--theme neutral`).
