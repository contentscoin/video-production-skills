---
name: guardrail-check
description: 4-Part guardrail for AI video: Korean ad law, AI rights (OpenAI/SAG-AFTRA/MPA/Vimeo), visual (real-person/logos), AI checklist. Use before distribution. Auto-triggers on AI generation.
---

# Guardrail Check (v0.4 확장)

광고·콘텐츠의 카피·시각·시나리오에 대해 **금지 표현·법적 리스크·플랫폼 정책 위반·AI 권리 이슈**를
자동 점검하는 스킬.

## v0.4 확장 사항

기존 v0.2 가드레일(카테고리별 금지어 + 한국 광고법)에 다음 4개 권위 자료를 흡수.
이 권위 자료의 원문·스냅샷은 저장소에 번들하지 않고, 필요할 때 외부 OpenCrab MCP에서 조회:
- **OpenAI Usage Policies** (사용 정책)
- **Vimeo Acceptable Use Policy** (업로드 정책)
- **MPA(미국영화협회)** Seedance 2.0 침해 경고 (저작권)
- **SAG-AFTRA AI** 가이드라인 (배우 권리)

특히 **AI 시대의 권리 이슈**(저작권·초상권·디지털 레플리카)가 강화됐습니다.

## When to use

- 카피·자막·내레이션 작성 후 송출 전 점검
- 새 캠페인 시작 시 카테고리별 가드레일 로드
- 외주 카피·시안 검수
- 시리즈 전 편 통합 점검
- **AI 생성 콘텐츠 송출 전** (v0.4 특화)

법률 검토를 대체하지 않습니다. 자동 1차 필터.

---

## Part 1: 한국 광고 카테고리 (v0.2 유지)

### 골프 회원권·리조트

```yaml
forbidden_phrases:
  - "최저가 보장"
  - "예약 확정"
  - "수익 보장"
  - "100% 환불"
  - "무조건"
  - "절대"
  - "유일한"

caution_phrases:
  - "VIP" → "무조건 VIP" 금지, "VIP 의전" 등은 OK
  - "프리미엄" → 객관 근거 권장
  - "최고" → "업계 최고" 등 비교 표현 주의
  - "특별가" → 가격 표시법 준수

required_disclosures:
  - "회원권 가입 절차·조건"
  - "환불·해지 정책"
  - "광고임 표시"
```

### 식품·건강 / 금융·투자 / 부동산 / 일반 광고

(v0.2 내용 그대로 유지 — 본 문서 v0.2 버전 참조)

### 한국 광고 관련 법규

- 표시광고법 / 개인정보보호법 / 정보통신망법 / 소비자보호법

---

## Part 2: AI 생성 콘텐츠 권리 (v0.4 신규)

### 2.1 OpenAI Usage Policies

OpenAI의 모든 모델(GPT Image 2 포함) 사용 시 적용. **사용자 책임**이지만 정책 위반 시 결과물도 차단됨.

**절대 금지 (OpenAI 명시)**:
```yaml
absolute_forbidden:
  protect_people:
    - "위협·협박·괴롭힘·명예훼손"
    - "자살·자해·섭식장애 조장·촉진"
    - "성폭력 또는 비합의적 친밀 콘텐츠"
    - "테러·폭력 (혐오 기반 폭력 포함)"
    - "무기 개발·조달·사용 (재래식 + CBRNE)"
    - "불법 활동·재화·서비스"

  protect_minors:
    - "아동 성적 콘텐츠 (절대)"
    - "미성년자 대상 유해 콘텐츠"

  honest_engagement:
    - "허위 정보 유포 의도"
    - "선거·정치 조작"
    - "사칭 (impersonation)"
    - "사기·기만"

  intellectual_property:
    - "저작권 침해 콘텐츠 생성"
    - "타인 작품의 무단 모방"
```

### 2.2 SAG-AFTRA AI Guidelines (배우 권리)

**디지털 레플리카·AI 초상권** 관련. 광고·콘텐츠에 AI로 인물 생성 시 적용.

