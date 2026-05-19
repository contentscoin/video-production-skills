---
name: cinematic-shot
description: Specify cinematic shots in 5 layers: size, angle, lens, lighting, look. Use when designing shots or as Step 2 of prompt-engineer pipeline. Unified vocabulary for visual specs.
---

# Cinematic Shot

영화적 한 컷의 시각 명세를 작성하는 스킬. **샷 사이즈 → 앵글 → 렌즈 → 조명 → 룩** 5레이어로
프롬프트를 구조화합니다. Nano Banana 2/Pro, GPT-Image-2 등 어떤 이미지 생성 모델에든 적용 가능합니다.

## When to use

- 단일 시네마틱 이미지/영상의 프롬프트를 작성할 때
- 샷리스트의 각 샷을 구체 프롬프트로 변환할 때
- 사용자가 "이 장면을 이미지로", "이 컷의 프롬프트" 같은 요청을 할 때

이 스킬은 **단일 컷**을 깊이 있게 다룹니다. 다중 컷 시퀀스는 호출자(shot-designer 등)가 컷마다 이 스킬을
반복 호출하세요.

## 5 Layer Framework

순서대로 결정. 앞 단계가 정해지지 않으면 뒤 단계는 의미 없음.

### Layer 1: 샷 사이즈 (Shot Size)
| 약어 | 풀네임 | 효과 | 적합한 순간 |
|------|--------|------|-------------|
| EWS | Extreme Wide Shot | 풍경 안 작은 인물, 고독·스케일 | 오프닝, 환경 묘사 |
| WS | Wide Shot | 인물 전신 + 환경 | 인물-공간 관계 |
| FS | Full Shot | 인물 전신 꽉 차게 | 동작 강조 |
| MS | Medium Shot | 허리 위 | 대화 기본 |
| MCU | Medium Close-Up | 가슴 위 | 인터뷰, 감정 진입 |
| CU | Close-Up | 얼굴 | 감정 |
| ECU | Extreme Close-Up | 눈·입·손 디테일 | 강렬한 순간 |

### Layer 2: 앵글 (Angle)
- **Eye Level**: 중립, 동등한 시선
- **High Angle**: 위에서 → 인물이 작아 보임, 취약함
- **Low Angle**: 아래에서 → 인물이 커 보임, 권위·위협
- **Dutch / Canted**: 기울임 → 불안정, 긴장
- **Bird's Eye / Top Down**: 완전 위 → 추상화, 패턴
- **Worm's Eye**: 완전 아래 → 압도감
- **OTS (Over the Shoulder)**: 어깨너머 → 대화, 관찰자 시점
- **POV**: 인물 시점 → 몰입

### Layer 3: 렌즈 (Lens)
| 초점거리 | 효과 | 적합한 샷 |
|----------|------|-----------|
| 14~24mm | 광각, 왜곡, 공간 확장 | 풍경, 액션, 폐쇄공간 강조 |
| 35mm | 자연스러운 광각 | 다큐, 핸드헬드 |
| 50mm | 사람 눈에 가장 가까움 | 표준, 대화 |
| 85mm | 인물 포트레이트 | 클로즈업, 인터뷰 |
| 100mm+ | 망원, 압축 | 도시 압축감, 관찰자 시점 |

**조리개**:
- f/1.2~f/2.8 — 얕은 심도, 인물 분리, 보케
- f/4~f/5.6 — 중간, 자연스러움
- f/8~f/16 — 깊은 심도, 풍경, 전부 선명

### Layer 4: 조명 (Lighting)
- **방향**: front / side / back / top / bottom / 3-point
- **성격**: hard (직사) vs soft (디퓨즈) / high contrast vs low contrast
- **광원 색**: warm (3200K) / neutral (5600K) / cool (7000K) / mixed
- **광원 종류**:
  - Natural: north window / golden hour / overcast / moonlit
  - Practical: lamps in frame / neon / candle / TV glow
  - Cinematic: hard rim / soft fill / hair light / kicker

