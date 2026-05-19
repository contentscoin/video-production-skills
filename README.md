<h1 align="center">Video Production System v0.6</h1>

<p align="center">
  <strong>AI 영상 제작을 위한 Claude Skills 28종</strong><br>
  <em>kkirikkiri (취향공동체) + pumasi (품앗이) — 듀얼 팀 아키텍처</em>
</p>

<p align="center">
  <a href="#-빠른-시작">빠른 시작</a> ·
  <a href="#-설치">설치</a> ·
  <a href="#-28-스킬-카탈로그">28 스킬</a> ·
  <a href="#-제작-워크플로우">워크플로우</a> ·
  <a href="#-지식-기반">지식 기반</a> ·
  <a href="CONTRIBUTING.md">기여</a>
</p>

<p align="center">
  <img alt="Skills" src="https://img.shields.io/badge/skills-28-c9a961">
  <img alt="License" src="https://img.shields.io/badge/license-Apache%202.0-blue">
  <img alt="Compatibility" src="https://img.shields.io/badge/Claude.ai%20%7C%20Claude%20Code-compatible-success">
  <img alt="Version" src="https://img.shields.io/badge/version-0.6-orange">
</p>

---

## 무엇을 하는 시스템인가요?

Claude를 **종단간(end-to-end) AI 영상 제작 협업자**로 변환하는 28개의 Claude Skills입니다. 톤·정서 찾기(kkirikkiri 팀)부터 샷 설계, 프롬프트 엔지니어링, FACS 표정 코딩, Seedance 2.0의 15초 제한을 위한 클립 분할, 그리고 풀 포스트프로덕션 명세(pumasi 팀)까지.

각 스킬의 근거는 다음에서 옵니다:

- 📦 **6개 OpenCrab 팩** (movie_seedance_pack + 율파파 Notion 가이드 5종) — 71 sources / 484 evidence / 777 nodes / 1,297 relationships
- 🛡 **5개 외부 권위 자료** (OpenAI Usage / SAG-AFTRA AI / MPA Copyright / Vimeo AUP / U.S. Copyright Office)
- ⚙ **4개 시스템 고유 추가** (series-closer, copy-tone-check, workflow-curator, clip-segmentation)

모든 스킬의 출처가 명시적입니다.

## 왜 필요한가요?

사용자가 "30초 브랜드 필름 만들어줘"라고 했을 때 Claude가 알아야 할 것들:

- 영화적 샷 묘사 어휘 (5레이어: 사이즈·앵글·렌즈·조명·룩)
- Seedance 2.0의 4-15초 클립 제한
- 한국 광고법 가드레일
- MPA-안전 레퍼런스 변환 ("in the style of [감독]" 같은 표현 회피)
- 얼굴 컷의 FACS 코딩된 표정
- 결과물을 표준 인계 패키지로 묶는 방법

이 시스템은 위 모든 것을 **명시적이고 분리된 스킬**로 제공합니다. 필요할 때만 활성화되어 컨텍스트 비용을 낮게 유지하고 출력 일관성을 보장합니다.

## ⚡ 빠른 시작

### 방법 1: Claude.ai에서 단일 스킬 시도 (1분)

```bash
# 업로드 가능한 zip 생성
git clone https://github.com/contentscoin/video-production-skills.git
cd video-production-skills
./scripts/package.sh

# Claude.ai에서: dist/clip-segmentation.zip 업로드
```

### 방법 2: Claude Code에 28개 모두 설치

```bash
git clone https://github.com/contentscoin/video-production-skills.git
cd video-production-skills
./install.sh
```

### 방법 3: 읽고 학습하기

```bash
git clone https://github.com/contentscoin/video-production-skills.git
cd video-production-skills
cat skills/shared/clip-segmentation/SKILL.md
```

## 📦 설치

환경별 안내. 자세한 내용은 [INSTALL.md](INSTALL.md) 참고.

### → Claude.ai (웹 / 데스크톱)

1. `./scripts/package.sh` 실행하여 각 스킬을 `.zip`으로 생성 (`dist/`)
2. Claude.ai에서: **설정 → Skills → 업로드**
3. .zip 파일 하나 또는 여러 개 업로드

