# Installation Guide

세 가지 환경에서 사용할 수 있습니다. 가장 자주 쓰는 환경을 선택하세요.

---

## 🌐 Claude.ai (Web / Desktop App)

가장 쉬운 방법. 마우스 클릭만으로 설치됩니다.

### Prerequisites
- Claude Pro / Max / Team / Enterprise (Free 플랜은 Skills 미지원)
- **Settings → Capabilities → Code execution and file creation** 활성화

### 단일 스킬 설치

1. **저장소 클론 또는 zip 다운로드**:
   ```bash
   git clone https://github.com/contentscoin/video-production-skills.git
   cd vps-skills
   ```

2. **dist/ 디렉토리에서 원하는 .zip 선택**:
   ```bash
   ls dist/
   # aesthetic-director.zip  clip-segmentation.zip  editor.zip ...
   ```

3. **Claude.ai에 업로드**:
   - 좌측 사이드바: **Customize → Skills**
   - 우측 상단 **+** 버튼 → **Upload skill**
   - .zip 파일 선택
   - 자동 활성화됨

### 28개 모두 설치

위의 3번 단계를 28번 반복할 수도 있지만, 한 번에 모두 업로드하려면:

```bash
# 먼저 zip 묶음 생성 (이미 dist/에 있다면 건너뛰기)
./scripts/package.sh

# 28개 모두 업로드 (Claude.ai는 다중 선택 지원)
ls dist/*.zip
```

Claude.ai 업로드 화면에서 Ctrl/Cmd + 클릭으로 다중 선택 가능합니다.

### Team / Enterprise 사용자

조직 전체에 공유하려면:
1. 위 단계로 본인 계정에 설치
2. **Skill 상세 페이지 → Share → Entire organization**
3. 조직원 전원에게 자동 노출

### 확인

대화에서 `/` 키를 눌러 슬래시 커맨드 목록 확인. 또는 자연어로:

> "30초 브랜드 필름 만들어줘"

Claude가 자동으로 `intake-router`, `clip-segmentation` 등을 활성화합니다.

---

## 💻 Claude Code (CLI)

개발자에게 가장 추천. git pull 한 번으로 업데이트 가능.

### Prerequisites
- Claude Code 설치 완료 (`claude --version`)
- Node.js 18+

### 28개 모두 설치

```bash
git clone https://github.com/contentscoin/video-production-skills.git
cd vps-skills
./install.sh
```

스킬은 `~/.claude/skills/`에 복사됩니다.

### 선택적 설치

```bash
# 특정 스킬만
./install.sh --only mood-curator,shot-designer,seedance-prompt

# 미리 보기 (실제 설치 X)
./install.sh --dry-run

# 제거
./install.sh --uninstall
```

### 프로젝트 단위 설치

특정 프로젝트에서만 쓰고 싶다면 `.claude/skills/`로 복사:

```bash
cd /path/to/your-project
mkdir -p .claude/skills
cp -r /path/to/vps-skills/skills/agents/*/{*}/* .claude/skills/
cp -r /path/to/vps-skills/skills/shared/*/* .claude/skills/
```

git에 커밋하면 팀원 모두가 같은 스킬 사용 가능.

### 확인

```bash
ls ~/.claude/skills/
# aesthetic-director  clip-segmentation  editor  ...

# 또는 Claude Code 내에서
claude --help-skills
```

### 업데이트

```bash
cd vps-skills
git pull
./install.sh        # 기존 스킬 덮어씀
```

---

## 🔌 Claude API (개발자용)

직접 API로 스킬을 활용하려면:

```python
import anthropic

client = anthropic.Anthropic()

# 1. 스킬을 zip으로 업로드
with open("dist/clip-segmentation.zip", "rb") as f:
    skill = client.beta.skills.create(
        file=f,
        display_title="Clip Segmentation"
    )

# 2. 메시지에서 사용
message = client.beta.messages.create(
    model="claude-opus-4-7",
    max_tokens=4096,
    skills=[{"type": "custom", "id": skill.id}],
    messages=[
        {"role": "user", "content": "30초 영상을 클립으로 나눠줘"}
    ]
)
```

자세한 API 문서: [docs.claude.com/skills](https://docs.claude.com/en/docs/build-with-claude/skills)

---

## 📦 Cowork (Excel / PowerPoint)

Cowork에서 Claude.ai에 설치된 스킬은 자동 동기화됩니다:

1. Claude.ai에서 스킬 설치 (위 첫 번째 섹션)
2. Excel/PowerPoint에서 Claude 사이드바 열기
3. `/` 입력 시 사용 가능한 스킬 표시

영상 제작 스킬은 Cowork에선 제한적입니다 (Excel/PowerPoint 환경이라). `production-brief`로 shotlist.csv 분석 정도가 자연스러운 활용입니다.

---

## ❓ 설치 후 동작 안 함

### 1. Code execution이 꺼져 있음

Settings → Capabilities → **Code execution and file creation** 토글 ON 확인.

Skills는 코드 실행 환경에서 동작합니다. 이게 꺼져 있으면 SKILL.md를 읽지 않습니다.

### 2. Skill이 자동 트리거되지 않음

description이 모호하면 Claude가 트리거를 망설입니다. 강제 호출:

> "@clip-segmentation 스킬을 사용해서 30초 영상을 나눠줘"

또는 `/` 키를 눌러 슬래시 커맨드로.

### 3. 충돌

다른 마켓플레이스 스킬과 이름이 겹치면 새로 설치한 게 덮어씁니다.
기존 스킬 확인:

```bash
ls ~/.claude/skills/
```

### 4. 권한 오류 (Claude Code)

```bash
chmod +x install.sh
chmod +x scripts/package.sh
```

---

## 🚀 다음 단계

설치 후:

1. **튜토리얼**: [docs/workflow.md](docs/workflow.md)에서 30초 영상 만드는 흐름 따라하기
3. **실제 예시**: [examples/fmgmember-brand-film/](examples/fmgmember-brand-film/) 결과물 보기
4. **커스터마이징**: 자신의 브랜드에 맞게 visual-bible 활용
