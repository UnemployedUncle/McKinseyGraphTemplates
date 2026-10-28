# BCG — Pension portfolios invest far below permitted alternative caps

## Source and provenance
- Publication: Putting Africa's Capital to Work
- Official URL: https://www.bcg.com/publications/2026/putting-africas-capital-to-work
- Published: **2026-10-27**; retrieval: **2026-10-29T07:18:48.245871+09:00**
- Figure reference: **Pension allocation vs regulatory ceilings (article quantitative discussion; not a direct exhibit reproduction)**. Original figure pixels were not downloaded or persisted.
- Visualization status: **unverified**; original exhibit was not visually available for direct comparison. The chart here is an analytical redesign of reported data, not an exact original reproduction.

## Article summary (3 sentences)
BCG는 아프리카 연기금과 보험자산이 약 0.9조 달러 규모로 늘었지만 대체투자 비중은 매우 낮다고 분석한다. 남아공·나이지리아·케냐·가나에서 법정 상한과 실제 배분 사이의 차이가 큼을 본문 수치로 보여준다. 투자자 역량·실적 신뢰·외환 및 펀드 구조 등 비규제적 장애가 중요한 원인 후보라고 제시한다.

## One So what
**남아공·나이지리아·케냐·가나의 연기금 대체투자 실배분은 법정 상한에 현저히 못 미치므로, 투자 확대의 제약을 규제 상한만으로 설명하기 어렵다.**

## Context → metric → decision
- Business context: 2026년 아프리카 주요국 연기금의 대체투자 실배분율과 법정 투자상한의 괴리
- Values / unit: 0.8, 15.0, 1.7, 10.0, 0.7, 10.0, 1.1, 25.0 (percent)
- Period: 2026 report (observation years vary by national source)
- Denominator: National pension AUM; actual and cap vary by eligible asset category
- Source-backed observation: categorical values reported in source text (not derived from raw microdata).
- Recommended decision (agent interpretation): focus discussion on actual portfolio constraints beyond formal regulatory limits.

## Insight and visualization anatomy
- Main insight type: **gap**. Chart type: **dumbbell**.
- Encoding: x=pension AUM share (%), y=country/asset-class, color/marker fill=actual vs legal ceiling; horizontal connectors and direct labels. No dual/log/truncated axis. Countries follow a fixed, non-ranked order.
- Original chart structure and annotation positions: **not independently verified**; source theme is a reconstruction-inspired style, not the source's exact design.
- Key readability choice: numerical direct labels without a secondary axis.
- Interpretation risk: 규제 상한은 실제 적절 배분의 목표가 아니다. 국가별 적격 자산 정의·연도·투자 가능성·상품 공급·수탁규정이 다르다. 자산 정의를 일치시키거나 실배분율이 상한과 비슷해지면 현재의 gap 메시지를 수정한다.

## Data source and modeling
- Data basis: published source article; population and sampling detail: National pension AUM; actual and cap vary by eligible asset category.
- Source survey/model: BCG report analysis; country pension and regulatory source details not disclosed for each statistic in article excerpt.
- Unreported microdata, per-category sample, regression, or data weighting formula: **not independently available**.
- Each CSV row contains `reported` values. No synthetic or visually digitized points.
- Data recipe: 관측 단위 country × pension_fund × eligible_asset_category × period. 연기금 통계, 감독당국의 현재 규제표와 각 펀드별 PE/VC/alternatives 배분 현황을 수집한다. 기간/asset class 정의를 맞추고, actual_share=100×eligible_investment_value/pension_AUM, gap_pp=ceiling_pct−actual_share를 계산한다. 남아공·나이지리아는 PE, 케냐는 PE/VC, 가나는 대체투자 광범위 정의로 직접 국가 순위를 매길 때 조심해야 한다. 이 차이가 규제 완화만으로 메워진다는 주장은 금지한다.

## Message validity and disconfirming observations
규제 상한은 실제 적절 배분의 목표가 아니다. 국가별 적격 자산 정의·연도·투자 가능성·상품 공급·수탁규정이 다르다. 자산 정의를 일치시키거나 실배분율이 상한과 비슷해지면 현재의 gap 메시지를 수정한다.

## Reuse
- Edit palette/layout in `config.json` (`THEME.source` or `THEME.neutral`); title/axes/series in `CONTEXT`. Edit long-form values in `data.csv`.
- Run: `python chart.py --theme source --data data.csv --config config.json --output output.png`
- Example reuse: commercial credit utilization versus policy ceilings, provided definition and periods are comparable.
- Fidelity score: **null** (`unverified`). Rendering and semantic tests are separate from visual-source fidelity.

## Source-visual disclaimer
BCG 본문에 보고된 국가별 4쌍으로 새로 설계한 덤벨 그래프; 공식 Exhibit 재현 아님.
