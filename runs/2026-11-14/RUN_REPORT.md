# Consulting Graph Template — 2026-11-14

## 당일 준비 결과 (Asia/Seoul)
- 준비 시작: 2026-11-14 03:16:32 KST
- 실행 단계: 03:15 사전 준비. 07:15 전달 단계에는 이 준비본을 재조회해 재조사·중복 커밋을 피한다.
- 신규 Bronze: 2/3 목표, BCG 1건 / McKinsey 1건, Bain 0건 (발행일·접근 가능한 원본 정량 차트·비중복을 동시에 입증한 사례 미확보).
- 저장소 누적: Bronze 58 / Silver 0 / Gold 0; 역사적 에이전트 원본 재현 자체검증 통과 14건; 오늘 신규 원본 재현 검증 0건.
- 현재 신규 둘 다 editorial chart, validation_status=unverified, fidelity_score=null, human_review=pending, training_eligible=false.
- 실행 검증: Python unit test 8/8 passed, local medallion validate passed, source+neutral PNG 4개 200dpi 렌더링, 양쪽 시각 확인. Python 3.13.5, matplotlib 3.10.8, pandas 2.2.3.
- Source/Neutral PNG은 코드 불변 묶음 밖 아티팩트로 보존한다. 실제 GitHub Actions 재검증은 워크플로 결과를 확인해야 한다.

## BCG · Banking AI governance implementation gap
- 공식 출처: https://www.bcg.com/publications/2026/ai-governance-banking-benchmark
- 원문 게시일: 2026-11-13. 조사 시점: 2026 benchmark; 정확한 현장 조사 기간/문항별 분모 미공개.
- 공개값: 전용 AI 정책 77%, 일부 실제 Agent 배포 허용 73%, Agent 전용 포괄적 통제 8%. 전체 벤치마크 26개 은행. 모든 값은 `reported`.
- So what: AI 정책과 배포 여부뿐 아니라 운영 중인 Agent 통제의 성숙도를 별도 KPI로 평가해야 한다.
- 편집형 Ranked Horizontal Bar, x=0–100%, y=governance measure, 직접값 레이블. 서로 다른 질문들의 비율은 퍼널 단계가 아니며 77->73->8 전환율이 아니다.
- Original chart not visually compared: self fidelity score null, original reconstruction not passed.
- Bronze: bronze/2026-11-14/bcg_banking_ai_governance_operational_gap_editorial

## McKinsey · European farmers' net investment sentiment
- 공식 출처: https://www.mckinsey.com/industries/energy-and-materials/our-insights/blog/global-farmer-insights-2026-a-closer-look-at-europe
- 원문 게시일: 2026-11-12; 조사: 2026-04~07, 총 701명 (스페인 200, 독일 250, 프랑스 251). 향후 12~18개월 투입지출 의향.
- 공개 `net spending sentiment`: 스페인 +78%p, 독일 +44%p, 프랑스 −8%p. 증가 응답 비율에서 감소 응답 비율을 뺀 값; 증가 응답 비율이 아님.
- So what: 농업 구매·판매 계획은 유럽 평균보다 국가별 향후 지출 기대 차이를 확인해 설계해야 한다.
- 편집형 Diverging Horizontal Bar, x=percentage points (pp), 중심선 0, y=country. 원본 Exhibit 2 시각적 충실도 미확인, fidelity null.
- Bronze: bronze/2026-11-14/mckinsey_europe_farm_spending_sentiment_ex2_editorial

## 재사용·제한
- 공통 CLI: `pip install -r requirements.txt` 후 `python chart.py --data data.csv --config config.json --theme source --output source.png` 또는 `--theme neutral`. 실제 검증은 `validation.json`에 기록.
- BCG 필드 `measure,value,unit,period,provenance,denominator`; McKinsey 필드 `country,value,unit,period,provenance,denominator,sample_n`.
- 기사에서 공식 그림을 그대로 시각 확인하지 못했으므로 **원본 충실도 통과가 아니라 공개 수치 편집형 구성**이다.
- Silver/Gold, 인간의 승인 기록, model training, 외부 학습 업로드 없음.

## GitHub 무결성
- `scripts/medallion.py`의 `ingest/validate` 규칙과 호환되는 파일별 SHA256 및 payload_sha256을 manifest에 작성했다.
- 카탈로그 `catalog/index.json`, `catalog/README.md`, `dataset/bronze.jsonl`는 같은 목록으로 동기화한다.
- GitHub는 `main` 현재 HEAD를 부모로 하는 Git tree 커밋, `expected_sha` fast-forward 업데이트, 원격 재조회가 완료된 경우에만 저장 성공으로 판단한다.
