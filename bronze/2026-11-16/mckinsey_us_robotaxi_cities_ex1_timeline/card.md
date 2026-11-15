# Autonomous mobility gains ground — Exhibit 1 — Shared autonomous services are expanding rapidly in the United States

## 글 요지 (3문장)
미국 상업용 로보택시가 운영되는 도시의 수가 늘고 있다. 2024년 말 3개, 2025년 말 6개, 2026년 9월 15개가 확인됐다. 이후 20개와 약 40개는 전망치다.

## 단 하나의 So what
미국 상용 로보택시 도시 수는 2024년 말 3곳에서 2026년 9월 15곳으로 늘었다. 2026년 말 20곳과 2027년 말 약 40곳은 전망이므로 관측과 분리해 실행 계획을 수립해야 한다.

## 공식 사실 / 시각 관찰 / 해석 / 재사용
- 공식 사실: 2024-12 3, 2025-12 6, 2026-09 15, 2026-12 20 forecast, 2027-12 약 40 forecast는 공식 그림 설명 값.
- 시각 관찰: 공식 이미지 대체 텍스트를 열었으나 SVGZ 원본은 열리지 않음.
- 해석: 미국 상용 로보택시 도시 수는 2024년 말 3곳에서 2026년 9월 15곳으로 늘었다. 2026년 말 20곳과 2027년 말 약 40곳은 전망이므로 관측과 분리해 실행 계획을 수립해야 한다.
- 재사용 제안: 신규 점포·제품·AI Agent 서비스의 관측 실적과 운영계획을 분리해 표현.

## 비즈니스 맥락 → 지표 → 판단
- source_url: https://www.mckinsey.com/featured-insights/charts/autonomous-mobility-gains-ground
- 게시일 2026-11-12; 검색/수집일 2026-11-16 (Asia/Seoul)
- 그림: Exhibit 1 — Shared autonomous services are expanding rapidly in the United States
- 모집단/출처: 자료는 기업 사이트와 보도 검색에 기반한 McKinsey Center for Future Mobility 집계. 원본 SVGZ는 확인할 수 없으며 텍스트 대체설명의 다섯 수치를 사용했다.
- 관측 단위: date milestone × observed/forecast
- Y 또는 핵심 측정: Cities with commercial robotaxi or roboshuttle service
- 분모: Distinct US cities with commercial shared AV services, including safety-driver services
- 단위 count; 기간 2024-12, 2025-12, 2026-09, 2026-12 forecast, 2027-12 forecast
- 비교: 과거 상용 서비스 도시 수 대비 미래 확장 가정. 실선과 점선은 실제/예상을 구분.
- 계산: 시점별 상용 로보택시 서비스 도시의 고유 개수를 합산하며, 도시별 사업자 중복은 제거해야 함.

## 시각 인코딩과 디자인
- 유형 milestone_timeline; x=period_label, y=cities, 색상=observed vs forecast, 크기=fixed, 라벨=cities
- 정렬: 날짜 오름차순; 불규칙한 시점은 명시적인 범주형 마일스톤 배치.
- 강조: 과거 실측은 실선, 미래 예측은 점선; 직접 수치 라벨.
- 제목/주석/축: config.json의 CONTEXT와 THEME에서 제어; 데이터 유래 위치는 CSV로부터 계산.

## 재사용 data_recipe
1. List US cities with commercial shared AV launches at each date
2. Count each city once with consistent commercial-service definition
3. Keep observed data separate from forecast assumptions
4. Render sequential milestones; use solid line for observed and dashed for projected
5. Validate new forecasts against actual launches before reusing

## 메시지 성립 조건 · 반례 · 한계
- Forecasted 20 and 40 are not actual deployments
- Cities with service are not market size, riders, or fleet count
- Includes services operating with and without safety driver
- 반례: 미래 도시 수가 예측대로 증가하지 않거나 실제 수익성 확보에 실패하면 도시 확대가 가치창출로 이어진다는 결론은 성립하지 않는다.
- diff_notes: Original McKinsey SVGZ asset failed public image fetch; all five quantitative labels are available in official image description. This is an editorial line timeline rather than a fidelity-certified original reproduction.
- 원본 충실도: unverified / null (사용자 승인과 무관)

## 실행 및 재사용
`python chart.py --data data.csv --config config.json --theme source --output artifacts/source.png` 및 `--theme neutral`로 200dpi 렌더링. 새 사업 자료에 적용할 때 CSV, config.json/THEME/CONTEXT만 교체한다. 합성값은 원본 관측 자료와 혼합하지 않는다.
