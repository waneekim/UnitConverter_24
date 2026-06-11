# ARRR — Mom Test Round 3 (사용자 인터뷰)

| 항목 | 값 |
|------|------|
| 근거 | [Report/mom-test-report-03.md](../Report/mom-test-report-03.md) |
| Phase | repeat — **완료** |
| pytest | **61 passed** (Export 시점) |

---

## 완료 묶음

| RED 묶음 | Test ID | GREEN |
|----------|---------|-------|
| D-FMT-04 | CL-R6-001 | `length_spec` unit/value `.strip()` |
| U-FLOW-01 | UI-FLOW-001 | `run_single_from_stdin()` — 1프롬프트 즉시 출력 |
| U-SINGLE-01 | UI-SINGLE-001 | `is_batch_mode()` + `--batch` 일괄 분리 |

---

## 실행

```bash
python UnitConverter.py              # 단건
python UnitConverter.py --batch      # 일괄
```

---

*본 문서는 docs/ARRR-mom-test-r3.md — Mom Test R3 TDD SSOT입니다.*
