# McKinsey Global Institute · Trade vulnerability, Exhibit 3 (Marimekko-style reconstruction)

## 글의 요지 (3문장)
MGI는 2024년 약 19조 달러의 글로벌 상품수입을 대상으로 제품 중요도·공급국 집중·지정학적 거리의 중첩 위험을 평가했다. 전체 수입의 약 23%가 두 가지 이상 위험을 갖고, 4%는 세 가지 모두에 해당한다. 국가별로 일본의 복합 취약 수입 비중이 36%인 데 비해 말레이시아는 10%이며 절대 수입금액도 서로 다르다.

## So what
무역조달 위험은 취약 비율만 보지 말고 **수입규모 × 위험의 중첩 정도**로 우선순위를 정해야 한다.

## 비즈니스 맥락 → 데이터 → 판단
- 맥락: 전 세계 교역의 지정학·공급원 다변화 압력이 커져 기업들이 공급망 취약 부분을 식별해야 함
- 관측단위: 경제권 × 제품 바스켓, 2024년 상품 수입 (서비스/자본 이동 제외)
- X: `imports_usd_billion` ($bn), 열 너비. 전체 19조 달러와 달리 15개 주요 경제권의 수치만 시각화
- Y: `exposure_total_pct` (% of own goods imports), 2+ 위험 노출 비율
- 색: `exactly_two_pct` (파생 = 총비율 - 세 위험), `all_three_pct` (공개값)으로 적층
- 비교기준: 같은 정의의 제품 중요도·공급국 집중·지정학적 거리
- 판단: 높은 비율과 큰 수입규모를 함께 가진 지역의 위험량이 더 클 수 있음

## 인사이트 유형과 시각화 설계
- Insight: dual-scale exposure and vulnerability layering
- Original stated chart type: **variable-width stacked columns (column width = total imports)**
- Implementation: width-weighted Marimekko columns; heights derived from reported percentage values; sorted by total exposure descending
- Label: economy on x; `exposure_total_pct` above columns wide enough for legible annotations; y=0–40%, not 100% of total imports
- Color: 2 risks = theme accent, all 3 = theme highlight
- Figure/picture: article's Exhibit 3 description and full numeric table read from official HTML; image not directly inspected, so no fidelity claim
- Column widths are comparative *USD import values*, not equal categories; total set is 15 economies, not the entire global $19T universe

## 데이터 출처·표본·계산법
- Official: https://www.mckinsey.com/mgi/our-research/the-achilles-heel-of-global-trade-building-resilience-where-it-matters-most (published 2026-11-12)
- Sources named by MGI: UN Comtrade, US Draft List of Critical Supply Chains (2022), MGI analysis
- Data year: 2024. Global base excludes intra-Europe-30 flows, Europe-30 consists EU27 plus Norway Switzerland UK
- Public inputs: 15 economy rows, reported total exposed pct, all-3 pct, total import $bn
- Derived: `exactly_two_pct = exposure_total_pct - all_three_pct`, rounding uncertainty inherited from displayed percentages
- No unreported product-level weights or models constructed. Printed percentages are rounded.

## 재사용 data_recipe
1. Fix period, goods definition, partner and economy perimeter and product classification
2. Compute economy total imports in a common currency ($bn) and identical year
3. Classify product-level vulnerability count (0/1/2/3) using transparent thresholds
4. Aggregate shares for exactly 2 and exactly 3 vulnerabilities per economy
5. Use import value as column width (not bar height), stack percentages on y
6. Annotate rounding, excluded trade flows and high-risk product examples; prioritize exposure dollars and mitigation options

## 메시지 성립 조건과 반례·한계
- Countries with greater percentages do not necessarily have greater exposed dollars or disruption losses.
- Imports in categories are not necessarily impossible to substitute; policy risk and supply continuity differ by product.
- Europe-30 intraregional flows are excluded; comparing unadjusted national accounts would be inconsistent.
- Same column can represent risk types but a wider bar **does not** imply greater probability.
- Exact split between 2 and 3 is derived from rounded percentages; slight sum differences are expected.
- Original exhibit visual pixels not accessed; exact label placement and colors unverified.

## 사용 방법
`pip install -r requirements.txt`, then `python chart.py --data data.csv --config config.json --theme source --output source.png`; repeat `--theme neutral`. To adapt, replace CSV values using identical goods-trade definitions and modify THEME/CONTEXT.
