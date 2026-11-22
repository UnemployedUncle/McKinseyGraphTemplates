# Consulting Graph Template — 2026-11-23 사전 준비 결과

- 시작: 2026-11-23 03:15:47 KST
- 완료: 2026-11-23T03:32:12.483+09:00
- 신규 목표/완료: **3/3** (Bain·BCG·McKinsey 회사별 1건).
- 누적: **Bronze 79 / Silver 0 / Gold 0**.
- 원본 재현 자체검증 누적 18건(신규 Bain 1건), 인간 검수 승인 신규 0건.
- 준비 `prepared_complete=true`; 전달 `delivered=false`.
- 코드 커밋: [9ac94805536dfbb0c2c3f27f4e20fa1fddae0845](https://github.com/UnemployedUncle/McKinseyGraphTemplates/commit/9ac94805536dfbb0c2c3f27f4e20fa1fddae0845)
- 신규 Bronze: [2026-11-23](https://github.com/UnemployedUncle/McKinseyGraphTemplates/tree/main/bronze/2026-11-23)

## 1. Bain — AI 사업성과 입증 기업의 추이

- [공식 원문](https://www.bain.com/insights/survey-workflow-redesign-is-key-to-ai-success/) (2026-11-18 발행), Figure 1.
- 조사 시점: 2024 Q4 / 2025 Q3 / 2026 Q1 / 2026 Q3; 표본 n=199/197/200/200.
- 공개값: 정량적 매출·비용 성과를 확보한 응답 기업의 비중 **18%, 23%, 30%, 33%**.
- **So what:** AI 도입 건수가 아닌 정량 사업성과를 확보한 기업 비중을 추적한다.
- 방법: X=조사 시점, Y=응답 비율(%), 직접 값 레이블이 있는 선그래프; 0에서 시작하는 세로축과 조사 차수의 표본 주석.
- 검증: 원본 Flourish Figure 1 이미지 확인, 자체 4.71/5 (역사적 자동 평가; 소유자 승인 아님). 표본이 다르고 원인 추정 불가.
- 파일: `bronze/2026-11-23/bain_ai_results_survey_fig1/`.

## 2. BCG — Agentic AI와 마케팅 팀의 업무 믹스

- [공식 원문](https://www.bcg.com/publications/2026/agentic-ai-reshaping-marketing-team) (2026-11-20 발행), **Exhibit 7**. 동일 기사 Exhibit 2는 과거 다른 Bronze로 저장되었으나 이번 차트는 다른 그림.
- CMO 설문 현재→2~3년 전망: Full-timers **57→48%**, Agency **25→16%**, Freelance **8→5%**, Agentic AI **7→27%**, Other **4→2%**.
- **So what:** 미래 인력 계획에서는 AI와 사람·대행사 업무 분담을 함께 시나리오화한다.
- 방법: 동일 크기의 두 원형 도형으로 현재/전망을 비교하고 직접 레이블; 발표값 합계 현재 **101%**, 전망 **98%**는 반올림으로 표기하고 도형만 정규화.
- 검증: 공식 Exhibit 이미지를 열어 확인했지만 원본 segmented radial 유형에서 editorial paired donut으로 재설계. **unverified / fidelity null**, 원본 복제로 간주하지 않음. 조사 예상이지 실제 인력 감축 아님.
- 파일: `bronze/2026-11-23/bcg_cmo_agentic_team_mix_ex7/`.

## 3. McKinsey — Physical AI 가치사슬의 미래 가치풀

- [공식 원문](https://www.mckinsey.com/industries/industrials/our-insights/physical-ai-is-breaking-out-of-the-box) (2026-11-20 발행), **Exhibit 3** 관련 모델 데이터.
- 2035년 전망모형의 구성요소 중간값: Hardware **35%**, Software **30%**, Deployment **12.5%**, Field operations **22.5%**; 합계 100%.
- **So what:** 하드웨어 외에도 배포와 현장 운영 가치풀을 분리하여 분석한다.
- 방법: 면적이 중간값 비중을 반영하는 editorial treemap; 원본 모형 전망이지 관측된 거래액·시장 매출이 아님.
- 검증: 원본의 수치 설명과 각주만 확인, 원본 차트 파일은 시각 확인 불가. **unverified / fidelity null**, 원본 복제 통과 주장 금지.
- 파일: `bronze/2026-11-23/mckinsey_physical_ai_value_chain_ex3/`.

## 실제 검증과 한계

- 로컬 Python 3.13.5 / matplotlib 3.10.8: unit tests **5/5 통과**, 로컬 medallion validate 통과.
- 로컬에서 Source/Neutral **6장(200dpi)** 생성 및 육안 확인.
- **GitHub 원격 신규 파일 21/21 SHA256, payload_sha256 3/3** 직접 재계산 일치; `human_review=pending` 유지.
- 다운로드 Preview ZIP의 로컬 코드/설정과 GitHub Bronze의 **바이트 일치를 보장하지 않음**. exact renderer를 GitHub 커밋으로부터 독립 재실행하지 못했으므로 원격 정확 코드 렌더링은 미확인. 검수 시 GitHub 원본과 manifest만 기준.
- GitHub Actions의 Push 실행 결과는 현재 조회 기능에서 확인되지 않았으며 **성공이라고 표시하지 않음**.
- 신규 Bronze 불변 버전은 GitHub main 카탈로그 및 `dataset/bronze.jsonl`로 색인됨. Silver/Gold 변경 없음.
- 원본 기업 로고·이미지·폰트·원문 전문·자격증명 비공개 자료는 Git에 포함하지 않음.

## 오전 전달 참고

이 보고서와 `prepared.json` 및 Bronze manifest가 당일 07:15 전달의 조회 기준이다. 동일 날짜 신규 조사, 중복 커밋, 임의 승인·승격, 새 예약을 생성하지 않는다. 사용자 학습 완료나 전달 완료로 기록하지 않는다.
