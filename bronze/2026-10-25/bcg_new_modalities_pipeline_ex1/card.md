# BCG · New Drug Modalities 2026 — Exhibit 1

- 출처: BCG, **New Drug Modalities 2026**, 2026-10-22; 원문: https://www.bcg.com/publications/2026/new-drug-modalities-pipeline-plateau
- 그림: Exhibit 1, “Conventional and New Modalities' Shares of Projected Pipeline Value”; 원본 공식 이미지: https://web-assets.bcg.com/dims4/default/1d1a827/2147483647/strip/true/crop/3600x1994%2B0%2B0/resize/499x276%21/format/webp/quality/80/?url=http%3A%2F%2Fboston-consulting-group-brightspot.s3.amazonaws.com%2Fbc%2Ffe%2F5d3c748e412287719f4a14bfc5b7%2Fnew-drug-modalities-2026-ex01.png
- 관찰: 공식 Exhibit 1 이미지를 직접 열어 수치·막대 수·색상·수치표시·레이아웃을 확인했다. 원본 픽셀/로고 파일은 보존하지 않았다.

## 원문 요지 (3문장)
2026년 전 세계 의약품의 5년 후 예상 파이프라인 가치는 $347B로 전년의 $330B보다 증가했다. 신기전 치료제 비중은 60%에서 57%로 낮아졌지만 여전히 절반을 넘는다. 기존 치료제의 예상 가치가 성장하며 파이프라인 구성비가 달라졌다.

## So what
**신기전 치료제의 비중은 여전히 우세하지만, 기존 치료제가 빠르게 회복되는 만큼 투자 포트폴리오를 하나의 기술군에 편중하기보다 가치 변화의 원인별로 재평가해야 한다.**

## 맥락 → 숫자 → 경영 판단
| 맥락 | 수치/단위 | 관측 기준 | 판단 |
|---|---|---|---|
| 파이프라인 전체 성장 | 2025 $330B → 2026 $347B | 매년 시점의 향후 5년 예상 매출가치 | 절대 규모 증가와 구성 변화 분리 |
| 신기전 우위 지속 | 60% → 57% (-3%p) | 각 연도 전체 파이프라인 예상 가치가 분모 | 점유율 하락≠절대가치 붕괴 |
| 기존 치료제 반등 | 40% → 43% (+3%p) | 보완적인 합계 100% 두 분류 | 모달리티별 수익전망 재점검 |

## 시각화 설계 해부 (실제 원본 관찰)
- 주요 유형: **절대 규모를 반영한 세로 누적 막대**; 구성(composition), 보조 추세(trend).
- 인코딩: x=2019~2026 파이프라인 시점; 막대 전체 높이=향후 5년 총 예상 가치($B); 두 분할 높이=총 예상 가치×해당 분류 비중; 색=신기전 초록, 전통 회색.
- 위쪽은 연도별 총액을 직접 라벨링, 각 구간 중앙은 퍼센트 라벨. x는 연대순, 범례는 하단, y축 숫자 눈금과 그리드는 제거한다. 대조적인 초록색으로 신기전의 지배적 비중을 부각한다.
- 제목은 주장형보다는 설명형이다. 총액/비율을 한 도표에 넣어 수치 메시지의 두 축을 함께 보여준다. y축이 숨겨져 있기 때문에 막대가 절대 총액에 비례하는지 명시해야 한다.

## 데이터 확보와 모델링
- BCG 원문 출처: **Evaluate Pharma와 BCG 자체 분석**; 실제 개별 약물 집계 기준·추정 알고리즘·가중치는 여기 공개된 도표만으로 확인할 수 없다. 보도자료 숫자를 환산하거나 추측해 추가하지 않았다.
- raw: `pipeline_year`, `product_id`, `modality_class`, `five_year_forward_revenue_forecast_usd` (가능한 라이선스가 있는 데이터 소스에서 수집).
- cleaning: 시점별 중복 약물 ID 제거 → modality class 동일 매핑 → 결측·통화·평가 기준 확인 → 동일 시점 분모로 합산.
- model: `total_forecast = SUM(forecast_usd)`; `segment_share_pct = segment_forecast / total_forecast * 100`; 구성비 100% 검증 후 `total × share / 100`으로 막대 높이를 계산한다.
- 리포트의 2025 전망은 '2030년 파이프라인 예측 가치', 2026 전망은 '2031년 예측 가치'다. **같은 약물군의 실제 매출 증감률**로 읽지 않는다.
- CSV는 직접 공개한 총액과 반올림된 구성비 `reported`를 별도 행으로 기록한다. 원본에 없는 세부 치료제 값은 생성하지 않는다. 비중 반올림에 따른 $B 환산은 재현용 기하학적 계산이며 새 관측값이 아니다.

## 메시지 성립·반례·한계
신기전의 57% 우위와 2025 대비 -3%p 변화는 실제로 원본 도표에서 확인된다. 자료가 다른 기준 시점·계산 방법·분류 기준으로 수정되면 비교가 깨질 수 있으므로 제목을 재평가해야 한다. 데이터 자체는 기존 치료제로 자본을 이전해야 한다는 인과효과를 입증하지 않는다. 차트는 BCG 원자료의 일부를 **독립 코드로 연구 목적으로 재구성**한 것이며, 픽셀 동일성을 보증하지 않는다.

## 재사용
`config.json`의 `THEME` 팔레트·배치와 `CONTEXT` 문구·계열 순서를 바꾸고 `data.csv`는 `period,series,value,total`(2개 계열의 비중 합계=100)로 교체한다. 적용 예: 연도별 **포트폴리오 시장규모와 채널별 매출 구성** 비교. 재사용 시 데이터 패턴에 맞는 새 제목을 작성해야 한다.

실행: `python chart.py --theme source --data data.csv --output output.png` (중립 테마: `--theme neutral`).

## 라이선스·학습 제한
BCG 페이지는 컨텐츠의 **AI 상업적 학습·평가·개선** 등에 대해 사전 허가를 요구한다. 이 폴더는 개인 비상업 연구용이며 `training_eligible=false`, `rights_status=permission_required`이다. 코드 MIT 라이선스가 BCG 데이터와 출판물 권리를 대체하지 않는다.
