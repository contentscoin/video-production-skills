# FMGmember Brand Film 30s — Production Brief (v0.6)

## Meta
- **Project ID**: FMGmember_BrandFilm_30s
- **Client**: FMGmember.kr (골프회원권 B2B 서비스)
- **Date**: 2026-05-19 (v0.6 업데이트)
- **System Version**: Video Production System v0.6
- **Project Type**: 신규 단편 (V1~V6 시리즈와 별개)

## v0.5 → v0.6 핵심 변경

⚠️ **이 패키지는 v0.6에서 재구성됨**. v0.5 버전과 차이:

| | v0.5 (이전) | v0.6 (현재) |
|---|------|------|
| 영상 구조 | 9 shots 단일 영상 가정 | **8 Seedance 클립 + 1 edit-only segment** |
| Seedance 호출 | 1번 (불가능) | **8번** (각 4-15초) |
| 편집 단계 | 선택적 | **필수** (edit_decision_list) |
| 클립 디렉토리 | 없음 | **clips/** 디렉토리에 8 raw clips |
| ECU triple 처리 | 1.33초 직접 생성 (불가능) | **4초 생성 후 1.33초 트림** |

**왜 변경됐나**: Seedance 2.0의 HARD LIMIT은 4-15초. 30초 영상은 절대 단일 생성 불가능. v0.5는 이를 인지하지 못한 명세였음.

## Mission
- **Logline**: 30초 안에 FMGmember의 본질 — 신중한 선택이 만드는 깊은 시간 — 을 정서적 브랜드 필름으로 전달한다.
- **Theme**: earned stillness (노력해서 얻은 고요함)
- **Genre**: 시네마틱 브랜드 필름
- **Target Platform**: 회사 공식 채널 (YouTube, Vimeo, 자사 웹사이트, LinkedIn) + Instagram 1:1 재프레이밍
- **Duration**: 30초
- **Aspect**: 16:9 (마스터) + 1:1 (Instagram 변형)

## v0.6 클립 분할 (Pattern A + D)

8 Seedance 클립으로 분할:

| Clip | Beat | Gen Duration | Edit Duration | Trim | 처리 |
|------|------|--------------|---------------|------|------|
| CLIP-1 | Opening | 4s | **3s** | 마지막 24f 자름 | 단일 위치 (dawn) |
| CLIP-2 | Ritual (pen) | 4s | **1.33s** | 마지막 64f 자름 | ECU triple 1 (seed 42) |
| CLIP-3 | Ritual (cup) | 4s | **1.33s** | 마지막 64f 자름 | ECU triple 2 (seed 42) |
| CLIP-4 | Ritual (light) | 4s | **1.33s** | 마지막 64f 자름 | ECU triple 3 (seed 42) |
| CLIP-5 | Departure (hero) | 6s | **6s** | 트림 없음 | Hero shot, manual check |
| CLIP-6 | Connection | 5s | **5s** | 트림 없음 | Two-shot, manual check ×2 |
| CLIP-7 | Conviction | 4s | **4s** | 트림 없음 | Still life |
| CLIP-8 | Resolution | 5s | **5s** | 트림 없음 | Dusk (mirror of CLIP-1) |
| EDIT-ONLY | Anchor | — | **3s** | — | 후처리 합성 |

**Total Seedance generation: 36초** (실제 사용은 30초)
**Total Seedance API calls: 8회**

## 7비트 시네마틱 구조

| Beat | Time | Clip | Emotion |
|------|------|------|---------|
| 1. Opening | 0-3s | CLIP-1 | 정적·기대 |
| 2. Ritual | 3-7s | CLIP-2 + CLIP-3 + CLIP-4 (ECU triple) | 집중·신중함 |
| 3. Departure | 7-13s | CLIP-5 (hero) | 결심·시작 |
| 4. Connection | 13-18s | CLIP-6 | 만남·신뢰 |
| 5. Conviction | 18-22s | CLIP-7 | 확신 |
| 6. Resolution | 22-27s | CLIP-8 | 회수·소속감 |
| 7. Brand Anchor | 27-30s | EDIT-ONLY | 정착 |

## Tone
- **Floor**: 정중함
- **Ceiling**: 절제된 자신감
- **Character**: earned stillness, considered choice, inheritable confidence
- **Forbidden**: 과장된 흥분, 직접적 영업, 가벼움

## Visual Bible (v1.0 단편용)
- **Color**: `#0B1A14` / `#C9A961` / `#E8E3D7` / `#5A6B5E` / `#1A1A1A`
- **Look**: Kodak Vision3 250D, low contrast 0.85, lifted shadows +15 IRE
- **Lens Kit**: 35mm / 50mm / 85mm / 100mm macro
- **Movement**: static or very slow push-in
- **BGM**: Neoclassical 72 BPM, solo piano + sustained cello

## Character Pool
- **FMG_CHAR_A_REVIEWER** (V1~V6 시리즈에서 재활용): CLIP-2/3/5/6/8
- **FMG_CHAR_BF_COMPANION** (신규): CLIP-6에만

## Copy & Subtitles

**유일한 자막** (27-30s, EDIT-ONLY segment):
- 메인: "선택은 신중하게, 시간은 깊게" (15자)
- CTA: "FMGmember.kr"
- AI 표시: "#광고 #AI생성" (top-right, opacity 0.7)

## Audio

**BGM** (자체 작곡, 25초):
- Neoclassical cinematic, 72 BPM
- Solo piano + sustained cello
- 구조: 5s silence → 5s piano fade in → 10s cello entry → 18s build → 22s peak → 27s resolve
- License: PASS_PROVISIONAL (작곡 계약서 PENDING)
- **편집 단계에서 8개 클립 위에 한 트랙으로 얹음** (Seedance가 클립별로 만들지 않음)

**SFX 8종** (모두 royalty-free):
- 각 클립별 적용: birdsong (CLIP-1), pen friction (CLIP-2), porcelain tap (CLIP-3), footsteps grass (CLIP-5), wind (CLIP-5,6), subtle laugh (CLIP-6, human voice library), paper rustle (CLIP-7), evening ambient (CLIP-8)
- 모두 PASS_IF_VERIFIED

## Production Pipeline (v0.6)

```
Phase 0: intake-router → 30초 인지 → v06_clip_strategy → clip-segmentation 필수
Phase 1: kkirikkiri 4명 → look_spec + narrative_arc (7비트)
Phase 2: visual-bible v1.0 잠금
Phase 3: character-pool (CHAR-A 재활용 + CHAR-BF-COMPANION 신규)
Phase 4: pumasi 순차:
  script-writer (7비트 시나리오)
  shot-designer (9행 shotlist with clip_id 컬럼)
  ↓ duration 초과 자동 검출 → clip-segmentation 호출
  clip-segmentation (Pattern A + D → 8 클립 분할)
  prompt-engineer × 8 클립 (각각 image + Seedance)
  motion-director (FACS, CLIP-6만)
  editor (edit_decision_list + 트랜지션 + 트림)
  ↓ music-rights-check 자동
Phase 5: qa-review (각 클립 + 어셈블 후 전체)
Phase 6: guardrail-check 4-Part 통합
Phase 7: production-brief (clips/ 디렉토리 포함)
```

⚠️ copy-tone-check + series-closer는 단편이라 호출 안 함.

## 실제 작업 흐름 (시간 추정)

| 단계 | 추정 시간 |
|------|----------|
| 8 이미지 생성 (Nano Banana Pro) | 30-60분 (iteration 포함) |
| 8 Seedance 클립 생성 | 8-24분 (모델 처리 + 재시도 1.5배) |
| Manual real-person check (CLIP-5, 6) | 15-30분 |
| 편집·어셈블 (edit_decision_list 따라) | 1-2시간 |
| BGM 작곡 (외주 또는 자체) | 별도 |
| SFX 준비 | 30분 |
| 컬러 그레이드·자막·로고 합성 | 1-2시간 |
| 4종 export | 30분 |
| **총 (BGM 제외)** | **4-7시간** |

## Guardrails Final Status

### Part 1: 한국 광고 ✅ PASS

### Part 2: AI 권리 4종
- ✅ OpenAI Usage Policies: PASS
- ⚠️ SAG-AFTRA AI: CLIP-5, CLIP-6 real-person manual check
- ✅ MPA Copyright: 감독·작품명 0건
- ⚠️ Vimeo AUP: 라이선스 증빙 PENDING

### Part 3: 시각 ⚠️ Manual check

### Part 4: AI 생성 체크리스트 ⚠️ 진행 중

**Overall**: PASS_WITH_PENDING_MANUAL_CHECKS_AND_LICENSE_VERIFICATIONS

## Risk Register

| 리스크 | 영향 | 완화 |
|-------|------|------|
| CLIP-5 hero shot vs Callaway 'At Last' 우연 닮음 | Medium | 시각 차별성: lower-third 인물 배치, 6초 짧은 페이싱 |
| CLIP-2/3/4 캐릭터 일관성 (3개 별도 클립) | Medium | seed 42 고정 + character-pool reference 동일 사용 |
| Seedance 학습 데이터 권리 (MPA 경고) | Medium | qa-review에서 결과물 시각 검수 |
| ECU triple 컷 리듬 (1.33초 ×3) | Low-Medium | 편집에서 정확한 프레임 트림 + 음악 비트 동기화 |
| BGM 작곡 계약서 PENDING | High | 송출 전 확보 필수 |

## File Inventory (v0.6)

```
fmg_brand_film_30s/
├── README.md                              (인계 안내)
├── production_brief.md                    (이 파일)
├── clip_segmentation.json                 ⭐ v0.6 신규 - 8 클립 분할 명세
├── shotlist.csv                           BF30-S1~S9 + clip_id 컬럼
├── gpt_image_prompts.jsonl                이미지 프롬프트 8개 (clip_id 참조)
├── seedance_prompts.jsonl                 영상 프롬프트 8개 (clip_id + 트림 명세)
├── post_production_spec.json              ⭐ v0.6 - edit_decision_list 포함
└── music_rights_audit.json                음악 권리 점검
```

⚠️ **이 패키지가 생성된 후 추가로 필요한 디렉토리**:

```
fmg_brand_film_30s/
├── clips/                                 ⭐ Seedance 생성 후 채워짐
│   ├── CLIP-1_raw.mp4 (4초)
│   ├── CLIP-2_raw.mp4 (4초)
│   ├── CLIP-3_raw.mp4 (4초)
│   ├── CLIP-4_raw.mp4 (4초)
│   ├── CLIP-5_raw.mp4 (6초)
│   ├── CLIP-6_raw.mp4 (5초)
│   ├── CLIP-7_raw.mp4 (4초)
│   └── CLIP-8_raw.mp4 (5초)
└── final_outputs/                         ⭐ 편집 완료 후
    ├── BF30_master_16x9.mp4 (30초 마스터)
    ├── BF30_4k.mp4
    ├── BF30_1x1_instagram.mp4
    └── BF30_linkedin.mp4
```

## Next Actions (실무 체크리스트)

1. ✅ **8 이미지 생성 (Nano Banana Pro)**:
   - CLIP-1 + CLIP-8 먼저 (location 일관성)
   - CLIP-2 + CLIP-3 + CLIP-4 연속 (seed 42, ECU 일관성)
   - CLIP-5 (hero, iteration 많이 필요할 수 있음)
   - CLIP-6 + CLIP-7

2. ✅ **8 Seedance 클립 생성**:
   - 각 first frame을 @이미지1로
   - 각 prompt와 duration 따라
   - clips/ 디렉토리에 저장

3. ✅ **Manual checks**:
   - CLIP-5 real-person likeness (역이미지 검색)
   - CLIP-5 vs Callaway 'At Last' 차별성
   - CLIP-6 두 인물 real-person likeness

4. ✅ **BGM 작곡 의뢰**: 25초, 72 BPM, neoclassical

5. ✅ **SFX 8종 확보**: Epidemic Sound 등

6. ✅ **편집·어셈블**: edit_decision_list 따라 정확히
   - 트랜지션 적용 (dissolve, cut, fade)
   - 트림 정확하게 (CLIP-1: -24f, CLIP-2/3/4: -64f씩)

7. ✅ **자막·로고·AI 표시 합성** (27-30s segment)

8. ✅ **컬러 그레이드 통일 적용**

9. ✅ **4종 Export**: 16:9 1080p / 4K / 1:1 / LinkedIn

10. ✅ **최종 QA + 라이선스 증빙 정리 → 송출**
