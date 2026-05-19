# GitHub Push 가이드

기존 저장소(`contentscoin/video-production-skills`)에 잘못 push된 구조를 덮어쓰기 위한 절차입니다.

## 절차 (5분)

### 1. 압축 해제

```bash
cd ~/Downloads
unzip video-production-skills.zip
cd video-production-skills
```

### 2. 구조 확인

```bash
ls
```

다음이 보여야 합니다:

```
.github         CONTRIBUTING.md   PUBLISH.md     install.sh
.gitignore      INSTALL.md        PUSH_NOW.md    scripts
README.md       LICENSE           docs           skills
                                  examples
```

**보이면 안 되는 것**: `mnt/` 폴더, 폴더 안에 또 폴더가 있는 경우 → 한 단계 안으로 `cd`

### 3. 28개 스킬 검증

```bash
find skills -name "SKILL.md" | wc -l
# 결과: 28

head -3 skills/agents/kkirikkiri/mood-curator/SKILL.md
# 결과:
# ---
# name: mood-curator
# description: Curate visual mood for AI video. ...
```

### 4. Git 초기화 및 강제 push

```bash
# 기존 .git 폴더 있다면 제거
rm -rf .git

git init
git branch -M main
git add .
git commit -m "Restructure: proper Claude Skills v1 directory layout"

git remote add origin https://github.com/contentscoin/video-production-skills.git
git push -u origin main --force
```

`--force`로 기존 잘못된 구조를 덮어씁니다. 본인 저장소이므로 안전합니다.

### 5. (선택) 첫 릴리스 태그

```bash
git tag -a v0.6.0 -m "v0.6.0 - Initial Release"
git push origin v0.6.0
```

태그 push하면 GitHub Actions가 28개 .zip을 자동 빌드해 릴리스에 첨부합니다.

## Push 후 확인

브라우저에서 `https://github.com/contentscoin/video-production-skills` 접속:

### 메인 페이지 — 루트 파일
```
.github/        scripts/        README.md
docs/           skills/         LICENSE
examples/                       INSTALL.md
                                CONTRIBUTING.md
                                PUBLISH.md
                                PUSH_NOW.md
                                install.sh
                                .gitignore
```

**없어야 하는 것**: `mnt/` 폴더, 루트의 `release.yml`, `package.sh`, `validate.py`

### skills/ 폴더
```
skills/
├── agents/
│   ├── kkirikkiri/  (4개 폴더)
│   └── pumasi/      (5개 폴더)
└── shared/          (19개 폴더)
```

28개 폴더 안에 각각 `SKILL.md`.

### Actions 탭
- "Validate Skills" 자동 실행 → 녹색 ✓
- (태그 push했다면) "Package Skills on Release" 도 실행

## 트러블슈팅

### 인증 오류
```
remote: Support for password authentication was removed
```

Personal Access Token 사용:
1. https://github.com/settings/tokens
2. Generate new token (classic)
3. `repo` 스코프 체크
4. push 시 password 자리에 토큰 입력

### 압축이 이상하게 풀림 (macOS Safari)

Safari가 자동으로 압축을 풀면서 폴더 한 단계가 추가될 수 있습니다:

```bash
# 안쪽 폴더로 한 번 더 들어가기
cd video-production-skills
```

또는 터미널에서 직접:
```bash
cd ~/Downloads
unzip video-production-skills.zip
cd video-production-skills
```

## Push 성공 후 추가 작업

### Topics 추가 (검색 노출)
저장소 페이지 → About 옆 ⚙ → 추가:
```
claude  claude-skills  ai-video  seedance  video-production
prompt-engineering  anthropic  korean  filmmaking
```

### Discussions 활성화
Settings → General → Features → Discussions 체크
