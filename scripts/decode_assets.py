#!/usr/bin/env python3
from pathlib import Path
import base64, sys

root = Path(__file__).resolve().parent.parent
src = root / "assets" / "b64"
if not src.exists():
    sys.exit("assets/b64 introuvable")
n = 0
for p in sorted(src.rglob("*.b64")):
    rel = p.relative_to(src)
    dest = root / "assets" / rel.as_posix()[:-4]  # strip .b64
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(base64.b64decode("".join(p.read_text().split())))
    n += 1
    print(f"decoded {dest.relative_to(root)} ({dest.stat().st_size} bytes)")
print(f"{n} fichiers écrits")
