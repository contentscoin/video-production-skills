---
name: qa-review
description: 6-dimension QA for AI video: character consistency, artifacts, lipsync, cut rhythm, prompt drift, evidence. Plus AI rights checks. 3-cycle limit. Use after generation, before confirmation.
---

# QA Review

생성된 이미지·비디오 산출물을 **체크리스트 기반으로 점검**하고 재생성·수정 루프를 돌리는 스킬.
청사진의 8단계 워크플로우에서 마지막 단계 (QA 루프)에 대응합니다.

## When to use

- 첫 생성 결과가 나온 직후
- 시리즈 작업에서 편 간 일관성 체크
- 클라이언트 컨펌 전 최종 점검
- 외주 인계 전 자체 검수

이 스킬은 **사람의 눈을 대체하지 않습니다**. 사람이 놓치기 쉬운 체크 항목을 체계화해서 누락을 줄이는 도구.

## 청사진 근거

청사진의 워크플로우 단계 8:
> "QA: 캐릭터 일관성, 얼굴/손 artifact, 립싱크, 오디오 싱크, 컷 리듬, 프롬프트 drift를 체크한다."

및 required_claim_checks 중 `claim_postproduction_loop`, `claim_evidence_traceability`.

## 6가지 QA 차원

### 1. 캐릭터 일관성 (Character Consistency)

같은 캐릭터가 여러 컷·여러 편에서 **동일하게 보이는가**.

**체크 항목**:
- [ ] 얼굴 윤곽·이목구비가 첫 등장과 동일한가
- [ ] 헤어 스타일·길이·색이 일치하는가
- [ ] 의상이 시트와 일치하거나 정의된 alt 버전인가
- [ ] 액세서리(시계·안경 등)가 일치하는가
- [ ] 체형·키의 비율이 흔들리지 않는가

**자동 체크 보조**:
- character-pool의 시트와 생성 이미지를 나란히 놓고 비교
- 얼굴 인식 모델로 동일 인물 점수 산출 (선택)

**대처**:
- 일관성 깨짐 → 시드 고정 + 시트 재참조 후 재생성
- 작은 차이는 후처리 보정 가능, 큰 차이는 재생성

### 2. 얼굴·손 artifact

AI 생성의 고전적 약점.

**체크 항목**:
- [ ] 손가락 개수가 5개인가 (특히 양손이 보이는 경우)
- [ ] 손가락 길이·관절이 자연스러운가
- [ ] 손의 자세가 물리적으로 가능한가
- [ ] 눈동자가 두 개 다 같은 방향을 보는가
- [ ] 귀가 양쪽에 있고 비대칭이 과하지 않은가
- [ ] 치아·잇몸이 부자연스럽지 않은가
- [ ] 머리카락의 끝과 두피 연결이 자연스러운가
- [ ] 옷의 솔기·단추·라인이 끊기지 않았는가

**자동 체크 보조**:
- 손 인식 모델 (있다면) — 손가락 개수 점검
- 좌우 대칭 점수 산출

**대처**:
- 손이 핵심이면 ECU로 재촬영 또는 손을 프레임 밖으로
- 작은 artifact는 후처리 (Photoshop generative fill)

### 3. 립싱크·오디오 싱크 (Lip Sync / Audio Sync)

비디오 생성물에 한정.

**체크 항목**:
- [ ] 입 모양이 음성·대사와 일치하는가 (대사 있는 경우)
- [ ] BGM 비트와 컷 전환이 일치하는가 (뮤비 작업)
- [ ] SFX가 시각 동작과 동기화되는가 (발자국·문 닫힘 등)
- [ ] 음성 톤이 캐릭터 시트와 어울리는가

**대처**:
- 립싱크 어긋남 → 대사 컷은 별도 모델(Kling 3.0 등)로 재생성
- 립싱크가 자신 없으면 처음부터 대사 없는 설계 (V1처럼)

### 4. 컷 리듬 (Cut Rhythm)

여러 컷이 연결된 시퀀스.

**체크 항목**:
- [ ] 컷의 길이가 의도와 일치하는가
- [ ] 음악의 비트·강박과 컷 전환이 맞는가
- [ ] 너무 빠른 컷으로 멀미 유발하지 않는가
- [ ] 너무 긴 컷으로 시청자 이탈 위험이 없는가
- [ ] 컷 사이 트랜지션(매치컷·디졸브)이 자연스러운가

**플랫폼별 기준**:
- 숏폼: 첫 1초 이내 후킹 컷 필수, 컷 평균 1.5~3초
- 시네마틱: 컷 평균 3~8초, 정적 와이드는 5~10초까지 OK
- 광고 15초: 5~6 컷이 표준, 7컷 이상은 산만

### 5. 프롬프트 드리프트 (Prompt Drift)

여러 컷을 만들면서 프롬프트가 미세하게 변하면서 룩이 흔들리는 현상.

