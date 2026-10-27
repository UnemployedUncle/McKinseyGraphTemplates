# BCG — 코발트·니켈 공급 지역 집중 (Exhibit 2의 공개 수치 일부)

## 출처 및 사실
- 공식 글: **Why Critical Mineral Shortages Are a CEO Issue**, 2026-10-27.
- 원본 Exhibit 2 이미지 링크: https://web-assets.bcg.com/dims4/default/e9475c4/2147483647/strip/true/crop/3600x2193%2B0%2B0/resize/499x304%21/format/webp/quality/80/?url=http%3A%2F%2Fboston-consulting-group-brightspot.s3.amazonaws.com%2F39%2Ffb%2Fe0c62c6e4a64ac7be2ea4f8039ab%2Fwhy-critical-mineral-shortages-are-a-ceo-issue-ex02.png
- 본문은 콩고민주공화국의 코발트 채굴 비중을 **약 3분의 2**, 인도네시아의 니켈 상류 생산능력을 **약 70%**로 기술한다. 원본 그림에는 위치별 생산과 **소유권 집중**을 비교하는 추가 막대가 있지만 전체 상세 수치는 제공되지 않는다.
- 자산 소유 비율과 표본 기간은 **미공개**. 66.7은 본문 `2/3`의 근사 환산(`derived`)이고 70은 원문의 대략치(`reported`), 정밀 실측값 아님.

## 글 요지 (3문장)
원자재 위험은 조달 비용과 1차 공급자 데이터에만 의존하면 누락되기 쉽다. 핵심광물 공급 위험은 채굴뿐 아니라 정련·가공 및 자산 소유권에 잠복해 있다. BCG는 공급망을 다층적으로 추적하고 대체 공급·수요 전환을 사전에 검토하라고 제안한다.

## 단 하나의 So what
**핵심광물의 생산 지역이 고도로 집중돼 있고 실제 통제 주체는 다를 수 있으므로, 조달액·채굴 국가만으로 공급 위험을 평가하지 말아야 한다.**

## 맥락 → 숫자 → 판단
| 맥락 | 정량 근거 | 범위·분모 | 판단 |
|---|---|---|---|
| Cobalt | DRC 약 2/3 | 전세계 채굴 코발트 | 광산 국가 의존성 확인 |
| Nickel | Indonesia 약 70% | 전세계 해당 상류 생산능력 | 정련·지분 소유까지 평가 |

## 설계 해부와 공개 여부
원본 Exhibit 2는 코발트와 니켈의 **생산 소재지 대 지분 소유주**를 대비하는 막대형 차트로 설명된다. 그러나 원본 PNG 자체가 열리지 않았고 소유주 비율도 수치상 공개되지 않아 **이번 이미지는 두 공개 수치만 비교한 편집형 차트**, 원본 시각 재현이 아니다. x는 항목별 집중도(%), y는 광물+단계+국가, 녹색은 니켈 바 강조, 축 범위 0~100. 두 막대는 **서로 다른 광물과 관측 단계**이므로 공통 기업 시장점유율처럼 해석하면 안 된다.

## 재사용 data_recipe
1. `mineral × stage × asset × country × beneficial_owner`를 관측 단위로 구성.
2. USGS·IEA·기업보고서로 품목별 생산/가공/캐파 확보. 국가별 자료와 지배회사 소재지/실소유자 분리.
3. 동일 연도·동일 제품 등급·톤수/정련능력/실제 생산량을 통일. 사업장/소유권 이중계산 제거.
4. `country_quantity / global_quantity × 100`, `owner_controlled_quantity / global_quantity × 100` 계산.
5. 공개하지 않은 나머지 소유자 수치는 `missing`으로 두고 원본 시각 완성이라고 주장하지 않는다.
6. 중국 기업의 해외 소유권이 높다면 물리적 다변화로도 실질 위험이 낮아지지 않을 수 있다는 **분석 가설**을 검증한다.

## 반증 조건·한계
대체 공급자의 실소유주가 다양하고, 단계별 공급 집중도가 낮으며, 공급 자격 승인시간이 충분히 짧다면 '숨겨진 집중' 메시지는 약화된다. 이번 수치만으로 완제품의 매출손실액을 계산할 수 없다.

## 재사용
`config.json` THEME/CONTEXT와 `data.csv`만 교체한다. 예: 1차 거래선별 제철소 공급량과 궁극 소유 주체의 공급 집중을 구분하는 분석. `python chart.py --theme neutral --data data.csv --output output_neutral.png`. **원본 비교 불가, 충실도 null, user review pending**.
