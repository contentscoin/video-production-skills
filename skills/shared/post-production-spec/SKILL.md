---
name: post-production-spec
description: Standard JSON spec for video post-production: transitions, text overlays, audio tracks, color grade, edit_decision_list, export variants. Use as deliverable format from editor agent.
---

# Post-Production Spec

AI 생성 영상의 **편집·후처리 단계**에 필요한 명세를 표준 포맷으로 작성하는 스킬.
편집자(또는 자기 자신)가 합성할 자막·로고·사운드·그레이딩 정보를 일관된 포맷으로 인계합니다.

## When to use

- AI 생성 영상에 텍스트·로고를 후처리로 삽입할 때
- 자막·BGM·SFX 동기화가 필요한 모든 광고·콘텐츠
- 여러 편을 편집팀이나 외주에 넘겨야 할 때
- 캠페인 운영 중 일관된 후처리 톤을 유지하고 싶을 때

AI 생성만으로 완결되는 작업(소셜 짤, 컨셉 비주얼 등)이면 이 스킬은 과잉.

## 핵심 원칙

### 1. AI 원본에는 텍스트·로고 미삽입
AI 생성 모델은 정확한 한글·정확한 로고를 못 그림. 후처리에서 깔끔히 합성.
→ 프롬프트 단계에서 "no text, no logo, no signage" 명시.

### 2. 후처리 영역을 미리 확보
AI 영상의 어느 위치에 자막·로고가 들어갈지 **프롬프트 단계에서 예약**. 사후에 위치 못 잡으면 재생성.

### 3. 모든 합성 요소에 시간 마커
"2-5초", "끝에서 1초" 같은 모호한 표현 금지. **타임코드 절대값**으로 명시.

## Spec Schema

### 풀 명세서 (한 편당 1개)

```json
{
  "episode_id": "V1",
  "duration_s": 15.0,
  "aspect": "9:16",
  "resolution": "1080x1920",
  "fps": 24,
  "master_format": "ProRes 422 HQ",
  "delivery_formats": ["MP4 H.264 high quality", "MOV ProRes"],

  "text_overlays": [
    {
      "id": "text_01",
      "content_ko": "감으로 고르지 마세요",
      "content_en_alt": "Don't choose by intuition",
      "in_tc": "00:00:06:00",
      "out_tc": "00:00:09:12",
      "position": "lower_third",
      "alignment": "center",
      "font": "Pretendard SemiBold",
      "font_size_pt": 56,
      "color": "#FFFFFF",
      "stroke": "none",
      "shadow": "soft drop shadow, opacity 35%, blur 8px, y+4",
      "animation_in": "fade 12 frames",
      "animation_out": "fade 12 frames",
      "background_safety": "S4의 하단 1/3에 어두운 영역 확보됨 (잔디·실루엣)"
    }
  ],

  "logo_overlays": [
    {
      "id": "logo_01",
      "asset_ref": "FMG_FIND_ME_A_GOLF_SPONSOR_LOGO",
      "in_tc": "00:00:13:00",
      "out_tc": "00:00:15:00",
      "position": "center",
      "size_pct_of_height": 18,
      "animation_in": "fade 16 frames",
      "animation_out": "hold to end",
      "padding_from_edges_pct": 8
    },
    {
      "id": "logo_02",
      "asset_ref": "FMG_LUCKY_BALL_BADGE",
      "in_tc": "00:00:13:12",
      "out_tc": "00:00:15:00",
      "position": "bottom_right",
      "size_pct_of_height": 8,
      "animation_in": "fade 12 frames"
    }
  ],

  "audio_tracks": [
    {
      "track_id": "bgm_01",
      "type": "BGM",
      "source": "to_compose 또는 license_track_id",
      "description": "80 BPM 솔로 피아노 + 첼로 sustained",
      "in_tc": "00:00:03:00",
      "out_tc": "00:00:15:00",
      "fade_in_frames": 24,
      "fade_out_frames": 36,
      "peak_volume_db": -12,
      "duck_for_vo": false
    },
    {
      "track_id": "sfx_01",
      "type": "SFX",
      "description": "펜이 종이에 마찰하는 소리",
      "in_tc": "00:00:00:12",
      "out_tc": "00:00:02:00",
      "peak_volume_db": -18
    },
    {
      "track_id": "sfx_02",
      "type": "SFX",
      "description": "발자국 (잔디), 1초 간격 4회",
      "in_tc": "00:00:06:00",
      "out_tc": "00:00:10:00",
      "peak_volume_db": -20
    }
  ],

  "vo_track": null,

  "color_grade_master": {
    "shadow_lift": "+15 IRE",
    "midtone_shift": "warm +8 toward orange",
    "highlight_shift": "cool -5 toward cyan",
    "contrast": 0.85,
    "saturation": 0.9,
    "grain": "35mm 250D simulation, intensity 30%"
  },

  "transitions": [
    {"from_tc": "00:00:02:00", "type": "match_cut", "to": "next_shot"},
    {"from_tc": "00:00:06:00", "type": "dissolve", "duration_frames": 4},
    {"from_tc": "00:00:13:00", "type": "fade_to_black", "duration_frames": 24}
  ],

  "safe_areas": {
    "title_safe_pct": 90,
    "action_safe_pct": 95,
    "platform_specific": {
      "instagram_reels": "bottom 220px reserved for caption/UI",
      "tiktok": "right 180px reserved for action bar"
    }
  },

  "platform_variants": [
    {
      "variant_id": "ig_reels",
      "based_on": "master",
      "modifications": []
    },
    {
      "variant_id": "ig_feed_4x5",
      "based_on": "master",
      "modifications": ["reframe to 1080x1350", "logo size +20%"]
    }
  ]
}
```

## Position 표준값

