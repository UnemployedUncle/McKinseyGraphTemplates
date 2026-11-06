# McKinsey | Latin American insurance premium growth, editorial article subset

## Article in three original sentences
McKinsey reports that Latin America's insurance market remains profitable but that region-wide premium growth slowed in 2025. Between 2024 and 2025, Colombia, Mexico and Chile posted reported growth rates of 9%, 11%, and 12% at fixed exchange rates. The article discusses how AI-enabled distribution and operational productivity might unlock growth, but does not claim these three growth results were caused by AI.

## One So what
Insurance executives should avoid extrapolating the 4% regional aggregate to each market and should prioritize country-level evidence when selecting AI growth initiatives.

## Fact → observation → interpretation → reuse
**Reported:** 2025 Latin America aggregate growth of around 4%; 2024–25 Colombia 9%, Mexico 11%, Chile 12%. **Observed:** The selected markets outperformed the regional aggregate. **Interpretation:** The regional market slowdown conceals strong local growth, which may matter for expansion prioritization. **Reuse proposal:** Build comparable country-level bars with a regional benchmark, then check regulatory and mix effects.

## Data and decision chain
Business: insurers' geographic growth and investment focus. Metric: year-over-year premium growth; unit %, 2024–25, constant exchange rates. Denominator: prior-year premium base within each geography; region aggregate uses regional aggregate premium base rather than mean of country growth rates. Comparison: three markets vs region-wide aggregate. The article gives no market-specific numerical sample or premium volume table for this subset. Values refer to the same broad period but do not establish the same product mix. Do not use 4% as an unweighted country mean. Source reporting date 2026-11-05; underlying regulator data 2024–25. Nominal vs real price adjustment not disclosed; fixed FX is not inflation-adjusted.

## Insight type and visual grammar
Insight: benchmark gap/comparative ranking. X: percent growth, Y: selected geographies, descending bars bottom-to-top, source theme shades country blue and highlights region aggregate dark navy. Each bar has a numerical label and shared x scale with sparse grid lines. Width represents growth, not share of total; these independent rates do not sum to 100%. Edited presentation designed from prose numbers, **not a reproduction of McKinsey's Exhibit 1**, which compares multiple measures.

## Public evidence, provenance and calculation
All four data rows are `reported`. Sources: McKinsey Global Insurance Pools and national regulators, as cited in the article. The article describes constant exchange rates. Formula to reuse: premium growth = (premiums_t / premiums_t-1 - 1) × 100 after harmonized FX conversion. Other business lines and all model coefficients are not disclosed in the source article text used here.

## Stepwise reusable data_recipe
1. Collect actual written premiums by geography and year, on a matched accounting/product basis. 2. Apply a common FX base year and confirm perimeter. 3. Compute per-market growth from adjacent-year values. 4. Compute a weighted regional aggregate from total premiums, not the average of country rates. 5. Sort market values, add the regional benchmark and source annotation. 6. Replace `data.csv`, `THEME` and `CONTEXT`; compare 2024–25 values with chart.

## Message conditions and counterexamples
Differences in insurance product mix, country inflation and changing pension regulation can dominate headline growth. A country's 12% premium growth is not proof of above-average profit or underwriting quality. Fixed FX does not remove inflation effects. No causal link to agentic AI adoption is supported by these premiums. Original chart has not been visually reproduced: `fidelity_score=null`.

## Usage
`pip install -r requirements.txt` then `python chart.py --theme source --data data.csv --config config.json --output source.png`; use neutral theme for reusing layout on another comparable geography-level growth dataset.
