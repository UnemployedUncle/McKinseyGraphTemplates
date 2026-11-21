# BCG — Agentic AI adds materially to future CPU capacity demand

## 원문 정보
- 공식 출처: https://www.bcg.com/publications/2026/ai-data-center-supply-demand-outlook
- 게시일: 2026-11-20 · 수집일: 2026-11-22 · 데이터 조사/전망 기간: 2025–2031 forecast (BCG model, September 2026)
- 원본 그림 위치: Slideshow slide 4 of 9 — Agentic AI CPU growth · 원본 직접 열람: 확인

## 글 요지 — 3문장
1. BCG는 데이터센터 CPU 설치 수요가 2025년부터 2031년 사이 크게 늘 것으로 전망한다.
2. Agentic AI의 orchestration 요구가 기존 범용 CPU 증가분에 추가 성장요인이 될 수 있다고 설명한다.
3. 슬라이드 4는 설치 기반·전통적 CPU 성장분·AI 기여분을 누적 막대로 구분한다.

## So what — 단 하나
2031년 BCG 모형상 CPU 설치 용량 총 53GW 중 기준 설치기반 약 28GW 외에 기존 수요 성장 약 12GW, AI 추가 수요 약 13GW가 포함된 것으로 판독된다.

## 비즈니스 판단의 연결
- 맥락: AI 데이터센터 CPU 설비의 구매·공급부족, 투자와 공급망 시나리오 판단.
- 지표·단위·기간·분모/비교기준: GW; 2025–2031 연도별 installed base 구성. 총값은 원그림 라벨 reported, 구성값은 소형 도형 판독에 의한 digitized_estimate ±1GW.
- 판단: 2031년 BCG 모형상 CPU 설치 용량 총 53GW 중 기준 설치기반 약 28GW 외에 기존 수요 성장 약 12GW, AI 추가 수요 약 13GW가 포함된 것으로 판독된다.
- 인사이트 유형: component of growth / forecast stacked bars

## 그래프 설계 분석
- x 인코딩: year; y 인코딩: CPU capacity (GW)
- 색·라벨·정렬·축·주석·범례·여백: 2025–2031 연도를 오름차순 배열하고 installed 28GW, traditional growth, AI uplift를 진녹/녹청/연청 3색 누적막대로 구분; 각 총량을 상단에 직접 표시. 0부터 시작하는 축.
- 데이터 원천·표본·계산법: BCG 슬라이드 4/9; 2026년 9월 BCG 내부 수급 모형. 표본 구성·지역별 추정방식은 미공개. BCG 공개된 2026년 9월 자체모형; 독립 표본·모형 계수 미공개. 2025 28GW; 2031 28+12+13=53GW. Component digits ±1GW.

## Reuse data_recipe
1. 원그림의 연도별 total label을 reported로 기록한다.
2. segment 높이는 원그림 눈금으로 판독하고 ±1GW 오차를 명시한다.
3. 연도별 current+traditional+AI=total 근사 합을 확인한다.
4. THEME 색상과 CONTEXT 축 라벨, CSV 입력을 교체해 동일 구조로 재사용한다.

## 성립조건·반례·한계
원그림에서 판독한 구성값은 정밀한 모형 입력값이 아니다. 2026 AI 효과가 0으로 반올림된 것은 실제 0이라는 의미가 아니며 전망 모형·지역분포 변화에 따라 결과가 달라진다.
원본 슬라이드 시각적으로 열었지만 개별 segment 값은 소형 그래프 판독 추정이라 정량 원본 재현 점수 부여 불가.

## 실행 방법
- `pip install -r requirements.txt`
- `python chart.py --data data.csv --config config.json --theme source --output source.png`
- `python chart.py --data data.csv --config config.json --theme neutral --output neutral.png`
- 출처 수치를 교체할 때 `provenance`, `denominator`, `unit`, `period`를 함께 검증한다.
- 생성 이미지는 불변 Bronze 밖 `artifacts/`에 둔다. 자체검증과 사용자 승인은 별개이다.
