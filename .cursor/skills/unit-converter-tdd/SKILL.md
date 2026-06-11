---
name: unit-converter-tdd
description: >-
  UnitConverter_24 Dual-Track TDD workflow (ARRR, C2C, RED/GREEN/REFACTOR).
  Use when Phase is red, green, or refactor; when invoking /red-test-plan,
  /red-skeleton, /green-minimal, /golden-master, /refactor-smell, /refactor-safe;
  or when the user mentions TDD, RED, GREEN, REFACTOR, Dual-Track, C2C,
  pytest.fail, validate_lines, Mom Test, or ARRR.
disable-model-invocation: true
---

# UnitConverter TDD Skill

Mom Test 기반 **UnitConverter_24** TDD·ARRR 워크플로. 명시 호출·Command 실행 시에만 적용.

## SSOT (읽기 순서)

1. `.cursorrules` — R1~R4, API, ECB, TDD 금지
2. `docs/PRD.md` — FR, RED 묶음, Test ID
3. `.cursor/commands/*.md` — 해당 Phase Command 본문

---

## 1. ARRR ↔ TDD 매핑

| ARRR | TDD | 단계 | Command 예 |
|------|-----|------|------------|
| **Ask** | RED ③ | C2C 설계·플랜 (코드 없음) | `/red-test-plan` |
| **Ask** | RED ④ | `pytest.fail` 스켈레톤 | `/red-skeleton` |
| **Ask** | RED | assert 실패 테스트 | `/tdd-red` |
| **Respond** | GREEN | RED 1묶음 최소 구현 | `/green-minimal` |
| **Respond** | GREEN | Golden Master | `/golden-master` |
| **Refine** | REFACTOR ⑦ | 스멜 탐지 (수정 없음) | `/refactor-smell` |
| **Refine** | REFACTOR ⑦ | Safe Refactor 1건 | `/refactor-safe` |

---

## 2. Phase 선언 (응답 첫 줄)

| Phase | 선언 형식 |
|-------|-----------|
| RED 설계 | `Phase: red | Layer: entity | Track: Logic` |
| RED (legacy) | `Phase: RED` |
| GREEN | `Phase: green | Layer: entity | Track: Logic` |
| GREEN (legacy) | `Phase: GREEN` |
| REFACTOR 탐지 | `Phase: refactor | Scope: src/ tests/ | Track: Logic+UI` |
| REFACTOR 실행 | `Phase: refactor | Layer: entity | Track: Logic` |
| EXPORT | `Phase: EXPORT` |

- **Layer**: `entity` (도메인) | `boundary` (UI·I/O)
- **Track**: `Logic` (Track B) | `UI` (Track A)

---

## 3. C2C Rule 1~3 (요약)

| Rule | 내용 |
|------|------|
| **Rule1** | PRD **FR 인용** (ID·문장) — `docs/PRD.md` |
| **Rule2** | FR당 **To-Do 1개** — 검증 행동·판정 한 줄 |
| **Rule3** | To-Do당 **Test ID + Given/When/Then** — RED assert·golden 기대까지 |

Test ID 패턴: `VL-R{n}-{seq}` (예: `VL-R1-001`). RED 묶음: `D-LOC-01`, `D-UNIT-01` 등.

---

## 4. RED 절대 금지

- `src/`·`entity/`·`UnitConverter.py` **구현 변경** (RED는 `tests/`만)
- `@pytest.mark.skip`, `xfail`, 테스트 삭제
- **assert 완화** (`==` → `in`, 기대값 느슨화)
- **Logic Track Domain Mock** — 실제 `grid`·문자열만
- **E001~E005** emit·assert
- RED 없이 GREEN·구현 선제
- 의도하지 않은 실패 없이 GREEN 진행

---

## 5. GREEN 규칙

- **1커밋 = 1 RED 묶음** (commit은 사용자 요청 시만)
- `src/` **최소 구현** — 이번 묶음 Test ID만
- **constants SSOT**: `src/constants.py` — Magic Number·비율·epsilon
- `tests/fixtures.py` — 픽스처 문자열 (테스트 전용; `src/` import 금지)
- `pytest.fail` → `validate_lines` + assert 교체
- 이번 묶음 **외** Test ID 동시 해결 금지
- ECB: `pass`/`fail`/`incomplete`만; boundary import 금지

---

## 6. REFACTOR 규칙

### Change Budget (`/refactor-safe` 1회)

| 항목 | 한도 |
|------|------|
| 파일 | ≤ 3 |
| 클래스 | ≤ 1 |
| 메서드 | ≤ 3 |

### Golden 유지

