# Mom Test 인터뷰 보고서 — Round 4 (부분 종료)

**인터뷰 일자:** 2026-06-11  
**방식:** `/momtest` — Q1~Q2 응답 후 **조기 종료**  
**대상 제품:** `UnitConverter.py` (meter/feet/yard — **cm/mm/inch 미지원**)  
**근거 Transcript:** [Prompting/mom-test-transcript-04.md](../Prompting/mom-test-transcript-04.md)

---

## 1. 표면 문제 (잘못된 정의)

- "**cm·mm·inch 지원 변환 앱**을 만든다."
- "**미터법 단위 추가 프로그램**을 만든다."
- "**전 단위 지원 변환기**를 만든다."

---

## 2. 진짜 문제 (한 문장)

도면·현장에서 **cm/mm와 inch·feet 간 환산**이 필요할 때 지원 단위 밖이면 **핸드폰 변환기에 의존**하며 **10분·1분/회** 시간이 새고 집중이 끊긴다.

---

## 3. Mom Test 증거

| # | 인용 | 손실 |
|---|------|------|
| 1 | "cm 나 mm 를 inch로 변환하고 싶었지만 변환하지 못했어" | **10분** |
| 2 | "핸드폰의 단위변환기를 이용하고 있어. 1분걸려" | **1분/회** |

*(Q3~Q6 미수집 — 조기 종료)*

---

## 4. 인터뷰 요약

| Q | 응답 |
|---|------|
| Q1 | cm/mm → inch 실패, **10분** |
| Q2 | 핸드폰 단위 변환기, **1분**/회 |
| Q3~Q6 | 미응답 |

---

## 5. 갭 분석

| 행동/손실 | 현재 CLI | 갭 |
|-----------|----------|-----|
| cm/mm → inch | meter/feet/yard만 | **cm, mm, inch 단위 없음** |
| 현장 1분/회 | cmd·PC | 핸드폰 변환기 의존 지속 |

---

## 6. Test Loop 후보

| 우선 | 후보 | Mom Test |
|------|------|----------|
| 1 | **D-UNIT-03** — `cm:`, `mm:` 입력 파싱 | 10분 |
| 2 | **D-UNIT-04** — `inch:` 또는 inch 출력 | cm/mm↔inch |
| 3 | **FR 연동** — cm/mm ↔ feet/meter 일관 | 핸드폰 우회 감소 |

---

## 관련 문서

| 문서 | 설명 |
|------|------|
| [mom-test-report-03.md](mom-test-report-03.md) | Round 3 |
| [.cursor/commands/momtest.md](../.cursor/commands/momtest.md) | `/momtest` (객관식 개편) |

---

*본 문서는 Report/mom-test-report-04.md — Round 4 부분 보고서입니다.*
