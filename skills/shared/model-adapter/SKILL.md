---
name: model-adapter
description: Adapt prompts for AI models: GPT Image 2, Nano Banana Pro, Seedance 2.0/1.5 Pro, Kling 3.0. Auto-blocks director/film names for MPA safety. Use as Step 3 of prompt-engineer pipeline.
---

# Model Adapter

이미지·비디오 생성 모델 **각각의 특성과 최적 프롬프트 패턴**을 다루는 스킬.
같은 의도라도 GPT Image 2, Nano Banana Pro, Seedance 2.0, Kling 3.0은 각자 다른 입력 형식을 선호합니다.

## When to use

- 모델 독립 프롬프트(image-prompt-foundations 출력)를 특정 모델용으로 최종 변환할 때
- 같은 컷을 여러 모델로 시도하면서 결과 비교할 때
- 새 모델이 출시되어 어휘·문법을 업데이트할 때

이 스킬은 **image-prompt-foundations 다음 단계**. 모호함 제거된 구체 프롬프트를 모델 특성에 맞게 다듬습니다.

## 청사진 근거

청사진(`seedance_video_director_skill.md`)이 명시한 책임:
- `image_prompting` (특히 GPT Image 2를 첫 단계로 지정)
- `seedance_prompting` (소스 바인딩·타임라인 분절)

그리고 외부 스냅샷에서 확인된 모델:
- ByteDance Seedance 2.0 / 1.5 Pro (공식 launch 문서)
- OpenAI GPT Image 2

## 모델별 프로필

### 🎨 GPT Image 2 (OpenAI)

**강점**:
- 텍스트 렌더링 정확도 (한글 포함, 단 100% 보장 아님)
- 캐릭터 일관성 (멀티턴 편집)
- 정확한 구도 지시 이해
- 스타일 트랜스퍼 (레퍼런스 이미지 기반)

**약점**:
- 매우 사실적인 인물 사진 → 위상 약함
- 검열 강도 높음 (실존 인물 차단)

**프롬프트 패턴**:
```
[Subject]: 자연어 묘사, 명확한 명사 + 형용사
[Style]: "in the style of ~", 또는 레퍼런스 명시 (영화 제목, 사진작가)
[Composition]: rule of thirds, low angle, etc.
[Quality]: 명시 불필요 (high quality 같은 단어는 무시됨)
```

**예시**:
```
A man in his 50s reading a newspaper at a cafe table, viewed from over his shoulder. 
Wide shot, 35mm lens, soft morning light through cafe window casting long shadow 
across the table. Style: Wong Kar-wai cinematography, warm tungsten + cool window light contrast.
```

**용도 권장**:
- 캐릭터 시트 (multi-turn edit으로 정밀)
- 스타일 바이블 키프레임
- 텍스트가 있어야 하는 컷 (포스터 등)

### 🍌 Nano Banana 2 / Pro (Google)

**강점**:
- 사실적 인물 사진 품질
- 자연 풍경·환경
- 빠른 생성 속도

**약점**:
- 텍스트 렌더링 (한글 거의 못 함)
- 복잡한 멀티 액션 (한 컷에 여러 동작)

**프롬프트 패턴**:
```
간결한 자연어, 키워드 나열보다 문장 형식 선호.
스타일 레퍼런스는 작가·감독·필름 스톡으로.
종횡비는 --ar 16:9 같은 플래그.
```

**예시**:
```
A 50-year-old Korean man in navy cashmere sweater reading the Wall Street Journal 
at a cafe table, over-the-shoulder medium shot, soft morning window light, 
Kodak Vision3 250D, low contrast, lifted shadows --ar 16:9
```

**용도 권장**:
- 사실적 캐릭터 컷 (얼굴 식별 안 되는 OTS, 옆모습)
- 풍경·환경 와이드
- Seedance 2.0의 @이미지 입력용 첫 프레임

### 🎬 Seedance 2.0 (ByteDance)

**강점** (1.5 Pro 대비 차이점):
- 멀티모달 동시 입력: 이미지 9 + 비디오 3 + 오디오 3, 총 12파일
- 소스 바인딩 (@이미지1 = 첫 프레임)
- 4~15초 출력, 최대 2K
- 음향(BGM·SFX) 자동 포함 옵션

**약점**:
- 실존 인물 검열 강도 매우 높음
- 한 클립 내 복잡한 시퀀스는 분절 필요

**프롬프트 패턴**: `seedance-prompt` 스킬 참고.

### 🎵 Seedance 1.5 Pro (ByteDance, 공식 launch 정보)

**1.5 Pro 핵심 차별** (`bytedance_seedance_15_launch.txt` 근거):
- **joint audio-visual generation** — 텍스트·이미지 입력에서 오디오·비주얼을 함께 생성
- **audio-synchronized generation** — 음원과 비디오 자동 동기화
- **breakthroughs in audio-visual synergy, visual impact, narrative coherence**
- 1.0은 "performance floor" (motion 안정성), 1.5 Pro는 "performance ceiling" (시각 임팩트·모션 효과)

