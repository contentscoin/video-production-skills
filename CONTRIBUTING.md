# Contributing

기여를 환영합니다! 이 시스템은 영상 제작 실무에서 발견한 패턴을 모은 살아있는 자료라, 여러분의 운영 경험이 그대로 가치가 됩니다.

## 🌟 어떤 기여가 환영받나요

### 매우 환영
- **새 모델 어댑터**: Wan, Hailuo, Pika 등을 model-adapter에 추가
- **번역**: 현재 한/영 혼용. 영문 통일 또는 다른 언어 번역
- **examples/**: 자신의 프로젝트 산출물 (브랜드명 마스킹 후)
- **버그 리포트**: description이 안 트리거되거나, 잘못된 어휘 변환 등
- **새 가드레일**: 다른 나라 광고법, 새로운 AI 권리 정책

### 환영
- **새 스킬**: 단, 기존 스킬과 명확히 다른 책임이어야 함
- **워크플로우 변형**: 단편/시리즈/뮤비 외에 새로운 포맷
- **테스트 케이스**: 스킬이 의도대로 동작하는지 검증

### 조심스러움
- **대규모 리팩토링**: 먼저 issue로 논의
- **버전 번호 변경**: maintainer만 가능
- **OpenCrab 팩 출처 변경**: 검증 필요

## 🛠 개발 환경

```bash
git clone https://github.com/contentscoin/video-production-skills.git
cd video-production-skills

# 기존 스킬 변환 도구 (레거시 원본이 있을 때만)
python3 scripts/convert_skills.py /path/to/legacy/skills

# 패키징
./scripts/package.sh

# 설치
./install.sh
```

## 📐 SKILL.md 작성 가이드

새 스킬 추가 시 다음 구조 준수:

```markdown
---
name: skill-name
description: When and what. Be specific about trigger conditions (max 200 chars).
---

# Skill Name

> "One-line role description in Korean"

스킬의 한 문단 소개.

## When to call

- 트리거 조건 1
- 트리거 조건 2

## Inputs

(필요한 입력)

## Output

(생성되는 산출물)

## Heuristics

(원칙·규칙)

## 시스템 연결

- 상위: 이 스킬을 호출하는 스킬
- 하위: 이 스킬이 호출하는 스킬

## 청사진 매핑

(OpenCrab 팩 또는 외부 자료 출처)
```

### Description 작성 룰

Claude는 description으로 트리거 결정하니 중요합니다:

✅ **좋은 예**: 
> "Segment videos longer than 15 seconds into multiple generation clips for AI video production. Critical for Seedance 2.0 4-15s HARD LIMIT. Uses 4 patterns. Use when shotlist contains rows over 15 seconds."

❌ **나쁜 예**:
> "A skill for clip stuff."

룰:
- 200자 이내
- **trigger 조건**을 구체적으로 명시
- "Use when..." 패턴 사용
- 다른 스킬과 차별점 강조
- 약간 "pushy"하게 — Claude는 스킬을 덜 트리거하는 경향이 있음

### 출처 명시

스킬 본문 끝에 출처 명시:

- 📦 **OpenCrab pack 근거**: `## 청사진 매핑` 섹션에 어떤 팩의 어떤 부분 참조 명시
- 🛡 **External authority**: OpenAI, SAG-AFTRA 등 정책 명시
- ⚙ **System-unique**: 청사진 외 시스템 고유 추가임을 명시

## 🔄 Pull Request 절차

1. **Issue 먼저** (큰 변경의 경우)
2. **Fork → branch**: `feature/add-wan-adapter` 같은 명확한 이름
3. **변경**:
   - 스킬 추가 시: `skills/<category>/<name>/SKILL.md` 생성
   - `install.sh`의 `ALL_SKILLS` 배열에 이름 추가
   - 레거시 원본을 변환하는 경우 `scripts/convert_skills.py`의 `SKILL_METADATA`에 description 추가
   - `README.md`의 스킬 목록 업데이트
4. **테스트**:
   ```bash
   ./scripts/package.sh        # zip 생성 확인
   ./install.sh --dry-run      # 설치 시뮬레이션
   python3 scripts/validate.py  # YAML 형식 검증
   ```
5. **PR 작성**:
   - 무엇을 추가/변경했는지
   - 어떤 OpenCrab 팩/외부 자료에 근거하는지
   - 실제 사용 사례 (있다면)

## 🧪 테스트

### 수동 테스트

새 스킬 만들면 Claude.ai에 설치 후 실제 호출:

```
사용자: "30초 영상을 클립으로 분할해야 해"

기대: clip-segmentation 스킬 자동 활성화 → 4 패턴 중 선택
```

### 자동 검증

```bash
python3 scripts/validate.py
# - YAML frontmatter 형식
# - name 필드 (영문, 하이픈 허용)
# - description 길이 (200자 이내)
# - 폴더 구조 (folder name == name)
```

## 📋 코드 스타일

### Markdown
- 헤더는 `##` 부터 (`#`은 스킬명에만)
- 코드 블록 언어 명시 (```json, ```python 등)
- 한국어 본문 + 영어 기술 용어 혼용 OK

### Shell scripts
- `set -euo pipefail` 필수
- 색상 사용 시 변수로 정의
- `--help` 옵션 제공

### Python
- Python 3.10+
- type hints 권장
- f-string 사용

## 🌍 다국어

현재 본문은 한/영 혼용입니다. 이게 의도된 디자인입니다:
- **기술 용어**는 영어 (look_spec, shotlist, FACS)
- **설명·맥락**은 한국어
- **description (YAML)**은 영어 (Claude의 다국어 트리거 일관성)

기여 시 이 패턴 따르거나, 완전한 영문 버전 PR도 환영.

## 🤝 행동 강령

- 존중하기
- 비판은 코드/아이디어에 대해, 사람에 대해서는 X
- 출처가 불확실하면 ⚙ (system-unique)로 정직하게 표시
- 한 명의 갑작스러운 큰 변경보단 여러 명의 작은 개선이 좋음

## ❓ 질문

- **사용법**: README + INSTALL 확인 → 안 풀리면 Discussions 탭
- **버그**: Issues 탭
- **새 아이디어**: Discussions → Ideas

---

📦 Foundation: 율파파 Notion guides · movie_seedance_pack blueprint · AI rights synthesis  
🛡 Backed by external authorities (OpenAI · SAG-AFTRA · MPA · Vimeo · U.S. Copyright Office)  
⚙ System-unique additions explicitly marked

기여 감사합니다!
