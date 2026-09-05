# PM-Problem-Solving Skill

**Version:** 2.0  
**Status:** Active  
**Last Updated:** 2026-09-06

## Purpose
실전 프로젝트 Issue를 구조화하고, 긴급성·영향도·개발 리소스·원인·해결안·검증·Side Effect·회귀시험까지 관리하여 PM 의사결정과 문제 종료를 지원한다.

## Core Principle
> 문제를 빨리 처리하는 것이 아니라, 문제를 정의하고 검증 가능한 실행계획으로 바꿔 조직이 움직이게 한다.

## Process

### 1. DEFINE — 문제 정의
- 증상과 실제 문제를 구분한다.
- 현재 상태 / 목표 상태 / Gap을 명확히 한다.
- Business Impact와 Deadline을 기록한다.
- 문제를 한 문장으로 정의한다.

### 2. EVIDENCE — 증거 확보
확보 여부를 확인한다.
- Video
- Screenshot
- Log
- Error Message
- 발생 시간
- SW/FW Version
- Model
- 환경정보
- 설정값
- 재현 횟수/빈도

가능하면 Video와 Log의 Time Stamp를 맞춘다.

### 3. REPRODUCTION — 재현 시나리오
다음 형식으로 재현 조건을 명확히 한다.
- Pre-condition
- Step-by-step
- Expected Result
- Actual Result
- Reproduction Rate
- Reproduction Environment

핵심 질문: 개발자가 동일 환경에서 재현할 수 있는가?

### 4. URGENCY VALIDATION — 긴급성 검증
'긴급'이라는 요청을 그대로 받아들이지 않고 근거를 확인한다.
- 고객 영향
- 출하 영향
- 매출/사업 영향
- 일정 영향
- 안전/법규 영향
- 발생 빈도
- 재현율
- Workaround 존재 여부
- Deadline

Priority: P0 / P1 / P2 / P3

### 5. IMPACT — 영향도 분석
범위를 확인한다.
- Customer
- Product
- Function
- Region
- Model
- SW Version
- Release
- Schedule
- Business

같은 원인이 다른 모델/제품에도 존재할 가능성을 확인한다.

### 6. RESOURCE — 개발 리소스 확인
문제 심각도와 별도로 실제 실행 가능성을 확인한다.
- 담당 개발자
- 필요 인원
- 예상 MD
- 분석 가능 시점
- 수정 예상일
- QA 필요 여부
- Infra/Platform 지원
- 해외 연구소/외부 협력 지원
- Deadline 달성 가능 여부

### 7. ROOT CAUSE — 원인 분석
추측을 사실처럼 다루지 않는다.

**Fact → Hypothesis → Verification → Root Cause**

검증되지 않은 원인은 가설로 표시한다.

### 8. SOLUTION — 해결안 도출
최소 3개 옵션을 만든다.
- Option A: 근본 해결
- Option B: 임시 해결
- Option C: 우회/대체

각 옵션을 효과 / 비용 / 일정 / Risk 기준으로 비교한다.

### 9. DECISION — PM Recommendation
PM은 선택지를 나열하는 데 그치지 않고 추천안을 제시한다.

예:
> 일정 리스크를 즉시 차단하기 위해 B를 먼저 적용하고, A를 근본 해결책으로 진행한다.

### 10. ACTION — 실행계획
모든 Action은 Owner와 Deadline을 갖는다.

| Action | Owner | Deadline | Success Criteria |
|---|---|---|---|

Owner 없는 Action은 완료 가능한 Action으로 보지 않는다.

### 11. FIX — 수정
수정 완료를 문제 해결 완료와 동일시하지 않는다.
수정은 검증 전까지 '해결 후보'로 취급한다.

### 12. SIDE EFFECT — 부작용/영향 검증
수정으로 인해 다음 문제가 생기지 않는지 확인한다.
- 다른 기능 장애
- 기존 기능 변경
- UI/UX 영향
- CPU 증가
- Memory 증가
- Network 증가
- Response Time 증가
- Boot Time 증가
- 다른 Model 영향
- 다른 Platform 영향

### 13. VALIDATION — 검증
최소 다음 테스트를 확인한다.
1. 문제 재현 TC
2. 수정 검증 TC
3. 관련 기능 TC
4. 기본 Smoke TC
5. Regression TC
6. Performance Test
7. Stability / Long-run Test
8. 고객 사용 시나리오

### 14. PERFORMANCE — 성능 검증
필요 시 다음을 비교한다.
- Response Time
- CPU
- Memory
- Network
- Boot Time
- 처리속도
- 안정성
- 장시간 동작 결과