- 입출력·`failed_lines` API **0-based** 불변
- Golden 파일: `failed_lines` **int[6] 1-index**, `error_code=none`
- 완료 후: `pytest tests/ -v` + `pytest tests/entity/test_d_sol_01.py -v` (**UPDATE_GOLDEN 없음**)
- golden diff 비의도 → **롤백**; 의도 → `docs/` ISS + `UPDATE_GOLDEN=1`

### 금지

- 기능 추가·버그 수정 (→ `/green-minimal`)
- 스멜 2건 이상 동시 수정
- golden `.approved.txt` 수동 편집

---

## 7. Track A (UI) vs Track B (Logic)

| | Track A — UI (`boundary`) | Track B — Logic (`entity`) |
|---|---------------------------|----------------------------|
| **Layer** | `boundary` | `entity` |
| **Track** | `UI` | `Logic` |
| **대상** | `UnitConverter.py`, stdin/stdout | `src/validate_lines.py` |
| **검증** | 오류 메시지·입력 형식 | `validate_lines(grid)` 판정 |
| **FR 예** | FR-IN-01, U-IN-01 | FR-LOC-01, D-LOC-01 |
| **Mock** | UI 드라이버만 | **Domain Mock 금지** |
| **ECB** | I/O 경계만 | E001~E005 emit 금지 |
| **Golden** | stdout/stderr 문자열 | `status`/`failed_lines`/`error_code` |

동일 Command에서 **Layer만** `boundary`로 바꿔 Track A 재사용.

---

## 8. Command 체인

```
/red-test-plan     → docs: C2C·플랜 (코드 없음)
/red-skeleton      → tests: pytest.fail 스켈레톤
/tdd-red           → tests: assert 실패 테스트
/green-minimal     → src: RED 1묶음 최소 구현
/golden-master     → tests/golden: Approval Test
/refactor-smell    → 탐지만 (수정 금지)
/refactor-safe     → 스멜 1건 Safe Refactor
```

보조: `/tdd-green`, `/tdd-refactor`, `/export-session`

**docs 최종 산출물**: `docs/PRD.md`, `docs/D-LOC-01-*.md`  
**tests 작업 소스**: `tests/entity/`, `tests/fixtures.py`, `tests/_approval.py`

---

## 9. pytest 명령 패턴

```bash
# 전체 회귀 (REFACTOR·GREEN 전제)
python -m pytest tests/ -v

# RED 묶음 (entity)
pytest tests/entity/test_d_loc_01.py -v
pytest tests/entity/test_d_loc_01.py::test_vl_r1_001_arch_notation_3ft_6in_passes -v

# Golden 생성 (1회)
UPDATE_GOLDEN=1 pytest tests/entity/test_d_sol_01.py -v

# Golden matched 확인
pytest tests/entity/test_d_sol_01.py -v

# Logic 전체
pytest tests/test_validate_lines.py -v
```

`pyproject.toml`: `pythonpath = ["src", "tests"]`

---

## 10. 완료 보고 형식

### RED (`/red-test-plan`)

```markdown
Phase: red | Layer: entity | Track: Logic
## 1. C2C · 2. Track B · 3. 테스트 플랜 · 4. ECB·Mock
/red-skeleton 으로 넘길 준비됐다
```

### GREEN (`/green-minimal`)

```markdown
Phase: green | Layer: entity | Track: Logic
## PASS Test ID · 변경 파일 · pytest · 다음 단계
```

### Golden (`/golden-master`)

```markdown
Phase: green | Layer: entity | Track: Logic
## golden 경로 · matched · diff 요약
```

### REFACTOR smell (`/refactor-smell`)

```markdown
Phase: refactor | Scope: src/ tests/ | Track: Logic+UI
## pytest 전제 · 스멜 표 · /refactor-safe 후보 · P0 1개 선택 안내
```

### REFACTOR safe (`/refactor-safe`)

```markdown
Phase: refactor | Layer: entity | Track: Logic
## 스멜 ID · 변경 요약 · Budget · pytest · golden matched
```

---

## 도메인 Quick Reference

| Rule | 요약 |
|------|------|
| R1 | `X'-Y"` → 소수 feet; `3'-6"` = 3.75, `feet:3.5` fail |
| R2 | meter 기준 feet↔yard 일관; 혼동 fail |
| R3 | 견적 반올림 (선택) |
| R4 | 형식·빈 셀 → fail/incomplete |

API: `validate_lines(grid) -> {"status", "failed_lines"}`

---

## 언어·Git

- 응답 **한국어**
- `git commit`·push·PR — **사용자 명시 요청 시만**
