#!/usr/bin/env bash
#
# Package all 28 skills as .zip files for Claude.ai upload
#
# Each .zip contains the skill folder as root, with SKILL.md inside.
# This matches the Claude Skills v1 spec for Claude.ai uploads.
#
# Output: dist/<skill-name>.zip × 28
#

set -euo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_DIR="$( cd "$SCRIPT_DIR/.." && pwd )"
SKILLS_DIR="$REPO_DIR/skills"
DIST_DIR="$REPO_DIR/dist"

PYTHON_BIN="${PYTHON_BIN:-}"
if [[ -z "$PYTHON_BIN" ]]; then
  if command -v python3 > /dev/null 2>&1; then
    PYTHON_BIN="python3"
  elif command -v python > /dev/null 2>&1; then
    PYTHON_BIN="python"
  else
    echo "Python 3 is required to package skills."
    exit 1
  fi
fi

GREEN='\033[0;32m'
BRASS='\033[38;5;179m'
DIM='\033[2m'
RESET='\033[0m'

echo -e "${BRASS}Packaging skills for Claude.ai upload...${RESET}"
echo ""

# Clean dist
rm -rf "$DIST_DIR"
mkdir -p "$DIST_DIR"

count=0
# Find every skill folder (each contains a SKILL.md at its root)
while IFS= read -r skill_md; do
  skill_dir="$(dirname "$skill_md")"
  skill_name="$(basename "$skill_dir")"
  
  # Skip if SKILL.md is not at the immediate root of the folder
  # (we want the folder itself to be the skill)
  
  # Create zip with the skill folder as root
  "$PYTHON_BIN" - "$skill_dir" "$skill_name" "$DIST_DIR/$skill_name.zip" <<'PY'
import sys
import zipfile
from pathlib import Path

skill_dir = Path(sys.argv[1])
skill_name = sys.argv[2]
zip_path = Path(sys.argv[3])

with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(skill_dir.rglob("*")):
        if not path.is_file() or path.name == ".DS_Store":
            continue
        archive.write(path, Path(skill_name) / path.relative_to(skill_dir))
PY
  
  size=$("$PYTHON_BIN" - "$DIST_DIR/$skill_name.zip" <<'PY'
import sys
from pathlib import Path

print((Path(sys.argv[1]).stat().st_size + 1023) // 1024)
PY
)
  echo -e "  ${GREEN}✓${RESET} $skill_name ${DIM}(${size}KB)${RESET}"
  count=$((count + 1))
done < <(find "$SKILLS_DIR" -name "SKILL.md" -type f | sort)

echo ""
echo -e "${GREEN}Packaged $count skill(s) to:${RESET} $DIST_DIR"
echo ""
echo -e "${DIM}Upload to Claude.ai:${RESET}"
echo -e "${DIM}  1. Settings → Capabilities → Code execution: ON${RESET}"
echo -e "${DIM}  2. Customize → Skills → Upload${RESET}"
echo -e "${DIM}  3. Select one or more .zip files from $DIST_DIR${RESET}"
