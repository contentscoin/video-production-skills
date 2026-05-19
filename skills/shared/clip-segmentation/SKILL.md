---
name: clip-segmentation
description: Segment videos over 15s into clips for Seedance 2.0 HARD LIMIT. 4 patterns: Beat-Boundary, Action-Boundary, Match-Cut, Detail Sequence. Sweet spot 8-12s per clip. v0.6 critical for long video.
---

# Clip Segmentation

긴 시나리오를 **각 15초 이하의 생성 클립들로 분할**하고, **편집 시 연결되도록 설계**하는 스킬.
Seedance 2.0의 4-15초 HARD LIMIT 제약을 시스템적으로 해결합니다.

## When to use

- 15초 초과 영상을 만들어야 할 때 (30초, 1분, 시리즈 등)
- shot-designer가 한 행의 duration을 15초 초과로 잡았을 때 (자동 검출)
- 시나리오·콘티를 받았는데 어떻게 클립으로 나눠야 할지 모를 때
- 시리즈 마지막 편의 series-closer 작업 (Type A 리프라이즈는 자연스럽게 분할됨)

**v0.5까지**: 이 작업이 shot-designer의 휴리스틱에 묻혀 있었음.
**v0.6 이후**: 전담 스킬로 분리, 명시적 절차.

## 핵심 룰

> **하나의 Seedance 생성 클립은 최대 15초**.
> 그 이상은 무조건 다중 클립 + 편집.

이 룰은 협상 불가능. 모델 자체 제약이라 우회 방법 없음.

## Inputs

- **시나리오** (script-writer의 scenes)
- **타깃 영상 길이** (intake-router에서)
- **narrative_arc** (narrative-weaver의 비트 구조)
- **emotional 흐름** (어디서 끊을지 결정 기준)

## Output

```yaml
clip_segmentation:
  total_target_duration_s: 30
  generation_clip_count: 4  # 또는 5
  edit_segment_count: 4  # 편집 후 최종 컷 수
  avg_clip_length_s: 7.5
  
  clips:
    - clip_id: "CLIP-1"
      duration_s: 8.0
      contains_shots: ["S1", "S2"]  # shot-designer의 shot_id들
      narrative_beats_covered: ["beat_1 Opening", "beat_2 Ritual partial"]
      ends_on: "ECU on pen tip"  # 다음 클립과 자연스럽게 이어질 마지막 프레임
      transition_out: "match_cut"  # 다음 클립으로의 연결 방법
      seedance_call:
        @이미지1: "CLIP-1 first frame"
        seed: null  # 또는 시리즈 시드
    
    - clip_id: "CLIP-2"
      duration_s: 6.0
      contains_shots: ["S3", "S4"]
      narrative_beats_covered: ["beat_2 Ritual complete"]
      starts_on: "ECU on cup (matches pen ECU framing)"  # 이전 클립과 매치
      ends_on: "ECU on pen with light reflection"
      transition_in: "match_cut from CLIP-1"
      transition_out: "dissolve 6 frames to CLIP-3"
      seedance_call:
        @이미지1: "CLIP-2 first frame"
        seed: 42  # 캐릭터 일관성 유지
```

## 4가지 분할 패턴

### Pattern A: 비트 경계 분할 (Beat-Boundary Cut)

narrative_arc의 비트 경계를 클립 경계로 사용. 가장 자연스러움.

**적합한 경우**:
- 비트마다 시각·정서가 명확히 달라질 때
- 비트 길이가 모두 15초 이하일 때

**예시 (BF30)**:
- CLIP-1: beat_1 Opening (3초)
- CLIP-2: beat_2 Ritual (4초)
- CLIP-3: beat_3 Departure (6초)
- ... (각 비트가 한 클립)

### Pattern B: 액션 경계 분할 (Action-Boundary Cut)

한 비트 안에서도 액션이 끝나는 자연 지점에서 분할.

**적합한 경우**:
- 한 비트가 15초 초과일 때 (예: 10초 hero shot)
- 또는 시각적으로 같은 위치라도 액션이 명확히 끊길 때

