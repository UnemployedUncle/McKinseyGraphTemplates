# McKinsey — Closing the women's health gap: Switzerland's CHF 7 billion opportunity / Exhibit 1

- 공식 출처: https://www.mckinsey.com/mhi/our-insights/closing-the-womens-health-gap-switzerlands-chf-7-billion-opportunity
- 공개일: 2026-10-19 · 이 실행 열람일: 2026-10-26 · 원본 시각 자료(저장하지 않음): https://www.mckinsey.com/~/media/mckinsey/mckinsey%20health%20institute/our%20insights/closing%20the%20womens%20health%20gap%20switzerlands%20chf%207%20billion%20opportunity/exhibit%20svgz%20files/health-gap_exhibit%201_v2.svgz
- 데이터/조사 시점: Model based on GBD 2019; analysis published 2026 · 원자료: IHME Global Burden of Disease Study 2019; McKinsey Health Institute analysis; modeled disease-burden categories
- 그림 번호: Exhibit 1 · 유형: horizontal_share_stack · 인사이트 유형: composition

## 글의 요지 (원문 사실의 요약)
Swiss female disease burden composition, not the between-sex health gap를 공식 자료에서 정량적으로 분석한다. 원문 수치를 비교해 전략적 논점을 제공한다. 공개되지 않은 집단별 분모·원시자료는 추정하지 않는다.

## So what (에이전트 해석)
스위스 여성의 전체 질병부담 중 여성만의 고유 질환은 8%이고, 양성 모두에 영향을 주지만 여성에서 더 빈번한 질환이 63%이므로 여성건강 투자는 생식건강을 넘어 공통 질환의 성차에 초점을 넓혀야 한다.

## 비즈니스 맥락 → 숫자 → 판단

| 비즈니스 맥락 | 지표/분모 | 기간·단위 | 관찰 및 결정상 시사점 |
|---|---|---|---|
| Swiss female disease burden composition, not the between-sex health gap | total health burden among women in Switzerland (DALYs) | Model based on GBD 2019; analysis published 2026, percent | 스위스 여성의 전체 질병부담 중 여성만의 고유 질환은 8%이고, 양성 모두에 영향을 주지만 여성에서 더 빈번한 질환이 63%이므로 여성건강 투자는 생식건강을 넘어 공통 질환의 성차에 초점을 넓혀야 한다. |

원문 보고값: female_specific 8%, female_prevalent 63%, female_different 4%, no_known_difference 25%. 합성·임의 추정값을 사용하지 않았다.

## 시각화 설계 해부
- X 인코딩: 전체 여성 DALY 비중(0–100%); Y 인코딩: 단일 기준집단의 구성
- 색: THEME.source.palette 또는 bar_color; 정렬: config.json의 category_order; 원본 특징과 차이는 validation.json 참조
- 강조 수단: single 100% stacked horizontal bar, four fixed mutually exclusive categories, direct segment percentages, legend maps all categories
- 공통축·라벨: 정확히 100% 전체 구성으로 제한한 단일 행, 범례에 각 범주 비율 병기
- 주의: 비율 분모를 비교대상 간 혼동하지 않으며 인과 결론을 도출하지 않는다.

## 데이터 확보 및 모델링 레시피 (제안이지 원본 구현 주장 아님)
Collect DALYs by disease, sex, location and age; classify conditions as sex-specific, more prevalent among women, affecting women differently, or neither; sum female DALYs by group; divide by all female DALYs; maintain consistent year, classification and standardization.

표본·가중치 및 상세 계산식은 공개된 범위만 기록한다: IHME Global Burden of Disease Study 2019; McKinsey Health Institute analysis; modeled disease-burden categories.

## 메시지 성립 조건·반례·한계
63% is the largest component; 8% is sex-specific. These are shares of all female DALYs, not the women-versus-men excess DALY gap.
반대되는 관측값이 나오면 액션 타이틀과 결론을 바꾼다. 단위/분모/범주를 재정의하지 않고 수치를 합치지 않는다.

## 원본 확인과 검증 한계
원문 SVGZ가 이미지로 렌더링되지 않아 원본 그림의 색·축·위치 구조를 직접 검증하지 못했다. 작성한 것은 공개된 수치를 활용한 대안 시각화이다.

## 재사용
config.json의 THEME.source/neutral에서 색·폰트·공간을, CONTEXT에서 제목·라벨·출처·범주 순서를 바꾸고 data.csv의 reported 값을 새 데이터로 교체한다.

```bash
python chart.py --theme source --data data.csv --output output.png
python chart.py --theme neutral --data data.csv --output output_neutral.png
```

유사 업무 예: 사업부별 매출 구성비의 상호배타적 분해.
