---
name: unit-converter-docs
description: >-
  UnitConverter Report·Transcript Export SSOT. Use for Report Export, Transcript,
  /export-session, Phase repeat, ARRR 1사이클 완료 보고, 세션 N 보고서.
  Creates Report/NN.REPORT.md and Prompting/NN.Export-Transcript.md pairs.
---

# unit-converter-docs — Report & Transcript Export

UnitConverter_24 프로젝트의 **세션 보고서·Transcript**를 SSOT 형식으로 생성·갱신한다.

## SSOT 경로

| 종류 | 패턴 | 예시 |
|------|------|------|
| Report | `Report/{NN}.REPORT.md` | `Report/05.REPORT.md` |
| Transcript | `Prompting/{NN}.Export-Transcript.md` | `Prompting/05.Export-Transcript.md` |

- `NN` = 2자리 zero-pad (`01`, `02`, …)
- `Report/`, `Prompting/` 각각 `^\d{2}\.` 접두 파일만 번호 산정
- `session-workbook.md`, `mom-test-report.md` 등 `NN.` 없는 파일은 **제외**
- Report·Transcript는 **항상 동일 NN** 쌍

## 트리거

- Report Export, Transcript 작성
- `/export-session` Command
- `Phase: repeat` (ARRR 1사이클 완료)
- ARRR 1사이클 완료 보고, 세션 N 보고서

## /export-session 연동

Export 요청 시 **unit-converter-docs Skill 로드 후 checklist 수행**.

1. [phase-checklist.md](phase-checklist.md) 공통 + 해당 Phase 섹션 열기
2. 아래 워크플로 Step A~F 순서 실행
3. checklist 항목 전부 충족 후 완료 보고

Command 정의: [export-session.md](../../commands/export-session.md)

## 금지

| 금지 | 이유 |
|------|------|
| git commit 임의 실행 | 사용자 요청 시만 |
| `UPDATE_GOLDEN` 임의 실행 | golden 갱신은 명시적 승인·워크플로만 |
| 채팅·터미널에 없는 pytest 결과 기재 | SSOT 신뢰성 |

pytest는 Export 직전 `python -m pytest tests/ -v` 실행 가능. **실행하지 않았으면** Report에 `미실행` 또는 생략.

## 보조 파일

| 파일 | 용도 |
|------|------|
| [report-template.md](report-template.md) | Report 본문 구조 |
| [transcript-template.md](transcript-template.md) | Transcript User/Cursor 블록 |
| [phase-checklist.md](phase-checklist.md) | Phase별 Export 체크리스트 |

---

## 워크플로

### Step A — 입력 수집

다음을 수집한다. 없으면 `미확인` / `미실행`으로 명시.

| 입력 | 수집 방법 |
|------|-----------|
| git status | `git status --short` |
| pytest | 채팅·터미널 기존 출력, 또는 Export 직전 `python -m pytest tests/ -v` |
| Phase | `RED` / `GREEN` / `REFACTOR` / `repeat` / `EXPORT` |
| Test ID | `D-LOC-01`, `VL-R1-001` 등 (`docs/PRD.md`) |
| Command | `/tdd-red`, `/export-session` 등 |

세션 대화·변경 파일·도메인 Rule(R1~R4) 맥락도 함께 정리.

### Step B — NN 결정

```
NN = max(Report 폴더 NN, Prompting 폴더 NN) + 1
```

구현:

1. `Report/`에서 `^\d{2}\.` 매칭 파일의 숫자 최대값
2. `Prompting/`에서 동일
3. `max(report_max, prompting_max) + 1` → 2자리 문자열

예: 최대 `01` → 다음 `02`.

### Step C — Report 작성

1. [report-template.md](report-template.md) 기반
2. Phase별 STEP 강조:

| Phase | Report에 반드시 포함 |
|-------|----------------------|
| **RED** | 실패 테스트 목록, `src/` 미수정, pytest failed |
| **GREEN** | 최소 구현 파일, pytest passed |
| **REFACTOR** | smell·변경 요약, Green 유지 |
| **repeat** | RED→GREEN→(Golden)→REFACTOR 한 사이클 타임라인 |

3. 저장: `Report/{NN}.REPORT.md`

### Step D — Transcript 작성

1. [transcript-template.md](transcript-template.md) 기반
2. 헤더:
   - `_Exported on {YYYY-MM-DD} from Cursor_`
   - `_Source: {uuid}` — `agent-transcripts/*.jsonl` 또는 세션 메타에서 확인 가능 시
3. 본문: **User** / **Cursor** 블록으로 대화 턴 정리 (요약 허용, pytest는 실제만)
4. 저장: `Prompting/{NN}.Export-Transcript.md`

### Step E — README 문서 표 갱신

`README.md`에 **문서 인덱스 표**가 있으면 새 행 추가. 없으면 아래 표를 `## 문서 (Report / Prompting)` 섹션으로 추가.

```markdown
## 문서 (Report / Prompting)

| NN | Report | Transcript | Phase | Test ID | 날짜 |
|----|--------|------------|-------|---------|------|
| {NN} | [Report/{NN}.REPORT.md](Report/{NN}.REPORT.md) | [Prompting/{NN}.Export-Transcript.md](Prompting/{NN}.Export-Transcript.md) | {Phase} | {Test ID} | {YYYY-MM-DD} |
```

기존 행은 유지, 최신 `NN`만 추가.

### Step F — 완료 보고

응답에 **생성 경로 2개**를 반드시 포함:

```
Report/NN.REPORT.md
Prompting/NN.Export-Transcript.md
```

추가: Phase, Test ID, pytest(실제만), 다음 단계 1~2줄.

응답 첫 줄 (Export 시):

```
Phase: EXPORT
```

---

## 도메인 참고 (Report 작성 시)

| Rule | Mom Test SSOT |
|------|----------------|
| R1 | `3'-6"` = **3.75** feet (`Y/8`, `R1_ARCH_INCH_DIVISOR=8`) — `feet:3.5`는 fail |
| R2 | meter 기준 `3.28084` / `1.09361`, 혼동·비율 불일치 → fail |
| R4 | `단위:값`, 건축 표기, 빈 셀 → incomplete |

API: `validate_lines(grid)` — `failed_lines`는 0-based; golden 출력은 1-index `int[6]` 별도.

## 관련 경로

| 경로 | 역할 |
|------|------|
| `docs/PRD.md` | FR, RED 묶음, Test ID |
| `.cursor/commands/export-session.md` | `/export-session` |
| `.cursor/skills/unit-converter-tdd/SKILL.md` | ARRR·TDD Command 체인 |
| `Report/session-workbook.md` | Mom Test 워크북 |

---

*Skill: unit-converter-docs — Report/Transcript Export SSOT for UnitConverter_24.*
