---
name: intake-router
description: Route user video requests to right team and skills. Classifies format, purpose, platform, duration, AI rights, clip strategy. Use at entry point of every video task to determine workflow.
---

# Intake Router

작업 요청을 받으면 가장 먼저 실행되는 라우팅 스킬. 들어온 주제를 **형태·목적·플랫폼**으로 분류하고
적절한 **팀(kkirikkiri/pumasi)** 과 **모드(순차/병렬)** 를 결정합니다.

## When to use

영상 제작 관련 작업이 시작될 때, 다른 어떤 스킬보다 먼저 실행. 트리거 예시:
- "OOO 영상 만들어줘"
- "이 주제로 뮤비/광고/숏폼 기획해줘"
- "영상 컨텐츠 아이디어 좀"
- "이거 영상으로 어떻게 풀까?"

이미 분류가 명확하고 사용자가 특정 스킬을 지목한 경우(예: "FACS로 표정 프롬프트만 짜줘")는
이 스킬을 건너뛰고 해당 스킬을 바로 실행해도 됩니다.

## Classification Matrix

### 1. 영상 형태 (Format)

| 형태 | 길이 | 특징 | 기본 가이드 |
|------|------|------|-------------|
| 시네마틱 컷 | 단일 컷 | 이미지 1장 + 짧은 영상화 | 시네마틱 이미지 생성 |
| 숏폼 | 15~60초 | 후킹 강력, 세로 비율 | MV 가이드 + 플랫폼 어댑터 |
| 뮤직비디오 | 1~5분 | 음악 동기화, 컷 전환 빠름 | AI 뮤직비디오 가이드 |
| 광고/브랜드필름 | 15초~3분 | 메시지 명확, 후킹+CTA | 단편영화 + 시네마틱 |
| 단편영화 | 3~20분 | 내러티브 완결, 대사 가능 | AI 단편영화 가이드 |
| 다큐/인터뷰 | 가변 | 정보 전달, 인서트 위주 | 단편영화 + 편집 강조 |

### 2. 영상 목적 (Purpose)

| 목적 | 우선순위 | 기본 팀 |
|------|----------|---------|
| 브랜딩 | 톤·룩 일관성 > 메시지 | kkirikkiri |
| 스토리텔링 | 내러티브 > 비주얼 | pumasi |
| 정보 전달 | 명확성 > 감성 | pumasi |
| 감성 환기 | 무드 > 정보 | kkirikkiri |
| 제품 시연 | 디테일 > 분위기 | pumasi |
| 아티스트 표현 | 작가성 > 효율 | kkirikkiri |

### 3. 플랫폼 (Platform)

| 플랫폼 | 비율 | 길이 | 후킹 | 사운드 |
|--------|------|------|------|--------|
| YouTube (가로) | 16:9 | 1분~ | 0~5초 | ON |
| YouTube Shorts | 9:16 | ~60초 | 0~3초 | ON |
| Instagram Reels | 9:16 | ~90초 | 0~2초 | ON (음악 필수) |
| Instagram Feed | 1:1 또는 4:5 | ~60초 | 0~3초 | 자동재생 무음 고려 |
| TikTok | 9:16 | ~3분 | 0~2초 | ON |
| 영화제 출품 | 16:9 또는 시네스코프 | 가변 | 길어도 됨 | 후처리 정성 |
| 웹사이트 히어로 | 16:9 또는 9:16 모바일 | 5~15초 루프 | 즉시 | 무음 기본 |
| 사내/B2B | 16:9 | 가변 | 0~10초 | ON |

## Routing Logic

### Step 1: 분류 추출
사용자 입력에서 다음을 추출. 명시되지 않은 항목은 사용자에게 한 번에 물음:
- 형태(이미 아는 경우)
- 목적(핵심 가치)
- 플랫폼(어디서 재생)
- 톤/레퍼런스(있다면)
- 제약(길이, 마감, 자산)

### Step 2: 팀 선택

**kkirikkiri 호출 조건** (하나 이상 해당):
- 목적이 브랜딩·감성환기·아티스트 표현
- 형태가 뮤직비디오·시네마틱 컷
- "느낌이", "분위기", "톤", "무드", "결" 같은 단어 등장
- 레퍼런스가 영화·뮤비·아트워크 중심

