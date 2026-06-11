# TDD RED — validate_lines

`validate_lines`에 대한 **RED 단계 전용** 커맨드. 실패하는 테스트만 추가·수정한다.

## Phase 선언 (필수)

응답 **첫 줄**에 반드시 작성:

```
Phase: RED
```

## 대상

- API: `validate_lines(grid) -> {"status": "pass"|"fail"|"incomplete", "failed_lines": list[int]}`
- `grid`: `list[list[str]]` — 행마다 치수 문자열 셀 목록
- 구현 파일 `src/validate_lines.py`는 **이 Phase에서 건드리지 않음**
- 수정 허용: `tests/test_validate_lines.py` 및 `tests/` 하위만

## 절차 (AAA)

1. **Rule 연결** — `Report/session-workbook.md`의 R1~R4·Mom Test 증거와 연결할 행동/실패를 한 줄로 정의
2. **Arrange** — `grid` fixture 구성. 기존 상수 재사용: `ARCH_3FT_6IN`, `ARCH_9FT_2IN`, `STEEL_DIMS_8`
3. **Act** — `result = validate_lines(grid)`
4. **Assert** — `status`와 `failed_lines`를 **구체적으로** 기대 (모호한 assert 금지)
5. **실행** — `pytest tests/test_validate_lines.py -v` 로 **의도한 실패** 확인 후 보고

## pytest 예시

```python
def test_feet_3_5_misrepresents_3ft_6in_fails():
    # Arrange — R1: feet:3.5는 3'-6"(3.75) 오환산 (Mom Test 증거 #1)
    grid = [[ARCH_3FT_6IN, "feet:3.5"]]
    # Act
    result = validate_lines(grid)
    # Assert
    assert result["status"] == "fail"
    assert result["failed_lines"] == [0]


def test_empty_cell_marks_incomplete():
    # Arrange — R4: 빈 셀 = 미완 입력
    grid = [[ARCH_3FT_6IN, ""]]
    # Act
    result = validate_lines(grid)
    # Assert
    assert result["status"] == "incomplete"
    assert result["failed_lines"] == []


def test_eight_steel_dims_one_misconversion_fails():
    # Arrange — 성공 기준 3: 8개 중 1개 오환산 → fail + 행 인덱스
    grid = [
        [ARCH_3FT_6IN],
        [ARCH_9FT_2IN],
        ['12\'-0"'],
        ['6\'-8"'],
        ["feet:3.5"],  # row 4
        ['10\'-6"'],
        ['8\'-3"'],
        ['5\'-4"'],
    ]
    # Act
    result = validate_lines(grid)
    # Assert
    assert result["status"] == "fail"
    assert result["failed_lines"] == [4]
```

## 보고 형식

RED 완료 시 아래 템플릿으로 보고:

```markdown
Phase: RED

## Rule / Mom Test
- Rule: R?
- 증거: (예: 3'-6" → 3.5 feet 착각, 15분 손실)

## 추가·수정 테스트
- `test_...` — 기대: status=..., failed_lines=...

## pytest 결과
- 명령: `pytest tests/test_validate_lines.py::test_... -v`
- 결과: FAILED (의도한 RED) / 실패 메시지 요약

## 다음 단계
- GREEN: `src/validate_lines.py` 최소 구현 (별도 커맨드)
```

## 금지

- `src/`·`UnitConverter.py` 등 프로덕션 코드 수정
- assert 완화 (`==` → `in`, 조건 삭제, 기대값 느슨하게 변경)
- `@pytest.mark.skip`, `xfail`, 테스트 삭제로 통과 처리
- RED 없이 GREEN 제안·구현
- 요청·Rule 범위 밖 테스트·파일 추가

## 사용자 인자

`/tdd-red` 뒤 텍스트가 있으면 그 Rule·시나리오를 우선 RED 대상으로 삼는다.
(예: `/tdd-red R2 yard와 feet 동일 수치 혼동`)
