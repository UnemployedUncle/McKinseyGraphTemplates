# McKinsey · 유럽 농가의 구매 의향은 국가별로 다르다 (편집형)

## 원문 요지 (직접 작성, 3문장)
McKinsey의 2026년 Global Farmer Insights는 마진 압박 속 유럽 농가의 구매 행동 변화를 다룬다. 같은 유럽 내에서도 스페인·독일·프랑스의 향후 지출 의향이 크게 갈린다. 공급업체는 농가 유형과 시장별로 가격·유통·제품 조합을 달리 설계해야 한다.

**So what — 농자재·장비 매출 전망과 영업 투자 우선순위는 유럽 전체 평균보다 국가별 지출 순의향에 맞춰 수립해야 한다.**

### 비즈니스 맥락 → 데이터 → 판단
- 맥락: 농가의 비용 절감과 제품 수요 변동
- 지표: `increase_pct - decrease_pct` 순지출 의향, 단위 `%p`; **지출 증가 예상자의 비율 자체가 아님**
- 2026년 4~7월 조사, 향후 12~18개월 의향; 스페인 78, 독일 44, 프랑스 −8 %p (`reported`)
- 유럽 표본 총 701명: 스페인 200, 독일 250, 프랑스 251; 글로벌 조사 5,500명
- 판단: 지역별 수요 전망을 분리해야 하지만 실제 구매나 매출 증가로 해석하면 안 됨

### 차트 구성 근거
- 인사이트 유형: cross-market divergence
- x=순지출 의향 %p, y=국가, 색=음수와 주요국 강조, 크기=막대 길이, 정렬=내림차순
- 0 수직 기준선, 부호 있는 직접 레이블, 음수 왼쪽 확장, 제목·출처·설문 기간 주석
- 원본 Exhibit 2 이미지는 직접 보지 못해 **형식 동일 재현이 아닌 편집형 재구성**임

### 공개 데이터와 계산
- 원문: https://www.mckinsey.com/industries/energy-and-materials/our-insights/blog/global-farmer-insights-2026-a-closer-look-at-europe (2026-11-12)
- 자료: Global Farmer Insights 2026 (조사 2026-04~07); 정확한 국가별 원 응답수·가중치·신뢰구간은 미공개
- `reported`: 순수치 78, 44, -8. `increase_pct`와 `decrease_pct`의 원시 값은 미공개이며 역산하지 않음

### 재사용 data_recipe
1. `respondent_id × country × wave` 단위로 실제 조사를 수집한다.
2. 국가별 유효 응답 중 증가/감소 의향의 비율을 별도 계산한다.
3. `net_sentiment_pp=increase_pct-decrease_pct`로 산출하고 0 기준에서 부호 검증한다.
4. `data.csv`, `CONTEXT`, `THEME`을 수정하고 동일한 chart.py를 재사용한다.

### 메시지 조건 및 반례·한계
- 양수라고 해서 그 비율의 농가가 지출을 늘린다는 뜻이 아니다.
- 표본이 다르고 국가별 농장 구성·품목 비중 차이가 있어 인과 주장은 불가.
- 조사 이후 실물 가격 변동, 기상이변, 정책 변경이 실현 지출을 바꿀 수 있다.
- 원본 이미지 접근 불가로 재현 충실도 점수 `null`, `unverified`. 데이터 공개값과 실행 성공은 별도 검증한다.

### 사용법
`pip install -r requirements.txt` 후 `python chart.py --data data.csv --config config.json --theme source --output source.png`; `neutral`도 동일.
