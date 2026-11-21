# Consulting Graph Template — 2026-11-22 (Asia/Seoul)

**준비 시작:** 2026-11-22 03:11:47 +09:00 · **준비 완료:** 2026-11-22T03:23:45.102+09:00

## 준비 결과

- 완료 **3/3건** (Bain 1, BCG 1, McKinsey 1)
- GitHub 누적 **Bronze 76 / Silver 0 / Gold 0**
- 원본 재현 자체검증 누적 **17건** (이전 16, 이번 Bain +1), 신규 원본 미검증 **2건**
- 신규 사용자 검수 **0건**, `human_review=pending`, `training_eligible=false`
- Bronze 코드/데이터/설정/문서 21개 파일과 manifest 3개 원격 재조회 후 SHA256 파일별 21/21, payload 3/3 일치
- Python 3.13.5 / matplotlib 3.10.8 / numpy 2.3.5; 의미·무결성 테스트 5/5, Source·Neutral 6개 PNG 200dpi(2200×1240) 실제 생성 및 육안 검토

## 01 Bain — LNG 거래이익의 급격한 하방 위험

- **출처:** https://www.bain.com/insights/lng-glut-how-to-win-when-trading-gets-crowded/
- **발행일:** 2026-11-18. **원본:** Figure 2 직접 열어 확인. **기간:** 2017–19, 2020, 2022–23, 2026E, 2030–34F.
- **So what:** 2030–34F 총 거래이익 약 5.5 US$bn/yr와 미국 LNG 취소 수수료 약 5.8 US$bn/yr를 단순 차감하면 약 −0.3 US$bn/yr이다. 이는 조건부 모형 전망이며 실적이 아니다.
- **표현:** 회색 양의 gross-profit bars, 빨강 음의 취소비용 bars, 검정 net dots(두 값 모두 공개된 시점에 한정). 시점별 순서 유지, 0 기준선과 음의 전망 주석.
- **재사용:** 구매계약·운임·규제비용을 포함한 업계별 gross-to-net profit bridge. `period`, `gross_usd_bn`, `cancellation_loss_usd_bn`, `net_usd_bn`, `status`, `provenance`를 수정.
- **한계:** 취소수수료 미공개 연도는 `missing`이지 0이 아님. gross 이익은 모든 비용을 반영한 순이익이 아님. 공개값 반올림과 시나리오 편차.
- **원본 재현 자체점수:** 4.71/5 (유형/수치·순서/축/색·강조/라벨·주석/범례/여백 7요소 평가). 사용자 승인과 별개.
- **Bronze:** [파일](../../bronze/2026-11-22/bain_lng_trading_profit_fig2/) · payload 229ea8d4e96ba8493cdae2fcf12e987ba50204bf0ddb366c791aa884f800bcb2

## 02 BCG — Agentic AI가 CPU 인프라 용량에 기여하는 구조

- **출처:** https://www.bcg.com/publications/2026/ai-data-center-supply-demand-outlook
- **발행일:** 2026-11-20. **원본:** 슬라이드쇼 4/9 시각 열람. **데이터 기준:** BCG 2026-09 모형, 2025–2031 전망.
- **So what:** 2031년 총 CPU 용량 전망 53GW는 2025 기준 설치용량 약 28GW, 전통적 수요 증가 약 12GW, AI 추가 증가 약 13GW로 분해된다.
- **표현:** 세 시리즈 누적 막대, 연도순 정렬, 각 막대 상단 total GW 레이블, 출처·전망기간 명시.
- **재사용:** 용량 성장/시장규모 성장 drivers. `current_gw`, `traditional_cpu_growth_gw`, `ai_uplift_gw`, `total_gw`와 값별 provenance 수정.
- **한계:** 총량 수치는 원본 그림의 reported 라벨, 세부 구성은 화면 판독에 의한 `digitized_estimate` 오차 ±1GW. 2026년 AI 구성 0은 반올림 값이며 실제 0이라는 보증이 아님. 정밀 재현 점수는 `null`.
- **Bronze:** [파일](../../bronze/2026-11-22/bcg_agentic_cpu_growth_slide4/) · payload df67b9d51f9834b301089073b2587c8b186069bff80413216dcdb3098461e738

## 03 McKinsey — 호주·뉴질랜드의 Agtech 도입격차

