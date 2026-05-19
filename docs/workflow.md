# Workflow Example — 30-second Brand Film

This walkthrough shows exactly which skills activate, in what order, when you ask Claude to make a 30-second brand film.

## The Request

```
User: "30초 브랜드 필름 만들고 싶어. 16:9, 회사 공식 채널용."
```

## Step-by-Step Flow

### Step 01 · intake-router

**Triggers**: Every video request.

**What happens**: Classifies the request:
- format: `cinematic_brand_film`
- duration: `30s`
- platform: `corporate_channel` (YouTube/Vimeo/website)
- aspect: `16:9`
- AI rights: `enabled` (auto-add `#광고 #AI생성` disclosure)
- **clip_strategy: multi-clip required** (30s > 15s HARD LIMIT)

**Output**: classification + clip_strategy hand-off to next skills.

**Time**: 2-3 minutes.

---

### Step 02 · kkirikkiri 4 agents (parallel)

**Triggers**: After classification, when emotional/visual direction is needed.

**Agents called**:
- **mood-curator** → 5-color palette + texture + light character
- **reference-scout** → MPA-safe references (no "in the style of [director]")
- **aesthetic-director** → consolidates above into `look_spec`
- **narrative-weaver** → emotional arc with 7 beats for 30 seconds

**Output**: 
- `look_spec.yaml` (colors, lens kit, lighting rules, grade)
- `narrative_arc.yaml` (7 beats with emotion/meaning/anchor per beat)
- `emotional_dna.yaml` (overall tone fingerprint)

**Time**: 15-30 minutes (parallel execution).

---

### Step 03 · visual-bible v1.0 LOCK + character-pool registration

**Triggers**: Once kkirikkiri outputs are consolidated.

**What happens**:
- 7-section master document created: brand_identity, color_palette, typography, look_spec, character_pool_ref, motif_library, taboos
- **Locked** — subsequent V2-Vn cannot change these
- Characters registered with `facs_defaults` and `what_to_avoid`

**Output**: `visual_bible.yaml` (LOCKED) + `character_sheets.json`

**Time**: 10-20 minutes.

---

### Step 04 · script-writer

**Triggers**: After visual-bible lock; when narrative needs to become scenes.

**What happens**:
- Translates `narrative_arc` beats into scene-level scripts
- Auto-adds subtitle, CTA, AI disclosure (`#광고 #AI생성`)
- Real-time guardrail check for forbidden phrases (Korean ad law)

**Output**: `scenes.yaml` with subtitles and CTA

**Time**: 15-25 minutes.

---

### Step 05 · shot-designer

**Triggers**: After script; when scenes need to become shots.

**What happens**:
- Decomposes scenes into shots with 5-layer spec (size/angle/lens/lighting/look)
- Auto-applies `what_to_avoid` from character-pool
- Recommends models (Nano Banana Pro vs GPT Image 2 vs Seedance)
- Adds `clip_id` column (v0.6) for clip segmentation

**Output**: `shotlist.csv` (typically 8-10 rows for 30s film)

**Time**: 15-30 minutes.

---

### Step 06 · clip-segmentation ⭐ v0.6 critical

**Triggers**: When shotlist contains rows exceeding 15s, OR when total duration > 15s.

**What happens**:
- Detects HARD LIMIT violations
- Selects from 4 patterns:
  - **Pattern A** (Beat-Boundary): use narrative beats as clip boundaries → best for 30s film
  - **Pattern B** (Action-Boundary): split mid-beat at natural action ends
  - **Pattern C** (Match-Cut): same composition different times
  - **Pattern D** (Detail Sequence): ECU triple, generate 4s and trim to 1.33s each
- Outputs detailed `clip_segmentation.json` with `seedance_generation_duration_s` and `trim_in_frames`/`trim_out_frames`

**Example for 30s brand film**: 8 generation clips + 1 edit-only segment
- CLIP-1 (Opening, 4s gen, 3s edit)
- CLIP-2/3/4 (ECU Triple ritual, 4s gen each, 1.33s edit each, seed 42 locked)
- CLIP-5 (Departure hero, 6s gen)
- CLIP-6 (Connection two-shot, 5s gen)
- CLIP-7 (Conviction still life, 4s gen)
- CLIP-8 (Dusk resolution mirror of CLIP-1, 5s gen)
- EDIT-ONLY-9 (3s anchor with subtitle + logo + AI disclosure)

**Output**: `clip_segmentation.json` with assembly order and transitions

