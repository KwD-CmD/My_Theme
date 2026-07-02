#!/usr/bin/env python3

import shutil
from pathlib import Path

home = Path.home()
termux = home / ".termux"
termux.mkdir(exist_ok=True)

colors = """background=#0D1117
foreground=#C9D1D9
cursor=#58A6FF
color0=#161B22
color1=#FF7B72
color2=#3FB950
color3=#D29922
color4=#58A6FF
color5=#BC8CFF
color6=#39C5CF
color7=#C9D1D9
color8=#484F58
color9=#FFA198
color10=#56D364
color11=#E3B341
color12=#79C0FF
color13=#D2A8FF
color14=#56D4DD
color15=#F0F6FC
"""

(termux / "colors.properties").write_text(
    colors,
    encoding="utf-8"
)

banner = r'''
# KIAN_THEME

echo ""
echo "██╗  ██╗██╗ █████╗ ███╗   ██╗"
echo "██║ ██╔╝██║██╔══██╗████╗  ██║"
echo "█████╔╝ ██║███████║██╔██╗ ██║"
echo "██╔═██╗ ██║██╔══██║██║╚██╗██║"
echo "██║  ██╗██║██║  ██║██║ ╚████║"
echo "╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝"
echo ""

PS1="\[\e[1;34m\]>>>\[\e[0m\] "
'''

for shell in (".bashrc", ".zshrc"):
    rc = home / shell

    if rc.exists():
        text = rc.read_text(encoding="utf-8")
    else:
        text = ""

    if "# KIAN_THEME" not in text:
        with rc.open("a", encoding="utf-8") as f:
            f.write("\n")
            f.write(banner)
            f.write("\n")

reload_cmd = shutil.which("termux-reload-settings")

if reload_cmd:
    import subprocess
    subprocess.run([reload_cmd],
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)

print("Theme installed successfully.")
