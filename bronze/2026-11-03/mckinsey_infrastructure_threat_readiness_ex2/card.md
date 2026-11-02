# McKinsey — Critical infrastructure is under threat. Are organizations prepared? | Exhibit 2, reported values (editorial visualization)

**공식 원문:** https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/critical-infrastructure-is-under-threat-are-organizations-prepared  
**게재일:** 2026-11-02 / **수집 및 코드 생성일:** 2026-11-03 / **데이터 시점:** Q1 2026  
**원본 그림 위치:** Exhibit 2, reported values (editorial visualization) / 원본 이미지 파일은 저장하지 않음.

## 글의 요지 (3문장)
1. 복합·하이브리드 위협에 대비한 조직 보안 포트폴리오 편중을(를) 다룬 공식 자료다.
2. 사이버·IT 위협 대응 역량은 98%의 조직이 보유했지만 간첩·은밀한 작전 대응 역량은 32%에 불과하므로, 인프라 회복력 투자는 디지털 보안 외의 사각지대도 다뤄야 한다.
3. 원문에서 확인 가능한 수치는 기록했으나 원본 차트의 모든 시각적 요소는 확인하지 못했다.

## So what
사이버·IT 위협 대응 역량은 98%의 조직이 보유했지만 간첩·은밀한 작전 대응 역량은 32%에 불과하므로, 인프라 회복력 투자는 디지털 보안 외의 사각지대도 다뤄야 한다.

## 비즈니스 맥락 → 숫자 → 판단
- 관찰: 위협별 대응 역량 보유율은 Cyber/IT 98%, Physical/hardware 77%, Information/psychological 59%, Economic/political coercion 47%, Espionage/covert 32%로 기사에 서술되어 있다.
- 해석: 기존 디지털 인프라 중심 보호체계와 간첩·은밀한 작전 등 비가시적 위협 대응 간 역량 격차가 66%p다.
- 재사용 제안: 자산 또는 조직별 위협 대응 capability matrix를 구성하고 중요도와 결합해 gap priority를 계산한다.


## 측정·집계 정의
- insight_type: comparison / gap; metric: `capability_presence_share`
- unit: percentage of the relevant denominator; denominator: responding organizations (n=122).
- period: Q1 2026; sample/method: 2026년 1분기 조사 참여 조직 122개; 위협별 역량 존재 여부의 복수 응답.
- numeric provenance: **reported** (원문에 서술된 값), 항목별 값은 `data.csv`에 기록.
- value retrieval: HTML 기사 본문에 수치가 직접 등장하며 부재한 값은 채우지 않았다.

## 시각화 해부
x=capability_presence_share(0–100%), y=threat_category sorted descending, color=lowest capability highlight, direct percentage labels, non-truncated zero axis.
다섯 위협별 대응 역량 보유율을 공통 0~100% 축에서 내림차순 가로 막대로 비교하고 최저 역량인 간첩·은밀한 작전을 강조.
색상·주석·레이아웃은 `config.json`의 `THEME`와 `CONTEXT`에 분리했다. 원본 로고·저작권 이미지는 사용하지 않았다.

## 재사용 data_recipe
1. 조직·사업장별 특정 위협에 대한 대응 capability 유무와 기준 기간을 수집한다.
2. 위협 분류를 중복 없는 코드로 정규화하고 질문 문항별 유효 응답 조직을 분모로 사용한다.
3. threat_category 별 established=true 조직 수 / 유효 응답조직 수 ×100을 계산한다.
4. reported/derived 구분 및 표본·시점·반올림을 검증한다.
5. 내림차순 정렬 후 최저 보유율을 highlight로 표기한다. 위협의 발생확률 또는 피해 심각도와 혼동하지 않는다.


## 메시지 성립 조건·반례 및 한계
이 메시지는 설문 문항이 측정한 **역량 보유**에만 해당한다. 실제 회복력이나 침해 사고 가능성의 차이를 직접 뜻하지 않는다. 위협 위험도·발생 가능성을 포함한 비용편익 결론은 추가 데이터가 필요하다.

## 정확성·원본 비교
`chart.py` 실행은 검증했으나 원본 그림의 시각적 픽셀·인코딩 비교는 하지 못했다. **편집형 시각화(`validation_status=unverified`, `fidelity_score=null`)**로 저장한다. 설문 수치와 모델 시나리오 수치를 관측 성과로 혼용하지 않는다.

## 사용법
`pip install -r requirements.txt` 후 `python chart.py --data data.csv --config config.json --theme source --output output.png` 실행. `neutral` 테마도 동일하게 동작한다. 값과 문맥이 바뀌면 제목·강조 항목을 새 주장에 맞게 재검토한다.
