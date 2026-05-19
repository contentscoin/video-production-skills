---
name: series-closer
description: Design final episode of video series via 3 closure types: Reprise Montage (5+ eps), Synthesis Landscape (3-4 eps), Compressed Narrative (8+ or standalone). Hybrids possible. Use for finale.
---

# Series Closer

시리즈 캠페인의 **마지막 편**(또는 종합 편)을 만드는 전용 스킬.
이전 편들의 자산을 어떻게 압축·재구성·합성할지에 대한 명시적 패턴입니다.

## When to use

- 시리즈 캠페인의 마지막 편 (V6, 시즌 피날레 등)
- 리타겟팅용 종합 광고 (이전 편을 본 사용자에게 압축 노출)
- 시즌 마무리 / 시리즈 회고
- 신규 진입자도 보고 한 번에 이해할 수 있는 "캠페인 요약 편"

**v0.2에서 발견된 갭**: V6 리프라이즈 컷이 즉흥적이었던 문제를 패턴으로 잠금.

## 청사진 근거

청사진은 시리즈 클로저 패턴을 명시적으로 다루지 않음. 하지만:
- `claim_music_video_structure` (구조 일관성)
- `claim_evidence_traceability` (이전 편 추적)
- `series-variation` 스킬과의 호환성

을 종합해서 도출한 우리 시스템 고유의 패턴.

## 클로저 편의 3가지 유형

### 🅰️ Type A: 리프라이즈 몽타주 (Reprise Montage)

이전 편들의 **상징 컷을 짧게 압축**해서 재등장시키는 방식.

**구조**:
```
0-1s   : 후킹 (시리즈에서 가장 강렬한 컷 1개)
1-N×K  : 각 이전 편에서 1컷씩 (N편 × K초 = 보통 0.5~1초)
N×K-13 : 새 컷 (시리즈의 정서적 종합 풍경)
13-15s : 로고 + CTA
```

**적합한 경우**:
- 시리즈가 5편 이상
- 각 편마다 명확히 식별되는 상징 컷이 있음
- 시청자가 이전 편을 봤다고 가정 (리타겟팅)

**FMGmember V6에 사용된 패턴**.

**리프라이즈 컷 선정 규칙**:
- 각 편의 **가장 상징적인 단일 컷** (각 편의 motif_library 첫 번째 항목)
- 인물 식별 가능하면 안 됨 (편마다 다른 인물이 일관성 깨뜨림)
- 클로즈업·디테일 위주가 안전 (와이드는 다음 컷과 충돌)

### 🅱️ Type B: 종합 풍경 (Synthesis Landscape)

이전 편의 **모티프를 합성한 새 풍경**을 만드는 방식.

**구조**:
```
0-2s   : 후킹 (새로 만든 인상적인 풍경 또는 풀샷)
2-13s  : 같은 풍경 안에서 카메라가 천천히 움직이며
         이전 편의 오브제·인물 디테일이 차례로 발견됨
13-15s : 로고 + CTA
```

**적합한 경우**:
- 시리즈의 모티프가 한 공간에 모일 수 있음 (모든 편이 같은 골프장이라면)
- 정적인 미적 인상이 메시지의 핵심
- 시리즈가 3~4편 정도

**예시 구조**:
```
풍경: 클럽하우스 라운지 + 페어웨이 + 19홀 라운지가 동시에 보이는 와이드
카메라 슬로우 트래킹:
  → 노트가 펼쳐진 테이블 (V1 모티프)
  → 두 잔이 놓인 옆 테이블 (V2 모티프)
  → 창밖으로 보이는 연습장 (V3 모티프)
  → 선물 박스 (V4 모티프)
  → 노트북 위 그래프 (V5 모티프)
```

### 🅾️ Type C: 압축 내러티브 (Compressed Narrative)

이전 편들의 **공통 정서 곡선을 한 편에 압축**해서 새로 풀어내는 방식.

**구조**:
```
0-2s   : 후킹 (시리즈의 일반화된 페르소나)
2-5s   : 시리즈 전체의 Context 압축 (3편 분량을 5초에)
5-10s  : 시리즈 전체의 Core Value 압축 (3편 분량을 5초에)
10-13s : 시리즈 전체의 Promise 압축
13-15s : 로고 + CTA
```

**적합한 경우**:
- 시리즈가 너무 많아서 (8편 이상) 리프라이즈 어려움
- 클로저가 단독 노출용으로도 작동해야 함 (이전 편 안 본 사람도 이해)
- 광고 외 콘텐츠 (브랜드 다큐, 회사 소개 등)

## 선택 매트릭스