**체크 항목**:
- [ ] 모든 컷의 그레이드 키워드가 일관되는가 (Vision3 250D 등)
- [ ] 컬러 팔레트 어휘가 visual-bible과 일치하는가
- [ ] 렌즈 화각이 정의된 lens_kit 안에 있는가
- [ ] 조명 방향·색온도가 일관되는가
- [ ] negative 프롬프트가 누락되지 않았는가

**자동 체크 보조**:
- 모든 프롬프트를 한 표로 정렬해서 컬럼별 일관성 점검
- visual-bible 검증 호출

### 6. Evidence Traceability (근거 추적)

청사진의 `claim_evidence_traceability` 항목.

**체크 항목**:
- [ ] 각 결정에 근거가 있는가 (브리프·바이블·레퍼런스)
- [ ] 외주·후속 작업자가 "왜 이렇게 했나"를 추적 가능한가
- [ ] 변경 이력이 기록되어 있는가
- [ ] 클라이언트 컨펌이 어디서 났는지 명시되어 있는가

**대처**:
- 누락된 근거 → 작업 메모로 보충
- 시리즈 작업이면 변경 이력 표 유지

## QA 출력 포맷

```json
{
  "qa_target": "FMGmember V1 final master",
  "review_date": "2026-05-18",
  "reviewer": "qa-review skill",

  "checks": {
    "character_consistency": {
      "status": "PASS",
      "notes": "CHAR-A 5개 컷 모두 시트와 일치"
    },
    "face_hand_artifact": {
      "status": "WARNING",
      "issues": [
        {
          "shot": "V1-S3",
          "issue": "왼손 손가락 4개로 보임",
          "severity": "minor",
          "fix": "ECU로 재생성 또는 손 프레임 밖으로 재구성"
        }
      ]
    },
    "lip_audio_sync": {
      "status": "N/A",
      "notes": "대사 없는 작품"
    },
    "cut_rhythm": {
      "status": "PASS",
      "notes": "5컷 평균 3초, 숏폼 표준 범위"
    },
    "prompt_drift": {
      "status": "PASS",
      "notes": "Vision3 250D 일관 적용"
    },
    "evidence_traceability": {
      "status": "PASS",
      "notes": "visual-bible v1.0 잠금 후 작업"
    }
  },

  "overall": "WARNING - 1개 minor 수정 후 통과 가능",
  "recommended_actions": [
    "V1-S3 재생성 (손 artifact)",
    "그 외 모든 항목 PASS"
  ],
  "next_loop": "수정 후 재QA 권장"
}
```

## QA 루프 (Iteration)

```
[Generation 1차]
   ↓
qa-review 실행
   ↓
   ├─ ALL PASS → 마무리
   ├─ MINOR WARNING → 수정 후 부분 재QA
   └─ MAJOR FAIL → 해당 영역 전면 재생성
   ↓
[Generation 2차]
   ↓
qa-review 재실행
   ↓
... (최대 3 사이클 권장. 그 이상은 설계 자체 재검토)
```

**3 사이클 이상 못 통과하면**:
- 프롬프트가 모델 한계 너머일 수 있음 → 디렉션 조정
- 또는 모델 선택 변경 (model-adapter 재호출)
- 또는 후처리 합성으로 보강

## QA 우선순위 (시간 부족 시)

상위→하위 순서로 체크. 첫 번째 FAIL에서 멈춰서 수정 후 재시작:

1. **캐릭터 일관성** — 깨지면 시리즈 자체가 무너짐
2. **얼굴·손 artifact** — 시청자가 가장 쉽게 알아챔
3. **프롬프트 드리프트** — 룩의 일관성
4. **컷 리듬** — 시청 완주율
5. **립싱크·오디오 싱크** — 대사 있을 때만
6. **Evidence Traceability** — 후속 작업이 있을 때만

## 시스템 호출

- 생성 직후 자동 호출 권장
- `editor` (pumasi)의 마무리 단계
- `post-production-spec` 작성 전 (수정 사항이 있으면 spec에 반영)
- 시리즈 후속 편 시작 전 (이전 편 QA 결과 회고)

## 자동화 vs 사람 검수

| 항목 | 자동 가능 | 사람 필요 |
|------|----------|----------|
| 손가락 개수 | 부분 (인식 모델) | 미묘한 경우 |
| 캐릭터 일관성 | 부분 (얼굴 인식) | 의상·체형 |
| 컷 리듬 | 거의 자동 | 정서적 흐름 |
| 프롬프트 드리프트 | 거의 자동 | — |
| 정서 톤 적합성 | — | 100% 사람 |
| 브랜드 정합성 | 부분 (visual-bible 검증) | 최종 판단 |

자동 체크로 잡은 것은 사람의 시간을 아껴주고, 사람은 자동이 못 잡는 정서·맥락에 집중.

## 오픈크랩 컨텍스트

근거 자료:
- 청사진 `skill_blueprint/seedance_video_director_skill.md`의 QA 단계
- 청사진의 `claim_postproduction_loop`, `claim_evidence_traceability`
- 시리즈 작업의 QA 이력도 별도 팩으로 관리 가능
