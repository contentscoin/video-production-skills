---
name: music-rights-check
description: Check music rights across 5 categories: Self-Composed, Royalty-Free, Sync, AI Generated (SUNO), Voice Cloning (SAG-AFTRA). Auto-called after editor. Use to verify license before delivery.
---

# Music Rights Check

영상의 **BGM·SFX·VO** 등 모든 음향 자산의 권리 이슈를 전문적으로 점검하는 스킬.
guardrail-check Part 2의 한 줄로 다뤄졌던 음악 권리를 별도 스킬로 분리.

## When to use

- audio_tracks가 정의된 직후
- BGM·SFX 추가·교체 시
- 외주 음원 계약 검수
- 송출 직전 라이선스 증빙 정리
- SUNO·Suno 등 AI 음원 생성 결과물 검토

## 청사진 근거

- 청사진의 `claim_policy_gate` 중 "source licenses, voice replicas" 부분
- Vimeo AUP: "third-party works (like background music or stock footage) must have the right to include those works"
- U.S. Copyright Office AI 보고서: AI 생성 음원의 저작권 보호 범위
- SAG-AFTRA AI: 음성 클로닝 동의

원문 근거는 저장소에 번들하지 않습니다. 근거 확인이 필요하면 외부 OpenCrab MCP에서 `movie_seedance_pack` 및 관련 외부 권위 자료 노드를 조회합니다.

## 음향 자산의 5가지 권리 카테고리

### 🅰️ Category A: 자체 작곡·녹음 (Self-Composed)

가장 안전한 카테고리.

```yaml
status: self_composed
license_required: false
proof_needed: "작곡가·연주자 명시 + 양도/이용 계약서"
risk_level: low

verification:
  - "작곡가가 본인 또는 직접 의뢰한 작곡가"
  - "연주자가 본인 또는 계약된 세션"
  - "녹음 스튜디오·엔지니어 정보 명시"
```

**주의**: 의뢰 작곡이라도 **이용 범위 명시** 필요:
- 광고 송출 기간 (1년, 2년 등)
- 매체 (디지털 / TV / 영화관)
- 지역 (국내 / 글로벌)
- 수정·편집 권리

### 🅱️ Category B: 로열티 프리·구독형 라이선스

Epidemic Sound, Artlist, AudioJungle, MusicBed 등.

```yaml
status: royalty_free OR subscription_licensed
license_required: true
proof_needed:
  - "라이선스 ID 또는 사용자 계정"
  - "라이선스 약관 (사용 범위·기간)"
  - "구독 활성 상태 증빙"

verification:
  - "라이선스가 광고 사용 허용하는가"
  - "기간 만료 전인가"
  - "라이선스가 영구 vs 구독 종료 시 만료인지"

high_risk_cases:
  - "구독 종료 후에도 송출 지속 — 일부 서비스는 구독 만료 시 라이선스 만료"
  - "광고 vs 개인 사용 구분 — 광고에 못 쓰는 라이선스 다수"
  - "Sync license 별도 필요 여부 — 일부 트랙은 별도 sync 비용"
```

### 🅾️ Category C: 일반 라이선스 (Sync License)

상업용 음악을 광고에 쓰는 경우.

```yaml
status: sync_licensed
license_required: true
proof_needed:
  - "Sync license 계약서"
  - "저작권자 + 마스터 권리자 양쪽 클리어"
  - "이용 범위 명시 (매체·지역·기간·수정 권리)"

verification:
  - "두 권리 다 클리어됐는가 (대부분 분리됨)"
  - "공동 작곡인 경우 모든 작곡가 동의"
  - "샘플 사용한 곡인 경우 원곡 클리어도 확인"

cost_range: "수백만원 ~ 수억원 (곡 인지도·이용 범위에 따라)"
processing_time: "2~8주 표준"
```

**중요**: 같은 곡이라도 **저작권(작곡·작사)** 과 **저작인접권(마스터·녹음)** 이 별개. 둘 다 클리어 필요.

### 🆎 Category D: AI 음원 생성 (SUNO 등)

