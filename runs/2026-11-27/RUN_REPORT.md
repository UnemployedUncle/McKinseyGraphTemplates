# Consulting Graph Template | 2026-11-27

시작 03:11:27 KST, 로컬 검증 03:16:32, 원격 파일·카탈로그 재확인 03:18:01. 신규 3/3건, Bronze 91 / Silver 0 / Gold 0, 원본 재현 자체검증 신규 1건·누적 24건. 사용자 승인 0건. [Bronze 커밋](https://github.com/UnemployedUncle/McKinseyGraphTemplates/commit/7be09e67362fa96d8192e34108ea42eb84591373).

## 01 Bain — 글로벌 개인 명품 시장 장기 성장 추이
- [공식 원문, 2026-11-18, Snap chart](https://www.bain.com/insights/luxury-holds-its-ground-in-2026-with-new-opportunities-ahead-snap-chart/). 최근 7일 후보 중 신규 원본 정량 차트 확보가 어려워 30일로 확장. 공식 Flourish desktop thumbnail 30871188 직접 확인.
- 공개값 EUR bn: 2005년 139, 2008년 159, 2010년 167, 2015년 245, 2017년 255, 2020년 223, 2023년 369, 2026E 367. 2025→2026E 성장률 원문 2% (현행 환율), 3% (고정 환율). 14개 무표시 막대는 썸네일 기준선과 높이에서 약 ±3bn 판독 추정. 2025 약 358bn에서 성장률을 확정 역산하지 않음. 조사일·추정 모형 미공개.
- 연도별 막대와 국면 주석, 마지막 전망 적색 강조로 장기 성장 경로 및 최근 정체를 동시에 파악. 시장규모·매출 장기 추이 분석에 재사용 가능. 동일 시장 범위·환율 기준이 필요.
- 3회 렌더링, 자체평가 4.29/5 (5/3/5/5/4/4/4), unverified. 원본 미표시 값과 hover, 글꼴·KPI 위치·비율 차이.

## 02 BCG — AI 성장 전략과 업종 대비 성장 성과
- [공식 원문, 2026-11-25, Exhibit 1](https://www.bcg.com/publications/2026/ai-reshaping-corporate-growth-strategy), 원본 이미지 직접 확인.
- 2025년 매출 10억 달러 이상이고 두 기간 중 적어도 한 기간 업종 성장률 초과한 상장사 3,669개. AI 성장 관련 공시 언급 비중: GenAI 이전(2017–22) 3.5%/5.5%, 이후(2023–25) 5.7%/15.5% (2023–25 업종 대비 성장 미달/초과). 이후 격차 9.8%p, 이전 2.0%p. 표본별 세부 n·수집일 미공개.
- 공통 0 기준 y축에 기간별 짝막대, 초과 성장 집단 초록 강조, 직접 값 레이블. 성과 집단별 AI 활용 지표·시점별 벤치마크 재사용. 공시 언급은 실제 활용·인과 효과가 아님.
- 1회 렌더링, 자체평가 4.71/5 (5/5/5/5/5/4/4), verified. 제목 재작성, 글꼴/범례/여백 근사.

## 03 McKinsey — 국가별 생성형 AI 인지도·사용·금융 사용
- [공식 PDF, Exhibit 2, zero-based page 7](https://www.mckinsey.com/~/media/mckinsey/industries/financial%20services/our%20insights/global%20banking%20annual%20review%202026%20part%202/global-banking-annual-review-2026-the-ai-disruption-dividend.pdf). [상위 보고서](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/global-banking-annual-review) 발행 2026-11-17. 최근 7일 경제이동성 후보는 기존 Exhibit 1 관련 중복 및 SVGZ 직접 확인 불가로 30일 확장. PDF 8번째 페이지 스크린샷 실제 확인. 기존 PDF Exhibit 1,3과 다른 그림이며 동일 split_group 유지.
- 2026년 6월 13개국 약 46,000명 설문. 글로벌 금융 사용 23%, 일반 사용 58%, 인지도 92% 공개값. 국가별 39개 점은 스크린샷 425~862px 축 기준 ±2%p 판독 추정. 인도 금융 사용 약 53%, 독일 약 13%는 추정. 원본 순서를 보존하며 근사값의 1%p 역전은 오차 범위. 평균은 재산출하지 않음.
- 국가별 가로 점열과 색상별 연결선, 평균 별도 패널, 공통 0–100 축. 국가·사업부별 인지/활용/업무 적용 단계 분석에 재사용. 집단 비교이지 개인 전환율/인과효과가 아님.
- 3회 렌더링, 자체평가 4.29/5 (5/3/5/5/4/4/4), unverified. 국가값 미표시, 도형 판독·레이블·여백 근사.

## 실제 실행·무결성
- Python 3.13.5, matplotlib 3.10.8, pandas 2.2.3. Source·Neutral PNG 6개 200dpi 실제 생성 및 라운드별 직접 확인. 로컬 단위검사 6/6(값, 순서·단위, 추정 provenance, PNG, 데이터/설정 교체 재사용, ingest 중복·revision·tamper) 통과.
- 현재 원격 medallion.py의 관련 8개 함수 소스 해시가 로컬 실행 코드와 동일함을 확인. 격리 환경에서 ingest/validate/catalog를 실제 수행. 새로 생성된 색인 행을 기존 88개 행에 추가하며 기존 행과 승인 상태 보존. 전체 저장소 로컬 CI는 실행하지 못함(컨테이너 GitHub DNS 제한). 연결 GitHub 도구로 정상 저장.
- ZIP 파일별 SHA256 21/21 및 payload 3/3 재계산 일치. 원격 신규 24개 파일(3개 manifest 포함) 전부 실제 파일 내용과 일치. 원격 index와 JSONL 91행 동일, README 신규 항목 포함. main 기존 HEAD를 부모로 하고 expected_sha, force=false로 업데이트.
- [Actions 45874717532](https://github.com/UnemployedUncle/McKinseyGraphTemplates/actions/runs/45874717532) 조회 당시 in_progress; 최종 결과 미확정.
- ZIP: Consulting_Graph_Template_2026-11-27_PREPARED.zip, 32개 파일, 908919 bytes, SHA256 e827ff6c7cb4e8b7077686b3b13a7eda762d34658417959bd51a11f369c88184. 기존 사용자 Library에 저장 성공. 생성 이미지 및 로그는 ZIP의 artifacts/에 포함. 원본 이미지/로고/폰트 저장 안 함.
- 전 회사 완료. 원본 충실도 자체검증 통과는 BCG 1건만. 사용자 검수는 전부 pending, training_eligible=false. Silver/Gold 승격 없음. 당일 전달은 저장된 준비본과 CI 상태를 조회하여 새 조사·중복 커밋 없이 진행.
