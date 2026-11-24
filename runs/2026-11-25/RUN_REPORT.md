# Consulting Graph Template — 2026-11-25

시작 03:15:03 KST, 로컬 및 원격 파일 확인 03:22:47 KST. 3/3건 신규 Bronze, 누적 85/0/0, 원본 재현 자체검증 21건(신규 3건). 모두 pending, 학습 승인 없음. 정확한 코드는 신규 Bronze 커밋 cf95a489f30cf5f64c54a5fbc694a2a5ec5b9e39 기준이다.

## Bain — AI 검색 가시성과 시장점유율
공식 원문: https://www.bain.com/insights/ai-is-the-new-search-heres-how-retailers-win-the-answer/ (11월 21일). Figure 1의 Overall 탭의 실제 원본 썸네일을 확인했다. 4개 업종, 업종별 5개 기업, 40개 공개 수치의 가로 짝막대를 유지했다. Lowe's 26% vs 9%, Amazon 전자제품 12% vs 25%는 AI 검색 가시성과 시장점유율의 차이를 보여준다. 4,400+ 프롬프트/300,000+ 실행, 2026년 10월 서비스 월간 사용자 가중치, 실제 수집일 미공개. 분모와 프롬프트 구성이 달라 매출 인과효과는 아님. 동일한 분류 내 벤치마킹과 지표별 격차 분석에 재사용 가능. 자체평가 4.71/5, 정적 Overall 화면 한정, 제목·각주·비율 근사, 탭과 hover 미구현.

## BCG — 일본 Physical AI 기술적 가치 상한
공식 원문: https://www.bcg.com/publications/2026/physical-ai-japan-value-opportunity (11월 24일), Methodology sidebar exhibit 실제 이미지 확인. Restricted 27+10=37, Medium 142+78=220, Maximum 296+154=450 (USD billion/year); FY2025 GDP 대비 각각 0.8%, 4.9%, 10.0%. 2040년 기술 상한 시나리오, 실현 매출 전망 아님. 20개 산업, 232개 직종, 약 7,500개 작업, 환율 2025년 평균 150엔/USD. 비용 절감과 신규 가치의 구성 차이를 누적 막대와 GDP 주석으로 설명. 기술 성숙도별 투자 상한 분석에 재사용 가능. 자체평가 4.57/5, 괄호를 범례로 변경, 작은 구간 라벨 오프셋 및 글꼴 차이.

## McKinsey — 은행 Agentic AI 가치 도달 기간
공식 PDF: https://www.mckinsey.com/~/media/mckinsey/industries/financial%20services/our%20insights/global%20banking%20annual%20review%202026%20part%202/global-banking-annual-review-2026-the-ai-disruption-dividend.pdf (Exhibit 1, PDF page index 2), 공식 상위 보고서 11월 17일, PDF 표지는 2026년 11월. 7일 후보에서 원본 정량 도형 직접 확인이 불가능하거나 개념도여서 30일 범위로 확장했다. PDF 스크린샷 확인. 구축+램프업 기간: Operations 6+6=12, Risk 6+10=16, Knowledge 5+3=8, Software 9+9=18, Other 8+4=12개월; 보고된 평균 7+6=13개월. 도메인별 표본 33/7/4/4/4, 52개 사례(2026년 9~10월 인터뷰). 약 10개월 투자회수(구축비 회수에 필요한 정상 가동 효과 개월 수)와 3년 ROI 약 2.9배는 별도 KPI. 집계 가중치 및 사례별 현금흐름은 미공개. 구축/램프업/회수 단계를 분리하여 사업계획 분석에 재사용 가능. 자체평가 4.71/5, 제목과 각주·글꼴·여백 근사.

## 실행과 저장
- Python 3.13.5, matplotlib 3.10.8. Source/Neutral 6개 PNG 200dpi 실제 렌더링·최종 시각 확인, 재사용 변경 데이터 테스트 포함 6/6.
- 저장소의 현재 스크립트와 테스트를 읽어 12/12 로컬 단위 테스트 통과(격리된 테스트 fixture). medallion.py ingest/validate로 오늘 3개 manifest 및 새 색인 행 생성. 기존 82개 색인과 합쳐 85개 행 일치 확인. 전체 기존 묶음의 로컬 재검사는 하지 않음.
- 로컬 ZIP 21개 payload 파일 SHA256 및 3개 payload SHA256 실제 재계산. Git 원격 24개 파일(21 payload + 3 manifest)을 재조회해 정확한 문자열 일치 확인. 기존 Silver/Gold 변경 없음.
- ZIP: Consulting_Graph_Template_2026-11-25_PREPARED.zip, SHA256 50f09c3c5b99b0b9f225871e92b444fe3240ccb42a58b98109a1d65a35cb433b, 33개 파일(코드/데이터/설정/분석/검증/manifest 24개 및 PNG 6개, 로그 2개, contact sheet).
- Actions: https://github.com/UnemployedUncle/McKinseyGraphTemplates/actions/runs/45458777060, 기록 당시 in_progress/pending. 실행 성공과 원본 검증, 사용자 검수는 별개.
- 정확한 버전은 GitHub Bronze. 모든 신규 파일 human_review pending, training_eligible false. 원본 이미지·로고·폰트 미저장. 모델 학습 미수행. 오전 전달 전 준비본 조회, 중복 적재 금지.
