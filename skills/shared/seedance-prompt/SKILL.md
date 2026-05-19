---
name: seedance-prompt
description: Generate Seedance 2.0 multimodal prompts with 4-15s HARD LIMIT awareness. 12-file input, source binding (@image1), time markers. Use as Step 4 of prompt-engineer pipeline for video generation.
---

# Seedance Prompt

Seedance 2.0의 **멀티모달 동시 입력**(이미지 9 + 비디오 3 + 오디오 3, 총 12파일)과
**소스 바인딩** 체계로 비디오 생성 프롬프트를 작성하는 스킬.

## When to use

- Seedance 2.0으로 비디오를 생성할 때
- 캐릭터·배경·카메라무빙·동작·사운드를 분리해서 지시하고 싶을 때
- 4~15초 길이의 음향 포함 영상이 필요할 때
- "@이미지1", "@비디오2" 같은 소스 바인딩이 효과적인 작업

다른 비디오 모델(Kling, Runway 등)을 쓸 경우 이 스킬의 구조 일부는 호환되지만
소스 바인딩 문법은 Seedance 전용입니다.

## Seedance 2.0 핵심 사양

### 멀티모달 동시 입력
- **이미지 최대 9장** (jpeg/png/webp/bmp/tiff/gif, 단일 < 30MB)
- **비디오 최대 3개** (mp4/mov, 480p~720p, 단일 < 50MB, 단일 ≤ 15초)
- **오디오 최대 3개** (mp3/wav, 단일 < 15MB, 총 ≤ 15초)
- **이미지+비디오+오디오 총합 ≤ 12개 파일**

### 출력 (v0.6 강조)
- **길이: 4~15초 (HARD LIMIT)** — 한 생성 클립은 **절대 15초 초과 불가**
- 해상도: 최대 2K
- 음향 효과·BGM 자동 포함 가능

### ⚠️ v0.6 핵심 룰: 15초 초과 영상은 다중 클립 + 편집

**한 번의 Seedance 생성으로 만들 수 있는 영상은 최대 15초**. 그 이상은 다음 절차:

1. **clip-segmentation** 스킬로 시나리오를 15초 이하 클립들로 분할
2. 각 클립을 별도 Seedance 호출로 생성 (각각 ≤ 15초)
3. **editor**가 편집 단계에서 컷·디졸브·페이드로 연결
4. 최종 영상 길이 = 클립 합 + 트랜지션 (이론상 무제한)

**이 룰의 함의**:
- "30초 영상 생성" 요청 = 최소 2개 클립 + 편집
- "1분 영상" = 최소 4-6개 클립 + 편집
- 클립 간 트랜지션은 cut / dissolve / fade (Seedance가 자동으로 못 함)
- 캐릭터 일관성은 시드 + reference image로 클립 간 유지

### 클립 분할 휴리스틱

| 시나리오 길이 | 권장 클립 수 | 평균 클립 길이 |
|-------------|------------|---------------|
| 15초 이하 | 1개 | 전체 |
| 16-30초 | 2-3개 | 8-12초 |
| 30-60초 | 4-6개 | 8-12초 |
| 1-3분 | 8-15개 | 7-12초 |
| 3분 이상 | 15개 이상 | 7-10초 |

**왜 8-12초가 sweet spot인가**:
- 4-5초는 너무 짧아 한 액션 완성 어려움
- 13-15초는 모델 한계 가까워 품질·일관성 저하
- 8-12초는 한 액션 + 약간의 여백, 일관성 안정적

### 검열 주의
실존 인물은 시스템이 자동 차단. **일러스트·AI 가상 캐릭터·동물·제품·장면 이미지**를 사용.

## 소스 바인딩 (Source Binding)

업로드한 각 소재에 자연어로 역할을 부여하는 방식. **Kling의 'Omni'와 유사한 메커니즘**.

문법:
```
@이미지1 @이미지2 @이미지3 ... @이미지9
@비디오1 @비디오2 @비디오3
@오디오1 @오디오2 @오디오3
```

각 소스에 역할을 명시적으로 할당:
```
@이미지1 = 첫 프레임
@이미지2 = 배경 레퍼런스
@이미지3 = 캐릭터 정면
@이미지4 = 캐릭터 측면
@비디오1 = 카메라 움직임 참조
@비디오2 = 캐릭터 동작 참조
@오디오1 = 배경음악
@오디오2 = 효과음
```

## Prompt Structure

### 풀 템플릿
```
[소스 바인딩 선언]
@이미지1 = 첫 프레임 (start frame)
@이미지2 = 캐릭터 레퍼런스
@비디오1 = 카메라 무빙 참조
@오디오1 = BGM

[샷 묘사]
Subject: ...
Action: ...
Camera: (follow @비디오1)
Lighting: ...
Style: ...
Duration: 8s
Aspect: 16:9
```

