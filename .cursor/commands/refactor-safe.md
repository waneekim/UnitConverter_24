# Refactor Safe — ARRR Refine (⑦ 실행)

**`/refactor-smell` 표에서 선택한 스멜 1개만** Safe Refactor 실행. Change Budget 준수, **동작·golden 포맷 불변**.

## Phase 선언 (필수)

응답 **첫 줄**에 반드시 작성:

```
Phase: refactor | Layer: entity | Track: Logic
```

- upstream: `/refactor-smell` 스멜 ID (S-01 등) · 후보 (R-A 등)
- downstream: `/refactor-smell` 재실행 또는 다음 RED 묶음

## 역할·범위

| 하는 일 | 하지 않는 일 |
|---------|----------------|
| 스멜 **1건** 구조·명명·상수화 리팩터 | 스멜 표 **2건 이상** 동시 수정 |
| Budget 내 `src/`·(필요 시) `tests/` 정리 | **기능 추가**·버그 수정 (별도 GREEN) |
| `pytest` + golden **matched** 검증 | E001~E005 emit |

## 전제

```bash
python -m pytest tests/ -v
```

- **전부 PASS** 후 시작
- `/refactor-smell`에서 **Budget ✓** 로 표시된 후보만 실행

## Change Budget (1회)

| 항목 | 한도 |
|------|------|
| 파일 | ≤ **3** |
| 클래스 | ≤ **1** |
| 메서드 | ≤ **3** |

초과 시 **이 커맨드 중단** — 스멜을 더 쪼개서 재탐지.

## Safe Refactor 원칙

| 원칙 | 내용 |
|------|------|
| **입출력 불변** | `validate_lines(grid)` 시그니처·반환 `dict` 키·값 의미 동일 |
| **예외 불변** | 새 raise·E001~E005 **emit 금지** |
| **golden 포맷** | `status` / `failed_lines` int[6] **1-index** / `error_code=none` **변경 금지** |
| **ECB** | entity → boundary/control import 금지 |
| **SSOT** | Magic Number → `src/constants.py` (리터럴 직접 삽입 금지) |
| **범위** | 스멜 1건에 해당하는 최소 diff만 |

## 절차

1. **스멜 확인** — 사용자 인자 또는 직전 `/refactor-smell` 표의 **ID 1개** (예: `S-03`)
2. **Budget 점검** — 파일·메서드 한도 내 계획
3. **리팩터** — rename · extract constant · 작은 extract method (동작 동일)
4. **`pytest tests/ -v`** — 전부 PASS
5. **golden matched** — `UPDATE_GOLDEN` **없이**:
   ```bash
   pytest tests/entity/test_d_sol_01.py -v
   ```
6. **golden diff 처리** (아래 규칙)
7. **보고** — 변경 요약 · pytest · golden matched

## golden diff 규칙

| 경우 | 조치 |
|------|------|
| **비의도** diff (포맷·인덱스·status 변경) | **롤백** → 리팩터 재설계 |
| **의도적** diff (golden 포맷 규칙 변경은 본 커맨드 범위 **밖**) | `docs/` ISS 문서화 + `UPDATE_GOLDEN=1` (별도 승인) |

본 커맨드 기본: **golden diff 없음 = matched** 기대.

## 사용자 인자

```
/refactor-safe S-03 FEET_COMPARE_EPSILON 상수화
/refactor-safe S-01 R1 상수 SSOT 정리
```

- 스멜 ID **1개** + 한 줄 설명
- 인자 없으면 직전 `/refactor-smell` **P0 1건** 또는 **R-A 후보** 적용

## 실행 예시

### Magic Number (S-03)

```python
# src/constants.py
FEET_COMPARE_EPSILON = 1e-9

# src/validate_lines.py
from constants import FEET_COMPARE_EPSILON
# abs(a - b) < FEET_COMPARE_EPSILON
```

### Mysterious Name (S-04)

- `_row_passes_d_loc_01` → `_row_passes_r1_arch_row` (호출부·정의만, 로직 동일)

## 보고 형식

```markdown
Phase: refactor | Layer: entity | Track: Logic

## 스멜
- ID: S-03 · 유형: Magic Number

## 변경 요약
- `src/constants.py`: FEET_COMPARE_EPSILON 추가
- `src/validate_lines.py`: 1e-9 → 상수 import

## Change Budget
- 파일 2 / 메서드 1 — ✓

## pytest
`python -m pytest tests/ -v` → 13 passed

## golden matched
`pytest tests/entity/test_d_sol_01.py -v` → 2 passed, UPDATE_GOLDEN 없음 — **matched**

## 커밋
- 사용자 요청 시만
```

## 금지

- 스멜 **2건 이상** 한 번에 수정
- Change Budget 초과
- 기능 추가·버그 수정·Rule 변경 (→ `/green-minimal`)
- 입출력·`failed_lines` 0-index·golden 포맷 변경 (의도적이면 ISS+UPDATE_GOLDEN 별도)
- E001~E005 raise/return
- golden `.approved.txt` **수동 편집**
- `git commit`·push (사용자 요청 시만)

## Track A (boundary)

`Phase: refactor | Layer: boundary | Track: UI` — `UnitConverter.py`만; entity import는 domain API 호출만. golden은 stdout/stderr 문자열 — 포맷 변경 시 ISS+UPDATE_GOLDEN.
