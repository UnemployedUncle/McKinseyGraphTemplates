# How New Drug Pricing Models Will Play Across Europe

**Source:** https://www.bcg.com/publications/2026/us-drug-pricing-changes-europe

**Publication:** 2026-11-16; collection: 2026-11-17; data: 2026 published model; scenario horizon not fully disclosed

**Figure:** Article Exhibit 1 referenced; editorial range from article text, not image reproduction

## Article in 3 sentences
1. 미국 약가 연동 정책의 변화가 유럽 제약사의 신약 출시 경제성에 미치는 영향을 다룬다.
2. 기사에 따르면 향후 신약 출시 이익은 시나리오에 따라 기존 수준의 25~70%로 추정된다.
3. 원본 모델의 구체적인 시나리오 가중치와 산정에 쓰인 수익 분모는 공개되지 않았다.

## So what
BCG의 약가 정책 시나리오에 따라 미래 출시 제품의 이익 수준은 현재 대비 25~70% 범위로 달라질 수 있다. 규제 시나리오별 손익 민감도와 가격전략을 분리해서 검토해야 한다.

## Business context → measure → judgment
Future launch profit relative to current level; unit percent_of_current_profit, denominator and period: 2026 published model; scenario horizon not fully disclosed. Compare values only under a consistent definition; this chart supports a practical decision, not a causal conclusion.

## Insight and visual design
Single range interval; x is modeled profit as a percentage of current, y is one modeled range, labeled endpoints and a common 0–100 scale.

Source theme and neutral theme use separate colors; layout, text, footnotes and axis settings are in config.json. Position and labels are derived from CSV observations.

## Public source/sample/calculation
All plotted data values have reported provenance in data.csv. The 25% and 70% endpoints imply a 45-percentage-point range, not a 45% probability. Additional model inputs, observations or sample sizes are not disclosed.

## Reuse data_recipe
1. Set current profit to the common baseline of 100%.
2. Extract low and high remaining-profit scenario endpoints.
3. Record both endpoints as reported model estimates, not observed profit.
4. Check percent versus percentage-point interpretation and compare horizon.
5. Plot the range; data-derived width is 70−25=45 pp; change CSV and theme for reuse.

## Message conditions and counterexamples
- Range is a scenario estimate, not a statistical confidence interval.
- Both percentages describe retained profit level, not percent decline.
- Original Exhibit 1 is a different bar chart; reproduction fidelity cannot be scored.
- Regional/asset assumptions, sample and timing are unpublished.

## Fidelity and limitations
The original figure was not visually reproduced; this is a text-derived editorial chart. Fidelity score is null, validation unverified. The chart type must not be presented as the source figure's design.

## Usage
Run `python chart.py --data data.csv --config config.json --theme source --out artifacts/source.png` and again with neutral. Edit CSV and THEME/CONTEXT for reuse, and retain unit/provenance metadata. Do not add original reports, images, fonts or logos.