```yaml
status: ai_generated
license_required: 사용 서비스의 약관에 따라
proof_needed:
  - "AI 서비스 계정·생성 ID"
  - "해당 서비스의 라이선스 약관"
  - "상업 사용 가능 플랜인지 확인"

verification:
  - "SUNO 등 서비스의 약관: 무료 플랜은 보통 상업 사용 제한"
  - "유료 플랜이라도 라이선스 범위 확인 (저작권 양도 vs 사용권만)"
  - "AI 학습 데이터 권리 이슈 (U.S. Copyright Office 보고서 참조)"

us_copyright_office_position: |
  "AI가 생성한 결과물은 사람의 창작적 기여가 있어야 저작권 보호.
   순수 AI 생성은 저작권 보호 안 됨. 광고에 사용은 가능하지만
   다른 사람이 같은 결과물 생성·사용해도 막을 권리 없음."

high_risk_cases:
  - "프롬프트에 '[유명 곡] 스타일'이라고 명시 → 우연 닮음 위험"
  - "학습 데이터의 저작권 이슈가 미래에 소급될 가능성"
  - "AI 음원의 매체 사용에 대한 플랫폼 정책 (YouTube Content ID 등)"
```

### 🆔 Category E: 음성 클로닝 (Voice Cloning)

```yaml
status: voice_cloned
license_required: true (SAG-AFTRA 룰)
proof_needed:
  - "음성 원 소유자의 명시적 서면 동의"
  - "사용 범위·기간 합의"
  - "재현 거부권 명시 (당사자가 언제든 철회 가능)"

verification:
  - "동의자의 음성이 맞는가 (제3자 음성 클로닝 절대 금지)"
  - "AI 생성임을 청자에게 표시"
  - "정치적·기만적 맥락 사용 금지"

absolute_forbidden:
  - "유명 성우·배우의 음색 모방 (동의 없이)"
  - "이미 사망한 인물의 음성 부활 (유족 동의 없이)"
  - "허위 정보·사칭 의도의 음성 클로닝"
```

## SFX는 별도 룰

SFX(효과음)는 BGM보다 권리 이슈 작지만:
- **자연음·일반 효과음**: 대체로 안전 (저작권 보호 약함)
- **시그너처 사운드**: 주의 (THX, MGM Lion 등 트레이드마크)
- **유명 영화·게임 효과음**: 저작권 보호 (피하기)

## SUNO 라이선스 상세 (자주 쓰는 케이스)

```yaml
suno_license_summary:
  free_plan:
    commercial_use: false  # 무료 플랜은 비상업
    notes: "광고에 절대 사용 금지"
    
  pro_plan_2026:
    commercial_use: true
    ownership: "사용자에게 양도 (단 SUNO도 학습 데이터로 사용 권리 보유)"
    redistribution: true
    restrictions:
      - "SUNO 브랜드명 명시 의무는 없음 (이전 버전과 다름)"
      - "타인의 저작물을 입력으로 사용한 결과물은 권리 불명확"

  premier_plan:
    commercial_use: true
    extra_rights: "사용자에게 모든 권리 양도, SUNO도 학습 미사용 옵션"

verification_step:
  - "SUNO 계정 플랜 스크린샷 보관"
  - "각 트랙의 생성 ID + 프롬프트 보관"
  - "SUNO 약관 버전 명시 (분기마다 변경)"
```

⚠️ **이 정보는 분기마다 변경됨**. 송출 직전 SUNO 약관 페이지 직접 확인 필수.

## Output Format

