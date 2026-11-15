# Corporate Giants Are Staying on Top Longer. Should They Feel Safe? — Exhibit 1 — Leadership Has Been Locking In, but the Degree Varies by Sector

## 글 요지 (3문장)
상장사 시장가치 리더의 지위는 더 오래 유지되는 경향이다. 15개 산업의 중앙값은 과거 24%에서 최근 13%로 하락했다. 그러나 일부 업종은 다른 방향으로 변화한다.

## 단 하나의 So what
시장가치 상위 기업의 가치 가중 교체율은 1990–2004년 중앙값 24%에서 2005–2025년 13%로 낮아졌지만 업종별 차이가 크므로 산업별 고착화 위험을 따로 평가해야 한다.

## 공식 사실 / 시각 관찰 / 해석 / 재사용
- 공식 사실: 기간별 전체 업종 giant churn 중앙값 24%, 13%는 공식 본문에 보고됨.
- 시각 관찰: BCG의 15개 업종 x/y 산점도 이미지를 직접 열었고, 점 좌표는 축 판독 근삿값.
- 해석: 시장가치 상위 기업의 가치 가중 교체율은 1990–2004년 중앙값 24%에서 2005–2025년 13%로 낮아졌지만 업종별 차이가 크므로 산업별 고착화 위험을 따로 평가해야 한다.
- 재사용 제안: 기업·제품·지역별 신규 진입자의 시장점유율 변화를 두 기간에 비교.

## 비즈니스 맥락 → 지표 → 판단
- source_url: https://www.bcg.com/publications/2026/market-leaders-staying-on-top-longer
- 게시일 2026-11-06; 검색/수집일 2026-11-16 (Asia/Seoul)
- 그림: Exhibit 1 — Leadership Has Been Locking In, but the Degree Varies by Sector
- 모집단/출처: 미국 거래소 상장 시가총액 상위 2,000개 기업, S&P Capital IQ. 15개 업종 점의 좌표는 공개된 축/마커를 축척 판독한 것으로 ±3%p 정도의 오차를 갖는다.
- 관측 단위: sector × comparison period
- Y 또는 핵심 측정: Giant churn: entrants' market cap as % of sector top-ten market cap
- 분모: Top ten firms' market capitalization in each industry
- 단위 percent; 기간 1990-2004, 2005-2025
- 비교: 기존 기간 대비 최근 기간의 업종별 giant churn. y=x 아래면 경쟁 주도기업의 변화율이 감소.
- 계산: 업종별 top-ten 중 새로 진입한 기업의 시가총액 / top-ten 합계 ×100; 공개 점 좌표는 시각 판독해 digitized_estimate 지정.

## 시각 인코딩과 디자인
- 유형 industry_scatter; x=previous_pct, y=recent_pct, 색상=selected sectors, 크기=fixed, 라벨=sector
- 정렬: 업종 관측점을 좌표 위치로 배치하며 45도 동등선으로 방향을 판단.
- 강조: 선택 업종 마커 강조, 나머지 점 중립색; 축은 서로 다른 최대값을 갖는다.
- 제목/주석/축: config.json의 CONTEXT와 THEME에서 제어; 데이터 유래 위치는 CSV로부터 계산.

## 재사용 data_recipe
1. Collect top-ten companies by sector and market cap at five-year intervals
2. Identify companies entering the top ten relative to the preceding period
3. Sum entrant market cap divided by total top-ten cap
4. Take median of five-year observations separately in each era
5. Plot sector-level pairs, retaining point digitization uncertainty

## 메시지 성립 조건 · 반례 · 한계
- Sector classification must be consistent across eras
- Point coordinates are digitized estimates, not reported underlying observations
- Omitted private companies and non-US-only listings limit generalization
- 반례: y>x인 업종에는 산업별 교체율 감소 주장이 성립하지 않는다.
- diff_notes: Original public low-resolution Exhibit 1 opened; point coordinate readings approximate. Recreated labels and equality diagonal, but removed original colored sector shading and arrow design; not a verified pixel reproduction.
- 원본 충실도: unverified / null (사용자 승인과 무관)

## 실행 및 재사용
`python chart.py --data data.csv --config config.json --theme source --output artifacts/source.png` 및 `--theme neutral`로 200dpi 렌더링. 새 사업 자료에 적용할 때 CSV, config.json/THEME/CONTEXT만 교체한다. 합성값은 원본 관측 자료와 혼합하지 않는다.
