#!/usr/bin/env python3
"""Build a small WorkBuddy ZIP from the maintained Codex skill sources."""

import hashlib
import json
from pathlib import Path
import re
import zipfile


ROOT = Path(__file__).resolve().parents[1]
NAME = "shengcai-positioning-interview"
FILES = ("SKILL.md",) + tuple(
    str(path.relative_to(ROOT)) for path in sorted((ROOT / "references").rglob("*.md"))
)


def build():
    payloads = {name: (ROOT / name).read_bytes() for name in FILES}
    source = payloads["SKILL.md"].decode("utf-8")
    parts = source.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError("SKILL.md must start with YAML frontmatter")
    header, body = parts[1].strip(), parts[2].lstrip("\n")
    name = re.search(r"^name:\s*(\S+)\s*$", header, re.MULTILINE)
    description = re.search(r"^description:\s*(.+)$", header, re.MULTILINE)
    if not name or name.group(1) != NAME or not description:
        raise ValueError("Unexpected skill name or missing single-line description")
    extra = [
        'display_name: "航海定位官"',
        "description_zh: " + description.group(1),
        'description_en: "Use verified creator profiles and cases to choose an AI content focus through stepwise questions."',
        'version: "0.3.1"',
        'author: "七天假"',
    ]
    payloads["SKILL.md"] = (
        "---\n" + header + "\n" + "\n".join(extra) + "\n---\n\n" + body
    ).encode("utf-8")

    output = ROOT / "dist" / (NAME + "-workbuddy.zip")
    output.parent.mkdir(exist_ok=True)
    temporary = output.with_suffix(".zip.tmp")
    with zipfile.ZipFile(temporary, "w") as archive:
        for relative, content in payloads.items():
            info = zipfile.ZipInfo(NAME + "/" + relative, (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
    temporary.replace(output)
    print(json.dumps({
        "package": str(output.relative_to(ROOT)),
        "files": len(payloads),
        "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
    }, ensure_ascii=False))


if __name__ == "__main__":
    build()