각 .zip 안에는 `SKILL.md`가 폴더 루트에 있는 단일 스킬 폴더가 들어 있습니다 (Claude Skills v1 사양).

### → Claude Code (CLI)

```bash
git clone https://github.com/contentscoin/video-production-skills.git
cd video-production-skills
./install.sh                  # 28개 모두 ~/.claude/skills/ 로 복사
```

원하는 것만 골라 설치:

```bash
./install.sh --only mood-curator,shot-designer,seedance-prompt
```

확인:

```bash
ls ~/.claude/skills/
# aesthetic-director/  clip-segmentation/  mood-curator/ ...
```

### → 수동 (그냥 읽기만 하려면)

각 스킬은 독립된 `SKILL.md`로 직접 읽을 수 있습니다:

```bash
git clone https://github.com/contentscoin/video-production-skills.git
cd video-production-skills/skills
ls -R                         # 구조 탐색
cat shared/clip-segmentation/SKILL.md
```

### → Claude API

[Anthropic Skills API 문서](https://docs.claude.com/en/docs/build-with-claude/skills) 따라 업로드. 각 `SKILL.md`가 그대로 사용 가능.

## 🎯 28 스킬 카탈로그

### 9개 에이전트 — 두 팀의 분업

**kkirikkiri 팀 — 취향공동체 (Taste Community)** · 작품의 **결**(texture)을 찾는 역할

| 에이전트 | 역할 | 한 줄 설명 |
|---|---|---|
| [mood-curator](skills/agents/kkirikkiri/mood-curator/) | 결의 발견자 | 5색 팔레트 + 재질감 + 광원 + 무드 키워드 큐레이션 |
| [reference-scout](skills/agents/kkirikkiri/reference-scout/) | 차용과 회피의 균형 | 감독·작품명을 안전한 기술 어휘로 자동 변환 (MPA 저작권 안전) |
| [aesthetic-director](skills/agents/kkirikkiri/aesthetic-director/) | 결의 최종 결정자 | look_spec 통합 — kkirikkiri와 pumasi 사이의 인터페이스 |
| [narrative-weaver](skills/agents/kkirikkiri/narrative-weaver/) | 정서의 곡선을 그리는 사람 | 비트 단위 정서 곡선·구조, 비트별 5요소 |

**pumasi 팀 — 품앗이 (Collaborative Labor)** · 작품을 **실제로 만들어내는** 역할

| 에이전트 | 역할 | 한 줄 설명 |
|---|---|---|
| [script-writer](skills/agents/pumasi/script-writer/) | 정서를 구조로 풀어내는 사람 | 비트 → 씬 시나리오 + 자막 + CTA + AI 표시 자막 |
| [shot-designer](skills/agents/pumasi/shot-designer/) | 씬을 샷으로 분해하는 사람 | shotlist.csv 생성 (5레이어 시네마틱 명세 포함) |
| [prompt-engineer](skills/agents/pumasi/prompt-engineer/) | 샷을 모델 입력어로 변환하는 사람 | 4단계 파이프라인 (foundations → cinematic → adapter → seedance) |
| [motion-director](skills/agents/pumasi/motion-director/) | 표정과 움직임을 지시하는 사람 | FACS 표정 코딩 + 신체 모션 |
| [editor](skills/agents/pumasi/editor/) | 조각들을 한 호흡으로 잇는 사람 | 포스트프로덕션 명세 + edit_decision_list 어셈블 |

### 19개 공유 스킬 — 5개 기능 카테고리

#### 🟢 기초 인프라 (5) — 어휘의 기본

| 스킬 | 한 줄 설명 |
|---|---|
| [intake-router](skills/shared/intake-router/) | 작업 요청 진입점 라우팅. 형태·목적·플랫폼으로 분류하고 팀(kkirikkiri/pumasi)·모드(순차/병렬)를 결정 |
| [cinematic-shot](skills/shared/cinematic-shot/) | 영화적 한 컷의 시각 명세를 **샷 사이즈 → 앵글 → 렌즈 → 조명 → 룩** 5레이어로 구조화 |
| [facs-expression](skills/shared/facs-expression/) | AI 캐릭터의 정밀한 얼굴 연기. FACS의 AU·AD·Intensity 체계로 표정을 좌표화 |
| [seedance-prompt](skills/shared/seedance-prompt/) | Seedance 2.0 **멀티모달 동시 입력**(이미지 9 + 비디오 3 + 오디오 3) + 소스 바인딩 |
| [mv-builder](skills/shared/mv-builder/) | 뮤직비디오 풀 파이프라인. 율파파 7단계 (음악 분석 → 컨셉 → 샷리스트 → 이미지 → 비디오 → 편집) |

#### 🟣 시리즈·캠페인 (4) — 규모에서의 일관성

| 스킬 | 한 줄 설명 |
|---|---|
| [character-pool](skills/shared/character-pool/) | 시리즈 전반 등장 캐릭터를 **명시적 자산**으로 관리. 시트(ID) 기반으로 어느 편에서나 동일 재현 |
| [series-variation](skills/shared/series-variation/) | 시리즈에서 편마다의 **차이를 의도적으로 설계**. LOCKED + VARIABLE 매트릭스 |
| [post-production-spec](skills/shared/post-production-spec/) | AI 생성 영상의 **편집·후처리 명세**를 표준 포맷으로 작성. JSON 표준 |
| [guardrail-check](skills/shared/guardrail-check/) | 광고·콘텐츠의 카피·시각·시나리오에 대한 **금지 표현·법적 리스크·플랫폼 정책·AI 권리** 자동 점검 (4-Part) |

#### 🟠 청사진 정렬 (5) — 생성·검증·패키징

| 스킬 | 한 줄 설명 |
|---|---|
| [visual-bible](skills/shared/visual-bible/) | 시리즈의 마스터 비주얼 바이블 7섹션 잠금 (브랜드·컬러·룩·모티프·금기 등) |
| [image-prompt-foundations](skills/shared/image-prompt-foundations/) | 이미지 프롬프트의 **모델 독립적 일반 원칙**. 모호함 3유형 + 그림자 + 5층 구조 |
| [model-adapter](skills/shared/model-adapter/) | 모델별 입력 패턴 변환. GPT Image 2 · Nano Banana Pro · Seedance · Kling 어휘 |
| [qa-review](skills/shared/qa-review/) | 생성 산출물의 **체크리스트 기반 점검**과 재생성·수정 루프. 6차원 점검, 3사이클 한도 |
| [production-brief](skills/shared/production-brief/) | 영상 제작의 **표준 산출물 파일들**을 정의·생성. 5표준 파일 + clips/ 디렉토리 |

#### 🟡 운영 보강 (2) — 실제 운영에서 발견된 갭

| 스킬 | 한 줄 설명 |
|---|---|
| [series-closer](skills/shared/series-closer/) | 시리즈의 **마지막 편**(또는 종합 편) 전용. 3 Type (리프라이즈 / 종합 풍경 / 압축 내러티브) |
| [copy-tone-check](skills/shared/copy-tone-check/) | 시리즈 캠페인의 **카피·자막·CTA들을 한꺼번에** 놓고 톤 일관성 점검. 5차원 |

#### 🔵 권리·메타 (3) — v0.6 핵심 추가 포함

| 스킬 | 한 줄 설명 |
|---|---|
| [music-rights-check](skills/shared/music-rights-check/) | 영상의 **BGM·SFX·VO** 등 음향 자산 권리 점검. 5 카테고리 (자작·로열티 프리·싱크·AI·보이스 클로닝) |
| [workflow-curator](skills/shared/workflow-curator/) | OpenCrab 워크플로우 진단·재구성 메타 스킬. 진단만 제공, 자동 수정 없음 |
| [clip-segmentation](skills/shared/clip-segmentation/) ⭐ | 긴 시나리오를 **15초 이하 클립으로 분할** + 편집 시 연결되도록 설계. 4 패턴. **v0.6 핵심** |

## 🎬 제작 워크플로우

30초 브랜드 필름을 만들 때의 흐름:

```
사용자: "30초 브랜드 필름 만들고 싶어"
   ↓
[01] intake-router        → 분류 + 클립 전략 결정 (8개 클립 필요)
[02] kkirikkiri 4 에이전트  → look_spec + narrative_arc (병렬)
[03] visual-bible LOCK + character-pool 등록
[04] script-writer        → 7-비트 씬 시나리오
[05] shot-designer        → shotlist.csv (9 rows)
[06] clip-segmentation    → 8 생성 클립 + 1 편집-전용 ⭐ v0.6 핵심
[07] prompt-engineer × 8  → 이미지 + Seedance 프롬프트
[08] motion-director      → 얼굴 컷에만 FACS
[09] editor               → edit_decision_list + music-rights 자동
[10] qa-review + guardrail-check + production-brief 패키징
   ↓
출력: 5 표준 파일 + clips/ 디렉토리 + 최종 마스터
예상 시간: 4-7시간 (BGM 외주 제외)
```

자세한 설명은 [docs/workflow.md](docs/workflow.md) 참고.

## 📚 지식 기반

모든 스킬은 출처를 다음 3가지 기호로 표시합니다:

### 📦 OpenCrab 팩 (6종, 1,200+ 노드)

| 팩 | 통계 | 활용 스킬 |
|---|---|---|
| **movie_seedance_pack** | 71 sources · 484 evidence · 777 nodes · 1,297 relationships | 18+ 스킬 (중심 청사진) |
| Seedance 2.0 프롬프팅 가이드 | 26 nodes · 율파파 | seedance-prompt, clip-segmentation |
| 시네마틱 이미지 생성 가이드 | 26 nodes · 율파파 | cinematic-shot, aesthetic-director, shot-designer |
| AI 단편영화 만들기 가이드 | 26 nodes · 율파파 | narrative-weaver, mv-builder, script-writer |
| AI FACS 표정연기 가이드 | 26 nodes · 율파파 | facs-expression, motion-director |
| 영화만들기·이미지 프롬프트 | 13 nodes · MCP | image-prompt-foundations, prompt-engineer |

위 OpenCrab 팩과 권위 자료 원문은 이 저장소에 번들하지 않는 **외부 의존성**입니다. 근거 수준의 확인이 필요하면 OpenCrab MCP에서 해당 팩과 노드를 조회하세요.

### 🛡 외부 권위 자료 (5종)

OpenAI Usage Policies · SAG-AFTRA AI Guidelines · MPA Copyright · Vimeo AUP · U.S. Copyright Office (AI 음악)

### ⚙ 시스템 고유 (4종)

series-closer · copy-tone-check · workflow-curator · clip-segmentation

이 투명성은 의도된 것입니다 — Claude가 추천하는 모든 것의 근거가 무엇인지 정확히 알 수 있어야 합니다.

## 🔧 개발

```bash
# 전체 스킬 설치
./install.sh

# 업로드 가능한 zip 생성
./scripts/package.sh         # dist/<skill-name>.zip × 28

# 스킬 형식 검증 (YAML frontmatter 등)
python3 scripts/validate.py
```

## 📝 라이선스

Apache 2.0 — [LICENSE](LICENSE) 참고.

허용적인 오픈소스 라이선스입니다. 상업적 사용·수정·재배포가 모두 가능합니다 (저작자 표시 필요).

OpenCrab 팩과 율파파 Notion 가이드는 각자의 원본 라이선스를 따릅니다. 이 저장소의 라이선스는 통합·합성(SKILL.md 구조, 통합 로직, 시스템 고유 스킬)에만 적용됩니다.

## 🙏 감사의 말

다음 자료들 위에 만들어졌습니다:

- **율파파 (Yoolpapa)** Notion 가이드 — Seedance, 시네마틱 이미지, AI 단편영화, FACS 표정연기, 이미지 프롬프트
   ->  율파파님의 ai로 영화만들기 오픈채팅방 : https://open.kakao.com/o/g82nllki
- **알렉스(Alexai)** 오픈크랩 ㅡ **movie_seedance_pack** — OpenCrab의 공개 expert-pack 온톨로지
   -> 오픈크랩 주소 : Opencrab.sh
- **Anthropic** — Claude Skills 사양 + Claude Code

## 🤝 기여

[CONTRIBUTING.md](CONTRIBUTING.md) 참고.

특히 환영하는 기여:

- SKILL.md 콘텐츠 번역 (현재 한/영 혼용)
- 추가 모델 어댑터 (Wan, Hailuo, Pika 등)
- `examples/` 의 새 예시
- 트리거가 잘 동작하지 않는 description 버그 리포트

---

<details>
<summary><strong>🌐 English</strong></summary>

# Video Production System v0.6

**28 Claude Skills for AI-assisted video production**  
*kkirikkiri (Taste Community) + pumasi (Collaborative Labor) — dual-team architecture*

## What is this?

A system of 28 Claude Skills that turns Claude into an end-to-end AI video production collaborator. From mood-finding (kkirikkiri team) through shot design, prompt engineering, FACS expression coding, clip segmentation for Seedance 2.0's 15-second limit, to full post-production specification (pumasi team).

Grounded in:
- 📦 **6 OpenCrab packs** (movie_seedance_pack + 5 Yoolpapa Notion guides) — 71 sources / 484 evidence / 777 nodes / 1,297 relationships
- 🛡 **5 external authorities** (OpenAI Usage / SAG-AFTRA AI / MPA Copyright / Vimeo AUP / U.S. Copyright Office)
- ⚙ **4 system-unique additions** (series-closer, copy-tone-check, workflow-curator, clip-segmentation)

OpenCrab packs and source-level authority snapshots are external dependencies, not bundled files in this repository. Use the OpenCrab MCP when source-level provenance must be checked.

Every skill's provenance is explicit.

## Quick Start

```bash
# Build uploadable zips for Claude.ai
git clone https://github.com/contentscoin/video-production-skills.git
cd video-production-skills
./scripts/package.sh

# All 28 to Claude Code
./install.sh
```

## The 28 Skills

### 9 Agents

**kkirikkiri team — Taste Community** · finds the *결* (texture/grain)

- mood-curator · reference-scout · aesthetic-director · narrative-weaver

**pumasi team — Collaborative Labor** · brings the work into being

- script-writer · shot-designer · prompt-engineer · motion-director · editor

### 19 Shared Skills

- **🟢 Foundation (5)**: intake-router · cinematic-shot · facs-expression · seedance-prompt · mv-builder
- **🟣 Series & Campaign (4)**: character-pool · series-variation · post-production-spec · guardrail-check
- **🟠 Blueprint (5)**: visual-bible · image-prompt-foundations · model-adapter · qa-review · production-brief
- **🟡 Operational (2)**: series-closer · copy-tone-check
- **🔵 Rights & Meta (3)**: music-rights-check · workflow-curator · ⭐ clip-segmentation (v0.6 critical)

## Workflow Example

Producing a 30-second brand film:

```
[01] intake-router → classification + clip strategy
[02] kkirikkiri 4 agents (parallel) → look_spec + narrative_arc
[03] visual-bible LOCK + character-pool registration
[04] script-writer → 7-beat scenes
[05] shot-designer → shotlist.csv
[06] clip-segmentation → 8 generation clips + 1 edit-only ⭐
[07] prompt-engineer × 8 → image + seedance prompts
[08] motion-director → FACS for face shots
[09] editor → edit_decision_list + music-rights auto
[10] qa-review + guardrail-check + production-brief packaging
   ↓
Output: 5 standard files + clips/ + final master
Estimated time: 4-7 hours (excluding BGM)
```

See [docs/workflow.md](docs/workflow.md) for full annotation.

## License

Apache 2.0. See [LICENSE](LICENSE). Underlying packs and guides retain their original licenses; this repository's license covers only the synthesis.

## Acknowledgments

Built on: 율파파 (Yoolpapa) Notion guides · movie_seedance_pack expert ontology · Anthropic Claude Skills

</details>

---

<p align="center">
  <em>Foundation: 율파파 Notion 가이드 · movie_seedance_pack 청사진 · AI 권리 통합</em>
</p>
