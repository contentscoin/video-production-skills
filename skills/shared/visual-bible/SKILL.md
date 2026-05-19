---
name: visual-bible
description: Master visual bible for video series. 7 sections: brand, color, typography, look_spec, characters, motifs, taboos. Init/lock/validate/export ops. Use to lock V1 for V2-Vn consistency.
---

# Visual Bible

캠페인·시리즈·작품의 **시각적 결정 사항 전체를 한 문서로 잠그는** 스킬.
캐릭터·룩·팔레트·타이포·로고·금지 사항이 한 곳에 정리되어, 어느 에이전트가 호출하든 동일한 시각 기준을 사용합니다.

## When to use

- 시리즈 캠페인 시작 시 (1편 작업 후 잠금)
- 한 작품 안에서 여러 사람이 협업할 때
- AI 생성의 일관성이 흐트러지고 있을 때 (재정렬용)
- 외주·후속 작업자에게 인계할 때

**character-pool**이 인물 시트라면, **visual-bible**은 시각 결정 전체의 마스터 문서. character-pool도 그 안에 포함됩니다.

## 청사진 근거

이 스킬은 외부 OpenCrab MCP의 `movie_seedance_pack` 청사진에 명시된
**"visual bible"** 산출물에 대응합니다. 청사진의 워크플로우 단계 5("이미지 생성: GPT Image 2로 캐릭터시트, 스타일 바이블, 키프레임, 스토리보드를 만든다")의 핵심 산출물입니다.

청사진 원문은 저장소에 번들하지 않습니다. 근거 확인이 필요하면 OpenCrab MCP에서 `movie_seedance_pack`의 visual bible 또는 seedance video director 청사진 노드를 조회합니다.

## 비주얼 바이블의 7개 섹션

```yaml
visual_bible:
  meta:
    campaign_id: "..."
    version: "1.0"
    locked_at: "..."
    locked_by: "..."

  1_brand_identity:
    logo:
      primary: "asset path"
      variants: ["badge", "wordmark", "monogram"]
      clear_space: "로고 높이의 1배"
      min_size: "..."
      forbidden: ["회전", "기울임", "그라데이션", "그림자"]

    wordmark:
      font: "..."
      tracking: "..."
      cases: ["uppercase", "title case"]

    color_logo: { primary: "#...", reversed: "#FFF on dark" }

  2_color_palette:
    primary: { hex: "#0B1A14", role: "메인·그림자", usage_pct: 40 }
    accent: { hex: "#C9A961", role: "강조·메탈", usage_pct: 10 }
    secondary: { hex: "#E8E3D7", role: "여백·텍스트 배경", usage_pct: 35 }
    midtone: { hex: "#3A4A3F", role: "중간톤·자연", usage_pct: 12 }
    black: { hex: "#1A1A1A", role: "텍스트·로고", usage_pct: 3 }
    forbidden_colors: ["#FF0000 채도 90% 이상의 원색"]

  3_typography:
    primary_hangul: { family: "Pretendard", weights: ["SemiBold", "Bold"], usage: "headlines" }
    primary_latin: { family: "Inter", weights: ["Medium", "Semibold"], usage: "captions" }
    forbidden_fonts: ["나눔고딕", "스크립트체 일반"]
    pairing_rule: "헤드라인 ≤ 2 weights, 캡션 1 weight"

  4_look_spec:
    grade:
      reference: "Kodak Vision3 250D"
      shadow_lift: "+15 IRE"
      midtone_warm: "+8"
      highlight_cool: "-5"
      contrast: 0.85
      saturation: 0.9
      grain: "35mm 250D simulation 30%"

    lens_kit:
      primary: "85mm f/1.8"
      secondary: "35mm f/2.8"
      macro: "100mm macro f/2.8"
      forbidden: ["fisheye", "wide distortion under 24mm"]

    lighting_rules:
      day_exterior: "golden hour backlight + grass bounce"
      day_interior: "soft north-facing window + practical warm lamps"
      signature_moment: "misty dawn diffusion"
      forbidden: ["하드 형광등 직사", "단일 강한 키 라이트"]

    movement_rules: "static or slow / no handheld / no whip pan"

  5_character_pool_ref:
    # character-pool 스킬의 결과물 ID 리스트
    - "FMG_CHAR_A_REVIEWER"
    - "FMG_CHAR_B_PARTNER"
    # ... (자세한 시트는 character-pool에서 관리)

  6_motif_library:
    visual_motifs:
      - id: "M1"
        name: "혼자 있는 인물의 뒷모습"
        meaning: "회원권의 사적 가치"
        used_in: ["V1-S4"]
      - id: "M2"
        name: "두 사람의 비공식적 대화"
        meaning: "비즈니스 라운딩의 친밀함"
        used_in: ["V2-S2", "V2-S4"]
      # ...

    object_library:
      - "골프공 (Lucky Ball, 화이트 또는 다크 그린)"
      - "골프 티 (브라스)"
      - "노트 (다크 브라운 가죽)"
      - "만년필 (메탈)"
      - "포장 박스 (다크 그린 + 골든 리본)"

  7_taboos:
    visual:
      - "AI 원본에 텍스트·로고 합성 금지"
      - "실존 인물 닮은 얼굴 절대 금지"
      - "특정 골프장 식별 가능한 시그너처 홀 노출 금지"
      - "경쟁사 로고 노출"
    copy:
      - "최저가 보장 / 예약 확정 / 수익 보장 / 무조건 VIP"
    composition:
      - "정면 풀 클로즈업 (얼굴 식별)"
      - "수평선 기울어진 컷"
```

