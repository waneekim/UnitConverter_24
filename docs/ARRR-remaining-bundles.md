# ARRR 완료 — D-UNIT · D-FMT · D-BATCH (Logic entity)

| 항목 | 값 |
|------|------|
| Phase | repeat (5묶음 ARRR) |
| Track | Logic · entity |
| 완료일 | 2026-06-11 |
| pytest | **27 passed** (`tests/` 전체, Export 시점) |

---

## 사이클 요약

| RED 묶음 | Test ID | GREEN (src) | Golden | entity 테스트 |
|----------|---------|-------------|--------|---------------|
| **D-UNIT-01** | VL-R2-001 | `_row_fails_r2` feet·yard 동일 수치 | matched | `test_d_unit_01.py` |
| **D-UNIT-02** | VL-R2-002 | `_row_fails_r2` meter 비율 | matched | `test_d_unit_02.py` |
| **D-FMT-01** | VL-R4-001, VL-R4-002 | `_row_fails_r4_format` | matched | `test_d_fmt_01.py` |
| **D-FMT-02** | VL-R4-003 | `validate_lines` incomplete 선행 | matched | `test_d_fmt_02.py` |
| **D-BATCH-01** | VL-R3-001, VL-R3-002 | R1+R2+R4 행 검증 일괄 | matched | `test_d_batch_01.py` |

---

## src 변경 (GREEN)

| 파일 | 내용 |
|------|------|
| `src/constants.py` | `FEET_PER_METER`, `YARD_PER_METER`, `KNOWN_UNITS` 추가 |
| `src/validate_lines.py` | R1·R2·R4·batch 통합 `_row_passes` 파이프라인 |

---

## Golden (`tests/entity/test_d_sol_02.py`)

| Test ID | golden | matched |
|---------|--------|---------|
| VL-R2-001 | `tests/golden/VL-R2-001.approved.txt` | yes |
| VL-R2-002 | `tests/golden/VL-R2-002.approved.txt` | yes |
| VL-R4-001 | `tests/golden/VL-R4-001.approved.txt` | yes |
| VL-R4-002 | `tests/golden/VL-R4-002.approved.txt` | yes |
| VL-R4-003 | `tests/golden/VL-R4-003.approved.txt` | yes |
| VL-R3-001 | `tests/golden/VL-R3-001.approved.txt` | yes |
| VL-R3-002 | `tests/golden/VL-R3-002.approved.txt` | yes |

---

## REFACTOR

- R2 비율·단위 집합을 `constants.py` SSOT로 이전 (매직넘버 제거)
- 행 검증을 `_row_fails_r4` → `_row_fails_r1` → `_row_fails_r2` → `_row_passes`로 구조화
- Golden diff 없음 · `UPDATE_GOLDEN` 1회(기준 생성) 후 matched 확인

---

## UI Track

→ [ARRR-ui-bundles.md](./ARRR-ui-bundles.md) (U-IN-01 · U-IN-02 완료)

---

*docs/ARRR-remaining-bundles.md — D-LOC-01 이후 Logic entity RED 묶음 ARRR 기록.*
