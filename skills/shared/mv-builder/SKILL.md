---
name: mv-builder
description: Build music videos via 7-step methodology: analysis, concept, lyric mapping, motifs, shotlist, generation, editing. Clip-based mapping for videos over 15 seconds. Use for music video work.
---

# MV Builder

뮤직비디오 풀 파이프라인을 다루는 스킬. 율파파의 AI 뮤직비디오 가이드 7단계
(**음악 분석 → 컨셉/샷리스트 → 이미지 → 비디오 → 편집**)를 구조화한 것.

## v0.6 핵심: 1분 이상 뮤비는 다중 클립 + 편집

⚠️ **Seedance 2.0의 15초 HARD LIMIT**으로 인해 1분 이상 뮤비는 무조건 다중 클립.

**클립 단위 음악 매핑 룰**:
- 한 클립 ≤ 15초
- 클립 경계는 **음악의 자연 분절**(verse / chorus / bridge / 후렴 / 인트로 / 아웃트로) 또는 **마디 경계**(4마디 / 8마디)에 맞추기
- 클립 평균 8-12초 권장 (마디 단위로 떨어지는 길이)

**예시 (120 BPM, 60초 뮤비)**:
- 60초 / 8마디 (16초) → 너무 길음, 15초 초과
- 60초 / 4마디 (8초) → 적합, 7-8 클립
- 60초 / 6마디 (12초) → 적합, 5 클립

## When to use

- 1~5분 길이의 뮤직비디오 제작
- 음원이 있거나 SUNO로 생성할 음악이 있는 경우
- 컷 전환과 음악 비트의 동기화가 핵심인 영상
- 숏폼이라도 음악이 결과물의 50% 이상을 차지하는 경우

## 뮤비 vs 시네마틱: 무엇이 다른가

| 측면 | 시네마틱 (단편/광고) | 뮤직비디오 |
|------|---------------------|-----------|
| 시간 단위 | 씬 (수초~수십초) | 비트·바·소절 (수초 단위) |
| 컷 빈도 | 낮음~중간 | 높음 |
| 내러티브 | 명시적 | 암시적·정서적 |
| 일관성 | 인물·공간 일관성 중요 | 비주얼 모티프 일관성이 더 중요 |
| 사운드 | 대사·앰비언스 | 음악이 절대 기준 |

## 7-Step Pipeline

### Step 1: 음악 준비 & 분석

**Input**: 음원 파일 또는 음악 컨셉

**할 일**:
1. 장르 식별 (K-pop / 힙합 / EDM / 인디포크 / 록 / 발라드 등)
2. BPM 측정
3. 구조 분해 (Intro / Verse / Pre-Chorus / Chorus / Bridge / Outro)
4. 각 구간 길이 측정 (초 단위)
5. 정서 곡선 그리기 (각 구간의 에너지·정서)

**SUNO 스타일 태그 예시** (음원 없으면 먼저 만들기):
```
발라드: Korean ballad, piano-driven with soft strings, female vocals breathy delicate tone, 78 BPM, melancholic yet hopeful

K-pop: K-pop dance pop, synth-heavy, punchy 808 drums, female group vocals with harmonies, 122 BPM, addictive hook-driven

힙합: Korean hip-hop trap, heavy 808 bass, trap hi-hats, male rapper aggressive flow, 140 BPM half-time feel, dark atmospheric

EDM: Progressive house, massive synth leads, four-on-the-floor kick, female vocal chops, 128 BPM, euphoric festival anthem

인디 포크: Indie folk, acoustic guitar fingerpicking, male vocals raw vulnerable, 92 BPM, nostalgic storytelling

록: Alternative rock, distorted guitars, aggressive drums, male vocals clean to raspy, 136 BPM, anthemic cathartic
```

**구조 태그** (SUNO에 가사와 함께 입력):
- `[Intro]` `[Verse]` `[Pre-Chorus]` `[Chorus]` `[Bridge]` `[Outro]`

