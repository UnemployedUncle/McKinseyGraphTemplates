# Consulting Graph Template — 2026-11-15 preparation

- Local start (Asia/Seoul): 2026-11-15 03:15:37 +09:00
- Target: 3 firms, new Bronze: 2 (BCG, McKinsey). Bain: no verified recent nonduplicate accessible original quantitative chart.
- Current baseline was 58 Bronze / 0 Silver / 0 Gold; after commit expected 60 / 0 / 0.
- Cumulative original self-fidelity verified: 15 if BCG original match is accepted; today's BCG 4.57/5, McKinsey unverified/null. Historical agent evaluation is not human approval.
- bronze/2026-11-15/bcg_canada_black_friday_budget_ex1: BCG Nov 12 2026; Exhibit 1 source examined; descending waterfall, values 530 / 200 / 130 / 80 / 70 / 50 CAD; low-ticket share 62%.
- bronze/2026-11-15/mckinsey_us_soybean_use_mix_article_editorial: McKinsey Nov 11 2026; soybean use 57% crush and 35% exports in 2026/27, with ±5pp earlier mix inferred; editorial grouped bars, original SVGZ not rendered.
- Local Python render tests: source and neutral PNG at 200dpi for each; 4 generated PNG, directly inspected. Dedicated semantic checks: 5 passed. Full repository tests and Actions to be confirmed separately after commit.
- All new human_review=pending; no Silver/Gold, no model retraining.
- Screenshots/reports from third parties, branding files, fonts, secrets, and generated PNG are not committed as Bronze payloads.

## Confirmed GitHub Actions evidence
- Code commit: 7f7c9bdc1e6d1296f318e15d2bc9d47ae2cf4845
- Workflow run: https://github.com/UnemployedUncle/McKinseyGraphTemplates/actions/runs/43626645416 — completed/success.
- Artifact: https://github.com/UnemployedUncle/McKinseyGraphTemplates/actions/runs/43626645416/artifacts/14126202636 — chart-previews-and-smoke-tests.
- CI checks: unit tests successful; medallion validate successful; render_all successful; artifact upload successful.
- Both source/neutral output variants rendered locally at 200dpi and directly inspected; all exact code/data/config local SHA256 hashes matched committed manifest files before upload.
- New BCG self-fidelity verified 4.57/5 (original screenshot inspected); McKinsey editorial reconstruction unverified/null. Both are human_review=pending.
- No notification during preparation; 07:15 delivery should read prepared.json and this report, and must not repeat research or commit.