**2.0과의 차이**:
- 1.5 Pro는 음향 합성에 강점, 멀티모달 입력 채널은 2.0보다 제한적
- 2.0은 멀티모달 동시 입력의 확장이 핵심

**선택 기준**:
- 음악·BGM 동기화가 핵심 → 1.5 Pro
- 캐릭터·배경·카메라무빙·동작 분리 지시 → 2.0

### 🎥 Kling 3.0 (참고)

**강점**:
- "Omni" 매커니즘 (Seedance 소스 바인딩의 원조)
- 인물 모션의 자연스러움
- 립싱크 품질

**약점**:
- 출력 길이 제한
- 검열 정책 변동성

**Seedance와의 호환성**:
Seedance 소스 바인딩(`@이미지1` 등)은 Kling Omni와 매커니즘이 유사. 두 모델 간 프롬프트 변환 비교적 쉬움.

## 모델 선택 매트릭스

| 작업 | 1순위 | 2순위 |
|------|------|------|
| 캐릭터 시트 (정면·측면·후면) | GPT Image 2 | Nano Banana Pro |
| 사실적 얼굴 클로즈업 (AI 인물) | Nano Banana Pro | GPT Image 2 |
| 풍경·환경 와이드 | Nano Banana Pro | GPT Image 2 |
| 텍스트·로고가 있는 정지 이미지 | GPT Image 2 | (후처리 합성) |
| 음향 포함 짧은 영상 | Seedance 1.5 Pro | Seedance 2.0 |
| 카메라·동작 분리 지시 영상 | Seedance 2.0 | Kling 3.0 |
| 립싱크가 핵심인 영상 | Kling 3.0 | Seedance 2.0 |
| 멀티 레퍼런스 입력 영상 | Seedance 2.0 | Kling Omni |

## 변환 패턴: 같은 컷, 다른 모델

**원본 (모델 독립)**:
```
A 50-year-old Korean man reading a newspaper at a cafe table, 
over-the-shoulder medium shot, soft morning window light from left, 
warm tungsten desk lamp from right, Kodak Vision3 250D look, low contrast, 16:9
```

**→ GPT Image 2 변환**:
```
Over-the-shoulder view of a 50-year-old Korean man in a navy cashmere sweater, 
reading a folded newspaper at a wooden cafe table. Medium shot composition.
Lighting: soft north-facing window light from the left, warm tungsten lamp from upper right.
Style: in the style of Wong Kar-wai cinematography, Kodak Vision3 250D film stock,
low contrast, slightly lifted shadows. Aspect ratio: 16:9.
```

**→ Nano Banana Pro 변환**:
```
50-year-old Korean man in navy cashmere sweater reading newspaper at cafe table,
over-the-shoulder medium shot, soft window light left + warm lamp right,
Kodak Vision3 250D, low contrast, lifted shadows --ar 16:9
```

**→ Seedance 2.0 변환 (영상화)**:
```
@이미지1 = first frame (above generated image)

Start from @이미지1. Camera holds still in over-the-shoulder position. 
The man turns one page of the newspaper over 2 seconds, then resumes reading. 
Soft ambient cafe sound, distant espresso machine. No music.

Duration: 5s
Aspect: 16:9
```

## Output Format

```json
{
  "source_prompt": "모델 독립 프롬프트",
  "target_model": "gpt_image_2",
  "adapted_prompt": "...",
  "rationale": "이 모델 변환에서 강조한 점 / 생략한 점",
  "alternatives": {
    "nano_banana_pro": "...",
    "seedance_2": "..."
  },
  "warnings": [
    "GPT Image 2는 실존 인물 닮음 차단. 캐릭터 이름 명시 피하기."
  ]
}
```

## 휴리스틱

- **GPT Image 2는 문장형, Nano Banana는 키워드형** — 같은 의미라도 형식 다름
- **Seedance는 항상 @이미지1을 첫 프레임으로** — 정지 이미지 먼저 만들고 영상화
- **검열 회피**: 모든 모델에서 "실존 인물 이름·닮음" 절대 금지. "AI 생성 가상 인물" 명시
- **새 모델 출시 시**: 1~2주 안에 모델 프로필 업데이트. 외부 자료(공식 launch, 사용자 가이드)를 오픈크랩으로 ingest해서 컨텍스트화.

## 시스템 호출

- `prompt-engineer` (pumasi)의 모든 프롬프트 작성 마지막 단계
- `image-prompt-foundations`의 출력을 입력으로 받음
- `seedance-prompt` 스킬은 이 스킬의 Seedance 변환 부분을 더 깊이 다룸
- `qa-review`가 모델별 artifact 체크 시 이 스킬의 프로필 참조

## 오픈크랩 컨텍스트

근거 자료:
- `notion_gpt_image_2_prompt_guide.md` (movie_seedance_pack) — GPT Image 2 전용
- `notion_image_prompt_guide.md` — 일반 원칙
- `bytedance_seedance_15_launch.txt` — 1.5 Pro 공식 정보
- `notion_seedance_2_prompt_guide.md` — 2.0 가이드
