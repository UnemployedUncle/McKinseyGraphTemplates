# McKinsey | Second-line risk FTE distribution (Exhibit 1, partial)

## Article in three original sentences
McKinsey describes how banks can scale agentic systems across multiple risk disciplines through shared data, approved models and human oversight. Exhibit 1 compares the typical staffing distribution across 13 second-line risk and compliance functions. The article associates each function with possible AI use cases but does not report measured adoption levels for them.

## One So what
Banks planning cross-domain AI transformation should first map where second-line risk resources sit, while prioritizing workflows by value and control requirements rather than FTE share alone.

## Fact → observation → interpretation → reuse
**Fact:** Official article 2026-11-04, Exhibit 1. The largest reported groups are credit risk 27%, financial-crime compliance 16%, and operational/nonfinancial risk 13%. **Observation:** top three comprise 56 percentage points; the 13 displayed values add to 99%, a rounding remainder. **Interpretation:** exposure to automation differs from staffing distribution. **Reuse:** rank process capacity before selecting cases, then separately measure complexity, throughput and measurable achievable benefit.

## Data and decision chain
Metric: percent of **second-line risk/compliance FTEs**, not employees of the entire bank. Period: typical distribution stated in a Nov 2026 report; source observation period and denominator headcount **not disclosed**. Population: large international/global banks; sample count **not disclosed**. Numerator: FTEs in category; denominator: second-line risk and compliance FTEs. Decision: select high-capacity functions for deeper process discovery but do not infer potential cost savings from percentages alone.

## Insight and visual grammar
Chart family: horizontal rank bar (quantitative left panel only). X: FTE distribution in percent, 0–30; Y: risk service; fill: major categories emphasized, other categories neutral; marks equal thickness. Descending ranking and direct right-hand labels minimize search time. Original Exhibit 1 also places textual AI use case examples next to bars; the separate qualitative panel is **not reproduced**. This is a **partial editorial reconstruction**, not validated original reproduction. Source colors, labels and geometry could not be independently inspected because the official SVGZ was inaccessible; color choices are neutral design decisions.

## Source, provenance, calculations
Official URL: https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/the-ai-enabled-risk-function-of-the-future . Exhibit 1 describes all 13 percentages as typical distribution. All values are `reported`; top-three 56 and total 99 are `derived` (sum). No inferred missing 1% category is inserted. The article lists specific AI use cases, but the graphic is not evidence of their adoption rate. Units and rounded shares were reviewed.

## Reuse data_recipe
1. Identify the second-line organizational perimeter, include/exclude contractors and shared services consistently.
2. Obtain `team_id`, `risk_service`, `fte_equivalent`, `snapshot_date`, `bank_size_group`.
3. Aggregate FTE equivalents by mutually exclusive service categories, reconcile full denominator and explain multi-service allocations.
4. Compute percentages using the same denominator and date; round only for display, preserve raw values for calculation.
5. Sort categories descending and choose labeled horizontal bars; test long category text and direct data labels.
6. Add separate efficiency, control-quality, exception-volume and implementation difficulty data before recommending automation priorities.

## Message conditions / counterexamples / limitations
If local FTE allocations differ materially, the published ranking is not representative. Risk appetite and regulatory expectations may make some smaller teams more important than larger ones. Sum of rounded bars is 99%; this is not proof of missing staff. Because original SVGZ was not visually opened, fidelity_score is null and no original-match claim is made.

## Usage
`python chart.py --data data.csv --config config.json --theme source --output source.png`. For a new institution, replace csv and chart titles/thresholds/colors in config, then recalculate denominators.
