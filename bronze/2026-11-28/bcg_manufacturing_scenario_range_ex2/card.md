# BCG | Exhibit 2

출처: [How Technology, Geopolitics, and Energy Could Redraw the Global Manufacturing Map](https://www.bcg.com/publications/2026/ai-automation-reshape-manufacturing) · 게시 2026-11-23 · 수집 2026-11-28 · 데이터 기간 2025 MVA base; scenario assumptions 2025–2026 · Exhibit 2 official image; technology-geopolitics-energy-the-new-map-of-manufacturing-ex02.png

## 글 요지 (사실과 해석)
BCG는 기존 제조 부가가치의 지역 간 재배치를 기술, 무역, 에너지 조건별로 모형화했다. 기술 범위는 4,337~6,595십억 달러로 관세와 에너지 범위보다 크다. 이는 생산성 투자가 경쟁력 회복에 중요할 수 있다는 시나리오 결과다.

**So what:** 다른 조건을 고정한 모형에서 기술 시나리오만 기존 제조 허브의 부가가치를 2025년 기준 이상으로 높일 수 있다.

## 비즈니스 질문과 인코딩
Agent ROI 민감도, 생산비·공급망 시나리오별 가치 범위 비교. x=기술/관세/에너지; y=2025 USD bn; 막대 시작=하한, 끝=상한; 색=요인; 점선=6102 기준; 범위 레이블 하단; y축 절단 3000. 인사이트 유형: Scenario sensitivity range. 원문 관찰값은 data.csv에 reported로 표시했다.

## 데이터 출처와 한계
BCG Manufacturing Competitiveness Advisor Tool; BCG Institute analysis. 기존 2025년 글로벌 MVA를 고정한 즉시 재배치 시뮬레이션이며 시점이나 성장률의 예측이 아니다. 54개국·47개 산업, 1,000명 제조 임원 설문에 기반한 모형. 관세의 공개 차이는 1492, 표시된 끝값 차이는 1491로 1bn 반올림 불일치가 있어 공개값 보존. 범위는 신뢰구간이 아니다.

## 재사용 절차
1. 같은 기준연도·가격 기준으로 기준값을 정한다.
2. 한 번에 하나의 변수를 변화시켜 하한과 상한을 수집한다.
3. high-low를 계산하고 공개 차이와 반올림 오차를 확인한다.
4. 구간을 부동 막대로 그리고 기준선을 추가한다.

## 사용
`pip install -r requirements.txt` 후 `python chart.py --theme source --output source.png --dpi 200` (neutral도 가능). 새 데이터와 설정은 별도 작업 폴더에서 변경한다. 원본 그림, 로고, 폰트는 포함하지 않는다.
