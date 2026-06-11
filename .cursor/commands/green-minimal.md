# GREEN Minimal — ARRR Respond (GREEN)

**ARRR R단계(Respond = GREEN)** 전용 커맨드. **RED 1묶음당** `src/` **최소 구현**만 추가한다. **1커밋 = 1 RED 묶음** (커밋은 사용자 요청 시만).

## Phase 선언 (필수)

응답 **첫 줄**에 반드시 작성:

```
Phase: green | Layer: entity | Track: Logic
```

- upstream: `/tdd-red` 또는 `tests/test_d_loc_01.py` assert 확정 + RED 묶음 Test ID
- downstream: 다음 RED 묶음 또는 `/tdd-refactor` (별도 커맨드)

## SSOT (읽기 순서)

1. `docs/PRD.md` — FR·RED 묶음·Test ID
2. `.cursorrules` — R1~R4, ECB, TDD 금지
3. `src/constants.py` — 도메인 상수 SSOT (없으면 **본 묶음에 필요한 최소 상수만** 추가)
4. `tests/constants.py` — 픽스처 상수 (테스트 전용, `src/`에서 import 금지)

## RED 묶음 예시

| RED 묶음 | Test ID | FR |
|----------|---------|-----|
| D-LOC-01 | VL-R1-001 ~ VL-R1-002 | FR-LOC-01, FR-LOC-02 |
| D-UNIT-01 | VL-R2-001 | FR-UNIT-01 |
| D-FMT-01 | VL-R4-001 ~ VL-R4-003 | FR-FMT-01, FR-FMT-02 |

## 절차

1. **RED 재확인** — 이번 묶음 Test ID만 `pytest`로 **FAIL** 상태 확인
2. **src/ 최소 구현** — 해당 assert만 통과하는 최소 코드 (`src/validate_lines.py` 등)
3. **tests/ 정리** — `pytest.fail` → `validate_lines` 호출 + **assert** 교체 (`tests/test_d_loc_01.py`)
4. **PASS 확인** — 묶음 Test ID **PASS** + **회귀 없음** (다른 실패는 이번 묶음 범위 밖이면 유지)
5. **보고** — PASS Test ID · 변경 파일 · pytest 결과

## 상수·ECB

### constants.py SSOT

| 파일 | 용도 | 예시 |
|------|------|------|
| `src/constants.py` | 도메인 비율·파싱 상수 | `FEET_PER_METER = 3.28084`, `INCHES_PER_FOOT = 12` |
| `tests/constants.py` | 픽스처 문자열 | `ARCH_3FT_6IN` |

- **하드코딩·매직넘버 금지** — 리터럴은 `src/constants.py`에서 import
- `src/`에서 `tests/constants.py` import **금지**

### ECB (entity Track)

| 항목 | entity (Logic) |
|------|----------------|
| E001~E005 | **raise·return 금지** — `pass`/`fail`/`incomplete` 판정만 |
| import | **boundary·control** (`UnitConverter.py`, I/O 핸들러) **금지** |
| Domain Mock | 금지 — 실제 `grid`·문자열 처리 |

## pytest 명령 예시

```bash
# 단일 Test ID (이번 RED 묶음)
pytest tests/test_d_loc_01.py::test_vl_r1_001_arch_notation_3ft_6in_passes -v

# 파일 전체 회귀
pytest tests/test_d_loc_01.py tests/test_validate_lines.py -v
```

## 보고 형식

```markdown
Phase: green | Layer: entity | Track: Logic

## RED 묶음
- D-LOC-01 (VL-R1-001 ~ VL-R1-002)

## PASS Test ID
- VL-R1-001 — status==pass, failed_lines==[]
- VL-R1-002 — status==fail, failed_lines==[0]

## 변경 파일
- src/constants.py — (신규/추가 상수)
- src/validate_lines.py — R1 최소 구현
- tests/test_d_loc_01.py — pytest.fail → assert

## pytest 결과
- 단일: `pytest tests/test_d_loc_01.py::test_vl_r1_001_... -v` → 1 passed
- 전체: `pytest tests/test_d_loc_01.py tests/test_validate_lines.py -v` → N passed, M failed

## 회귀
- (없음) / (실패 시 즉시 수정 내역)

## 커밋
- 사용자 요청 시만 — 메시지 예: `green(D-LOC-01): R1 arch notation validate_lines`
```

## 금지

- **이번 RED 묶음 외** Test ID를 동시에 GREEN으로 해결
- REFACTOR (중복 제거·대규모 정리 — `/tdd-refactor`로 분리)
- `tests/` assert 완화·skip·xfail·삭제
- E001~E005 emit, boundary/control import
- 하드코딩 매직넘버 (`3.28084` 등 리터럴 직접 삽입)
- git commit·push (사용자 명시 요청 없이)

## 회귀 실패 시

- 즉시 수정 — 구현 롤백 또는 최소 diff 추가
- assert 변경으로 우회 **금지**
- 보고에 실패 Test ID·원인·수정 한 줄 기록

## 사용자 인자

`/green-minimal` 뒤 텍스트가 있으면 RED 묶음을 **우선** 적용한다.
(예: `/green-minimal D-LOC-01`)

**Track A (boundary)**: `Phase: green | Layer: boundary | Track: UI` — `UnitConverter.py` 경계만; entity import는 domain API 호출만 허용.
