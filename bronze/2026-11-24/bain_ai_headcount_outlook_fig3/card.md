# Bain — Figure 3 — AI-related headcount expectations by function, Q1 vs Q3 2026

## Article: three original sentences
- Bain의 2026년 AI 준비도 설문은 기업들이 AI 활용 이후 인원 계획 전망을 재조정하고 있음을 보여준다.
- 소프트웨어 개발 인력 증감 전망은 Q1 -2%에서 Q3 +10%로 바뀌었다.
- 고객 서비스는 여전히 감소 전망이지만 -19%에서 -13%로 감소폭이 완화되었고, 마케팅은 +1%에서 -3%로 반전되었다.

## So what
AI의 인력 영향은 전체 인원 감축이라는 하나의 평균보다 직무별 전망 변화로 관리해야 한다.

## Business context → metric → decision
- Original article: Survey: Workflow Redesign Is Key to AI Success (2026-11-18)
- Business context: Survey: Workflow Redesign Is Key to AI Success
- Metric and units: group, category, q1_pct, q3_pct, unit, provenance, survey_period, denominator; see data.csv for source-reported values, period, unit and denominator.
- Comparison and reference: 2026 Q1 and Q3 survey waves, reported category ordering.
- Decision: AI에 따른 인력 전망이 직무별로 다르게 재평가되므로, 일률적 감원 가정 대신 직무별 계획을 업데이트해야 한다.
- Insight type: Directional shift / occupational segmentation

## Official source facts, observation, interpretation, reuse
- Source fact and observed figure: Bain Flourish Figure 3 공식 썸네일을 직접 열어 Q1/Q3 11개 직무의 수치·레이아웃을 판독. 조사 시점은 2026 Q1 및 Q3 두 응답 집단이며 결과는 인원 변화에 대한 전망.
- Author interpretation (not demonstrated causality): AI의 인력 영향은 전체 인원 감축이라는 하나의 평균보다 직무별 전망 변화로 관리해야 한다.
- Reuse proposal: Replace values with equivalent numerator, denominator, units and period; retain chart mapping.
- Original figure inspection: Official Flourish thumbnail viewed https://public.flourish.studio/visualisation/30552254/thumbnail

## Visual encoding
세 개의 의미 집단에 직무별 5/4/2개의 작은 slope chart를 나열하고 공통 -20~+10% Y축, 직접값 레이블, 변화 방향별 강조를 사용한다. X=Q1·Q3, Y=expected change (%), 색=그룹, 크기=균등, 원본 직무 순서.
Titles, annotations, palette and background are configurable in config.json. Axis positions, bar heights, percentages and label placement are calculated from data.csv. Do not include source logos or images.

## Public provenance and limitations
- All observations in data.csv are reported public figures, while gaps and shares computed during rendering are derived; unknown values must be missing, not zero.
- Public data, sample and calculation: Bain Flourish Figure 3 공식 썸네일을 직접 열어 Q1/Q3 11개 직무의 수치·레이아웃을 판독. 조사 시점은 2026 Q1 및 Q3 두 응답 집단이며 결과는 인원 변화에 대한 전망.
- Conditions: Same meaning of headcount expectations in each survey wave; Two separate cross-sectional samples, not a panel; No causal claim or observed headcount outcome.
- Counterexample and limitations: AI로 실제 발생한 고용 변화가 아닌 조사 시점별 예상 변화다. Q1과 Q3 표본의 직무별 분모 및 표준오차는 미공개; 관찰된 인과관계가 아니다. 원본과 완전 동일한 시각 디자인은 보장하지 않는다.

## Step-by-step data_recipe
1. 직무별 Q1/Q3 전망값을 동일 정의로 수집한다.
2. 백분율은 %로 저장하고 변화량은 Q3-Q1의 %p로 계산한다.
3. 직무별 그룹 구성과 원본 순서를 유지한다.
4. CSV의 q1_pct/q3_pct, config.json의 THEME와 CONTEXT를 교체한다.
5. 두 테마를 200dpi로 렌더링하고 모든 값과 축을 점검한다.

## Usage
```bash
python chart.py --data data.csv --config config.json --theme source --output source.png --dpi 200
python chart.py --data data.csv --config config.json --theme neutral --output neutral.png --dpi 200
```
PNG generated files are outside the immutable Bronze bundle. No user review or model retraining was performed.
