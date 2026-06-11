# UnitConverter_XX — {세션 제목}

| 항목 | 내용 |
|------|------|
| 프로젝트 | UnitConverter_XX |
| 단계 | {세션 단계 — 예: TDD RED, GREEN, REFACTOR, ARRR 1사이클} |
| Phase | {RED \| GREEN \| REFACTOR \| repeat \| EXPORT} |
| Test ID | {예: D-LOC-01, VL-R1-001 — 없으면 `-`} |
| Command | {예: `/tdd-red`, `/export-session` — 없으면 `-`} |
| 보고서 생성일 | {YYYY-MM-DD} |
| 목적 | {한 줄} |

---

## 1. 요약

| 구분 | 결과 |
|------|------|
| Phase | **{Phase}** |
| 대상 | {주요 파일·모듈·Command} |
| pytest | `{실제 실행 결과만 — 채팅·터미널에 없으면 `미실행`}` |
| **판정** | **{완료 \| 진행 중 \| RED 완료 \| GREEN 완료 등}** |

{2~4문장: 세션에서 무엇을 했고, 왜, 결과가 무엇인지}

---

## 2. 핵심 결정·산출물

### 2.1 도메인·API (해당 시)

| Rule | 내용 |
|------|------|
| R1 | `X'-Y"` → 소수 feet (`R1_ARCH_INCH_DIVISOR` SSOT) |
| R2 | meter 기준 feet↔yard, 혼동·비율 불일치 → `fail` |
| R4 | `단위:값`, 건축 표기, 빈 셀 → `incomplete` |

API: `validate_lines(grid) -> {"status": "pass"|"fail"|"incomplete", "failed_lines": list[int]}`

### 2.2 테스트·검증 (해당 시)

| Test ID | 테스트 | Rule | 검증 의도 |
|---------|--------|------|-----------|
| {ID} | `{test_name}` | {R1~R4} | {의도} |

### 2.3 변경 파일

| 파일 | 작업 |
|------|------|
| `{path}` | {신규 \| 수정 \| —} — {한 줄 설명} |

### 2.4 진행 타임라인 (선택)

| 순서 | 사용자 요청 / Command | 결과 |
|------|------------------------|------|
| 1 | {요청} | {결과} |

---

## 3. git status 스냅샷 (Export 시점)

```
{git status --short 출력 — 없으면 `미수집`}
```

---

## 4. 다음 단계

1. {다음 TDD Phase 또는 작업}
2. `pytest tests/ -v` — {기대 결과}
3. git commit — **사용자 요청 시만**

---

## 관련 문서

| 문서 | 설명 |
|------|------|
| [Prompting/{NN}.Export-Transcript.md](../Prompting/{NN}.Export-Transcript.md) | 본 세션 Transcript |
| [docs/PRD.md](../docs/PRD.md) | FR·Test ID 매핑 |
| [.cursorrules](../.cursorrules) | 프로젝트 Rule |

---

*본 문서는 Report/{NN}.REPORT.md — {세션 제목} 세션 보고서입니다.*
