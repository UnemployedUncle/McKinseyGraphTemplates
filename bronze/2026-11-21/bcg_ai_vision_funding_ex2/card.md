# BCG | Clear AI ambition and transformation funding (Exhibit 2)

## Article summary (three sentences)
BCG and the Global Marketing and Media Alliance surveyed about 60 CMOs across sectors in May–July 2026. The C-suite is shifting AI discussions beyond efficiency toward growth and operating-model change. CMOs with a clear, articulated AI vision report better access to AI transformation funding than peers without a clear vision.

**So what:** Frame AI vision clarity as a funding-readiness hypothesis to test, not an established causal effect.

## Evidence chain
- **Fact:** Exhibit 2 reports clear-vision responses 54% "Have what I need", 8% "Have more than I need", 38% "Need a lot more". Without a clear vision: 37% "Have what I need", 33% "Need a little more", 30% "Need a lot more".
- **Derived comparison:** Sufficient-or-more funding among clear-vision CMOs = 54 + 8 = 62%; no-clear-vision respondents reporting sufficient funding = 37%; difference = 25 percentage points, not 25%.
- **Context / metric:** CMO perceived budget adequacy by AI-vision clarity; unit is survey respondent %, within each distinct clarity subgroup, May–July 2026; not spending levels or actual AI return. Subgroup n, question wording and uncertainty intervals are not disclosed in the web article.
- **Interpretation:** A clearly expressed ambition accompanies better perceived funding access; alternative factors include larger budgets, organizational maturity, or selection effects.

## Visual encoding
- **Original observed:** two horizontal bands, three framed mini-bars per band, percentages inside, different accent colors, direct response captions; no numeric axes or legend. Each mini-bar has a 100% container and value-proportional fill.
- **Recreated:** y = clarity group (original order); x = three item slots (source order); fill length = response %, hue = group, prominent direct data labels; original caption wording is preserved. Empty area up to 100% is meaningful for *each item*, not a 100% stacked composition. Title, space, color, margins and annotation are configurable.
- **Insight type:** distribution-within-segment / relative adequacy / benchmark comparison. Do **not** compare the three slots as if each category had matching definitions across the groups: the second categories differ.

## Data & provenance
BCG/MMA CMO survey, approximately 60 respondents across sectors, May–July 2026; published Nov 20, 2026. All six data.csv entries are `reported`. 62% and +25pp are `derived` in analysis only, not falsely presented as published chart rows. No synthetic values, digitizing or assumed subgroup sizes. Values sum to 100% in each group.

## data_recipe for reuse
1. Define the two contrasting segment groups and their within-group respondent bases.
2. Collect category response shares, exact labels, sequence, survey period, denominator and provenance; do not force unmatched category labels to match.
3. Check each group's category shares total 100% within rounding tolerance.
4. Set `CONTEXT.group_order`, `CONTEXT.group_titles` and message-specific caption; edit `THEME` only for source/neutral palettes.
5. Supply new CSV to `chart.py`; render both variants and visually inspect all six labels.

## Message conditions, counterexamples, limits
The claim requires consistent funding question definitions and comparable CMO subgroups. The survey does not establish whether vision clarity causes funding access, whether funded projects deliver value, or whether this applies to all firms. Small, non-random CMO survey and unknown subgroup counts limit generalization. A counterexample would be highly funded but vague AI programs or a clear AI strategy lacking budget. Avoid implying a probability improvement for an individual executive.

## Usage
`python chart.py --theme source --output ../../artifacts/source.png` (and `neutral`). Modify only `data.csv`, `config.json` for structure reuse.
