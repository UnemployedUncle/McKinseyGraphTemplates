# BCG — Exhibit 1 — Traditional manufacturing could lose $1.8tn MVA and 26m jobs

## Article: three original sentences
- BCG는 54개국 47개 산업의 경쟁력을 모델링해 기존 제조업 거점의 생산 이동 위험을 평가했다.
- 현 경쟁력 격차가 유지되면 미국·서유럽·일본에서 약 1.8조 달러의 제조 부가가치가 다른 지역으로 이전될 수 있다.
- 서유럽 약 9,910억 달러와 일자리 약 1,500만 개가 세 지역 가운데 가장 큰 위험 규모다.

## So what
자동화·생산성 투자를 평가할 때 단순 투자비보다 기존 제조 부가가치와 고용의 해외 이전 방지 잠재력을 함께 봐야 한다.

## Business context → metric → decision
- Original article: How Technology, Geopolitics, and Energy Could Redraw the Global Manufacturing Map (2026-11-23)
- Business context: How Technology, Geopolitics, and Energy Could Redraw the Global Manufacturing Map
- Metric and units: region, base_mva_usd_bn, loss_mva_usd_bn, jobs_base_m, jobs_at_risk_m, mva_unit, jobs_unit, provenance, scenario; see data.csv for source-reported values, period, unit and denominator.
- Comparison and reference: 2025 manufacturing base under current-competitiveness model, reported category ordering.
- Decision: 생산성 개선이 없을 때 제조업 이전 위험은 서유럽에 가장 집중되므로 국가·산업별 현대화 투자 우선순위를 재검토해야 한다.
- Insight type: Scenario exposure / regional decomposition

## Official source facts, observation, interpretation, reuse
- Source fact and observed figure: BCG Exhibit 1 공식 그림을 실제로 열고 지역별 MVA 기준액, 위험액과 고용 직접·간접 손실량 판독. 2025년 기준 달러, 54개국·47개 산업 모델, 제조업 경영진 약 1,000명 조사로 가중치 추정.
- Author interpretation (not demonstrated causality): 자동화·생산성 투자를 평가할 때 단순 투자비보다 기존 제조 부가가치와 고용의 해외 이전 방지 잠재력을 함께 봐야 한다.
- Reuse proposal: Replace values with equivalent numerator, denominator, units and period; retain chart mapping.
- Original figure inspection: Official BCG Exhibit 1 visual opened and inspected

## Visual encoding
원본과 같은 미국·서유럽·일본 3열 패널. X=2025 기준/위험/이동 후, Y=2025 USD bn, 녹색=남은 부가가치, 주황=위험 MVA, 길이/위치=데이터 산출, 정렬=원본 순서, 상단 비율과 하단 고용 숫자 주석.
Titles, annotations, palette and background are configurable in config.json. Axis positions, bar heights, percentages and label placement are calculated from data.csv. Do not include source logos or images.

## Public provenance and limitations
- All observations in data.csv are reported public figures, while gaps and shares computed during rendering are derived; unknown values must be missing, not zero.
- Public data, sample and calculation: BCG Exhibit 1 공식 그림을 실제로 열고 지역별 MVA 기준액, 위험액과 고용 직접·간접 손실량 판독. 2025년 기준 달러, 54개국·47개 산업 모델, 제조업 경영진 약 1,000명 조사로 가중치 추정.
- Conditions: Same base year and price basis; Same definition of direct and indirect jobs; Clearly label a modeled relocation scenario.
- Counterexample and limitations: 현실의 해외 이전이나 해고 실적이 아닌 2025년 전체 생산을 한 번에 경쟁력 기준 재배치한 모형상 극단 시나리오다. 42개 경쟁력 요인, 조사 가중치와 가정에 민감하다. 460+991+314=1765bn을 1.8tn으로 반올림.

## Step-by-step data_recipe
1. 지역별 MVA 기준값과 위험값을 동일 기준연도 및 통화로 수집한다.
2. after=base-loss와 loss/base 비율을 계산·검증한다.
3. 일자리 기준값과 손실은 직접+간접 고용 정의를 유지한다.
4. CSV 행 순서를 유지하고 THEME/CONTEXT 색과 제목을 바꾼다.
5. 두 테마를 200dpi로 렌더링하며 부동 막대 시작점과 모든 수치를 확인한다.

## Usage
```bash
python chart.py --data data.csv --config config.json --theme source --output source.png --dpi 200
python chart.py --data data.csv --config config.json --theme neutral --output neutral.png --dpi 200
```
PNG generated files are outside the immutable Bronze bundle. No user review or model retraining was performed.
