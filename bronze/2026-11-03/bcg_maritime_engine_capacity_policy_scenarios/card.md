# BCG — Charting the Maritime Fuel Transition | Exhibit 2 context (two reported engine-capacity values; editorial visualization)

**공식 원문:** https://www.bcg.com/publications/2026/maritime-fuel-mix-regulation-cost  
**게재일:** 2026-11-02 / **수집 및 코드 생성일:** 2026-11-03 / **데이터 시점:** modeled 2050  
**원본 그림 위치:** Exhibit 2 context (two reported engine-capacity values; editorial visualization) / 원본 이미지 파일은 저장하지 않음.

## 글의 요지 (3문장)
1. 글로벌 해운의 탄소가격 정책에 따른 엔진·연료 투자 유연성을(를) 다룬 공식 자료다.
2. 2050년 탄소가격 정책 시나리오에 따라 탄소포집 없는 기존 엔진의 선대 용량 비중이 19%에서 37%로 달라질 수 있으므로, 선주와 항만 운영자는 단일 연료 전략 대신 규제 시나리오별 유연성을 확보해야 한다.
3. 원문에서 확인 가능한 수치는 기록했으나 원본 차트의 모든 시각적 요소는 확인하지 못했다.

## So what
2050년 탄소가격 정책 시나리오에 따라 탄소포집 없는 기존 엔진의 선대 용량 비중이 19%에서 37%로 달라질 수 있으므로, 선주와 항만 운영자는 단일 연료 전략 대신 규제 시나리오별 유연성을 확보해야 한다.

## 비즈니스 맥락 → 숫자 → 판단
- 관찰: 원문은 2050년 고탄소가격 시나리오에서 OCCS 미장착 기존 엔진 용량 비중 19%, 지역 규제 중심 시나리오에서는 37%를 제시한다.
- 해석: 동일한 2050년 엔진 용량 비중 지표라도 규제 시나리오에 따라 18%p 차이가 난다.
- 재사용 제안: 공급망·생산설비·선대 투자안의 정책 시나리오별 결과를 비교할 때, 서로 다른 종류의 지표를 합산하지 않는 공통 분모 비교 차트를 사용한다.


## 측정·집계 정의
- insight_type: comparison / gap; metric: `conventional_engine_capacity_share_without_occs`
- unit: percentage of the relevant denominator; denominator: global fleet engine capacity in modeled 2050 scenario.
- period: modeled 2050; sample/method: BCG·GCMD의 2050년 연료 믹스 모델 시나리오; 표본조사가 아닌 모델 결과.
- numeric provenance: **reported** (원문에 서술된 값), 항목별 값은 `data.csv`에 기록.
- value retrieval: HTML 기사 본문에 수치가 직접 등장하며 부재한 값은 채우지 않았다.

## 시각화 해부
x=policy_scenario category, y=conventional_engine_capacity_share_without_occs (0–100% concept; display 0–49% with explicit scale), color=regional-only highlight, direct labels and +18 pp annotation.
탄소포집 없는 기존 엔진 용량 비중 19%와 37%를 비교하는 세로 막대. 원본 Exhibit 2의 전체 연료 믹스 차트가 아닌 본문 발표값의 부분 재구성.
색상·주석·레이아웃은 `config.json`의 `THEME`와 `CONTEXT`에 분리했다. 원본 로고·저작권 이미지는 사용하지 않았다.

## 재사용 data_recipe
1. policy_scenario 및 동일한 capacity_unit를 정의한다.
2. 모델에서 scenario별 conventional_engine_capacity_without_occs 및 global_fleet_capacity를 수집한다.
3. 같은 시나리오의 전체 선대 엔진 용량을 분모로 사용하여 비중을 산출한다.
4. 예측 시점(2050)과 정책 가정(Tier 2 carbon penalty 혹은 지역별 규제)을 명시한다.
5. 동일 지표만 막대 비교하고 차이를 percentage points로 표시한다. 완성된 원본 연료 믹스 차트인 척하지 않는다.


## 메시지 성립 조건·반례 및 한계
이는 정책 시나리오 결과 비교로 기술 선택의 확정적 전망이나 실현 가능성은 보장하지 않는다. 2050년 85% fossil fuel consumption의 분모는 엔진 용량 37%와 다르므로 함께 더할 수 없다.

## 정확성·원본 비교
`chart.py` 실행은 검증했으나 원본 그림의 시각적 픽셀·인코딩 비교는 하지 못했다. **편집형 시각화(`validation_status=unverified`, `fidelity_score=null`)**로 저장한다. 설문 수치와 모델 시나리오 수치를 관측 성과로 혼용하지 않는다.

## 사용법
`pip install -r requirements.txt` 후 `python chart.py --data data.csv --config config.json --theme source --output output.png` 실행. `neutral` 테마도 동일하게 동작한다. 값과 문맥이 바뀌면 제목·강조 항목을 새 주장에 맞게 재검토한다.
