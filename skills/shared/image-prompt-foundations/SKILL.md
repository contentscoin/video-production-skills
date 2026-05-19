---
name: image-prompt-foundations
description: Foundational image prompting: removes 3 ambiguity types (abstract emotion, subjective qualifiers, broad subjects), requires shadow spec, uses 5-layer structure. Use as Step 1 of prompt pipeline.
---

# Image Prompt Foundations

이미지 프롬프트의 **모델 독립적 일반 원칙**을 다루는 스킬.
모호함을 죽이고, 추상 어휘를 시각 속성으로 변환하고, "다른 사람이 같은 이미지를 떠올릴 수 있도록" 쓰는 방법.

## When to use

- 이미지 프롬프트를 처음 작성하기 전 (모델 선택 전)
- 생성 결과가 의도와 어긋날 때 (프롬프트 점검)
- 사용자가 추상 어휘("슬픈 분위기")로 요청할 때
- 시리즈 작업에서 프롬프트의 일관성 점검

**cinematic-shot**이 시네마틱 컷 전용 5레이어라면, **image-prompt-foundations**는 모든 이미지 프롬프트의 토대.
**model-adapter**가 모델별 최적화라면, 이 스킬은 그 이전에 와야 함.

## 청사진 근거

movie_seedance_pack의 `notion_image_prompt_guide.md`에 명시된 원칙 기반.

> "내 프롬프트를 읽은 다른 사람이, 나와 같은 이미지를 머릿속에 떠올릴 수 있는가?"
> 이 질문에 "아니오"라면, 프롬프트가 모호한 것입니다.

## 핵심 원칙: 모호함의 3가지 유형

### 유형 1: 추상적 감정 서술

**문제**:
```
❌ a sad and lonely atmosphere
❌ a dramatic moment
❌ a peaceful scene
```

**원인**: LLM은 감정 단어를 시각 속성으로 직접 변환하지 못합니다. "슬픔"이 무엇인지 AI는 모릅니다.

**해결**: 감정을 **유발하는 구체 장면**으로 변환.

| 추상 어휘 | 구체 변환 예시 |
|----------|--------------|
| "슬픈 분위기" | "비에 젖은 벤치, 텅 빈 복도, 창문에 맺힌 빗방울" |
| "외로움" | "혼자 앉은 카페 창가, 식어가는 커피 한 잔, 흐린 창밖" |
| "고요한 아침" | "황금빛 햇살이 얇은 커튼 사이로 스며들고, 김이 모락모락 나는 컵, 새소리만 들림" |
| "긴장감" | "어두운 복도, 깜빡이는 형광등, 멀리서 들리는 발자국, 손이 문 손잡이 위에 머뭄" |
| "따뜻함" | "벽난로 옆 양털 담요, 흔들리는 그림자, 따스한 황금빛 조명, 양손에 감싼 머그컵" |

### 유형 2: 주관적 품질 수식어

**문제**:
```
❌ very beautiful
❌ extremely detailed
❌ super realistic
❌ amazing quality
```

**원인**: "매우 아름다운"의 기준은 사람마다 다릅니다. LLM에게 이런 수식어는 약간의 품질 가중치만 더할 뿐, **장면을 구성하지 않습니다**.

**해결**: 구체 묘사로 대체.

| 주관적 수식어 | 구체 대체 |
|--------------|-----------|
| "아주 아름다운 일출" | "황금빛 노을이 잔잔한 바다 위로 비추고, 흩어진 권운(cirrus)이 보인다" |
| "매우 디테일한 얼굴" | "주름의 음영이 보이고, 속눈썹 한 가닥마다 그림자가 있다" |
| "초현실적 광경" | "달이 두 개 떠있는 사막, 보라색 모래, 유리 같은 표면에 비친 반사" |
| "환상적 분위기" | "안개 속에서 부유하는 발광 입자, 보랏빛 어둠, 식물이 빛을 내고 있음" |

### 유형 3: 범위가 너무 넓은 주제

**문제**:
```
❌ a cool sci-fi scene
❌ a fantasy landscape
❌ a noir city
```

**원인**: "sci-fi"는 스타워즈일 수도, 블레이드 러너일 수도, 인터스텔라일 수도 있습니다. AI는 거대한 풀에서 무작위로 하나를 건져올립니다.

**해결**: 구체 레퍼런스·시대·미장센으로 범위 좁히기.

| 넓은 주제 | 좁힌 묘사 |
|----------|-----------|
| "sci-fi 장면" | "1980년대 블레이드 러너 스타일, 네온 사이버펑크, 비 내리는 도쿄 거리, 홀로그램 광고 간판" |
| "판타지 풍경" | "스튜디오 지브리 풍의 자연주의 판타지, 푸른 언덕과 흰 양들, 거대한 떡갈나무 한 그루" |
| "느와르 도시" | "1940년대 LA, 흑백, 비에 젖은 골목, 베니션 블라인드 그림자, 페도라 쓴 인물의 실루엣" |

## 모호함 제거 체크리스트

