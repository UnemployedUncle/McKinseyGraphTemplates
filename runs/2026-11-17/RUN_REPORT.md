# Consulting Graph Template | 2026-11-17 preparation

- **Started:** 2026-11-17 03:42:34 Asia/Seoul
- **Prepared:** 2026-11-17T03:51:23.079+09:00
- **New today:** 2 of 3 target (BCG 1, McKinsey 1; Bain excluded)
- **Repository counts:** Bronze 64 / Silver 0 / Gold 0
- **Historical agent-original reproduction verified:** 15 (today new verified: 0)
- **Human approval:** 0 today; both new bundles remain pending, training_eligible=false
- **Source Git commit:** [1c391bfd69eb6f4dde15411ff2aaf2b23ac9bd82](https://github.com/UnemployedUncle/McKinseyGraphTemplates/commit/1c391bfd69eb6f4dde15411ff2aaf2b23ac9bd82)
- **Preparation starting main HEAD:** `9fe5b02b0a937c89cafaa5a2fecb300ea70309e0`
- **Actions:** [43931066765](https://github.com/UnemployedUncle/McKinseyGraphTemplates/actions/runs/43931066765), completed/success; chart-previews-and-smoke-tests artifact **14257459918**.
- **Delivery:** false; use this one preparation at 07:15, without duplicate commits.

## BCG — US–Europe drug pricing scenarios

**Official source:** [How New Drug Pricing Models Will Play Across Europe](https://www.bcg.com/publications/2026/us-drug-pricing-changes-europe), published November 16, 2026; collected November 17, 2026. **Data time:** 2026 policy/model scenarios; forecast horizon and confidential assumptions not fully disclosed.

**Three-sentence article synopsis:** 미국의 최혜국 약가 모델은 미국과 유럽의 신약 가격결정이 상호 연결되는 구조를 강화한다. 미국 정부보험에만 적용하는지 민간보험까지 적용하는지에 따라 이익 영향이 달라진다. 유럽 제약사·보험자·정책당국은 가격, 출시 순서, 환자 접근성을 함께 재설계해야 한다.

**One So what:** 약가 규제 시나리오마다 신약 출시 손익 민감도가 크게 달라지므로 기업은 출시 순서와 국가별 가격전략을 시나리오별로 분리해 판단해야 한다.

**Facts and chart:** 원문 Exhibit 1을 직접 시각적으로 열어 확인했다. 원본은 **세 가지 MFN 적용 시나리오의 현재 baseline 100 대비 적용 후 이익 수준을 보여주는 다중 전후 막대그래프**다. 원본 시나리오의 이익 잔존 범위는 정부 채널 한정 **70–95**, 미국 전체 채널 **30–80**, 미국 전체 채널+8개 참조국 **25–70** (% of current baseline)로 표시되어 있다. 오늘 등록된 별도 편집형 `interval`은 **마지막 25–70 범위만** 보여주므로 원본 Exhibit 1의 재현이 아니다. `fidelity_score=null`, `validation_status=unverified`를 유지한다. 공식 기사 본문은 신약 출시의 이익 영향이 현재 수준 대비 25%~70% 범위라고 설명한다. 원본의 계산 모형과 비공개 세부 가정은 미공개다.

**Encoding:** x = 현재 대비 이익 수준(%), y = 단일 모델 범위, 직접 라벨 25/70, 범위 폭 `70-25=45 percentage_points`; 색·폰트·여백은 config `THEME`, 메시지·축은 `CONTEXT`가 관리한다. 두 endpoint 모두 `reported`이며 실제 관측 이익이 아니라 모델 시나리오다.

**Data recipe:** 동일한 손익 baseline 100을 확정하고, 시나리오 정의·적용 지역·규제 채널을 동일한 기준으로 정렬한다. 각각의 결과값과 출처를 `reported`로 기록하며 비공개 가정을 사실로 쓰지 않는다. 범위 `high-low`를 `derived`로 계산해 직접 레이블을 생성한다. 사용자 CSV, THEME/CONTEXT를 교체하되 마지막 시나리오만 보여준다는 제한을 명시한다.

**Message conditions / alternatives:** 단일 구간은 통계적 신뢰구간이 아니다. 범위 25–70은 원본의 모든 가정·시나리오를 망라한 정식 재현이 아니므로 원본과 같다는 주장을 금한다. 약가 정책별 가격변동의 방향과 실제 EBIT는 시나리오·수요·비용에 따라 달라질 수 있다.

**Immutable Bronze:** [BCG chart files](https://github.com/UnemployedUncle/McKinseyGraphTemplates/tree/main/bronze/2026-11-17/bcg_europe_drug_pricing_profit_range_editorial), payload `7153505df0576d7e66368806d5137ede3bb29e847bc53f6001364b8b153ced14`.

## McKinsey — Danfoss Green Ask coverage

**Official source:** [The CEO’s role in leading on sustainability](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/the-ceos-role-in-leading-on-sustainability), published November 16, 2026; collected November 17, 2026. Original data attribution: Danfoss climate transition plan, May 2026, reporting prior-year/current-year supplier program coverage.

**Three-sentence article synopsis:** 지속가능성을 기업 전략과 연결하는 CEO의 역할을 다룬다. Danfoss Green Ask는 연간 매입액 기준 참여 협력사 포괄 비중을 전년 40%에서 58%로 확대했다. 이는 탄소 감축량이 아니라 공급망 프로그램이 포괄하는 매입액 비중이다.

**One So what:** 공급망 탈탄소 프로그램의 확장 성과는 협력사 수뿐 아니라 **매입액 포괄률**로 측정하되 실제 탄소 감축성과와 구분해야 한다.

**Facts and encoding:** `2025=40`, `2026=58` (% of annual purchases), `reported`; `58-40=+18 percentage_points` is `derived`. x=year, y=coverage%, zero/70 axis, direct value labels and slope annotation. This is an editorial slope from article text, **not** a reproduction of McKinsey Exhibit 1 (the article's Exhibit 1 presents SBTi targets).

**Data recipe:** 협력사 연간 거래액 중 프로그램 적용 대상 거래액을 분자로 정의한다. 같은 분모·기간·포괄 조건에서 40/58 비중을 수집하고, 18%p 변화량을 계산한다. 새 기업으로 재사용할 때 거래액 정의, 공급업체 적용 조건, 실측 탄소 감축량을 별도 관리한다.

**Message conditions / alternatives:** 프로그램 참여 확대와 실제 배출 감축은 다르다. 58%는 전체 공급업체 중 58%라는 뜻이 아니다. 샘플 규모와 모니터링 방식은 기사에서 완전 공개하지 않았다.

**Immutable Bronze:** [McKinsey chart files](https://github.com/UnemployedUncle/McKinseyGraphTemplates/tree/main/bronze/2026-11-17/mckinsey_danfoss_green_ask_supplier_coverage_editorial), payload `11a57893b6b66922ebb3ebadf45e5e7b751332145470e2311dd4ac70e1cb3ba8`.

## Bain — not ingested

Recent 7-day review, extended to 30 days, did not establish a Bain official publication meeting **all three** criteria together: confirmed publication date in the window, directly inspectable numeric figure, and new canonical URL plus figure/chart key. Secondary reporting about procurement appeared, but was not used as primary official chart evidence. No fabricated Bain values or synthetic chart were added.

## Rendering, integrity, tests and next delivery

**GitHub Actions:** [Run 43931066765](https://github.com/UnemployedUncle/McKinseyGraphTemplates/actions/runs/43931066765), head `9fe5b02b0a937c89cafaa5a2fecb300ea70309e0`, completed/success. Steps `python -m unittest discover -s tests -v`, `python scripts/medallion.py validate`, `python scripts/render_all.py`, artifact upload all concluded success. The artifact `chart-previews-and-smoke-tests` contains all **128** theme renders (64 bundles × 2) with a smoke-results record.

**Independent local check:** Executed both current immutable `chart.py` sources, each using exact SHA256-matched `data.csv` and `config.json` bytes. Rendered source/neutral PNG 4/4, all **2200 × 1240** at 200 dpi. Four local PNG outputs were pixel-identical to corresponding GitHub Actions outputs. Verified BCG numeric endpoints 25/70, McKinsey shares 40/58, delta +18pp. No pixel similarity score to the *original* exhibit is asserted: both are clearly marked editorial.

**Integrity:** GitHub Actions medallion check passed for all current bundles. Local copied code/CSV/config file hashes match both new immutable manifests. Catalog/index.json recorded Bronze 64, Silver 0, Gold 0, with 15 historical verified statuses. User has not approved the new files. Do not alter Bronze, Silver, Gold, or review flags.

**Reuse:** In a copy of the bundle, modify only `data.csv` and `config.json` THEME/CONTEXT, then run:
```bash
python chart.py --data data.csv --config config.json --theme source --out artifacts/source.png
python chart.py --data data.csv --config config.json --theme neutral --out artifacts/neutral.png
```

**07:15 delivery:** Read `runs/2026-11-17/prepared.json` and this report; verify HEAD and Actions if possible. Give the full Korean result with chart visuals via linked Actions artifact and official source links. Do **not** start a new research session, create duplicate versions, execute user approval, or change delivery to completed without actually delivering.