**Time**: 10 minutes.

---

### Step 07 · prompt-engineer (4-stage pipeline × 8 clips)

**Triggers**: After clip-segmentation; for each clip.

**What happens** (per clip):
1. **image-prompt-foundations** → remove 3 ambiguity types + add shadow spec + 5-layer
2. **cinematic-shot** → unified 5-layer vocabulary
3. **model-adapter** → translate to specific model (Nano Banana Pro / Seedance 2.0)
4. **seedance-prompt** → multimodal binding with `@image1` and audio plan

Auto-applies **guardrail Part 2** (AI rights blocking).

**Output**:
- `gpt_image_prompts.jsonl` (8 lines, one per clip first frame)
- `seedance_prompts.jsonl` (8 lines, one per clip video generation)

**Time**: 30-60 minutes including generation iteration.

---

### Step 08 · motion-director (face shots only)

**Triggers**: For shots showing faces. Typically 1-2 of 8 clips.

**What happens**:
- FACS Action Units + intensity (advertising uses A-C only)
- Body motion + camera movement spec
- Auto-references character-pool's `facs_defaults`

**Example**: CLIP-6 (two-shot connection)
- CHAR-A: AU6+AU12 intensity C (subtle Duchenne smile)
- CHAR-BF: AU1+AU2 intensity B (slight eyebrow raise of recognition)
- Body: slight forward lean
- Camera: static, no movement

**Output**: `motion_directions.json`

**Time**: 10-15 minutes.

---

### Step 09 · editor + music-rights-check (auto)

**Triggers**: After clip generation, assembly time.

**What happens**:
- Generates `edit_decision_list` from `clip_segmentation.json` with precise trim points
- Transition catalog (cut/dissolve/fade) applied per clip boundary
- BGM + SFX + text overlays + logo + AI disclosure composed
- **music-rights-check auto-called** to verify license across 5 categories

**Output**:
- `post_production_spec.json` with full edit_decision_list
- `music_rights_audit.json` with PASS/WARN/BLOCK per audio track

**Time**: 1-2 hours.

---

### Step 10 · qa-review + guardrail-check + production-brief

**Triggers**: Pre-delivery final check.

**What happens**:
- **qa-review** runs 6-dimension check (character consistency, artifacts, lipsync, cut rhythm, prompt drift, evidence) — 3-cycle limit
- **guardrail-check 4-Part** final integration:
  - Part 1: Korean ad compliance
  - Part 2: AI rights (4 sources)
  - Part 3: Visual (real-person, logos, minors)
  - Part 4: AI generation checklist (23 items)
- **production-brief** packages everything into handoff zip

**Output**: 
```
campaign_2026Q3_BrandFilm/
├── production_brief.md
├── visual_bible.yaml (LOCKED)
├── character_sheets.json
├── shotlist.csv
├── gpt_image_prompts.jsonl
├── seedance_prompts.jsonl
├── clip_segmentation.json       ← v0.6
├── clips/                       ← v0.6 (8 raw clips)
│   ├── CLIP-1_raw.mp4
│   ├── ...
│   └── CLIP-8_raw.mp4
├── post_production_spec/
├── qa_reports/
├── music_rights_audit.json
└── final_outputs/
    ├── master_16x9.mp4
    ├── 9x16_vertical.mp4
    └── 1x1_square.mp4
```

**Time**: 30-60 minutes.

---

## Total

- **Single 30-second brand film**: 4-7 hours (excluding BGM composition)
- **Skills auto-activated**: ~20 skills (some called multiple times)
- **Standard deliverable**: 5 files + clips/ directory + final outputs

## Decision Points

| Situation | What changes |
|-----------|--------------|
| Single one-off film | `copy-tone-check` and `series-closer` not called |
| Series V1 (first episode) | Full pipeline + `visual-bible` lock |
| Series V2 to V(n-1) | kkirikkiri partially reused from V1 LOCKED |
| Series V(n) (final) | `series-closer` 3-Type analysis added |
| Music video | `mv-builder` 7-step replaces standard flow |

## Common Pitfalls

1. **Forgetting clip-segmentation for 16+ second videos** → Seedance fails silently or produces garbage
2. **Not locking visual-bible after V1** → V2-Vn drift in look/feel
3. **Skipping motion-director for face shots** → uncanny valley expressions
4. **Missing music-rights-check** → potential takedowns post-publication
5. **Not running guardrail-check Part 4** → AI disclosure missed on Korean ads

This is exactly why each skill exists.
