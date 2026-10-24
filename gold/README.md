# Gold — 재사용·배포 후보

현재 Gold 코드는 없습니다. Silver를 거치지 않고 승격할 수 없습니다.

Gold는 사용자 검수된 Silver 중 렌더링, 데이터 검사, 다른 데이터/문맥을 사용한 재사용 테스트, 원본 비교를 통과한 버전입니다. quality.json에 render_passed, data_checks_passed, reuse_test_passed, original_comparison_passed=true, fidelity_score>=4.5, evidence를 기록해야 합니다. quality.json도 검수 대상이므로 최초 Silver 승인 전에 포함하거나 새 Bronze 버전으로 만들어 재검수합니다.

같은 수동 승격 워크플로에서 target=gold를 선택합니다. Gold 승격은 자동 모델 학습이 아니며, 학습 후보 표시에는 training_rights_confirmed=true가 추가로 필요합니다. 이 표시는 법적 권한의 자동 검증을 뜻하지 않습니다.
