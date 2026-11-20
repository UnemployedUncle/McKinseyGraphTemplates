# Consulting Graph Template — 2026-11-21 (Asia/Seoul)

## 상태
- 준비 시작: 2026-11-21 03:10 KST (실제 최초 repo 조회); 준비 완료: GitHub 커밋 및 원격 재검증 후 확정
- 목표 3건 / 신규 2건: BCG 1, McKinsey 1, Bain 0
- Bronze 73 / Silver 0 / Gold 0; 신규 원본 재현 자체검증 통과 0, 기존 누적 자체검증 16
- 두 신규 템플릿: human_review=pending, validation_status=unverified, fidelity_score=null, training_eligible=false

## BCG — Agentic AI 투자와 명확한 비전
- 공개일: **2026-11-20**. 원문: https://www.bcg.com/publications/2026/agentic-ai-reshaping-marketing-team
- Figure: Exhibit 2. 수집일: **2026-11-21**. 조사 기간: **2026년 5~7월**. 약 60명의 CMO 관련 설문(MMA Global/BCG); 정확한 분모 그룹별 수는 비공개
- 원문 3문장 요약: 에이전틱 AI가 마케팅 조직 구조를 바꾸는 과정에서 거버넌스와 실험 투자가 필요하다. 명확한 AI 비전의 유무에 따라 투자 예산의 충분성 응답 분포가 다르다. 비전이 명확한 그룹은 투자 자원이 충분하거나 초과한다고 응답한 비중이 더 높다.
- 공개값: 명확한 비전 그룹 Have what I need 54%, Have more than I need 8%, Need a lot more 38%. 명확하지 않은 그룹 Have what I need 37%, Need a little more 33%, Need a lot more 30%. 각각 합계 100%. 두 집단에서 **응답 범주가 동일하지 않음**을 원형 라벨에 그대로 반영
- So what: 전략·비전 정렬과 AI 실행 재원 확보의 연관성은 보이지만 인과효과를 주장하지 않는다.
- 차트: 원본 2행×3 범주 미니 가로바를 matplotlib로 유사 구조로 표시; data.csv의 group,category,value_pct,sequence; 시각적 원본 참조 확인. 세부 색·공백·크기 재현 완전 일치는 입증하지 못해 unverified/fidelity null
- 재사용: 그룹별 설문 분포. 그룹마다 다른 응답 범주를 합치지 말고 원래 라벨과 분모를 유지하며 총합과 값별 provenance 확인
- 링크: [Bronze](../../bronze/2026-11-21/bcg_ai_vision_funding_ex2/)

## McKinsey — AI 자동화 채택 근로시간 중 대체 예상 비중
- 공개일: **2026-11-20**. 원문: https://www.mckinsey.com/institute-for-economic-mobility/our-insights/advancing-us-economic-mobility-in-the-age-of-ai
- Figure: Exhibit 1 관련 기사 공개 수치. 수집일: **2026-11-21**. 데이터/모델: 현재 미국 직업 분포와 2035년까지 자동화 채택 추정 시나리오; BLS/ACS 및 MGI 모델
- 원문 3문장 요약: AI 채택과 과업 대체·증강은 노동집단에 비대칭적으로 영향을 줄 수 있다. 모델은 자동화가 채택된 시간 중 대체될 수 있는 시간의 비중을 비교한다. 기술 채택률·직업구성·정책 대응에 따라 결과가 달라질 수 있다.
- 공개값: Latino 41%, Black 40%, White 37%, Asian 36%. **전체 근로시간의 41% 대체가 아니고 직업/일자리의 41% 상실도 아님.** 분모는 *automation-adopted work hours* 중 각 집단 수행시간; 수치는 추정 전망이지 현재 관측이 아님
- So what: 노동집단별 전환 지원·재교육 자원을 배분할 때 자동화 채택에 따른 잠재 업무 대체 위험을 동일 분모로 비교한다.
- 차트: 원문 원본 SVGZ 접근 불가로 실제 원본을 보지 못한 **편집형 ranked horizontal bar**. 값·순서·라벨·단위를 재사용하도록 data.csv/config.json 분리. 원본 재현 검증 불가로 unverified/fidelity null
- 재사용: 동일한 분모·시점의 집단별 시나리오 위험 비교; 회귀계수·신뢰구간·표본수 비공개, 다른 자동화 시나리오에서는 재검증 필요
- 링크: [Bronze](../../bronze/2026-11-21/mckinsey_automation_displacement_ex1_editorial/)

## Bain — 오늘 제외
- 공식 사이트 최근 7일을 먼저 조사하고 30일까지 확장했으나 공식 발행일·직접 접근 가능한 원본 정량 차트·기존 카탈로그 비중복을 함께 증명한 후보는 확보하지 못함. 제3자 호스팅 PDF 및 단독 보도자료를 신규 원본 차트로 간주하지 않음

## 실행/검수와 사용자 승인
- Python 단위 의미검사 3/3 성공: 동일 파일 SHA256/manifest payload 무결성, 설문 그룹합 100%, 자동화 비중과 정렬, 생성 이미지 크기 2200x1240
- Python matplotlib source/neutral 각 2개 총 4개를 200 dpi 렌더하고 모두 직접 확인; 초기 BCG row label 겹침을 수정해 실제 재실행 (BCG 2회, McKinsey 1회)
- 이미지와 실행 로그는 사용자 ZIP/artifacts에만 보관하고 원본 이미지/로고/폰트는 Git에 포함하지 않음
- 코드 실행 성공과 원본 재현 검증, 사용자 검수는 서로 별개. Silver/Gold 승격이나 인간 승인 대리 실행 없음, 모델 재학습 없음
- GitHub Actions의 성공은 별도 실제 실행 조회로 확인될 때에만 표시

## 원격 파일
- [2026-11-21 Bronze](../../bronze/2026-11-21/)
- [전체 카탈로그](../../catalog/README.md)
