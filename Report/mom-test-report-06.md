# Mom Test 인터뷰 보고서 — Round 6 (완료)

**인터뷰 일자:** 2026-06-11  
**방식:** `/momtest` — AskQuestion UI, Q1~Q6 전체 응답  
**대상 제품:** `UnitConverter.py` (meter/feet/yard·`3'-6"`·`4½"` — **cm/mm/inch 미지원**)  
**근거 Transcript:** [Prompting/mom-test-transcript-06.md](../Prompting/mom-test-transcript-06.md)

---

## 1. 표면 문제 (잘못된 정의)

- "**cm·mm·inch 지원 변환 앱**을 만든다."
- "**cmd 없는 GUI 프로그램**을 만든다."
- "**현장용 스마트폰 변환기**" (솔루션 포장)

→ 사용자는 앱을 요청하지 않음. 고통은 **미지원 단위·cmd 진입 장벽·반복 입력·집중 단절**.

---

## 2. 진짜 문제 (한 문장)

도면·현장에서 **cm/mm↔inch** 환산이 필요한데 지원 단위 밖이면 **핸드폰 변환기에 의존**하고, **cmd black screen** 때문에 PC CLI는 쓰지 않으며, 다중 치수는 **순차 입력·지우기 반복**으로 **10분·1분+/회** 집중이 끊긴다.

---

## 3. Mom Test 증거 3줄

1. > "cm/mm를 inch로 바꾸지 못해 **10분** 허비했다"
2. > "인치 치수 **하루 10회+**, 회당 **1분+** 집중 단절"
3. > "핸드폰에 **순차 입력** — 지우고 다시 입력 반복"

---

## 4. 인터뷰 요약

| Q | 응답 |
|---|------|
| Q1 | cm/mm → inch 실패, **10분** |
| Q2 | 핸드폰 단위 변환기, **1분**/치수 |
| Q3 | **미사용** — cmd/search black screen 부담 |
| Q4 | 인치 **10회+/일**, **1분+/회** 집중 단절 |
| Q5 | inch 사용, **현장=핸드폰** — PC/cmd 안 씀 |
| Q6 | 핸드폰 **순차 입력·지우기 반복** |

---

## 5. 갭 분석 (관찰, 솔루션 아님)

| 인터뷰 행동/손실 | 현재 CLI | 갭 |
|------------------|----------|-----|
| cm/mm → inch 필요 | meter/feet/yard만 | **cm·mm·inch 미지원** (R4와 동일) |
| cmd black screen | `python UnitConverter.py` | **진입·발견 장벽** — 미사용 |
| 현장 10회+/일 1분+ | PC/cmd 전제 | **현장 경로 없음** — 핸드폰 유지 |
| 다중 치수 지우기 반복 | `--batch` 있음 | **미인지·미사용** (Q6은 핸드폰 경로) |

---

## 6. Test Loop 후보

| 우선 | 후보 | Mom Test 연결 |
|------|------|---------------|
| 1 | **D-UNIT-03** — `cm:` / `mm:` 파싱·변환 | Q1 · **10분** |
| 2 | **D-UNIT-04** — `inch` 단독·분수 인치 출력 연계 | Q1 · Q5 |
| 3 | **U-BATCH-02** (가칭) — 일괄 모드 **발견성** (도움말·첫 실행 힌트) | Q6 순차 입력 |

*cmd/GUI 장벽·현장 스마트폰은 Mom Test 범위 밖 — 증거는 **미지원 단위·반복 입력·집중 단절**에 고정.*

---

## 7. Round 간 비교

| Round | 핵심 증거 | 차이 |
|-------|-----------|------|
| R3 | `meter: 2.5` 형식, 5분 | CLI 사용·형식 고통 |
| R4 | cm/mm→inch, 10분 (Q1~Q2만) | 단위 갭 강조 |
| **R6** | cm/mm→inch + cmd 미사용 + 10회+/일 | **단위 갭 + 진입 장벽 + 일괄 미경로** 통합 |

---

## 관련 문서

| 문서 | 설명 |
|------|------|
| [mom-test-report-04.md](mom-test-report-04.md) | Round 4 (부분) |
| [mom-test-report-03.md](mom-test-report-03.md) | Round 3 |
| [.cursor/commands/momtest.md](../.cursor/commands/momtest.md) | `/momtest` Command |

---

*본 문서는 Report/mom-test-report-06.md — `/momtest` Round 6 보고서입니다.*
