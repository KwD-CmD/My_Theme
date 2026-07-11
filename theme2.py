import os
import sys
import time
import random
import shutil
import platform
import socket
import datetime

# =========================================
# CONFIGURATION
# =========================================
class CyberConfig:
    USER = "KWD"
    HOST = "cyber"
    COLORS = {
        "neon_green": "\033[92m",
        "bright_red": "\033[91m",
        "white": "\033[97m",
        "reset": "\033[0m"
    }
    BANNER = r"""
███████╗███████╗ ██████╗██╗   ██╗██████╗ ██╗████████╗██╗   ██╗
██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██║╚══██╔══╝╚██╗ ██╔╝
███████╗█████╗  ██║     ██║   ██║██████╔╝██║   ██║    ╚████╔╝
╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗██║   ██║     ╚██╔╝
███████║███████╗╚██████╗╚██████╔╝██║  ██║██║   ██║      ██║
╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝
"""

# =========================================
# SYSTEM CORE
# =========================================
class TerminalEngine:
    @staticmethod
    def clear():
        sys.stdout.write("\033[2J\033[H")

class Animations:
    @staticmethod
    def loading_bar(text="SYSTEM"):
        for i in range(21):
            bar = "█" * i + "-" * (20 - i)
            sys.stdout.write(f"\r{CyberConfig.COLORS['neon_green']}[{bar}] {text} {i*5}%")
            sys.stdout.flush()
            time.sleep(0.03)
        print()

class Dashboard:
    @staticmethod
    def show():
        stats = {
            "USER": CyberConfig.USER,
            "OS": platform.system(),
            "PYTHON": platform.python_version(),
            "IP": socket.gethostbyname(socket.gethostname())
        }
        print(f"\n{CyberConfig.COLORS['neon_green']}┌── SYSTEM DASHBOARD ──┐")
        for k, v in stats.items():
            print(f"│ {CyberConfig.COLORS['white']}{k:7}: {CyberConfig.COLORS['neon_green']}{v}")
        print(f"{CyberConfig.COLORS['neon_green']}└──────────────────────┘\n")

# =========================================
# MAIN SHELL
# =========================================
class CyberShell:
    def __init__(self):
        TerminalEngine.clear()
        # نمایش بنر به محض اجرا
        print(f"{CyberConfig.COLORS['neon_green']}{CyberConfig.BANNER}")
        print(f"{CyberConfig.COLORS['bright_red']}  Welcome back, {CyberConfig.USER} | Hacker Mode Activated")
        Animations.loading_bar("BOOTING")
        self.active = True

    def run(self):
        while self.active:
            try:
                cmd = input(f"{CyberConfig.COLORS['neon_green']}┌──({CyberConfig.USER}㉿{CyberConfig.HOST})-[~]\n└─>>> {CyberConfig.COLORS['reset']}").lower().strip()

                if not cmd: continue
                if cmd == "exit": self.active = False
                elif cmd == "clear": TerminalEngine.clear()
                elif cmd == "dashboard": Dashboard.show()
                elif cmd == "help": print("Commands: clear, dashboard, exit, [system cmd]")
                else: os.system(cmd)
            except KeyboardInterrupt:
                print("\nUse 'exit' to quit.")

if __name__ == "__main__":
    app = CyberShell()
    app.run()
