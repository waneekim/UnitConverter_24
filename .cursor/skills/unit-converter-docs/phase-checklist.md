# Phase Checklist — unit-converter-docs Export

Export 전·후에 Phase별로 확인한다. **채팅·터미널에 없는 pytest 결과는 기록하지 않는다.**

---

## 공통 (모든 Export)

- [ ] `Phase:` 첫 줄 선언 (`EXPORT` 또는 해당 Phase)
- [ ] `git status --short` 수집 (Report §3)
- [ ] `Report/`, `Prompting/`에서 `^\d{2}\.` 최대 번호 → `NN = max + 1`
- [ ] `Report/{NN}.REPORT.md` + `Prompting/{NN}.Export-Transcript.md` **동일 NN** 쌍 생성
- [ ] Transcript: `_Exported on`, `_Source` uuid (가능 시)
- [ ] Transcript: **User** / **Cursor** 블록 구분
- [ ] README 문서 표 갱신 (해당 섹션 있을 때만)
- [ ] 완료 보고에 **경로 2개** 명시
- [ ] git commit **하지 않음** (사용자 요청 시만)
- [ ] `UPDATE_GOLDEN` **임의 실행 안 함**

---

## RED

- [ ] `src/` 미수정 (스텁만 허용)
- [ ] `tests/`만 변경
- [ ] assert 완화·skip·xfail 없음
- [ ] pytest: **failed** 기대 (구현 없음 또는 의도적 실패)
- [ ] Report: Test ID·RED 묶음(D-LOC-01 등) 명시
- [ ] `docs/*-red-skeleton.md` 또는 entity 스켈레톤 참조 여부 기록

---

## GREEN

- [ ] `src/` 최소 구현으로 대상 테스트 통과
- [ ] pytest: **passed** (실제 실행 결과만 기록)
- [ ] `docs/*-green.md` 산출 여부 (해당 시)
- [ ] RED에서 고정한 API·Rule 변경 없음

---

## REFACTOR

- [ ] Green 유지 (pytest 전체 passed)
- [ ] smell ID·변경 요약 (S-01, R-B 등)
- [ ] 동작 변경 없음 (리팩터만)
- [ ] golden·approved 파일 임의 수정 없음

---

## repeat (ARRR 1사이클 완료)

- [ ] RED → GREEN → (Golden) → REFACTOR 순서 요약
- [ ] 1사이클 Test ID·FR 매핑 (`docs/PRD.md`)
- [ ] 다음 RED 묶음 후보 1~2개
- [ ] 세션 N 보고서 형식: 요약 표 + 타임라인

---

## EXPORT (Report / Transcript 전용)

- [ ] `unit-converter-docs` Skill 워크플로 Step A~F 수행
- [ ] `mom-test-report.md`, `session-workbook.md` 등 `NN.` 없는 파일은 번호 산정 제외
- [ ] 채팅에 없는 pytest 숫자·판정 **미기재**
