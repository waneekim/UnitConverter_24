# Refactor Smell — ARRR Refine (⑦)

**ARRR R단계(Refine = ⑦)** 전용 커맨드. **코드 스멜 탐지만** 수행한다. **수정·commit 금지.**

> downstream: `/refactor-safe` — 탐지된 후보 **1개(P0)** 만 실제 리팩터

## Phase 선언 (필수)

응답 **첫 줄**에 반드시 작성:

```
Phase: refactor | Scope: src/ tests/ | Track: Logic+UI
```

## 역할·범위

| 하는 일 | 하지 않는 일 |
|---------|----------------|
| `src/`·`tests/` **정적 분석** — 스멜 목록·우선순위 | 코드 **수정** |
| P0/P1/P2 분류 · Change Budget 적합 후보 선정 | `git commit`·push |
| `/refactor-safe` 넘길 후보 1~3개 제안 | assert·golden·동작 변경 |

## 전제 (중단 조건)

```bash
python -m pytest tests/ -v
```

- **전부 PASS** — 탐지 진행
- **1개라도 FAIL** — **즉시 중단**, 스멜 표 출력 **금지**, GREEN/fix 먼저 안내

## SSOT

| 문서 | 용도 |
|------|------|
| `.cursorrules` | ECB·R1~R4·TDD |
| `docs/PRD.md` | FR·Test ID |
| `src/constants.py` | 상수 SSOT (Magic Number 기준) |

## 스멜 유형 (탐지 대상)

| 유형 | 설명 | 흔한 위치 |
|------|------|-----------|
| **Long Method** | 한 함수가 Arrange·파싱·판정·집계를 모두 담당 | `validate_lines`, `main()` |
| **Duplicated Code** | 동일 파싱·비교·golden 포맷 반복 | `tests/` assert vs `_approval` |
| **Mysterious Name** | `_row_passes_d_loc_01`, `d_sol` 등 맥락 없는 이름 | `src/`, `tests/entity/` |
| **Magic Number** | `1e-9`, 리터럴 비율·`6` 슬롯이 상수 밖에 존재 | `src/`, `_approval.py` |
| **ECB 위반** | entity가 boundary import, E001~E005, Domain Mock | `src/` ↔ `UnitConverter.py` |
| **Feature Envy** | 행 검증이 셀 파싱 데이터를 과도하게 참조·조작 | `_row_passes_*` |

## 우선순위 (P0 / P1 / P2)

| 등급 | 기준 | 예시 |
|------|------|------|
| **P0** | ECB 위반·오동작 위험·Mom Test Rule 혼동 | Magic Number로 R1 틀림, entity→UI import |
| **P1** | 유지보수 비용·중복·다음 RED 묶음 방해 | Long Method, Duplicated Code |
| **P2** | 가독성·네이밍·미세 정리 | Mysterious Name, 주석 정리 |

## Change Budget (`/refactor-safe` 1회 한도)

| 항목 | 한도 |
|------|------|
| 파일 | ≤ **3** |
| 클래스 | ≤ **1** |
| 메서드 | ≤ **3** |

후보 제안 시 Budget **초과** 리팩터는 `/refactor-safe`에 넘기지 않음.

## 절차

1. **`pytest tests/ -v`** — FAIL 시 중단·보고만
2. **`src/`·`tests/` 스캔** — 스멜 유형별 후보 수집
3. **P0/P1/P2 표** 작성
4. **Budget 내** `/refactor-safe` 후보 **1~3개** 선정
5. **다음 안내** — P0 **1개만** 골라 `/refactor-safe` 실행

## 출력 형식

### 1. pytest 전제

```text
python -m pytest tests/ -v → N passed / M failed
```

### 2. 스멜 표

| ID | P | 유형 | 위치 (파일:라인·심볼) | 요약 | Budget |
|----|---|------|----------------------|------|--------|
| S-01 | P0 | Magic Number | `src/validate_lines.py:47` `_row_passes_d_loc_01` | `1e-9` → `constants` | 1파일·1메서드 |
| S-02 | P1 | Mysterious Name | `src/validate_lines.py:29` | `d_loc_01` → R1 행 검증 | 1파일·1메서드 |
| S-03 | P1 | Duplicated Code | `tests/entity/test_d_loc_01.py` vs `test_d_sol_01.py` | 동일 grid·assert | 2파일·2메서드 |

### 3. `/refactor-safe` 후보 (1~3개)

| 후보 | 스멜 ID | 제안 리팩터 | Budget |
|------|---------|-------------|--------|
| **R-A** | S-01 | `EPSILON` → `src/constants.py` | ✓ |
| R-B | S-02 | `_row_passes_d_loc_01` → `_row_passes_r1_arch` | ✓ |
| R-C | S-03 | golden 테스트만 유지, assert 중복 제거 논의 | ✗ tests 변경 — 별도 |

### 4. 다음 안내 (필수)

```markdown
P0가 있으면 **1개만** 선택하여 `/refactor-safe` 실행.
예: `/refactor-safe S-01 EPSILON 상수화`

P0 없으면 P1 1개 — Budget 준수.
본 커맨드에서는 **코드 수정·commit 하지 않음**.
```

## 보고 템플릿 (전체 응답 골격)

```markdown
Phase: refactor | Scope: src/ tests/ | Track: Logic+UI

## pytest 전제
(passed / 중단)

## 스멜 표
(표)

## /refactor-safe 후보
(1~3개)

## 다음 단계
P0 1개 → `/refactor-safe`
```

## 금지

- `src/`·`tests/`·golden **코드 수정**
- `git commit`·push·PR
- 스멜 탐지 없이 리팩터 실행
- pytest FAIL 상태에서 스멜 표 작성
- Change Budget 초과 후보를 `/refactor-safe`에 **단일 호출**로 넘기기

## 사용자 인자

`/refactor-smell` 뒤 텍스트가 있으면 **스캔 범위**를 우선한다.
(예: `/refactor-smell src/validate_lines.py` · `/refactor-smell D-UNIT-01 준비`)

**Track**: `Logic+UI` — `src/validate_lines.py`(Logic) + `UnitConverter.py`(UI boundary) 모두 스캔, ECB 위반 우선 P0.
