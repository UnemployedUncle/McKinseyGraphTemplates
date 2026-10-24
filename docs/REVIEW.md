# 검수와 승격

1. catalog/README.md에서 Bronze 묶음을 엽니다. chart.py, data.csv, config.json, record.json과 이미지 실행 결과를 검토합니다.
2. manifest.json의 payload_sha256을 복사합니다. 이 값이 검수한 파일 묶음을 식별합니다.
3. GitHub Actions → Promote reviewed template → Run workflow에서 main, path, expected_sha256, target=silver를 선택하고 본인 검수 확인을 체크합니다.
4. 워크플로 성공 후 silver/<template_id>/v001/에 복사된 검수본이 생성됩니다. 원본 Bronze는 보존됩니다.
5. Gold는 Silver에 포함되어 검수된 quality.json 증거와 별도 수동 승격이 필요합니다.

에이전트는 이 워크플로를 사용자 대신 승인 실행하거나 approved를 임의로 기록하지 않습니다. 승인자는 현재 UnemployedUncle 한 명입니다. GitHub가 제공하는 실행 주체·실행 URL을 감사 기록으로 사용합니다.

파일을 수정하면 기존 해시 승인은 유효하지 않습니다. 변경본을 새 Bronze로 적재하고 다시 검수합니다. 기존 승인본에 직접 수정하거나 품질 파일을 사후 추가하지 않습니다.

## 운영상 한계

이 워크플로와 파일 해시는 검수 절차와 무결성을 검사합니다. 저장소 관리자나 쓰기 권한자의 직접 push를 막는 보안 경계는 아닙니다. CODEOWNERS는 검토자 지정이며 자체로 필수 승인을 강제하지 않습니다. main 보호 규칙과 Code Owner 필수 리뷰는 저장소 설정에서 별도로 활성화해야 합니다. 이 구성 작업에서는 보호 규칙을 변경하지 않았습니다.

원본 시각 검증이 되지 않은 편집형 차트는 사용자 검수 후 Silver로 관리할 수 있지만, 현재 정의의 원본 재현 Gold 조건에는 통과하지 못합니다. 과거 자동 평가의 verified는 사용자 승인과 독립적인 참고 정보입니다.
