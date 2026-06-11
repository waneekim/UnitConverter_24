# UnitConverter_XX — {세션 제목}
_Exported on {YYYY-MM-DD} from Cursor_
_Source: {agent-transcript uuid — 없으면 `세션 내 미확인`}_

---

**User**

{사용자 첫 요청 — 원문 또는 요약}

---

**Cursor**

{응답 요약: 수행 작업, 생성·수정 파일, pytest 결과(실제만)}

---

**User**

{다음 사용자 메시지}

---

**Cursor**

{다음 Cursor 응답 요약}

---

*(대화 턴을 User / Cursor 블록으로 반복. 긴 코드·로그는 `...`로 생략 가능)*

---

## Export 메타

| 항목 | 값 |
|------|-----|
| Report | `Report/{NN}.REPORT.md` |
| Phase | {RED \| GREEN \| REFACTOR \| repeat \| EXPORT} |
| Test ID | {D-LOC-01 등} |
| Command | {/export-session 등} |
| pytest (마지막 확인) | {터미널·채팅에 있는 결과만} |

---

*본 문서는 Prompting/{NN}.Export-Transcript.md — Cursor 세션 Transcript입니다.*