**예시**:
- 비트 3 (Departure, 6초) — 인물이 페어웨이로 걸어감
- 비트 3을 두 클립으로: CLIP-3a (출발, 3초) + CLIP-3b (도착·정지, 3초)

### Pattern C: 매치 컷 활용 (Match-Cut Sequence)

같은 구도·다른 시간/장소를 매치 컷으로 연결. 클립 끝과 다음 클립 시작이 시각적으로 거의 동일.

**적합한 경우**:
- 시간 경과를 표현할 때 (여명 → 정오 → dusk)
- 같은 오브제의 다양한 각도

**예시 (BF30 S1 ↔ S8)**:
- CLIP-1: 여명 클럽하우스 외관 (3초)
- ... 다른 클립들 ...
- CLIP-N: dusk 클럽하우스 외관 (같은 구도, 다른 시간)
- 편집 시 디졸브 또는 컷으로 거울 구조

### Pattern D: ECU Triple / 디테일 시퀀스 (Detail Sequence)

여러 ECU를 1.3-2초씩 빠르게 연결. **이 자체로 한 클립이 가능** (총 4-6초).

**예시 (BF30 ECU Triple)**:
- CLIP-2: 펜 ECU (1.33) + 컵 ECU (1.33) + 빛 reflection ECU (1.33) = 4초 한 클립
- 단, Seedance는 한 클립 안에서 컷 전환이 자연스럽지 않으므로 **별도 클립으로 분할 권장**:
  - CLIP-2a: 펜 ECU (1.33초 단독 클립)
  - CLIP-2b: 컵 ECU (1.33초 단독 클립)
  - CLIP-2c: 빛 reflection ECU (1.33초 단독 클립)
  - 편집 시 cut으로 연결

⚠️ 단, **Seedance 최소 길이는 4초** — 1.33초 단독 클립 생성 불가.
해결책: **4초 클립으로 생성하고 편집에서 1.33초만 잘라 사용** (앞뒤 트림).

## 핵심 결정: ECU·짧은 컷의 처리

Seedance 최소 4초, 최대 15초. 따라서:

| 원하는 컷 길이 | Seedance 생성 길이 | 편집 처리 |
|--------------|-----------------|----------|
| 1-3초 | 4초 (최소) | 앞뒤 트림으로 원하는 길이 |
| 4-15초 | 그대로 | 트림 불필요 |
| 16초+ | 분할 필요 | 다중 클립 + 편집 연결 |

**예시**: 1.33초 ECU 컷 3개 = Seedance 4초 클립 3개 생성 → 편집에서 각각 1.33초 트림 → 4초 시퀀스

## 캐릭터 일관성 (클립 간)

15초 이내 클립이지만 같은 캐릭터가 여러 클립에 등장하면 일관성이 중요:

1. **첫 클립의 마지막 프레임을 다음 클립의 reference image로 사용**
   - Seedance의 @이미지1을 직전 클립의 outframe으로 설정
2. **같은 시드 유지** (선택)
   - 단, 시드는 첫 생성 외 효과 제한적
3. **character-pool의 시트를 매 클립 reference에 포함**
   - 의상·외모 일관성 검증

## 트랜지션 카탈로그

편집에서 클립 간 연결 방법:

| 트랜지션 | 사용 시점 | duration_frames |
|---------|---------|-----------------|
| **straight cut** | 같은 시간·장소·인물의 다른 각도 | 0 |
| **match cut** | 시각적으로 비슷한 두 컷 (같은 모양·움직임) | 0 |
| **L-cut / J-cut** | 오디오를 다음 컷에 미리/뒤늦게 | 0 (오디오 오프셋) |
| **dissolve** | 시간 경과·정서 전환 | 4-12 |
| **fade to black** | 시퀀스·시간 큰 점프·종료 | 12-24 |
| **fade in from black** | 시작 또는 큰 시간 점프 후 | 12-24 |

⚠️ Seedance 자체로 트랜지션 못 만듦. 편집 단계에서 추가.

## Output JSON 표준

