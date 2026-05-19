# FMGmember Brand Film 30s — v0.6 Output

영상 제작 시스템 **v0.6** (15초 HARD LIMIT 반영) 을 회사 공식 채널용 브랜드 필름 30초에 적용한 결과 패키지.

## v0.5 → v0.6 핵심 차이

이 패키지는 v0.5 버전의 **재구성**입니다. 차이:

| | v0.5 | v0.6 |
|---|------|------|
| 영상 구조 | 9 shots 단일 영상 가정 | **8 Seedance 클립 + 1 edit-only** |
| Seedance 호출 | 1번 (실제론 불가능) | **8번** |
| 편집 단계 | 선택적 | **필수** (edit_decision_list) |
| ECU triple (1.33초 ×3) | 직접 생성 가정 | **4초씩 생성 → 트림** |
| clips/ 디렉토리 | 없음 | **있음** (raw clip 저장) |

### 왜 변경됐나

Seedance 2.0의 실제 제약: **한 생성 클립은 4-15초가 HARD LIMIT**.

v0.5는 이 제약을 인지하지 못하고 30초 영상을 단일 명세로 만들었음. v0.6는:
1. clip-segmentation 스킬로 8개 ≤ 15초 클립으로 분할
2. ECU 짧은 컷은 4초 생성 후 트림으로 처리
3. editor가 edit_decision_list로 정확히 어셈블

## 패키지 구성

```
fmg_brand_film_30s/
├── README.md                       (이 파일)
├── production_brief.md             종합 브리프 (v0.6)
├── clip_segmentation.json          ⭐ v0.6 신규 - 8 클립 분할 명세
├── shotlist.csv                    9행 + clip_id 컬럼 (v0.6)
├── gpt_image_prompts.jsonl         8개 (clip_id 참조)
├── seedance_prompts.jsonl          8개 (clip_id + 트림 명세)
├── post_production_spec.json       ⭐ v0.6 - edit_decision_list 포함
└── music_rights_audit.json         음악 권리 점검
```

## 활용 순서

### 1. 작업 계획 단계
1. **production_brief.md**: 전체 흐름·구조 파악
2. **clip_segmentation.json**: 8 클립이 어떻게 나뉘는지·왜 그렇게 나뉘는지

### 2. 자산 생성 단계
1. **gpt_image_prompts.jsonl**: 8개 라인 각각 → Nano Banana Pro로 이미지 생성
2. **seedance_prompts.jsonl**: 8개 라인 각각 → Seedance 2.0으로 4-6초 클립 생성
3. 생성된 raw 클립을 `clips/` 디렉토리에 저장 (CLIP-1_raw.mp4 ~ CLIP-8_raw.mp4)

### 3. 검수 단계
- **CLIP-5, CLIP-6 manual real-person check** (역이미지 검색)
- **CLIP-5 vs Callaway 'At Last' 차별성 검증**

### 4. 편집 단계
1. **post_production_spec.json의 edit_decision_list 따라**:
   - CLIP-1: 4초 raw → 처음 3초만 사용 (-24f 트림)
   - CLIP-2: 4초 raw → 처음 1.33초만 (-64f 트림)
   - CLIP-3, 4: 동일 패턴
   - CLIP-5~8: 트림 없이 전체 사용
2. 트랜지션 적용: dissolve / cut / fade
3. BGM + SFX 트랙 합성
4. 자막·로고·AI 표시 합성 (마지막 3초 EDIT-ONLY)
5. 컬러 그레이드 통일 적용
6. 4종 export

### 5. 검증 & 송출
- **music_rights_audit.json**: 라이선스 증빙 PENDING 3종 확보
- 최종 QA + guardrail-check 4-Part 통과 → 송출

## v0.6 시스템 활용 흐름

```
intake-router → "30초 영상" 인지
  ↓ v06_clip_strategy: single_clip_possible = false
  ↓ estimated_clip_count: 8
  ↓ clip-segmentation 필수

kkirikkiri 4명 (병렬)
  ↓ look_spec + narrative_arc (7비트)

visual-bible v1.0 잠금 + character-pool 등록

pumasi 순차:
  script-writer → 7비트 시나리오
  shot-designer → shotlist.csv (clip_id 컬럼 추가, v0.6)
    ↓ duration 검증 → 30초 초과 검출
  clip-segmentation → Pattern A + D
    ↓ 8개 클립 분할 (CLIP-1~8)
  prompt-engineer × 8 클립:
    image-prompt-foundations → cinematic-shot → 
    model-adapter → seedance-prompt
    각 클립별 first_frame_reference + Seedance 명세
  motion-director → FACS (CLIP-6만)
  editor:
    edit_decision_list 작성 (v0.6 신규)
    각 클립의 trim_in/trim_out 정확히 명시
    트랜지션 카탈로그 적용
    ↓ music-rights-check 자동
qa-review (각 클립 + 어셈블 후 전체)
guardrail-check 4-Part 통합
production-brief (clips/ 디렉토리 + clip_segmentation.json 포함)
```

## 핵심 의사결정 5가지

### 1. Pattern A + D 분할
- Pattern A (Beat-Boundary): 비트 경계를 클립 경계로 사용
- Pattern D (Detail Sequence): ECU triple을 별도 4초 클립 ×3으로

### 2. ECU 짧은 컷의 처리
1.33초 ECU 직접 생성 불가능 (Seedance 최소 4초).
**해결**: 4초 클립 생성 → 편집에서 처음 1.33초만 트림 추출.

### 3. CLIP-2/3/4 seed 42 고정
같은 캐릭터·라이팅이라 시드 고정으로 일관성. Reference image도 직전 클립의 결과 활용.

### 4. CLIP-1 ↔ CLIP-8 거울 구조
같은 위치 다른 시간 (dawn vs dusk). 30초 안에 하루를 압축. 브랜드 필름의 정서적 회수.

### 5. BGM은 편집 단계에서 한 트랙으로
8개 Seedance가 각각 BGM을 만들지 않음. BGM은 편집 단계에서 8개 클립 위에 한 트랙으로 얹음. SFX만 클립별로 분배.

## Seedance API 호출 추정

- **8 클립 × 평균 1.5 attempts = 12 API 호출**
- 클립당 처리 시간 1-3분
- 총 처리 시간 추정: **8-24분** (모델만)
- Manual check + iteration 포함 총 작업 시간: **4-7시간** (BGM 제외)

## ⚠️ 송출 전 PENDING 5가지

1. **BGM 작곡 계약서**
2. **SFX 9종 라이선스 증빙**
3. **CLIP-5, CLIP-6 manual real-person check**
4. **CLIP-5 vs Callaway 'At Last' 시각 차별성 검증**
5. **Instagram 1:1 자막 재배치**

## 시스템 출처

영상 제작 시스템 v0.6 — `/mnt/user-data/outputs/video-production-system/`

신규 스킬 (v0.6):
- **clip-segmentation** — 15초 이하 클립 자동 분할 (4 패턴)

업데이트된 스킬:
- seedance-prompt (HARD LIMIT 강조)
- shot-designer (clip_id 컬럼)
- editor (edit_decision_list 필수)
- intake-router (v06_clip_strategy)
- mv-builder (음악 분절 룰)
- production-brief (clips/ 디렉토리 구조)

기반 자료:
- 율파파 가이드 7종
- movie_seedance_pack expert-pack (오픈크랩)
- 청사진: skill_blueprint/seedance_video_director_skill.md
- AI 권리 4종 + 음악 권리
