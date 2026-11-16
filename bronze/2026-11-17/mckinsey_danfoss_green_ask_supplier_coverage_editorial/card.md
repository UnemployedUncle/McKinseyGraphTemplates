# The CEO’s role in leading on sustainability

**Source:** https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/the-ceos-role-in-leading-on-sustainability

**Publication:** 2026-11-16; collection: 2026-11-17; data: 2025 prior-year and 2026 current-year, per May 2026 Danfoss climate transition plan cited by McKinsey

**Figure:** Article, Own the supply chain, Danfoss Green Ask paragraph; not source Exhibit 1

## Article in 3 sentences
1. McKinsey는 CEO가 공급망 탈탄소화 목표와 공급업체 실행관리를 연결해야 한다고 설명한다.
2. Danfoss Green Ask가 포괄하는 연간 매입액 비중은 40%에서 58%로 증가했다.
3. 포괄률 증가는 실제 온실가스 감축량·투자 수익률과는 다른 지표다.

## So what
Danfoss Green Ask의 연간 매입액 포괄 비중은 전년도 40%에서 58%로 18%p 확대됐다. 공급망 프로그램의 성과는 협력사 수보다 거래액 포괄률을 중심으로 측정하되 탄소 감축 성과와 구별해야 한다.

## Business context → measure → judgment
Annual purchases covered by Green Ask supplier program; unit percent_of_annual_purchases, denominator and period: 2025 prior-year and 2026 current-year, per May 2026 Danfoss climate transition plan cited by McKinsey. Compare values only under a consistent definition; this chart supports a practical decision, not a causal conclusion.

## Insight and visual design
Slope line: x=2025/2026, y=program coverage (%), point labels 40/58 and derived +18pp; neutral and source themes.

Source theme and neutral theme use separate colors; layout, text, footnotes and axis settings are in config.json. Position and labels are derived from CSV observations.

## Public source/sample/calculation
All plotted data values have reported provenance in data.csv. 58% minus 40% = +18 percentage points; published by McKinsey with a May 2026 Danfoss plan as source. Additional model inputs, observations or sample sizes are not disclosed.

## Reuse data_recipe
1. Identify covered supplier purchases as numerator and all annual purchases as denominator.
2. Retain the period-specific 40% and 58% reported shares.
3. Compute 58−40=18 percentage-point change, not a relative 18% change.
4. Preserve the company-specific definition of supplier program coverage.
5. Reconfigure CSV, colors and labels for another period-pair comparison.

## Message conditions and counterexamples
- Denominator is spend share, not supplier count.
- The figures indicate program coverage, not measured carbon reduction.
- Specific supplier inclusion and verification methods remain unpublished.
- Original article Exhibit 1 is an unrelated SBTi chart, so this editorial slope is not a reproduction.

## Fidelity and limitations
The original figure was not visually reproduced; this is a text-derived editorial chart. Fidelity score is null, validation unverified. The chart type must not be presented as the source figure's design.

## Usage
Run `python chart.py --data data.csv --config config.json --theme source --out artifacts/source.png` and again with neutral. Edit CSV and THEME/CONTEXT for reuse, and retain unit/provenance metadata. Do not add original reports, images, fonts or logos.
