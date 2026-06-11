# RED Skeleton — ARRR Ask (RED ④)

**ARRR A단계(Ask = RED ④)** 전용 커맨드. **`/red-test-plan` 설계표**를 기준으로 `pytest.fail` **스켈레톤만** `tests/`에 작성한다.

> **magic-square-tdd Skill**이 프로젝트·사용자 Skill에 있으면 **자동 따름** (픽스처·네이밍·AAA 관례 우선).

## Phase 선언 (필수)

응답 **첫 줄**에 반드시 작성:

```
Phase: red | Layer: entity | Track: Logic
```

- upstream: `/red-test-plan` 4블록(특히 C2C·테스트 플랜·RED 묶음 범위)
- downstream: `/tdd-red` — 스켈레톤의 `pytest.fail`을 **실제 assert**로 교체

## SSOT (읽기 순서)

1. 채팅·직전 `/red-test-plan` 출력 (Test ID, Given/When/Then, 파일·함수명)
2. `.cursor/commands/red-test-plan.md` — 설계·ECB 규칙
3. `.cursor/commands/tdd-red.md` — AAA·fixture·pytest 관례 (assert 단계는 **아직 적용 안 함**)
4. **magic-square-tdd Skill** (있으면) — 상수·grid 픽스처·테스트 네이밍

## 역할·범위

| 하는 일 | 하지 않는 일 |
|---------|----------------|
| `tests/`에 `pytest.fail` 스켈레톤 함수 추가 | `src/`·`entity/` **구현** 추가·수정 |
| `tests/conftest.py` 픽스처 (`grid_g1` 등) | `assert` 본문, 통과 더미, GREEN/REFACTOR |
| `entity/constants.py` **import만** (34/16/4) | skip·xfail |
| 완료 후 `pytest` 실행·보고 | 설계표 없이 임의 시나리오 작성 |

## 절차

1. **설계표 확인** — RED 묶음의 Test ID 목록·함수명·Given/When 추출
2. **conftest** — `grid_g1` 없으면 `tests/conftest.py`에 추가 (row-major, **0 두 개**)
3. **스켈레톤 작성** — Test ID당 함수 1개, AAA 주석 + `pytest.fail` 한 줄
4. **import** — `from entity.constants import GRID_SIZE, MAGIC_SUM, CELL_COUNT` (34/16/4 매핑)
5. **실행** — RED 묶음 범위만 `pytest -v`
6. **보고** — Test ID · FAIL 한 줄 · 변경 파일(`tests/`만)

## AAA + pytest.fail 규칙

- **Given** — Arrange 주석: 픽스처·상수·`grid` (설계표 그대로)
- **When** — Act 주석: 호출 대상·입력 (구현 호출 가능, **판정은 하지 않음**)
- **Then** — **한 줄만**: `pytest.fail("RED: {Test ID} — {Then 요약}")`
- `assert` 본문·`assert True`·빈 `pass`·`return` 통과 **금지**

## 상수·픽스처

### entity/constants.py (import만, 본 커맨드에서 생성·수정 금지)

| 이름 | 값 | 용도 |
|------|-----|------|
| `MAGIC_SUM` | 34 | 4×4 마방진 행·열·대각 합 |
| `CELL_COUNT` | 16 | 격자 셀 수 |
| `GRID_SIZE` | 4 | 한 변 길이 |

```python
from entity.constants import CELL_COUNT, GRID_SIZE, MAGIC_SUM
```

픽스처·주석에서만 참조. 도메인 로직·계산 코드 추가 금지.

### tests/conftest.py — `grid_g1`

- **row-major** 1차원 또는 2차원 표현 (프로젝트 관례 따름)
- **0이 정확히 2개** — 빈 칸(미배치) 시나리오용
- `D-LOC-01` / 좌표·치수 blank 케이스에 사용

```python
import pytest

@pytest.fixture
def grid_g1():
    """row-major 4×4, blank(0) 2개 — D-LOC-01 픽스처."""
    return [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 0, 11],
        [12, 13, 14, 15],
    ]
```

`validate_lines` 프로젝트: 설계표 Given이 문자열 `grid`이면 `grid_g1` 대신 `ARCH_3FT_6IN` 등 **red-test-plan 픽스처** 사용.

## 템플릿 예시 — `test_d_loc_01_blank_coords_row_major`

```python
import pytest
from entity.constants import CELL_COUNT, GRID_SIZE, MAGIC_SUM

# Given: red-test-plan D-LOC-01 / FR-LOC-01


def test_d_loc_01_blank_coords_row_major(grid_g1):
    # Given — FR-LOC-01: row-major 격자, blank(0) 2개, MAGIC_SUM=34
    grid = grid_g1
    assert GRID_SIZE == 4 and CELL_COUNT == 16 and MAGIC_SUM == 34  # 상수 import 확인만
    # When — validate_lines(grid) 또는 좌표 판정 진입점 (스텁 호출 허용)
    # Act placeholder: 대상 함수 미연결
    # Then
    pytest.fail("RED: D-LOC-01 — row-major blank 2개 좌표가 FR-LOC-01 Rule로 판정되지 않음")
```

> **주의**: 상수 확인 `assert`는 import·픽스처 데이터 검증용 **예외** 1줄만 허용. Then 판정 assert는 금지.

### validate_lines 변형 (VL-R1-00x)

```python
import pytest

ARCH_3FT_6IN = '3\'-6"'


def test_vl_r1_001_arch_notation_3ft_6in_passes():
    # Given — VL-R1-001: grid=[[ARCH_3FT_6IN]]
    grid = [[ARCH_3FT_6IN]]
    # When — validate_lines(grid)
    # Act placeholder
    pytest.fail("RED: VL-R1-001 — 3'-6\" 단독 행 status==pass, failed_lines==[] 미구현")


def test_vl_r1_002_feet_3_5_misrepresents_3ft_6in_fails():
    # Given — VL-R1-002: grid=[[ARCH_3FT_6IN, \"feet:3.5\"]]
    grid = [[ARCH_3FT_6IN, "feet:3.5"]]
    # When — validate_lines(grid)
    pytest.fail("RED: VL-R1-002 — feet:3.5 오환산 fail, failed_lines==[0] 미구현")
```

## 보고 형식

```markdown
Phase: red | Layer: entity | Track: Logic

## RED 묶음
- D-LOC-01 (FR-LOC-01) — VL-R1-001 ~ VL-R1-002

## pytest 결과
| Test ID | FAIL 한 줄 |
|---------|------------|
| VL-R1-001 | RED: VL-R1-001 — … |
| VL-R1-002 | RED: VL-R1-002 — … |

## 변경 파일 (tests/만)
- tests/conftest.py — grid_g1 추가
- tests/test_validate_lines.py — 스켈레톤 N개

## 다음 단계
- `/tdd-red` — pytest.fail → assert 교체, 의도한 실패 유형 확인
```

## 금지

- `src/`·`entity/` **파일 생성·수정** (`entity.constants` import는 기존 모듈 가정)
- Then에 `assert` 판정 본문 (상수 import 확인 1줄 제외)
- `@pytest.mark.skip`, `xfail`, 통과 더미
- `/red-test-plan` 없이 RED 묶음·Test ID 임의 발명
- GREEN / REFACTOR 구현

## 사용자 인자

`/red-skeleton` 뒤 텍스트가 있으면 RED 묶음·Test ID 범위를 **우선** 적용.

**Track A (boundary)**: `Layer: boundary | Track: UI` — UI 핸들러 스켈레톤; `grid_g1` 대신 stdin/stdout 픽스처.
