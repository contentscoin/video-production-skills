---
name: series-variation
description: Manage variation matrix for video series. Tracks LOCKED assets (brand, color, look, narrative) vs VARIABLE dimensions (persona, location, protagonist, motif). Use for multi-episode campaigns.
---

# Series Variation

시리즈 캠페인에서 편마다의 **차이를 의도적으로 설계**하는 스킬.
LOCKED(공통 자산)과 VARIABLE(편별 변주) 차원을 분리해서, 시리즈의 일관성을 깨지 않으면서
각 편이 서로 다른 메시지·정서·시각 어휘를 갖도록 합니다.

## When to use

- 시리즈 캠페인 2편 이상 기획
- 이미 1편이 만들어졌고 후속 편을 만들 때
- 시리즈의 톤·결이 흐트러지거나 편들이 너무 비슷해서 차별이 안 될 때
- 시즌 캠페인, 멀티 페르소나 타깃 광고, 다회차 콘텐츠

## 핵심 개념: LOCKED vs VARIABLE

### LOCKED (시리즈 자산 — 모든 편 공통)

이 항목들이 흔들리면 시리즈가 아니라 별개의 광고들이 됨.

```yaml
locked:
  brand_assets:
    logo: "..."
    wordmark: "..."
    cta_text: "..."

  format:
    duration: "15s"
    aspect: "9:16"
    end_card_duration: "2s"

  look_spec:
    color_palette: [...]
    lens_kit: [...]
    grade: "..."
    movement_rules: "..."

  narrative_arc:
    structure: ["Hook", "Context", "Core", "Promise", "CTA"]
    timing: [2, 4, 4, 3, 2]  # 초 단위

  guardrails:
    forbidden_phrases: [...]
    tone_floor: "..."  # 최저 톤 (이보다 가벼우면 안 됨)
    tone_ceiling: "..."  # 최고 톤 (이보다 무거우면 안 됨)
```

### VARIABLE (편별 변주 — 7개 차원)

```yaml
variable_dimensions:
  1_target_persona:    # 누구에게 말하는가
  2_location:          # 어디서 일어나는가
  3_protagonist:       # 누가 주인공인가 (pool에서)
  4_central_motif:     # 핵심 시각 모티프
  5_emotional_tone:    # 핵심 정서
  6_information_density: # 추상적 ↔ 구체적
  7_narrative_perspective: # 관찰자/1인칭/3인칭
```

## 7가지 변주 차원 상세

### 1. Target Persona (타깃 페르소나)
같은 브랜드라도 편마다 다른 사람에게 말함.
- 의사결정자 vs 실무자
- 신규 잠재고객 vs 기존 고객
- B2B vs B2C
- 연령대·역할·관여도

### 2. Location (로케이션)
시각적 다양성의 1차 원천.
- 실내 ↔ 실외
- 일상 공간 ↔ 비일상 공간
- 한정된 공간 ↔ 풍경
- 시간대 (새벽·낮·골든아워·밤)

### 3. Protagonist (주인공)
character_pool에서 누구를 메인으로 세울지.
- 단독 ↔ 2인 ↔ 그룹
- 정의된 캐릭터 ↔ 익명 (손·실루엣)
- 등장 없음 (오브제 중심)

### 4. Central Motif (핵심 모티프)
편을 기억하게 만드는 시각 어휘 1~2개.
- 도구 (펜·노트·브로셔·태블릿)
- 행위 (악수·스윙·잔 부딪힘·포장 풀기)
- 풍경 (페어웨이·클럽하우스·연습장·오피스)
- 신체 디테일 (손·실루엣·옆모습)

### 5. Emotional Tone (핵심 정서)
LOCKED의 tone_floor와 tone_ceiling 사이에서 편별 위치.
- 신중함 / 정성 / 편의 / 품격 / 합리성 / 신뢰
- 정서의 강도(어느 정도 짙게)와 색(어떤 방향)

### 6. Information Density (정보 밀도)
편마다 시청자에게 전달되는 정보의 추상도가 다름.
- **추상 (1)**: 오브제·풍경만, 정보 없음, 분위기로 전달 (예: V4)
- **준추상 (2)**: 행위 보여줌, 자막은 시적 (예: V1)
- **중간 (3)**: 시나리오 명확, 자막이 메시지 (예: V2)
- **구체 (4)**: 데이터·기능·프로세스 시각화 (예: V5)
- **직설 (5)**: 가격·혜택 명시 (대부분의 시리즈에서 회피)

시리즈는 보통 **1~4 사이에서 분포**. 5는 캠페인 후반·전환 광고용.

### 7. Narrative Perspective (서술 관점)
- **관찰자**: 카메라가 인물을 외부에서 본다 (V1, V2)
- **OTS·시점**: 인물의 어깨너머·시점 (V1-S3)
- **1인칭 손**: 시청자의 손인 듯 (V4)
- **상징**: 인물 없음, 오브제·풍경이 화자 (V4, V6 부분)

## Variation Matrix

시리즈 전체를 한 표로 관리:

```
┌─────┬──────────┬──────────┬──────────┬──────────┬─────────┬───────┬─────────┐
│  편 │ Target   │ Location │ Protag   │ Motif    │ Tone    │ Info  │ Persp   │
├─────┼──────────┼──────────┼──────────┼──────────┼─────────┼───────┼─────────┤
│ V1  │ 검토자   │ 클럽인테리│ CHAR_A   │ 펜·노트  │ 신중    │ 2     │ 관찰자  │
│ V2  │ 접대담당 │ 다이닝   │ CHAR_C+D │ 식기·악수│ 정성    │ 3     │ 관찰자  │
│ V3  │ 복지임원 │ 연습장   │ CHAR_E~G │ 레슨·스윙│ 편의    │ 3     │ 관찰자  │
│ V4  │ 기프팅   │ 책상     │ 익명손   │ 박스·골프공│ 품격   │ 1     │ 1인칭손 │
│ V5  │ 도입실무 │ 오피스   │ CHAR_I   │ 그래프   │ 합리성  │ 4     │ 관찰자  │
│ V6  │ 통합     │ 압축     │ 다수     │ 시리즈종합│ 신뢰    │ 2     │ 관찰자  │
└─────┴──────────┴──────────┴──────────┴──────────┴─────────┴───────┴─────────┘
```

## Variation Health Check

매트릭스가 완성되면 다음 체크:

### 다양성 (Variety)
- 각 차원에서 **최소 2개 이상의 값**이 등장하는가?
- 한 차원이 6편 내내 같으면 시리즈가 단조로움 (단, LOCKED 항목 제외)

### 차별성 (Distinctiveness)
- 어떤 두 편이 6개 이상 차원에서 동일하면 사실상 같은 광고
- 인접 편(V1과 V2 등)이 너무 비슷하면 운영 순서 재고

### 균형 (Balance)
- Information Density 분포: 1과 4가 동시에 있어야 시리즈 폭이 넓음
- Protagonist 분포: 익명/등장의 비율이 한쪽으로 쏠리지 않게
- Location 분포: 실내·실외 비율 균형

### 누락 점검
- 빠진 페르소나·로케이션·모티프 후보를 자동 제안 (예: "야간 컷이 없음", "여성 주인공이 부족")

## Operations

### 1. 시리즈 초기화
```
input: 캠페인 정보 + 편수
output: 빈 LOCKED 템플릿 + 빈 VARIABLE 매트릭스
```

### 2. LOCKED 정의
```
input: 1편 작업 결과
process: LOCKED 항목 자동 추출 (look_spec, format, narrative_arc, guardrails)
output: locked.yaml
```

### 3. 변주 제안
```
input: 새 편의 타깃 페르소나
process: 매트릭스 분석 → 비어있는 변주 차원 식별 → 후보 제안
output: 7개 차원의 값 후보들
```

### 4. 변주 등록
```
input: 새 편의 7개 차원 값
process: Health Check 자동 실행 → 경고 또는 OK
output: 매트릭스 업데이트
```

### 5. 매트릭스 감사
```
output: 다양성·차별성·균형 리포트 + 누락 후보 제안
```

## 변주 제안 휴리스틱

### "이전 편들과 가장 다른 편 만들기"
이전 편들의 차원별 평균에서 가장 먼 값을 선택. 예:
- V1~V3이 모두 "관찰자" 관점이면 V4는 "1인칭 손" 또는 "상징"
- V1~V3이 모두 Info Density 2~3이면 V4는 1 또는 4

### "쌍으로 다양성 만들기"
한 차원에 두 개의 대조 값을 고의로 배치:
- 추상(V4) ↔ 구체(V5) 인접 배치 → 시청자가 시리즈 폭을 빨리 인지
- 인물 등장(V1~V3) ↔ 익명(V4) ↔ 인물 등장(V5~V6)

### "타깃에 맞는 차원 자동 매핑"
- 데이터 기반 의사결정자 → Info Density 4 추천
- 정서 구매자 → Info Density 1~2 추천
- B2B 임원 → Protagonist는 단독 또는 2인, OTS 관점 추천

## Output Format

```json
{
  "campaign_id": "FMGmember_2026Q3",
  "operation": "register_variation",
  "episode_id": "V3",
  "locked_check": "passed",
  "variation": {
    "target_persona": "복지 담당 임원",
    "location": "도심 골프 연습장",
    "protagonist": ["FMG_CHAR_E", "FMG_CHAR_F", "FMG_CHAR_G"],
    "central_motif": "코칭 동작 + 스윙",
    "emotional_tone": "편의·접근성",
    "information_density": 3,
    "narrative_perspective": "관찰자"
  },
  "health_check": {
    "variety_score": "8/10",
    "distinctiveness_warnings": [],
    "balance_warnings": ["전체 시리즈에 야간 컷 부재"],
    "suggested_for_next_episodes": ["야간 로케이션", "여성 단독 주인공"]
  }
}
```

## 휴리스틱

- **첫 편은 시리즈의 정중앙**: Info Density 2~3, 관찰자, 메인 페르소나로 시작. 양극단은 2~3편 이후.
- **6편 이상이면 페르소나 매트릭스 권장**: 타깃 × 정보밀도 표로 시각화
- **편 간 거리 = (다른 차원의 수)**: 인접 편은 거리 3 이상 권장
- **상징·추상 편은 시리즈에서 최대 1~2편**: 너무 많으면 메시지가 흐려짐

## 시스템 호출

- `intake-router`가 시리즈 작업 감지하면 → 이 스킬 호출해서 매트릭스 먼저 구축
- `script-writer`가 새 편 시작 시 → 매트릭스의 해당 행 참조해서 콘티 작성
- `narrative-weaver` (kkirikkiri)가 정서 곡선 만들 때 → emotional_tone 차원 참조
- `intake-router`가 마지막 편 통합 작업 결정 시 → 매트릭스로 시리즈 종합 확인

## 오픈크랩 컨텍스트

시리즈 캠페인이 완료되면 매트릭스 자체를 오픈크랩 팩으로 ingest해서 다음 캠페인의 기준 자료로 사용.
