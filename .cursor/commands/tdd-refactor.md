# TDD REFACTOR — validate_lines

`validate_lines`에 대한 **REFACTOR 단계 전용** 커맨드. Green을 유지한 채 `src/` 코드만 정리한다.

## Phase 선언 (필수)

응답 **첫 줄**에 반드시 작성:

```
Phase: REFACTOR
```

## 전제

- 직전 GREEN에서 `pytest tests/test_validate_lines.py` **전체 통과**
- REFACTOR는 **동작 변경 없음** — 외부에서 보이는 API·반환값 동일

## 대상

- API: `validate_lines(grid) -> {"status": "pass"|"fail"|"incomplete", "failed_lines": list[int]}`
- 수정 허용: `src/validate_lines.py` 및 `src/` 하위 (구조 정리용)
- 수정 금지: `tests/` (assert·fixture·시나리오 변경 없음), `UnitConverter.py`

## 절차

1. **Green 확인** — REFACTOR 전 `pytest tests/test_validate_lines.py -v` 실행
2. **냄새 식별** — 중복 분기, 긴 함수, 매직 넘버, 불명확한 변수명 등 1~2곳만 선택
3. **작은 단위 리팩터** — extract 함수, 상수 추출, early return 정리 등 **한 번에 한 종류**
4. **회귀 확인** — 매 변경 후 `pytest tests/test_validate_lines.py -v` 재실행
5. **보고** — 무엇을 왜 바꿨는지, 테스트 결과 기록

## 리팩터 예시 (허용)

```python
FEET_PER_METER = 3.28084
YARD_PER_METER = 1.09361

def _parse_arch_feet(cell: str) -> float | None:
    """R1: X'-Y" → X + Y/12"""
    ...

def validate_lines(grid):
    ...
```

- 비율 상수 명명, 파싱·검증 헬퍼 분리, 중복 루프 제거
- R3(견적 반올림) 등 **아직 테스트가 없는** 기능 추가는 REFACTOR가 아님 → RED 필요

## 보고 형식

REFACTOR 완료 시 아래 템플릿으로 보고:

```markdown
Phase: REFACTOR

## 정리한 항목
- (예: 건축 표기 파싱을 `_parse_arch_feet`로 추출)

## 변경 파일
- `src/validate_lines.py`

## pytest 결과
- 명령: `pytest tests/test_validate_lines.py -v`
- 결과: N passed / 0 failed (REFACTOR 전후 동일)

## 다음 단계
- 다음 RED 또는 세션 종료
```

## 금지

- `tests/` 수정 (동작 맞추기 위한 assert 변경 포함)
- 관측 가능한 동작·API 시그니처 변경
- skip·xfail·테스트 삭제
- Harness 전체 OCP/SRP 리팩터, 설정 외부화, JSON/CSV CLI (세션 범위 밖)
- Green이 깨진 상태에서 REFACTOR 계속 진행

## 사용자 인자

`/tdd-refactor` 뒤 텍스트가 있으면 그 영역(파싱, 단위 비교, incomplete 처리 등)을 우선 정리 대상으로 삼는다.
(예: `/tdd-refactor R1 건축 표기 파싱 헬퍼 분리`)
