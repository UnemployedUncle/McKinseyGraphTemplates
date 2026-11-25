# Bain | Figure 2 — grocery citations by source type

출처: https://www.bain.com/insights/ai-is-the-new-search-heres-how-retailers-win-the-answer/

게시: 2026-11-21 / 수집: 2026-11-26 / 조사: 2026; exact collection dates not disclosed

## 요지 (원문 사실과 해석)
AI가 상품 탐색을 중개하면서 소매업체의 노출 경쟁이 바뀌고 있다. 식료품 답변에서 인용하는 출처는 플랫폼마다 다르다. 기업은 자체 사이트와 외부 콘텐츠를 함께 관리하며 출처 구성을 추적할 필요가 있다.

## So what
AI 검색 최적화에는 플랫폼별 인용 출처 구성을 구분한 콘텐츠 전략이 필요하다.

## 비즈니스 맥락 → 데이터 → 판단
플랫폼마다 어떤 출처를 근거로 답변하는지 진단. 지표 단위: percent of citations per assistant. 분모: All source occurrences in what-to-buy and where-to-buy grocery prompts per assistant. 비교 기준: ChatGPT, Google AI, Google Gemini, Claude. 판단: 위 So what 참조.

## 원본 관찰 및 시각화 설계
stacked: 동일 폭 세로 100% 누적막대, 플랫폼 순서 유지, 출처 유형별 고정색, 공개 레이블만 표기. 상단 범례, 하단 출처·추정 경고. 작은 구간은 별도 수치 라벨 없이 표현.

## 재사용 data_recipe (제안)
플랫폼별 인용 발생 건수를 출처 유형별로 집계하고 각 플랫폼의 전체 인용수로 나눈다. 분류를 동일하게 유지하고 중복 인용 발생 건수 처리 기준을 고정한다. 공개 라벨과 판독 추정치를 구분하고 반올림 합계는 도형만 정규화한다.

## 성립 조건 및 반례·한계
인용 구성은 클릭률·매출 기여가 아니다. 프롬프트와 모델 버전이 바뀌면 결과도 바뀐다. 비표시 세부 구간은 썸네일의 100% 축 412px 및 경계 판독으로 반올림한 추정값(±1%p); 0 추정도 확정 0이 아니다. 표본 수와 상세 조사일 미공개. 원본 hover는 재현하지 않음.

## 사용법
`python chart.py --theme source --output source.png --dpi 200` 또는 `--theme neutral`. CSV의 group/series/value 및 config의 groups/series/colors를 함께 변경한다. 출처·분모·기간·provenance도 변경한다.

## 실제 검증
Source/Neutral 200dpi 렌더링 및 시각 확인, 로컬 테스트 6/6. 자체 충실도 4.43/5, unverified. 원본 정적 썸네일의 4개 플랫폼과 8개 색상, 0–100% 축, 표시된 라벨을 유지. 12개 미표시 구간은 약 ±1%p 판독치이므로 값 항목 감점. 정규화로 인한 도형 차이, 원본 6열 범례와 글꼴·비율 차이. hover 미구현. 사용자 검수는 pending.
