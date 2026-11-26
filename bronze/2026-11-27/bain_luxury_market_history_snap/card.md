# Luxury market holds near its recent peak

## 출처와 사실
- [Bain 공식 원문](https://www.bain.com/insights/luxury-holds-its-ground-in-2026-with-new-opportunities-ahead-snap-chart/) · 게시 2026-11-18 · 수집 2026-11-27 · Snap chart — global personal luxury goods market 2005–2026E
- 2026년 개인 명품 시장은 전년 대비 성장할 것으로 추정된다. 보석류의 성장세가 거시경제 역풍을 상쇄하는 데 기여했다. 장기간 시장 규모는 위기와 반등을 거치며 변화했다.

## So what
시장 성장의 장기 경로와 최근 정체를 구분해 성장 전략을 수립해야 한다.

## 비즈니스 맥락과 지표
시장 규모의 장기 추세와 성장 국면 진단 → EUR billion / 2005–2026E / 글로벌 개인 명품 시장 연간 매출; 현행 환율 기준, 물가조정 여부 미공개 → 동일 기준 비교로 판단.

## 원본 관찰 및 데이터
연도 x, 연간 매출 y, 막대 길이, 회색 국면과 적색 마지막 전망, 국면 시작 주석과 일부 공개값 레이블; y축 눈금 생략, 0 기준선.
출처/표본/계산: Bain & Company luxury study; 조사 시점/세부 추정법 미공개.
비표시 14개 막대는 썸네일 높이 판독 추정, hover 미구현, KPI/국면 위치 및 글꼴 근사.
판독식: round((623−막대 상단 y)×367/335); 1000×657 썸네일에서 기준선 623px, 2026E 높이 335px. 수동 경계 판독 및 반올림에 대한 보수적 ±3bn. 공개값은 직접 레이블 사용.

## 재사용 data_recipe (제안)
1. 동일 범위의 연도별 시장규모를 확보한다.
2. 공개 레이블과 추정값을 분리하고 환율 기준을 확인한다.
3. 연도 정렬 후 전망 연도와 국면을 지정한다.
4. 성장률은 원문 환율 기준을 유지한다.

## 성립 조건·반례
같은 시장 경계·통화·기간을 사용해야 한다. 명목 환율 변동 및 반올림에 의해 성장률이 달라질 수 있다. 고정환율 3%는 시장 규모 바에서 역산하지 않는다.

## 사용
`pip install -r requirements.txt`; `python chart.py --theme source --output source.png --dpi 200`; neutral로 교체 가능. CSV와 config 수정 후 별도 작업폴더에서 실행.
