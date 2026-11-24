# Physical AI: labor savings and new demand in Japan

## 원문 요지
일본은 인력 부족과 제조기술 기반 때문에 Physical AI의 중요한 시험 시장이다. 기술 진전 시나리오에 따라 자동화 가능한 작업과 가치 상한이 크게 달라진다. 기업은 기술 성숙도와 실제 운영 환경을 함께 검토해야 한다.

## So what
기술 진전 수준에 따라 일본 Physical AI의 2040년 기술적 가치 상한이 크게 달라지므로 투자 판단에서 시나리오를 분리해야 한다.

## 비즈니스 맥락과 데이터
{
  "unit": "USD billion/year; GDP share percent",
  "period": "2040 scenario; GDP denominator FY2025; FX 2025 average",
  "denominator": "annual Japanese addressable value; FY2025 Japan GDP for percentage",
  "source": "US BLS; US Department of Labor O*NET; IFR; company data; expert interviews; BCG Institute analysis",
  "sample": "20 industries, 232 occupations, approximately 7,500 tasks mapped to O*NET",
  "provenance": "All numeric observations are printed on original figure; calculated bar stack total equals printed total.",
  "nominal_real": "price basis not disclosed; USD converted at 2025 average FX",
  "missing": "raw data, detailed model or survey weights not disclosed"
}

## 시각화 관찰과 설계
{
  "x": "ordered scenarios",
  "y": "annual USD billion",
  "color": "cost savings vs new value",
  "size": "bar length from values",
  "sort": "restricted, medium, maximum",
  "labels": "component values, totals, GDP percentages"
}

## 재사용 data_recipe (제안)
1. 기준연도 직종·업무별 인원과 임금을 정리한다.
2. 기술 시나리오별 업무 대체율로 절감 가능 가치를 산출한다.
3. 미충족 수요와 수익성·확장 가정을 반영해 추가 가치를 산출한다.
4. 두 구성값을 합산하고 동일한 기준 GDP 대비 비중을 주석으로 표시한다.

## 조건·반례·한계
- 비용절감과 추가 가치의 중복 집계 방지
- 최대 기술적 대체율은 실현율이 아님
- 자본비용·규제·현장 적합성 및 사회적 수용성이 제약
- 모형의 세부 입력 및 가격 기준은 미공개

## 원본과 차이
원본 누적 막대 구조, 순서, 색, 총합, GDP 비중 유지. 글꼴, 제목·각주 재작성, 원본 오른쪽 수직 괄호 대신 범례 사용. 로고 미포함.

## 계산법 및 해석
절감 가치는 인원·임금과 기술 대체율에 기반하고 신규 가치는 수익성과 기술 대체율 및 수요 확대 가정에 의존한다. 최대 $450bn은 2040년 기술적 상한이며 실현 매출이나 GDP 증가 예측이 아니다.

인사이트 유형: Scenario ceiling.

## 실행
`python chart.py --theme source --output source.png --dpi 200` (neutral도 동일). CSV와 config의 THEME/CONTEXT를 바꿔 재사용.

출처: https://www.bcg.com/publications/2026/physical-ai-japan-value-opportunity · Methodology sidebar exhibit — cost savings and new value · 게시 2026-11-24 · 수집 2026-11-25
