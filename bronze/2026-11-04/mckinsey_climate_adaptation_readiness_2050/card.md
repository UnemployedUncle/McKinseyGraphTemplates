# Advancing adaptation: Breaking barriers to a trillion-dollar opportunity — By 2050 deployment-ready climate adaptation will grow (web graphic context; editorial decomposition)

**출처:** https://www.mckinsey.com/mgi/our-research/advancing-adaptation-breaking-barriers-to-a-trillion-dollar-opportunity  
**실제 게시일:** 2026-11-03 / **수집·코드 생성일:** 2026-11-04 / **데이터 관측 기간:** modeled 2050; 2020 price base

## 원문의 글 요지 (직접 작성한 세 문장)
McKinsey Global Institute는 20개 검증된 기후적응 조치의 투자 필요액과 집행 장벽을 분석했다. 2050년 2°C 온난화 조건에서 즉시 집행 가능한 조치 비용을 연간 약 4,600억 달러로 추정한다. 나머지 약 6,900억 달러는 수요·조정 역량 또는 자금조달 장벽에 직면해 필요액이 그대로 시장 규모로 전환되지 않는다.

## So what (한 가지)
2050년 연간 기후적응 필요액 중 약 4,600억 달러가 현재의 조건 아래 집행 가능한 반면 약 6,900억 달러는 수요·자금 조달 장벽에 직면하므로, 투자기회를 평가할 때 사회적 필요와 실제 실행가능성을 구분해야 한다.

## 비즈니스 맥락 → 지표 → 판단
- 사실: 공식 보고서의 연구 대상과 공개 수치 또는 공식 차트상 도형을 기반으로 한다.
- 관찰: `부분 대비 전체·자금조달 장벽 / editorial stacked bar`를 통해 비교 분모와 차이의 의미를 강조한다.
- 해석: 2050년 연간 기후적응 필요액 중 약 4,600억 달러가 현재의 조건 아래 집행 가능한 반면 약 6,900억 달러는 수요·자금 조달 장벽에 직면하므로, 투자기회를 평가할 때 사회적 필요와 실제 실행가능성을 구분해야 한다.
- 재사용 제안: 동일한 분모·기간의 비즈니스 데이터로 교체하기 전 인과관계, 모델 가정, 표본을 점검한다.

## 지표와 출처·단위
```json
{
  "observation_unit": "global adaptation-readiness segment, year 2050 scenario",
  "metric": "annual adaptation costs",
  "unit": "USD billion, real 2020 prices",
  "denominator": "20 proven adaptation measures under 2°C 2050 scenario",
  "period": "modeled 2050; 2020 price base",
  "provenance": "reported",
  "rounding": "460+690=1150 (USD bn); original says approx 1.2 trillion rounded, not exact equality",
  "sampling": "20 measures, 1 km geographic pixels and 9 population-demographic groups, scenario modeling (not respondent survey)"
}
```
공식 원본 식별자는 `By 2050 deployment-ready climate adaptation will grow (web graphic context; editorial decomposition)`이며 원본 이미지 및 로고 파일은 배포하지 않는다. 관측치별 provenance는 CSV에 기록하고 도형 판독값은 수치 추정으로 명확히 구분한다.

## 그래프 설계와 강조 근거
x=annual estimated cost share of 460+690, y=one 2050 scenario, fill by deployment readiness, labels show reported $ billions plus shares derived using component sum. No misleading separate percentage axis; reading order ready then barriers.
색상·마커·제목·여백·주석은 `config.json`에서 분리한다. 원본 글꼴·워드마크는 포함하지 않는다. 축·그룹·데이터의 정렬은 재사용 데이터의 정렬을 유지한다.

## data_recipe — 다른 업무에 적용하는 절차
1. Define 20 hazard-protection measures, exposure geography and common price year.
2. Estimate annualized capital plus operating costs under consistent climate scenario.
3. Classify each measure/location as deployment-ready or requiring demand or financing interventions.
4. Sum each class at the global level, retain exact vs rounded totals separately.
5. Render 100% shares from reported components while labeling original absolute amounts.

## 메시지가 성립하는 조건 및 반례
- Model estimates, not realized 2050 spending or financial addressable market guarantees.
- Reported total ~$1.2T is rounded; do not force 460/690 to sum to 1200.
- The original report embeds a larger interactive breakdown; this is an editorial two-segment summary, not original Exhibit replication.

## 확인된 한계와 검증 구분
- McKinsey official HTML narrative and graphic text checked; original interactive visual geometry not verified. This is a clearly labeled editorial summary.
- 자체 원본 충실도: 평가하지 않음 (`fidelity_score=null`); 실행 성공과 원본 정확성, 사용자 검수는 별개이다.
- `human_review=pending`; 제3자 콘텐츠의 외부 AI 학습 이용 권한 확인 전까지 `training_eligible=false`.

## 사용법
`pip install -r requirements.txt` 후 `python chart.py --theme source --data data.csv --config config.json --output source.png` 혹은 `--theme neutral`로 실행한다. 생성 이미지는 불변 Bronze 바깥 `artifacts/`에 보관한다.
