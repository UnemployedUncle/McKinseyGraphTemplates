# The Geopolitics of Critical Minerals: Navigating Scarcity, Concentration, and Control — Exhibit 3

**출처:** https://www.bcg.com/publications/2026/critical-minerals-geopolitics  
**실제 게시일:** 2026-11-03 / **수집·코드 생성일:** 2026-11-04 / **데이터 관측 기간:** research published 2026-11-03; underlying mineral snapshot dates undisclosed

## 원문의 글 요지 (직접 작성한 세 문장)
원문은 23개 핵심광물에 대한 매장·채굴·정련·제조 및 국제 소유망을 분석한다. Exhibit 3은 광물별 채굴과 정련 시장 집중도를 두 축에 배치하고 중국의 수출통제 대상 여부를 표시한다. 정련 집중도가 높은 광물은 채굴국이 다변화되어도 실질 공급망 위험이 남을 수 있다.

## So what (한 가지)
핵심광물의 채굴과 정련은 서로 다른 국가·기업에 집중될 수 있어 공급망 다변화 전략은 생산국뿐 아니라 정련의 집중도와 수출통제 대상 여부를 함께 평가해야 한다.

## 비즈니스 맥락 → 지표 → 판단
- 사실: 공식 보고서의 연구 대상과 공개 수치 또는 공식 차트상 도형을 기반으로 한다.
- 관찰: `집단별 비교·위험 집중 / quadrant scatter`를 통해 비교 분모와 차이의 의미를 강조한다.
- 해석: 핵심광물의 채굴과 정련은 서로 다른 국가·기업에 집중될 수 있어 공급망 다변화 전략은 생산국뿐 아니라 정련의 집중도와 수출통제 대상 여부를 함께 평가해야 한다.
- 재사용 제안: 동일한 분모·기간의 비즈니스 데이터로 교체하기 전 인과관계, 모델 가정, 표본을 점검한다.

## 지표와 출처·단위
```json
{
  "observation_unit": "mineral",
  "x": "extraction_concentration",
  "y": "processing_concentration",
  "color": "group",
  "unit": "concentration index (0-1)",
  "denominator": "mineral-specific concentration definition not numerically disclosed; see official methodology",
  "period": "research published 2026-11-03; underlying mineral snapshot dates undisclosed",
  "provenance": "digitized_estimate",
  "uncertainty": "coordinate ±0.04, based on manual interpretation of official 499-pixel preview",
  "sampling": "20 visually legible points out of chart; one or more labels may be omitted, not exhaustive"
}
```
공식 원본 식별자는 `Exhibit 3`이며 원본 이미지 및 로고 파일은 배포하지 않는다. 관측치별 provenance는 CSV에 기록하고 도형 판독값은 수치 추정으로 명확히 구분한다.

## 그래프 설계와 강조 근거
x=extraction index, y=processing index; point marker and color encode source-figure leader/control classification; one point per mineral. Both axes span 0–1 with 0.5 horizontal reference. The source labels many points; template uses data-driven placements with manual legibility offsets.
색상·마커·제목·여백·주석은 `config.json`에서 분리한다. 원본 글꼴·워드마크는 포함하지 않는다. 축·그룹·데이터의 정렬은 재사용 데이터의 정렬을 유지한다.

## data_recipe — 다른 업무에 적용하는 절차
1. Secure minerals and jurisdiction-level extraction/processing market shares for the same period.
2. Compute concentration using the source-defined index, not raw percentages.
3. Mark each mineral by the leader and official export-control policy at the snapshot date.
4. Plot x extraction / y processing on 0–1 scales; annotate selected risk minerals.
5. Validate the raw point coordinates against the original source dataset before claiming research-grade accuracy.

## 메시지가 성립하는 조건 및 반례
- Only compare x and y if underlying concentration-index methodology matches.
- Do not interpret estimated coordinates as directly reported values or exact current policy classification.
- Labels overlap, original downloadable data unknown; direct original image was viewed but fidelity of complete chart remains unverified.

## 확인된 한계와 검증 구분
- Source Exhibit 3 static graphic inspected. Diagram type is similar; estimated points, partial label placement, legend layout and typography differ; not a quantitative exact reproduction.
- 자체 원본 충실도: 평가하지 않음 (`fidelity_score=null`); 실행 성공과 원본 정확성, 사용자 검수는 별개이다.
- `human_review=pending`; 제3자 콘텐츠의 외부 AI 학습 이용 권한 확인 전까지 `training_eligible=false`.

## 사용법
`pip install -r requirements.txt` 후 `python chart.py --theme source --data data.csv --config config.json --output source.png` 혹은 `--theme neutral`로 실행한다. 생성 이미지는 불변 Bronze 바깥 `artifacts/`에 보관한다.