### Step 2: 컨셉 설계

**Input**: 음악 분석 결과 + 아티스트/브랜드 정보

**할 일**:
1. 비주얼 컨셉 선언문 한 줄 (예: "도심 야경 속 고독한 추격")
2. 톤·룩 결정 (kkirikkiri 호출 가능)
3. 비주얼 모티프 3~5개 (반복될 이미지)
4. 컬러 팔레트 (3~5색)
5. **퍼포먼스 vs 내러티브 비율** (예: 60:40)

**결정 매트릭스**:
| 음악 성격 | 추천 비주얼 컨셉 |
|----------|------------------|
| 발라드·인디 | 내러티브 ↑, 자연광, 정적 컷, 인물 클로즈업 |
| K-pop·EDM | 퍼포먼스 ↑, 강한 컬러, 빠른 컷, 멀티 앵글 |
| 힙합 | 도시 야경, 클로즈업 + 와이드 교차, 강한 백라이트 |
| 록 | 퍼포먼스 + 추상, 어두운 무대, 헤이즈, 백라이트 |

### Step 3: 샷리스트

**Input**: 컨셉 + 음악 구조

**할 일**: 각 음악 구간을 샷 단위로 분해. **비트당 1샷 또는 1마디당 1샷**이 기본.

예시 (3분 K-pop, 122 BPM, 약 95마디):
```
[Intro 0:00-0:15] 4샷 (도입, 천천히)
[Verse 1 0:15-0:45] 12샷 (각 8비트 단위)
[Pre-Chorus 0:45-1:00] 6샷 (점진적 클로즈업)
[Chorus 1 1:00-1:30] 16샷 (퍼포먼스 + 빠른 전환)
[Verse 2 1:30-1:55] 10샷
[Chorus 2 1:55-2:25] 16샷
[Bridge 2:25-2:45] 6샷 (정적 전환)
[Final Chorus 2:45-3:15] 18샷 (최고조)
[Outro 3:15-3:30] 3샷 (페이드)
```

각 샷은 `cinematic-shot` 스킬로 시각 명세를 채움.

### Step 4: 이미지 생성

**Input**: 샷리스트

**할 일**:
1. 각 샷의 이미지 프롬프트 작성 (`cinematic-shot` 호출)
2. **캐릭터 일관성 유지** — 동일 시드, 동일 모델, 동일 캐릭터 레퍼런스
3. 장르별 프롬프트 패턴 적용 (아래 참고)
4. 이미지 생성 → 선별 → 보정

**장르별 이미지 프롬프트 패턴**:

힙합 세트:
```
[IMG - Verse] [캐릭터 묘사] on empty urban street night, low angle,
neon reflections wet pavement, Cinestill 800T, 24mm wide --ar 16:9

[IMG - Hook] [캐릭터 묘사] intense close-up, hard light upper right,
deep shadows, gold chain detail, 50mm f/1.8, dark bokeh --ar 16:9
```

EDM 세트:
```
[IMG - Drop] Explosion of liquid neon light zero gravity,
electric blue hot pink against black, maximum saturation,
abstract energy --ar 16:9

[IMG - Breakdown] Single silhouette vast dark space,
single cyan beam from above, pool of light, dense fog,
minimalist --ar 16:9
```

인디 포크 세트:
```
[IMG - Verse] [캐릭터 묘사] walking through golden wheat field,
medium shot from behind, 35mm, Kodak Portra 160 earth tones,
overcast light --ar 16:9

[IMG - Chorus] [캐릭터 묘사] profile portrait golden hour,
sun flare, warm amber, 50mm f/1.4, Fujifilm Superia tones,
light leak --ar 16:9
```

록 세트:
```
[IMG - 퍼포먼스] Rock band dark stage, wide shot,
strong backlight through haze, red amber lighting,
[추가 디테일]
```

### Step 5: 비디오 생성

