# McKinsey | PDF zero-based page 8, Exhibit 3 — preferences for AI vs human assistance

출처: https://www.mckinsey.com/~/media/mckinsey/industries/financial%20services/our%20insights/global%20banking%20annual%20review%202026%20part%202/global-banking-annual-review-2026-the-ai-disruption-dividend.pdf

게시: 2026-11-17 / 수집: 2026-11-26 / 조사: June 2026

## 요지 (원문 사실과 해석)
은행 고객의 생성형 AI 활용이 빠르게 확대되고 있다. 다만 업무가 달라지면 원하는 지원 방식도 달라진다. 기본 금융 질문과 달리 투자 조언에서는 사람의 전문성과 신뢰가 더 중요하게 나타난다.

## So what
기본 금융 질문과 투자 조언의 AI 선호도 차이를 반영해 사람의 개입 수준을 업무별로 설계해야 한다.

## 비즈니스 맥락 → 데이터 → 판단
업무의 복잡성과 신뢰 요구에 따른 Human-in-the-loop 설계. 지표 단위: percent of respondents. 분모: Consumer survey respondents; ~46,000 across 13 countries. 비교 기준: Basic financial questions, Investment advice. 판단: 위 So what 참조.

## 원본 관찰 및 시각화 설계
ribbon: 양단 100% 구성막대와 동일 범주 연결 리본. AI는 청색, 둘 다 회색, 사람은 남색. 값 중앙 표기, 오른쪽 직접 범주 라벨. 축 생략, 합계와 리본 면적은 데이터에서 계산.

## 재사용 data_recipe (제안)
같은 설문 문항과 동일 분모로 업무별 지원 선호도를 집계한다. AI·둘 다·사람의 상호 배타적 응답 비중을 산출하고 100%인지 확인한다. 양쪽 누적 경계 위치를 계산하고 같은 범주끼리 부드러운 면으로 연결한다.

## 성립 조건 및 반례·한계
개인별 전환표가 없으므로 리본은 개인 이동이 아니다. 설문 선호가 실제 행동이나 투자 성과를 의미하지 않는다. 표본은 13개국 약 46,000명, 국가별 가중치 및 문항별 유효 응답수 미공개. 보고서 발행일은 상위 보고서 날짜; PDF 표지는 2026년 11월.

## 사용법
`python chart.py --theme source --output source.png --dpi 200` 또는 `--theme neutral`. CSV의 group/series/value 및 config의 groups/series/colors를 함께 변경한다. 출처·분모·기간·provenance도 변경한다.

## 실제 검증
Source/Neutral 200dpi 렌더링 및 시각 확인, 로컬 테스트 6/6. 자체 충실도 4.57/5, verified. PDF 9번째 페이지 직접 스크린샷. 6개 값, 순서, 양쪽 막대·부드러운 리본, 색상 근사 및 직접 레이블 일치. 설명문 위치, 글꼴, 제목, 리본 너비·곡률 차이. 개인별 전환량으로 해석하지 않음. 사용자 검수는 pending.
