# How Retailers Can Reinvent the Digital Flywheel for Agentic Commerce

AI 쇼핑 에이전트 대응에서 제품 데이터 보강 계획(67%)이 실시간 재고·가용성 제공 계획(58%)을 9%p 앞서므로, 데이터 품질과 실시간 실행 정보를 함께 투자 과제로 관리해야 한다.

원문: https://www.bcg.com/publications/2026/retailers-win-ai-shopping-agents

## 이관 상태
기존 생성 코드와 CSV를 보존한 Bronze입니다. 이 문서는 이관 요약이며 원문의 수치·이미지를 이번 이관에서 재검증하지 않았습니다. 이전 자동 평가는 사용자 검수 승인이 아닙니다. 전체 데이터 확보·모델링 설명은 record.json의 data_recipe와 message_conditions를 확인합니다.

## 실행
`python chart.py --theme source --data data.csv --output /absolute/path/output.png`

색과 문구는 config.json의 THEME/CONTEXT, 값은 data.csv에서 수정합니다. Bronze 파일은 직접 고치지 않고 수정본을 새 버전으로 적재합니다.
