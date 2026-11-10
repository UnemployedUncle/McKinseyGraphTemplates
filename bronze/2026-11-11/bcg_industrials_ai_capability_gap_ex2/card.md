# BCG — Industrial AI capability gaps | Exhibit 2

## 원문 요지 (3문장)
BCG는 산업기업의 AI 가치 창출이 도구 배포만으로 완성되지 않고 프로세스·조직 재설계를 필요로 한다고 분석한다. 조사에서는 산업기업과 기타 업종 사이에 데이터 관리 역량 격차가 나타난다. 특히 데이터 전략 역량의 격차가 가장 큰 것으로 보고된다.

**So what:** 산업기업의 AI 전환에서는 모델 도입 속도만이 아니라 데이터 전략을 먼저 진단하고 업무·운영모델의 변경을 검토해야 한다.

## 비즈니스 맥락 → 지표 → 판단
- 문제: 어떤 데이터 역량이 다른 업종보다 특히 부족한가?
- 관측 단위: 데이터 역량 영역 × 업종 그룹, BCG Applied AI Index 2026.
- 지표: best-in-class 기업 비율(%)과 산업기업-타업종 차이(%p). Best-in-class는 해당 차원 0–100점 중 75점 초과.
- 비교: Data strategy 10%/-8%p, governance 15%/-5%p, quality 11%/-4%p, product 9%/-4%p, compliance 31%/-2%p.
- 공개된 산업기업 비율 및 gap은 reported; 타업종 비율 18%, 20%, 15%, 13%, 33%는 industrial_pct-gap_pp로 derived.
- 분모: 각 업종 그룹의 응답기업 집단. 표본 크기·가중치 및 조사항목별 검정은 공개 도표만으로 확인되지 않음.
- 판단: Data strategy -8%p를 첫 진단 항목으로 삼되 실제 투자 우선순위는 기업의 위험·운영제약에 따라 조정한다.

## 인사이트·시각적 인코딩
유형: 업종별 데이터 역량 격차 진단. 원본 Exhibit 2는 5열 KPI 카드다. X는 다섯 역량(원본 순서), 카드의 상단은 산업기업과 타업종 격차(%p), 중앙은 산업기업의 best-in-class 기업 비중(%), 하단은 역량명이다. 시각화 상의 y축/점 크기나 누적 단위는 존재하지 않으며, 동일 크기 카드가 표본 크기가 같다는 의미는 아니다. 원본 유사 녹색 계열/중립 테마, 직접 숫자라벨, 영역별 고른 여백을 사용한다. 원본의 설명 문단은 코드 편집본에서 생략했음을 검증 기록에 명시한다.

## 공개 데이터·추론의 한계
원문 2026-11-10, BCG Exhibit 2, BCG Applied AI Index 2026. 정확한 필드조사일 및 집단별 상세 표본은 미공개로 둔다. %와 %p는 각각 기업 비율과 집단 간 차이로 구분한다. 다른 업종 값은 명시적 계산 결과이며 원본에 독립적으로 보고된 응답값으로 취급하지 않는다.

## 재사용 data_recipe
1. 동일한 시점·설문 정의로 company_id, sector_group, capability, score, weight를 수집한다.
2. 공통 score cutoff(예: 75 초과)에 따라 best_in_class(Boolean)을 산출한다.
3. 섹터 집단별 달성률을 같은 분모 정의로 집계한다.
4. gap_pp = industrial_pct - other_sector_pct를 계산하고 부호·반올림·누락을 확인한다.
5. data.csv, config.json의 THEME.source/neutral 및 CONTEXT만 바꾸고 render(data,theme,context)로 재사용한다.

## 메시지 성립 조건·반례
산업별 조사 표본과 점수 기준이 비교 가능할 때에만 집단별 차이가 의미 있다. 격차는 조직 역량의 연관성을 보여줄 뿐 데이터 전략이 수익 향상을 직접 유발한다는 실험적 인과근거가 아니다. 이미 역량이 충분하거나 강한 규제가 있는 산업기업은 우선순위가 다를 수 있다.

## 실행
pip install -r requirements.txt
python chart.py --data data.csv --config config.json --theme source --output source.png
python chart.py --data data.csv --config config.json --theme neutral --output neutral.png
