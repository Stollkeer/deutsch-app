"""Wrap conjugations JSON into JS globals so index.html can load them via <script>."""
from pathlib import Path
import json

ROOT = Path(__file__).parent
DATA = ROOT / "data"

for lang, var in [("de", "CONJUGATIONS_DE"), ("fr", "CONJUGATIONS_FR")]:
    src = DATA / f"conjugations-{lang}.json"
    dst = ROOT / f"conjugations-{lang}.js"
    d = json.loads(src.read_text(encoding="utf-8"))
    body = f"/* Auto-generated from {src.name}. {len(d)} verbs. */\n"
    body += f"window.{var} = " + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + ";\n"
    dst.write_text(body, encoding="utf-8")
    print(f"wrote {dst.name} ({len(d)} verbs, {len(body)} chars)")
