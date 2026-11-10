# McKinsey — State service satisfaction intervals | Exhibit 1 article-reported subset

## 원문 요지 (3문장)
McKinsey는 2026년 미국 전역의 20개 주정부 서비스에 대한 50,744명의 경험을 조사했다. 전국 단위의 비슷한 평균 만족도와 달리 동일 서비스에서도 주별 만족도의 편차가 컸다. 서비스별·지역별 차이를 드러내는 지표가 개선의 우선순위 설정에 도움이 된다.

**So what:** 서비스 평균만 볼 것이 아니라 동일 업무의 지역별 최소~최대 성과를 파악해 최우선 개선여지를 식별해야 한다.

## 비즈니스 맥락 → 지표 → 판단
- 문제: 동일 공공서비스의 거주자 만족도가 주마다 얼마나 달라지는가?
- 전체 조사: 2026-04-15~2026-06-06, 50개 주와 DC, 50,744명 응답, 20개 서비스.
- 지표: 거주자 만족(10점 중 9~10점 응답) 비율(%), 서비스별 주의 최솟값~최댓값.
- 공개 두 가지 예: retirement benefits 34~71%; small-business financial assistance 29~69%.
- range width는 max-min의 derived 결과로 37%p와 40%p. 각 최소값과 최대값은 reported.
- 분모: 각 주의 해당 서비스 응답자. 50,744명 전체를 서비스별 응답 분모로 사용할 수 없다.
- 비교/판단: 공통 0~100% 축에서 범위를 비교하며, 어떤 주의 운영 개선 여지가 큰지 별도 원자료를 요청한다.

## 인사이트·시각적 인코딩
유형은 지역 간 운영성과 분산/벤치마크. 원본 Exhibit 1은 서비스 전반의 만족도 분산을 보여주는 별도 도표인데 SVGZ 원본을 시각적으로 열지 못했다. 본 결과는 기사 본문에 명시된 두 서비스의 reported range만 사용한 **편집형 interval plot**이다. X는 만족 응답률(%), Y는 서비스명이며 min→max 수평선, 연한 색=min, 진한 색=max. 직접 라벨과 0~100% 공통축을 유지하고 데이터 없는 중간 분포는 추정하지 않는다. 범례 대신 색상·양 끝 라벨을 사용하며 공식 원본 재현이라고 표시하지 않는다.

## 데이터 출처·표본·계산법
공식 기사 2026-11-09, Exhibit 1과 본문, McKinsey 2026 State of the States Survey (n=50,744). 지역별 개별값·표준오차·가중치 원자료 및 서비스별 응답 수는 이 두 범위에서 미공개. 별도의 Johnson Relative Weights 모델은 두 서비스 범위 계산에 사용하지 않는다.

## 재사용 data_recipe
1. respondent_id, state, service, satisfaction_score, weight, period를 확보한다.
2. 주별 같은 정의와 공통 표본으로 satisfaction_pct(9 또는 10점 응답 비율)를 계산한다.
3. 서비스별 min_pct, max_pct 및 width_pp=max_pct-min_pct를 산출한다.
4. 규모 차이나 표본 편향에 따른 신뢰도를 점검하고 data.csv, THEME, CONTEXT를 바꿔 재생성한다.

## 메시지 조건·반례
주별 측정 기준과 응답 집단이 비교 가능해야 한다. 작은 표본의 극값은 오차에 취약하며, 범위가 넓다고 어떤 특정 규제나 정책의 인과효과를 입증하지 않는다. 서비스 평균은 본 자료에 없으므로 차트에서 임의로 만들어 넣지 않는다.

## 실행
pip install -r requirements.txt
python chart.py --data data.csv --config config.json --theme source --output source.png
python chart.py --data data.csv --config config.json --theme neutral --output neutral.png
