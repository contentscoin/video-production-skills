#!/usr/bin/env bash
#
# Video Production System v0.6 — Claude Code installer
#
# Copies the 28 skills to ~/.claude/skills/ so Claude Code can use them.
# Usage:
#   ./install.sh                          # install all
#   ./install.sh --only mood-curator,editor
#   ./install.sh --dry-run                # show what would happen
#   ./install.sh --uninstall              # remove all VPS skills
#

set -euo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SOURCE_DIR="$SCRIPT_DIR/skills"
TARGET_DIR="${HOME}/.claude/skills"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
BRASS='\033[38;5;179m'
DIM='\033[2m'
RESET='\033[0m'

# All 28 skill names
ALL_SKILLS=(
  # kkirikkiri agents
  "mood-curator" "reference-scout" "aesthetic-director" "narrative-weaver"
  # pumasi agents
  "script-writer" "shot-designer" "prompt-engineer" "motion-director" "editor"
  # v0.1 foundation
  "intake-router" "cinematic-shot" "facs-expression" "seedance-prompt" "mv-builder"
  # v0.2 series
  "character-pool" "series-variation" "post-production-spec" "guardrail-check"
  # v0.3 blueprint
  "visual-bible" "image-prompt-foundations" "model-adapter" "qa-review" "production-brief"
  # v0.4 operational
  "series-closer" "copy-tone-check"
  # v0.5 rights & meta
  "music-rights-check" "workflow-curator"
  # v0.6 clip
  "clip-segmentation"
)

DRY_RUN=false
UNINSTALL=false
SELECTED_SKILLS=""

# Parse args
while [[ $# -gt 0 ]]; do
  case "$1" in
    --only)
      SELECTED_SKILLS="$2"
      shift 2
      ;;
    --dry-run)
      DRY_RUN=true
      shift
      ;;
    --uninstall)
      UNINSTALL=true
      shift
      ;;
    --help|-h)
      echo "Video Production System v0.6 — Installer"
      echo ""
      echo "Usage:"
      echo "  ./install.sh                          # install all 28 skills"
      echo "  ./install.sh --only NAME,NAME         # install specific skills"
      echo "  ./install.sh --dry-run                # preview without making changes"
      echo "  ./install.sh --uninstall              # remove all VPS skills"
      echo ""
      echo "Target: ~/.claude/skills/"
      exit 0
      ;;
    *)
      echo -e "${RED}Unknown option: $1${RESET}"
      exit 1
      ;;
  esac
done

echo -e "${BRASS}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
echo -e "${BRASS}  Video Production System v0.6 — Skill Installer${RESET}"
echo -e "${BRASS}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
echo ""

# Sanity check
if [[ ! -d "$SOURCE_DIR" ]]; then
  echo -e "${RED}✗ Source directory not found: $SOURCE_DIR${RESET}"
  echo "  Run this script from the repository root."
  exit 1
fi

# Determine which skills to act on
SKILLS_TO_INSTALL=()
if [[ -n "$SELECTED_SKILLS" ]]; then
  IFS=',' read -ra SKILLS_TO_INSTALL <<< "$SELECTED_SKILLS"
else
  SKILLS_TO_INSTALL=("${ALL_SKILLS[@]}")
fi

# UNINSTALL mode
if [[ "$UNINSTALL" == true ]]; then
  echo -e "${YELLOW}Uninstalling ${#SKILLS_TO_INSTALL[@]} skill(s) from $TARGET_DIR${RESET}"
  echo ""
  removed=0
  for skill in "${SKILLS_TO_INSTALL[@]}"; do
    skill_path="$TARGET_DIR/$skill"
    if [[ -d "$skill_path" ]]; then
      if [[ "$DRY_RUN" == true ]]; then
        echo -e "  ${DIM}[dry-run]${RESET} would remove $skill_path"
      else
        rm -rf "$skill_path"
        echo -e "  ${GREEN}✓${RESET} removed $skill"
      fi
      removed=$((removed + 1))
    else
      echo -e "  ${DIM}~ $skill not installed, skipping${RESET}"
    fi
  done
  echo ""
  echo -e "${GREEN}Uninstall complete. Removed $removed skill(s).${RESET}"
  exit 0
fi

# Find skill in source tree
find_skill_source() {
  local name="$1"
  for path in \
    "$SOURCE_DIR/agents/kkirikkiri/$name" \
    "$SOURCE_DIR/agents/pumasi/$name" \
    "$SOURCE_DIR/shared/$name"; do
    if [[ -d "$path" ]]; then
      echo "$path"
      return 0
    fi
  done
  return 1
}

# Create target directory
if [[ "$DRY_RUN" == false ]]; then
  mkdir -p "$TARGET_DIR"
fi

echo -e "Installing ${#SKILLS_TO_INSTALL[@]} skill(s) to ${BLUE}$TARGET_DIR${RESET}"
if [[ "$DRY_RUN" == true ]]; then
  echo -e "${YELLOW}(DRY RUN — no changes will be made)${RESET}"
fi
echo ""

installed=0
skipped=0
errors=0

for skill in "${SKILLS_TO_INSTALL[@]}"; do
  src=$(find_skill_source "$skill") || src=""
  if [[ -z "$src" ]]; then
    echo -e "  ${RED}✗${RESET} $skill ${DIM}(not found in source)${RESET}"
    errors=$((errors + 1))
    continue
  fi

  dst="$TARGET_DIR/$skill"

  if [[ -d "$dst" ]]; then
    if [[ "$DRY_RUN" == true ]]; then
      echo -e "  ${YELLOW}↻${RESET} $skill ${DIM}(would overwrite existing)${RESET}"
    else
      rm -rf "$dst"
    fi
  fi

  if [[ "$DRY_RUN" == true ]]; then
    echo -e "  ${BRASS}→${RESET} $skill ${DIM}(would copy from ${src##*/skills/})${RESET}"
  else
    cp -r "$src" "$dst"
    echo -e "  ${GREEN}✓${RESET} $skill"
  fi
  installed=$((installed + 1))
done

echo ""
echo -e "${BRASS}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"

if [[ "$DRY_RUN" == true ]]; then
  echo -e "${YELLOW}Dry run complete. Would install $installed skill(s).${RESET}"
  echo -e "${DIM}Run without --dry-run to actually install.${RESET}"
else
  echo -e "${GREEN}✓ Installed $installed skill(s).${RESET}"
  if [[ $errors -gt 0 ]]; then
    echo -e "${RED}✗ $errors error(s).${RESET}"
  fi
  echo ""
  echo -e "Skills available at: ${BLUE}$TARGET_DIR${RESET}"
  echo ""
  echo -e "${DIM}Verify with:${RESET}"
  echo -e "  ${DIM}ls $TARGET_DIR${RESET}"
  echo ""
  echo -e "${DIM}In Claude Code, the skills now activate automatically when relevant.${RESET}"
  echo -e "${DIM}Type / to see them as slash commands, or just describe your task.${RESET}"
fi
echo -e "${BRASS}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
