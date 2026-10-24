# The AI value curve: The economics of applying AI to existing work

AI 단위 비용이 30% 상승하면 미국과 글로벌 AI 가치풀 모두 약 3분의 1 줄어드는 모형 결과이므로, 사용량 확대 전에 비용 민감도 테스트가 필요하다.

원문: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-ai-value-curve-the-economics-of-applying-ai-to-existing-work

## 이관 상태
기존 생성 코드와 CSV를 보존한 Bronze입니다. 이 문서는 이관 요약이며 원문의 수치·이미지를 이번 이관에서 재검증하지 않았습니다. 이전 자동 평가는 사용자 검수 승인이 아닙니다. 전체 데이터 확보·모델링 설명은 record.json의 data_recipe와 message_conditions를 확인합니다.

## 실행
`python chart.py --theme source --data data.csv --output /absolute/path/output.png`

색과 문구는 config.json의 THEME/CONTEXT, 값은 data.csv에서 수정합니다. Bronze 파일은 직접 고치지 않고 수정본을 새 버전으로 적재합니다.
