---
name: facs-expression
description: Specify facial expressions using FACS Action Units AU1-AU45 with intensity A-E (ads use A-C), M Code, Gross Behavior. Use when faces need precise expression spec for AI video generation.
---

# FACS Expression

AI 캐릭터에게 정밀한 얼굴 연기를 지시하는 스킬. **FACS(Facial Action Coding System)** 의
AU(Action Unit)·AD(Action Descriptor)·Intensity 체계로 표정을 좌표화합니다.

## When to use

- 캐릭터의 표정이 결과물의 핵심일 때 (드라마, 광고 클로즈업, 캐릭터 중심 콘텐츠)
- "슬픈 표정"처럼 추상적 지시 대신 **재현 가능한** 표정 명세가 필요할 때
- 같은 캐릭터의 표정 일관성을 여러 컷에서 유지해야 할 때
- 미묘한 정서(고통을 숨김, 거짓 미소, 의심) 표현이 필요할 때

**FACS는 정답표가 아니라 좌표계**입니다. 슬픔=AU1+AU4 가 절대값이 아니라, 슬픔을 표현할 때
**관찰 가능한 움직임의 좌표**입니다. 실감나는 표정 연기를 위한 보조 수단으로 사용하세요.

## 핵심 개념

### AU (Action Unit)
얼굴 근육(또는 근육군)의 관찰 가능한 움직임 단위. 코드 번호로 표기.

### AD (Action Descriptor)
근육 기반으로 명확히 특정되지 않는 행동 기술 코드.

### M Code
특정 AU와 동반되는 머리·눈 움직임 코드. **비디오 생성에만 적용 가능** (정지 이미지엔 의미 없음).

### Intensity (강도)
AU 뒤에 A~E로 강도 표시.
| 표기 | 의미 | 설명 |
|------|------|------|
| A | Trace | 미세한 흔적 |
| B | Slight | 약한 움직임 |
| C | Marked / Pronounced | 뚜렷한 움직임 |
| D | Severe / Extreme | 강한 움직임 |
| E | Maximum | 최대 강도에 가까움 |

표기 예: `AU4C` = AU4의 뚜렷한 강도

### Gross Behavior Code
말하기, 삼키기, 고개 끄덕임처럼 큰 행동. **비디오에만 적용 가능**.

## 자주 쓰이는 AU 빠른 참조

상반부 (눈썹·이마):
- **AU1**: 내측 눈썹 올림 (Inner Brow Raiser) — 슬픔, 걱정
- **AU2**: 외측 눈썹 올림 (Outer Brow Raiser) — 놀람
- **AU4**: 눈썹 내림·모음 (Brow Lowerer) — 분노, 집중, 의심
- **AU5**: 윗눈꺼풀 들어올림 (Upper Lid Raiser) — 놀람, 공포
- **AU6**: 볼 올림 (Cheek Raiser) — 진짜 미소 (뒤셴 미소)
- **AU7**: 아랫눈꺼풀 조임 (Lid Tightener) — 의심, 집중

하반부 (입·턱):
- **AU9**: 코주름 (Nose Wrinkler) — 혐오
- **AU10**: 윗입술 들어올림 (Upper Lip Raiser) — 경멸, 혐오
- **AU12**: 입꼬리 올림 (Lip Corner Puller) — 미소 (가짜 미소는 AU6 없이 AU12만)
- **AU14**: 보조개 만듦 (Dimpler) — 경멸, 비웃음
- **AU15**: 입꼬리 내림 (Lip Corner Depressor) — 슬픔
- **AU17**: 턱 올림 (Chin Raiser) — 분노, 결의
- **AU20**: 입술 늘림 (Lip Stretcher) — 공포
- **AU23**: 입술 조임 (Lip Tightener) — 분노 억제
- **AU24**: 입술 누름 (Lip Pressor) — 결의, 인내
- **AU25**: 입 벌어짐 (Lips Part)
- **AU26**: 턱 떨어짐 (Jaw Drop) — 놀람

## 자주 쓰이는 감정 매핑 (참고용, 절대값 아님)

