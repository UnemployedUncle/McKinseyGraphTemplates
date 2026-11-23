# Consulting Graph Template — 2026-11-24 사전 준비

- 시작: 2026-11-24 03:14:09 Asia/Seoul; Git 저장 단계 완료: 2026-11-24 03:32 KST 이후.
- 당일 목표 3건 / 작성 3건 (Bain, BCG, McKinsey 회사별 1).
- Bronze 누적 **82**, Silver 0, Gold 0. 원본 재현 **자체 검증 통과 누적 18건**, 신규 0건 (새 차트 3개 `unverified`). 사용자 승인 0건.
- 저장 계층 Bronze / human_review=pending / training_eligible=false.
- 원본 링크 및 그림은 아래, 다운로드 미리보기의 원본 보고서 이미지·브랜드 자산은 포함하지 않음.

## 1. Bain — AI 인력 영향은 직무별로 엇갈린다

- 출처: [Bain 2026-11-18](https://www.bain.com/insights/survey-workflow-redesign-is-key-to-ai-success/), **Figure 3** (지난날 저장한 동일 기사 Figure 1과 중복되지 않음).
- 수집·분석일: 2026-11-24. 조사 시점: **2026 Q1 및 Q3**. 서로 다른 설문 파동의 기대 인원증감(%)이며 실현된 고용량 변화가 아님.
- 원본 Flourish Figure 3을 직접 열어 총 11개 직무의 slope/micro-line 시각 구조와 수치를 확인.
- 주요 수치: Software development -2%→+10%; Sales operations +1→+6%; Customer onboarding -6→+2%; Finance -9→-3%; Customer service -19→-13%; Marketing +1→-3%. 나머지 전체 값은 data.csv.
- **So what:** AI의 조직 영향은 전체 평균 고용감축률이 아니라 **직무별 전망의 방향 및 변화량**으로 계획해야 한다.
- 시각화: 3개 그룹 아래 5/4/2 미니 slope 차트, X=Q1/Q3, Y=% 전망, 직접 레이블, 고정 축.
- 재사용: 같은 2개 파동·여러 직무의 기대값을 대조하는 workforce planning, 부서별 채용계획, agent 업무 전환 전망.
- 한계: 각 직무별 표본·오차범위는 미공개; 종단 동일 응답기업 조사 아님; AI 도입의 고용 인과효과 주장 불가.
- `validation_status=unverified`, `fidelity_score=null` (원본 직접 확인했지만 7개 충실도 기준 4.5 이상 확정하지 않음).

## 2. BCG — 제조업 생산 이전 위험은 서유럽에 집중

- 출처: [BCG 2026-11-23](https://www.bcg.com/publications/2026/ai-automation-reshape-manufacturing), **Exhibit 1**.
- 2025년 제조 부가가치(MVA, USD bn)를 **현재 경쟁력 조건으로 즉시 재배치하는 모형 시나리오**. 이것을 실제 생산 이전 및 미래 특정연도 전망으로 취급하지 않음.
- 미국: 기준 **2,514**, 위험 **460**, 잔존 **2,054** (고용 24m 중 5m 위험).
- 서유럽: 기준 **2,595**, 위험 **991**, 잔존 **1,604** (고용 42m 중 15m 위험).
- 일본: 기준 **993**, 위험 **314**, 잔존 **679** (고용 18m 중 6m 위험).
- MVA 위험합 1,765bn≈1.8tn, 고용 위험합 26m. 공개값은 `reported`, 잔존액·비율 및 합계는 `derived` 계산.
- **So what:** 제조업 경쟁력 투자는 전체 평균보다 지역별 가치와 고용 이전에 노출된 영역을 먼저 평가해야 한다.
- 시각화: 3개 지역 패널; 기준 및 재배치 후 녹색 막대, 위험액을 주황색 floating bar로 표시; 하단 일자리 콜아웃.
- 재사용: 지역별 경쟁력 손실, 물류 비용 리스크, 생산기지 이전 시나리오, 규제 노출 손익.
- 한계: 조사 기반 모델과 재배치 가정에 민감, 실제 고용 감소나 공장 이전 실적 아님.
- 원본 그래프 열어 확인; 충실도 7축 검증 미완료로 `unverified`, 점수 null.

## 3. McKinsey — AI 사용에서 역할 재설계까지 성숙도 격차

- 출처: [McKinsey 2026-11-23](https://www.mckinsey.com/capabilities/quantumblack/our-insights/rewiring-gcc-countries-for-ai-realizing-value-in-government), **Exhibit 2**.
- 설문기간: **2026-08-11~2026-10-12**, GCC 고위리더 n=135 중 불완전 14명·불일치 1명을 제외한 **n=120**.
- 단계별 응답 비중: Early 12%, Scaled use 7%, Workflow redesign 65%, Role redesign 16%. 합계=100%, 동일 분모를 갖는 상호배타 범주.
- **So what:** Agent 활용 여부가 아니라 **업무흐름과 사람의 역할을 실제로 재설계했는지**를 별도 KPI로 관리해야 한다.
- 시각화: 단일 100% 가로 누적 막대, 단계별 색과 직접 레이블, 0–100% 축.
- 재사용: AI 성숙도, 프로세스 혁신 수준, 조직별 Agent 도입 성과 진단.
- 한계: 응답 자체보고와 비대표 표본. 원본 Exhibit의 SVGZ를 시각적으로 열 수 없고 alt description/공개 정량값만 확인; 원본 충실도 `unverified`·점수 null.

## 산출물 및 검증

각 경로 `bronze/2026-11-24/{firm}_{slug}_{figure}/`는 `chart.py`, `data.csv`, `config.json`, `requirements.txt`, `card.md`, `record.json`, `validation.json`, `manifest.json`을 포함한다.

- 템플릿 `render(data, theme, context)->fig`; Source/Neutral config와 CSV 수치만 바꿔 재사용.
- 로컬 Python 3.13.5, matplotlib 3.10.8로 **3 × 2 = PNG 6개**를 200dpi 실제 생성·확인, 기초 단위/산술·축·분모 검사 통과. 동일 `chart.py`, `data.csv`, `config.json`의 원격 SHA256이 로컬 렌더 입력과 일치한다.
- 정확한 검수 파일 버전은 GitHub manifest의 `files` 및 `payload_sha256` 기준. 보조 미리보기 ZIP의 card/record/validation/manifest는 별도 초안이며 원격 SHA 바이트 일치를 주장하지 않는다. PNG 자체는 GitHub에 커밋하지 않음.
- 파일 SHA256과 payload SHA256을 실제 GitHub UTF-8 파일별로 재계산하여 새 manifest 생성; 카탈로그 `catalog/index.json`, `catalog/README.md`, `dataset/bronze.jsonl`을 갱신했다.
- 새 레코드는 `human_review=pending`이며 Silver/Gold 변경 및 승인 대리 실행·모델 재학습·외부 업로드 없음. `training_pair`는 미승인 학습 후보일 뿐.
- 저장 단계에는 **작업 브랜치에서 원본 main HEAD의 내용을 보존하며 파일별 커밋을 순차 생성**하는 경로를 사용했고, GitHub main으로 fast-forward 전파한다. 단일 atomic tree 커밋 방식은 연결 도구에 base tree SHA 조회가 없어 사용하지 않음.
- GitHub Actions는 push 이후 상태를 별도 확인해야 하며, 워크플로 등록만으로 성공을 주장하지 않는다.

## 다음 전달

2026-11-24 07:15에는 이 보고서와 `prepared.json`을 GitHub main에서 먼저 읽는다. 이미 준비된 자료만 한 번 전달하고 신규 자료 조사·중복 커밋·Silver/Gold 승인 대행을 수행하지 않는다.
