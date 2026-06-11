# GREEN 산출물 — D-LOC-01 (FR-LOC-01 · FR-LOC-02)

| 항목 | 값 |
|------|-----|
| Phase | green \| Layer: entity \| Track: Logic |
| RED 묶음 | **D-LOC-01** |
| FR | FR-LOC-01, FR-LOC-02 |
| Test ID | VL-R1-001 ~ VL-R1-002 |
| Command | `/green-minimal` |
| upstream | [D-LOC-01-red-skeleton.md](./D-LOC-01-red-skeleton.md) · [PRD.md](./PRD.md) §4.1 |
| 완료일 | 2026-06-11 |

---

## PASS Test ID

| Test ID | FR | Then |
|---------|-----|------|
| VL-R1-001 | FR-LOC-02 | `status==pass`, `failed_lines==[]` |
| VL-R1-002 | FR-LOC-01 | `status==fail`, `failed_lines==[0]` |

---

## 구현 요약

- `validate_lines`: 건축 표기 `X'-Y"` 파싱 + 동일 행 `feet:값` 교차 검증
- R1: `X + Y / ARCH_INCH_DIVISOR` — `3'-6"` = **3.75**, `feet:3.5` 오환산 **fail**
- 빈 셀 → `incomplete` (`failed_lines==[]`)
- ECB: `pass`/`fail`/`incomplete`만 반환 — E001~E005·boundary import 없음

---

## 변경 파일

### `src/` (구현)

| 파일 | 작업 |
|------|------|
| `src/constants.py` | 신규 — `INCHES_PER_FOOT`, `ARCH_INCH_DIVISOR` (SSOT) |
| `src/validate_lines.py` | D-LOC-01 R1 최소 구현 |

### `tests/` (작업 소스)

| 파일 | 작업 |
|------|------|
| `tests/entity/test_d_loc_01.py` | `pytest.fail` → assert (VL-R1-001/002) |
| `tests/fixtures.py` | 픽스처 상수 (`tests/constants.py`에서 분리) |
| `tests/conftest.py` | `fixtures` import |
| `tests/test_validate_lines.py` | `fixtures` import |
| `tests/test_d_loc_01.py` | 삭제 → `tests/entity/`로 이동 |

---

## pytest 결과

```text
# D-LOC-01 묶음
pytest tests/entity/test_d_loc_01.py -v → 2 passed

# 회귀
pytest tests/entity/test_d_loc_01.py tests/test_validate_lines.py -v → 11 passed
```

| 범위 | 결과 |
|------|------|
| D-LOC-01 (2) | **2 passed** |
| test_validate_lines (9) | **9 passed** (R1 범위 겹침 — 부수 PASS) |
| **합계** | **11 passed / 0 failed** |

---

## 회귀

- D-LOC-01 GREEN으로 `test_validate_lines.py` 9개도 함께 PASS
- 원인: R1 arch-only pass·`feet:3.5` fail·`incomplete` 처리가 기존 RED 시나리오와 겹침
- 다음 RED 묶음(D-UNIT-01 등)은 별도 `/green-minimal`로 진행

---

## 다음 단계

1. `/tdd-refactor` — Green 유지하며 `src/validate_lines.py` 정리 (선택)
2. **D-UNIT-01** — `/red-test-plan` → RED → `/green-minimal`
3. git commit — **사용자 요청 시만** (`green(D-LOC-01): R1 arch notation validate_lines`)

---

## 관련 문서

| 문서 | 설명 |
|------|------|
| [PRD.md](./PRD.md) | FR-LOC-01/02 |
| [D-LOC-01-red-skeleton.md](./D-LOC-01-red-skeleton.md) | RED ④ 스켈레톤 |
| [.cursor/commands/green-minimal.md](../.cursor/commands/green-minimal.md) | `/green-minimal` |

---

*본 문서는 docs/ 최종 산출물 — D-LOC-01 GREEN (`/green-minimal`) 보고서입니다.*
