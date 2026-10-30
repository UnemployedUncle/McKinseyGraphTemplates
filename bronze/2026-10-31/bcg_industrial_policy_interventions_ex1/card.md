# BCG — Industrial policy interventions (Exhibit 1)

## 1. 출처와 구분
- **공식 원문**: https://www.bcg.com/publications/2026/navigate-energy-policy-uncertainty
- **발행**: 2026-10-29; 수정일: 미공개; 열람: 2026-10-31 KST.
- **원본 그림**: https://web-assets.bcg.com/dims4/default/a3e3e14/2147483647/strip/true/crop/3600x2245%2B0%2B0/resize/499x311%21/format/webp/quality/80/?url=http%3A%2F%2Fboston-consulting-group-brightspot.s3.amazonaws.com%2F44%2F1b%2Fa4be3de14dc4b901ee0a73122c00%2Fhow-energy-companies-can-gain-advantage-ex01.png — Exhibit 1, “Advanced economies have seen a surge...” (웹 이미지; 페이지 번호 해당 없음).
- **원문 요지**: 정부의 산업정책 개입은 2015년 이후 크게 늘었다. 에너지기업은 정책 변화 빈도·변경 속도·대상을 동시에 평가해야 한다. 정책 모니터링이 기업의 자본배분 결정에 연결되는 것이 중요하다.
- **단 하나의 So what (해석)**: 산업정책 개입 건수가 2015년 2,273건에서 2025년 6,651건으로 약 2.93배 늘었으므로 에너지·산업기업은 정책 노출도를 투자심사와 시나리오 관리에 통합해야 한다.

## 2. 비즈니스 맥락 → 숫자 → 판단
| 구분 | 관측 사실·단위·기간·분모 | 의사결정 제안 |
|---|---|---|
| 현황 | 2015년 2,273건; 2025년 6,651건, 연간 정책 개입 건수, 원문에 표시된 전체 지리 범위 | 투자안의 정책 리스크 시나리오 갱신 주기 단축 |
| 증가 | 6,651/2,273 = 2.93배; 4,378건 증가(derived) | 국가·에너지 밸류체인 노출도의 변화 감시 |
| 구성 | 선진경제/기타경제 구간의 실제 값은 원문에 숫자로 공개되지 않음; 본 복원은 **그림 높이 판독 추정** | 구성비를 감사·투자 결론에 단독 사용 금지 |

## 3. 시각화 해부
- **원본 직접 관찰**: 2015~2025년 11개 연도의 두 색상 누적 세로 막대, 어두운 초록=선진경제, 밝은 초록=기타경제, 범례 하단, 연도별 총합 직접 라벨, 0~7,000 y축(1,000 간격), COVID-19와 2022년 이후 정책 관련 주석. 이중축·로그축·축 절단 없음. 원본 헤드라인은 급증이라는 메시지를 직접 전달.
- **재현 해석/한계**: 연간 총합은 `reported`; 두 색상 구간은 499×311 보기에서 y축 0~7000을 약 143픽셀로 계산해 눈금/경계 위치로 판독한 추정치(`digitized_estimate`), 약 ±160건은 **약 3픽셀 판독 범위**의 한계이지 신뢰구간 아님. 실제 숫자 공개가 없어 추정을 원문 사실로 취급하지 않음.
- **디자인 선택**: 연도 순서와 동일한 축으로 규모 추이를 읽고, 이벤트 주석을 최소화하며, 전체 높이를 값에서 산출.

## 4. 데이터·모델링
- 공개 데이터 출처: New Industrial Policy Observatory, International Monetary Fund, BCG analysis(원문 차트 하단). 정책 분류체계의 세부 레코드 및 가중치: 미공개. 인과추정·회귀모형을 본 차트에서 사용했다는 근거 없음.
- **data_recipe (재사용 제안)**: Unit of observation: intervention_id × announcement_year × location_group. Collect an official intervention ledger with country, announcement date, policy category, and affected industry. Deduplicate policy identifiers and check coverage changes by year; map jurisdictions to geography using a frozen crosswalk; count distinct interventions in each year/segment and sum across segments. Keep observed totals separate from digitized components; calculate growth ratio = end/start and absolute change = end - start. Plot yearly group totals, flag missing components, then interpret whether changes persist across definitions.
- **메시지 성립 조건**: Interventions in 2025 > 2015 with stable definition. If the rise disappears when counting comparable jurisdictions or reporting scopes, revise the action title. Counts do not demonstrate a policy causes losses or identify which laws affect any particular company.
- **수치 점검**: `Advanced economies` + `Other economies` = 원문 `Total`(각 연도). 총합은 실제 그림 표시 숫자 그대로, 구성요소는 추정치. 기간 간 비율은 2.93배, 단위는 건수(%)가 아님.

## 5. 재사용
- `config.json`의 `THEME.source/neutral`에서 색·글꼴·폭·비율을, `CONTEXT`에서 제목·축·주석·연도 순서를 변경하고 `data.csv`에서 관측값을 교체.
- 실행: `python chart.py --theme source --data data.csv --config config.json --output output.png`; `--theme neutral --output output_neutral.png`.
- 적합 사례: 국가별 무역 규제·관세 공지 건수의 연도별 추이. 새 데이터의 패턴이 다르면 action title도 바꿔야 함.
- 원본 시각 평가·실행 결과: `validation.json` 확인. 원본의 구간별 수치 미공개라는 본질적 한계가 있음.
