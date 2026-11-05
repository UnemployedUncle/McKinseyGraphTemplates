# BCG | Household energy-bill waterfall (Exhibit 1)

## Article in three original sentences
BCG argues that an integrated energy offering can compete on the complete household bill, not only electricity unit price. Its scenario illustrates self-generation and demand flexibility as sequential savings levers. The investment proposition depends on price risk, household equipment and retailer economics.

## One So what
Energy retailers should test bill-level offers and monetizable flexibility separately, rather than equating modeled gross household savings with retailer margins.

## Fact → observation → interpretation → reuse
**Fact:** Published 2026-11-05. In Exhibit 1 a typical European household starts at EUR 3,500 per year; the figure gives two optimized endpoints EUR 1,400 (60% lower) and EUR 700 (80% lower). Initial modeled bill splits EUR 1,100 base appliances, EUR 1,400 heating/cooling, EUR 1,000 EV charging; intermediate steps are sourced from chart labels. Data observation: steps sum to EUR 2,100 before the first checkpoint and EUR 700 thereafter. Interpretation: household value extends beyond the power supply contract. Reuse recommendation: compare future scenarios as savings bridges only after verifying mutually exclusive components.

## Data and decision chain
Business context: European residential energy bundles. Metric: annual EUR per household, nominal/real price base **not disclosed**, source model rather than realized bill. Reference period: article 2026-11-05; model input period **not disclosed**. Denominator: one modeled typical household, not a sampled household average. Comparison: total 3,500 → optimized 1,400 → full 700. Decision: investment prioritization of solar/battery, off-peak use, grid export; ignore potential capital costs only with an explicit caveat.

## Insight and visual grammar
Type: waterfall/bridge with baseline stacked components. X: ordered interventions, Y: EUR/year; color: baseline energy components versus savings versus remaining bill; width constant; connecting hairlines link cumulative levels. Sequence is causal scenario order, **not category sorting**. Large savings blocks get internal labels; small blocks get external labels. Two checkpoints use darker emphasis. Axes deliberately spare, direct data labels and 60%/80% guide annotations above checkpoints. Color/spacing/title/notes are isolated in config.json.

## Source, provenance and method
Official URL: https://www.bcg.com/publications/2026/energy-retailers-cut-household-bills ; original: Exhibit 1 (chart graphic linked on page). All rows are `reported` values transcribed from the official figure. `derived`: cumulative remaining bill and savings shares, computed in code. Numerical sample and modeled price assumptions were not published in the article. Savings are **potential** and do not include equipment investment costs. Independent full-model audit unavailable.

## Reuse data_recipe
1. Define one account/household/project and a single annual cost denominator in consistent currencies/price year.
2. List baseline cost segments with non-overlapping ledger categories and reconcile to the baseline total.
3. Assign each initiative an incremental net saving after previous actions, preventing double counting.
4. Aggregate savings sequentially, calculate remaining bill, and compare checkpoints against supplied totals.
5. Render waterfall; update captions to distinguish forecast/observed, and check negative remaining bills.
6. Sensitivity-test initial prices, capex/financing, and adoption/availability before using for an investment decision.

## Message conditions, counterexamples and limitations
Only holds for the **modeled** household and full combination of technologies/market access. If capex, maintenance and financing exceed gross bill savings, economic value is smaller; if solar output, bidirectional availability or hourly pricing differs, the 60–80% range changes. The graphic does not establish retailer profitability or observed realized outcomes.

## Usage
`python chart.py --data data.csv --config config.json --theme source --output source.png` (or `--theme neutral`). Settings and data can be replaced without modifying chart code; validate step arithmetic first.