```yaml
person_likeness_rules:
  real_person:
    - "실존 인물의 얼굴 닮음 (식별 가능 수준) 금지"
    - "유명인(배우·정치인·운동선수) 명시 또는 닮음 절대 금지"
    - "이미 사망한 유명인의 디지털 부활 — 유족·재단 동의 없이 금지"

  voice_likeness:
    - "특정인의 음성 클로닝 금지 (동의 없이)"
    - "유명 성우의 음색 모방 금지"

  digital_replica_consent:
    - "AI 모델·데이터셋이 특정인을 학습한 결과로 생성된 콘텐츠는 동의 필요"
    - "광고 출연자의 AI 변형(나이대 변경, 의상 변경 등)도 별도 동의"

  general_principles:
    - "AI 생성 인물이라도 실존 인물과 우연히 닮으면 위험"
    - "특정 인종·국적·종교를 대표하는 식의 묘사 회피"
```

### 2.3 MPA 저작권 경고 (Seedance 2.0)

**Motion Picture Association(MPA)**이 ByteDance에 Seedance 2.0의 저작권 침해 중단을 요구한 사건. AI 영상 생성의 **학습 데이터·결과물 모두 저작권 리스크**를 환기.

```yaml
copyright_rules:
  training_data_risk:
    - "AI 모델이 특정 영화·드라마를 학습했을 가능성 → 결과물이 우연히 닮을 위험"
    - "Seedance·Kling 등 비디오 모델 사용 시 더 높음"
    - "프롬프트에 영화 제목·캐릭터 명시 금지"

  style_imitation:
    - "특정 감독의 영상 스타일을 'in the style of [감독명]'로 명시 — 위험"
    - "'블레이드 러너 스타일' 같은 표현 — 위험"
    - "대안: 시대·미장센·기술적 특성으로 묘사 ('1980s neon noir')"

  character_imitation:
    - "유명 캐릭터(디즈니·마블 등) 묘사 → 저작권 침해"
    - "코스튬·소품의 트레이드마크 디자인 (스파이더맨 슈트 등) — 위험"

  music_imitation:
    - "유명 곡의 멜로디·후크 모방 (SUNO 등 음악 생성 포함)"
    - "음원은 라이선스 트랙만 사용 또는 완전 새 창작"

  brand_imitation:
    - "코카콜라·나이키 등 브랜드 로고·디자인 — 광고에 무단 노출 금지"
    - "경쟁사 시각 어휘 모방 (브랜드 마크 없어도 식별 가능하면 위반)"
```

### 2.4 Vimeo Acceptable Use Policy

업로드·송출 시 적용. 다른 플랫폼도 유사.

```yaml
vimeo_rules:
  ownership_requirement:
    - "업로드자는 다음 중 하나여야 함:"
    - "  (a) 콘텐츠 소유"
    - "  (b) 적절한 라이선스 확보"
    - "  (c) 기타 명확한 법적 근거"
    - "AI 생성 콘텐츠도 동일 — 학습 데이터의 권리 이슈는 업로드자 책임"

  third_party_works:
    - "BGM·스톡 푸티지·폰트 등 제3자 저작물 포함 시 라이선스 명시 필요"

  community_safety:
    - "혐오·괴롭힘·폭력 조장 콘텐츠 금지"
    - "성적 콘텐츠 (별도 정책 카테고리)"
    - "허위정보·선거 조작"

  account_risk:
    - "침해 콘텐츠 업로드 시 계정 정지·법적 책임"
```

### 2.5 플랫폼별 정책 (v0.2 확장)

**Meta (Instagram·Facebook)**:
- 정치·종교 콘텐츠 광고 제한
- 의약품·건강기능식품 별도 인증
- 도박·주류 지역별 제한
- 비포·애프터 카테고리별 제한
- "당신은 ~" 개인 속성 추정 금지

**TikTok**:
- 미성년 타깃 별도 정책
- 음원 저작권 엄격 (라이선스 트랙만)
- 표시되지 않는 텍스트 제한

**YouTube**:
- YPP(광고 친화 카테고리) 별도
- YMYL(Your Money Your Life) 신뢰성 강조
- 클릭베이트 페널티

