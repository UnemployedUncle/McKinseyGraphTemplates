# AI features more often in strong growers’ plans

## 출처와 사실
- [BCG 공식 원문](https://www.bcg.com/publications/2026/ai-reshaping-corporate-growth-strategy) · 게시 2026-11-25 · 수집 2026-11-27 · Exhibit 1
- BCG는 매출 성장 기업들의 AI 관련 공시를 조사했다. 생성형 AI 확산 이후 성장 전략에서 AI 언급이 증가했다. 특히 업종 대비 성장률이 높은 기업 집단에서 증가폭이 크다.

## So what
AI를 비용 절감뿐 아니라 성장 전략과 연결하되 공시 연관성을 인과 효과로 해석하지 말아야 한다.

## 비즈니스 맥락과 지표
성장 성과별 AI 활용 신호 비교 → percent of companies / 2017–2022; 2023–2025 / 매출 2025년 10억 달러 이상이며 둘 중 한 기간 이상 업종 성장률을 초과한 상장사 3,669개; 집단별 n 미공개 → 동일 기준 비교로 판단.

## 원본 관찰 및 데이터
기간 x, 기업 비중 y, 성과 그룹별 짝막대, 초과 성장 집단 초록 강조, 0 기준 및 직접 레이블, 내부 범례.
출처/표본/계산: S&P Capital IQ, earnings reports, call transcripts, public announcements, BCG analysis; 수집일 미공개.
원본 그림에서 공개값 4개 확인. 제목 재작성, 글꼴·범례 박스·축 여백 근사.
공개값: 이전 3.5/5.5%, 이후 5.7/15.5% (미달/초과). 이후 집단 격차 9.8%p, 이전 2.0%p.

## 재사용 data_recipe (제안)
1. 두 기간에 대해 동일 기업 모집단을 정의한다.
2. 성과 기준으로 상호 배타적 집단을 정의한다.
3. AI 성장 관련 언급 기업수/해당 집단 기업수×100을 계산한다.
4. 기간별 짝막대를 동일 0 기준 축에 표시한다.

## 성립 조건·반례
집단 정의와 공시 코딩 규칙이 일정해야 한다. 공시 언급은 실제 배포나 매출 기여와 다르며 선택편향·역인과가 가능하다.

## 사용
`pip install -r requirements.txt`; `python chart.py --theme source --output source.png --dpi 200`; neutral로 교체 가능. CSV와 config 수정 후 별도 작업폴더에서 실행.
