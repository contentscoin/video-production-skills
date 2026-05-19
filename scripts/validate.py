#!/usr/bin/env python3
"""
Validate all SKILL.md files in the repo conform to Claude Skills v1 spec.

Checks:
- YAML frontmatter exists
- 'name' field (matches folder name, max 64 chars, lowercase-hyphen)
- 'description' field (max 200 chars, non-empty)
- Folder structure (folder name == skill name)
- File name is 'SKILL.md' exactly (case-sensitive)
"""

import re
import sys
from pathlib import Path

# ANSI colors
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
DIM = "\033[2m"
RESET = "\033[0m"

NAME_PATTERN = re.compile(r"^[a-z][a-z0-9-]*$")


def safe_symbol(symbol: str, fallback: str) -> str:
    """Return a console-safe symbol for Windows legacy encodings."""
    encoding = sys.stdout.encoding or "utf-8"
    if "UTF" not in encoding.upper():
        return fallback
    try:
        symbol.encode(encoding)
        return symbol
    except UnicodeEncodeError:
        return fallback


OK = safe_symbol("✓", "[OK]")
FAIL = safe_symbol("✗", "[FAIL]")
ARROW = safe_symbol("└─", "->")
SEPARATOR = safe_symbol("─", "-")
DOT = safe_symbol("·", "-")


def parse_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter from SKILL.md."""
    if not content.startswith("---"):
        return {}
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    
    fm_text = parts[1].strip()
    result = {}
    current_key = None
    current_value_lines = []
    
    for line in fm_text.split("\n"):
        if ":" in line and not line.startswith(" "):
            if current_key:
                result[current_key] = " ".join(current_value_lines).strip()
            key, value = line.split(":", 1)
            current_key = key.strip()
            current_value_lines = [value.strip()]
        elif current_key:
            current_value_lines.append(line.strip())
    
    if current_key:
        result[current_key] = " ".join(current_value_lines).strip()
    
    return result


def validate_skill(skill_md_path: Path) -> tuple[bool, list[str]]:
    """Validate one SKILL.md file. Returns (passed, errors)."""
    errors = []
    
    # Check filename
    if skill_md_path.name != "SKILL.md":
        errors.append(f"Filename must be exactly 'SKILL.md', got '{skill_md_path.name}'")
    
    # Read content
    try:
        content = skill_md_path.read_text(encoding="utf-8")
    except Exception as e:
        errors.append(f"Cannot read file: {e}")
        return False, errors
    
    # Parse frontmatter
    fm = parse_frontmatter(content)
    if not fm:
        errors.append("Missing or invalid YAML frontmatter (must start with ---)")
        return False, errors
    
    # name field
    name = fm.get("name", "")
    if not name:
        errors.append("Missing 'name' field in frontmatter")
    elif len(name) > 64:
        errors.append(f"'name' too long: {len(name)} chars (max 64)")
    elif not NAME_PATTERN.match(name):
        errors.append(f"'name' invalid format: '{name}' (must be lowercase-hyphen)")
    else:
        # Check folder name matches
        folder_name = skill_md_path.parent.name
        if folder_name != name:
            errors.append(f"Folder name '{folder_name}' != skill name '{name}'")
    
    # description field
    description = fm.get("description", "")
    if not description:
        errors.append("Missing 'description' field in frontmatter")
    elif len(description) > 200:
        errors.append(f"'description' too long: {len(description)} chars (max 200)")
    elif len(description) < 30:
        errors.append(f"'description' too short: {len(description)} chars (need more detail to help Claude trigger correctly)")
    
    return len(errors) == 0, errors


def main():
    repo_root = Path(__file__).parent.parent
    skills_dir = repo_root / "skills"
    
    if not skills_dir.exists():
        print(f"{RED}✗ Skills directory not found: {skills_dir}{RESET}")
        sys.exit(1)
    
    skill_files = sorted(skills_dir.rglob("SKILL.md"))
    
    if not skill_files:
        print(f"{YELLOW}⚠ No SKILL.md files found in {skills_dir}{RESET}")
        sys.exit(1)
    
    print(f"Validating {len(skill_files)} skill(s)...\n")
    
    passed = 0
    failed = 0
    all_errors = []
    
    for skill_md in skill_files:
        rel_path = skill_md.relative_to(repo_root)
        ok, errors = validate_skill(skill_md)
        
        if ok:
            print(f"  {GREEN}{OK}{RESET} {rel_path}")
            passed += 1
        else:
            print(f"  {RED}{FAIL}{RESET} {rel_path}")
            for err in errors:
                print(f"      {RED}{ARROW}{RESET} {err}")
            failed += 1
            all_errors.append((rel_path, errors))
    
    print()
    print(f"{SEPARATOR * 60}")
    if failed == 0:
        print(f"{GREEN}{OK} All {passed} skill(s) valid.{RESET}")
        sys.exit(0)
    else:
        print(f"{GREEN}{OK} {passed} passed{RESET} {DOT} {RED}{FAIL} {failed} failed{RESET}")
        sys.exit(1)


if __name__ == "__main__":
    main()
