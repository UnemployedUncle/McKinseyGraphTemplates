# BCG | Full-potential carve-outs — Exhibit 1

## 원문 요지 (직접 작성, 3문장)
일반적 사업분리와 달리, 분리 대상과 존속 기업 양쪽의 운영모델을 재설계하는 접근은 장기 주주수익 성과가 더 높은 사례와 연결되어 있다. BCG는 거래 이후 24개월 시점에서 두 유형의 누적 상대 TSR 지수 차이를 제시한다. 이 차이는 분리 자체보다 양 회사의 전략·실행 재구성이 중요할 수 있다는 메시지를 지원한다.

## So what (단 하나)
**Carve-out 실행 계획은 거래 종결/분리뿐 아니라 NewCo·RemainCo 양측의 전략·운영모델 재설계를 성과관리 범위에 포함해야 한다.**

## 원문 사실 → 관찰 → 해석 → 재사용
- **원문 사실:** 2026-10-28 발행, Exhibit 1. 공개 그림의 9개 후속시점 직접 라벨을 `reported`로 전사. 최종 24개월 상대 TSR 지수는 full-potential 121.1, all carve-outs 100.8. BCG 본문은 TSR 격차를 20.3 percentage points라고 서술.
- **관찰:** 24개월 이후 차이 = 121.1−100.8 = **20.3 지수 포인트**. 그래프 숫자의 index point와 본문에서 쓰는 TSR %p는 표기·분모가 다르므로 혼용하지 않는다.
- **해석:** 가치창출을 목표로 한 재설계가 더 큰 성과를 보이는 연관성을 시사하지만, 거래 선정효과 등으로 인과효과가 증명된 것은 아니다.
- **재사용 제안:** 사업분리/PMI/운영모델 재설계 프로젝트의 비교 집단 이벤트 상대 지수 분석에 적용.

## Business context → metric → decision
- **비즈니스 맥락:** 자산 매각 이후 주주성과 개선의 근원 평가.
- **지표:** 누적 relative total shareholder return **index**. 단위: index points. 기간: T-3 days baseline through 24 months, 동일 거래 이벤트 이후 경과기간. 지수 기준선: 100. 분모: BCG의 상대 TSR 지수 산출 기준; 회사별 종목·가중치·거래별 표본 세부값은 공개 그림만으로 검증 불가.
- **비교 기준:** full-potential carve-outs vs all carve-outs. 표본 중첩 가능성에 유의.
- **판단:** 분리 후 운영모델 변화까지 투자안에서 관리할 필요 여부.

## 인사이트 및 시각화 원칙
- **Insight type:** time-indexed cohort divergence.
- **X:** 이벤트 후 경과시점(`period_label`, 순서는 `order`). **Y:** indexed cumulative relative TSR. **색:** 전환+분리 연두색, 전체 carve-out 회색; neutral 파랑/회색. **크기:** 두 선 동일 규모, 얇은 관측점. **정렬:** 시간 오름차순. **강조:** 최종 20.3 index points 격차, 두 그룹 direct value labels.
- **라벨·축:** Y 90~130, 100 기준선, 월별 거래경과. **주석:** 마지막 시점 차이 계산. **범례:** 두 그룹. **레이아웃:** 긴 시간축과 제목, 범례·출처 하단.
- **원본과 차이:** 회사 전용 폰트·워드마크는 사용하지 않음. 레이블 여백·제목 줄 수와 축 스타일 일부 재구성. 원본 그래프에서 직접 라벨 확인.

## 공개 데이터·계산법
- **Source URL:** https://www.bcg.com/publications/2026/carve-out-strategy-both-companies
- **Figure:** Exhibit 1 (official image available on article; no image stored). **Published:** 2026-10-28. **Collected:** 2026-11-09. **Data observation:** T-3 days baseline through 24 months following transactions; exact aggregation sample and underlying event timestamps not disclosed sufficiently for independent reproduction.
- **Raw source:** 공식 그림에 인쇄된 9쌍의 값(18개)은 `reported`, T-3 days 기준선 100의 1쌍은 지수 정규화 정의에서 `derived`. `full_potential_index`, `all_carveouts_index`, `uncertainty_index_points=0` signifies *no numeric digitization undertaken*, not estimation error zero for original analyses.
- **Calculation:** index gap = `full_potential_index[-1] - all_carveouts_index[-1]` = 20.3. 중간시점의 오버레이와 비교만 사용; 세부 거래별 모델·표본수 미공개.

## 단계별 data_recipe
1. `transaction_id`, `close_date`, `cohort_flag`, `peer_group`, `tsr_relative_series` 확보.
2. 거래 후 공통 이벤트경과일로 관측치 정렬하고 계열별 동일 지수 100으로 정규화.
3. `full_potential` 및 `all` 코호트의 집계 정의·가중치를 명시하고 기간별 지수 생성.
4. 동일 이벤트 스냅샷만 남긴 후 상호 중첩 여부 및 표본잔존을 검증.
5. 기간별 지수와 최종 gap 계산 후 `data.csv` 구성.
6. `config.json`의 `THEME`와 `CONTEXT`를 바꿔 렌더링; 새 자료에서 메시지 성립 조건 재검증.

## 메시지 성립 조건·반례·한계
- **성립 조건:** 동일 사건 기간, 일치하는 TSR 계산법, 비교가능 거래 구성, 동종업계·기업규모 조정. 중간 시간의 실현지수와 이벤트 시간축 혼동 금지.
- **반례:** 표본의 성공거래만 선별하거나 full-potential 집단의 산업·규모가 본질적으로 다르면 우월성이 재설계의 원인이라는 주장을 할 수 없다.
- **한계:** 표본수·회귀계수·실질 통제변수·분모 구성 비공개; 원본 그래프만으로 개별 거래 결과를 역산할 수 없다. 사용권은 별도 확인.

## 사용 방법
`python chart.py --data data.csv --config config.json --theme source --output source.png`; neutral도 실행. 원본 이미지는 저장하지 않고 URL·그림 위치만 인용. 코드 실행 성공, 원본 의미 정확성, 사용자 승인 상태를 분리한다.
