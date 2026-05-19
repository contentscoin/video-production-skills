---
name: character-pool
description: Manage character sheets for video series: demographics, face, wardrobe, demeanor, facs_defaults, what_to_avoid, ai_rights_notes. Use at series start; lock after V1 for consistency.
---

# Character Pool

시리즈·캠페인 전반에 걸친 등장 캐릭터를 **명시적 자산**으로 관리하는 스킬.
한 번 정의된 캐릭터는 시트(ID) 기반으로 호출되어 어느 편에서나 동일하게 재현됩니다.

## When to use

- 시리즈 캠페인(2편 이상) 시작 시 — 첫 번째 작업에 들어가기 전 풀 구조부터 만듦
- 새 편 진입 시 — pool에서 기존 캐릭터 선택 vs 신규 추가 결정
- 캐릭터 일관성 문제가 발생했을 때 (예: V3와 V5의 같은 인물이 다르게 보임)
- 외주·후속 작업자에게 인계할 때 (캐릭터 시트 = 인수인계 문서)

단편 1회성 작업이면 이 스킬은 과잉. 그 경우 캐릭터 정의는 prompt-engineer 단계에 인라인.

## Pool 구조

```yaml
campaign_id: "FMGmember_2026Q3"
pool_version: "1.2"
created_at: "..."
characters:
  CHAR_ID:
    role: "캐릭터의 캠페인 내 역할"
    appears_in: ["V1-S1", "V1-S2", "V6-S1"]
    locked: true  # 한번 lock되면 외모 변경 불가, 새 ID 발급 필요
    sheet: { ... }
```

### 캐릭터 시트 필수 필드

```json
{
  "character_id": "FMG_CHAR_A_REVIEWER",
  "role": "회원권 검토자",
  "appears_in": ["V1-S1", "V1-S2", "V1-S3", "V1-S4", "V6-S1"],
  "locked": true,
  "created_at": "2026-05-18",

  "demographics": {
    "age_range": "55-62세",
    "gender": "남성",
    "ethnicity": "한국",
    "build": "중간 체격, 키 175cm 가정"
  },

  "face": {
    "shape": "약간 긴 타원형, 광대 절제됨",
    "skin": "지긋한 나이감, 미세한 주름",
    "hair": "은백색 50%, 짧은 사이드 스왭트",
    "eyebrows": "회색 섞인 차분한 직선형",
    "facial_hair": "없음, 깨끗하게 면도",
    "distinguishing": "왼쪽 손목 클래식 메탈 시계"
  },

  "wardrobe": {
    "indoor": "네이비 캐시미어 V넥 + 화이트 셔츠 + 다크 그레이 울 트라우저",
    "outdoor": "차콜 그레이 테일러드 재킷 + 라이트 그레이 풀오버 + 네이비 트라우저",
    "accessories": "라이트 브라운 가죽 벨트, 메탈 시계"
  },

  "demeanor": {
    "movement_speed": "느림, 신중함",
    "gaze_pattern": "한 곳에 머무름",
    "hand_motion": "작고 명확",
    "posture": "곧음, 약간 앞으로 기울임 (3도)"
  },

  "facs_defaults": {
    "neutral_state": "AU24A (입술 미세 다물림)",
    "common_emotions": {
      "consideration": "AU4B + AU7A",
      "quiet_confidence": "AU17A + AU24A",
      "subtle_approval": "AU6A + AU12B"
    },
    "intensity_ceiling": "C (D~E 강도 금지 — 절제된 캐릭터)"
  },

  "what_to_avoid": [
    "얼굴이 완전히 식별되는 정면 클로즈업",
    "명품 로고 노출",
    "지나치게 젊거나 노쇠한 외모",
    "과장된 표정 (D~E 강도)"
  ],

  "alt_versions": [
    {
      "version_id": "CHAR_A_outdoor_winter",
      "modification": "외투 추가 (캐시미어 오버코트)"
    }
  ]
}
```

### 필수 vs 선택 필드

**필수 (캐릭터 정체성)**: character_id, role, appears_in, demographics, face, wardrobe
**상황별 권장**: demeanor (인물 중심 컷이 많을 때), facs_defaults (얼굴 노출 컷이 있을 때)
**선택**: alt_versions, what_to_avoid (중요하면 강력 권장)

## Locked / Unlocked

