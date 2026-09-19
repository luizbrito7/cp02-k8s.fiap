#!/usr/bin/env python3
import re
import subprocess
import sys
from pathlib import Path

import markdown
from pygments.formatters import HtmlFormatter

ASSETS = Path(__file__).resolve().parent
ICON = ASSETS.parent / "material/docs/icon.png"
CSS = (ASSETS / "03-style.css").read_text()
FONTS = "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;700&display=swap"

src = Path(sys.argv[1]).resolve()
out = Path(sys.argv[2]).resolve()

text = re.sub(
    r"^\{\{(.+)\}\}$",
    lambda m: (src.parent / m[1]).read_text().rstrip(),
    src.read_text(),
    flags=re.M,
)
body = markdown.markdown(
    text,
    extensions=["fenced_code", "codehilite", "tables"],
    extension_configs={"codehilite": {"guess_lang": False}},
)
body = re.sub(
    r'<div class="codehilite">(.*?)</div>',
    lambda m: f'<div class="codehilite{" keep" if m[1].count(chr(10)) <= 38 else ""}">{m[1]}</div>',
    body,
    flags=re.S,
)
syntax = HtmlFormatter(style="monokai").get_style_defs(".codehilite")

html = f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<base href="file://{src.parent}/">
<link rel="stylesheet" href="{FONTS}">
<style>{syntax}{CSS}</style></head><body>
<header class="brand"><img src="file://{ICON}"><strong>Luiz Brito</strong><span>CP1 · Cloud Native Development</span></header>
<main>{body}</main>
</body></html>"""

page = out.with_suffix(".html")
page.write_text(html)
subprocess.run(
    [
        "google-chrome", "--headless", "--no-sandbox", "--disable-gpu",
        "--no-pdf-header-footer", "--virtual-time-budget=15000",
        f"--print-to-pdf={out}", f"file://{page}",
    ],
    check=True,
    capture_output=True,
)
page.unlink()
