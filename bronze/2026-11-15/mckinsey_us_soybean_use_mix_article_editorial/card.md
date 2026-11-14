# Taking stock: Farm pressures and uneven recovery in the United States and Brazil — Soybean crush versus exports exhibit (editorial bar using article values)

## 글 요지 (3문장)
미국 농업의 수요구조가 대두 가공 중심으로 이동하고 있습니다. McKinsey는 2026/27 마케팅연도에 국내 가공 57%, 수출 35%를 제시하며 두 비중이 최근 2년간 각각 ±5%p 움직였다고 설명합니다. 가공과 수출 이외의 용도도 있으므로 두 비율을 전체 구성의 합계로 취급하면 안 됩니다.

## So what (하나)
미국 대두 총 사용량 중 국내 가공 비중은 2026/27년 57%로 증가하고 수출 비중은 35%로 감소할 전망이므로, 농산물 트레이딩·가공 투자에서 최종 수요처 변화를 반영해야 한다.

## 사실과 인사이트의 연결
- **Source:** https://www.mckinsey.com/industries/energy-and-materials/our-insights/blog/taking-stock-farm-pressures-and-uneven-recovery-in-the-united-states-and-brazil
- **Published:** 2026-11-11; **retrieved:** 2026-11-15 Asia/Seoul
- **Data context:** McKinsey Agriculture Industry Review 2026-11-11, citing underlying US soybean supply and use projections; detailed source in article notes.
- **Business question:** 국내 가공과 수출 수요 비중이 어떻게 이동하는가?
- **Metric / unit / denominator / baseline:** percentage share of US total soybean use / Total soybean use by US marketing year; marketing year × soybean use destination
- **Interpretation:** mix shift / domestic versus export channels; 지표의 비교는 공통 단위·기간·분모를 갖는 경우에만 유효.

## Chart encoding / visual reasoning
- **Type:** grouped_share. Original type: soybean share exhibit (original SVGZ not visually inspected; editorial).
- **X / Y:** marketing year; percentage of total use.
- **Colors / order:** crush versus exports; marketing years chronological.
- **Size / labels:** shared vertical percent axis; numeric annotations from data, no fixed invented values.
- **Axis / spacing:** shared zero baseline, explicit units; background and palette configured in THEME.
- **Annotation:** Key group comparison is stated in chart; source and scope in footer.

## Data provenance / limitations
- **Reported and derived:** See per-row provenance in data.csv. Recent 57%/35% shares are reported; 52%/40% are derived from the two stated 5 pp movements.
- **Sampling and calculation:** McKinsey Agriculture Industry Review 2026-11-11, citing underlying US soybean supply and use projections; detailed source in article notes.
- **Message validity conditions:** 1. Both series use share of total US soybean use, not production or crop acreage. 2. Two-year baseline derived using explicitly stated five percentage-point changes.
- **Counterexamples and limits:** 1. Other soybean uses are omitted; the two percentages do not add to 100%. 2. Underlying original vector exhibit inaccessible; fidelity cannot be scored. 3. Published text may round reported changes, and inferred earlier values inherit that uncertainty.
- **Provenance separation:** Public facts = reported; computed values = derived; design choices = editorial when noted. Unpublished field-level microdata and detailed models remain unpublished.

## Stepwise data_recipe
1. Confirm common soybean-use denominator and marketing-year conventions.
2. Extract use shares per category from official cited sources.
3. Derive earlier shares only when the stated period and percentage-point changes match.
4. Separate domestic processing and exports without assuming they exhaust total use.
5. Render grouped bars with unit, year, and reported/derived provenance.

## How to use
```bash
pip install -r requirements.txt
python chart.py --data data.csv --config config.json --theme source --output source.png
python chart.py --data data.csv --config config.json --theme neutral --output neutral.png
```
Change data.csv plus THEME and CONTEXT only, keeping unit/denominator/provenance checks. Generated PNG belongs outside the immutable Bronze bundle under artifacts/.
