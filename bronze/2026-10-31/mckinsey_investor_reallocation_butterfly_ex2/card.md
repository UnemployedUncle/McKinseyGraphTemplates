# McKinsey — Institutional allocation intentions (Exhibit 2)

## 1. 출처·확인 범위
- **공식 원문**: https://www.mckinsey.com/industries/financial-services/our-insights/rewiring-securities-services-for-a-new-era-of-competition-and-growth
- **발행**: 2026-10-28; 업데이트: 미공개; 열람: 2026-10-31 KST.
- **원본 위치**: Exhibit 2, https://www.mckinsey.com/~/media/mckinsey/industries/financial%20services/our%20insights/rewiring%20securities%20services%20for%20a%20new%20era%20of%20competition%20and%20growth/svgz_mck260709_rewiring-securities_v10_exh2.svgz?cpy=Center&cq=50. 원문 설명에 Butterfly Chart 명시. SVGZ 이미지는 웹 도구에서 콘텐츠 유형 제한으로 직접 열지 못함.
- **글 요지**: 증권서비스 시장은 실시간 결제·AI·디지털자산·사모시장 성장의 영향을 받고 있다. 기관투자자는 대체자산에 대한 익스포저 확대 의향이 높다. 서비스 제공자는 변화하는 자산군과 지역에 맞춰 운영·수탁 시스템을 재설계해야 한다.
- **So what (해석)**: 기관투자자의 인프라 투자 의향은 확대 38%, 축소 3%로 순증가 의향 +35%p이므로 증권서비스 기업은 대체투자 지원 역량과 서비스 인프라를 우선 점검해야 한다.

## 2. 비즈니스 주장 → 수치 → 판단
| 주장 | 사실·단위/기간/분모 | 의사결정 제안 |
|---|---|---|
| 인프라 투자 선호 | 2026년 설문, 확대 38%, 축소 3%, 순의향 +35%p(derived) | 비상장 인프라 수탁/관리 수요 대응 계획 |
| 사모투자 확대 | PE 확대 37%, 축소 12%; 순 +25%p(derived) | 대체자산 서비스 자동화·보고 역량 검토 |
| 조사 범위 | 2026년 CIB Voice of Customer Survey, 총 100개 기업·기관투자자(유럽·아시아) | 세부 유효응답 수·가중치 미공개로 통계적 일반화 주의 |

## 3. 시각화 해부
- **원본 텍스트 관찰**: 공식 사이트의 이미지 대체 설명에는 전통 자산 8개와 대체자산 7개, 총 15개 항목의 **좌측 감소/우측 증가 Butterfly Chart**로 명시돼 있음. 각 범주 수치는 공식 대체 설명에 표시; 점/막대 위치·폰트·세부 색상은 직접 확인 못함.
- **재현**: 0 중심의 양방향 수평 막대, 자산군별 2패널, 공통 축(-25~45%), 직접 수치 라벨, 반대 방향 표시의 색 구분, 로고 제외. 이중축·로그축 없음. 원본 제목이 action title인지 시각 확인 불가; 재사용 제목은 실제 데이터 패턴에 맞춰 작성.
- **해석 위험**: 왼쪽 축의 부호는 그래픽 변환일 뿐 `Decrease` 자체는 양의 응답 비율. 두 비율은 같은 분모이지만 `Increase+Decrease`가 100%일 필요 없음(변경 없음 등 기타 응답 포함).

## 4. 데이터 확보·모델링
- 원자료: McKinsey 2026 Corporate and Investment Banking Voice of Customer Survey, n=100; 문항별 n과 가중치·무응답 처리 세부는 미공개. 공개된 30개 수치를 `reported`로 옮겼으며, `net`은 별도 계산값으로만 제시. 인과모형·회귀는 이 차트의 확인된 방법이 아님.
- **data_recipe**: Observation: respondent_id × strategy. Extract survey intent (increase/decrease/unchanged) with eligibility; preserve question-level denominators and survey weights, remove duplicate responses, align asset labels, and compute P(increase)=count(increase)/eligible*100, P(decrease)=count(decrease)/eligible*100, net percentage points=P(increase)-P(decrease). Pivot to category/series/value CSV; left-transform decreases only for display, not in data.csv. Sort by source category order or configurable business order; inspect whether positive net is supported by both components.
- **메시지 성립 조건·반례**: Infrastructure increase (38%) exceeds decrease (3%) by 35pp; if category net <= 0 the title needs revision. Intent is not realized fund flows, and these responses do not add to 100% because unchanged is omitted.

## 5. 재사용
- `data.csv`의 `category,series,value`와 `config.json`의 `THEME.source/neutral`, `CONTEXT.categories/panel_order/title`을 수정. 새 데이터 방향과 반대되는 제목을 유지하지 말 것.
- 명령: `python chart.py --theme source --data data.csv --config config.json --output output.png`; 중립 테마는 `--theme neutral`.
- 적합 사례: 거래선별 견적조건 완화/강화 의향 또는 자산·지역 투자 확대/축소 설문 분석.
- 자체점수: **null (unverified)** — 이미지 직접 비교 불가. 수치 입력·단위·기능 실행 검사와 원본 시각 충실도는 별개.
