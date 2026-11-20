# McKinsey | Modelled displacement of automation-adopted work hours (Exhibit 1 related)

## Article summary (three sentences)
McKinsey's November 20, 2026 economic mobility report investigates the unequal occupational effects of AI and other automation by 2035. The analysis maps work activity estimates onto occupational distributions from US labor statistics and surveys. It distinguishes task automation that reduces labor demand from automation that augments work and raises productivity.

**So what:** Before designing reskilling investments, separate automation adoption from labor displacement and target occupational transitions where displacement exposure is greater.

## Evidence chain
- **Reported model outputs:** projected displaced share among automation-adopted work hours: Latino 41%, Black 40%, White 37%, Asian 36%; all reported in the article's Exhibit 1 discussion.
- **Metric:** modelled percentage of automation-adopted work hours within each group that could reduce labor demand; 2035 horizon using today's occupation distribution. This is not the percent of all worker hours, the share of jobs lost, nor an observed labor outcome.
- **Derived contrast:** Latino minus Asian = 5 percentage points; group differences are small in aggregate but can compound with occupational concentration.
- **Calculation/data source:** McKinsey Global Institute automation adoption and labor-demand model linked to BLS and American Community Survey activities. Model considers work-hours displacement versus alternative absorption pathways (new demand, overwork alleviation, new activities, regulatory barriers). Public piece lacks row-level sample or error intervals; do not invent them.
- **Interpretation:** Differences reflect occupational task distribution, not intrinsic worker attributes or deterministic job loss.

## Visual encoding
- **Original image not visually confirmed:** official SVGZ link could not be opened for graphic comparison. Article and Exhibit 1 caption were accessible; structure remains unknown.
- **Editorial design:** horizontal bar order 41,40,37,36, x = displaced share of automation-adopted hours %, y = workforce group; highlight two groups mentioned in narrative, muted reference bars, numeric end labels, x starts at zero. Text explicitly distinguishes modeled from observed. Not a faithful original reconstruction.
- **Insight type:** ranked cross-group model comparison.

## Data provenance and recipe
Four `reported` values from the November 20, 2026 article, modeled horizon 2035, underlying occupational/work-hour data from BLS/ACS. No fabricated values. Define groups and consistent denominator, collect rates with provenance, order by rate only if story calls for ranking, highlight selectively, preserve projected label, and validate 0≤value≤100; render source/neutral. To reuse, change CSV `group`, `value_pct`, `denominator`, `period`, and `CONTEXT`, preserving same unit across rows.

## Message conditions / counterexamples / limits
Assumes McKinsey's modelled adoption and baseline workforce mix. Labor-market transitions, new jobs, policy, adoption speed, future occupation changes and geographic labor supply may alter realized outcomes. A higher modeled displacement share among automated hours is not proof of job losses. Different denominators (all hours, automated hours, workers, jobs) invalidate comparison. No source-image fidelity rating can be assigned.

## Usage
`python chart.py --theme source --output ../../artifacts/source.png`; repeat for `neutral`. Actual artwork is newly generated, not copied from the report.
