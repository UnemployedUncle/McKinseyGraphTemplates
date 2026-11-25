# BCG | Exhibit 4 — indexed annualized five-year IMS TCO

출처: https://www.bcg.com/publications/2026/telco-core-network-as-a-service

게시: 2026-11-25 / 수집: 2026-11-26 / 조사: 2026 case analysis; five-year annualized TCO

## 요지 (원문 사실과 해석)
통신 코어를 서비스로 조달하면 운영 책임과 고정비의 구조가 바뀐다. 사례 분석에서 클라우드 전환은 기존 구조보다 비용이 낮고 관리형 서비스는 추가 절감 효과가 있다. 가입자가 많을수록 자체 구축도 규모의 경제를 얻어 추가 절감률은 줄어든다.

## So what
공유형 관리서비스의 상대적 비용 우위는 가입자 규모가 작을수록 크므로 자체 구축과 서비스 구매 판단에 규모를 반영해야 한다.

## 비즈니스 맥락 → 데이터 → 판단
구축 대 구매 의사결정과 규모별 단위비용 비교. 지표 단위: index, traditional IMS at 1m = 100. 분모: Annualized five-year IMS total cost per subscriber, normalized to traditional IMS at 1m. 비교 기준: 1 million subscribers, 2 million subscribers, 5 million subscribers. 판단: 위 So what 참조.

## 원본 관찰 및 시각화 설계
grouped: 가로축 가입자 규모, 세로축 공통 비용 지수, 모델별 세 막대. 데이터에서 계산한 절감률을 점선 괄호로 표시, 중립·짙은 녹색·연두색으로 모델 분리. 범례 아래 배치.

## 재사용 data_recipe (제안)
동일 서비스·품질 범위의 5년 구축비와 운영비를 연간화하고 가입자수로 나눈다. 기준 모델의 비용을 100으로 지수화한다. 각 규모별 비교모델 대비 절감률을 1−관리형 비용/비교비용으로 계산한다.

## 성립 조건 및 반례·한계
실제 통화 비용과 세부 모델 가정, 표본 수, 조사 시점 미공개. 원본 주석의 2m traditional 대비 −71% 등은 반올림이며 동일 서비스 수준·지역 규제·보안 요구 조건에 따라 우위가 달라질 수 있다.

## 사용법
`python chart.py --theme source --output source.png --dpi 200` 또는 `--theme neutral`. CSV의 group/series/value 및 config의 groups/series/colors를 함께 변경한다. 출처·분모·기간·provenance도 변경한다.

## 실제 검증
Source/Neutral 200dpi 렌더링 및 시각 확인, 로컬 테스트 6/6. 자체 충실도 4.71/5, verified. 원본 직접 이미지에서 9개 지수값, 순서, 0–120 축과 색·절감률 괄호를 확인. 절감률은 표시 지수로 재계산. 원본 서체·제목·부제 위치·여백 차이, 원본 오른쪽 Subscribers 축 라벨 생략. 사용자 검수는 pending.
