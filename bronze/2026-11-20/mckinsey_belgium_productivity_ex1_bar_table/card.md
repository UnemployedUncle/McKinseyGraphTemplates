# McKinsey — A bold vision for Belgium / Exhibit 1

## 글 요지: 3문장
벨기에의 시간당 생산성은 비교국보다 높은 편이지만 고용률은 상대적으로 낮다. 생산가능인구당 GDP는 고용률, 노동시간, 시간당 생산성을 분해하면 국가별 차이를 설명하기 쉽다. McKinsey는 잠재 성장률을 높이기 위해 생산성과 노동 참여를 함께 높이는 정책의 필요성을 강조한다.

**So what:** 단일 생산성 수치가 아니라 참여율·노동시간·생산성의 기여를 분해해 성장 병목을 판단하라.

## 비즈니스 맥락 → 지표·단위·기간·분모·비교 → 판단
공식 Exhibit 1은 2024년 United States, Belgium, Netherlands, Denmark, EU를 비교한다. 20–64세 1인당 GDP(2024 벨기에 PPP 가격의 €천)는 96/88/88/87/70이며, 고용률(%) 76/72/84/80/76, 시간당 GDP(€) 71/77/72/79/57, 근로자당 연간 근로시간 1775/1583/1452/1372/1661이다. 전체 20개 값은 reported이고 실제 기초자료는 OECD·Eurostat(갱신일 2026년 7~10월)다. Belgium의 1인당 GDP는 Netherlands와 같지만 72%와 84%의 고용률 차이, €77과 €72의 생산성 차이가 있다.

## 인사이트 유형 및 시각 설계
원문 HTML 이미지 설명은 국가별 막대와 3개 지표 표를 함께 보여주지만 원본 픽셀은 직접 열지 못했다. editorial bar_and_table로 분류하며 fidelity_score=null이다. x축=국가, y축=20–64세 1인당 GDP(€천, 0축), Belgium만 강조색, 기타 국가는 중립색. 상단 막대의 각 €k 수치와 하단 고용률·시간당 GDP·근로시간 표를 같은 국가 순으로 정렬한다. 제목·PPP 단위·반올림 주석은 CONTEXT로 관리한다.

## 출처, 계산과 표본
McKinsey 공식 2026-11-19 보고서 Exhibit 1. GDP/working-age ≈ employment_rate_pct/100 × gdp_per_hour_eur × hours_per_worker; 표시된 항목은 독립적으로 반올림되어 완전 일치하지 않을 수 있다. Belgium 0.72×77×1583=€87,767, 공개 GDP/working-age €88,000과 반올림 차이. 시장환율 명목€와 PPP조정€을 혼동하지 않는다. 상세 원시표본 가중치는 미공개다.

## data_recipe
1. 20–64세 인구 및 취업 정의, 조사연도와 PPP 물가기준을 일치시킨다.
2. 고용률·시간당 생산성·연간 근로시간·총 KPI를 수집하고 열별 provenance를 표시한다.
3. 3개 구성요소의 곱으로 총 KPI를 반올림 오차 범위에서 검증한다.
4. 국가별 총 KPI를 공통 0축 막대에, 동인을 하단 정렬 표에 배치한다.
5. 기간·산업구성·인구 분모 차이를 주석으로 구분한다.

## 조건·반례 및 사용법
고용률 증가가 같은 인당 생산성으로 이어진다는 보장은 없고, 국가별 산업 구성과 연령구조 차이는 별도 통제해야 한다. 원본 차트의 여백·색·범례 검증이 없어 source-fidelity unverified다. python chart.py --data data.csv --config config.json --theme source --output artifacts/source.png; neutral 반복. 다른 기업·사업부 KPI에도 적용 가능하다.
