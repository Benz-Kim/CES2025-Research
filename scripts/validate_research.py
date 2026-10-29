#!/usr/bin/env python3
"""Validate local document targets and source IDs without network access."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
register = (ROOT / "sources/REGISTER.md").read_text(encoding="utf-8")
known = set(re.findall(r"^\| ((?:S|D)\d{2}) \|", register, re.M))
errors = []
checked = 0
for path in sorted(ROOT.rglob("*.md")):
    if ".git" in path.parts:
        continue
    text = path.read_text(encoding="utf-8")
    checked += 1
    for source_id in set(re.findall(r"\b[SD]\d{2}\b", text)):
        if source_id not in known:
            errors.append(f"{path.relative_to(ROOT)}: unknown source {source_id}")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
            continue
        target = target.split("#", 1)[0]
        resolved = (path.parent / target).resolve()
        if not resolved.is_relative_to(ROOT) or not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: missing local target {target}")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"PASS: {checked} Markdown files; {len(known)} registered source IDs; local targets resolve.")
