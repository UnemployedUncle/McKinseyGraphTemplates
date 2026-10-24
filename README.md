# Consulting Graph Templates · Bronze / Silver / Gold

McKinsey·BCG·Bain 차트를 분석하고 코드로 재현하는 개인 연구 저장소입니다. 공식 컨설팅사 제품이 아닙니다.

**생성 → Bronze / 사용자 검수 → Silver / 재사용·품질 검증 및 승인 → Gold**

| 계층 | 의미 | 진입 조건 |
|---|---|---|
| Bronze | 처음 생성한 코드와 데이터·설정 | 모든 신규 산출물. 기존 스냅샷은 덮어쓰지 않음 |
| Silver | 사용자가 읽고 검수한 버전 | 소유자의 명시적 승인, 검수한 파일 해시 일치 |
| Gold | 재사용·배포 후보 | Silver + 렌더링·데이터·재사용·원본 비교 증거 + 수동 승인 |

에이전트의 자체 평가 점수는 사용자 승인으로 간주하지 않습니다. 처음 이관하는 9개 차트 묶음은 모두 Bronze입니다. 기존 실험 코드 2개는 bronze/legacy/와 원래 lab/에 보존합니다. Silver와 Gold는 승인 전까지 비어 있습니다.

## 바로 보기

[전체 카탈로그](catalog/README.md) · [Bronze](bronze/) · [Silver](silver/) · [Gold](gold/) · [검수 방법](docs/REVIEW.md)

```text
bronze/YYYY-MM-DD/firm_topic/  # chart.py, data.csv, config.json, record.json, manifest.json
bronze/legacy/                # 원래 lab/의 실험 스크립트
silver/template_id/v001/      # 사용자 검수본
 gold/template_id/v001/       # Gold 승인본
catalog/                     # 계층별 목록과 검수 상태
 dataset/                    # 계층별 색인 JSONL; 모델 학습을 실행하지 않음
scripts/                     # 적재·검증·승격·이미지 실행
prompts/                     # 매일 생성 에이전트 지침
.github/workflows/           # 자동 검사, 수동 검수 승격
```

## 실행

Python 3.11 기준입니다.

```bash
pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/medallion.py validate
python scripts/render_all.py
```

생성 이미지는 artifacts/<tier>/<template_id>/source.png 및 neutral.png에 저장합니다. GitHub Actions의 Validate medallion 실행 결과에서도 이미지 묶음과 실행 로그를 내려받습니다. 실행 성공은 원본 수치·디자인의 정확성 검증을 뜻하지 않습니다.

같은 구조의 새 차트는 config.json의 THEME/CONTEXT와 data.csv를 바꿔 생성합니다. 최초 코드 보존을 위해 Bronze 안에서 직접 수정하지 말고 별도 작업 폴더에서 수정한 뒤 ingest합니다.

```bash
python scripts/medallion.py ingest --source /path/to/generated_bundle --date 2026-10-25 --slug firm_topic_figure
```

Silver 승격은 [검수 방법](docs/REVIEW.md)에 따라 GitHub Actions에서 직접 실행합니다. Gold도 같은 절차로 승인합니다. GitHub 커밋의 원본 이력과 manifest의 부모 경로·SHA256으로 계보를 추적합니다.

## 일일 운영

기존 ChatGPT 07:15 Asia/Seoul 일정이 생성·분석을 담당하고 이 저장소 Bronze에 적재합니다. GitHub Actions는 검사·미리보기·명시적 승격을 담당합니다. 별도의 중복 일일 크롤러는 만들지 않습니다. 매일 실행에서 GitHub 쓰기 실패 시 성공으로 보고하지 않고 로컬 패키지와 실패 이유를 남깁니다.

## 이관·권한

이관에서는 초기 chart.py와 data.csv를 보존합니다. config.json은 의미 변경 없이 JSON 공백만 정리했습니다. record.json은 공개 저장소에 필요한 정보로 정리하고 내부 Library ID·임시 경로·중복 코드 본문을 제외했습니다. card.md는 이관 요약입니다. 과거 validation은 역사적 자체 평가로 표시하며 이번 이관에서 원문을 재검증했다고 하지 않습니다. 이전 전체 분석과 이미지는 기존 대화의 날짜별 ZIP에 남아 있습니다.

원본 회사 로고, 원본 그래프 파일, 폰트 파일, API 키, 사내 데이터는 저장하지 않습니다. 기존 MIT LICENSE는 저장소 코드에 적용되며 제3자 보고서·데이터의 별도 권리를 부여하지 않습니다. Gold라도 외부 모델 학습에 사용하기 전 출처별 이용 조건을 확인합니다.

기존 README는 docs/README.before-medallion.md에 보존했습니다. CODEOWNERS를 추가했지만 저장소 보호 규칙은 별도 설정입니다.
