# Publishing to GitHub

This guide shows how to publish this repository to GitHub so others can install via `git clone`.

Estimated time: **10 minutes**.

## Option 1: GitHub Web (no command line)

### 1. Create the repo

1. Go to https://github.com/new
2. **Repository name**: `vps-skills` (or your preferred name)
3. **Description**: "28 Claude Skills for AI video production — kkirikkiri + pumasi dual-team architecture"
4. **Public** (so others can install via `git clone`)
5. **Initialize**: do NOT add README/LICENSE/.gitignore (we already have them)
6. Click **Create repository**

### 2. Upload files

On the empty repo page, click **uploading an existing file**:

1. Drag the entire `vps-skills-github/` folder contents (not the folder itself)
2. Commit message: "Initial release: Video Production System v0.6 - 28 skills"
3. Click **Commit changes**

### 3. Create first release

1. On the repo page, click **Releases** (right sidebar)
2. Click **Create a new release**
3. **Tag**: `v0.6.0`
4. **Title**: `v0.6.0 - Initial Release`
5. **Description**: Copy from the section below
6. Click **Publish release**

GitHub Actions will auto-trigger and attach 28 `.zip` files to the release.

## Option 2: Command Line

### 1. Create the repo on GitHub

Same as Option 1 step 1.

### 2. Push from local

```bash
cd vps-skills-github

# Initialize git
git init
git add .
git commit -m "Initial release: Video Production System v0.6 - 28 skills"

# Connect to GitHub (replace contentscoin)
git branch -M main
git remote add origin https://github.com/contentscoin/video-production-skills.git
git push -u origin main
```

### 3. Tag the release

```bash
git tag -a v0.6.0 -m "v0.6.0 - Initial Release"
git push origin v0.6.0
```

This triggers `.github/workflows/release.yml` which auto-packages all 28 skills.

## Option 3: GitHub CLI (gh)

If you have `gh` installed:

```bash
cd vps-skills-github

git init
git add .
git commit -m "Initial release: Video Production System v0.6"

# Create repo and push in one command
gh repo create vps-skills --public --source=. --remote=origin --push

# Create release
gh release create v0.6.0 \
  --title "v0.6.0 - Initial Release" \
  --notes-file PUBLISH_RELEASE_NOTES.md
```

## Release Notes Template

```markdown
# Video Production System v0.6 - Initial Release

28 Claude Skills for AI-assisted video production, organized into a dual-team architecture (kkirikkiri + pumasi).

## What's included

- **9 agents** (4 kkirikkiri + 5 pumasi)
- **19 shared skills** across 5 functional categories
- **Foundation**: 6 OpenCrab packs + 5 external authorities
- **System-unique additions**: series-closer, copy-tone-check, workflow-curator, clip-segmentation

## Highlights

### ⭐ clip-segmentation (v0.6 critical)
Solves Seedance 2.0's 4-15 second HARD LIMIT for any video longer than 15 seconds. 4 segmentation patterns automatically detect when and how to split.

### 🛡 4-Part guardrail
Korean advertising law + AI rights (OpenAI/SAG-AFTRA/MPA/Vimeo) + visual + 23-item AI checklist.

### 📦 Knowledge transparency
Every skill marks its provenance: 📦 OpenCrab pack, 🛡 external authority, or ⚙ system-unique.

## Installation

See [INSTALL.md](INSTALL.md). Quick install for Claude Code:

\`\`\`bash
git clone https://github.com/contentscoin/video-production-skills.git
cd video-production-skills
./install.sh
\`\`\`

For Claude.ai, download individual `.zip` files from this release and upload via Customize → Skills.

## Foundation

Built on 율파파 Notion guides + movie_seedance_pack expert ontology + AI rights synthesis. Licensed Apache 2.0.
```

## After publishing

### Update README badges

Edit `README.md` to replace `<your-fork>` placeholders with your actual GitHub username:

```bash
# Find and replace
sed -i 's|<your-fork>|contentscoin|g' README.md
git add README.md
git commit -m "Update repo links"
git push
```

### Add topics for discoverability

On GitHub repo page → ⚙ icon next to "About" → add topics:
- `claude`
- `claude-skills`
- `ai-video`
- `seedance`
- `video-production`
- `prompt-engineering`
- `anthropic`

### Enable GitHub Pages (optional, for docs/)

Settings → Pages → Source: Deploy from branch → `main` / `docs`

```

### Submit to Claude Skills directory (optional)

If Anthropic establishes a community skills directory, submit a PR there with a link to this repo.

### Share

- Post on r/ClaudeAI subreddit
- LinkedIn post explaining the dual-team architecture
- Discord communities (Anthropic, AI filmmaking)

## Maintaining the repo

### When you update skills

```bash
# After editing skills in source
python3 scripts/convert_skills.py /path/to/legacy/skills  # only when converting legacy sources
python3 scripts/validate.py          # verify spec compliance
./scripts/package.sh                 # rebuild .zip files

git add .
git commit -m "feat: improve mood-curator description"
git push
```

### Creating new releases

```bash
git tag v0.6.1 -m "v0.6.1 - improved descriptions"
git push origin v0.6.1
# → GitHub Actions auto-packages and attaches .zip to release
```

## You're done

Your skills are now public. Anyone can:
- `git clone https://github.com/contentscoin/video-production-skills.git`
- Run `./install.sh` for Claude Code
- Download individual .zip from Releases for Claude.ai

📦 Welcome to the open source AI video production community.