| 감정 | 핵심 AU 조합 |
|------|--------------|
| 진짜 기쁨 (뒤셴 미소) | AU6C + AU12C |
| 가짜 미소 (사회적) | AU12C (AU6 없음) |
| 슬픔 | AU1C + AU4B + AU15C |
| 놀람 | AU1C + AU2C + AU5C + AU26C |
| 공포 | AU1C + AU2B + AU4C + AU5D + AU20C + AU26B |
| 분노 | AU4D + AU5C + AU7C + AU23C |
| 혐오 | AU9C + AU10C + AU17B |
| 경멸 | AU12C (한쪽만) + AU14C |
| 고통 숨김 | AU24C + AU17B + (눈가 미세 긴장) |
| 거짓 미소 | AU12C + AU6 없음 + (AU14 미세) |

## 비디오 전용 동작 (이미지 생성엔 무의미)

- **M51**: 머리 한쪽으로 기울임
- **M55**: 머리 오른쪽으로 돌림
- **M57**: 고개 끄덕임
- **M59**: 고개 흔듦
- **M61**: 눈 좌측 이동
- **M63**: 눈 우측 이동
- **AU45**: 깜빡임 (Blink)
- **AU46**: 윙크

Gross Behavior:
- 말하기 / 삼키기 / 한숨 / 입술 핥기

## Prompt Templates

### 이미지 생성용 (정적 표정)
```
[기본 캐릭터 묘사], facial expression: AU1C + AU4B + AU15C
(inner brow raised, brows slightly drawn together, lip corners depressed)
```

영문 풀이를 괄호로 같이 넣어주는 게 모델이 더 잘 따라옵니다.

### 비디오 생성용 (표정 변화)
```
Start: neutral face, AU12A (faint smile)
Transition: AU4C develops over 1s (brows draw together)
End: AU4C + AU17B + AU24C held (suppressed concern)
```

### 정밀 지시 예시
```
[캐릭터: 30대 한국 여성, 짧은 단발, 흰 셔츠]
표정 명세: AU1C + AU4B + AU15C + AU17A
(내측 눈썹 뚜렷이 올림, 눈썹 살짝 모음, 입꼬리 뚜렷이 내림, 턱 미세하게 올림)
정서: 슬픔을 참고 있는 상태, 시선은 약간 아래
강도: 전체적으로 절제됨, 눈물은 없음
```

## Output Format

```json
{
  "character_ref": "캐릭터 묘사 또는 ID",
  "emotion_intent": "한 줄로 표현하려는 정서",
  "au_codes": ["AU1C", "AU4B", "AU15C"],
  "english_gloss": "inner brow raised, brows slightly drawn together, lip corners depressed",
  "korean_gloss": "내측 눈썹 올림, 눈썹 살짝 모음, 입꼬리 뚜렷이 내림",
  "for_video": {
    "head_motion": "M51 (slight tilt left)",
    "eye_motion": "M61 (eyes slightly left)",
    "gross_behavior": null,
    "duration": "2s hold"
  },
  "final_prompt": "최종 프롬프트 문자열"
}
```

## 휴리스틱

- **진짜 vs 가짜 감정 구분**: 진짜는 AU6 동반, 가짜는 AU12만
- **억제된 감정**: AU24 (입술 누름) + AU17 (턱 올림) + 핵심 AU의 강도 한 단계 낮춤
- **이중 감정 (예: 슬픈데 웃음)**: 두 감정의 AU를 섞되 시간차로 (비디오) 또는 비대칭으로 (이미지)
- **미묘함이 핵심**: B~C 강도가 보통 가장 자연스러움. E는 만화적
- **눈물 같은 부수 요소**는 AU 외에 별도로 명시 필요

## 모델별 적용 가능성

- **Nano Banana 2/Pro, GPT-Image-2**: AU 코드 직접 인식은 제한적이지만 영문 풀이를 같이 주면 잘 반영
- **Kling 3.0, Seedance 2.0**: 비디오 전용 동작(M코드, Gross Behavior)이 의미를 가짐
- **Midjourney**: AU 코드보다는 자연어 풀이 위주 권장

## 의존 스킬과 다음 단계

- 보통 `cinematic-shot` 작업의 마지막에 표정 레이어를 추가하는 형태
- 비디오 생성 시 `seedance-prompt`와 결합 (Seedance는 비디오 참조로 표정 입력 가능)
- 캐릭터 일관성이 중요한 시리즈 작업이면 캐릭터 시트와 함께 관리

## 오픈크랩 컨텍스트

근거 자료:
- `AI 캐릭터에게 표정연기 지시하기 - FACS를 기반으로` (80423f00 팩)
- AU 전체 리스트가 필요하면 `opencrab_get_node_context` 로 해당 노드 조회
