# RED Test Plan — ARRR Ask (RED ③)

**ARRR A단계(Ask = RED ③)** 전용 커맨드. **C2C 설계표·테스트 플랜만** 작성한다. 코드·테스트 파일은 만들지 않는다.

## Phase 선언 (필수)

응답 **첫 줄**에 반드시 작성 (3항목 한 줄):

```
Phase: red | Layer: entity | Track: Logic
```

- **Layer**: `entity`(도메인·Rule 검증) | `boundary`(UI·I/O 경계)
- **Track**: `Logic`(Track B — `validate_lines` 등) | `UI`(Track A — boundary 시 Layer만 `boundary`로 바꿔 동일 커맨드 재사용)

## SSOT (읽기 순서)

1. `.cursorrules` — R1~R4, API, TDD 금지 사항
2. `docs/PRD.md` — FR(Functional Requirement) 인용 (**없으면** `Report/session-workbook.md` 성공 기준·R-G-I-O로 FR 대체)
3. `.cursor/commands/tdd-red.md` — AAA·pytest·RED 보고 관례

## 자동 추출 (추가 입력 없음)

`/red-test-plan` 만으로 동작. 아래를 **채팅 맥락 + SSOT**에서 자동 도출:

| 항목 | 추출 소스 |
|------|-----------|
| 세션 주제 | 워크북 1) 주제 문장 또는 PRD 제목 |
| 대상 API | `.cursorrules` API 계약 (`validate_lines` 등) |
| Test ID | `{모듈약어}-R{n}-{seq}` — 예: `VL-R1-001`, `VL-R2-002` |
| Mom Test 증거 | session-workbook 성공 기준 #1~3 |
| RED 묶음 | Rule·FR 단위 1묶음 (한 `/red-skeleton` 호출 범위) |

## 역할·범위

- **하는 일**: C2C 표, Track B 표, 테스트 플랜, ECB·Mock 점검 **문서 출력**
- **하지 않는 일**: `tests/`·`src/` 파일 생성·수정, pytest 실행, GREEN/REFACTOR

## 출력 4블록 (표 형식, 필수)

응답 본문에 아래 **4개 섹션을 순서대로** 표로 작성한다.

### 1. C2C (Rule1~3)

PRD FR → To-Do 1개 → Test ID Given/When/Then 체인.

| C2C Rule | 내용 |
|----------|------|
| Rule1 | PRD **FR 인용**(문장·ID) — SSOT에서 그대로 인용 |
| Rule2 | FR당 **To-Do 1개** — 검증할 행동·판정 한 줄 |
| Rule3 | To-Do당 **Test ID + Given/When/Then** — RED assert 기대까지 |

**C2C 설계표 예시:**

| FR (PRD 인용) | To-Do (1개) | Test ID | Given | When | Then (RED 기대) |
|---------------|-------------|---------|-------|------|-----------------|
| FR-01 / R1: `3'-6"` = 3.75 ft | 건축 표기 단독 행은 pass | VL-R1-001 | `grid=[[ARCH_3FT_6IN]]` | `validate_lines(grid)` | `status==pass`, `failed_lines==[]` |
| FR-01 / R1: 3.5 ≠ 3.75 | `feet:3.5` 오환산 행 fail | VL-R1-002 | `grid=[[ARCH_3FT_6IN,"feet:3.5"]]` | `validate_lines(grid)` | `status==fail`, `failed_lines==[0]` |

### 2. Track B 표 (Logic Track)

`Track: Logic` 일 때 작성. `Track: UI` + `Layer: boundary`이면 동일 열에 UI 대상(핸들러·포맷터)으로 치환.

| Test ID | 대상 함수 | Given → Then | Invariant | Expected RED Failure |
|---------|-----------|--------------|-----------|----------------------|
| VL-R1-001 | `validate_lines` | `[[ARCH_3FT_6IN]]` → pass | R1 파싱 정확도 | `TypeError` 또는 `status` 불일치 (스텁) |
| VL-R1-002 | `validate_lines` | arch + `feet:3.5` → fail `[0]` | 3.75 ≠ 3.5 | `status!=fail` 또는 `failed_lines` 오류 |
| VL-R2-001 | `validate_lines` | `feet:3` + `yard:3` → fail | meter 기준 일관성 | 혼동 미검출 |
| VL-R4-001 | `validate_lines` | 빈 셀 → incomplete | incomplete 시 `failed_lines==[]` | `status!=incomplete` |

### 3. 테스트 플랜

| 항목 | 값 |
|------|-----|
| 파일 경로 | `tests/test_validate_lines.py` (신규 시에도 **본 커맨드에서는 생성하지 않음**) |
| 함수명 | C2C Test ID와 1:1 — 예: `test_vl_r1_001_arch_notation_passes` |
| conftest 픽스처 | `ARCH_3FT_6IN`, `ARCH_9FT_2IN`, `STEEL_DIMS_8` (`tests/conftest.py` 또는 모듈 상수) |
| pytest 명령 | `pytest tests/test_validate_lines.py -v` |
| RED 묶음 범위 | 이번 플랜: `VL-R1-001`~`VL-R1-002` (또는 FR 단위 전체) — `/red-skeleton`에 전달 |

### 4. ECB·Mock 점검

| 점검 항목 | Logic Track (`entity`) | boundary Track (`UI`) |
|-----------|------------------------|------------------------|
| Domain Mock | **금지** — 실제 `grid`·문자열 입력만 | UI 드라이버 Mock만 허용 (도메인 로직 Mock 금지) |
| E001~E005 emit | **금지** — 에러 코드 emit·assert 없음 | UI 에러 표시만 (도메인 E001~E005 직접 emit 금지) |
| ECB 경계 | 순수 Rule 판정 (`pass`/`fail`/`incomplete`) | I/O 형식·표시 경계만 |
| 스텁 의존 | `validate_lines` 미구현 RED 허용 | CLI/핸들러 미연결 RED 허용 |

**점검 결과 표:**

| Test ID | Domain Mock | E001~E005 | 판정 |
|---------|-------------|-----------|------|
| VL-R1-00x | 없음 ✓ | emit 없음 ✓ | Logic Track 적합 |
| … | … | … | … |

## 보고 형식 (전체 응답 골격)

```markdown
Phase: red | Layer: entity | Track: Logic

## 세션
- 주제: (자동 추출)
- API: validate_lines(grid) → {status, failed_lines}

## 1. C2C (Rule1~3)
(표)

## 2. Track B
(표)

## 3. 테스트 플랜
(표)

## 4. ECB·Mock 점검
(표)

/red-skeleton 으로 넘길 준비됐다
```

## 금지

- `src/`·`tests/`·`UnitConverter.py` **파일 생성·수정**
- GREEN / REFACTOR 제안·구현
- `@pytest.mark.skip`, `xfail`, assert 완화 전제
- Domain Mock, E001~E005 emit이 포함된 플랜
- C2C·Track B·플랜·ECB **4블록 생략**

## 다음 단계

- 테스트 **골격·코드** 작성: `/red-skeleton` (별도 커맨드)
- 실패 테스트 구현·실행: `/tdd-red`

## 사용자 인자

`/red-test-plan` 뒤 텍스트가 있으면 FR·Rule·RED 묶음 범위를 **우선** 적용한다.
(예: `/red-test-plan R2 yard feet 혼동만`)

**Track A (boundary)**: `Layer: boundary`로 선언만 바꾸면 본 커맨드·4블록 구조를 UI Track에 그대로 재사용한다.
