# ARRR 완료 — U-IN-01 · U-IN-02 (UI boundary)

| 항목 | 값 |
|------|------|
| Phase | repeat (UI Track 2묶음) |
| Layer | boundary |
| Track | UI |
| 완료일 | 2026-06-11 |

---

## 사이클 요약

| RED 묶음 | Test ID | FR | GREEN | Golden |
|----------|---------|-----|-------|--------|
| **U-IN-01** | UI-R4-001 | FR-IN-01 | `process_input` 콜론 누락 오류 | matched |
| **U-IN-02** | UI-R4-002 | FR-IN-02 | `process_input` unknown unit 오류 | matched |

---

## RED · entity 테스트

| 파일 | 검증 |
|------|------|
| `tests/boundary/test_u_in_01.py` | `meter2.5` → `ERROR_INVALID_FORMAT` |
| `tests/boundary/test_u_in_02.py` | `foo:1.0` → `Unknown unit: foo` |

---

## GREEN (`UnitConverter.py`)

| 변경 | 내용 |
|------|------|
| `process_input(input_str)` | 파싱·변환·오류 분리 (테스트·golden 드라이버) |
| `main()` | `process_input` 호출 후 print |
| `src/constants.py` | `FEET_PER_METER`, `YARD_PER_METER`, `KNOWN_UNITS` SSOT import |

오류 메시지 (FR-IN-01/02):

- 콜론 누락: `Invalid format. Use unit:value (ex: meter:2.5)`
- unknown unit: `Unknown unit: {unit}`

---

## Golden (`tests/boundary/test_u_sol_01.py`)

| Test ID | golden | matched |
|---------|--------|---------|
| UI-R4-001 | `tests/golden/UI-R4-001.approved.txt` | yes |
| UI-R4-002 | `tests/golden/UI-R4-002.approved.txt` | yes |

포맷: `stdout={메시지}\n` (`format_ui_golden`)

---

## REFACTOR

- 매직넘버 `3.28084` / `1.09361` → `constants.FEET_PER_METER` / `YARD_PER_METER`
- `KNOWN_UNITS` SSOT 공유
- I/O와 로직 분리 (`process_input` / `main`) — boundary 테스트 without stdin mock

---

## pytest

```bash
python -m pytest tests/boundary/ -v   # 4 passed
# 전체: entity + boundary + integration → 31 passed
```

---

*docs/ARRR-ui-bundles.md — UI Track U-IN ARRR 기록.*
