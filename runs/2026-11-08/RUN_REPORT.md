# 주의: 데이터 단위 오류 수정 및 새 불변 Bronze 버전 (2026-11-08)

초기 GitHub 커밋 `ff5be245e5ca5223f65062ac5df252982eceb38d`의 BCG Exhibit 2 CSV에서 **비율값의 단위가 `percentage points`로 잘못 기록**되었고, 오차 필드가 `uncertainty_pct`로 작성되었습니다. 이 데이터 의미 검증 오류는 재사용에 영향을 줄 수 있으므로 새 불변 Bronze 버전 `bronze/2026-11-08/bcg_market_leader_value_capture_tenure_ex2_rev_e7c87238d0c9/`을 추가했습니다. 수정본은 **단위 `percent`**, 판독오차 `uncertainty_pp=4`로 의미를 분리했으며 기존 최초 묶음은 변경하지 않았습니다. **BCG 원본은 코드/교육용 재사용에는 수정본만 사용**합니다. 신규 주제는 2건으로 유지되지만 첫 버전 포함 저장된 Bronze 묶음은 3개이며 커밋 후 누적은 **45건**입니다. McKinsey 원본 묶음은 그대로 유지합니다. 현 실행 6개 단위 테스트와 4개 PNG 렌더링 완료; GitHub Actions는 최초 커밋 success이고 최종 수정 커밋 상태는 07:15 전 또는 전달 전 확인해야 합니다.

# Consulting Graph Template — 준비 보고서 / 2026-11-08 (Asia/Seoul)

**모드:** 03:15 준비 단계. **시작:** 2026-11-08 03:19 KST. **완료:** 2026-11-08T03:33:01+09:00 KST. **목표/완료:** 3/2건. **기준 Git:** main, parent `1287efcd5110e538920cd54693fff5500b418810`. **새 파일:** Bronze 3묶음(2주제+BCG 수정본), 24개 파일. **당일 신규 자체 원본 재현 통과:** 0 (두 건 모두 unverified). **기존 누적:** Bronze 42 → 커밋 후 45, Silver 0, Gold 0, 과거 자체 원본 통과 12. **승인:** 모두 pending. **코드 테스트:** 6/6 통과. **렌더링:** PNG 200dpi 4개 확인. 원본 정확성·코드 실행·사용자 검수는 별개.

## 1) BCG — 기업의 장기 선도 지위가 실제 신규 가치 포획으로 연결되는가?

- **원문 게시일** 2026-11-06; **수집일** 2026-11-08; **자료 기준** 2015–25 누적 가치 창출 / 2025 상위5기업의 과거 tenure; **Exhibit 2**.
- **공식 URL** https://www.bcg.com/publications/2026/market-leaders-staying-on-top-longer
- **한 줄 So what:** 업계 상위 지위를 오래 유지한다는 사실만으로 경쟁우위를 인정하지 말고, 최근 10년 새로 창출된 가치의 포획률과 함께 판정해야 한다.
- **그래프 설계:** X `value_capture_pct`, Y `tenure_pct`, 14개 읽을 수 있는 산업 라벨·점 표시·선택 산업 강조. 서로 정의가 다른 두 지표를 함께 판단하려는 목적의 scatter. 실제 원본도 산점도이지만 이번 50% 분할선과 강조색은 편집적 선택.
- **값의 출처:** 499×377 저해상도 공식 Exhibit 2 이미지에서 판독한 추정 좌표 14개, **digitized_estimate / ±4%p**, 정확한 원자료 없음. 분모: 각 업종 상위 5개 기업. 전체 보고서는 15개 업종이므로 커버리지 14/15, 잔여 1개를 임의로 보간하지 않음.
- **한계:** 개별 기업의 시총 자료를 사용해 재계산하지 않았고, 겹친 라벨은 혼동될 수 있으므로 fidelity_score=null, `unverified`. 원문 데이터 학습 이용 권한이 제공된 것은 아님.
- **재사용:** 특정 품목·거래선의 시장 지위 유지와 신규 이익풀 확보를 함께 비교. 관측단위 `industry × period`; 데이터 수집→상위5 업체 선정→가치 증분과 상위5 점유 산출→활동기간 비교→표시.
- **Git 재사용 권장:** `bronze/2026-11-08/bcg_market_leader_value_capture_tenure_ex2_rev_e7c87238d0c9/`. 최초 버전은 수정 전 이력으로 유지됨. 그림은 Git에 넣지 않고 GitHub Actions 아티팩트 또는 일일 패키지에서 조회.

