# BCG — How Companies Can Find New Value in Existing Materials

## 원문 요지 (3문장)
순환경제의 경쟁력은 폐기물 처리뿐 아니라 제품 안에 남은 가치의 보존에 있다. EU 사용 제품의 핵심광물 내재 가치와 연간 종료 제품의 회수 잠재가치를 대비한다. 실제 사업기회는 경제적 회수와 재사용 가능성에 달려 있다.

## So what (단 하나)
EU 사용중인 전자제품·가전의 핵심광물 재고 가치는 €65B를 넘고 연간 사용종료 핵심광물 가치 약 €9B는 EU 전자산업의 연간 수요 약 €6B보다 크지만, 실질 회수가능량은 별도 평가해야 한다.

## 비즈니스 맥락 → 지표 → 판단
- 관측 단위: scope × stock or annual-flow category.
- X/y, 크기, 색: X=value, Y=metric, 막대 길이=value, THEMEs의 강조색과 중립색.
- 단위, 기간, 분모: stock EUR billion과 연간 EUR billion/year는 서로 다른 시간단위로 패널 분리, 분모 없음.
- 데이터 관측연도: 미공개. 공식 글 발행일 2026-11-11; 수집일 2026-11-12.
- 인사이트 유형: stock versus annual flow 대비.
- 정렬: stock와 annual-flow 범주별 분리 후 데이터 순서; 공통 원점 0; 레이블과 주석은 config.json의 CONTEXT로 설정.
- 원본 차트 이미지 직접 확인 불가. 본문 수치만으로 구성한 **편집형 시각화**이므로 원본 재현 점수 null.

## 자료, 표본, 계산법, provenance
- Official URL: https://www.bcg.com/publications/2026/circularity-value-existing-materials
- Figure ref: Exhibit 1 (article reported values; editorial)
- 모든 CSV 값의 provenance=reported. 기초자료의 표본수·측정기간·모델·오차범위는 미공개로 기록.
- €65B는 strict lower bound, 약 €9B와 €6B는 연간 유량의 근사값. 연간 유량을 재고와 합산하거나 동일 회수량으로 간주하면 안 됨.
- 편집형 차트 설계는 원문의 원본 이미지와 유형이 같다는 주장이 아님.

## 단계별 data_recipe
1. Define geography, product coverage and material valuation basis
2. Calculate embedded in-use mineral stock
3. Value annual end-of-use stream and annual manufacturing demand on comparable boundaries
4. Separate stock and annual flow units
5. Model recovery, collection and quality constraints before claiming substitution

## 메시지 조건, 반례와 한계
Stock >€65B is not a flow. About €9B and €6B are annual flows; theoretical end-of-use value does not equal recoverable supply.
EU 회수 재료의 가치는 품질, 부품 재사용 여부, 처리비용에 따라 크게 달라질 수 있다. 수요 대체율은 실제 회수율이나 품위 검증 없이는 알 수 없다.
현재 값만으로 실현 매출이나 인과효과를 추론하지 않는다.

## 실행·재사용
Install requirements.txt; run: python chart.py --data data.csv --config config.json --theme source --output source.png. Repeat with neutral. Reuse by changing data.csv and THEME/CONTEXT in config.json; outputs belong outside immutable Bronze.
