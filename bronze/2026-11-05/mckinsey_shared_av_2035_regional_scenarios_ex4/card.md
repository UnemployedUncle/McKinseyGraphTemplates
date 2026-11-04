# McKinsey | 2035 shared AV market scenarios by region

## 기사 요지 (직접 작성, 3문장)
McKinsey는 자율주행 공유교통 시장이 실증 서비스에서 상업적 규모로 확장되는 초기 단계라고 분석한다. 장기 시장 규모는 기술 효율뿐 아니라 안전, 도시별 규제, 소비자의 교통수단 전환, 차량 가동률에 좌우된다. 연구의 2035년 두 시나리오에서 전 세계 연간 시장 규모는 1,900억~4,300억 달러로 크게 달라진다.

**So what (단 하나):** 자율주행 공유서비스 투자안은 단일 시장 규모를 확정적 전망으로 사용하기보다 지역별 두 시나리오와 운영경제성을 분리해 감도 분석해야 한다.

## Business context → metrics → decision
- **Why**: Robotaxi/roboshuttle operators and investors must decide rollout pace and market priorities while deployment capacity and demand remain uncertain.
- **Metric**: Annual modeled shared AV market revenue; **USD billion**, nominal/real price basis **not stated in the article**, **year 2035**, four regions, separate low/base and upside scenarios.
- **Denominator**: Regional annual shared AV market revenue—not a percentage or fleet count. Summation across distinct regions only.
- **Comparator**: US = 100–190, Europe = 20–70, China = 60–150, Middle East = 10–20 (USD bn). Lower-bound total = 190, upper-bound total = 430. China + US constitute 160/190 and 340/430, respectively.
- **Decision**: Stress-test region allocation and utilization before committing fleet financing.

## Insight / design
**Insight type**: Scenario range + regional composition. This is an **editorial stacked-column redesign of publicly reported regional scenario endpoints**, **not** a faithful Exhibit 4 geometric reproduction. `x=scenario`, `y=USD billions`, `fill=region`, bar stacks=regional components, direct labels for material cells and totals, sorted ordered scenario low-to-high, value-driven heights and totals. Theme source adopts blue/cyan family; neutral is grayscale. No literal McKinsey logo or licensed fonts. Both axes and the modeled time horizon are labeled. The original Exhibit 4 is linked in the official article as SVGZ, but the tool could not inspect its graphical content, so fidelity comparison is not possible.

## Public source / sample / calculation
McKinsey article Nov 4, 2026 citing the proprietary McKinsey Shared AV Market Model; it models supply and demand in Greater China, Europe, US and Middle East with base/upside cases. Regional revenue endpoints are **reported** in body text, not independent observations. Market model parameters (price curves, utilization, adoption shares, regional revenues breakdown) are **not public**. Scenario total sums are **derived**: 100+20+60+10=190; 190+70+150+20=430, consistent with reported global 190–430 range. 2026 consumer survey has >20,000 participants in five countries but **does not determine** these modeled scenario revenues directly; do not label the figure as survey results.

## Data recipe (reuse)
1. Define `region`, `scenario`, `target_year`, `market_metric`, and common price/FX basis; source or develop consistent projection inputs.
2. Ingest one `value_usd_bn` for each region×scenario; mark each value `reported`, `derived`, `digitized_estimate` or `missing` with evidence.
3. Verify regional boundaries are non-overlapping and each case uses the same market definition; reconcile scenario totals and rounding.
4. Define base and upside internally as two coherent sets of assumptions; **do not mix different sources' high/low bounds**.
5. Draw totals using the actual sum of segment data, not hard-coded annotations; label the year and currency basis.
6. Reuse: edit `data.csv` and JSON `THEME` / `CONTEXT` only; rerun `chart.py --theme source|neutral`.

## Message conditions, counterexamples, limits
A cross-region stack is valid only when market slices are collectively additive. If selected regions overlap or definitions differ, use separate range bars instead of a stack. The two scenarios are illustrative conditional model outcomes—not forecasts, actual realized 2035 spending or confidence intervals. USD price-year basis, model coefficients and precise scenario probabilities are **not disclosed**; no assumptions were fabricated. Individual regional lower and upper bounds add to the reported global range; this numerical coincidence does not license certainty about intermediate paths. No verified reproduction score is assigned; source SVGZ was not visualized.

## Facts vs observation vs interpretation vs reuse
- **Source facts**: eight regional endpoints and global 190–430 USD bn span in the November 4, 2026 McKinsey article.
- **Visual observation**: publication labels Exhibit 4 and links an SVGZ image; original geometry inaccessible in available tool, thus no figure match.
- **Interpretation**: regional concentration persists across scenarios; market uncertainty remains substantial.
- **Reuse**: scenario-by-region stacked columns for sales or investment portfolios with additive regional financial values; not an assertion that model is independently validated.

## Usage
`pip install -r requirements.txt`; `python chart.py --data data.csv --config config.json --theme source --output source.png`; `--theme neutral` for grayscale. Outputs kept in artifacts, not immutable Bronze.

## Official source
https://www.mckinsey.com/industries/automotive-and-assembly/our-insights/from-science-fiction-to-reality-the-next-phase-of-shared-autonomous-mobility (2026-11-04), Exhibit 4 numerical context, survey Jan–Feb 2026 distinct from 2035 proprietary model. Collected 2026-11-05 Asia/Seoul.
