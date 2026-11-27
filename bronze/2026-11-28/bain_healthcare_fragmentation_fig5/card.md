# Bain | Figure 5

출처: [In US Healthcare, Consumer Loyalty Is Up for Grabs](https://www.bain.com/insights/in-us-healthcare-consumer-loyalty-is-up-for-grabs-us-front-line-of-healthcare-2026/) · 게시 2026-11-16 · 수집 2026-11-28 · 데이터 기간 June 2026 · Flourish 30558156 thumbnail; Figure 5

## 글 요지 (사실과 해석)
미국 소비자의 의료 경험은 디지털 서비스가 개선되더라도 단절된 진료 흐름에 영향을 받는다. 복수 의료진 방문과 여러 장소 방문을 경험한다는 응답은 각각 47%, 46%였다. 서비스 연속성과 기록 공유가 별도 개선 과제임을 시사한다.

**So what:** 환자 경험 개선은 개별 접점의 디지털화뿐 아니라 분절된 진료 경로를 연결하는 데 집중해야 한다.

## 비즈니스 질문과 인코딩
업무 분절, 시스템 전환, 고객 불편 설문에서 우선순위 진단. x=동의율(0부터); y=문항; 가로막대 길이=응답비율; 모두 적색; 내림차순; 막대 끝 직접 레이블; 범례 불필요. 인사이트 유형: Ranking / pain points. 원문 관찰값은 data.csv에 reported로 표시했다.

## 데이터 출처와 한계
Bain US Front Line of Healthcare, June 2026, n=500. 복수 문항에 동의할 수 있어 합산하지 않는다. 응답은 자기보고이고 500명 표본의 세부 가중치 및 신뢰구간은 미공개다. 47%와 46%의 차이가 통계적으로 유의하다고 할 수 없다.

## 재사용 절차
1. 같은 설문 분모와 조사기간을 정의한다.
2. 항목별 동의 응답자 비중을 계산한다.
3. 내림차순을 지정하고 CSV order를 유지한다.
4. 가로 막대 길이와 직접 레이블을 비교한다.

## 사용
`pip install -r requirements.txt` 후 `python chart.py --theme source --output source.png --dpi 200` (neutral도 가능). 새 데이터와 설정은 별도 작업 폴더에서 변경한다. 원본 그림, 로고, 폰트는 포함하지 않는다.
