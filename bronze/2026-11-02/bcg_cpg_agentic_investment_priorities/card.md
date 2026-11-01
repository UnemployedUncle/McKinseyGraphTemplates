# BCG | Are CPG Companies Ready for Agentic Commerce?

## 출처와 사실
- 기관: BCG
- 공식 원문: https://www.bcg.com/publications/2026/how-cpg-companies-win-agentic-commerce
- 게시일: 2026-10-30 (공식 기사 표기 확인); 수정일: 미표기; 열람일: 2026-11-02
- 그림 식별자: Body: next-year investment priorities (editorial chart, not an original exhibit)
- 공식 이미지 URL: 해당 수치와 대응되는 단일 정량 그림 없음(본문 숫자 기반 편집형)
- 공개 데이터/표본: BCG GenAI CPG Survey 2026. 표본·조사 시점·중복선택/가중치 상세 미공개; 본문 수치만 사용.

## 원문 요지 (사실; 3문장 이내)
CPG 기업의 Agentic Commerce 대응에서 어떤 투자 영역을 우선할지 판단한다. 공식 공개 자료는 GEO 65%, product data 47%, owned agents 41%, ecosystem integration 35%. 각각 독립 응답비율로 합계 188%이며 구성비가 아니다. 차트의 수치와 원문 서술 사이를 구분해야 하며, 결과 해석의 범위는 해당 모집단과 조건으로 한정된다.

## 단 하나의 So what (해석/의사결정 제안)
**CPG 기업의 향후 1년 투자 계획에서 GEO 최적화(65%)와 상품 데이터 구조화(47%)가 자체 에이전트(41%)·외부 생태계 연동(35%)보다 우선해, 데이터 준비와 유통 채널 연결 투자를 균형 있게 설계할 필요가 있다.**

## 비즈니스 맥락 → 숫자 → 판단
| 구분 | 내용 |
|---|---|
| 질문 | CPG 기업의 Agentic Commerce 대응에서 어떤 투자 영역을 우선할지 판단한다. |
| 공개값 | GEO 65%, product data 47%, owned agents 41%, ecosystem integration 35%. 각각 독립 응답비율로 합계 188%이며 구성비가 아니다. |
| 단위·시점·분모 | BCG GenAI CPG Survey 2026. 표본·조사 시점·중복선택/가중치 상세 미공개; 본문 수치만 사용. |
| 관찰 사실 | 원문의 보고값/범위만 data.csv로 복원, 분모 정의 유지. |
| 제안할 판단 | CPG 기업의 향후 1년 투자 계획에서 GEO 최적화(65%)와 상품 데이터 구조화(47%)가 자체 에이전트(41%)·외부 생태계 연동(35%)보다 우선해, 데이터 준비와 유통 채널 연결 투자를 균형 있게 설계할 필요가 있다. |

## 인사이트와 차트 해부
- 주 인사이트: 순위; 차트 유형: `horizontal_bar`.
- 실제 원본 시각 직접 확인 여부: 아니오: 원문 글의 수치만 확인한 편집형 시각화.
- x: 응답비율(%); y: 투자 항목/에너지 설비.
- color: 전략적으로 중요한 항목만 강조; size: 없음; panel: 단일 패널.
- 정렬: config.CONTEXT.category_order; 값은 data.csv에서 읽고 길이/위치를 계산.
- 제목: 한 문장 액션 타이틀로 편집(원본의 긴 제목 또는 기사 요지를 직접 번역·복제하지 않음).
- 라벨·범례: 수치 직접 표시. 설정에 따른 항목 순서 및 범례 최소화.
- 축: 0 기준선 유지; 로그/이중축/절단축 없음. [공통 퍼센트 눈금으로 비교].
- 가독성: 핵심값 직접 표기, 비교 대상의 안정적인 정렬. 해석 주의: GEO가 다른 투자 항목보다 높은 응답 비율이면 제목 성립. 우선순위 역전 시 제목 수정. 선택률만으로 실제 지출·성과·매출 인과를 주장하지 않음.

## 데이터 확보·모델링 및 재사용 data_recipe
respondent × planned_investment_category → CPG 설문 → 중복선택 인정·무응답 처리 → 문항별 유효 분모 확정 → category별 선택 응답자 / 유효 응답자 ×100 → 내림차순 가로막대 → 우선순위와 절대 ROI 구분

## 메시지 성립 조건과 반례
GEO가 다른 투자 항목보다 높은 응답 비율이면 제목 성립. 우선순위 역전 시 제목 수정. 선택률만으로 실제 지출·성과·매출 인과를 주장하지 않음.

## 재사용
- 예시 업무: 트레이딩 Agent 도입 후보 기능별 투자 의향 또는 현업의 개선 우선순위 설문.
- `data.csv`에서 category/series/value (range일 때 lower/upper)를 변경.
- `config.json` → `THEME.source`, `THEME.neutral`로 색상·폰트·여백·막대/마커 스타일을 변경.
- `CONTEXT`에서 제목·정렬·축 범위·단위·소스 표기·주석을 변경. 새 데이터의 패턴에 맞게 제목 수정 필수.
- 실행: `python chart.py --theme source --data data.csv --config config.json --output output.png` (neutral도 동일).
- 총 충실도와 남은 차이: 원본 그래프가 없는 편집형 차트 → 원본 재현 점수 null, unverified.
- 수치의 한계: 원문 보고값의 정밀도·유효 표본 또는 모델 시나리오 계산의 일부 미공개.

_본 분석은 자체 작성한 해설로, 원문 전문·그림 이미지를 복제하거나 제3자 콘텐츠의 재학습 권리를 부여하지 않습니다._
