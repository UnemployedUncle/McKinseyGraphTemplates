# Banking agentic AI: build, ramp-up and payback

## 원문 요지
은행의 Agentic AI 경쟁은 비용절감뿐 아니라 조직의 실행 속도와 고객 접점 변화에 달려 있다. 52개 사례에서 구축과 완전한 효과 달성까지의 평균 기간을 업무 영역별로 비교한다. 투자회수 및 ROI 추정은 구축 후 효과 발생과 운영비용 가정에 의존한다.

## So what
Agentic AI 투자회수기간과 완전한 효과 도달 기간은 다른 지표이므로 구축·램프업·손익 회수의 세 기준을 분리해야 한다.

## 비즈니스 맥락과 데이터
{
  "unit": "months; case counts; ROI multiple",
  "period": "Client interviews Sep–Oct 2026; 3-year ROI model; parent report Nov 17, PDF month Nov 2026",
  "denominator": "domain-level use cases; 52 total",
  "source": "Client interviews, September–October 2026; McKinsey AI ROI benchmark",
  "sample": "52 use cases: 33 operations, 7 risk, 4 knowledge, 4 software, 4 other",
  "provenance": "All printed values reported; 10 and 2.9 are approximate. Domain payback and ROI missing.",
  "nominal_real": "not applicable; ROI formula as source footnote, price basis not disclosed",
  "missing": "raw cases, aggregation weights, individual cashflows not disclosed"
}

## 시각화 관찰과 설계
{
  "x": "ordered domains and separate published aggregate",
  "y": "duration months",
  "color": "build vs ramp-up",
  "size": "bar length from values",
  "sort": "original order, aggregate last",
  "labels": "component values, total, case-count row, separate summary KPIs"
}

## 재사용 data_recipe (제안)
1. 도메인별 실제 구축 시작·완료 및 효과 정착 날짜를 정의한다.
2. 동일한 월 단위로 구축·램프업 기간을 구분해 집계한다.
3. 사례수와 집계방식을 별도 표시한다.
4. 현금흐름 정의에 따른 투자회수 및 ROI를 별도로 계산해 요약한다.

## 조건·반례·한계
- 기간과 현금흐름 정의가 같아야 비교 가능
- 집계 평균의 가중 방식은 미공개, 공개 평균을 재계산하지 않음
- 10개월은 전체 착수부터 회수까지라는 뜻이 아님
- 선별된 사례 표본이며 모든 AI 사업의 보장 수익이 아님

## 원본과 차이
PDF 원본의 누적막대, 구분선, 사례수 행, 요약 KPI 보존. 제목과 각주를 재작성하고 폰트·여백은 근사. 로고 없음.

## 계산법 및 해석
공식 상위 보고서 발행일은 11월 17일이고 PDF 표지에는 2026년 11월만 표기된다. 평균 13개월은 공개 집계값이며 표본별 가중치 미공개. 3년 ROI의 원문 산식 설명은 연간 영향 2배에서 연간 운영비 2배와 구축비를 차감하는 방식으로 첫 해 효과를 0으로 가정한다. 정확한 비율 분모와 사례별 현금흐름은 공개되지 않았다.

인사이트 유형: Time to value.

## 실행
`python chart.py --theme source --output source.png --dpi 200` (neutral도 동일). CSV와 config의 THEME/CONTEXT를 바꿔 재사용.

출처: https://www.mckinsey.com/~/media/mckinsey/industries/financial%20services/our%20insights/global%20banking%20annual%20review%202026%20part%202/global-banking-annual-review-2026-the-ai-disruption-dividend.pdf · PDF page 2 (zero-based page 2), Exhibit 1 — time to value by domain · 게시 2026-11-17 · 수집 2026-11-25
