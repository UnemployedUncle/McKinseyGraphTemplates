# Bain — 글로벌 특수화학 시장 지역별 비중 (Figure 2)

## 출처 및 사실
- 공식 글: **Chemical Companies Don’t Have to Settle for Managed Decline**, 2026-10-19.
- Figure 2: *By 2030, China is expected to capture almost one-third of the global specialty chemicals market*.
- 원본 이미지: https://public.flourish.studio/visualisation/30502197/thumbnail (이번 실행에서 직접 확인; 원본 파일은 보관하지 않음).
- 데이터 출처: Bain analysis, CEFIC, S&P Global Energy Platts; 표본과 상세 추정 모형은 공개되지 않음.
- 2030년 예상 전체 시장 **$911B**. 중국 31%, 북미 19%, 유럽 15%, 동남아 6%, 기타 30%는 모두 원문 이미지 라벨에서 확인한 **reported** 값. 표시값의 합은 반올림 때문에 101%.

## 글 요지 (3문장)
화학업의 과잉설비와 원료원가 차이는 일시적 사이클이 아닌 구조적 변화로 분석된다. 중국은 기초화학뿐 아니라 특수화학에서도 시장 지위를 강화하고 있다. 사업자는 기존 비용절감만 반복하기보다 지역·품목별 경쟁 우위를 선택하고 포트폴리오를 조정해야 한다.

## 단 하나의 So what
**2030년 특수화학 시장에서 중국 비중이 북미와 유럽을 각각 크게 앞설 것으로 전망되므로, 기존 서구 중심 시장·투자 전략을 재검토해야 한다.**

## 비즈니스 맥락 → 숫자 → 판단
| 구분 | 내용 |
|---|---|
| Business context | 글로벌 특수화학 시장 지역 구도의 변화 |
| Metric | 글로벌 특수화학 매출시장 중 지역별 비중, % |
| Base | 2030E $911B 전세계 시장 = 100% |
| Period | 2030 전망, 관측된 2030 실적 아님 |
| Comparison | 중국 31 vs 북미 19 vs 유럽 15 vs 동남아 6 vs 기타 30 |
| Observation | 중국이 단일 지역 기준 최대 비중 |
| Decision suggestion | 신규 설비·M&A·R&D 포지셔닝에서 중국의 수요·경쟁력을 별도 고려 |

## 시각화 해부
인사이트 유형 **composition**. 원본은 세로형 단일 **100% 누적 막대**: y축 0~100%, 하단 중국 선명한 빨강, 북미·유럽·동남아 밝은 회색의 농도 차이, 상단 기타 지역 어두운 회색. 내부 직접 라벨과 위쪽 **$911B** 표시. 순서를 통해 중국의 구성비를 하단에 강조하고 범례 없이 모든 구성요소를 인지시킨다. 제목은 구성 전망을 직접 말하는 설명형 메시지이다. 가로축 눈금·크기 인코딩·이중축은 없다.

### 반올림 정합성
31+19+15+6+30=101. 원문 라벨을 고치거나 비율을 100으로 맞춰 조작하지 않는다. `chart.py`는 각 구간의 실제 **화면 높이**만 101로 나눠 100%로 정규화하며 표기값은 원문 그대로 둔다. 이를 원문 값 변경으로 취급하지 않는다. 정확한 비반올림 구성비·달러 절대값은 **미공개**.

## 재사용 data_recipe
1. 관측 단위: `product_segment × region × forecast_year`; 지역 경계·제품 포함 범위를 정한다.
2. 공시/산업 DB/판매자료에서 통일된 통화의 2030E 시장액을 추정하며 중복 거래와 지역별 공장/판매지 기준을 해결한다.
3. 기간·명목/실질·환율·계열 연결 여부를 정제한다. 결측이 있으면 추정치와 관측값을 구별한다.
4. 각 지역 비중=`region_market_value / global_market_value × 100` 계산. 미공개 원모형을 사용했다고 단정하지 않는다.
5. 반올림 전 합계 100%를 검증한 뒤 차트용 지역순서·하이라이트·직접 라벨을 생성한다.
6. 중국 비중이 가장 크지 않거나 지역 정의가 바뀌면 So what과 색 강조를 갱신한다.

## 메시지 성립 조건·한계
전망치라는 사실을 제목·주석에서 계속 명시한다. 지역별 전망 비중만으로 회사별 이익률, 기술 우위, 실제 2030 매출을 결론 내리지 않는다. 반올림의 차이로 진짜 점유율 순위가 뒤바뀌지 않는지는 원자료로 점검한다.

## 재사용
`config.json`의 `THEME.source/neutral`과 `CONTEXT`의 title/subtitle/total_label/series_order/source_note, 그리고 `data.csv`를 변경한다. 예: 상사업의 지역별 철강 매출 구성. `python chart.py --theme source --data data.csv --output output.png` 또는 `--theme neutral` 실행. 최초 코드 해시는 Bronze manifest로 관리한다. **원본 대비 자체평가는 validation.json 참고; 사용자 검수는 pending**.
