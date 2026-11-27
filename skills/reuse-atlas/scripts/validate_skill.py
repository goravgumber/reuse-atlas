#!/usr/bin/env python3
"""Lightweight structural checks for the ReuseAtlas distribution."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / "skills" / "reuse-atlas" / "SKILL.md"
REQUIRED_HEADINGS = ("## Activation and scope", "## Workflow", "## Implementation gate")


def main() -> int:
    errors = []
    if not SKILL.is_file():
        errors.append(f"Missing {SKILL.relative_to(ROOT)}")
    else:
        content = SKILL.read_text(encoding="utf-8")
        if not content.startswith("---\n"):
            errors.append("SKILL.md must begin with YAML frontmatter")
        else:
            parts = content.split("---", 2)
            frontmatter = parts[1] if len(parts) == 3 else ""
            name = re.search(r"^name:\s*(\S+)\s*$", frontmatter, re.MULTILINE)
            description = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
            if not name or name.group(1) != "reuse-atlas":
                errors.append("Frontmatter name must be reuse-atlas")
            if not description or not 1 <= len(description.group(1)) <= 1024:
                errors.append("Frontmatter description must contain 1-1024 characters")
        for heading in REQUIRED_HEADINGS:
            if heading not in content:
                errors.append(f"Missing required section: {heading}")
    if errors:
        print("Structural validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("ReuseAtlas skill structure is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
