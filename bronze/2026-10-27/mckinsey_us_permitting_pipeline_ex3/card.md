# McKinsey — State-level US federal permitting exposure

## 출처 및 사실
- [Federal permitting’s uneven economic impact, and what companies can do about it](https://www.mckinsey.com/industries/public-sector/our-insights/federal-permittings-uneven-economic-impact-and-what-companies-can-do-about-it), **2026-10-22**, Exhibit 3, All industries (interactive).
- 원문 요지: 미국의 연방 인허가 대기 인프라 프로젝트 규모는 지역과 산업별로 편중되어 있다. 인허가 지연은 프로젝트 자본의 묶임과 지역 경제활동 지연으로 이어질 수 있다. 사업자는 프로젝트 포트폴리오의 지역·산업별 노출도를 선제적으로 관리할 필요가 있다.

## 단 하나의 So what
**텍사스의 인허가 대기 투자액(3,733억 달러)은 두 번째인 캘리포니아(1,008억 달러)의 약 3.7배이므로, 인프라 투자 포트폴리오의 인허가 위험은 지역별 파이프라인 규모부터 구분해 점검해야 한다.**

## 맥락 → 숫자 → 판단
| 맥락 | 지표/기간/분모 | 원문 확인값 | 경영 판단 |
|---|---|---|---|
| 미국 연방 인허가 대기 사업의 지역 집중 | 2025년 기준 추정, 미국 주별 파이프라인 **절대금액**(USD billion) | TX 373.3, CA 100.8, FL 80.5, NY 61.3, AZ 59.7, MI 56.1, PA 54.3, NC 50.6, IL 46.4, OH 45.1 | 주별 승인 일정·자본집약도 우선 관리 |

이 10개 주는 전체 50개 주 중 상위 표시값이며 합계가 전국 전체 1.8조 달러를 나타내지 않는다. 주별 GDP 대비 노출도 순위는 와이오밍·알래스카 등으로 다르게 나타나며, 절대값 순위와 비교하지 않는다.

## 시각화 설계
원문 Exhibit 3은 산업을 선택하는 **인터랙티브한 주별 파이프라인 차트**로, 모든 산업 선택시 위 상위 10개의 주별 정확한 값을 직접 제공한다. x=추정 투자액(USD billion), y=주 이름, 색=텍사스를 선택적으로 강조, 정렬=금액 내림차순, 직접 라벨=소수 첫째자리. 이 스크립트는 해당 데이터를 독립적인 가로 순위 막대로 구성한 것이다. **원본 인터랙티브 시각 구조·원본 색을 직접 볼 수 없으므로 동일 재현으로 점수를 부여하지 않는다.** 축은 0에서 시작하고 이중축/로그축이 아니다.

## 데이터 recipe
(1) `project_id, state, sector, investment_value, investment_currency, permitting_status, snapshot_date` 수집 → (2) 최신 공시·프로젝트 파이프라인의 중복 프로젝트·다중 주 프로젝트 중복 산입 방지 → (3) 동일 기준 연도와 통화로 맞추고 금액 추정 여부 표시 → (4) `state`별 `SUM(investment_value)` → (5) 동률 정렬 정의 후 상위 10개 추출 → (6) 필요 시 같은 기간 state_GDP를 결합해 GDP 대비 노출도 산출 → (7) 절대 투자액 순위와 상대 GDP 노출도 메시지를 구별한다.

원문 방법론은 프로젝트 공표 내역과 관측 경제활동을 토대로 주별 노출도를 추정한 모델이다. 사업별 상세 원천 및 추정 오차·확률 분포는 확인 가능한 본문에서 공개되지 않아 재계산으로 원문 결과를 완전히 재현할 수 없다.

## 메시지 조건·한계
절대 금액 기준 텍사스가 2위보다 충분히 큰 경우 현재 메시지가 적합하다. 다주 프로젝트의 배분법이 바뀌거나 주별 GDP 분모를 적용하면 순위가 달라질 수 있다. 해당 투자가 모두 취소되거나 연간 GDP 손실로 확정됐다는 의미가 아니다.

## 재사용
`config.json.THEME`의 강조색과 레이블 크기, `CONTEXT`의 제목/단위, `data.csv`의 주·금액을 변경한다. 예: 글로벌 딜별 국가·상품별 인허가 대기 계약 규모. `python chart.py --theme source --data data.csv --output output.png`.

출처 도표 파일은 저장하지 않았고 재현 결과만 제공한다. 사용자 검수 전 Bronze 후보이며 모델 학습 이용 권한 미확인.
