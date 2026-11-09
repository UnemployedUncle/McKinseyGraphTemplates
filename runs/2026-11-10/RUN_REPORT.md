# Consulting Graph Template — 2026-11-10 사전 준비 기록

## 실행 요약
- 작업 예정 03:15 Asia/Seoul, 실제 시작 03:19:41; 준비본 확정: `2026-11-10T03:41:29+09:00`.
- 목표 회사별 3건 중 공식 원문 기준 중복 없는 정량 차트 **2개 신규 제작**: BCG 1, McKinsey 1, Bain 0. 공식 원본의 이용제한과 게시일 및 자료 시점 구분을 검토함.
- GitHub `main`에는 신규 Bronze 2건을 적재하고 원격 파일 16/16 일치를 조회. 누적 Bronze **50**, Silver **0**, Gold **0**; 역사적 원본 재현 `verified` **13건** (오늘 신규 0건). 누적 수치와 자동 점수는 사용자 승인과 별개.
- 단위 테스트 **8/8** 통과; `source.png`, `neutral.png` 각 2장, 총 4장 200dpi 실행·직접 확인. 둘 다 편집형/원본 시각 미확인 등으로 `fidelity_score=null`, `validation_status=unverified`.
- 신규 `human_review=pending`, `training_eligible=false`. Silver/Gold 생성, 수동 승격, 외부 모델 재학습 일절 없음.

## 1. BCG: Medtech 상업모델 혁신과 장기적 투자수익
- 공식 기사: **Beyond the Milkman: AI's New Playbook for Medtech Commercial Excellence**, 게시일 **2026-11-02**, 출처 https://www.bcg.com/publications/2026/ai-medtech-commercial-operations . **Exhibit 2** 원본 그림을 공식 웹에서 직접 열어 유형과 데이터 종료값 확인; 자료는 2012–2021 장기 집단, 2025년 종료 최근 연구집단. 수집일 2026-11-10. (7일 내 적격 비중복 미확보 → 30일 확장).
- **So what**: 영업조직의 AI 투자 성과는 채택률뿐 아니라 상업모델 변화와 상대적 장기 수익성과 함께 측정해야 한다. 인과효과가 아니라 연관성이다.
- 공식 표기 투자지수(시작 $100): 역사적 전환 집단 1,001, 업종 벤치마크 430 (CAGR 27%, 17%). 최근 구간 전환 집단 161, 벤치마크 112 (CAGR 10%, 2%). `data.csv` 4행 값 모두 `reported`, 정확한 코호트 수·중간 시계열 수치·리밸런싱 모델 미공개.
- 원본은 기간별 두 계열 **시계열 선그래프**. 공개되지 않은 중간점을 지어내지 않기 위해 종료값만의 2패널 `endpoint_lollipop`으로 **편집**; 원본 재현으로 검증 통과시키지 않음. 두 패널 X축 눈금은 서로 달라 패널 사이 가로길이 직접 비교 금지.
- 재사용: 데이터 필드 `period`, `cohort`, `value_index`, `annualized_cagr_pct`, `provenance`; 업종별 전환 여부와 정규화된 TSR 지수의 비교. 선정편향·회사규모·기간 차이를 인과효과로 혼동하지 않을 것.
- 실행 검증 2 PNG 성공, 원본 재현 점수 null; 파일 경로 `bronze/2026-11-10/bcg_medtech_transform_tsr_ex2_endpoints/`, payload `eb4566939caee0bdaa65938e151fa3ce4d9875ed4b78f3ba4f15c0b6108fc2e0`.