## Operations

### 1. 비주얼 바이블 초기화
```
input: campaign_id, 1편 작업 결과물 (look_spec, character_pool 등)
process: 모든 시각 자산 자동 추출 → 7개 섹션에 배치
output: visual_bible_v1.yaml + 잠금 후보 표시
```

### 2. 섹션 잠금 (lock_section)
```
input: section_id (예: "color_palette")
process: 해당 섹션의 모든 값이 후속 작업에서 변경 불가하게 잠금
output: locked_sections 리스트에 추가
```

### 3. 검증 (validate)
```
input: 새로 생성된 산출물 (이미지 프롬프트, 샷리스트 등)
process: 바이블의 각 항목과 대조
output: 위반 항목 + 자동 수정 제안
```

### 4. 변경 요청 (request_change)
```
input: 변경하려는 섹션 + 사유
process: 잠금 상태 확인 → 사용자 확인 요청 → 버전 업데이트
output: visual_bible_v1.1.yaml + 변경 이력
```

### 5. 외부 인계 (export)
```
output: 인계용 PDF + JSON + 후속 작업자가 즉시 이해할 수 있는 요약 1쪽
```

## 검증 자동화 예시

새 이미지 프롬프트가 생성될 때 비주얼 바이블이 자동 체크하는 항목:

| 체크 | 룰 출처 |
|------|---------|
| 컬러 헥스 값이 팔레트 내에 있는가? | section 2 |
| 렌즈 명시가 lens_kit 안에 있는가? | section 4 |
| 캐릭터 ID가 character_pool에 있는가? | section 5 |
| 금지 표현이 들어있지 않은가? | section 7 |
| 그레이드 키워드가 룩 명세와 일치하는가? | section 4 |

위반 시 → 경고 + 수정 제안 + 사용자 확인.

## 휴리스틱

- **1편 작업 후 즉시 작성**. 1편의 결정이 시리즈의 기준이 됨.
- **잠금은 신중하게**. 잠긴 항목은 시리즈 끝까지 못 바꾸므로 핵심만 잠금.
- **alt 버전은 별도 섹션** — 시즌 변형, 명절 한정판 등은 alt로 관리.
- **외부 작업자 인계 시 PDF 한 부 + JSON 한 부** — PDF는 빠른 이해용, JSON은 자동 검증용.

## 시스템 호출

- `intake-router`가 시리즈 작업이면 → visual-bible 초기화 권장
- `kkirikkiri.aesthetic-director`의 최종 산출물 → 바이블의 look_spec에 자동 등록
- `character-pool`의 결과 → 바이블의 character_pool_ref에 ID 리스트로 연결
- `pumasi.prompt-engineer`가 프롬프트 생성 시 → 바이블 검증 자동 호출
- `qa-review`의 첫 체크 항목 → 바이블 준수 여부

## 청사진 매핑

| 청사진 항목 | 바이블 섹션 |
|------------|------------|
| character sheet | 5_character_pool_ref |
| visual identity | 1_brand_identity |
| costume palette | 5에 포함 |
| reference image | 6_motif_library |
| color | 2_color_palette |
| lighting | 4_look_spec.lighting_rules |
| production design | 4_look_spec + 6_motif_library |
| likeness risk | 7_taboos.visual |

## 오픈크랩 컨텍스트

- 완성된 바이블은 오픈크랩 팩으로 ingest → 후속 캠페인의 레퍼런스
- 시리즈별 바이블 비교로 브랜드 룩 진화 추적 가능