**Input**: 선별된 이미지 + 모션 의도

**할 일**:
1. 각 이미지를 첫 프레임으로 비디오 생성 (`seedance-prompt` 호출)
2. 음악 비트에 맞는 길이로 (예: 4비트 = 약 2초 @ 122 BPM)
3. 카메라 무빙 일관성 (한 컷 안에서 한 가지 무빙만)

**장르별 비디오 모션 패턴**:

힙합:
```
[VID - Verse] Handheld tracking following rapper neon alley,
low angle, wet pavement reflections, moody cyan orange,
confident swagger
```

EDM:
```
[VID - Drop] Explosion of colorful particles slow motion against black,
vivid neon, zero gravity dynamics, maximum visual energy

[VID - Breakdown] Static wide shot silhouette in fog,
single cyan beam, minimal movement, meditative stillness after chaos
```

인디:
```
[VID - Verse] Gentle handheld tracking through field,
overcast light, wind moving grass, nostalgic warm tones, gentle pace
```

### Step 6: 편집

**Input**: 생성된 비디오 클립 전체 + 음원

**할 일**:
1. 비디오 클립을 음악 타임라인에 배치
2. **컷 포인트는 비트에 맞춤** (특히 강박 비트)
3. 트랜지션:
   - 컷 (기본)
   - 매치컷 (모양·움직임 연결)
   - 디졸브 (정서 전환)
   - 화이트·블랙 플래시 (강박)
4. 컬러 그레이딩 통일
5. 사운드 디자인 (효과음, 보컬 강조)

### Step 7: 부록 — 플랫폼 변형

**Input**: 마스터 16:9 영상

**할 일**:
1. 플랫폼별 비율 변환 (`platform-adapter` 호출)
2. 후킹 0~3초 재설계 (숏폼용)
3. 자막·캡션 (인스타·틱톡)
4. 무음 자동재생 대응 (피드용)

## Output Format

```json
{
  "music_analysis": {
    "genre": "K-pop",
    "bpm": 122,
    "structure": [
      {"section": "Intro", "start": 0, "end": 15, "shots": 4},
      {"section": "Verse1", "start": 15, "end": 45, "shots": 12}
    ]
  },
  "concept": {
    "visual_statement": "...",
    "tone_keywords": [...],
    "color_palette": [...],
    "performance_ratio": "70:30"
  },
  "shotlist": [
    {
      "shot_id": "01",
      "music_section": "Intro",
      "time_in_song": "0:00-0:04",
      "duration_s": 4,
      "shot_size": "EWS",
      "image_prompt": "...",
      "video_prompt": "..."
    }
  ],
  "edit_plan": {
    "cut_strategy": "on beat",
    "transitions": [...],
    "platform_variants": ["16:9 master", "9:16 reels"]
  }
}
```

## 휴리스틱

- **첫 뮤비**: 인디 포크나 발라드처럼 BPM 낮고 컷 적은 장르가 입문에 좋음
- **퍼포먼스 영상**: 같은 동작을 여러 앵글에서 — 5~6 앵글이 보통 충분
- **내러티브 + 퍼포먼스 교차**: 코러스는 퍼포먼스, 벌스는 내러티브
- **컷 너무 빠르면 멀미** — BPM 120 이상도 매 비트마다 컷하지 말 것. 2~4비트당 1컷.
- **모티프 반복**으로 일관성 만들기 — 특정 색·물체·앵글을 코러스마다 반복

## 의존 스킬

- `cinematic-shot`: 모든 샷의 시각 명세
- `seedance-prompt`: 비디오 생성 단계
- `facs-expression`: 인물 클로즈업이 많은 경우
- `platform-adapter`: Step 7

## 오픈크랩 컨텍스트

근거 자료:
- `AI로 뮤직비디오 만들기 가이드` (5864f0bc 팩)
- 부록 페이지 (장르별 프롬프트 세트)
