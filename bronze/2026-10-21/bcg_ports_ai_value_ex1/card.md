# Ports Are Scaling AI. Here’s How to Make It Deliver.

AI 확산 비율(44%)에 비해 실질적인 실적 기여를 입증하는 응답은 4%에 불과하므로, 적용 확대보다 ROI 측정·검증 체계부터 강화해야 한다.

원문: https://www.bcg.com/publications/2026/how-ports-terminals-prove-ai-value

## 이관 상태
기존 생성 코드와 CSV를 보존한 Bronze입니다. 이 문서는 이관 요약이며 원문의 수치·이미지를 이번 이관에서 재검증하지 않았습니다. 이전 자동 평가는 사용자 검수 승인이 아닙니다. 전체 데이터 확보·모델링 설명은 record.json의 data_recipe와 message_conditions를 확인합니다.

## 실행
`python chart.py --theme source --data data.csv --output /absolute/path/output.png`

색과 문구는 config.json의 THEME/CONTEXT, 값은 data.csv에서 수정합니다. Bronze 파일은 직접 고치지 않고 수정본을 새 버전으로 적재합니다.
