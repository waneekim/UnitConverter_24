# TDD GREEN — validate_lines

`validate_lines`에 대한 **GREEN 단계 전용** 커맨드. RED에서 실패한 테스트를 **최소 구현**으로 통과시킨다.

## Phase 선언 (필수)

응답 **첫 줄**에 반드시 작성:

```
Phase: GREEN
```

## 전제

- 직전 RED에서 **의도한 실패**가 `pytest`로 확인됨
- GREEN 대상 테스트·기대값은 **고정** — 테스트 수정으로 통과시키지 않음

## 대상

- API: `validate_lines(grid) -> {"status": "pass"|"fail"|"incomplete", "failed_lines": list[int]}`
- 수정 허용: `src/validate_lines.py` (필요 시 `src/` 하위 보조 모듈)
- 수정 금지: `tests/` 전체, `UnitConverter.py`

## 절차

1. **실패 확인** — RED 테스트 1개(또는 묶음)의 실패 메시지·기대값 재확인
2. **최소 구현** — 해당 assert만 만족하는 가장 짧은 코드 추가
3. **Rule 준수** — `Report/session-workbook.md` R1~R4 범위 내에서만 동작 확장
4. **실행** — `pytest tests/test_validate_lines.py -v` 로 **전체 통과** 확인
5. **보고** — 변경 요약·pytest 결과·REFACTOR 여부 기록

## 구현 예시 (스케치)

```python
def validate_lines(grid):
    failed_lines = []
    for row_idx, row in enumerate(grid):
        if any(cell == "" for cell in row):
            return {"status": "incomplete", "failed_lines": []}
        # R1: 3'-6" 파싱 → 3.75 feet와 feet:3.5 비교 등 행 단위 검증
        ...
    status = "fail" if failed_lines else "pass"
    return {"status": status, "failed_lines": failed_lines}
```

- 위는 형태 참고용. RED 시나리오에 맞는 **최소 분기**만 추가할 것
- 아직 RED가 없는 케이스를 선제 구현하지 않음

## 보고 형식

GREEN 완료 시 아래 템플릿으로 보고:

```markdown
Phase: GREEN

## RED에서 통과시킨 테스트
- `test_...` — 기대: status=..., failed_lines=...

## 구현 변경
- `src/validate_lines.py`: (한 줄 요약)

## pytest 결과
- 명령: `pytest tests/test_validate_lines.py -v`
- 결과: N passed / 0 failed

## 다음 단계
- REFACTOR: 중복·명명 정리 (별도 커맨드) 또는 다음 RED
```

## 금지

- `tests/` assert 완화·삭제·skip·xfail
- RED 없이 구현 추가
- Rule·테스트 범위 밖 기능 선제 구현 (OCP 리팩터, CLI, 설정 외부화 등)
- 모든 케이스를 한 번에 풀기 위한 과도한 추상화

## 사용자 인자

`/tdd-green` 뒤 텍스트가 있으면 그 테스트명·Rule을 우선 GREEN 대상으로 삼는다.
(예: `/tdd-green test_feet_3_5_misrepresents_3ft_6in_fails`)
