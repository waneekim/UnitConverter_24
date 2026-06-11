# Golden Master — Approval Test (GREEN 후)

**GREEN PASS 후** Golden Master(Approval Test)를 **구축·검증**한다. 기준 출력을 `tests/golden/`에 고정하고 이후 회귀를 diff로 잡는다.

## Phase 선언 (필수)

응답 **첫 줄**에 반드시 작성:

```
Phase: green | Layer: entity | Track: Logic
```

- upstream: `/green-minimal` PASS · `docs/D-LOC-01-green.md` 등 GREEN 산출물
- downstream: 다음 RED 묶음 또는 `/tdd-refactor`

## 전제

- 대상 **Test ID**가 `pytest` **PASS** 상태
- Golden은 **실행 결과 스냅샷** — assert 기대값과 **독립** 검증층 (이중 잠금)

## SSOT

| 문서 | 용도 |
|------|------|
| `docs/PRD.md` | Test ID · FR 매핑 |
| `docs/D-LOC-01-green.md` | PASS Test ID·pytest 명령 |
| `.cursorrules` | ECB — E001~E005 emit 금지 |

## 절차

1. **PASS 재확인** — 대상 Test ID `pytest` PASS
2. **`tests/_approval.py`** — `assert_matches_golden` 없으면 생성
3. **`tests/golden/{id}.approved.txt`** — Test ID당 golden 파일 연결
4. **기준 생성** — `UPDATE_GOLDEN=1 pytest …` 로 `.approved.txt` **자동 생성**
5. **검증** — `UPDATE_GOLDEN` **없이** `assert_matches_golden` → **matched** 확인
6. **보고** — golden 경로 · matched 여부 · diff 요약

## `tests/_approval.py` (스케치)

```python
import os
from pathlib import Path

GOLDEN_DIR = Path(__file__).parent / "golden"


def format_golden(result: dict) -> str:
    """Approval 출력 포맷 — 고정 (수동 편집 금지)."""
    status = result["status"]
    lines = result.get("failed_lines", [])
    # failed_lines: 1-index int[6] 슬롯, 미사용 0
    slots = [0] * 6
    for i, idx in enumerate(lines[:6]):
        slots[i] = idx + 1  # 0-based → 1-index
    line_str = ",".join(str(s) for s in slots)
    # 에러 코드: ECB entity — E001~E005 미사용, status 문자열만
    return f"status={status}\nfailed_lines=[{line_str}]\nerror_code=none\n"


def assert_matches_golden(test_id: str, actual: str) -> None:
    golden_path = GOLDEN_DIR / f"{test_id}.approved.txt"
    update = os.environ.get("UPDATE_GOLDEN") == "1"

    if update or not golden_path.exists():
        golden_path.parent.mkdir(parents=True, exist_ok=True)
        golden_path.write_text(actual, encoding="utf-8")
        return

    expected = golden_path.read_text(encoding="utf-8")
    if actual != expected:
        raise AssertionError(
            f"Golden mismatch: {test_id}\n"
            f"--- expected ({golden_path})\n{expected}"
            f"--- actual\n{actual}"
        )
```

## Golden 파일 규칙

| 규칙 | 내용 |
|------|------|
| 경로 | `tests/golden/{TestID}.approved.txt` — 예: `VL-R1-001.approved.txt` |
| 생성 | **`UPDATE_GOLDEN=1`** 환경에서만 자동 생성·갱신 |
| 편집 | **수동 편집으로 통과 우회 금지** — diff 실패 시 `src/` 또는 테스트 수정 |
| `failed_lines` | **int[6] 1-index** — `0,0,0,0,0,0` 패딩, 행 인덱스는 **1-based** |
| `error_code` | **문자열 고정** — entity Track: `none` (E001~E005 emit 금지) |
| `status` | `pass` \| `fail` \| `incomplete` |

### 예시 — `tests/golden/VL-R1-001.approved.txt`

```text
status=pass
failed_lines=[0,0,0,0,0,0]
error_code=none
```

### 예시 — `tests/golden/VL-R1-002.approved.txt`

```text
status=fail
failed_lines=[1,0,0,0,0,0]
error_code=none
```

## 테스트 연결 예시

```python
from validate_lines import validate_lines
from _approval import assert_matches_golden, format_golden

def test_vl_r1_001_golden():
    result = validate_lines([[ARCH_3FT_6IN]])
    assert_matches_golden("VL-R1-001", format_golden(result))
```

## pytest 명령

```bash
# 1) Golden 기준 파일 생성 (PASS 후 1회)
UPDATE_GOLDEN=1 pytest tests/entity/test_d_loc_01.py::test_vl_r1_001_golden -v

# 2) matched 확인 (UPDATE_GOLDEN 없음)
pytest tests/entity/test_d_loc_01.py::test_vl_r1_001_golden -v

# 묶음 전체 golden
UPDATE_GOLDEN=1 pytest tests/entity/ -k golden -v
pytest tests/entity/ -k golden -v
```

## 보고 형식

```markdown
Phase: green | Layer: entity | Track: Logic

## Golden Master
- RED 묶음: D-LOC-01
- Test ID: VL-R1-001, VL-R1-002

## golden 경로
| Test ID | 파일 | matched |
|---------|------|---------|
| VL-R1-001 | `tests/golden/VL-R1-001.approved.txt` | yes |
| VL-R1-002 | `tests/golden/VL-R1-002.approved.txt` | yes |

## diff 요약
- (없음 — 전부 matched) / (불일치 시 --- expected / --- actual 요약)

## 변경 파일
- `tests/_approval.py`
- `tests/golden/*.approved.txt`
- `tests/entity/test_*_golden.py` (연결 테스트)

## 다음 단계
- 다음 RED 묶음 또는 `/tdd-refactor`
```

## 금지

- `.approved.txt` **수동 편집**으로 matched 통과 우회
- `UPDATE_GOLDEN=1` 없이 golden 파일 임의 생성·수정
- `failed_lines` 0-index·가변 길이·`error_code` E001~E005 사용 (entity Track)
- PASS 미확인 Test ID에 golden 구축
- `src/` 동작 변경 없이 golden만 맞추기 (golden 갱신은 `UPDATE_GOLDEN=1`만)

## 사용자 인자

`/golden-master` 뒤 텍스트가 있으면 Test ID·RED 묶음을 **우선** 적용한다.
(예: `/golden-master VL-R1-001 VL-R1-002`)

**Track A (boundary)**: `Layer: boundary | Track: UI` — golden에 UI stderr/stdout 문자열; `error_code`는 표시 메시지 키만 (E001~E005 직접 emit 금지 유지).
