# Bronze — 처음 생성한 코드

날짜/차트별 최초 생성 산출물을 보존합니다. 새 생성물과 수정 재생성본은 모두 Bronze로 시작합니다. 자체 충실도 점수가 높아도 사용자 검수 승인이 아닙니다.

`python scripts/medallion.py ingest --source /path/to/bundle --date YYYY-MM-DD --slug firm_topic_figure`

같은 내용은 중복 생성하지 않습니다. 동일 경로의 내용이 달라지면 `_rev_<hash>` 새 폴더가 생성됩니다. 기존 Bronze를 덮어쓰지 않습니다. 출력 이미지는 묶음 밖의 artifacts/에 저장합니다.
