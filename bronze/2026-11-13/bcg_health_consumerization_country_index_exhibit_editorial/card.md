# BCG · Health care consumerization index (editorial)

## 글의 요지 (3문장)
BCG는 2026년 7~8월 10개 시장의 소비자 9,914명을 조사해 의료서비스에 대한 편의성·선택권·정보 접근 기대를 평가했다. 지수는 6개 설문 문항에 대한 동의 수준을 0~100점으로 표현하며, 국가별로 소비자화 수준이 다르다. 중국이 72점으로 가장 높고 일본이 36점으로 가장 낮다.

## So what
국가별 의료소비자화 인식지수 차이가 36점이므로 서비스 진입·상품·고객접점 전략을 국가별로 분리해 설계해야 한다.

## 비즈니스 맥락 → 데이터 → 판단
- 맥락: 디지털 소비자경험의 기대가 의료의 정보탐색·치료 선택·접점 설계에도 반영됨
- 관측단위: 국가, 2026년 7~8월 설문, 10개 시장; 전체 표본 9,914명, UAE 표본 354명
- 지표: `index_score`, 0~100의 **점수**; 응답자 비중(%)이 아님
- 분모: 국가별 표본의 설문응답을 기준으로 한 합성지수. 국가별 개별 n 및 오차 범위는 원문에 모두 공개되지 않음
- 비교기준: 국가 간 동일 설문문항을 이용한 지수. 최대 72, 최소 36, 격차 36 **점**(derived)
- 판단: 시장별 의료 정보·가격 투명성·예약·진료 경로에서 서로 다른 소비자경험을 제공해야 함

## 인사이트 유형과 시각화 인코딩
- Insight: geographic ranking and heterogeneity, ordinal comparison (단순 상관·인과 아님)
- `x=index_score`, `y=country`, `color=selected higher-score markets`, `size=bar length`, sort=descending
- 축: 0~82; 지수의 개념적 범위 0~100은 `x_label`에 명시, 시각적 표현은 읽기 쉬운 데이터 범위 사용
- 라벨: 값 직접 표기; `THEME` source/neutral과 `CONTEXT`에 색·제목·축·주석 보관
- 원본 영상/도표 접근 제약: 공식 HTML에서 'Health Care Consumerization Index by Country' 존재와 전 수치 확인, 원본 그림 픽셀/배치는 확인 불가. **원본 재현이 아닌 편집형 차트**

## 자료 및 계산
- 출처: https://www.bcg.com/publications/2026/health-care-consumerization-patients
- 별도 2026-11-12 BCG 보도자료로 국가별 정확한 10개 지수를 교차 검증
- 표본: 2026-07~08, 총 9,914명, 10개 시장, UAE는 354명, 시장 내 성별 균형 가중
- 계산: `gap_points = max(index_score) - min(index_score) = 36`, 실제 데이터의 공개값 `reported`
- 지수 6개 질문의 정확한 가중치·항목별 원시 응답은 공개되지 않음. 직접 재계산하지 않음

## 단계별 data_recipe
1. 시장별 동일한 질문·응답척도와 조사기간 정합화
2. 공통 지수(0~100) 산출법을 명시하고 국가별 표본·가중치 기록
3. 각 국가의 실제 공개 지수만 `data.csv`에 `reported`로 입력
4. 내림차순 정렬 후 최고·최저·범위(점)를 도출
5. `THEME`/`CONTEXT`로 강조 범주·제목·축과 주석 변경
6. 지역별 제품전략 판단시 규제·접근성·보험 구조를 별도 변수로 검증

## 성립 조건과 반례·한계
- 지수 점수는 이용률이나 소비자 만족도가 아니다. 2026년 시점의 태도·기대 측정이다.
- 의료 시스템 유형 차이, 문화적 응답 편향, 국가별 표본 크기가 해석에 영향을 줄 수 있다.
- 국가별 점수 차이를 서비스 매출 잠재력이나 AI 효용의 인과 근거로 바로 쓰지 않는다.
- 선정한 네 나라의 강조는 편집·분석을 위한 선택이지 원문의 권고 분류가 아니다.

## 사용 방법
`pip install -r requirements.txt`, 이후 `python chart.py --data data.csv --config config.json --theme source --output source.png` 및 `--theme neutral`. 실제 출처·대상·분모를 CSV에서 함께 갱신한다.
