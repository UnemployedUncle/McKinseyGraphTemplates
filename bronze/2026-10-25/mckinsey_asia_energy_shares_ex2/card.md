# McKinsey · Asia's Energy Reckoning — 편집형 Exhibit 2 요약

- 출처: McKinsey, **Asia’s energy reckoning: Securing the energy system to drive growth**, 2026-10-22; https://www.mckinsey.com/featured-insights/future-of-asia/asias-energy-reckoning-securing-the-energy-system-to-drive-growth
- 그림 번호: Exhibit 2, “Asia is at the epicenter of the energy transition...” / 원본 그림 링크는 본문 Image(Exhibit 2) 참조. 원본 SVGZ가 제공되지만 보기 도구의 형식 제약으로 실제 원본 그림을 열지 못했다. **충실도 점수 미산정**.

## 원문 요지 (3문장)
McKinsey는 수요 증가와 수입 의존 때문에 아시아의 에너지 시스템이 구조적 취약성에 노출됐다고 진단한다. 아시아는 세계 GDP의 38%와 에너지 수요의 약 50%, 온실가스 배출의 55%를 차지한다. 보고서는 국내 생산·대체 에너지·인프라를 함께 고려한 회복탄력성 투자를 강조한다.

## So what
**아시아는 경제 비중보다 높은 에너지 소비·배출 비중을 가지고 있으므로, 성장 전략과 함께 공급안보 및 에너지 효율 투자를 검토해야 한다.**

## 맥락 → 숫자 → 판단
| 관측 맥락 | 수치 | 기간/분모 | 판단 |
|---|---|---|---|
| 세계 경제 내 비중 | 38% | 세계 총 GDP | 기준 규모 |
| 세계 에너지 소비 | 약 50% | 세계 총 에너지 수요; 원문은 nearly 50% | 경제 비중 대비 높은 수준 |
| 온실가스 | 55% | 세계 총 온실가스 배출 | 전환 전략의 중요한 이해관계자 |

## 시각화 (독립 재설계, 원본 재현이 아님)
- 가로 막대, x=세계 총량 대비 비중(%), y=GDP/에너지 수요/온실가스, 색으로 온실가스 강조. 0~100% 공통 축, 각 값 직접 라벨.
- 원본 Exhibit 2는 복합 시각화이나 원본 그래프 원화상을 직접 확인하지 못해 본 코드는 **공개된 요약 수치 세 항목만을 편집형으로 표현**했다. 원본 일치도 7항목은 평가 불가다.
- 인사이트 유형: 비교 / 격차. 표본은 개별 소비자 설문이 아니라 기관별 거시 시나리오 분석이다. 통계적 인과를 주장하지 않는다.

## 재사용 data_recipe
`region,period,metric,value,unit,source`를 지역/기간별 공식 GDP·에너지 수요·배출 원자료에서 수집한다. GDP PPP/명목 기준, 에너지 수요의 1차/최종 수요, 배출의 CO2/전체 GHG 등 정의를 통일한다. `region_value / world_value × 100`으로 비중을 계산하고 동일 기간인지 확인한다. 항목마다 분모의 측정 단위가 다르므로 서로 더하지 않는다. 보고서의 수요 전망은 Continued Momentum 기준이라는 가정이 있다.

## 메시지 성립 조건 및 반례
동일한 산정 기준에서 에너지와 배출의 비중이 GDP 비중보다 높을 때에만 '경제규모 이상의 에너지·배출 비중' 메시지가 성립한다. 기준을 바꾼 데이터를 대입하면 제목도 바꿔야 한다. 3개 비중만으로 개별 국가의 배출집약도, 기업별 투자수익, 오일 수입 취약성을 예측할 수 없다.

## 재사용 방법
`config.json`의 `THEME.source/neutral` 및 `CONTEXT.title,subtitle,category_order`를 바꾸고 `data.csv`의 비율값을 교체한다. 프로젝트 예: 사업지역별 수입노출·해외매출·설비투자 비중의 비교 (단 각 비중 분모 설명 필수).

실행: `python chart.py --theme source --data data.csv --output output.png`.

## 권한
제3자 원본 이용조건 미검증. `training_eligible=false`; 라이선스 검토 전 외부 상업 학습에 사용하지 않는다.