**Vimeo**:
- AUP 준수 (위 2.4)
- 라이선스 명시 권장
- 비즈니스 플랜은 다른 정책 적용

---

## Part 3: 시각 가드레일 (v0.2 확장)

### 인물

- 실존 인물 무단 사용 금지 (AI 닮음 포함)
- 미성년자 등장 시 카테고리 제한
- 특정 인종·국적의 클리셰적 묘사 회피
- 디지털 레플리카는 별도 동의 필수

### 비교·경쟁사

- 경쟁사 로고·제품 의도적 노출 = 비교광고 규정
- 명시적 비방 금지
- 비교 광고는 출처 명시

### 가격·혜택

- 할인율·가격 시각화 정확성
- 별표·작은 글씨도 모바일 가독 가능해야

### 저작물·트레이드마크 (v0.4 강조)

- 영화·드라마·만화 캐릭터 묘사 금지
- 음악 후크·멜로디 모방 금지
- 폰트·아이콘 라이선스 확인
- 브랜드 디자인 의도적 모방 금지

---

## Part 4: AI 생성 콘텐츠 체크리스트 (v0.4 신규)

AI로 생성한 모든 콘텐츠 송출 전:

```
[Pre-Production]
- [ ] 모델의 사용 정책 확인 (OpenAI / ByteDance / Google)
- [ ] 학습 데이터의 권리 이슈 인지
- [ ] 프롬프트에 실존 인물·캐릭터·작품명 미포함

[During Production]
- [ ] 생성된 인물이 실존 인물과 닮지 않는지 확인
- [ ] 음악·BGM은 라이선스 확보 또는 완전 창작
- [ ] 로고·브랜드 디자인 모방 없음

[Pre-Delivery]
- [ ] AI 생성 콘텐츠임을 표시 (플랫폼 정책에 따라)
- [ ] 송출 플랫폼의 AUP 통과
- [ ] 라이선스·저작권 문서 정리
- [ ] 디지털 레플리카 동의 (해당 시)
```

---

## Check Operations

### 1. 텍스트 체크
forbidden_phrases / caution_phrases / required_disclosures (v0.2 동일)
+ AI 시대 표현 검출 ("in the style of [감독]", "[캐릭터명]처럼" 등)

### 2. 시나리오 체크
인물 묘사 / 행위 / 시각 요소 (v0.2 동일)
+ 디지털 레플리카 위험 자동 검출

### 3. 시각 체크
**v0.4 확장**:
- 실존 인물 닮음 자동 점수 (얼굴 인식 모델 사용 시)
- 트레이드마크 디자인 검출 (로고 인식)
- 음악 워터마크 검출

### 4. 전체 패키지 체크 (시리즈)
편마다 + 시리즈 일관성 + AI 권리 이슈 통합

### 5. 플랫폼 정책 체크
**v0.4 확장**:
- Vimeo AUP 호환성
- 각 플랫폼의 AI 콘텐츠 표시 정책

## Output Format (v0.4 확장)

```json
{
  "check_target": "...",
  "category": ["골프 회원권", "일반 광고"],
  "platforms": ["instagram_reels", "youtube_shorts", "vimeo_business"],
  "ai_generated": true,

  "violations": [
    {
      "level": "BLOCK",
      "rule_source": "OpenAI Usage Policies > Honest Engagement",
      "episode": "V2",
      "issue": "프롬프트에 '톰 행크스처럼 보이는 남자' 포함 → 실존 인물 닮음",
      "fix": "'50대 백인 남성, 친근한 인상' 같은 일반 묘사로 변경"
    }
  ],

  "ai_rights_check": {
    "real_person_likeness": "PASS (생성 인물 5명 모두 일반 묘사)",
    "copyrighted_style": "WARNING (V3 프롬프트 'Wong Kar-wai style' 포함)",
    "music_license": "PASS (SUNO 자가 생성)",
    "training_data_risk": "WARNING (Seedance 2.0 사용 → MPA 이슈 인지)"
  },

  "platform_policy": {
    "instagram_reels": "OK with #광고 #AI 표시",
    "youtube_shorts": "OK",
    "vimeo_business": "라이선스 정보 디스크립션에 명시 필요"
  },

  "audit_summary": {
    "block_count": 1,
    "warning_count": 2,
    "ai_rights_warnings": 2,
    "overall_status": "FIX REQUIRED",
    "estimated_fix_time": "45 minutes"
  }
}
```

