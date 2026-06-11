# ARRR — Mom Test Round 7 (맥락형 인터뷰 → TDD)

| 항목 | 값 |
|------|------|
| 근거 | [Report/mom-test-report-07.md](../Report/mom-test-report-07.md) |
| Phase | repeat — **완료** |
| pytest | **73 passed** (Export 시점) |

---

## 완료 묶음

| RED 묶음 | Test ID | GREEN |
|----------|---------|-------|
| U-OUT-02 | UI-R7-001, UI-R7-002 | `_format_result_lines` 4번째 **inch** 줄 |
| U-BATCH-02 | UI-R7-003, UI-R7-004 | `BATCH_INTRO` + `BATCH_PROMPT` 빈 줄 안내 |
| U-HINT-02 | UI-R7-005, UI-R7-006 | `SINGLE_MODE_HINT` 단건 시 `--batch` 한 줄 |

---

## Mom Test R7 증거 연결

| 증거 | 구현 |
|------|------|
| `cm:254` inch 따로 적음 **3분** | `cm:2.54` → **1.0 inch** CLI 출력 |
| 빈 줄 종료 몰라 **5분** | `BATCH_INTRO` / `SINGLE_MODE_HINT` |
| inch 없어 PC 포기 | 모든 변환 **4줄** (inch 포함) |

---

*본 문서는 docs/ARRR-mom-test-r7.md — Mom Test R7 TDD SSOT입니다.*
