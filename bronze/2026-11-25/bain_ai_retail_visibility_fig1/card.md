# AI visibility and retail market share can diverge

## 원문 요지
쇼핑 여정에서 AI 답변이 상품과 판매점 탐색을 매개한다. 업종별 AI 가시성은 기존 유통시장 점유율과 차이가 있다. 상품정보와 차별화된 가치 제안 및 외부 인용을 관리하는 전략이 필요하다.

## So what
AI 검색 내 가시성은 기존 시장점유율과 일치하지 않으므로 두 지표를 업종별로 독립적으로 모니터링해야 한다.

## 비즈니스 맥락과 데이터
{
  "unit": "percent (both metrics, distinct denominators)",
  "period": "AI assistant weights: October 2026; prompt fieldwork date not disclosed",
  "denominator": "indexed top-20 retailer mentions vs category market share",
  "source": "Profound; Jefferies; Flywheel; Euromonitor International; Convenience Store News; Pyxis; company financials; Bain analysis",
  "sample": "4,400+ shopping prompts; 300,000+ runs across LLMs; top 20 indexed mentions",
  "provenance": "All numeric observations are printed on original figure; rank follows original display, not recomputed from rounded values.",
  "nominal_real": "not applicable",
  "missing": "raw data, detailed model or survey weights not disclosed"
}

## 시각화 관찰과 설계
{
  "x": "common percent length within panels",
  "y": "retailer order within vertical",
  "color": "two metrics",
  "size": "bar length from values",
  "sort": "original rank, including rounded ties",
  "labels": "reported values; percent labels"
}

## 재사용 data_recipe (제안)
1. 업종별 동일한 프롬프트 집합 및 기간을 정의한다.
2. 모델별 응답에서 판매점 언급 여부를 집계하고 모델 이용자 가중치를 적용한다.
3. 상위 20개 판매점 기준 인덱스와 별도 시장점유율을 조인한다.
4. 가시성 순위를 유지하고 같은 축에 두 지표를 나란히 표시한다.

## 조건·반례·한계
- 같은 업종 내 비교, 시장점유율의 정의 및 모델 가중치 일치
- 프롬프트 구성·모델 버전이 바뀌면 순위가 달라질 수 있음
- AI 언급은 실제 구매, 매출 기여 또는 인과효과를 의미하지 않음

## 원본과 차이
Overall 탭만 정적 구현. 다른 탭 및 hover 미구현; 로고 미포함; 제목, 각주를 재작성; 원본 좌측 숫자 순위열과 패널 구분선 유지.

## 계산법 및 해석
AI 가시성은 해당 판매점 언급 실행을 판매점 언급이 있는 실행으로 나누고 AI 서비스 월간 이용자 기준으로 가중해 상위 20개 기준으로 인덱싱했다. 시장점유율은 별도 분모이며 카테고리별 프롬프트 구성 차이도 존재한다. 상위 5개만 표시되므로 합계가 100%일 필요는 없다.

인사이트 유형: Benchmark gap.

## 실행
`python chart.py --theme source --output source.png --dpi 200` (neutral도 동일). CSV와 config의 THEME/CONTEXT를 바꿔 재사용.

출처: https://www.bain.com/insights/ai-is-the-new-search-heres-how-retailers-win-the-answer/ · Figure 1 — Overall tab · 게시 2026-11-21 · 수집 2026-11-25