### Layer 5: 룩 (Look / Grade)
- **필름 스톡**: Kodak Portra 160/400/800 / Fujifilm Pro 400H / Cinestill 800T / Kodak Vision3
- **그레이드 성격**:
  - Lifted shadows + low contrast → 영화적
  - Crushed blacks + high contrast → 누아르
  - Teal & orange → 헐리우드 표준
  - Warm amber + cyan → 야경
  - Desaturated → 다큐, 회상
- **재질감**: grain / clean digital / halation / soft glow / sharp clinical

## Prompt Templates

### 기본 템플릿
```
[Shot Size] of [Subject + Action], [Angle], [Lens + Aperture],
[Lighting], [Color + Grade], [Aspect Ratio]
```

### 예시: 단편영화 클로즈업
```
Close-up of woman looking out window, eye level, 85mm f/1.4,
soft north-facing window light from left, low contrast warm midtones
cool highlights, Kodak Portra 400 grain --ar 16:9
```

### 예시: 뮤비 와이드
```
Extreme wide shot of single figure in foggy field, low angle,
24mm f/4, single cyan beam from sky, dense fog, minimalist
high contrast, Cinestill 800T halation --ar 16:9
```

### 예시: 광고 제품 컷
```
Extreme close-up of perfume bottle on marble, slight high angle,
100mm macro f/2.8, side rim light + soft fill, neutral grade
high clarity, clean digital --ar 1:1
```

## Output Format

이 스킬이 호출되면 다음 형식으로 반환:

```json
{
  "shot_id": "shot_001",
  "intent": "이 샷이 전달해야 할 한 줄 의미",
  "layers": {
    "size": "Close-up",
    "angle": "Eye level",
    "lens": "85mm f/1.4",
    "lighting": "soft north-facing window from left, warm fill",
    "look": "Kodak Portra 400, low contrast, lifted shadows"
  },
  "prompt": "최종 프롬프트 문자열",
  "negative_prompt": "blurry, distorted, multiple faces, ...",
  "aspect_ratio": "16:9",
  "platform_notes": "9:16 변형 시 인물을 프레임 1/3 위치로"
}
```

## 휴리스틱

- **감정 가까이** → CU/ECU + 85mm + 얕은 심도
- **공간 보여주기** → WS/EWS + 24~35mm + 깊은 심도
- **불안·긴장** → Dutch angle + hard lighting + high contrast
- **고요·관조** → Eye level + soft light + low contrast
- **세련·럭셔리** → 50mm or 100mm + side rim light + clean digital
- **빈티지·향수** → film stock 명시 (Portra, Cinestill) + grain
- **누아르** → low key + hard side light + crushed blacks

## 플랫폼별 조정

| 플랫폼 | 비율 | 조정 사항 |
|--------|------|-----------|
| YouTube | 16:9 | 표준 |
| Shorts/Reels/TikTok | 9:16 | 인물 프레이밍 타이트하게, 상단 1/3에 |
| 인스타 피드 | 4:5 또는 1:1 | 중앙 정렬, 헤드룸 줄임 |
| 영화제 | 2.39:1 시네스코프 | 좌우 확장, 위아래 좁음 |
| 웹 히어로 | 16:9 + 9:16 두 벌 | 같은 프롬프트의 비율만 변경, 인물 위치 재계산 |

## 의존 스킬과 다음 단계

- 얼굴 표정이 결과물의 핵심이면 → `facs-expression`도 같이 호출
- 비디오 생성으로 갈 거면 → 결과를 `seedance-prompt`로 넘김
- 뮤비 컨텍스트면 → `mv-builder`의 샷 슬롯에 들어감

## 오픈크랩 컨텍스트

이 스킬의 근거 자료:
- `시네마틱 이미지 생성 가이드` (4a5975a9 팩) — 핵심 어휘와 예시
- 필요 시 `opencrab_get_node_context` 로 특정 샷 사이즈/렌즈 노드 호출