### 케이스별 구조

#### A. 단일 이미지 → 비디오 (가장 흔한 경우)
```
@이미지1 = first frame

Start from @이미지1 (a woman standing in foggy forest).
Camera slowly pushes in over 5 seconds while morning mist drifts.
Subject remains still, eyes slowly close at 4s mark.
Soft ambient forest sound, no music.
Duration: 6s, 16:9
```

#### B. 캐릭터 + 배경 분리
```
@이미지1 = character reference (front view)
@이미지2 = character reference (side view)
@이미지3 = background environment (sunset rooftop)

Character from @이미지1/@이미지2 walks across background from @이미지3.
Medium tracking shot from left to right, golden hour backlight.
Wind moves character's hair gently.
Duration: 8s, 16:9
```

#### C. 카메라 무빙 + 동작 분리 (Seedance의 강점)
```
@이미지1 = key frame (subject's pose)
@비디오1 = camera movement reference (handheld drift)
@비디오2 = subject action reference (turning to look back)

Apply camera movement from @비디오1 to subject from @이미지1.
Subject performs action from @비디오2.
Cinematic Kodak Portra grade, soft overcast lighting.
Duration: 6s, 9:16
```

#### D. 음향 포함 한 번에
```
@이미지1 = first frame
@오디오1 = piano BGM (melancholic, 78 BPM)
@오디오2 = rain ambience

Static shot of @이미지1 (figure by rainy window).
Camera holds still. Figure raises hand to glass at 3s.
Sync @오디오1 to rise in volume at 2s.
@오디오2 plays throughout.
Duration: 8s, 16:9
```

## 작성 원칙

### 1. 카메라와 동작을 분리해서 지시
영화 현장에서 **연기 감독과 촬영 감독에게 따로 지시**하듯이.
- 카메라: 어디서 어떻게 움직이는가
- 피사체: 무엇을 하는가

### 2. 시간 마커 명시
`at 2s`, `over 5 seconds`, `at the 4s mark` 같은 명시적 시간 표현.

### 3. 단일 액션 원칙
4~15초 안에 여러 사건을 욱여넣지 말 것. **하나의 변화** 또는 **하나의 무빙**만.

### 4. 첫 프레임은 강력하게
@이미지1을 첫 프레임으로 쓰면 안정성이 크게 올라감. 정지 이미지를 먼저 잘 만든 후 영상화 권장.

### 5. 오디오는 분리하면 통제력 ↑
BGM과 SFX를 한 파일에 합치지 말고 분리해서 시간 동기화.

## Output Format

```json
{
  "shot_id": "shot_001",
  "duration_s": 8,
  "aspect": "16:9",
  "source_bindings": {
    "@이미지1": "first frame: woman in foggy forest",
    "@이미지2": "character ref: side view",
    "@비디오1": "camera ref: slow push-in"
  },
  "prompt": "Start from @이미지1. Camera follows @비디오1 movement...",
  "audio_plan": {
    "@오디오1": "ambient forest sound, no music",
    "sync_notes": "..."
  },
  "expected_output": {
    "resolution": "1080p",
    "fps": 24,
    "has_sound": true
  }
}
```

## 휴리스틱

- **첫 시도면**: 이미지 1장 + 짧은 텍스트로 시작. 결과 보고 소스 추가.
- **카메라 무빙이 핵심이면**: @비디오1로 무빙 레퍼런스 따로 줄 것. 텍스트만으론 한계.
- **표정 변화가 핵심이면**: @비디오2로 동작 레퍼런스 + FACS 코드 텍스트 병행
- **음향 동기화 필요하면**: @오디오 분리 + 시간 마커 명시
- **검열 회피**: 실존 인물 모티프 피하고, "AI 생성 캐릭터", "일러스트풍" 등 명시
- **연속 샷이면**: 앞 샷의 마지막 프레임을 다음 샷의 @이미지1로 → 자연스러운 연결

## 음수 프롬프트 (Negative)

Seedance도 일반 negative 패턴 적용 가능:
```
negative: deformed face, extra limbs, flickering, low quality,
watermark, text overlay, blurry, distorted hands
```

## 의존 스킬과 다음 단계

- 비디오 생성 전에 보통 `cinematic-shot`으로 첫 프레임 이미지부터 만듦
- 표정 연기 필요하면 `facs-expression`을 비디오 동작 레퍼런스에 반영
- 뮤비 작업이면 `mv-builder`의 비디오 생성 단계에서 호출

## 오픈크랩 컨텍스트

근거 자료:
- `Seedance 2.0 프롬프팅 가이드` (2f7fabb8 팩)
- 추가 디테일은 `opencrab_get_node_context`로 특정 노드 조회
