# McKinsey — Exhibit 2 — AI adoption maturity stage distribution

## Article: three original sentences
- McKinsey는 GCC 고위 리더 135명의 AI 성숙도를 조사했다.
- 완전하고 일관된 응답 120명 가운데 65%는 업무흐름을 재설계했지만 역할까지 재설계하지 않은 단계에 있었다.
- AI Agent를 중심으로 업무와 역할까지 재설계한 최상위 단계는 16%였다.

## So what
AI Agent 도입 효과를 측정할 때 단순 사용을 넘어 업무흐름과 역할 재설계의 성숙도 전환율을 관리해야 한다.

## Business context → metric → decision
- Original article: Rewiring GCC countries for AI: Realizing value in government (2026-11-23)
- Business context: Rewiring GCC countries for AI: Realizing value in government
- Metric and units: stage, share_pct, unit, provenance, sample_n, survey_period, denominator; see data.csv for source-reported values, period, unit and denominator.
- Comparison and reference: Survey 2026-08-11 to 2026-10-12, reported category ordering.
- Decision: AI 도입을 넘어 조직의 업무흐름을 바꾼 응답 비중은 높지만, 역할까지 재설계한 단계는 16%에 불과하다.
- Insight type: Maturity distribution / bottleneck to role redesign

## Official source facts, observation, interpretation, reuse
- Source fact and observed figure: McKinsey 웹페이지 Exhibit 2의 공식 alt text에서 Early12, Scaled7, Workflow65, Role16 확인. 조사 2026-08-11~10-12, 전체 n=135에서 불완전14명과 불일치1명 제외한 n=120.
- Author interpretation (not demonstrated causality): AI Agent 도입 효과를 측정할 때 단순 사용을 넘어 업무흐름과 역할 재설계의 성숙도 전환율을 관리해야 한다.
- Reuse proposal: Replace values with equivalent numerator, denominator, units and period; retain chart mapping.
- Original figure inspection: Official Exhibit 2 HTML alt description verified; SVGZ graphical file unsupported

## Visual encoding
X=응답자 비중(%) 0~100, Y=단일 범주, 색=Early/Scaled/Workflow/Role, 구간크기=공식값12/7/65/16, 순서=원본 성숙도, 직접값 레이블. 원본 설명상 100% 수평 누적 막대로 편집.
Titles, annotations, palette and background are configurable in config.json. Axis positions, bar heights, percentages and label placement are calculated from data.csv. Do not include source logos or images.

## Public provenance and limitations
- All observations in data.csv are reported public figures, while gaps and shares computed during rendering are derived; unknown values must be missing, not zero.
- Public data, sample and calculation: McKinsey 웹페이지 Exhibit 2의 공식 alt text에서 Early12, Scaled7, Workflow65, Role16 확인. 조사 2026-08-11~10-12, 전체 n=135에서 불완전14명과 불일치1명 제외한 n=120.
- Conditions: Mutually exclusive stages and total ~100%; Same n for every stage; Do not equate maturity with confirmed financial return.
- Counterexample and limitations: 고위 리더 자기보고·비확률 표본이라 GCC 전체 대표성이 없다. 성숙도 단계는 AI ROI 실현의 증거가 아니다. 원본 SVGZ 시각 파일은 접근 불가이므로 원본 색·비율·여백 시각 검증 미완료.

## Step-by-step data_recipe
1. 상호 배타적인 성숙도 단계 정의를 수집한다.
2. 조사 분모와 불완전 응답 제외 기준을 기록한다.
3. 비중합 100%와 단계 순서를 검사한다.
4. CSV의 stage/share_pct, config.json의 THEME/CONTEXT를 바꾼다.
5. 두 테마를 200dpi로 렌더링해 레이블 가독성을 확인한다.

## Usage
```bash
python chart.py --data data.csv --config config.json --theme source --output source.png --dpi 200
python chart.py --data data.csv --config config.json --theme neutral --output neutral.png --dpi 200
```
PNG generated files are outside the immutable Bronze bundle. No user review or model retraining was performed.