```json
{
  "project_id": "...",
  "skill_version": "clip-segmentation v0.6",
  "target_duration_s": 30,
  "generation_clip_count": 5,
  "edit_segment_count": 9,
  
  "clips": [
    {
      "clip_id": "CLIP-1",
      "seedance_generation_duration_s": 4.0,
      "edit_final_duration_s": 3.0,
      "trim_in_frames": 0,
      "trim_out_frames": 24,
      "contains_shots": ["BF30-S1"],
      "narrative_beat": "Opening Atmosphere",
      "first_frame_reference": "BF30-S1 first frame (dawn clubhouse)",
      "last_frame_for_next_clip": "still exterior, lights on in 2 windows",
      "transition_out": "dissolve 8 frames",
      "next_clip": "CLIP-2",
      "character_consistency_method": "N/A (no character)",
      "seed": null
    },
    {
      "clip_id": "CLIP-2",
      "seedance_generation_duration_s": 4.0,
      "edit_final_duration_s": 1.33,
      "trim_in_frames": 0,
      "trim_out_frames": 64,
      "contains_shots": ["BF30-S2"],
      "narrative_beat": "Ritual (pen)",
      "first_frame_reference": "ECU on hand with pen on notebook",
      "last_frame_for_next_clip": "pen tip at end of writing motion",
      "transition_out": "cut",
      "next_clip": "CLIP-3",
      "character_consistency_method": "character_pool ref + seed 42",
      "seed": 42,
      "trim_note": "4초 생성 → 편집에서 처음 1.33초만 사용"
    }
  ],
  
  "edit_assembly_order": [
    "CLIP-1 [0-3s] → dissolve 8f → CLIP-2 [3-4.33s] → cut → CLIP-3 [4.33-5.66s] → ..."
  ],
  
  "validation": {
    "all_clips_under_15s": true,
    "all_clips_over_4s_minimum": true,
    "total_edit_duration_matches_target": true,
    "character_consistency_strategy_defined": true
  }
}
```

## Heuristics

- **8-12초가 sweet spot** — 4-5초는 액션 완성 어려움, 13-15초는 모델 한계 근처
- **ECU·짧은 컷은 4초로 생성 후 트림** — 1-3초 클립 생성 불가
- **트랜지션은 클립 경계에서만** — 한 클립 안에서 컷 전환 자연스럽지 않음
- **same-character 클립끼리는 시드 고정 또는 reference 일관성**
- **첫 클립 + 마지막 클립이 거울 구조**일 때 가장 안정적 영상 구조 (BF30의 S1 ↔ S8)

## 협업 인터페이스

### shot-designer와 협업
- shot-designer가 한 행 duration > 15s 잡으면 → clip-segmentation 자동 호출
- shot_id 여러 개를 한 clip_id로 묶거나, 한 shot_id를 여러 clip_id로 분할

### editor와 협업
- clip-segmentation의 출력 → editor의 shots_to_assemble + transitions
- trim_in_frames / trim_out_frames → editor가 정확히 잘라냄

### prompt-engineer와 협업
- 각 clip의 first_frame_reference → image-prompt 생성
- 각 clip의 마지막 프레임 → 다음 clip의 reference

### production-brief와 협업
- 새 디렉토리 구조 추가:
```
project/
├── ... (기존 5파일)
├── clip_segmentation.json    ← v0.6 신규
├── clips/                    ← v0.6 신규
│   ├── CLIP-1_raw.mp4 (Seedance 생성 원본)
│   ├── CLIP-2_raw.mp4
│   └── ...
└── final_master.mp4
```

## 시스템 호출

- **상위**: shot-designer가 duration 초과 검출 시 / intake-router가 15초 초과 영상 인지 시
- **하위**: prompt-engineer + editor에 결과 전달
- **순서**: shot-designer 다음, prompt-engineer 이전

## 청사진 매핑

청사진의 `timeline_segmentation` claim에 직접 대응 (이전엔 seedance-prompt에 일부 묻혀 있었음).

## 오픈크랩 컨텍스트

- Seedance 2.0 가이드의 멀티모달 제약 명세
- 편집 워크플로우 (post-production-spec 스킬과 연동)