| 조건 | 추천 Type |
|------|-----------|
| 시리즈 5편 이상 + 리타겟팅 위주 | A (리프라이즈) |
| 시리즈 모티프가 한 공간에 모일 수 있음 | B (종합 풍경) |
| 신규 노출도 고려해야 함 | C (압축 내러티브) |
| 모티프가 다양하고 강렬함 | A |
| 정적 미적 인상 우선 | B |
| 시리즈가 너무 많음 (8편+) | C |

## 작업 절차

### Step 1: 시리즈 매트릭스 회고

`series-variation` 스킬의 매트릭스를 호출해서:
- 각 편의 central_motif 확인
- 각 편의 emotional_tone 확인
- 다양성·차별성 health check 재실행

### Step 2: 클로저 Type 결정

위 매트릭스로 자동 추천, 사용자 확인.

### Step 3: 자산 선정

**Type A (리프라이즈)** 인 경우:
- 각 편의 1순위 상징 컷 자동 선정 (motif_library에서)
- 각 컷의 길이 계산 (총 길이 - 후킹 - 마무리 = 리프라이즈 풀)
- 컷 순서: 시리즈 전개 순서 또는 정서 곡선 순서

**Type B (종합 풍경)** 인 경우:
- 통합 풍경 정의 (새 컨셉 작업 필요)
- 각 편의 오브제·디테일을 풍경 안에 배치
- 카메라 무빙 경로 설계

**Type C (압축 내러티브)** 인 경우:
- 시리즈의 공통 Hook-Context-Core-Promise-CTA 추출
- 일반화된 페르소나 정의
- 5비트 내러티브 작성

### Step 4: 일반 V1~V5와 동일한 파이프라인

이후는 `intake-router` → kkirikkiri → pumasi 표준 흐름.
단, **모든 산출물은 series-variation 매트릭스의 LOCKED 자산을 100% 준수**.

### Step 5: QA 가중 항목

`qa-review` 호출 시 다음 항목을 가중치 ↑:
- **리프라이즈 컷이 원본과 동일하게 보이는가** (Type A)
- **이전 편을 안 본 사람도 메시지가 통하는가** (Type C)
- **시리즈 정체성과 어긋나지 않는가** (모든 Type)

## Type별 산출물 차이

### Type A의 추가 산출물
```json
{
  "reprise_map": [
    {"source_episode": "V1", "source_shot": "V1-S1", "closer_position": "00:00:00:00", "duration_s": 1.0},
    {"source_episode": "V2", "source_shot": "V2-S4", "closer_position": "00:00:01:00", "duration_s": 1.0}
  ],
  "new_shots_only": ["V6-S6"]
}
```

### Type B의 추가 산출물
```json
{
  "synthesis_landscape": {
    "location_definition": "...",
    "objects_embedded": [
      {"object": "노트", "source_episode": "V1", "position_in_frame": "left third"},
      {"object": "두 잔", "source_episode": "V2", "position_in_frame": "center"}
    ],
    "camera_path": "left to right slow tracking"
  }
}
```

### Type C의 추가 산출물
```json
{
  "compression_map": {
    "hook_summary": "여러 페르소나의 공통 진입점",
    "core_value_compressed": "3편의 핵심을 5초에",
    "generalized_persona": "..."
  }
}
```

## 휴리스틱

- **클로저는 시리즈 전체의 50% 자원**을 따로 빼둘 가치가 있음 — 가장 많이 노출됨
- **Type A가 가장 안전**, Type C는 가장 어렵지만 가장 확장성 높음
- **리프라이즈 컷은 원본보다 살짝 짧게** (원본이 4초였으면 클로저에선 0.5~1초)
- **클로저의 BGM은 시리즈 BGM과 같은 곡** (마지막 절 또는 코다 부분)
- **리프라이즈 컷 사이의 트랜지션은 컷이나 빠른 디졸브** — 길게 디졸브하면 산만

## 운영 시 노출 순서

```
주차 1-2: V1~V5 동시 운영 (페르소나 타깃별)
주차 3+:  V6 (클로저) 추가 노출
  - V1~V5 본 시청자에게 리타겟팅
  - 신규에게도 노출 (Type C인 경우 효과적)
주차 4+:  V6만 단독 운영 + 캠페인 마무리
```

## 시스템 호출

- `series-variation`의 매트릭스 → Type 추천 결정
- `character-pool` lock 상태에서 호출 (캐릭터 변경 불가)
- `visual-bible` v1.0 잠금 후에만 호출 (룩 변경 불가)
- 결과 → `production-brief`의 마지막 에피소드로 자동 등록

## 오픈크랩 컨텍스트

- 시리즈 종료 후 클로저 패턴 자체를 ingest → 차기 시리즈의 참고
- Type별 성과 데이터를 누적하면 추천 정확도 향상
