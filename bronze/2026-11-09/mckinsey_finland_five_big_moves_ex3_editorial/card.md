# McKinsey | Finland five big moves — 본문 정량 수치 편집형 비교

## 원문 요지 (직접 작성, 3문장)
핀란드 대형 상장기업의 성장목표는 개선되고 있지만 실제 자원 재배치와 전략적 행동은 목표에 못 미친다. McKinsey는 21개 상장기업이 2025년 다섯 가지 `big moves` 기준을 충족한 수를 각각 공개했다. 다섯 요인 중 하나라도 충족하기 어려우며 21개 중 17개는 최대 한 가지, 세 가지 이상 수행한 회사는 없는 것으로 분석됐다.

## So what (단 하나)
**성장전략은 발표된 목표 대신 자본배분·차별화·생산성 등 실행된 전략 행동을 기업별로 점검하는 관리 체계가 필요하다.**

## 원문 사실·관찰·해석·재사용 구분
- **원문 사실:** 2026-11-06 게시. 2025년 핀란드 21개 대형 상장회사에 대하여 `dynamic resource reallocation=8`, `differentiation=7`, `big investments=3`, `productivity improvement=1`, `programmatic M&A=0`. 또한 17개는 실행한 move가 0~1개, 3개 이상 실행한 곳은 0개라고 설명.
- **관찰:** 특히 `programmatic M&A` 해당 기업이 0, 노동생산성 기준을 넘어선 곳이 1개에 불과하다.
- **해석:** 목표의 상승보다 실행 전환이 지연되는 것으로 읽을 수 있지만, 기계적 기준 충족 여부가 성장 성공의 인과효과를 증명하지는 않는다.
- **재사용 제안:** 기업/사업부의 비배타적 실행역량 요인별 통과 기업 수를 시각화.

## Business context → metrics → decision
- **경영 질문:** 21개 대기업이 실제로 어떤 고성장 실행수단을 선택하고 있는가?
- **관측 단위:** `company × move × observation_year`, 2025년, 분모 21개 상장사(기준별 동일). **표시 단위:** company count, not percent or exclusive share; 회사가 다수 move를 충족할 수 있으므로 5개 값을 합산하여 유일 회사 수로 해석하지 않음.
- **비교 기준:** 동일 표본 내 다섯 가지 전략 move의 통과 기업 수. **판단:** 자원배분·M&A·생산성 개선 등 저활용 분야의 장애요인 우선 분석.
- **증거 한계:** 회사별 원자료, 기업명별 통과여부 및 기준 산출 상세 모델 미공개.

## 시각화 설계
- **Insight type:** ranked multi-select coverage; **Chart:** horizontal sorted bars, **NOT** faithful reproduction of Exhibit 3.
- **X:** `company_count`, 공통 0~21 company count. **Y:** `move` 내림차순. **Color:** 낮은 수(0,1) 별도 강조, 나머지 중립. **Size:** 공통 폭·높이. **Alignment:** 동일 표본 기업 21개. **Labels:** bar 끝 `n/21`. **Axis:** 0,5,10,15,20, **Notes:** 분모·중복선택 가능·자료연도, **Legend:** 색상 의미는 낮은 항목 강조(본문 직접 라벨로 설명).
- **원본 확인:** 기사 본문 수치는 실제 확인; Exhibit 3 SVGZ 원본은 직접 열 수 없어 원본 형태/배치 비교 불가. 새 차트는 편집형이므로 점수 미부여.

## 공개 데이터 및 정의
- Source URL: https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/assessing-the-growth-trajectory-of-finlands-largest-companies
- Published: 2026-11-06; Collected: 2026-11-09; Observation: 2025. McKinsey Value Intelligence Platform, sample=21. Excluded sectors in 5000-global benchmark: financial services and real estate; Finnish sample comparability follows original.
- 다섯 값은 모두 `reported`, 수치별 분모 21. `dynamic resource reallocation`은 10년간 수익 10~30% 이동, `programmatic M&A`는 시총 대비 10년 누적 30% 이상의 중소규모 인수 등 원문 기준에 의존. 상세 원자료 미공개.

## 단계별 data_recipe
1. `company_id`, `observation_year`, `market_cap`, `move`, `criterion_value`, `passed`, `benchmark_peer_group`을 확보.
2. 각 move의 정의·기간·산업별 판정 기준을 동일하게 적용.
3. 회사별 5개 Boolean 통과 기록을 만들고 중복 허용.
4. 표본 21개(결측 없음 여부 별도 점검)를 분모로 `groupby(move).sum(passed)` 계산.
5. 5개 항목별 count를 내림차순으로 표시, 0/1 중요 영역 강조.
6. 새로운 대상에서는 실제 분모와 제목·관측연도·조건을 바꿔 `THEME/CONTEXT` 렌더링.

## 메시지 성립 조건·반례·한계
- **성립:** 동일한 회사 표본, 기준 충족 Boolean이 업종별로 조정된 공정한 기준이어야 함.
- **반례:** 기업이 M&A 대신 유기성장에 집중하거나 기준을 충족하지 않아도 높은 성과를 낼 수 있음. 단순 count 합산으로 전략 성공률을 추정하면 오류.
- **한계:** 동일 21개 기업이 여러 move를 충족할 수 있으므로 합계 19는 독립적인 기업 수가 아님. 표본이 작고 대형 상장사만 포함되어 핀란드 전체 기업에 일반화 불가. 실질 성과 예측모델 미공개.

## 사용 방법
`python chart.py --data data.csv --config config.json --theme source --output source.png` 또는 `--theme neutral`. 사용자 Silver/Gold 승인 없음, 실제 학습 금지.
