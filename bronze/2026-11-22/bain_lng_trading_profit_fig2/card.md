# Bain — LNG trading profit faces a downside in the 2030–34 glut

## 원문 정보
- 공식 출처: https://www.bain.com/insights/lng-glut-how-to-win-when-trading-gets-crowded/
- 게시일: 2026-11-18 · 수집일: 2026-11-22 · 데이터 조사/전망 기간: 2017–19, 2020, 2022–23, 2026E, 2030–34F
- 원본 그림 위치: Figure 2 — Aggregate LNG trading profits will likely fall below breakeven in the next glut · 원본 직접 열람: 확인

## 글 요지 — 3문장
1. Bain은 2030–34년 LNG 공급 과잉으로 거래 수익성이 약해질 수 있다고 전망한다.
2. 총거래이익과 미국 LNG 선적취소 수수료를 구분해 헤지·계약 위험을 판단해야 한다.
3. 미래 2030–34F 값은 관측 사실이 아니라 조건부 전망이다.

## So what — 단 하나
2030–34F 연간 총거래이익 약 $5.5bn보다 취소 수수료 약 $5.8bn이 클 수 있어 단순 차감 순이익은 약 −$0.3bn으로 내려갈 수 있다.

## 비즈니스 판단의 연결
- 맥락: LNG 장기 구매계약, 계약 유연성 및 취소 수수료에 노출된 트레이딩 포트폴리오의 수익성 설계.
- 지표·단위·기간·분모/비교기준: USD bn/year; 연도/구간별 정규화된 추정 이익; gross와 미국산 cargo cancellation fees, 순값은 공개값의 차이.
- 판단: 2030–34F 연간 총거래이익 약 $5.5bn보다 취소 수수료 약 $5.8bn이 클 수 있어 단순 차감 순이익은 약 −$0.3bn으로 내려갈 수 있다.
- 인사이트 유형: negative-profit risk bridge

## 그래프 설계 분석
- x 인코딩: period (historical/estimated/forecast); y 인코딩: USD billion per year
- 색·라벨·정렬·축·주석·범례·여백: 양의 회색 gross bar, 음의 적색 cancellation bar, 순값 검정 dot; 2030–34F 전망과 음의 순이익을 강조. 시간 순 정렬. 제목에 조건부 전망을 표시.
- 데이터 원천·표본·계산법: Bain Figure 2; Bain Intersect, GIIGNL, IGU and S&P Global 등 원그림에 표기된 공개 출처. 세부 회사별 계약분포·모형 미공개. 지역별 거래예상 모형; 세부 표본과 계수 미공개. 2020 net=4.2−1.7=2.5; 2030–34F net=5.5−5.8=−0.3. Other nets missing.

## Reuse data_recipe
1. 공개된 시기별 gross profit을 USD bn/year로 정규화한다.
2. 공개된 cancellation fees만 각 시기 필드에 기록한다(나머지는 missing).
3. 공개값이 모두 있는 시기에만 net=gross−fees를 계산하고 derived로 기록한다.
4. CSV의 status에 관측·추정·전망을 구분한 뒤 config THEME/CONTEXT로 렌더링한다.

## 성립조건·반례·한계
총거래이익과 취소 수수료가 동일 연간·통화 기준이라는 조건에서 성립. 누락된 fees를 0으로 해석하면 안 되며 gross는 모든 운영비를 뺀 실현 순이익이 아니다. 미래 원자재 가격이나 정책 변동으로 반례 가능.
원본 Figure 2 확인. 데이터·순서·signed bars 및 net dots를 재현했으나 주석·여백·스타일이 다르고 일부 값은 원본 반올림 수치.

## 실행 방법
- `pip install -r requirements.txt`
- `python chart.py --data data.csv --config config.json --theme source --output source.png`
- `python chart.py --data data.csv --config config.json --theme neutral --output neutral.png`
- 출처 수치를 교체할 때 `provenance`, `denominator`, `unit`, `period`를 함께 검증한다.
- 생성 이미지는 불변 Bronze 밖 `artifacts/`에 둔다. 자체검증과 사용자 승인은 별개이다.
