# Consulting Graph Template | 2026-11-26

시작 03:15:03 KST, 로컬 검증 03:19:59, 원격 파일 및 색인 확인 03:24:27. 신규 3/3, Bronze 88 / Silver 0 / Gold 0, 원본 자체검증 신규 2·누적 23. 사용자 승인 신규 0. 코드 커밋: 69819ce419ebff167018aa1b4cf1a01a78d952d6.

## 01 Bain — AI 식료품 검색 인용 출처 구성
- [공식 원문, 2026-11-21, Figure 2](https://www.bain.com/insights/ai-is-the-new-search-heres-how-retailers-win-the-answer/). 어제 Figure 1과 다른 차트다. 실제 Flourish 썸네일 확인.
- ChatGPT, Google AI, Google Gemini, Claude의 earned media 인용 비중은 30%, 24%, 46%, 58%. Google AI의 social 29%, search 25%. 플랫폼별 전체 인용 발생을 분모로 비교한다. 20개 표시 공개값, 12개 미표시 구간은 412px 100% 축과 경계 판독에서 약 ±1%p 추정. 합계는 도형만 정규화하며 0 추정도 확정 0이 아니다.
- 100% 누적 세로 막대의 동일 색/축/순서로 플랫폼별 출처 구성을 비교. AI 검색 콘텐츠 전략을 출처 유형별로 분리하는 데 재사용. 클릭·매출·전환율은 아니다. 조사일과 상세 표본 미공개.
- 3회 실제 렌더링, 점수 4.43/5 (5/3/5/5/5/4/4), unverified. 원본과 레이블·범례·비율 차이 및 hover 미구현.

## 02 BCG — IMS 구축 방식 및 규모별 단위비용
- [공식 원문, 2026-11-25, Exhibit 4](https://www.bcg.com/publications/2026/telco-core-network-as-a-service), 실제 원본 이미지 확인.
- 기존 IMS 100만 가입자 기준 100의 연간화 5년 TCO/가입자 지수. 100만은 traditional/cloud-native/IMSaaS 100/40/20, 200만 70/30/20, 500만 45/20/18. IMSaaS의 cloud-native 대비 절감률은 50%, 33%, 10%로 규모 확대 시 줄어든다. 사례 분석이며 실제 통화 비용이나 표본수, 세부 가정 미공개.
- 그룹 막대에 공통 비용 축 및 데이터로 계산한 절감률 괄호를 결합. 규모별 자체 구축 대 구매, Agent 서비스 단위비용과 운영비 분석에 재사용. 동일 품질과 비용 범위가 성립 조건.
- 2회 렌더링, 점수 4.71/5 (5/5/5/5/5/4/4), verified. 글꼴, 제목, 부제, 여백 차이.

## 03 McKinsey — 업무별 AI와 사람의 지원 선호
- [공식 PDF, Exhibit 3, zero-based page 8](https://www.mckinsey.com/~/media/mckinsey/industries/financial%20services/our%20insights/global%20banking%20annual%20review%202026%20part%202/global-banking-annual-review-2026-the-ai-disruption-dividend.pdf); 상위 보고서 2026-11-17, PDF 표지 11월. 최근 7일 내 적격 신규 원본 확보가 어려워 30일로 확장. 어제 Exhibit 1과 다르다. PDF 페이지 스크린샷 직접 확인.
- 2026년 6월 13개국 약 46,000명 소비자 설문. 기본 금융질문 AI/둘 다/사람 59/26/15%, 투자 조언 24/42/34%. 복잡한 조언에서 인간 또는 혼합 지원을 더 선호한다.
- 양단 구성비 막대와 범주별 리본. 업무별 AI·인간 역할과 검수 수준 설계에 재사용. 리본은 개인별 전환량이 아니며 실제 행동이나 성과도 아니다. 문항별 유효수 및 가중치 미공개.
- 2회 렌더링, 점수 4.57/5 (5/5/5/5/4/4/4), verified. 리본 곡률과 너비, 설명 위치, 글꼴 차이.

## 실제 검증 및 저장
- Python 3.13.5 / matplotlib 3.10.8 / numpy 2.3.5. source/neutral PNG 6개(200dpi) 직접 확인. 로컬 단위 테스트 6/6 (ingest revision·tamper, PNG, 재사용, 절감률, 합계, 값). 원격 스크립트의 ingest/validate/catalog 관련 정확한 함수들을 격리 환경에서 실행하고 새 색인 행을 생성했으며 기존 85행과 보존 병합. 전체 저장소 단위 테스트를 로컬에서 수행한 것으로 주장하지 않는다.
- manifest SHA256 21개 파일 및 payload 3개 검증. 원격 24개 파일(base64 원문 및 Git blob SHA)과 로컬 동일. index/bronze.jsonl 88행 동일, README 반영 확인. main 비강제 업데이트. Silver/Gold 기존 상태 유지.
- [Actions 45674771511](https://github.com/UnemployedUncle/McKinseyGraphTemplates/actions/runs/45674771511) 확인 시 in_progress, 완료 성공 미확정.
- ZIP: Consulting_Graph_Template_2026-11-26_PREPARED.zip, 33개 파일, 962110 bytes, SHA256 e7db3c424bee478d8184e0724c7e043e5f34cdc4685059399ba1f5f679cd41e8. 사용자 Library에 보존·목록 재확인. 생성 PNG는 패키지 외에 CI 아티팩트 생성 예정이며 원본 이미지·로고·폰트 파일은 Git/ZIP에 포함하지 않았다.
- 전 회사 완료, Bain 원본 자체검증 미통과는 정확히 구분. human_review=pending, training_eligible=false. 새 조사/중복 커밋 없이 당일 준비본을 전달할 것.
