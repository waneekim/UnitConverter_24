# RED Skeleton 산출물 — D-LOC-01

| 항목 | 값 |
|------|-----|
| Phase | red \| Layer: entity \| Track: Logic |
| RED 묶음 | **D-LOC-01** |
| FR | FR-LOC-01, FR-LOC-02 |
| Test ID | VL-R1-001 ~ VL-R1-002 |
| SSOT | [PRD.md](./PRD.md) §4.1 · §6 |

---

## 작업 소스 위치 (`tests/`)

| 파일 | 역할 |
|------|------|
| `tests/fixtures.py` | `ARCH_3FT_6IN`, `ARCH_9FT_2IN`, `STEEL_DIMS_8` |
| `tests/conftest.py` | `arch_3ft_6in` 픽스처 |
| `tests/entity/test_d_loc_01.py` | D-LOC-01 테스트 (VL-R1-001/002) |
| `tests/test_validate_lines.py` | 전체 RED assert 테스트 (9개) |

---

## pytest 결과

```text
pytest tests/test_d_loc_01.py -v          → 2 failed (pytest.fail RED)
pytest tests/test_validate_lines.py -v    → 9 failed (스텁 미구현)
```

| Test ID | FAIL 한 줄 |
|---------|------------|
| VL-R1-001 | `RED: VL-R1-001 — 3'-6" 단독 행 status==pass, failed_lines==[] 미구현` |
| VL-R1-002 | `RED: VL-R1-002 — feet:3.5 오환산 fail, failed_lines==[0] 미구현` |

---

## 다음 단계

- ~~`/green-minimal` D-LOC-01~~ → [D-LOC-01-green.md](./D-LOC-01-green.md) **완료**

---

*본 문서는 docs/ 최종 산출물 — D-LOC-01 RED Skeleton 보고서입니다.*
