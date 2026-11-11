# MCKINSEY — System advantage: The new source of value in chemicals

## 원문 요지 (3문장)
화학기업의 비용·입지·기술 경쟁력만으로는 과거 수준의 수익을 보장하기 어렵다. 중국의 공급구조 변화가 글로벌 무역과 산업별 마진에 압박을 가한다. 포트폴리오, 운영모델, 고객혁신 및 현금관리의 조합이 중요하다.

## So what (단 하나)
중국의 glyphosate 기존 공급은 글로벌 수요 대비 40% 많고 일부 고무 첨가제는 300% 많다. 화학기업의 포트폴리오는 업종 평균이 아니라 개별 품목의 공급구조를 기준으로 평가해야 한다.

## 비즈니스 맥락 → 지표 → 판단
- 관측 단위: chemical product × supply-demand comparison.
- X/y, 크기, 색: X=value, Y=metric, 막대 길이=value, THEMEs의 강조색과 중립색.
- 단위, 기간, 분모: 중국 기존 공급과 동일 품목 글로벌 수요의 차이 비율(%), 분모는 품목별 글로벌 수요.
- 데이터 관측연도: 미공개. 공식 글 발행일 2026-11-10; 수집일 2026-11-12.
- 인사이트 유형: 제품별 초과 공급 비교.
- 정렬: 값으로 정렬; 공통 원점 0; 레이블과 주석은 config.json의 CONTEXT로 설정.
- 원본 차트 이미지 직접 확인 불가. 본문 수치만으로 구성한 **편집형 시각화**이므로 원본 재현 점수 null.

## 자료, 표본, 계산법, provenance
- Official URL: https://www.mckinsey.com/industries/chemicals/our-insights/system-advantage-the-new-source-of-value-in-chemicals
- Figure ref: Article quantitative comparison near Exhibit 2 (editorial)
- 모든 CSV 값의 provenance=reported. 기초자료의 표본수·측정기간·모델·오차범위는 미공개로 기록.
- 40%와 300%는 각각 서로 다른 화학제품 그룹의 글로벌 수요 대비 중국 공급 초과 비율. 특정 제품 정의를 다른 첨가제에 일반화하지 않음.
- 편집형 차트 설계는 원문의 원본 이미지와 유형이 같다는 주장이 아님.

## 단계별 data_recipe
1. Define molecules and comparable supply and demand coverage
2. Collect existing Chinese supply and global demand in common year
3. Calculate percent above global demand using (China supply/global demand - 1)*100
4. Preserve distinct product identities and source qualifiers
5. Sort values and show a zero baseline
6. Check capacity utilization, logistics, tariffs and demand scenarios

## 메시지 조건, 반례와 한계
300% is specific to certain rubber additives. The underlying year, molecules and methodology are undisclosed; do not interpret as inventories or realized exports.
초과 공급량이 실제 판매 가능한 수출 물량을 뜻하지 않는다. 해당 물질의 가격과 수익성은 운임·관세·가동률·규제에도 좌우된다.
현재 값만으로 실현 매출이나 인과효과를 추론하지 않는다.

## 실행·재사용
Install requirements.txt; run: python chart.py --data data.csv --config config.json --theme source --output source.png. Repeat with neutral. Reuse by changing data.csv and THEME/CONTEXT in config.json; outputs belong outside immutable Bronze.
