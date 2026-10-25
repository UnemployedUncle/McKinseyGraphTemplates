# BCG — The Three Dimensions of Leadership for the AI Era / Exhibit 3

- 공식 출처: https://www.bcg.com/publications/2026/three-leadership-roles-ceos-ai
- 공개일: 2026-09-29 · 이 실행 열람일: 2026-10-26 · 원본 시각 자료(저장하지 않음): https://web-assets.bcg.com/dims4/default/e608136/2147483647/strip/true/crop/3600x1680%2B0%2B0/resize/499x233%21/format/webp/quality/80/?url=http%3A%2F%2Fboston-consulting-group-brightspot.s3.amazonaws.com%2F85%2F33%2F7f38d1fa4878b9ef82d7199a6c5e%2Fwhat-is-required-to-lead-in-an-ai-world-ex03.png
- 데이터/조사 시점: 2026 survey · 원자료: BCG Global Leadership Survey 2026; 563 senior company executives across the survey, subgroups undisclosed
- 그림 번호: Exhibit 3 · 유형: vertical_four_bars · 인사이트 유형: comparison

## 글의 요지 (원문 사실의 요약)
Employee centricity and organization AI maturity (2026 survey)를 공식 자료에서 정량적으로 분석한다. 원문 수치를 비교해 전략적 논점을 제공한다. 공개되지 않은 집단별 분모·원시자료는 추정하지 않는다.

## So what (에이전트 해석)
AI 전환에서 직원을 적극 참여시키는 집단은 제한적으로 참여시키는 집단보다 AI 성숙 기업 비율이 58% 대 18%로 높으므로, 기술 투자와 함께 공동 설계 방식을 우선 검토해야 한다.

## 비즈니스 맥락 → 숫자 → 판단

| 비즈니스 맥락 | 지표/분모 | 기간·단위 | 관찰 및 결정상 시사점 |
|---|---|---|---|
| Employee centricity and organization AI maturity (2026 survey) | executives grouped by employee centricity; within-group AI mature percentage | 2026 survey, percent | AI 전환에서 직원을 적극 참여시키는 집단은 제한적으로 참여시키는 집단보다 AI 성숙 기업 비율이 58% 대 18%로 높으므로, 기술 투자와 함께 공동 설계 방식을 우선 검토해야 한다. |

원문 보고값: limited 18%, moderate 29%, strong 36%, extensive 58%. 합성·임의 추정값을 사용하지 않았다.

## 시각화 설계 해부
- X 인코딩: 직원중심성 범주; Y 인코딩: 범주별 AI 성숙 기업 비율(%)
- 색: THEME.source.palette 또는 bar_color; 정렬: config.json의 category_order; 원본 특징과 차이는 validation.json 참조
- 강조 수단: four ascending columns, one chart-wide green category color, direct values; y-axis suppressed, pale rising line with 3x ratio badge
- 공통축·라벨: 원본처럼 y축은 간소화하고 직접 수치 표기
- 주의: 비율 분모를 비교대상 간 혼동하지 않으며 인과 결론을 도출하지 않는다.

## 데이터 확보 및 모델링 레시피 (제안이지 원본 구현 주장 아님)
Survey executives on employee-centricity and an explicit AI-maturity definition; group respondents; denominator=valid respondents within each centricity group; rate=100*AI-mature/valid; inspect weights/confounding and confidence intervals before cross-group conclusions.

표본·가중치 및 상세 계산식은 공개된 범위만 기록한다: BCG Global Leadership Survey 2026; 563 senior company executives across the survey, subgroups undisclosed.

## 메시지 성립 조건·반례·한계
58%>18%; the association is not evidence that employee-centricity caused AI maturity.
반대되는 관측값이 나오면 액션 타이틀과 결론을 바꾼다. 단위/분모/범주를 재정의하지 않고 수치를 합치지 않는다.

## 원본 확인과 검증 한계
원본 그림을 웹 미리보기로 직접 확인했으며 값 18,29,36,58 및 상승 화살표(3×)를 비교했다.

## 재사용
config.json의 THEME.source/neutral에서 색·폰트·공간을, CONTEXT에서 제목·라벨·출처·범주 순서를 바꾸고 data.csv의 reported 값을 새 데이터로 교체한다.

```bash
python chart.py --theme source --data data.csv --output output.png
python chart.py --theme neutral --data data.csv --output output_neutral.png
```

유사 업무 예: AI 조직 역량별 성공률의 비인과적 비교.
