# How Countries Can Strengthen Their Energy Security — Exhibit 2 related reported narrative (editorial approximate-share bar; original chart not inspected)

## Article gist (3 sentences)
BCG frames energy import dependence as a strategic vulnerability amid geopolitical and market disruptions. The public article states that about 60% of OECD countries import more than half of their energy. The publication does not provide exact country-level data or a precise measurement year in the passage used.

**So what:** Energy-security strategy should identify exposure to imports at the national level before choosing diversification, domestic capacity, or resilience policies.

## Business context → metric → decision
Approximately 60% of OECD countries depend on imports for more than half their energy. Unit is approx % of OECD countries; source publication 2026-11-18; underlying data Unpublished in excerpt; article published 2026-11-18. Denominator: OECD countries; n and survey year undisclosed. Compare observations only where definitions and periods align. This supports resource prioritization, not causal attribution.

## Data and provenance
| Category | Value | Unit | Provenance |
|---|---:|---|---|
| Import >50% of energy | 60 | approx % of OECD countries | reported |
| Others / at most 50% | 40 | approx % of OECD countries | derived |

Original chart: Not verified (original exhibit image inaccessible). Created: stacked_share. Visual encoding: x=share of OECD countries 0–100%; one horizontal stacked bar; teal=high import dependence, neutral=others; approximate value labels; no artificial country-level slices. Layout, colors, labels, font and chart title are set in config.json THEME/CONTEXT; derived locations use values in data.csv.

## Published data and method
Source: https://www.bcg.com/publications/2026/countries-strengthen-energy-security (published 2026-11-18, checked 2026-11-19). Underlying source context: Unpublished in excerpt; article published 2026-11-18. 60% is a rounded estimate, not exact observed country count. 40% is derived as an approximate complement and not separately reported. Missing country denominator, date and import-definition details prevent precision or confidence bounds. No inference about energy volume shares, import values or individual country risk from this aggregate count. Explicit unpublished data, weights and sample details remain undisclosed.

## Reusable data_recipe
1. Set the OECD country membership and measurement year before collecting country-level energy balances.
2. Compute net-import dependence consistently: imports, exports, production and total energy supply definitions must align.
3. Count countries above the 50% threshold, with the denominator explicitly known.
4. Label rounded aggregate shares as approximate; compute a residual only as an approximate complement.
5. Use a 100% stacked bar for an editorial summary; do not present it as the source's original exhibit.

## Message conditions and counterexamples
- 60% is a rounded estimate, not exact observed country count.
- 40% is derived as an approximate complement and not separately reported.
- Missing country denominator, date and import-definition details prevent precision or confidence bounds.
- No inference about energy volume shares, import values or individual country risk from this aggregate count.

**Counterexample:** A higher displayed value alone does not establish causation, eliminate composition bias or apply to different populations. Decisions require matched definitions and external operational evidence.

## Reuse and verification
Edit data.csv, config.json THEME.source / THEME.neutral and CONTEXT; run `python chart.py --theme source --output artifacts/source.png` and neutral analog. Render success, original fidelity and human review are separate statuses. **Status:** unverified (fidelity_score=null); human_review=pending. Official narrative value checked, but original BCG Exhibit 2 image was not visually available; deliberately editorial, with derived rounded complement.