## 2) McKinsey — 97개 항공사의 경제적 이익이 상·하위 기업에 극단적으로 분포

- **원문 게시일** 2026-11-06; **수집일** 2026-11-08; **자료 기준** 2025; **Exhibit 2의 본문 공개값**.
- **공식 URL** https://www.mckinsey.com/industries/travel/our-insights/could-aviation-at-last-be-close-to-earning-its-wings
- **한 줄 So what:** 항공업 평균 손익에 의존하지 말고, 상위·하위 기업별 경제적 이익 분포를 분리해 기업가치를 평가해야 한다.
- **공식 수치:** 상위 20개 항공사 +14.0bn USD, 가운데 57개 −2.3bn USD, 하위 20개 −22.9bn USD. 세 집단 합계 **−11.2bn USD** vs 기사 산업 전체 **−12.8bn USD**는 1.6bn USD 차이가 있음. 정확한 보정 근거 미공개; 97개 표본과 산업 전체의 범위 차이 가능성만 제기, 확정하지 않음.
- **차트 설계:** 원본은 **power curve**이나 SVGZ가 시각적으로 열리지 않아 원본을 그대로 재현하지 않음. 원문 본문 집단합계에서 유도한 **편집형 diverging bar** (X USD billion, 0 기준 양/음, Y 세 집단, 집단 수 직접 표시). 원본 그래프 정밀 재현 `unverified`; 점수 null.
- **재사용:** 사업부·제품군 간 투자자본비용 대비 초과수익이 극단적으로 치우치는지 진단. ROIC·WACC·투자자본에서 economic profit 산출→상·중·하위 구간 집계→표본 구성/전체 차이를 별도 표시.
- **Git:** `bronze/2026-11-08/mckinsey_airline_economic_profit_quintiles_ex2/`.

## 3) Bain 제외

최근 7일 우선, 이후 30일 범위를 확인했으나 **게시일·정량 원본·기존 카탈로그 중복 여부를 모두 검증할 수 있는 새 Figure 미확보**. 이전 10월29일 리테일 이익 Figure 1은 기존 Bronze 수록, 중복 적재하지 않음.

## 재현·코드 검증

`python -m unittest discover -s tests -v`는 신규 템플릿 및 메달리온 파일에 대해 **6개 통과**. source/neutral PNG는 네 개 직접 확인하였고, 해상도 200dpi. 임시 코드를 원본 불변 묶음에 포함시키지 않았고 generated PNG는 별도 artifacts에 두었음. 

`python chart.py --data data.csv --config config.json --theme source --output source.png` / `--theme neutral`. 재사용 변경 범위는 `data.csv`, `config.json`의 `THEME`와 `CONTEXT`이다. 만약 Bronze 내용을 수정하고자 하면 기존을 덮지 말고 새 ingest revision으로 생성할 것.

**원본 파일·로고·폰트·원문 전문 Git 저장 없음**, third-party source 이용에 대해 사용자 검수와 학습 권리 확인이 별도로 필요. 데이터 학습은 실행하지 않음.

## 07:15 전달 체크리스트

1. GitHub `main:runs/2026-11-08/prepared.json`과 본 보고서를 먼저 읽는다. 해당 파일이 없으면 준비 완료를 추정하지 않는다.
2. GitHub manifest, catalog/index.json, latest commit, Actions 렌더링 아티팩트 실제 완료 여부 확인.
3. 이 날짜에 **한 번만** BCG·McKinsey 차트 핵심 분석, 이미지/코드 링크, 2/3 결과, 45/0/0, 원본 verified 신규0, Bain 제외 이유를 사용자에게 알린다. 새 리서치·신규 주제·기존 차트 재생성을 시작하지 않는다.
4. `delivered=false`를 사용자가 자동으로 학습 완료한 상태로 해석하지 않는다. 사용자 승인·Silver/Gold 승격 금지.

