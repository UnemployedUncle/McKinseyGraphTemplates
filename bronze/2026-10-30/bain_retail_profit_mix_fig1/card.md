# Bain | Want to Lead in Consumer Products? Adapt to Retailing’s New Reality | Figure 1: Retail profit by source

## 출처·수치 성격
- Company: Bain / Published: 2026-10-29 / Updated: 미공개 / Retrieved: 2026-10-30
- Official source: https://www.bain.com/insights/want-to-lead-in-consumer-products-adapt-to-retailings-new-reality/
- Figure: Figure 1: Retail profit by source
- Original figure URL: https://public.flourish.studio/visualisation/30250905/thumbnail
- Data period: 2021, 2024, 향후 10년 전망
- Sample & provenance: Bain Retail Media Tech and Data POV; Retail Media Networks Overview (US, 2024); Future of Grocery Beyond Trade Compendium; details of samples/weights not published

## 글의 요지 — 원문 사실 (3문장 이내)
리테일러의 이익구조가 기존 상품 유통에서 광고·마켓플레이스·데이터 등 부가사업으로 이동할 가능성을 보여주는 전망에 관한 자료입니다. 공개된 수치로 비용/구성/도입 상태를 정량화합니다. 이 자료만으로 인과관계를 입증하지는 않습니다.

## 단 하나의 So what — 해석 및 의사결정 제안
리테일러 수익원 중 유통 외 사업의 비중이 2021년 10%에서 다음 10년 50%로 커질 전망이므로, 소비재 기업은 유통사와의 협력 의제를 가격·판촉에서 데이터·미디어·서비스로 확장할 필요가 있다.

## 비즈니스 맥락 → 숫자 → 판단
| category | series | value | unit |
|---|---|---:|---|
| 2021 | beyond_trade | 10 | % of period retail profit |
| 2021 | trading | 90 | % of period retail profit |
| 2024 | beyond_trade | 25 | % of period retail profit |
| 2024 | trading | 75 | % of period retail profit |
| next_decade | beyond_trade | 50 | % of period retail profit |
| next_decade | trading | 50 | % of period retail profit |

- [원문 사실] 숫자는 2021/2024 historical; next decade future estimate, not historical realized profit; denominator = retail profit per period.
- [직접 관찰 및 제안] [직접 관찰] 공식 원본 이미지를 열고 차트 유형·색·순서·라벨을 확인했습니다. 원본의 구조와 직접 비교하는 자체평가를 수행하되 일치 여부는 validation.json에 기록합니다.
- [의사결정 제안] 리테일러 수익원 중 유통 외 사업의 비중이 2021년 10%에서 다음 10년 50%로 커질 전망이므로, 소비재 기업은 유통사와의 협력 의제를 가격·판촉에서 데이터·미디어·서비스로 확장할 필요가 있다.

## 시각화 해부
- chart_type: `stacked_100` / insight_type: `구성`.
- x·y encoding: `config.json`의 `CONTEXT.chart_type`, `category_order`, `series_order`를 참고. 데이터 높이는 `value`, 색상은 `THEME.source.palette` 또는 `accent`.
- Category & series order: ['2021', '2024', 'next_decade']; ['beyond_trade', 'trading'].
- Title: 원본 취지를 보존한 재서술 제목. 축·눈금: 0–100% 구성비, 축선만 보이도록 단순화.
- Emphasis: original theme / neutral theme 구분; 숫자 직접 라벨; logo/wordmark 미포함; 이중축·로그축 없음. 표시값과 기준선·분모의 차이를 해석할 때 주의.

## 원자료·모델링 한계
- Source/methodology: Bain Retail Media Tech and Data POV; Retail Media Networks Overview (US, 2024); Future of Grocery Beyond Trade Compendium; details of samples/weights not published
- Unit/basis: % of period retail profit; date/baseline: 2021/2024 historical; next decade future estimate, not historical realized profit; denominator = retail profit per period
- Unpublished: 문항별 가중치, 원시데이터/세부 계산법 중 원문에서 확인되지 않은 항목은 미공개.
- Reported values are reproduced exactly in data.csv; provenance=reported. No synthetic inputs used.

## 재사용 data_recipe
Observe retailer-year-profit_source; gather profit by source; harmonize reporting periods and scopes, exclude overlapping profit, retain missing; sum category profit and divide each by total ×100; check 100% each period; plot beyond trade at bottom; interpret share shifts while separating historic and outlook.

## 메시지 성립 조건 / 반례 / 말할 수 없는 것
- 성립 조건: 원문과 동일한 분모·단위·기간·범주에서 표시된 값 또는 방향이 재현될 때 위 So what을 사용할 수 있습니다.
- 반례·제목 수정: 신규 데이터에서 추세나 순위가 반대이거나 차이가 통계·업무상 무의미하면 기존 액션 타이틀을 유지하지 마세요.
- 해석 제한: 전망치를 실적 데이터처럼 사용하거나 비중 상승만으로 절대이익의 증가를 주장하면 안 된다.

## 재사용 및 명령
- `config.json`: `THEME.source`/`THEME.neutral`에 색·폭·글꼴·여백, `CONTEXT`에 액션 타이틀·축·주석·범주·계열 순서.
- `data.csv`: category, series, value, unit, period, source_url, figure_ref, provenance, denominator, base, estimate_method, uncertainty_low, uncertainty_high, notes.
- `python chart.py --data data.csv --theme source --config config.json --output output.png`
- `python chart.py --data data.csv --theme neutral --config config.json --output output_neutral.png`
- Runtime: 3.13.5 / matplotlib 3.10.8; command and results in validation.json.
- Similar work: 연도별 사업부 이익원 구성과 전통/신사업 비중 변화
- 검증 상태와 미해결 원본 차이는 `validation.json`에 별도 기록합니다. 이 자체 평가가 사용자 검수나 콘텐츠 학습 권한을 뜻하지 않습니다.