**pumasi 호출 조건** (하나 이상 해당):
- 목적이 스토리텔링·정보전달·제품시연
- 형태가 단편영화·광고·다큐·튜토리얼
- "메시지", "전달", "스크립트", "샷리스트" 같은 단어 등장
- 명확한 시나리오·CTA가 있음

**두 팀 모두 호출** (대부분의 실전 작업):
- 광고·브랜드필름은 거의 항상 둘 다 — kkirikkiri가 톤 잡고 pumasi가 구현
- 위에서 양쪽 조건이 둘 다 매칭되는 경우

### Step 3: 모드 선택

**순차 모드**:
- 작업 단위가 1~2개 스킬로 끝남
- 사용자가 "단계별로", "하나씩", "확인하면서" 같은 표현
- 초기 학습/탐색 단계
- 결과물에 대한 사용자 확신이 낮음 → 중간 점검 필요

**병렬 모드**:
- 풀 파이프라인 (기획→샷→프롬프트→편집)
- "안 3개 줘", "다각도로", "여러 버전" 같은 표현
- 시간 제약 + 사용자 위임도 높음
- 컨셉 발산이 필요한 초기 단계

### Step 4: 출력 포맷

라우팅 결정을 다음 JSON으로 출력하고, 그대로 다음 스킬에 넘김:

```json
{
  "classification": {
    "format": "music_video",
    "purpose": "branding",
    "platform": "instagram_reels",
    "duration_s": 60,
    "tone_keywords": ["dark", "premium", "terracotta"]
  },
  
  "v06_clip_strategy": {
    "single_clip_possible": false,
    "reason": "60초는 Seedance 2.0의 15초 HARD LIMIT 초과",
    "estimated_clip_count": 6,
    "avg_clip_length_s": 10,
    "clip_segmentation_skill_needed": true,
    "editor_assembly_required": true
  },
  
  "team": "kkirikkiri",
  "secondary_team": "pumasi",
  "mode": "parallel",
  "agent_calls": [
    {"agent": "mood-curator", "task": "..."},
    {"agent": "reference-scout", "task": "..."},
    {"agent": "aesthetic-director", "task": "..."}
  ],
  "shared_skills_needed": ["cinematic-shot", "mv-builder", "clip-segmentation"],
  "opencrab_context": ["영상제작 workflow"],
  "rationale": "60초 영상은 Seedance 단일 클립 불가 → 6개 클립 + 편집. clip-segmentation 필수."
}
```

### v0.6 영상 길이 분류 자동 룰

| 요청 길이 | single_clip_possible | 권장 클립 수 |
|---------|---------------------|------------|
| ≤ 4초 | false (Seedance 최소 4초) | 1 (트림으로 처리) |
| 4-15초 | **true** | 1 |
| 16-30초 | false | 2-3 |
| 31-60초 | false | 4-6 |
| 1-3분 | false | 8-15 |
| 3분+ | false | 15+ |

## 휴리스틱 빠른 매핑

자주 들어오는 요청의 빠른 답안:

| 사용자 입력 (예시) | 팀 | 모드 |
|-----|-----|------|
| "브랜드 무드필름 만들고 싶어" | kkirikkiri | 병렬 |
| "이 캐릭터 표정 프롬프트만 좀" | (스킬 직호출: facs-expression) | 순차 |
| "유튜브 광고 30초 시나리오부터" | pumasi | 순차 |
| "K-pop 뮤비 컨셉 3안 줘" | kkirikkiri | 병렬 |
| "이 시나리오 샷리스트 짜줘" | pumasi | 순차 |
| "히어로 비디오 처음부터 끝까지" | 둘 다 | 병렬 |
| "Seedance 프롬프트 짜는 거 알려줘" | (스킬 직호출: seedance-prompt) | 순차 |

## 모호한 경우의 행동

- 형태/목적/플랫폼 중 2개 이상 모르면 → **사용자에게 한 번에 묻기** (ask_user_input_v0 사용)
- 팀 선택이 갈리면 → **둘 다 호출, 병렬 모드**
- 사용자가 "그냥 알아서 해줘"라고 하면 → 가장 보편적인 매핑 채택, 처음 결과 보여주고 피드백 받기

## 외부 의존성

이 스킬은 다음을 호출할 수 있어야 합니다:
- 오픈크랩 MCP: `opencrab_run_workflow`, `opencrab_search_packs`
- 사용자 질의 도구: `ask_user_input_v0`
- 후속 스킬: teams/* 및 skills/* 의 SKILL.md들
