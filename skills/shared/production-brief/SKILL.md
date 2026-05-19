---
name: production-brief
description: Package video deliverables in 5 standard files (brief, characters, shotlist, image/video prompts) plus clip_segmentation.json and clips/ directory. Use at project end for client handoff.
---

# Production Brief

영상 제작 프로젝트의 **표준 산출물 파일들을 정의·생성**하는 스킬.
청사진이 명시한 5개 표준 파일을 그대로 만들어, 어느 외주·후속 작업자라도 같은 포맷으로 받아볼 수 있게 합니다.

## When to use

- 시리즈·캠페인의 인계 단계
- 외주에 작업 일부를 위임할 때
- 후속 시즌 작업을 위한 자산 정리
- 클라이언트 최종 납품 패키지

이 스킬은 **이미 만들어진 산출물을 표준 파일로 정리하는 것**이지, 새로 만드는 게 아닙니다.

## 청사진 근거

청사진 `subagent_spec.json`의 `outputs` 필드에 명시된 5개 파일:

```json
"outputs": [
  "production_brief.md",
  "character_sheets.json",
  "shotlist.csv",
  "gpt_image_prompts.jsonl",
  "seedance_prompts.jsonl"
]
```

## 5개 표준 산출물 파일

### 1. `production_brief.md`

프로젝트 전체 개요를 한 문서로 요약.

**구조**:
```markdown
# {Campaign Name} Production Brief

## Meta
- Project ID: ...
- Client: ...
- Date: ...
- Version: ...

## Mission
- Logline: ...
- Theme: ...
- Genre: ...
- Target Platform: ...
- Total Running Time: ...
- Number of Episodes: ...

## Target Audience
- Primary: ...
- Secondary: ...
- Tone Floor / Ceiling: ...

## Visual Bible Reference
→ visual-bible v1.0 (locked at YYYY-MM-DD)

## Episode List
| # | Title | Duration | Target | Status |
| V1 | ... | 15s | ... | locked |
| V2 | ... | 15s | ... | drafted |

## Deliverables
- Master files (9:16, 1080p, ProRes 422 HQ)
- Platform variants (Instagram Reels, YouTube Shorts, TikTok)
- Audio: BGM tracks, SFX

## Guardrails Reference
→ guardrail-check categories: golf_membership, general
→ Forbidden phrases: ...

## Production Pipeline
- Phase 1: Concept (kkirikkiri)
- Phase 2: Script & Shotlist (pumasi)
- Phase 3: Image Generation (GPT Image 2 / Nano Banana Pro)
- Phase 4: Video Generation (Seedance 2.0)
- Phase 5: Edit & Post (post-production-spec)
- Phase 6: QA & Delivery (qa-review)

## Approval Chain
- Creative Lead: ...
- Client Contact: ...
- Approval Stages: ...

## Schedule
- Kickoff: ...
- Milestones: ...
- Delivery: ...

## Risk Register
- Identified risks + mitigation plans
```

### 2. `character_sheets.json`

character-pool 스킬의 출력을 JSON으로 정리.

```json
{
  "pool_version": "1.0",
  "campaign_id": "FMGmember_2026Q3",
  "characters": [
    {
      "character_id": "FMG_CHAR_A_REVIEWER",
      "role": "회원권 검토자",
      "locked": true,
      "appears_in": ["V1-S1", "V1-S2", "V1-S3", "V1-S4", "V6-S1"],
      "demographics": {...},
      "face": {...},
      "wardrobe": {...},
      "facs_defaults": {...},
      "what_to_avoid": [...]
    }
  ]
}
```

(상세 구조는 `character-pool-SKILL.md` 참고)

### 3. `shotlist.csv`

샷 단위 작업 표. 스프레드시트 호환.

**컬럼**:
```
episode, shot_id, time_in, time_out, duration_s, 
shot_size, angle, lens, aperture, movement, 
lighting, look, character_ids, central_motif, 
location, time_of_day, weather, props,
audio_notes, transition_to_next, post_text_overlay,
image_model, video_model, status, notes
```

**예시 행**:
```csv
V1,S1,00:00:00:00,00:00:02:00,2.0,
ECU,Top-down 45°,100mm macro,f/2.8,static,
"soft window light L + warm tungsten R","Kodak Vision3 250D low contrast",
"FMG_CHAR_A_REVIEWER","M3 도구 디테일",
"클럽하우스 라운지 실내",dawn,clear,"fountain pen, leather notebook",
"pen friction SFX","match cut to S2","none (CTA 영역 아님)",
"GPT Image 2","Seedance 2.0",approved,"hand only, no face visible"
```

### 4. `gpt_image_prompts.jsonl`

이미지 프롬프트 한 줄 = 한 JSON 객체.

```jsonl
{"shot_id":"V1-S1","model":"gpt_image_2","prompt":"Extreme close-up of...","negative":"text, watermark","aspect":"9:16","seed":null,"notes":"first frame for Seedance"}
{"shot_id":"V1-S3","model":"nano_banana_pro","prompt":"Over-the-shoulder...","negative":"face visible","aspect":"9:16","seed":42,"notes":"character ref locked"}
{"shot_id":"V1-S4","model":"gpt_image_2","prompt":"Wide shot of a single man...","negative":"second person","aspect":"9:16","seed":null,"notes":"golden hour exterior"}
```

**필수 필드**: shot_id, model, prompt, aspect
**선택 필드**: negative, seed, notes, reference_images

