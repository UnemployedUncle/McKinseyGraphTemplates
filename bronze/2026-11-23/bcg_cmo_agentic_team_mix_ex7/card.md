# BCG: Exhibit 7 — More Than One-Quarter of the Team Will Be Agentic AI Dovetailing with Humans

## 원문 요지 (3문장)
1. CMO Survey 2026: How Agentic AI Will Reshape the Marketing Team는 2026 survey, now vs forecast in 2–3 years를 정량적으로 분석한다.
2. CMO가 예상하는 Agentic AI 업무 비중은 현재 7%에서 2~3년 후 27%로 증가하지만 이는 실제 인력 감축 실적이 아닌 전망이다.
3. 원본 공개 수치는 reported로 보존하며 미공개 수치를 임의로 보간하지 않는다.

## So what (단 하나)
마케팅 운영모델 재설계에서 AI와 사람·외부 파트너의 미래 역할 분담을 함께 시나리오화하자.

## 비즈니스 맥락 → 측정과 판단
- 비즈니스 맥락: CMO Survey 2026: How Agentic AI Will Reshape the Marketing Team
- 지표와 단위: 비중(%), 퍼센트포인트(%p)는 공개 비중의 차이 계산에만 사용.
- 기간: 2026 survey, now vs forecast in 2–3 years; 분모·표본: Survey respondent CMOs, exhibit-specific n not disclosed
- 비교 기준: 동일 범주와 기간, 동일 응답 질문, 또는 전망 구성비 총합.
- 판단: CMO가 예상하는 Agentic AI 업무 비중은 현재 7%에서 2~3년 후 27%로 증가하지만 이는 실제 인력 감축 실적이 아닌 전망이다.
- 인사이트 유형: paired_donut chart, period or composition analysis.

## 시각화 설계와 원본 확인
- x/y: separate now/forecast panels with sector share (%).
- 색·크기: THEME.source/neutral의 설정값, 시계열 점 크기 일관, 파이의 반지름 통일, 트리맵 면적은 데이터 값에서 계산.
- 정렬·강조: 원문에서 확인된 값의 CSV 순서를 유지하고 레이블을 직접 표시.
- 주석·축·제목·범례·여백: config.json의 CONTEXT/THEME를 사용하며 전망 여부·반올림·분모를 표기.
- 원본 대비 확인/차이: Source Exhibit 7 graphic was opened; paired donut is an editorial redesign, not original reproduction. Rounded group shares total 101% and 98%.

## 공개 데이터 출처·시점·계산법
- 공식 URL: https://www.bcg.com/publications/2026/agentic-ai-reshaping-marketing-team
- 게시일 2026-11-20; 검색 수집일 2026-11-23 Asia/Seoul; 데이터 시점 2026 survey, now vs forecast in 2–3 years.
- 표본과 산식: Survey respondent CMOs, exhibit-specific n not disclosed. Raw reported values reside in data.csv; unknown model internals remain undisclosed.
- 도형 면적에 사용하는 보정(BCG)은 발표된 비중 합계가 101%/98%인 데 따른 표시용 정규화만이며 공개 레이블은 변경하지 않는다.

## 재사용 data_recipe
1. 동일 정의와 분모로 데이터를 수집하고 관측/전망의 상태를 표시한다.
2. 각 값의 provenance를 reported, derived, digitized_estimate, missing 중 하나로 분류한다.
3. 단위·기간·표본·합계·반올림·정렬·누락을 확인한다.
4. data.csv 및 config.json의 THEME/CONTEXT만 수정하고 render(data,theme,context)를 호출한다.
5. source/neutral을 200dpi로 재렌더링해 값·레이블·주석을 확인한다.

## 메시지 성립 조건·반례·한계
- 성립: 공통 분모·산식과 기간 구분을 유지하고 원문과 같은 지표를 사용할 때.
- 반례: 전망을 확정 실적처럼 표현, 반복단면 조사를 동일기업 인과효과로 해석, 반올림 101%/98%를 100%로 수치 조작하는 경우.
- 한계: Source Exhibit 7 graphic was opened; paired donut is an editorial redesign, not original reproduction. Rounded group shares total 101% and 98%. 원본 재현 자체 검증과 사용자 검수는 별개이며 human_review=pending.

## 실행 방법
```bash
python chart.py --data data.csv --config config.json --theme source --output source.png --dpi 200
python chart.py --data data.csv --config config.json --theme neutral --output neutral.png --dpi 200
```