- **출처:** https://www.mckinsey.com/industries/energy-and-materials/our-insights/blog/australian-and-new-zealand-farmers-adopt-agtech-at-twice-the-rate-of-their-global-peers
- **발행일:** 2026-11-20. **조사시점:** 2026-04~07, 호주/뉴질랜드 추가 조사 2026-07; 글로벌 약 5,500, 로컬 약 150 농가.
- **So what:** Agtech 도입 AUS/NZ 86% vs global 46%, +40%p; digital agronomy 61/24, precision hardware 56/23, management SW 50/19, GenAI 35/17.
- **표현:** 높은 로컬 사용률 순으로 정렬한 두 시리즈 가로 막대, 직접 퍼센트 레이블, x축 0–100%. 값은 `reported`, 집단 간 차이는 `derived`.
- **재사용:** 지역별 제품 활용률·기술 도입 비교. `category`, `aus_nz_pct`, `global_pct`, `difference_pp`, 응답분모 및 기간 수정.
- **한계:** 공식 Exhibit 1은 SVGZ로 시각 확인 불가. 원본과 다른 편집형 차트로 원본 충실도 `null`, `unverified`. 제품별 사용 비율의 합은 100%가 아님.
- **Bronze:** [파일](../../bronze/2026-11-22/mckinsey_anz_agtech_adoption_ex1_editorial/) · payload 47b7770785a2d61838f8e3c89f4a1fdc76b6f655ea50c6c60993a3cecbd202d5

## 검증·게시·재사용

- 각 chart는 `render(data, theme, context)->fig`이며 `config.json`의 `THEME.source`, `THEME.neutral`, `CONTEXT`, `data.csv` 교체로 재사용 가능.
- 실행: `python chart.py --data data.csv --config config.json --theme source --output source.png` (neutral 별도 렌더링), PNG는 원본 불변 bundle 밖 `artifacts/` 보관.
- `scripts/medallion.py`의 SHA256 계산 및 카탈로그 계약과 일치하는 manifest를 생성했고, GitHub `main` tree 기반 비강제 커밋 후 신규 파일 SHA256을 원격 재계산. GitHub Actions가 repository 전체 단위 테스트, `medallion.py validate`, 렌더링을 수행한다.
- Bronze 커밋: https://github.com/UnemployedUncle/McKinseyGraphTemplates/commit/5e35f3d81430ccf4e1ccd832fa2d74a376fa38e1
- [GitHub Actions](https://github.com/UnemployedUncle/McKinseyGraphTemplates/actions/runs/44935091011) — 확인 시점 `in_progress` / `null`. 진행 중인 실행은 성공으로 간주하지 않음.
- Bain은 원본 유형에 가까운 재현이지만 스스로 부여한 점수는 정확성 보증이나 사용자 승인이 아님. BCG 수치 판독 및 McKinsey 편집형의 원본 정확성은 검증 미완료.
- Silver/Gold 미생성 및 승인 미실행; 원본 이미지·로고·폰트·원문 전문·사내 비공개 데이터·비밀키 업로드 없음.

## 단일 전달 분리

- 준비 완료는 사용자 학습·전달 완료가 아님. `prepared_complete=true`, `delivered=false`.
- 오전 07:15 전달에서는 본 보고서와 manifest, 필요하면 Actions 기록을 재조회하여 준비된 결과만 제공. 신규 조사나 중복 커밋 금지.

## 원격 자동 검증 완료 확인 (추가)

- Bronze 코드 커밋에 대한 [GitHub Actions 실행 44935091011](https://github.com/UnemployedUncle/McKinseyGraphTemplates/actions/runs/44935091011)은 `completed/success`이며, requirements 설치·12개 기본 unittest·medallion 무결성·전체 Bronze 렌더링·아티팩트 업로드가 모두 성공했다.
- [생성 이미지 및 렌더링 로그 아티팩트](https://github.com/UnemployedUncle/McKinseyGraphTemplates/actions/runs/44935091011/artifacts/14719526807)
- GitHub 원격 신규 21개 파일 SHA256과 3개 payload_sha256은 실제 파일 내용으로 재계산하여 일치했다.
- 로컬 사용자 ZIP은 source chart.py/data.csv/config.json/requirements.txt 총 12개 Git 정확일치 코어 및 PNG 6개를 제공한다. 부가 분석 메모 초안은 GitHub의 record/manifest와는 별개이며, 검수 대상의 기준은 항상 GitHub 불변 Bronze이다.