```
정의된 위치 키워드:
- top_left, top_center, top_right
- center_left, center, center_right
- bottom_left, bottom_center, bottom_right
- upper_third (Y=25%)
- lower_third (Y=75%)
- title_safe_top, title_safe_bottom
```

## 폰트 표준

한글 광고 표준 권장 폰트:
- **Pretendard** (현대적 산세리프, 가장 안전)
- **Noto Sans KR** (구글 폰트, 무료, 다국어 호환)
- **Apple SD Gothic Neo** (애플 시스템, 라이선스 주의)
- **본명조 / Noto Serif KR** (세리프, 시네마틱 느낌)

브랜드 폰트가 있으면 LOCKED 자산에 등록 후 우선 사용.

## 사운드 표준값

| 요소 | 권장 dB | 비고 |
|------|---------|------|
| BGM (VO 없을 때) | -12 dB | 마스터 |
| BGM (VO 있을 때) | -22 dB | 보이스 아래로 덕킹 |
| VO | -9 to -6 dB | 가장 두드러짐 |
| SFX (앰비언트) | -22 to -18 dB | 배경 |
| SFX (포커스 효과) | -15 to -12 dB | 동작 강조 |
| 마스터 피크 | -1 dB TP | 플랫폼 정규화 대비 |
| 라우드니스 | -14 LUFS | 인스타·유튜브 표준 |

## 플랫폼별 안전 영역

```yaml
instagram_reels_9x16:
  resolution: 1080x1920
  title_safe: 1080x1500  # 위아래 210px 안전 마진
  bottom_caption_zone: 1080x220 (Y=1700~1920)  # UI 가림
  action_buttons_right: 100x600 (X=980~1080, Y=900~1500)

youtube_shorts_9x16:
  resolution: 1080x1920
  title_safe: 동일
  bottom_zone: 1080x250  # 더 큼

tiktok_9x16:
  resolution: 1080x1920
  right_action_bar: 200x800 (X=880~1080)  # 가장 침범 큼
  bottom_caption_zone: 1080x300

instagram_feed_4x5:
  resolution: 1080x1350
  title_safe: 1080x1200

instagram_feed_1x1:
  resolution: 1080x1080
  title_safe: 920x920
```

자막·로고 위치 정할 때 이 영역 침범 여부 자동 체크.

## Operations

### 1. 명세서 초기화
```
input: episode_id, duration, aspect
output: 빈 spec 템플릿
```

### 2. 자막 추가
```
input: 자막 내용, 시간, 위치
process: 안전 영역 체크 + 가독성 체크 (배경 대비)
output: text_overlays 항목 추가
```

### 3. 로고 배치
```
input: 로고 자산 ID, 시간, 위치, 크기
process: 안전 영역 + 다른 요소와 겹침 체크
output: logo_overlays 항목 추가
```

### 4. 사운드 트랙 추가
```
input: BGM·SFX·VO 정보
process: 시간 충돌 체크 + 음량 균형 체크
output: audio_tracks 항목 추가
```

### 5. 플랫폼 변형 자동 제안
```
input: 마스터 spec
output: 각 플랫폼용 modifications 리스트
```

### 6. Spec 감사
```
output: 누락 항목 + 충돌 + 안전영역 침범 + 가독성 경고
```

## 가독성 자동 체크

자막을 위치에 배치할 때 그 영역의 배경 상태 체크:
- 배경 밝기 < 30% → 흰 텍스트 OK
- 배경 밝기 > 70% → 검은 텍스트 OK
- 배경 밝기 30~70% (중간) → 그림자·외곽선 필수
- 배경에 디테일 많음 → 반투명 박스 또는 그라데이션 권장

이 체크는 첫 프레임 이미지를 기준으로 수행. 비디오 전체가 변할 수 있으므로 자막 표시 시간 동안의 평균 밝기 권장.

## Output Format

위 풀 명세서 JSON 그대로. 추가로:

```json
{
  "audit_summary": {
    "text_overlays_count": 2,
    "logo_overlays_count": 2,
    "audio_tracks_count": 3,
    "safe_area_violations": [],
    "readability_warnings": [
      {
        "overlay_id": "text_01",
        "warning": "S4 (06:00~10:00) 배경에 밝은 하늘. 그림자 강도 35% → 50% 권장"
      }
    ],
    "platform_compatibility": {
      "instagram_reels": "OK",
      "tiktok": "WARNING: text_01 위치가 right action bar와 겹칠 수 있음"
    }
  }
}
```

## 시스템 호출

- `editor` (pumasi)가 편집 가이드 작성 마지막 단계에 호출
- `intake-router`가 플랫폼 명시되면 자동으로 플랫폼별 안전영역 체크
- `series-variation`의 LOCKED에 폰트·컬러·라우드니스 표준 등록

## 휴리스틱

- **자막은 한 화면에 한 줄, 최대 두 줄**. 모바일 가독성.
- **자막 표시 시간 = 한국어 글자수 × 0.25초 + 1.0초 여유** (예: 9글자 → 3.25초)
- **로고는 페이드 인 + 홀드**, 페이드 아웃은 끝까지 유지 권장
- **BGM이 VO보다 강하면 안 됨** — VO 들어오는 순간 BGM -10dB 덕킹
- **숏폼은 첫 1초에 자막 금지** — 알고리즘이 잘라먹어서 잘 안 보임. 1.5초~ 이후 등장.
- **CTA는 마지막 2초 모두 같은 위치**에 — 시청자가 액션 취할 시간 확보

## 오픈크랩 컨텍스트

- 브랜드별 표준 폰트·컬러·로고 위치 등을 별도 팩으로 관리 가능
- 캠페인 spec 전체를 ingest해서 후속 캠페인에서 재사용