## 2. McKinsey: 동일 적립액에서 비용과 상품구성의 차이
- 공식 기사: **The 1 Percent Wake-up Call for Life Insurers**, 게시일 **2026-11-03**, 출처 https://www.mckinsey.com/industries/financial-services/our-insights/the-1-percent-wake-up-call-for-life-insurers . **Exhibit 1** 원본 SVGZ 렌더 접근은 실패했지만 공식 HTML의 상세 이미지 설명에서 두 패널과 수치를 확인. 검색 수집일 2026-11-10, 분석 가정은 월 €100/30년, EIOPA 2026 등 참조. (게시일 7일 경계).
- **So what**: 상품 선택을 비교할 때 고정 납입액 외에 연간 총비용과 수익률·보증 가정을 명시적으로 분리해야 한다.
- 상단(모두 gross 수익률 7%, 30년 월 €100): 국가 기본펀드 연 0.1% 비용→€120,000; 네오브로커 ETF 0.2%→€117,000; 보험사 유닛링크 1.85%→€86,000. `derived`: 최고/최저 €34,000 차이.
- 하단(서로 다른 gross/위험): 기존 보증 보험 3.2% 수익·1.5% 비용→€47,000; 네오브로커 ETF 7%·0.2%→€117,000. `derived` €70,000 차이는 수수료만의 인과효과가 아님.
- 모든 `final_savings_eur`은 **공식 모형 예시값 `reported`**이지 관측 실적이 아니고, 장래 수익을 보장하지 않음. 원본 시각을 직접 열 수 없어 편집형 2패널 `horizontal_bar`; `fidelity_score=null`, `unverified`.
- 재사용: `scenario`, `product`, `final_savings_eur`, `annual_cost_pct`, `annual_gross_return_pct`, `horizon_years`, `monthly_contribution_eur`; 동일 시뮬레이션 조건과 위험별 패널 분리.
- 실행 검증 2 PNG 성공; 파일 경로 `bronze/2026-11-10/mckinsey_insurance_30y_savings_cost_ex1/`, payload `9ab2365a0b78dacb7a7ca0ba3b2556ea7facc2446b246e5f0639ccf2954d5a03`.

## 제외: Bain
공식 Bain 사이트에서 2026-11-03~11-10 최근 7일과 2026-10-11~11-10 30일 범위를 검색했으나, 정확한 게시일·접근 가능한 독립 정량 Figure·기존 48건과의 비중복을 모두 입증할 신규 사례가 없어 제외. 적격하지 않은 오래된 자료 또는 기존 Figure를 중복 사용하지 않음.

## 검증/코드 사용
- `python -m unittest discover -s tests -v` ⇒ **8 passed**.
- 각 번들의 CLI: `python chart.py --data data.csv --config config.json --theme source --output source.png` 및 `--theme neutral --output neutral.png` ⇒ 총 4 PNG, ~200 dpi.
- `scripts/medallion.py ingest`로 파일 해시·payload·`human_review=pending` 생성 및 `validate` 로컬 통과. GitHub `main`에서 16개 신규 파일을 각각 재조회해 내용이 정확히 같음을 확인한 뒤 `catalog/index.json`, `catalog/README.md`, `dataset/bronze.jsonl`를 갱신. 원격 catalog 50/0/0 확인. **GitHub 커밋은 커넥터의 독립 create/update API 특성상 파일별 커밋으로 직렬 생성**했음; 기존 자료·검수본 삭제 없음.
- Source·Neutral PNG는 GitHub Bronze에 포함하지 않으며 다운로드 아카이브에만 보존. 원본 보고서 이미지·원문 전문·원본 로고·폰트 파일을 저장하지 않음.
- 원본 정확성/코드 실행/사용자 검수는 서로 구분; 기존 verified 13건도 사용자 승인 0건.
- GitHub Actions: push 실행의 완료 상태는 사용 가능한 연결 도구에서 확인되는 경우에만 보고. **미확인 상태를 success로 표시하지 않음**.

## 전달 관리
- 아침 전달 시 `runs/2026-11-10/prepared.json`과 이 보고서를 GitHub `main`에서 먼저 조회하고 확인된 **같은 2개 주제만** 07:15에 한 번 제공할 것. 새로운 조사·차트 생성·중복 커밋·검수 승인 없음.
- `prepared_complete=true`는 게시와 검증 및 기록에 대한 상태이며 사용자 학습·검수 완료가 아님. `delivered=false`는 아침 전달 전 상태.
