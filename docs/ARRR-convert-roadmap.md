# ARRR — convert_length 로드맵 (PRD §5.2 · FR-OUT-01)

| 항목 | 내용 |
|------|------|
| 선행 | Report/03 — Logic·UI validate_lines ARRR 완료 |
| 완료일 | 2026-06-11 |
| pytest | **41 passed** (entity + boundary + `test_validate_lines.py`) |

---

## 로드맵 순서

| # | 항목 | 상태 | 산출물 |
|---|------|------|--------|
| 1 | `convert_length` / `convert_lengths` | ✅ | `src/convert_length.py`, `src/length_spec.py`, `src/conversion_result.py` |
| 2 | FR-OUT-01 (R3 견적 반올림) | ✅ | `estimate_rounded`, `estimate_places` 파라미터 |
| 3 | 설정 외부화 (최소) | ✅ | `config/conversion.json` → `src/constants.py` 로더 |
| 4 | Boundary 연동 | ✅ | `UnitConverter.py` → `convert_length()` 위임 |

---

## Test ID 매핑

| Test ID | FR | RED 묶음 | 검증 |
|---------|-----|----------|------|
| CL-R1-001 | FR-LOC-01 | D-CONV-01 | `3'-6"` → `feet_decimal=3.75` |
| CL-UNIT-001 | — | D-CONV-02 | `meter:2.5` 변환 |
| CL-BATCH-001 | FR-BATCH-01 | D-CONV-BATCH | `STEEL_DIMS_8` 8건 일괄 |
| CL-OUT-001 | FR-OUT-01 | D-OUT-01 | `estimate_rounded` 기본 2자리 |
| CL-OUT-002 | FR-OUT-01 | D-OUT-01 | `estimate_places=None` 시 비활성 |
| CL-FMT-001/002 | FR-FMT-01 | D-CONV-FMT | `LengthSpecError` |

Golden: `CL-R1-001`, `CL-BATCH-001`, `CL-OUT-001` → `tests/golden/CL-*.approved.txt`

---

## API (§5.2)

```python
convert_length(spec: str, estimate_places: int | None = 2) -> ConversionResult
convert_lengths(specs: list[str], estimate_places: int | None = 2) -> list[ConversionResult]
```

`ConversionResult` 필드: `input_spec`, `feet_decimal`, `meter`, `feet`, `yard`, `estimate_rounded`

---

## 설정 (config/conversion.json)

| 키 | 기본값 | 용도 |
|----|--------|------|
| `feet_per_meter` | 3.28084 | R2 |
| `yard_per_meter` | 1.09361 | R2 |
| `r1_arch_inch_divisor` | 8 | R1 Mom Test (`Y/8` → 3.75) |
| `estimate_decimal_places` | 2 | FR-OUT-01 |
| `known_units` | meter, feet, yard | R4 |

파일 없을 시 `_DEFAULTS` fallback.

---

## Boundary 변경

`UnitConverter.process_input()` 출력 형식:

```text
meter:2.5 = 2.5 meter
meter:2.5 = 8.2021 feet
meter:2.5 = 2.734 yard
```

UI Golden (`UI-R4-001/002`) — 오류 경로만 검증, **변경 없음**.

---

## 실행

```bash
pytest tests/entity/test_d_conv_*.py tests/entity/test_d_out_01.py tests/entity/test_d_sol_conv_01.py -v
UPDATE_GOLDEN=1 pytest tests/entity/test_d_sol_conv_01.py -v   # golden 재생성 시만
```
