# McKinsey — AI shoppers value less friction across product research

## Source and provenance
- Publication: Who wins when AI does the shopping? New evidence on agentic commerce
- Official URL: https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/who-wins-when-ai-does-the-shopping-new-evidence-on-agentic-commerce
- Published: **2026-10-28**; retrieval: **2026-10-29T07:18:48.245871+09:00**
- Figure reference: **Exhibit 7 (three reported benefit items)**. Original figure pixels were not downloaded or persisted.
- Visualization status: **unverified**; original exhibit was not visually available for direct comparison. The chart here is an analytical redesign of reported data, not an exact original reproduction.

## Article summary (3 sentences)
2026년 6월 글로벌 11개국 AI 쇼핑 이용자 약 9,645명(가중 설문; 해당 문항)의 상위 2개 동의 응답 비중을 비교한다. 선택지를 좁혀 준다 81%, 스크롤·클릭을 줄인다 80%, 시간을 아낀다 79%가 원문에 제시됐다. 원문은 에이전트 커머스가 제품 발견에서 구매까지 확장되고 있음을 설명한다.

## One So what
**AI 쇼핑 이용자의 79~81%가 선택지 축소·클릭 감소·시간 절약에 동의하므로, 상품검색 에이전트의 우선 KPI는 개인화보다 탐색 마찰 감소를 포함해야 한다.**

## Context → metric → decision
- Business context: 2026년 6월 글로벌 AI 쇼핑 이용자들의 제품 탐색시 AI의 효용 응답
- Values / unit: 81, 80, 79 (percent)
- Period: 2026-06
- Denominator: AI shoppers in 11 markets; weighted top-two-box agreement (n=9,645)
- Source-backed observation: categorical values reported in source text (not derived from raw microdata).
- Recommended decision (agent interpretation): focus discussion on AI search quality and user effort reduction.

## Insight and visualization anatomy
- Main insight type: **comparison**. Chart type: **horizontal_bar**.
- Encoding: x=Top-two agreement (%), y=benefit, color=single emphasized benefit; horizontal bars from zero; each has direct labels. No dual/log/truncated axis. Title states an action-oriented implication.
- Original chart structure and annotation positions: **not independently verified**; source theme is a reconstruction-inspired style, not the source's exact design.
- Key readability choice: numerical direct labels without a secondary axis.
- Interpretation risk: 설문 자기보고식 동의율과 실제 행동·절감시간을 동일시할 수 없다. 여러 항목은 상호배타적이지 않다. 특정 효용 지표 순위가 역전되면 So what 및 강조를 수정한다.

## Data source and modeling
- Data basis: published source article; population and sampling detail: AI shoppers in 11 markets; weighted top-two-box agreement (n=9,645).
- Source survey/model: McKinsey Agentic Commerce Consumer Survey, June 2026; 11 markets; weighted responses.
- Unreported microdata, per-category sample, regression, or data weighting formula: **not independently available**.
- Each CSV row contains `reported` values. No synthetic or visually digitized points.
- Data recipe: 관측 단위 respondent × benefit_item. survey_id/respondent_id/market/age/tool_used/top2_agree/weight를 수집한다. 시장·모집단과 질문지를 통일한 뒤 결측·비응답을 제외하고 항목별 유효 응답자 및 가중치를 확인한다. 각 benefit_item의 Top-2-box 비율=100 × Σ(weight × top2_agree)/Σ(weight). 표본 9,645는 해당 전반의 조사집계이며 항목별 정확한 유효 응답자는 미공개. 이 값은 동의 정도이지 실측 시간절감이나 전환율이 아니다.

## Message validity and disconfirming observations
설문 자기보고식 동의율과 실제 행동·절감시간을 동일시할 수 없다. 여러 항목은 상호배타적이지 않다. 특정 효용 지표 순위가 역전되면 So what 및 강조를 수정한다.

## Reuse
- Edit palette/layout in `config.json` (`THEME.source` or `THEME.neutral`); title/axes/series in `CONTEXT`. Edit long-form values in `data.csv`.
- Run: `python chart.py --theme source --data data.csv --config config.json --output output.png`
- Example reuse: trading team agent usability survey with comparable option-level adoption responses.
- Fidelity score: **null** (`unverified`). Rendering and semantic tests are separate from visual-source fidelity.

## Source-visual disclaimer
원문 Exhibit 7의 일부 본문에 보고된 값을 사용한 편집형 비교 차트; 원본 그림 형태 미확인.
