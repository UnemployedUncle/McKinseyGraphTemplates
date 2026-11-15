# Consulting Graph Template — 2026년 11월 16일 사전 준비

한국시간 03:10:30 시작 / 03:29 준비 확정. 목표 3건 중 BCG·McKinsey 2건 신규 Bronze 누적. 기존 자료 덮어쓰기 없음.

**카탈로그 Bronze 62건 / Silver 0건 / Gold 0건, 기존 원본 재현 자체검증 통과 15건. 오늘 신규 통과 0건.**

두 신규 파일 모두 validation_status=unverified, fidelity_score=null, human_review=pending, training_eligible=false.

## BCG — 업종별 상위 시가총액 기업 교체율(Exhibit 1)

- 원문: https://www.bcg.com/publications/2026/market-leaders-staying-on-top-longer
- 공식 게시일 2026-11-06 (최근 30일로 검색 확장). 조사 기간은 1990–2004년 vs 2005–2025년.
- 시장가치 가중 giant churn의 전체 업종 중앙값 24%에서 13%로 하락. 업종별 변화는 다르므로 업종별 추세 확인 필요.
- 공식 499픽셀 축소 원본을 실제 열어 산점도 15개 업종 좌표를 추정해 digitized_estimate와 ±3%p 불확실성 표기. 전체 중앙값 24/13은 원문 reported이며 CSV 업종 좌표와 분리.
- x=과거 giant churn (%), y=최근 giant churn (%), y=x 동등선과 개별 업종 직접 라벨. S&P Capital IQ 상장기업 상위 2,000개 데이터 기반.
- 원본 색상 영역 및 주석 간소화, 좌표 정밀도 보증 없음: unverified.
- 재사용: 업종·거래처별 상위 플레이어 교체율, 경쟁구조 고착화 분석.
- Bronze: https://github.com/UnemployedUncle/McKinseyGraphTemplates/tree/main/bronze/2026-11-16/bcg_corporate_giant_churn_ex1_scatter_estimate

## McKinsey — 미국 상용 로보택시 서비스 도시 확대(Exhibit 1)

- 원문: https://www.mckinsey.com/featured-insights/charts/autonomous-mobility-gains-ground
- 공식 게시일 2026-11-12. 관측 2024년 12월 3, 2025년 12월 6, 2026년 9월 15도시 / 전망 2026년 12월 20, 2027년 12월 약 40도시.
- 출처: 기업 홈페이지·보도 검색·McKinsey Center for Future Mobility. 안전요원 동승 서비스를 포함한 상용 서비스 도시 수.
- 시각화: 시간별 milestone line; 관측 실선, 전망 점선, 0부터 시작하는 동일 축, 수치 직접 라벨.
- SVGZ 원본 접근 실패, 웹 공식 이미지 대체 텍스트로 수치만 확인. 편집형으로 unverified.
- 재사용: AI 서비스 확산, 지역별 점포/제품 출시, 투자 마일스톤의 실제/목표 분리.
- Bronze: https://github.com/UnemployedUncle/McKinseyGraphTemplates/tree/main/bronze/2026-11-16/mckinsey_us_robotaxi_cities_ex1_timeline

## 검증·Bain 제외·전달 상태

- 로컬 Python 3.13.5, matplotlib 3.10.8: Source/Neutral 4개를 200dpi (2200×1240px) 렌더링하고 직접 확인. 별도 Python 5개 테스트 통과.
- GitHub Actions: https://github.com/UnemployedUncle/McKinseyGraphTemplates/actions/runs/43746553302 (completed/success). 단위 테스트, scripts/medallion.py validate, render_all.py, 아티팩트 업로드 모두 성공. 아티팩트 ID 14174566744.
- Bronze 코드 커밋: https://github.com/UnemployedUncle/McKinseyGraphTemplates/commit/223a8fd8c65236108cee8557f67f493f6f472999
- 다운로드 패키지 Consulting_Graph_Template_2026-11-16_PREVIEWS_AND_CODE.zip: 원격 manifest와 SHA256이 일치하는 chart.py/data.csv/config.json/requirements.txt와 4개 PNG. card.md/record.json/validation.json/manifest.json의 canonical 원본은 GitHub 링크 참고.
- Bain: 최근 7일 우선, 30일 확장 조사에서 공식 게시일·정량 도표 직접 접근·카탈로그 비중복 조건을 모두 확인할 새 자료를 확보하지 못해 제외.
- 준비본 상태 prepared_complete=true / delivered=false. 오전 07:15에는 본 자료만 조회, 재조사·중복 커밋 금지.
- Silver/Gold 승격·사용자 승인 대리 처리·외부 모델 재학습·새 예약 생성 없음.
