# Canadians Are Shopping on Tighter Budgets This Black Friday — Exhibit 1 (Canadian shoppers' planned spend by price category)

## 글 요지 (3문장)
캐나다 소비자 1,000명의 2026년 연말 할인 행사 계획 예산은 평균 CAD 530입니다. 필수·저가품목 2개 항목의 합계는 CAD 330으로 약 62%이며, 고가품목은 CAD 200입니다. 채널 운영은 품목과 가격대를 구분하여 소비자가 확인 가능한 가치를 전달해야 합니다.

## So what (하나)
캐나다의 블랙프라이데이 평균 계획예산 CAD 530 중 생활필수·저가상품이 CAD 330(62%)이므로, 가격 민감도에 맞춘 상품·프로모션 믹스가 필요하다.

## 사실과 인사이트의 연결
- **Source:** https://www.bcg.com/publications/2026/canadians-are-shopping-on-tighter-budgets-this-black-friday
- **Published:** 2026-11-12; **retrieved:** 2026-11-15 Asia/Seoul
- **Data context:** BCG 2026 Black Friday Consumer Study; Canada respondents n=1,000; detailed fieldwork dates not disclosed.
- **Business question:** 가격에 민감한 소비자 예산의 품목별 배분은 어떻게 다른가?
- **Metric / unit / denominator / baseline:** CAD per shopper; share percent / Average Canadian survey respondent's planned budget CAD 530; spending category × 2026 survey
- **Interpretation:** composition/affordability allocation; 지표의 비교는 공통 단위·기간·분모를 갖는 경우에만 유효.

## Chart encoding / visual reasoning
- **Type:** descending_waterfall. Original type: descending waterfall (visually inspected).
- **X / Y:** ordered budget category; CAD descending offset.
- **Colors / order:** low/high price tiers; original category order.
- **Size / labels:** CAD 530 total; numeric annotations from data, no fixed invented values.
- **Axis / spacing:** shared zero baseline, explicit units; background and palette configured in THEME.
- **Annotation:** Key group comparison is stated in chart; source and scope in footer.

## Data provenance / limitations
- **Reported and derived:** See per-row provenance in data.csv. Dollar labels are reported; category shares may not sum to 100% after rounding.
- **Sampling and calculation:** BCG 2026 Black Friday Consumer Study; Canada respondents n=1,000; detailed fieldwork dates not disclosed.
- **Message validity conditions:** 1. Values refer to same shoppers, purchase event, CAD unit and time horizon. 2. Five segment dollars sum to CAD 530, low segments to CAD 330 and high segments to CAD 200.
- **Counterexamples and limits:** 1. Survey intention is not realized purchases. 2. Rounded percentage values sum to 99%. 3. Income/age mix and sample error are not disclosed in the graphic.
- **Provenance separation:** Public facts = reported; computed values = derived; design choices = editorial when noted. Unpublished field-level microdata and detailed models remain unpublished.

## Stepwise data_recipe
1. Normalize average planned budget in common currency and period.
2. Assign each segment to low/high affordability bands.
3. Compute dollar budget per segment and rounded share; reconcile rounding.
4. Order segments from higher spending to lower and render a descending waterfall.
5. Label total budget and group subtotals independently.

## How to use
```bash
pip install -r requirements.txt
python chart.py --data data.csv --config config.json --theme source --output source.png
python chart.py --data data.csv --config config.json --theme neutral --output neutral.png
```
Change data.csv plus THEME and CONTEXT only, keeping unit/denominator/provenance checks. Generated PNG belongs outside the immutable Bronze bundle under artifacts/.
