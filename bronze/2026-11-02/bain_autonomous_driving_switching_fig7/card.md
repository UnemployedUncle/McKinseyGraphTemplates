# BAIN | Global Auto Consumer Survey: Regional Trends in a Changing World

## 출처와 사실
- 기관: BAIN
- 공식 원문: https://www.bain.com/insights/global-auto-consumer-survey-regional-trends-in-a-changing-world/
- 게시일: 2026-10-21 (공식 기사 표기 확인); 수정일: 미표기; 열람일: 2026-11-02
- 그림 식별자: Figure 7
- 공식 이미지 URL: https://public.flourish.studio/visualisation/30413078/thumbnail
- 공개 데이터/표본: Bain Global Automotive Consumer Survey 2026 (n=12,351 overall). 국가/차급별 유효 표본, 가중치, 조사 월은 해당 그림에 별도 미공개.

## 원문 요지 (사실; 3문장 이내)
브랜드 전환 위험을 지역별 자동차 소비자의 자율주행 선호도 차이로 판단한다. 공식 공개 자료는 EU: Premium 48%, Mass 25%; US: 46%, 25%; China: 60%, 61%. Premium minus Mass: +23, +21, -1 pp. 차트의 수치와 원문 서술 사이를 구분해야 하며, 결과 해석의 범위는 해당 모집단과 조건으로 한정된다.

## 단 하나의 So what (해석/의사결정 제안)
**유럽·미국의 프리미엄 고객은 자율주행 기능을 위해 브랜드를 바꿀 의향이 대중차 고객보다 21~23%p 높지만, 중국에서는 두 집단이 60~61%로 거의 동일해 지역별 상품 전략을 달리해야 한다.**

## 비즈니스 맥락 → 숫자 → 판단
| 구분 | 내용 |
|---|---|
| 질문 | 브랜드 전환 위험을 지역별 자동차 소비자의 자율주행 선호도 차이로 판단한다. |
| 공개값 | EU: Premium 48%, Mass 25%; US: 46%, 25%; China: 60%, 61%. Premium minus Mass: +23, +21, -1 pp. |
| 단위·시점·분모 | Bain Global Automotive Consumer Survey 2026 (n=12,351 overall). 국가/차급별 유효 표본, 가중치, 조사 월은 해당 그림에 별도 미공개. |
| 관찰 사실 | 원문의 보고값/범위만 data.csv로 복원, 분모 정의 유지. |
| 제안할 판단 | 유럽·미국의 프리미엄 고객은 자율주행 기능을 위해 브랜드를 바꿀 의향이 대중차 고객보다 21~23%p 높지만, 중국에서는 두 집단이 60~61%로 거의 동일해 지역별 상품 전략을 달리해야 한다. |

## 인사이트와 차트 해부
- 주 인사이트: 격차; 차트 유형: `grouped_bar`.
- 실제 원본 시각 직접 확인 여부: 예 (Bain 공식 Figure 7 이미지 직접 열람).
- x: 지역(EU/US/China); y: 전환 의향(%).
- color: Premium vs Mass; 같은 지역 내 2개 막대; size: 없음; panel: 단일 패널.
- 정렬: config.CONTEXT.category_order; 값은 data.csv에서 읽고 길이/위치를 계산.
- 제목: 한 문장 액션 타이틀로 편집(원본의 긴 제목 또는 기사 요지를 직접 번역·복제하지 않음).
- 라벨·범례: 수치 직접 표시. 범례 2개와 EU/US 20%p 격차 점선 주석.
- 축: 0 기준선 유지; 로그/이중축/절단축 없음. [원본의 y 눈금 생략 구조를 따랐음].
- 가독성: 핵심값 직접 표기, 비교 대상의 안정적인 정렬. 해석 주의: 프리미엄−대중차 격차가 EU·US에서 크고 중국에서 0에 가까울 때 메시지가 성립. 중국 격차도 커지거나 미국·EU 프리미엄 전환의향이 낮으면 제목을 수정. 브랜드 전환이 실제 구매·이탈로 이어진다고 단정할 수 없음.

## 데이터 확보·모델링 및 재사용 data_recipe
respondent × region × customer_segment × autonomous_driving_switch_intent → 공식 서베이/소비자 설문 → 지역·차급 분류 정합성 및 결측 응답 제외 → 집단별 유효 응답 분모 일치 → 100×switch_yes/valid_respondents → grouped table → Premium−Mass pp → 지역별 차이를 먼저 해석

## 메시지 성립 조건과 반례
프리미엄−대중차 격차가 EU·US에서 크고 중국에서 0에 가까울 때 메시지가 성립. 중국 격차도 커지거나 미국·EU 프리미엄 전환의향이 낮으면 제목을 수정. 브랜드 전환이 실제 구매·이탈로 이어진다고 단정할 수 없음.

## 재사용
- 예시 업무: 자동차 차급 대신 고객 등급, 지역 대신 B2B 고객군으로 치환해 차별화 기능의 전환 의향을 비교.
- `data.csv`에서 category/series/value (range일 때 lower/upper)를 변경.
- `config.json` → `THEME.source`, `THEME.neutral`로 색상·폰트·여백·막대/마커 스타일을 변경.
- `CONTEXT`에서 제목·정렬·축 범위·단위·소스 표기·주석을 변경. 새 데이터의 패턴에 맞게 제목 수정 필수.
- 실행: `python chart.py --theme source --data data.csv --config config.json --output output.png` (neutral도 동일).
- 총 충실도와 남은 차이: 원본과 생성 이미지 직접 비교하여 validation.json에 별도 기록.
- 수치의 한계: 공개값만 사용, 구체적인 지역·차급 표본은 미공개.

_본 분석은 자체 작성한 해설로, 원문 전문·그림 이미지를 복제하거나 제3자 콘텐츠의 재학습 권리를 부여하지 않습니다._