프롬프트 작성 후 다음 체크:

- [ ] 감정·기분 단어가 있나? → **구체 장면 묘사**로 변환했나
- [ ] 주관적 품질 수식어("아름다운", "매우", "엄청난")가 있나? → **구체 묘사**로 대체했나
- [ ] 장르·시대·스타일이 너무 넓은가? → **시대·레퍼런스·미장센**으로 좁혔나
- [ ] 다른 사람이 이 프롬프트를 읽고 같은 이미지를 떠올릴 수 있는가?

## 그림자 원칙

청사진의 시네마틱 가이드에서 명시된 핵심 보강 원칙:

> 조명에서 가장 중요하지만 자주 빠뜨리는 것이 "그림자"입니다.
> 프롬프트에 밝은 빛만 묘사하고 그림자를 언급하지 않으면, AI는 그림자가 거의 없는 평면적인 이미지를 생성합니다.

**그림자 명시 어휘 라이브러리**:
- `deep shadows` — 짙은 그림자
- `shadow falling across the face` — 얼굴을 가로지르는 그림자
- `silhouette against the light` — 빛 앞의 실루엣
- `dappled shadow through leaves` — 잎새 사이로 들어오는 얼룩 그림자
- `split lighting, half face in shadow` — 분할 조명
- `long cast shadow on the floor` — 바닥으로 길게 늘어지는 그림자

**룰**: 모든 조명 묘사에 **그림자 묘사를 1개 이상 포함**.

## 구조화된 프롬프트 템플릿

모호함을 죽이는 5층 구조 (cinematic-shot의 5레이어와 호환):

```
[Subject & Action]
누가/무엇이, 무엇을 하고 있는가 — 가장 구체적으로

[Setting & Time]
어디서, 언제 (시대·계절·시각·날씨)

[Camera & Lens]
샷 사이즈, 앵글, 렌즈 (cinematic-shot 참고)

[Light & Shadow]
광원 종류·방향·색온도 + 그림자 묘사 필수

[Mood & Style]
스타일 레퍼런스 (영화 제목·필름 스톡·아트워크 시대)
— 단 추상 어휘 금지, 구체 명시
```

## 한국어 vs 영문

이미지 생성 모델 대다수는 영문 학습 데이터가 압도적. 따라서:
- **최종 프롬프트는 영문 권장**
- 한국어로 먼저 쓴 뒤 영문 변환은 가능
- 단, 한국적 디테일(한복 종류, 특정 음식, 지명)은 한국어로 그대로 두기보다 **구체 영문 묘사**로 풀어쓰기

## 예시 비교

**Before (모호)**:
```
A beautiful sad woman in a sad atmosphere, cinematic, dramatic, high quality
```

**After (구체)**:
```
A woman in her 30s sitting by a rain-streaked window in a dim cafe at dusk, 
holding a cooling cup of tea with both hands, her eyes lowered and unfocused, 
soft window light from her left casting a long shadow across the table, 
warm tungsten lamp from upper right creating practical fill, 
Kodak Portra 400 film stock, low contrast, lifted shadows, 35mm grain, 
medium close-up, 85mm f/1.8 lens.
```

## Output Format

```json
{
  "original_prompt": "사용자 입력 (있다면)",
  "ambiguity_check": {
    "type_1_emotion": ["sad", "lonely"],
    "type_2_subjective": ["beautiful", "very"],
    "type_3_broad": ["sci-fi scene"]
  },
  "concrete_rewrites": {
    "sad atmosphere": "rain-streaked window, dim cafe, cooling tea cup"
  },
  "shadow_check": "passed (1 shadow descriptor present)",
  "final_prompt": "...",
  "structure_layers": {
    "subject_action": "...",
    "setting_time": "...",
    "camera_lens": "...",
    "light_shadow": "...",
    "mood_style": "..."
  }
}
```

## 휴리스틱

- **첫 시도엔 한국어로 자유 작성 → 모호함 체크 → 구체 변환 → 영문 변환** 순서
- **5층 모두 작성하지 말 것** — 강조하고 싶은 2~3개 층에 집중. 나머지는 짧게.
- **"무엇이 보이지 않는가"도 명시**: "no people in frame", "empty street"
- **부정 프롬프트는 별도**: negative prompt에 "blurry, deformed, text, watermark" 등

## 시스템 호출

- `cinematic-shot` 이전 단계로 호출 권장 — 추상 입력을 구체화한 뒤 5레이어 적용
- `prompt-engineer` (pumasi)의 모든 프롬프트 작성 진입점
- `visual-bible`의 룰 검증을 통과한 후 최종 프롬프트로 진행
- `model-adapter`의 입력 (이 스킬의 출력 = 모델 독립 프롬프트 → 모델별 미세 조정)

## 오픈크랩 컨텍스트

근거 자료:
- `notion_image_prompt_guide.md` (movie_seedance_pack)
- `notion_cinematic_image_guide.md` (조명·그림자 원칙)
- 구체 변환 예시는 evidence chunk로 추가 검색 가능
