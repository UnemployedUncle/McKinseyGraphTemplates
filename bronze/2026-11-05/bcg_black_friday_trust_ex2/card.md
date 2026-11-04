# BCG | Net trust score at year-end sales events (Exhibit 2)

## 기사 요지 (직접 작성, 3문장)
BCG의 2026년 소비자 조사는 연말 판촉에서 소비자들이 가격 신뢰를 중요하게 판단한다고 설명한다. 유통사 평판·환불 보장·검증 구매 리뷰는 신뢰에 크게 기여하지만, 희소성 메시지·AI 요약·인플루언서 추천의 순 기여는 낮다. 할인 폭 확대보다는 실제 가격의 검증 가능성과 고객의 경험 근거가 더 중요한 차별화 요인으로 제시된다.

**So what (단 하나):** 유통사는 추가적인 판촉 메시지에 비용을 쓰기 전에 환불정책·가격 이력·검증 구매리뷰처럼 고객이 직접 확인할 수 있는 신뢰 증거를 우선 강화해야 한다.

## Business context → measurable claim → decision
- **Problem**: Promotions face price skepticism; retailers need to distinguish verifiable credibility from attention-generating persuasion.
- **Metric**: Net trust score = percentage reporting a factor increases trust **minus** percentage reporting it decreases trust; unit **percentage points (%p)**, not percentage of shoppers trusting a deal.
- **Observation / sample**: September 2026; BCG Year-End Sales Events Consumer Study; 10,220 consumers ages 18–75 across 10 markets, but item-specific valid denominators were not disclosed.
- **Comparison**: 11 factors in Exhibit 2. Both reputation and free returns = +65pp; verified reviews = +59pp; discounts comparison = +58pp; influencers = +3pp.
- **Decision**: Prioritize transparent proof, then measure actual conversion to avoid conflating reported trust with business impact.

## Chart logic and encodings
**Insight type**: Ranked driver comparison / evidence-vs-persuasion contrasts. **Source figure**: horizontal bar ranking with shared zero baseline, ordered descending as displayed in the original, direct integer end labels, dark teal for proof, turquoise for customer proof, pale cyan for persuasion. `x=net_trust_score`, `y=factor`, `color=source_category`; no size encoding; ranking is by value. The horizontal axis tick labels are hidden; bar-end values are directly labeled. Source-style title at upper left and one note near bottom; color legend groups factor themes. Directly inspected official Exhibit 2 image through its BCG-hosted link; some fonts, legend location and spacing differ from source; generated outputs contain no source artwork.

## Provenance and calculation
All **11 numbers** in data.csv are **reported** and visible in BCG's original Exhibit 2, not our inferences. Scores are net scores (can be negative), **not shares**: do not add them to 100%; difference between 65 and 3 is **62 percentage points**, not +62% relative lift. Sample selection, response weighting, factor-response counts and precise confidence intervals are **not publicly given** on the page; no inferential error bars should be invented.

## Data recipe (reuse)
1. Collect individual responses `respondent_id`, `factor`, `trust_effect` (increase / no effect / decrease), `survey_weight`, `market`, `survey_month`.
2. Apply mutually consistent valid-response filtering per factor; specify each `eligible_respondents` denominator and weights.
3. Calculate weighted `increase_share` and `decrease_share` for each factor separately.
4. Calculate `net_trust_pp = 100 * (increase_share - decrease_share)` and retain sign plus unrounded values.
5. Select a mutually interpretable set of factors; map `group`, sort by net trust, keep unchanged scores. Label difference in **pp**.
6. Edit `data.csv` (`category`, `value`, `group`) and `config.json` (THEME, CONTEXT) to render another survey ranking.

## When message holds / alternatives / limitations
Works when categories share question scale and respondent population/valid-weighting method. Counterexample: A tactic might score low on net trust yet drive conversions through short-term urgency; do not equate lower net trust to lower realized sales. No causal evidence that adopting refund policies itself generates a particular ROI. `n=10,220` is the overall survey, not necessarily the denominator for every item. The three color groups are our logical labels aligned to the original palette, not quantitative group estimates. Source's separate Exhibit 1 measures advertised-discount credibility, a distinct metric.

## Fact / observation / interpretation / reuse
- **Source fact**: all 11 Exhibit 2 factor scores and surveyed population.
- **Visual observation**: horizontal bars descending; values printed at ends; teal-based grouping and sparse axes.
- **Interpretation**: a strong observed association between verifiable proof and positive net trust responses.
- **Reuse proposal**: ranked driver chart for sales-channel trust, product discoverability or supplier assessment; no observed client outcomes are implied.

## Usage
`pip install -r requirements.txt`; `python chart.py --data data.csv --config config.json --theme source --output source.png`; use `--theme neutral` for portable monochrome. PNG is generated outside Bronze at dpi200.

## Official source
https://www.bcg.com/publications/2026/trust-matters-year-end-sales-events (November 4, 2026); Exhibit 2 image link available directly on the page. Retrieval 2026-11-05 Asia/Seoul.
