# PRD — UnitConverter_24

**Product Requirements Document**

| 항목 | 내용 |
|------|------|
| 프로젝트 | UnitConverter_24 |
| 버전 | 0.1 (Mom Test · TDD RED 기준) |
| 작성일 | 2026-06-11 |
| SSOT 순위 | 본 문서 → `.cursorrules` → `Report/session-workbook.md` |
| 근거 | [mom-test-report.md](../Report/mom-test-report.md) · [session-workbook.md](../Report/session-workbook.md) · [mom-test-prompt.md](../Prompting/mom-test-prompt.md) |

---

## 1. 문제 정의

### 1.1 진짜 문제 (한 문장)

도면에 **피트·인치**로 나온 치수를 발주·견적용 단위(미터·소수 feet 등)로 바꿀 때, **소수 feet 환산 착각·단위 혼동·치수별 반복 입력** 때문에 시간이 새고, 잘못된 수량 발주로 **비용**이 발생한다.

### 1.2 표면 문제 (범위 밖)

| 표면 정의 | 왜 범위 밖인가 |
|-----------|----------------|
| "건축업자용 단위 변환 CLI 프로그램을 만든다" | 사용자는 앱이 아니라 **판정 오류·반복 비용** 해소를 원함 |
| "피트·인치 지원 변환기 UI/앱" | 솔루션 포장 — 이번 범위는 **Rule · Command · Test Loop** |
| JSON/CSV 출력·동적 단위 등록·OCP 대규모 리팩터 | Mom Test·세션 범위 밖 |

### 1.3 Mom Test 증거

| # | 인용 | 손실 |
|---|------|------|
| E1 | *"3피트 6인치는 3.5피트가 아니다"* — `feet:3.5` 오입력 | 발주서 수정 **15분** (지난 화요일) |
| E2 | *"긴급 재주문하면서 배송비 **3만 원**"* — 야드/피트 착각 | 비용 (지난달) |
| E3 | *"치수 **8개**를 엑셀에 일일이… **10분**"* — CLI 8회 실행 부담 | 시간 (지난주 금요일) |

---

## 2. 사용자·목표

### 2.1 페르소나

건축 현장·사무실에서 도면(피트·인치) 치수를 발주서·견적서(미터·소수 feet)로 변환하는 **건축업자**.

- **현장:** 스마트폰 계산기, 줄자, 메모
- **사무실:** 엑셀 수식 일괄 변환
- **CLI:** `UnitConverter.py` — 거의 미사용 (콜론 형식, 1회 실행, inch·건축 표기 미지원)

### 2.2 목표 (측정 가능)

| 목표 | Mom Test 연결 |
|------|----------------|
| `3'-6"` → **3.75 feet** 정확 판정, `feet:3.5` 오환산 **fail** | E1 · 15분 |
| meter / feet / yard **일관** 변환, 혼동 **fail** | E2 · 3만 원 |
| 치수 N개 **일괄** 검증·변환, 1개 오류 시 행 인덱스 **fail** | E3 · 10분 |

---

## 3. 도메인 Rule (R1~R4)

| Rule | 정의 | 예시 |
|------|------|------|
| **R1** | `X'-Y"` → 소수 feet = X + Y/12 | `3'-6"` = **3.75** (3.5 아님) |
| **R2** | meter 기준 feet↔yard 비율 고정; 동일 수치 feet/yard 혼재·비율 불일치는 fail | `feet:3` + `yard:3` 동일 행 → fail |
| **R3** | 견적용 출력 소수 자릿수·반올림 (선택) | 소수 8자리 → 견적용 2자리 |
| **R4** | `단위:값`·건축 표기·그리드 형식 검증; 콜론 누락·알 수 없는 단위·빈 셀 처리 | `meter2.5` → fail; `""` → incomplete |

### 3.1 변환 상수 (기존 CLI 기준)

| 단위 | meter 환산 |
|------|------------|
| feet | `value / 3.28084` |
| yard | `value / 1.09361` |
| meter | `value` (기준) |

---

## 4. Functional Requirements (FR)

### 4.1 Logic Track — 치수·단위 (entity)

