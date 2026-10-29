# McKinsey | Agentic AI in strategic sourcing: Hype or hero? | Opening paragraphs: CPO survey statistics; editorial chart, not Exhibit 1

## 출처·수치 성격
- Company: McKinsey / Published: 2026-10-28 / Updated: 미공개 / Retrieved: 2026-10-30
- Official source: https://www.mckinsey.com/capabilities/operations/our-insights/agentic-ai-in-strategic-sourcing-hype-or-hero
- Figure: Opening paragraphs: CPO survey statistics; editorial chart, not Exhibit 1
- Original figure URL: 해당 없음 (원문에서 지표를 재편집)
- Data period: 2026년 6월 조사, 다음 12~18개월 투자 의향
- Sample & provenance: Trends in Procurement Organizational Design survey; June 2026; n=200; subgroup denominators/weights not published

## 글의 요지 — 원문 사실 (3문장 이내)
구매 부서 리더 설문에서 투자 확대 의향과 실제 AI 확산 단계 사이의 차이에 관한 자료입니다. 공개된 수치로 비용/구성/도입 상태를 정량화합니다. 이 자료만으로 인과관계를 입증하지는 않습니다.

## 단 하나의 So what — 해석 및 의사결정 제안
구매 리더의 80%가 향후 12~18개월 AI·기술투자 확대를 계획하지만 AI를 대규모로 내재화한 응답은 2%에 그치므로, 구매조직은 개별 도구 도입보다 업무 단위 확산과 성과 검증을 우선 설계해야 한다.

## 비즈니스 맥락 → 숫자 → 판단
| category | series | value | unit |
|---|---|---:|---|
| increase_investment | survey_item | 80 | % of eligible survey respondents |
| in_pilot | survey_item | 55 | % of eligible survey respondents |
| at_scale | survey_item | 2 | % of eligible survey respondents |

- [원문 사실] 숫자는 McKinsey Trends in Procurement Organizational Design survey, June 2026 n=200 CPO/procurement leaders; 80% plan increases in next 12–18 months; 55% pilot and 2% at scale are status responses, not a sequential funnel.
- [직접 관찰 및 제안] [관찰 제한] 공식 기사 본문 수치는 확인했지만 이 세 지표의 원본 차트는 존재하지 않아 편집형 차트로 제작했습니다. 원본과의 시각적 재현 비교는 불가능해 fidelity_score=null입니다.
- [의사결정 제안] 구매 리더의 80%가 향후 12~18개월 AI·기술투자 확대를 계획하지만 AI를 대규모로 내재화한 응답은 2%에 그치므로, 구매조직은 개별 도구 도입보다 업무 단위 확산과 성과 검증을 우선 설계해야 한다.

## 시각화 해부
- chart_type: `horizontal_bar` / insight_type: `격차`.
- x·y encoding: `config.json`의 `CONTEXT.chart_type`, `category_order`, `series_order`를 참고. 데이터 높이는 `value`, 색상은 `THEME.source.palette` 또는 `accent`.
- Category & series order: ['increase_investment', 'in_pilot', 'at_scale']; single series.
- Title: 원본 취지를 보존한 재서술 제목. 축·눈금: 공통 0–100% 축, 별개 질문.
- Emphasis: original theme / neutral theme 구분; 숫자 직접 라벨; logo/wordmark 미포함; 이중축·로그축 없음. 표시값과 기준선·분모의 차이를 해석할 때 주의.

## 원자료·모델링 한계
- Source/methodology: Trends in Procurement Organizational Design survey; June 2026; n=200; subgroup denominators/weights not published
- Unit/basis: % of eligible survey respondents; date/baseline: McKinsey Trends in Procurement Organizational Design survey, June 2026 n=200 CPO/procurement leaders; 80% plan increases in next 12–18 months; 55% pilot and 2% at scale are status responses, not a sequential funnel
- Unpublished: 문항별 가중치, 원시데이터/세부 계산법 중 원문에서 확인되지 않은 항목은 미공개.
- Reported values are reproduced exactly in data.csv; provenance=reported. No synthetic inputs used.

## 재사용 data_recipe
Observe survey_respondent-question-response; collect separately investment_intent and AI_deployment_status with eligible response denominators; deduplicate respondents, retain nonresponse, validate weights and time; share=sum(response matches item)/eligible respondents×100 per item; display side-by-side on independent common percentage scale, no sum or conversion.

## 메시지 성립 조건 / 반례 / 말할 수 없는 것
- 성립 조건: 원문과 동일한 분모·단위·기간·범주에서 표시된 값 또는 방향이 재현될 때 위 So what을 사용할 수 있습니다.
- 반례·제목 수정: 신규 데이터에서 추세나 순위가 반대이거나 차이가 통계·업무상 무의미하면 기존 액션 타이틀을 유지하지 마세요.
- 해석 제한: 투자 의향과 실제 도입 단계는 서로 다른 질문/응답 유형이다. 80%→55%→2% 전환 퍼널로 계산하거나 인과 추론하는 것은 금물이다.

## 재사용 및 명령
- `config.json`: `THEME.source`/`THEME.neutral`에 색·폭·글꼴·여백, `CONTEXT`에 액션 타이틀·축·주석·범주·계열 순서.
- `data.csv`: category, series, value, unit, period, source_url, figure_ref, provenance, denominator, base, estimate_method, uncertainty_low, uncertainty_high, notes.
- `python chart.py --data data.csv --theme source --config config.json --output output.png`
- `python chart.py --data data.csv --theme neutral --config config.json --output output_neutral.png`
- Runtime: 3.13.5 / matplotlib 3.10.8; command and results in validation.json.
- Similar work: 구매 Agent 전환 의향과 파일럿·확산 현황의 별도 측정
- 검증 상태와 미해결 원본 차이는 `validation.json`에 별도 기록합니다. 이 자체 평가가 사용자 검수나 콘텐츠 학습 권한을 뜻하지 않습니다.
