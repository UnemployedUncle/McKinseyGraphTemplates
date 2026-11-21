# McKinsey — Australia/NZ growers lead global agtech adoption

## 원문 정보
- 공식 출처: https://www.mckinsey.com/industries/energy-and-materials/our-insights/blog/australian-and-new-zealand-farmers-adopt-agtech-at-twice-the-rate-of-their-global-peers
- 게시일: 2026-11-20 · 수집일: 2026-11-22 · 데이터 조사/전망 기간: Global survey April–July 2026; AUS/NZ supplement July 2026
- 원본 그림 위치: Exhibit 1 related reported survey values — editorial AUS/NZ vs global · 원본 직접 열람: 미확인

## 글 요지 — 3문장
1. McKinsey의 2026 농가 조사에서 호주·뉴질랜드 농가의 Agtech 도입률은 세계 평균보다 높다.
2. 디지털 도구의 현장 활용 범위는 농업 관련 소프트웨어·정밀장비 및 생성형 AI에 걸쳐 넓다.
3. 기술 기업의 GTM 전략에서는 디지털 제품과 로컬 인적 지원을 함께 고려할 필요가 있다.

## So what — 단 하나
2026년 AUS/NZ 응답 농가의 Agtech 도입률 86%는 글로벌 46%보다 40%p 높으며 digital agronomy 등 제품별 도입에서도 격차가 보고되었다.

## 비즈니스 판단의 연결
- 맥락: Agtech 업체 시장 진출 우선순위와 제품별 확산, 도입 촉진 및 현장 지원 설계.
- 지표·단위·기간·분모/비교기준: 조사 응답 농가 중 해당 기술을 사용한다고 응답한 비율(%), 2026년 4–7월; AUS/NZ 약 150명, 글로벌 약 5,500명; 집단별 서로 다른 모집단.
- 판단: 2026년 AUS/NZ 응답 농가의 Agtech 도입률 86%는 글로벌 46%보다 40%p 높으며 digital agronomy 등 제품별 도입에서도 격차가 보고되었다.
- 인사이트 유형: adoption gap by survey segment

## 그래프 설계 분석
- x 인코딩: respondent share (%); y 인코딩: product category
- 색·라벨·정렬·축·주석·범례·여백: AUS/NZ vs global 2군 막대를 가로방향으로 배치하고 카테고리는 AUS/NZ 높은 순으로 정렬; 직접 값 레이블 표시, 최대 100% 축.
- 데이터 원천·표본·계산법: McKinsey Global Farmer Insights 2026, 약 5,500 농가/10개국 조사(4–7월), 호주·뉴질랜드 약 150개 농가 추가조사(7월). 가중치·구간 추정 미공개. McKinsey 2026 survey n~5,500 across 10 countries and AUS/NZ n~150; methodology weighting unavailable. any agtech +40pp = 86−46; other categories +37,+33,+31,+18pp.

## Reuse data_recipe
1. 조사 질문과 응답 비율 분모를 정의한다.
2. 두 집단의 기술별 사용 응답률을 CSV 컬럼에 reported로 기록한다.
3. difference_pp=aus_nz_pct−global_pct로 계산해 derived 표기한다.
4. 복수 응답 가능하므로 기술별 비율을 더해 100%라고 해석하지 않는다.
5. THEME,CONTEXT,CSV 수정만으로 타 산업 제품 채택률 비교에 재사용한다.

## 성립조건·반례·한계
지역·글로벌 샘플 특성이 다를 수 있고 글로벌 집단이 지역 부분표본을 포함할 가능성을 고려해야 한다. 이는 기술 구매 전환이나 정책 효과의 인과추정이 아니다. 원본 Exhibit 1 SVGZ는 시각적 확인 불가였고 원본은 지역별 비교여서 본 차트는 편집형.
원본 Exhibit 1은 SVGZ라 직접 열지 못했고 지역별 비교 구성이 다름. 편집형 paired horizontal은 원본 재현 점수를 받을 수 없음.

## 실행 방법
- `pip install -r requirements.txt`
- `python chart.py --data data.csv --config config.json --theme source --output source.png`
- `python chart.py --data data.csv --config config.json --theme neutral --output neutral.png`
- 출처 수치를 교체할 때 `provenance`, `denominator`, `unit`, `period`를 함께 검증한다.
- 생성 이미지는 불변 Bronze 밖 `artifacts/`에 둔다. 자체검증과 사용자 승인은 별개이다.
