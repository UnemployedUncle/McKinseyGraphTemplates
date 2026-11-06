# BCG | Market leader longevity (Exhibit 1)

## Article in three original sentences
BCG studied roughly 2,000 highly valued firms across 15 sector groups over 35 years. Across sectors, the median measure of top-ten turnover fell from 24% in 1990–2004 to 13% in 2005–2025. Long-held valuation leadership can arise from durable capabilities or from industry-specific pauses between disruptions.

## One So what
Corporate strategists should test whether incumbents still capture new industry value rather than treating lower leader turnover as proof of enduring competitive advantage.

## Fact → observation → interpretation → reuse
**Reported:** 24% vs 13% cross-industry median giant churn in earlier/later periods; 10 of 15 industries declined, and BCG's analysis includes the 2,000 most valuable US-listed firms at five-year intervals. **Observed:** Exhibit 1 plots sector-level median giant churn for the 1990–2004 x-axis and 2005–2025 y-axis against the y=x reference. **Interpretation:** Lower churn signals stronger leader persistence, not necessarily stronger value capture. **Reuse proposal:** Map baseline and latest portfolio concentration on the same coordinates to surface domains with rising entrenchment.

## Data and decision chain
Business: corporate strategy and industry resilience. Metric: `giant_churn`, share of top-ten combined market capitalization represented by firms absent from the prior five-year top ten, unit percent, not percentage-point growth. X: median of earlier period; Y: median of later period, each within sector. Comparison: equality line y=x. The original published exact sector coordinates are unavailable in extracted article text: **15 x/y positions in `data.csv` are digitized estimates from a 499x338 screenshot, with assumed reading tolerance ±2 percentage points per axis**. The 24%, 13% aggregate figures are reported but not plotted as sector points. Original sample coverage: US-listed top 2,000 by capitalization, excludes private and non-US-exclusive listings. Country mix and market-cap weighting are not public as row-level data. Nominal/real not relevant to percentage shares.

## Insight type and visual grammar
Insight: relationship/comparative positioning. X=historical giant churn; Y=recent giant churn, square dots, sector label at each dot, a y=x parity reference, soft green below parity (increased leadership lock-in), cream above parity (decreased lock-in). Fixed axes and label offsets are exposed in `config.json` and `data.csv`. Original proportions, font, wordmark are not reproduced exactly. `source` approximates muted green palette; `neutral` uses grayscale-blue.

## Public evidence and computation
Article published 2026-11-06. Exhibit 1 image was opened at its official BCG asset link; values estimated visually without OCR. We do not claim the approximate points are BCG published numbers. Source data set: S&P Capital IQ via BCG study; sample method described in article. Formula for exact re-creation: top-ten new entrants' combined cap / combined cap of all top ten * 100, sector and five-year window; medians across windows. 1990–2004 and 2005–2025 have distinct duration; definition follows article. Independent access to the actual company-level records was not available.

## Stepwise reusable data_recipe
1. Collect a time series of entity IDs and market values within each sector, with five-year-aligned snapshots. 2. Define top ten each snapshot, identify firms absent five years before. 3. Calculate newcomer-capitalization share relative to current top ten. 4. Aggregate the specified historical and recent windows by median. 5. Compute parity y=x and annotate sectors; estimate uncertainty for missing source years. 6. Render with `THEME.source` or `THEME.neutral` and update `CONTEXT` appropriately.

## Message conditions and counterexamples
The inference requires stable top-ten definitions, exchange listing coverage and comparable sectors. Lower churn can reflect consolidated platform structures, but can also mask declining profitability or weak new-value capture. Sector boundary changes, newly listed firms, and mergers can alter the metric; the digitization error can reverse very near-parity dots. No causality claimed.

## Usage
`pip install -r requirements.txt`, then `python chart.py --data data.csv --config config.json --theme source --output source.png`. Set `--theme neutral` for a reusable neutral design. Replace data/labels/settings for another comparable two-period concentration metric; derived label positions remain in data, not hard-coded by sector in Python. Outputs are outside the immutable Bronze bundle.
