# BCG | Who Will Pay the $2.6 Trillion AI Infrastructure Bill? | Exhibit 6: Cost to build 1 GW of AI compute in 2026

## 출처·수치 성격
- Company: BCG / Published: 2026-10-29 / Updated: 미공개 / Retrieved: 2026-10-30
- Official source: https://www.bcg.com/publications/2026/who-pays-for-ai-infrastructure
- Figure: Exhibit 6: Cost to build 1 GW of AI compute in 2026
- Original figure URL: https://web-assets.bcg.com/dims4/default/79b139f/2147483647/strip/true/crop/5760x3240%2B0%2B0/resize/768x432%21/format/webp/quality/80/?url=http%3A%2F%2Fboston-consulting-group-brightspot.s3.amazonaws.com%2F6b%2F0e%2F87f52210443d95c689f98d18bad5%2Fwho-will-pay-the-2-trillion-bill-exhibits-6.png
- Data period: 2026년 모델 시나리오
- Sample & provenance: BCG Global Data Center Model; project benchmarks (20 facilities for shell/land); Morgan Stanley, Nvidia, Epoch AI, Semianalysis, energy market sources; actual model underlying individual line items unpublished

## 글의 요지 — 원문 사실 (3문장 이내)
AI 데이터센터의 1GW Critical IT load 구축비용을 비용 구성요소별로 분해한 BCG의 예시적인 2026년 원가모형에 관한 자료입니다. 공개된 수치로 비용/구성/도입 상태를 정량화합니다. 이 자료만으로 인과관계를 입증하지는 않습니다.

## 단 하나의 So what — 해석 및 의사결정 제안
AI 연산능력 1GW의 구축비용 약 421억 달러 중 Core IT가 288억 달러로 가장 크므로, 데이터센터 투자안의 경제성은 칩·서버 비용과 교체주기 가정에 특히 민감하게 검토해야 한다.

## 비즈니스 맥락 → 숫자 → 판단
| category | series | value | unit |
|---|---|---:|---|
| Core IT | component | 28.8 | USD billion / GW critical IT load |
| Data center shell | component | 11.2 | USD billion / GW critical IT load |
| Power infrastructure | component | 1.8 | USD billion / GW critical IT load |
| Land | component | 0.2 | USD billion / GW critical IT load |
| Total | total | 42.1 | USD billion / GW critical IT load |

- [원문 사실] 숫자는 2026 model, $ billion per GW critical IT load, USA-heavy costs, 2030 global analysis excludes China; rounded sum of components 42.0 versus reported total 42.1.
- [직접 관찰 및 제안] [직접 관찰] 공식 원본 이미지를 열고 차트 유형·색·순서·라벨을 확인했습니다. 원본의 구조와 직접 비교하는 자체평가를 수행하되 일치 여부는 validation.json에 기록합니다.
- [의사결정 제안] AI 연산능력 1GW의 구축비용 약 421억 달러 중 Core IT가 288억 달러로 가장 크므로, 데이터센터 투자안의 경제성은 칩·서버 비용과 교체주기 가정에 특히 민감하게 검토해야 한다.

## 시각화 해부
- chart_type: `waterfall` / insight_type: `구성`.
- x·y encoding: `config.json`의 `CONTEXT.chart_type`, `category_order`, `series_order`를 참고. 데이터 높이는 `value`, 색상은 `THEME.source.palette` 또는 `accent`.
- Category & series order: ['Core IT', 'Data center shell', 'Power infrastructure', 'Land', 'Total']; single series.
- Title: 원본 취지를 보존한 재서술 제목. 축·눈금: 기여도 누적 위치 기반, y축 눈금을 생략.
- Emphasis: original theme / neutral theme 구분; 숫자 직접 라벨; logo/wordmark 미포함; 이중축·로그축 없음. 표시값과 기준선·분모의 차이를 해석할 때 주의.

## 원자료·모델링 한계
- Source/methodology: BCG Global Data Center Model; project benchmarks (20 facilities for shell/land); Morgan Stanley, Nvidia, Epoch AI, Semianalysis, energy market sources; actual model underlying individual line items unpublished
- Unit/basis: USD billion / GW critical IT load; date/baseline: 2026 model, $ billion per GW critical IT load, USA-heavy costs, 2030 global analysis excludes China; rounded sum of components 42.0 versus reported total 42.1
- Unpublished: 문항별 가중치, 원시데이터/세부 계산법 중 원문에서 확인되지 않은 항목은 미공개.
- Reported values are reproduced exactly in data.csv; provenance=reported. No synthetic inputs used.

## 재사용 data_recipe
Observe data_center_build-component-year-model; obtain chips, shell, power, land costs per GW on one consistent IT-load basis; standardize capitalization and power cost inclusion; keep non-disclosed inputs missing; sum component costs and compare model total, document rounding difference; waterfall from component costs to reported total; test chip pricing sensitivity.

## 메시지 성립 조건 / 반례 / 말할 수 없는 것
- 성립 조건: 원문과 동일한 분모·단위·기간·범주에서 표시된 값 또는 방향이 재현될 때 위 So what을 사용할 수 있습니다.
- 반례·제목 수정: 신규 데이터에서 추세나 순위가 반대이거나 차이가 통계·업무상 무의미하면 기존 액션 타이틀을 유지하지 마세요.
- 해석 제한: 원문의 합계 42.1과 개별 반올림 비용 합계 42.0의 0.1 차이를 수정하지 않고 주석으로 기록한다. 외부 고객의 실제 구매금액 예측은 아니다.

## 재사용 및 명령
- `config.json`: `THEME.source`/`THEME.neutral`에 색·폭·글꼴·여백, `CONTEXT`에 액션 타이틀·축·주석·범주·계열 순서.
- `data.csv`: category, series, value, unit, period, source_url, figure_ref, provenance, denominator, base, estimate_method, uncertainty_low, uncertainty_high, notes.
- `python chart.py --data data.csv --theme source --config config.json --output output.png`
- `python chart.py --data data.csv --theme neutral --config config.json --output output_neutral.png`
- Runtime: 3.13.5 / matplotlib 3.10.8; command and results in validation.json.
- Similar work: AI 인프라 및 클라우드 구축비용의 원가 항목별 기여도
- 검증 상태와 미해결 원본 차이는 `validation.json`에 별도 기록합니다. 이 자체 평가가 사용자 검수나 콘텐츠 학습 권한을 뜻하지 않습니다.
