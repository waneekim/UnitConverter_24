# Export Session — Report + Transcript

현재 Cursor 세션을 **Report 보고서**와 **Prompting Transcript** 두 파일로 Export한다.

**Export 요청 시 unit-converter-docs Skill 로드 후 checklist 수행.**

- Skill: `.cursor/skills/unit-converter-docs/SKILL.md`
- Checklist: `.cursor/skills/unit-converter-docs/phase-checklist.md`

## Phase 선언 (필수)

응답 **첫 줄**에 반드시 작성:

```
Phase: EXPORT
```

## 산출물 (2개만)

| 종류 | 경로 | 형식 |
|------|------|------|
| 보고서 | `Report/NN.REPORT.md` | `01.REPORT.md` 패턴 |
| Transcript | `Prompting/NN.Export-Transcript.md` | `01.Export-Transcript.md` 패턴 |

- `NN` = 두 폴더(`Report/`, `Prompting/`)의 `NN.*` 파일 중 **최대 번호 + 1** (2자리 zero-pad: `01`, `02`, …)
- `session-workbook.md`, `mom-test-report.md` 등 `NN.` 접두가 없는 파일은 번호 산정에서 **제외**
- 동일 `NN`으로 Report·Transcript **쌍** 생성

## 절차

1. **Skill 로드** — `unit-converter-docs` SKILL.md + `phase-checklist.md`
2. **번호 결정** — `Report/`, `Prompting/`에서 `^\d{2}\.` 패턴 파일 목록 확인 → `NN` 계산
3. **세션 수집** — 대화 전체, 변경 파일, TDD Phase(RED/GREEN/REFACTOR), pytest 결과
4. **보고서 작성** — `Report/NN.REPORT.md` (Skill `report-template.md` 또는 아래 템플릿)
5. **Transcript 작성** — `Prompting/NN.Export-Transcript.md` (Skill `transcript-template.md` 또는 아래 템플릿)
6. **메타 보고** — 생성 경로·변경 파일·pytest·Phase 요약

## Report 템플릿 (`Report/NN.REPORT.md`)

```markdown
# UnitConverter_XX — {세션 제목}

| 항목 | 내용 |
|------|------|
| 프로젝트 | UnitConverter_XX |
| 단계 | {세션 단계 — 예: TDD RED, GREEN, Command 구축} |
| 보고서 생성일 | {YYYY-MM-DD} |
| 목적 | {한 줄} |

---

## 1. 요약

| 구분 | 결과 |
|------|------|
| Phase | {RED / GREEN / REFACTOR / 설정·문서} |
| 대상 | {주요 파일·Command} |
| pytest | {N passed / N failed — 맥락} |
| **판정** | {RED 완료 / GREEN 완료 / …} |

{2~4문장 요약}

---

## 2. 핵심 결정·산출물

### 2.1 도메인·API
(R1~R4·validate_lines API — 세션에서 다룬 범위만)

### 2.2 테스트 / 구현
(테스트 표 또는 구현 요약)

### 2.3 변경 파일
| 파일 | 작업 |

### 2.4 진행 타임라인
| 순서 | 사용자 요청 | 결과 |

---

## 3. 다음 단계
(번호 목록)

---

## 관련 문서
| 문서 | 설명 |
| [Prompting/NN.Export-Transcript.md](../Prompting/NN.Export-Transcript.md) | 본 세션 Transcript |
| … | |

---

*본 문서는 Report/NN.REPORT.md — {세션 제목} 세션 보고서입니다.*
```

## Transcript 템플릿 (`Prompting/NN.Export-Transcript.md`)

```markdown
# UnitConverter_XX — {세션 제목}
_Exported on {YYYY-MM-DD} from Cursor_

---

**User**

{사용자 메시지 원문}

---

**Cursor**

{응답 요약 — Phase 선언·핵심 결과·코드 변경 포함}

---

(대화 턴 반복 — **이번 세션 전체**를 시간순으로 기록)

---

## Export 메타

| 항목 | 값 |
|------|-----|
| Report | `Report/NN.REPORT.md` |
| Transcript | `Prompting/NN.Export-Transcript.md` |
| 변경 파일 | {목록} |
| pytest | {결과} |
| Phase | {마지막 TDD Phase} |

---

*본 문서는 Prompting/NN.Export-Transcript.md — {세션 제목} 대화 Export입니다.*
```

## 응답 보고 형식

```markdown
Phase: EXPORT

## 생성 파일
- `Report/NN.REPORT.md`
- `Prompting/NN.Export-Transcript.md`

## Export 메타
| 항목 | 값 |
| Report | … |
| Transcript | … |
| 변경 파일 | … |
| pytest | … |
| Phase | … |
```

## 금지

- `Report/`, `Prompting/` 외 임의 경로에 저장
- 기존 `NN.REPORT.md` / `NN.Export-Transcript.md` **덮어쓰기** (항상 새 `NN`)
- Transcript 생략 또는 Report만 생성
- git commit·push (사용자 요청 시만)
- Export 범위 밖 파일 대량 생성
- 채팅·터미널에 없는 pytest 결과 기재
- `UPDATE_GOLDEN` 임의 실행

## 참고

- Skill·템플릿: `.cursor/skills/unit-converter-docs/`
- 기존 예시: `Report/01.REPORT.md`, `Prompting/01.Export-Transcript.md`
- 세션 근거: `Report/session-workbook.md`, `.cursorrules`

## 사용자 인자

`/export-session` 뒤 텍스트가 있으면 세션 제목·강조할 Phase로 사용한다.
(예: `/export-session validate_lines GREEN 완료`)
