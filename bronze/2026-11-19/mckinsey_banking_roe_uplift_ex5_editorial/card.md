# Global Banking Annual Review 2026 — Exhibit 5 — expected change in global banking ROE 2025–2028 (editorial waterfall)

## Article gist (3 sentences)
McKinsey describes structural pressures and opportunities facing the global banking industry. Its Exhibit 5 models 2025 ROE of 13% plus passive tailwinds of 2.3pp and active initiatives of a further 1.4pp by 2028. The increments are modeled contributions, not audited realized returns.

**So what:** Executives should separate externally available tailwinds from the incremental impact of active capital allocation before setting 2028 ROE targets.

## Business context → metric → decision
In a modeled scenario, banking ROE could rise from 13% to 15.3% through passive effects and to 16.7% with an additional 1.4pp active premium. Unit is % ROE; source publication 2026-11-17; underlying data 2025 observed baseline and 2028 modeled scenario. Denominator: Global banking ROE, modeled base. Compare observations only where definitions and periods align. This supports resource prioritization, not causal attribution.

## Data and provenance
| Category | Value | Unit | Provenance |
|---|---:|---|---|
| 2025 ROE | 13 | % ROE | reported |
| Passive uplift | 2.3 | percentage points | reported |
| Active premium | 1.4 | percentage points | reported |

Original chart: Original chart not visually verified (web exhibit accessible in prose only). Created: waterfall. Visual encoding: x=scenario component order (baseline, passive, active, combined final); y=ROE %; starting/full bars and floating contribution bars; colors distinguish base/increments/final; direct labels and connector rules. Layout, colors, labels, font and chart title are set in config.json THEME/CONTEXT; derived locations use values in data.csv.

## Published data and method
Source: https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/global-banking-annual-review (published 2026-11-17, checked 2026-11-19). Underlying source context: 2025 observed baseline and 2028 modeled scenario. The +2.3pp and +1.4pp values describe modeled average scenarios, not realized sector performance. The apparent 16.7% is derived by addition; source warns that rounded components can differ slightly. No bank-level distribution or confidence interval is available; neither increment is guaranteed. Avoid equating global modeled returns with returns to an individual bank. Explicit unpublished data, weights and sample details remain undisclosed.

## Reusable data_recipe
1. Record the historical 2025 ROE baseline and set the same denominator of equity in all periods.
2. Extract passive and active modeled ROE changes in percentage points, not relative percent growth.
3. Calculate intermediary scenario 13 + 2.3 = 15.3 and 2028 active scenario 15.3 + 1.4 = 16.7.
4. In a waterfall, render increments from the prior total and the final total from zero.
5. Distinguish observed 2025 baseline from conditional modeled 2028 increments; verify assumptions before adoption.

## Message conditions and counterexamples
- The +2.3pp and +1.4pp values describe modeled average scenarios, not realized sector performance.
- The apparent 16.7% is derived by addition; source warns that rounded components can differ slightly.
- No bank-level distribution or confidence interval is available; neither increment is guaranteed.
- Avoid equating global modeled returns with returns to an individual bank.

**Counterexample:** A higher displayed value alone does not establish causation, eliminate composition bias or apply to different populations. Decisions require matched definitions and external operational evidence.

## Reuse and verification
Edit data.csv, config.json THEME.source / THEME.neutral and CONTEXT; run `python chart.py --theme source --output artifacts/source.png` and neutral analog. Render success, original fidelity and human review are separate statuses. **Status:** unverified (fidelity_score=null); human_review=pending. Source chart image unavailable for direct visual comparison; reconstructed an editorial bridge of publicly reported numbers.
