# Golden Master 산출물 — D-LOC-01

| 항목 | 값 |
|------|-----|
| Phase | green \| Layer: entity \| Track: Logic |
| RED 묶음 | **D-LOC-01** |
| Test ID | VL-R1-001, VL-R1-002 |
| Command | `/golden-master` |
| upstream | [D-LOC-01-green.md](./D-LOC-01-green.md) |
| 완료일 | 2026-06-11 |

---

## PASS 전제

```text
pytest tests/entity/test_d_loc_01.py -v → 2 passed
```

---

## golden 경로 · matched

| Test ID | golden 파일 | approval 테스트 | matched |
|---------|-------------|-----------------|---------|
| VL-R1-001 | `tests/golden/VL-R1-001.approved.txt` | `test_d_loc_01_step_a_success` | **yes** |
| VL-R1-002 | `tests/golden/VL-R1-002.approved.txt` | `test_d_loc_01_step_b_misconversion_fail` | **yes** |

---

## golden 내용

### VL-R1-001

```text
status=pass
failed_lines=[0,0,0,0,0,0]
error_code=none
```

### VL-R1-002

```text
status=fail
failed_lines=[1,0,0,0,0,0]
error_code=none
```

---

## pytest 명령

```bash
# 기준 생성 (1회)
UPDATE_GOLDEN=1 pytest tests/entity/test_d_sol_01.py -v

# matched 확인
pytest tests/entity/test_d_sol_01.py -v
pytest tests/entity/test_d_sol_01.py::test_d_loc_01_step_a_success -v
```

**결과:** `UPDATE_GOLDEN=1` → 2 passed · matched 확인 → 2 passed

---

## diff 요약

- 없음 — 전부 matched

---

## 변경 파일

| 파일 | 작업 |
|------|------|
| `tests/_approval.py` | `format_golden`, `assert_matches_golden` |
| `tests/entity/test_d_sol_01.py` | Golden approval 테스트 2개 |
| `tests/golden/VL-R1-001.approved.txt` | 자동 생성 |
| `tests/golden/VL-R1-002.approved.txt` | 자동 생성 |

---

*본 문서는 docs/ 최종 산출물 — D-LOC-01 Golden Master 보고서입니다.*