| FR ID | RED 묶음 | Rule | 요구사항 (인용 가능 문장) | Mom Test |
|-------|----------|------|---------------------------|----------|
| **FR-LOC-01** | D-LOC-01 | R1 | `3'-6"` 입력 시 **3.75 feet**로 파싱·판정한다. 동일 행에 `feet:3.5`가 있으면 **fail**, `failed_lines`에 행 인덱스를 반환한다. | E1 |
| **FR-LOC-02** | D-LOC-02 | R1 | 건축 표기 `X'-Y"` 단독 행은 검증 **pass**한다. | E1 |
| **FR-UNIT-01** | D-UNIT-01 | R2 | 동일 행에 feet·yard **동일 수치**가 있으면 단위 혼동으로 **fail**한다. | E2 |
| **FR-UNIT-02** | D-UNIT-02 | R2 | meter 기준 feet↔yard 비율이 불일치하면 **fail**한다. | E2 |
| **FR-BATCH-01** | D-BATCH-01 | R1+R2 | 철골 치수 **8개** 그리드를 일괄 검증한다. 전부 정확하면 **pass**; 1개 오환산 시 **fail** 및 해당 행 인덱스. | E3 |
| **FR-FMT-01** | D-FMT-01 | R4 | 알 수 없는 단위·콜론 누락 입력은 **fail**한다. | 인터뷰 2분 손실 |
| **FR-FMT-02** | D-FMT-02 | R4 | 빈 셀이 있으면 **incomplete**이며 `failed_lines`는 빈 리스트이다. | — |
| **FR-OUT-01** | D-OUT-01 | R3 | *(선택)* 견적용 반올림·소수 자릿수 Rule을 적용한다. | 3~4분 손실 |
| **FR-FMT-03** | D-FMT-03 | R1 | 분수 인치 단독 표기 `4½"`, `2¼"`를 소수 feet로 파싱한다 (`N½"` → `N.5/R1_DIVISOR`). | R2 증거 1 · 15분 |

### 4.2 Boundary Track — CLI 입력 (UI)

| FR ID | RED 묶음 | Rule | 요구사항 | Mom Test |
|-------|----------|------|----------|----------|
| **FR-IN-01** | U-IN-01 | R4 | `단위:값` 형식이 아니면(콜론 누락) **명확한 오류 메시지**를 표시하고 종료한다. | 콜론 누락 2분 |
| **FR-IN-02** | U-IN-02 | R4 | 알 수 없는 단위면 **명확한 오류 메시지**를 표시한다. | — |
| **FR-OUT-02** | U-OUT-01 | R3 | CLI 출력에 견적용 **2자리** 반올림 값을 표시한다. | R2 견적 3~4분 |
| **FR-BATCH-02** | U-BATCH-01 | R4 | stdin **다중 줄** 1회 실행으로 N치수 변환한다. | R2 증거 3 · 8분 |
| **FR-IN-03** | U-HINT-01 | R4 | 프롬프트·오류에 **한국어 입력 예시**를 표시한다. | R2 cmd 10분+ |

---

## 5. API·Command 계약

### 5.1 `validate_lines` (현재 세션 — Logic)

```text
validate_lines(grid: list[list[str]]) -> dict
```

| 필드 | 타입 | 설명 |
|------|------|------|
| `status` | `"pass"` \| `"fail"` \| `"incomplete"` | 전체 판정 |
| `failed_lines` | `list[int]` | fail 시 0-based 행 인덱스; incomplete 시 `[]` |

- **구현:** `src/validate_lines.py`
- **테스트:** `tests/test_validate_lines.py`

### 5.2 `convert_length` / `convert_lengths` (후속 — Command)

| API | 입력 | 출력 |
|-----|------|------|
| `convert_length(spec: str)` | `"3'-6""`, `"meter:2.5"` 등 | `ConversionResult`: 입력 표기, 소수 feet, meter/feet/yard, (선택) 반올림 |
| `convert_lengths(specs: list[str])` | 치수 목록 (최대 8+ fixture) | `list[ConversionResult]` |

### 5.3 `UnitConverter.py` (Boundary)

- `process_input(spec)` — 단일 치수 → 견적용 2자리 출력 3줄
- `process_batch_input(specs)` — N치수 일괄 → `convert_lengths` 위임
- `main()` — 다중 줄 입력(빈 줄 종료) 또는 단일 줄
- FR-IN-01/02/03 · FR-OUT-02 · FR-BATCH-02 경계 검증

---

## 6. Test ID 매핑

