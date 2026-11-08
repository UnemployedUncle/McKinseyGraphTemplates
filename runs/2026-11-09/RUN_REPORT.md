# Consulting Graph Template — 준비 보고서 | 2026년 11월 9일

> 03:15 준비 실행(실제 시작 03:18:24, 준비 문서 기록 2026-11-09T03:32:24+09:00 Asia/Seoul). 이 문서는 07:15 전달용이며, 사용자 검수/학습 완료로 표시하지 않습니다.

## 실행 요약
- 목표 3개 중 **2개** 신규 차트 템플릿 작성(Boston Consulting Group 1, McKinsey 1, Bain 0). Bronze 기존 **46**, 추가 **2**, 예상 **48**. Silver 0 / Gold 0. 원본 자체검증 통과 기존 12 + BCG 1 = **13** (에이전트 평가, 사용자 승인 아님).
- `source/neutral` PNG 4개 직접 생성 및 시각적 확인, dpi=200. Python 3.13.5, matplotlib 3.10.8. 신규 차트 로컬 단위 테스트 6개 통과, 기존 Git 전체 검증은 GitHub Actions 별도 확인 필요.
- 원본 보고서 이미지, 로고, 원문 전문, 폰트 파일, 계정 자격증명은 Git과 ZIP에 포함하지 않음.

## 01 BCG: Carve-out 상대 TSR 지수의 분리
- **출처/발행**: https://www.bcg.com/publications/2026/carve-out-strategy-both-companies · 2026-10-28 · Exhibit 1 (2026-11-09 수집, 이미지 직접 열어 확인).
- **본문 요지:** Carve-out 거래를 재편의 계기로 활용할 경우 NewCo·RemainCo 양쪽의 미래 운영모델과 전략을 설계할 여지가 생긴다. BCG의 비교 차트는 실행 유형별 후속 상대 TSR 지수를 사건 시점 이후 24개월까지 보여준다. 단순 사업분리에 비해 전환까지 추진한 집단의 성과 차이가 나타난다.
- **So what:** **사업분리의 성공지표를 거래 종료 시점이 아니라 양쪽 법인의 전략 재설계와 장기 상대 TSR까지 확장해야 한다.**
- **비즈니스 맥락 → 수치 → 판단:** 거래 이벤트 이후 상대 TSR 지수(분모 baseline index=100), T-3 days~24 months, 2집단 비교. 24개월 full-potential **121.1**, all carve-outs **100.8**, 지수 차이 **20.3 index points**. BCG 본문은 상대 TSR 차이를 **20.3 percentage points**로 설명. 전체/실행 집단의 표본 수·업종 조정·상대수익 계산법은 공개 그림만으로 독립 검증 불가.
- **차트 구조:** 동일 시간축의 2선(녹색 vs 회색), 100기준선, 전 구간 수치 직접 라벨, 마지막 점 격차 수직 주석, legend 하단. 구성의 실제 원본에 준한 재현. T-3 days 기준선은 `derived`, 9개 후속시점 x 2집단 값은 `reported`.
- **원본 대비 자체 7항목 점수** 유형5 / 값순서5 / 축5 / 색강조4 / 라벨·제목5 / 범례비율4 / 여백4 = **4.57/5**. 반복 2회(누락 기준시점 보강 후 재렌더), 의미검사 통과. 브랜드 폰트·제목 줄 배치·세부 여백은 다름. 이는 사용자 승인 아님.
- **재사용:** `transaction_id × event_elapsed_time × cohort`, 같은 벤치마크·base index, 동일 보유 기간의 대조집단을 만든 뒤 지수 궤적/마지막 격차 계산. 거래별 선택편향이 있으면 인과 주장 금지. 데이터 원자료 확보 없이 과거 값으로 회귀·통계를 재구성하지 않음.
- **Bronze:** `bronze/2026-11-09/bcg_carveout_full_potential_tsr_ex1/` (Python+CSV+설정+분석+검증+record+manifest).

## 02 McKinsey: Finnish Large-Cap Five Big Moves
- **출처/발행**: https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/assessing-the-growth-trajectory-of-finlands-largest-companies · 2026-11-06 · 본문 정량 발표, Exhibit 3 인접 설명(2026-11-09 수집).
- **본문 요지:** 핀란드 대기업은 성장 목표를 높이지만 전략적 자원배치 실행은 제한적이다. McKinsey는 21개 상장사가 2025년에 다섯 개 `big moves` 기준을 충족한 기업 수를 공개했다. 17개는 0~1개 move만 수행했고 3개 이상을 충족한 기업은 없었다.
- **So what:** **성장 목표의 발표 여부보다 실제로 실행한 전략 행동을 기준으로 투자의 우선순위를 설정해야 한다.**
- **비즈니스 맥락 → 수치 → 판단:** n=21, 2025, 회사 수(명목 회사 수). Dynamic resource reallocation **8/21**, Differentiation **7/21**, Big investments **3/21**, Productivity improvement **1/21**, Programmatic M&A **0/21**. 하나의 기업이 여러 범주를 충족하므로 비율의 합을 100%라 표현하지 않음.
- **차트 구조:** 공식 SVGZ 원본의 시각적 확인이 불가하여 **편집형 내림차순 가로 막대**로 재설계. 공통 0~21 x축, `count/21` 직접 라벨, 최저항목 0·1 색 강조. 원본 재현 점수 `null`, `unverified`. Python 실행 성공과 분리 관리.
- **재사용:** `company_id × move` Boolean 판정 및 공통 유효 분모. 분류별 통과 회사 수와 수요·실행 격차 비교. 기준 변화, 산업별 상대평가, 표본 작은 문제 주의.
- **Bronze:** `bronze/2026-11-09/mckinsey_finland_five_big_moves_ex3_editorial/`.

## Bain 제외
- 최근 7일 우선·30일 확대 탐색. 발행일 확인·원본 정량차트 직접 접근·이전 catalog와 비중복 조건을 함께 충족하는 후보가 확인되지 않음. 2026-10-29 소비재 유통 Article Figure 1은 이미 10월30일 Bronze에 존재하므로 중복 적재하지 않음.

## 코드 사용
각 Bronze 폴더에서 `pip install -r requirements.txt` 후 `python chart.py --theme source --data data.csv --config config.json --output source.png` 및 `--theme neutral ...`. 테마/문구·축·라벨은 `config.json`과 `data.csv`에 외부화했고, 함수 시그니처는 `render(data, theme, context)->fig`.

## 무결성·승인
- 각각 file SHA256 및 payload SHA256을 파일 바이트 기반으로 산출, `human_review.status=pending`, `training_eligible=false`. 사용자의 Silver/Gold 승인, 워크플로 수동 promote, 외부 학습 업로드 없음.
- **준비 상태는 `prepared.json`의 GitHub publication 상태 및 최종 GitHub 원격 재조회 이후 확정**. 07:15에는 같은 자료만 전달, 새 조사/코드/커밋 금지.