### 5. `seedance_prompts.jsonl`

Seedance 비디오 프롬프트 한 줄 = 한 JSON 객체.

```jsonl
{"shot_id":"V1-S1","model":"seedance_2","source_bindings":{"@이미지1":"V1-S1 first frame"},"prompt":"Start from @이미지1. Hold framing static. Pen makes one writing motion...","duration_s":2,"aspect":"9:16","audio_plan":"pen friction SFX, no music","notes":"single action principle"}
{"shot_id":"V1-S4","model":"seedance_2","source_bindings":{"@이미지1":"V1-S4 first frame"},"prompt":"Start from @이미지1. Very slow push-in over 4 seconds...","duration_s":4,"aspect":"9:16","audio_plan":"footsteps + wind + piano swell","notes":"BGM enters at 3s"}
```

## 인계 패키지 (Delivery Package)

표준 인계 시 함께 가는 자료:

```
campaign_2026Q3_FMGmember/
├── production_brief.md
├── visual_bible.yaml
├── character_sheets.json
├── shotlist.csv
├── gpt_image_prompts.jsonl
├── seedance_prompts.jsonl
├── clip_segmentation.json          ← v0.6 신규
├── post_production_spec/
│   ├── V1_spec.json (edit_decision_list 포함)
│   ├── V2_spec.json
│   └── ...
├── qa_reports/
│   ├── V1_qa.json
│   └── ...
├── clips/                          ← v0.6 신규
│   ├── V1/
│   │   ├── CLIP-1_raw.mp4 (Seedance 원본, ≤15초)
│   │   ├── CLIP-2_raw.mp4
│   │   └── ...
│   ├── V2/
│   │   └── ...
│   └── ...
├── final_outputs/
│   ├── V1_master_9x16.mp4 (편집 완료 마스터)
│   ├── V1_variants/
│   │   ├── V1_4x5.mp4
│   │   └── V1_1x1.mp4
│   └── ...
└── README.md
```

**v0.6에서 변경된 점**:
- 새 파일: `clip_segmentation.json` (각 클립 정의 + 편집 순서)
- 새 디렉토리: `clips/` (Seedance 원본 클립 보관, ≤15초씩)
- post_production_spec에 edit_decision_list 포함
- final_outputs는 **편집 완료된 마스터**만 (Seedance 원본 아님)

## Operations

### 1. 초기화
```
input: campaign_id + 1편 작업 결과
process: 5개 파일의 빈 템플릿 생성
output: campaign_2026Q3/ 디렉토리 + 빈 파일 5개
```

### 2. 자동 채우기
```
input: 다른 스킬 호출 결과 (character-pool, shot-designer, prompt-engineer 등)
process: 각 결과를 해당 파일로 라우팅
output: 부분 채워진 파일들 + 빈 필드 리스트
```

### 3. 검증 (validate)
```
process: 
  - shotlist.csv의 모든 shot_id가 gpt_image_prompts.jsonl과 seedance_prompts.jsonl에 있는가
  - character_sheets.json의 ID들이 shotlist.csv의 character_ids와 일치하는가
  - production_brief.md의 episode list와 shotlist.csv의 episode 컬럼이 일치하는가
output: 누락·불일치 리포트
```

### 4. 인계 패키징 (package)
```
process: 모든 파일 + 디렉토리를 위 트리 구조로 정리 → zip
output: campaign_2026Q3_FMGmember.zip
```

## 휴리스틱

- **JSONL은 한 줄에 하나** — 일부만 가져갈 때 편리, 스트리밍 가능
- **CSV는 컬럼 순서 유지** — 외주가 스크립트로 처리할 때 일관성
- **production_brief.md는 사람이 읽음** — JSON·CSV는 자동화용. 두 종류 다 필요.
- **버전 표시는 시맨틱하게** (v1.0 = 잠금, v1.1 = 마이너 수정, v2.0 = 메이저 개편)
- **README.md 한 장 필수** — "이 패키지를 어떻게 읽을지" 1쪽 안내

## 시스템 호출

이 스킬은 다른 스킬들의 출력을 모아 정리하는 **수집·정리자** 역할:

- `character-pool` → character_sheets.json
- `series-variation` → production_brief.md의 Episode List
- `pumasi.shot-designer` → shotlist.csv
- `pumasi.prompt-engineer` → gpt_image_prompts.jsonl, seedance_prompts.jsonl
- `post-production-spec` → post_production_spec/ 하위
- `qa-review` → qa_reports/ 하위
- `visual-bible` → visual_bible.yaml
- `guardrail-check` 결과 → production_brief.md의 Guardrails 섹션

## 청사진 매핑

| 청사진 outputs | 우리 파일 | 생성 책임 |
|---------------|----------|----------|
| production_brief.md | ✅ | 이 스킬 (수집·통합) |
| character_sheets.json | ✅ | character-pool |
| shotlist.csv | ✅ | pumasi.shot-designer |
| gpt_image_prompts.jsonl | ✅ | pumasi.prompt-engineer + model-adapter |
| seedance_prompts.jsonl | ✅ | pumasi.prompt-engineer + seedance-prompt |

## 오픈크랩 컨텍스트

- 표준 산출물이 정리되면 오픈크랩 팩으로 ingest해서 후속 캠페인의 템플릿으로 사용
- 시리즈가 끝나면 production_brief.md를 ingest → 차기 시즌 기획의 컨텍스트