### 15. RELATED FUNCTION — 관련 기능 검증
수정 기능만 보지 않는다.
Dependency를 따라 연관 기능을 검증한다.

예:
`A 수정 → B → C → D`

### 16. DEFINITION OF DONE
Issue Closed 조건을 사전에 명확히 한다.
- Root Cause 확인
- Fix 완료
- 문제 재현 불가
- Side Effect 없음
- Performance OK
- 관련 기능 OK
- 기본 TC OK
- Regression OK
- 고객 시나리오 OK
- Release Risk 승인

### 17. CLOSURE — 종료
종료 시 다음을 기록한다.
- 최종 결과
- Root Cause
- Fix
- Test Result
- Release 판단
- 남은 Risk
- Lesson Learned
- 재발방지

### 18. KNOWLEDGE — Skill 업데이트
Issue 종료 후 일반화할 수 있는 지식을 추출한다.

`Problem → Root Cause → Solution → Result → Lesson Learned → Prevention → Skill Update`

## Standard Issue Template

```text
[PROJECT]
프로젝트명:

[ISSUE]
Issue 제목:
발생일:
발견자:
담당팀:

[1. DEFINE]
현재 상태:
목표 상태:
문제 정의:
Business Impact:
Deadline:

[2. EVIDENCE]
Video:
Screenshot:
Log:
Error Message:
발생시간:
SW/FW Version:
Model:
환경정보:

[3. REPRODUCTION]
Pre-condition:
Steps:
Expected:
Actual:
재현율:
재현환경:

[4. URGENCY]
고객 영향:
사업 영향:
출하 영향:
안전/법규:
Workaround:
Priority: P0/P1/P2/P3

[5. RESOURCE]
개발 담당:
필요 인원:
예상 MD:
분석 가능일:
수정 예상일:
QA/기타 지원:
Deadline 가능: YES/NO

[6. ROOT CAUSE]
Fact:
Hypothesis:
Verification:
Root Cause:

[7. SOLUTION]
Option A:
Option B:
Option C:
PM Recommendation:

[8. ACTION]
Action:
Owner:
Deadline:
Success Criteria:

[9. VALIDATION]
Problem Reproduction TC: PASS/FAIL
Fix Verification TC: PASS/FAIL
Related Function TC: PASS/FAIL
Basic Smoke TC: PASS/FAIL
Regression TC: PASS/FAIL
Performance: PASS/FAIL
Stability/Long-run: PASS/FAIL
Customer Scenario: PASS/FAIL

[10. SIDE EFFECT]
기능:
성능:
Memory:
CPU:
Network:
Model/Platform:
UI/UX:

[11. DEFINITION OF DONE]
Root Cause 확인: Y/N
Fix 완료: Y/N
재현 불가: Y/N
Side Effect 없음: Y/N
Performance OK: Y/N
관련 기능 OK: Y/N
기본 TC OK: Y/N
Regression OK: Y/N
고객 시나리오 OK: Y/N
Release Risk 승인: Y/N

[12. CLOSURE]
결과:
Lesson Learned:
재발방지:
Skill Update:
```

## AI Execution Rule
사용자가 **"문제해결 Skill 실행"**이라고 요청하면 이 문서를 기준으로 진행한다.

1. 입력 정보의 누락 항목을 먼저 식별한다.
2. 필요한 질문을 최소화하여 제시한다.
3. 문제 정의부터 DoD까지 순서대로 분석한다.
4. 긴급성은 객관적 근거로 재검증한다.
5. 개발 리소스와 Deadline의 현실성을 반드시 확인한다.
6. 원인과 가설을 구분한다.
7. 최소 3개 해결안을 비교한다.
8. PM Recommendation을 제시한다.
9. 수정 후 Side Effect / Performance / Related Function / Basic TC / Regression / Customer Scenario를 확인한다.
10. Closed 조건이 충족되지 않으면 Issue를 종료하지 않는다.
11. 종료 후 Lesson Learned를 추출한다.
12. 일반화 가능한 개선이면 마스터 Skill 버전업 후보로 제안한다.

## Versioning Rule
- 실제 Issue 적용 후 개선이 필요한 경우 `CHANGELOG.md`에 기록한다.
- 단순 사례는 Skill 버전을 올리지 않는다.
- 재사용 가능한 일반화 규칙이 추가/수정/삭제될 때 버전을 올린다.
- 예: v2.0 → v2.1 → v2.2