## 빠른 점검 체크리스트 (v0.4 확장)

### 기본 (v0.2)
- [ ] "절대·무조건·100%·확정" 검색 → 0건
- [ ] 가격·할인율 정확성
- [ ] 광고 표시 (#광고·#AD)
- [ ] 미성년자 등장 시 동의·인증
- [ ] 카테고리별 필수 고지문

### AI 시대 (v0.4 신규)
- [ ] 프롬프트에 실존 인물 이름 0건
- [ ] 프롬프트에 영화·드라마·캐릭터 제목 0건
- [ ] 프롬프트에 "in the style of [감독]" 0건
- [ ] 생성 인물이 실존 인물과 닮지 않음 (육안 확인)
- [ ] 음원 라이선스 확보 또는 완전 창작
- [ ] AI 생성 콘텐츠 표시 (플랫폼 정책)
- [ ] 학습 데이터 권리 이슈 인지 문서

## 가드레일 라이브러리 (v0.4 구조)

```
guardrails/
├── kr_categories/                  ← 한국 광고 카테고리
│   ├── golf_membership.yaml
│   ├── food_health.yaml
│   ├── finance.yaml
│   ├── real_estate.yaml
│   └── general.yaml
├── ai_rights/                      ← v0.4 신규
│   ├── openai_usage.yaml
│   ├── sag_aftra_ai.yaml
│   ├── mpa_copyright.yaml
│   └── digital_replica.yaml
├── platforms/
│   ├── meta.yaml
│   ├── tiktok.yaml
│   ├── youtube.yaml
│   └── vimeo.yaml                  ← v0.4 신규
└── kr_laws/
    ├── advertising_law.yaml
    ├── privacy_law.yaml
    └── consumer_law.yaml
```

캠페인 시작 시 해당 카테고리 + 플랫폼 + AI 권리 yaml들을 모두 로드.

## 시스템 호출

- `intake-router`가 캠페인 카테고리 + 플랫폼 + AI 생성 여부 분류하면 → 가드레일 자동 로드
- `script-writer` 단계마다 새 카피 실시간 체크
- `prompt-engineer`의 프롬프트도 체크 (실존 인물·스타일 모방 검출)
- `editor`의 마지막 단계에 전체 패키지 체크
- 외주 인계 직전 수동 호출

## 휴리스틱 (v0.4 보강)

- **BLOCK은 무조건 수정**, WARNING은 검토 후 결정
- **AI 권리 이슈는 BLOCK으로 다루는 게 안전** — 사후 분쟁이 비싸다
- **시리즈는 가장 보수적인 편 기준으로 통일**
- **모델 선택이 가드레일에 영향**: Seedance는 MPA 이슈, OpenAI는 사용 정책
- **AI 표시는 안전판** — 의무가 아니어도 표시하면 추후 리스크 ↓
- **법무 검토와 별개 운영** — 이 스킬은 1차 필터, 최종 책임은 사람

## 오픈크랩 컨텍스트

외부 OpenCrab 의존성:
- 이 저장소는 정책 원문 스냅샷을 번들하지 않습니다.
- 근거 확인이 필요하면 OpenCrab MCP에서 `movie_seedance_pack` 및 외부 권위 자료 노드를 조회합니다.
- 우선 조회할 근거: OpenAI Usage Policies, Vimeo Acceptable Use Policy, MPA copyright/Seedance notice, SAG-AFTRA AI/voice/likeness guidance.
- OpenCrab MCP를 사용할 수 없으면 현재 스킬 본문은 합성된 가드레일로만 취급하고, 고위험 법무 판단 전 최신 원문 확인을 요청합니다.
- 한국 광고 관련 법규는 프로젝트별 자체 정리와 최신 법령 확인이 필요합니다.

법규는 변경되므로 분기마다 업데이트 권장.