| Test ID | FR | RED 묶음 | 검증 요약 |
|---------|-----|----------|-----------|
| VL-R1-001 | FR-LOC-02 | D-LOC-01 | `[[ARCH_3FT_6IN]]` → pass |
| VL-R1-002 | FR-LOC-01 | D-LOC-01 | `[[ARCH_3FT_6IN,"feet:3.5"]]` → fail `[0]` |
| VL-R2-001 | FR-UNIT-01 | D-UNIT-01 | `feet:3` + `yard:3` → fail |
| VL-R2-002 | FR-UNIT-02 | D-UNIT-02 | meter/feet/yard 비율 불일치 → fail |
| VL-R4-001 | FR-FMT-01 | D-FMT-01 | `foo:1.0` → fail |
| VL-R4-002 | FR-FMT-01 | D-FMT-01 | `meter2.5` → fail |
| VL-R4-003 | FR-FMT-02 | D-FMT-02 | 빈 셀 → incomplete |
| VL-R3-001 | FR-BATCH-01 | D-BATCH-01 | `STEEL_DIMS_8` → pass |
| VL-R3-002 | FR-BATCH-01 | D-BATCH-01 | 8개 중 row 4 오환산 → fail `[4]` |
| UI-R4-001 | FR-IN-01 | U-IN-01 | `meter2.5` stdin → 오류 메시지 |
| UI-R4-002 | FR-IN-02 | U-IN-02 | `foo:1.0` stdin → unknown unit |
| CL-R5-001 | FR-FMT-03 | D-FMT-03 | `4½"` → `feet_decimal=0.5625` |
| CL-R5-002 | FR-FMT-03 | D-FMT-03 | `2¼"` → `feet_decimal=0.28125` |
| UI-R5-001 | FR-OUT-02 | U-OUT-01 | `3'-6"` → 견적용 2자리 출력 |
| UI-BATCH-001 | FR-BATCH-02 | U-BATCH-01 | STEEL_DIMS_8 8줄 → 24줄 출력 |
| UI-HINT-001 | FR-IN-03 | U-HINT-01 | 오류 메시지 한국어 예시 |
| UI-HINT-002 | FR-IN-03 | U-HINT-01 | 시작 프롬프트 한국어 |

### 6.1 Fixture (Mom Test)

| 상수 | 값 | 용도 |
|------|-----|------|
| `ARCH_3FT_6IN` | `'3\'-6"'` | FR-LOC-01/02 |
| `ARCH_9FT_2IN` | `'9\'-2"'` | 일괄 fixture |
| `ARCH_4HALF_IN` | `'4½"'` | FR-FMT-03 |
| `ARCH_2QUARTER_IN` | `'2¼"'` | FR-FMT-03 |
| `STEEL_DIMS_8` | 8행 그리드 | FR-BATCH-01 |

---

## 7. 성공 기준·비기능

### 7.1 성공 기준 (Acceptance)

| # | 기준 | pytest 근거 |
|---|------|-------------|
| AC-1 | `3'-6"` = 3.75 ft; `feet:3.5` fail | `test_arch_notation_*`, `test_feet_3_5_*` |
| AC-2 | yard/feet 혼동·비율 불일치 fail | `test_feet_and_yard_*`, `test_meter_feet_yard_*` |
| AC-3 | 8치수 일괄 pass; 1 오환산 fail+인덱스 | `test_eight_steel_dims_*` |
| AC-4 | 형식 오류 fail; 빈 셀 incomplete | `test_unknown_unit_*`, `test_missing_colon_*`, `test_empty_cell_*` |

### 7.2 TDD·품질

- 사이클: **RED → GREEN → REFACTOR**
- RED: `tests/`만 수정; assert 완화·skip·xfail 금지
- `/red-test-plan` → `/red-skeleton` → `/tdd-red` 워크플로

### 7.3 비기능 (이번 범위)

| 항목 | 결정 |
|------|------|
| 성능 | 8치수 그리드 즉시 응답 (CLI 대화형) |
| 설정 외부화 | 범위 밖 |
| 현장 스마트폰 UX | 후속 |
| git commit | 사용자 요청 시만 |

---

## 8. 로드맵

| 단계 | 산출물 | 상태 |
|------|--------|------|
| 1 | `.cursorrules`, TDD Command, RED 테스트 9개 | **완료** (RED) |
| 2 | `validate_lines` GREEN (R1~R4) | 대기 |
| 3 | REFACTOR — Green 유지 정리 | 대기 |
| 4 | `convert_length` / `convert_lengths` Command | 후속 |
| 5 | `UnitConverter.py` FR-IN-01/02 (boundary) | 후속 |
| 6 | FR-OUT-01 견적 반올림 (R3) | **완료** |
| 7 | Mom Test R2 — D-FMT-03 · U-OUT/BATCH/HINT | **완료** |

---

## 9. 관련 문서

| 문서 | 경로 |
|------|------|
| Mom Test R2 보고서 | [Report/mom-test-report-02.md](../Report/mom-test-report-02.md) |
| Mom Test 보고서 | [Report/mom-test-report.md](../Report/mom-test-report.md) |
| ARRR R2 플랜 | [ARRR-mom-test-r2.md](./ARRR-mom-test-r2.md) |
| 세션 워크북 | [Report/session-workbook.md](../Report/session-workbook.md) |
| 세션 보고서 | [Report/01.REPORT.md](../Report/01.REPORT.md) |
| 인터뷰 프롬프트 | [Prompting/mom-test-prompt.md](../Prompting/mom-test-prompt.md) |
| Transcript | [Prompting/01.Export-Transcript.md](../Prompting/01.Export-Transcript.md) |
| 프로젝트 Rule | [.cursorrules](../.cursorrules) |

---

*본 문서는 docs/PRD.md — UnitConverter_24 Product Requirements Document (Mom Test · validate_lines TDD 기준)입니다.*
