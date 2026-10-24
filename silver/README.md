# Silver — 사용자가 읽고 검수한 코드

현재 승인된 코드는 없습니다. 빈 계층은 의도된 상태입니다.

저장소 소유자 UnemployedUncle이 코드를 읽고 결과를 검수한 후 Actions의 **Promote reviewed template**을 수동 실행합니다. Bronze 경로, 검수한 payload_sha256, target=silver, approved=true를 지정합니다.

승인은 정확한 파일 해시에 연결되고 reviewer·시각·실행 URL·부모 경로가 manifest.json에 남습니다. Bronze는 삭제하거나 이동하지 않습니다. 변경된 코드는 새 Bronze 버전으로 적재하고 다시 검수합니다.