- **locked: true** — 외모·의상·디머너 변경 불가. 변경하려면 새 ID 발급 (예: `CHAR_A_v2`).
- **locked: false** — 작업 중 정의 보강 가능. 처음 정의 직후엔 unlocked, 첫 사용 후 lock.
- locked 상태로 외모 변경 요청이 들어오면 → 사용자에게 확인 후 alt_versions에 추가 또는 새 ID 발급.

## Operations

### 1. Pool 초기화
```
input: campaign_id
output: 빈 pool 구조 + 작업 디렉토리
```

### 2. 캐릭터 추가 (add)
```
input: 캐릭터 시트 + ID 제안
process: ID 중복 체크 → 시트 검증 → pool에 추가 (unlocked 상태로)
output: 추가된 character_id
```

### 3. 캐릭터 조회 (get)
```
input: character_id 또는 role 키워드
output: 전체 시트
```

### 4. 캐릭터 lock
```
input: character_id
process: 첫 사용 직후 자동 lock 또는 수동 lock
output: locked: true 상태
```

### 5. Alt 버전 추가
```
input: 기존 character_id + 수정사항
process: alt_versions에 추가 (메인 시트는 변경 안 함)
output: 새 version_id
```

### 6. 새 ID 발급 (외모 변경 시)
```
input: 기존 character_id + 새 외모
process: 새 ID 발급 (보통 _v2, _v3) + 메모로 derived_from 명시
output: 새 character_id
```

### 7. Pool 감사 (audit)
```
output: 시리즈에서 사용되지 않은 캐릭터 / 빈약한 시트 / lock 안 된 캐릭터 리스트
```

## ID 명명 규칙

```
{CAMPAIGN}_CHAR_{LETTER}_{ROLE}
```

예시:
- `FMG_CHAR_A_REVIEWER`
- `FMG_CHAR_B_PARTNER`
- `MONEV_CHAR_A_CLIENT`

- LETTER: A~Z 순차 (필요 시 AA, AB...)
- ROLE: 단어 1~2개, 영문 대문자 스네이크 케이스 (선택사항이지만 권장)
- 변형은 `_v2`, `_outdoor`, `_aged` 등 suffix

## 프롬프트 출력 시 사용

캐릭터를 프롬프트에 인용할 때:

```
[Image Prompt - V3-S2]

Character: FMG_CHAR_E_EMPLOYEE_M
  - 32-38세 한국 남성, 깨끗한 피부
  - 베이지 골프 폴로 + 베이지 슬랙스
  - 표정: 집중 (AU4A + AU7A)

Medium shot, side angle, 50mm f/2.0.
...
```

ID만 쓰면 안 됨 — 이미지 생성 모델은 ID를 모름. **ID는 인간 추적용**, 실제 프롬프트에는 시트 내용을 풀어서 작성.

## Output Format

```json
{
  "operation": "add",
  "character_id": "FMG_CHAR_I_HR_LEAD",
  "status": "added_unlocked",
  "sheet": { ... },
  "pool_state": {
    "total_characters": 9,
    "locked_count": 2,
    "unlocked_count": 7
  },
  "warnings": []
}
```

## 휴리스틱

- **시리즈 시작 전에 메인 캐릭터 2~3명은 미리 정의**. 작업 중 즉흥 정의는 일관성 깨짐.
- **얼굴 노출 없는 캐릭터도 시트화** — "익명의 손"도 손 형태·시계 유무·연령대를 적어둠.
- **alt_versions를 적극 활용** — 같은 인물의 계절·연령·의상 변형은 ID 분리보다 alt가 깔끔.
- **풀이 10명 넘으면 위험 신호** — 시리즈가 너무 산만하거나, ID가 너무 세분화됨. 통합 검토 권장.
- **외주·후속 작업자 인계 시 풀 전체 export** — 시트만 있으면 다른 사람이 이어받아도 일관성 유지.

## 시스템 호출

이 스킬은 다른 스킬과 다음과 같이 협력:
- `intake-router`가 시리즈 작업이라고 판단하면 → character-pool 초기화 권장
- `script-writer`가 인물을 도입할 때 → pool 조회 또는 신규 추가
- `prompt-engineer`가 이미지·비디오 프롬프트 쓸 때 → pool에서 시트 가져와서 풀어 씀
- `facs-expression`이 표정 명세 만들 때 → pool의 facs_defaults 참고

## 오픈크랩 컨텍스트

- 시리즈가 길어지면 캐릭터 풀 전체를 별도 오픈크랩 팩으로 ingest 가능
- `opencrab_ingest_text` 로 풀 JSON을 업로드 → 후속 작업에서 워크플로우로 컨텍스트 로드
