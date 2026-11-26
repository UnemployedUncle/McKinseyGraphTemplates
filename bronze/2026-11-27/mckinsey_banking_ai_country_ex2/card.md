# Banking AI use trails awareness across markets

## 출처와 사실
- [McKinsey 공식 원문](https://www.mckinsey.com/~/media/mckinsey/industries/financial%20services/our%20insights/global%20banking%20annual%20review%202026%20part%202/global-banking-annual-review-2026-the-ai-disruption-dividend.pdf) · 게시 2026-11-17 · 수집 2026-11-27 · PDF zero-based page 7, Exhibit 2 — consumer awareness and use of gen AI
- 2026년 소비자 금융 설문에서 생성형 AI 인지도는 높았다. 일반 목적 사용은 인지도보다 낮고 금융 목적 사용은 더 낮았다. 국가별 이용 수준의 차이는 금융 채널 전략을 세분화할 근거를 제공한다.

## So what
AI 인지도와 일반 사용, 금융 사용을 분리하여 국가별 전환 과제를 진단해야 한다.

## 비즈니스 맥락과 지표
국가별 AI 채택 단계 비교 → percent of respondents / June 2026 / 13개국 약 46,000명 소비자; 국가별 표본은 반올림 공개; 각 비율은 해당 응답자 기준 → 동일 기준 비교로 판단.

## 원본 관찰 및 데이터
국가 y, 응답 비율 x, 세 개 색의 점열/연결선, 평균 별도 패널, 교대 회색 행과 0–100 격자, 평균만 공개 레이블.
출처/표본/계산: McKinsey Global Banking Annual Review Consumer Survey 2026; 국가별 가중치 미공개.
평균 3개 공개값, 국가별 39개는 PDF 스크린샷 좌표 근사(±2%p); 선 및 패널 여백/글꼴 근사.
판독식: round((점 중심 x−425)×100/437), 1088×1408 페이지 스크린샷, x=425/862를 0/100으로 보정. 중심 수동 판독 및 반올림 ±2%p. 평균은 별도 공개값이며 국가 평균으로 재산출하지 않음.

## 재사용 data_recipe (제안)
1. 국가별 동일 문항의 응답 비율을 확보한다.
2. 인지/일반 사용/금융 사용을 분리하고 동일 분모인지 확인한다.
3. 금융 사용 기준 원본 순서를 보존하고 평균을 별도 행에 둔다. Canada/Netherlands의 1%p 역전은 판독 오차 범위다.
4. 동일 0–100 축에 세 점열을 연결하되 국가 간 흐름이 아님을 표시한다.

## 성립 조건·반례
국가별 표본 및 가중치가 비교 가능해야 한다. 각 점열은 범주 간 연결이 아니라 순위 비교이며 개인별 전환율·인과효과가 아니다.

## 사용
`pip install -r requirements.txt`; `python chart.py --theme source --output source.png --dpi 200`; neutral로 교체 가능. CSV와 config 수정 후 별도 작업폴더에서 실행.
