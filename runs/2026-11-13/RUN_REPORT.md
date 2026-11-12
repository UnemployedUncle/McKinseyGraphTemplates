# Consulting Graph Template | 2026-11-13 preparation

Start: 2026-11-13 03:19:11 Asia/Seoul; GitHub commit preparation: 2026-11-13T03:33:22.215+09:00.

## Execution summary

Two new subjects / target three. Bronze cumulative 56, Silver 0, Gold 0. Cumulative historical original reproduction self-verifications 14; today 0. Human approvals today 0. Both new charts unverified and pending. Source and neutral PNGs were rendered and inspected at 200dpi. Five local unit checks and local medallion.py validate passed. No new schedule, no review promotion.

## BCG: The Consumerization of Health Care: How Patients Are Reshaping the Industry

- Official article: https://www.bcg.com/publications/2026/health-care-consumerization-patients
- BCG official press release confirming all ten reported data points: https://www.bcg.com/press/12november2026-patients-to-consumers-reshaping-health-care
- Published Nov 12, 2026; surveyed July-August 2026; 9,914 respondents, ten markets, UAE subset n=354.
- Figure: Health Care Consumerization Index by Country; original picture was NOT inspected. Editorial ranked horizontal bars, not a reproduction.
- Reported index points: China72, India66, UAE63, Brazil62, US56, UK49, Switzerland47, Germany45, France41, Japan36.
- So what: China versus Japan differs by 36 index points. Adapt patient-control, convenience, and digital health propositions by market instead of generalizing from one global mean.
- Unit: six-measure consumerization composite index 0-100, not percent of patients. Data origin and data recipe, limitations and reuse are documented in card.md/record.json.
- Validated: chart.py runs for source/neutral, numeric range 0-100. fidelity_score=null, unverified because original visual was not opened.

## McKinsey: The Achilles’ heel of global trade: Building resilience where it matters most

- Official MGI article: https://www.mckinsey.com/mgi/our-research/the-achilles-heel-of-global-trade-building-resilience-where-it-matters-most
- Published Nov 12, 2026; 2024 UN Comtrade-based import data; 15 economy aggregates of product vulnerability.
- Figure: Exhibit 3; explanatory original chart description states width represents imports and vulnerability layers stack. Graphic pixels/PDF original were NOT viewed; structural reconstruction is unverified.
- Japan36% of imports vulnerable to at least two criteria; Malaysia10%. The share is an economy-specific import denominator, not likelihood of loss or unconditional economic damage.
- 15 published total-exposed % and all-three % plus imports USD billions in CSV. exactly_two_pct = exposure_total_pct - all_three_pct, marked derived (rounding-aware).
- Encoding: import-value-weighted Marimekko/variable-width stacked bars with data-derived x positions. Source/neutral variants rendered and visually inspected.
- So what: prioritize vulnerable trade portfolios by import value, product criticality, supplier options and resilience levers, not exposure fraction alone.
- Validated: 15 records, derived consistency; fidelity_score=null, unverified original pixel comparison.

## Excluded: Bain

No Bain official publicly accessible original quantitative chart with confirmed publication date and nonduplication against current catalog was established from the priority last-7-day search or expanded last-30-day search. Not fabricated.

## Immutability and verification

Original main parent: 804fe213b15d1cc7d025b1eca0ec77f8f006c776.
- bronze/2026-11-13/bcg_health_consumerization_country_index_exhibit_editorial: payload_sha256=56f20e003bd7e7e362e491c60832bc7183422dd763d3e5452c6e3b7b867bb579, human_review=pending
- bronze/2026-11-13/mckinsey_trade_achilles_heel_ex3_import_width: payload_sha256=44ef83ae0885ea0968e7aff70c1c838ab03b0d14a0e50273fc9caecf36bbd5d0, human_review=pending

Records and files: chart.py, data.csv, config.json, requirements.txt, card.md, record.json, validation.json, manifest.json per bundle. Exact SHA256 is in manifests. Catalog was recalculated preserving prior 54 entries and all Silver/Gold states. Delivery flag is false; separate 07:15 run should read this report and prepared.json and not repeat creation. Source/original logos/images/font files are not committed. GitHub Actions result must be verified from the actual run before claiming success.
