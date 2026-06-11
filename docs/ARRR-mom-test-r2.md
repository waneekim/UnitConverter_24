# ARRR — Mom Test Round 2 (Logic + UI)

| 항목 | 값 |
|------|------|
| 근거 | [Report/mom-test-report-02.md](../Report/mom-test-report-02.md) |
| Phase | repeat — **완료** |
| Track | Logic 1묶음 + UI 3묶음 |
| 완료일 | 2026-06-11 |
| pytest | **53 passed** |

---

## C2C 매핑

| FR | RED 묶음 | Test ID | Mom Test 증거 |
|----|----------|---------|---------------|
| FR-FMT-03 | D-FMT-03 | CL-R5-001, CL-R5-002 | `4½"` 15분 |
| FR-OUT-02 | U-OUT-01 | UI-R5-001 | 견적 반올림 3~4분 |
| FR-BATCH-02 | U-BATCH-01 | UI-BATCH-001 | 8치수 cmd 8회 |
| FR-IN-03 | U-HINT-01 | UI-HINT-001, UI-HINT-002 | cmd 10분+ |

---

## 사이클 순서

```
D-FMT-03 → U-OUT-01 → U-BATCH-01 → U-HINT-01
```

| RED 묶음 | entity/boundary | GREEN 대상 |
|----------|-----------------|------------|
| D-FMT-03 | `tests/entity/test_d_fmt_03.py` | `src/length_spec.py` |
| U-OUT-01 | `tests/boundary/test_u_out_01.py` | `UnitConverter.process_input` |
| U-BATCH-01 | `tests/boundary/test_u_batch_01.py` | `UnitConverter.process_batch_input` |
| U-HINT-01 | `tests/boundary/test_u_hint_01.py` | `UnitConverter` 프롬프트·오류 SSOT |

---

## R1 분수 인치 SSOT

`N½"` → `feet_decimal = N.5 / R1_ARCH_INCH_DIVISOR` (0피트 기준)

- `4½"` → **0.5625** feet
- `2¼"` → **0.28125** feet (`2.25 / 8`)

---

## Golden

| Test ID | golden 파일 | sol 테스트 |
|---------|-------------|------------|
| CL-R5-001 | `CL-R5-001.approved.txt` | `test_d_sol_03.py` |
| CL-R5-002 | `CL-R5-002.approved.txt` | `test_d_sol_03.py` |
| UI-R5-001 | `UI-R5-001.approved.txt` | `test_u_sol_02.py` |
| UI-BATCH-001 | `UI-BATCH-001.approved.txt` | `test_u_sol_02.py` |
| UI-HINT-001 | `UI-HINT-001.approved.txt` | `test_u_sol_02.py` |
| UI-HINT-002 | `UI-HINT-002.approved.txt` | `test_u_sol_02.py` |

---

*본 문서는 docs/ARRR-mom-test-r2.md — Mom Test Round 2 C2C 플랜 SSOT입니다.*