```json
{
  "campaign_id": "FMGmember_2026Q3",
  "episode_id": "V1",
  "audio_audit_date": "2026-05-18",
  
  "tracks": [
    {
      "track_id": "bgm_01",
      "type": "BGM",
      "description": "80 BPM 솔로 피아노 + 첼로",
      "category": "self_composed",
      "creator": "(작곡가 이름)",
      "proof": "작곡가 양도 계약서 #2026-XYZ",
      "usage_scope": "디지털 광고, 무제한 기간, 글로벌",
      "license_status": "PASS",
      "verification_complete": true
    },
    {
      "track_id": "sfx_pen",
      "type": "SFX",
      "description": "fountain pen friction",
      "category": "royalty_free",
      "source": "Epidemic Sound",
      "license_id": "ES-12345",
      "subscription_status": "active until 2026-12-31",
      "license_status": "PASS",
      "verification_complete": true
    },
    {
      "track_id": "vo_01",
      "type": "VO",
      "description": "narrator voice",
      "category": "self_recorded",
      "performer": "(성우 이름)",
      "performer_consent": "녹음 계약서 #2026-ABC",
      "voice_cloning_used": false,
      "license_status": "PASS",
      "verification_complete": true
    }
  ],
  
  "audit_summary": {
    "total_tracks": 3,
    "pass": 3,
    "warning": 0,
    "block": 0,
    "manual_check_needed": 0
  },
  
  "platform_compliance": {
    "youtube_content_id": "no claims expected (self_composed)",
    "instagram_music_library": "N/A (custom audio)",
    "vimeo_third_party_works": "all licensed and proven"
  },
  
  "ai_music_specific_check": {
    "any_ai_generated": false,
    "us_copyright_office_compliance": "N/A",
    "notes": "이번 V1은 자체 작곡, AI 음원 미사용"
  }
}
```

## 작업 절차

1. post-production-spec의 audio_tracks 추출
2. 각 트랙에 category 자동 분류
3. category별 verification 룰 적용
4. proof 누락 검출 → 사용자에게 증빙 요청
5. high_risk_cases 자동 매칭
6. 플랫폼 호환성 점검 (YouTube Content ID, Vimeo AUP 등)
7. 종합 리포트 생성

## 휴리스틱

- **AI 음원은 분기마다 약관 재확인** — SUNO 등 정책 변경 잦음
- **광고는 무조건 상업 라이선스 확인** — 개인용 라이선스 다수
- **저작권 + 저작인접권 둘 다** — 마스터 트랙 있는 곡은 양쪽 클리어
- **무료 음원이라도 출처·약관 보관** — 추후 분쟁 시 증빙
- **VO는 SAG-AFTRA 룰** — 음성 클로닝은 동의 필수
- **불확실하면 BLOCK** — "아마 괜찮을 거야"는 분쟁 시 무력

## 협업 인터페이스

### post-production-spec과 협업
- audio_tracks 정의 직후 자동 호출
- 각 트랙에 license_status 채움

### editor와 협업
- editor가 audio_tracks 추가 시 실시간 점검
- BLOCK 발생 시 대체 음원 권고

### guardrail-check Part 2와 협업
- music_imitation 룰 보강 (이 스킬이 깊게 다룸)
- AI 음원의 라이선스 → guardrail audit_summary에 통합

### production-brief에 통합
- audio_audit 결과 → production_brief.md의 Risk Register
- 라이선스 증빙 → 인계 패키지의 별도 폴더

## 시스템 호출

- **상위**: editor의 post_production_spec 작성 후
- **하위**: production-brief에 audit 결과 통합
- **연관**: guardrail-check Part 2 (music_imitation), post-production-spec

## 청사진 매핑

청사진의 `policy_gate` responsibility 중 음악 관련 영역 전담.
`claim_policy_gate`의 "source licenses" 부분 직접 책임.

## 오픈크랩 컨텍스트

외부 OpenCrab 의존성:
- 이 저장소는 정책 원문 스냅샷을 번들하지 않습니다.
- 근거 확인이 필요하면 OpenCrab MCP에서 `movie_seedance_pack` 및 외부 권위 자료 노드를 조회합니다.
- 우선 조회할 근거: Vimeo AUP third-party works 룰, U.S. Copyright Office AI 보고서, SAG-AFTRA AI/voice cloning guidance.
- SUNO 등 AI 음원 서비스 약관은 서비스별 최신 약관을 분기마다 재확인합니다.

## ⚠️ 면책 사항

이 스킬은 1차 필터. 최종 법무 검토 대체하지 않음.
고가 광고·해외 송출은 음악 전문 법무사 검토 권장.
