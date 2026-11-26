#!/usr/bin/env python3
"""Validate both SKILL.md files and every supporting file they reference.

Stdlib only (no yaml dependency) so it runs on any fresh clone. Checks the
frontmatter (name, <=60-char description ending in a period, version/author/
license/platforms present) and that every references/, templates/ and scripts/
path named in a SKILL.md body actually exists on disk.

Usage: python3 scripts/validate.py
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ["seo-blog-website-development", "seo-article-planning-schedule"]
errors = []


def field(fm: str, key: str):
    m = re.search(rf"^{key}:\s*(.+?)\s*$", fm, re.M)
    return m.group(1) if m else None


for name in SKILLS:
    md = ROOT / name / "SKILL.md"
    if not md.exists():
        errors.append(f"{name}/SKILL.md missing")
        continue
    content = md.read_text()
    if not content.startswith("---"):
        errors.append(f"{name}: frontmatter not at byte 0")
        continue
    m = re.search(r"\n---\s*\n", content[3:])
    if not m:
        errors.append(f"{name}: unclosed frontmatter")
        continue
    fm = content[3 : m.start() + 3]

    if field(fm, "name") != name:
        errors.append(f"{name}: frontmatter name mismatch")
    desc = (field(fm, "description") or "").strip().strip('"')
    if not (0 < len(desc) <= 60) or not desc.endswith("."):
        errors.append(f"{name}: description {len(desc)} chars or no trailing period")
    for f in ("version", "author", "license", "platforms"):
        if not field(fm, f):
            errors.append(f"{name}: missing frontmatter field {f}")

    for r in re.findall(r"`(references|templates|scripts)/[^`]+`", content):
        if not (ROOT / name / r).exists():
            errors.append(f"{name}: dangling {r}")

if errors:
    print("FAIL:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print("PASS: both skills valid, all referenced files exist")
