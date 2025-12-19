#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

PROFILE_MAP = {
    "Orange Pi Zero 3": "orange_pi_zero_series",
    "Orange Pi Zero3": "orange_pi_zero_series",
    "Orange Pi 3": "orange_pi_3_series",
    "Radxa Zero 3W": "radxa_zero3_series",
    "Radxa Zero 3E": "radxa_zero3_series",
    "Raspberry Pi 4": "raspberry_pi_4_series",
    "Raspberry Pi 5": "raspberry_pi_5_series",
    "Khadas VIM": "khadas_vim_series",
}

def detect_board():
    paths = [
        "/proc/device-tree/model",
        "/proc/cpuinfo",
        "/etc/os-release"
    ]

    text = ""
    for p in paths:
        if os.path.exists(p):
            try:
                text += Path(p).read_text(errors="ignore")
            except:
                pass

    for key, profile in PROFILE_MAP.items():
        if key.lower() in text.lower():
            return key, profile

    return "Unknown ARM Board", "generic_arm"


def run_cmd(cmd):
    print(f"\n[RUN] {cmd}")
    subprocess.run(cmd, shell=True, check=False)


def install_system_packages(profile):
    print("\nInstalling system packages...")

    run_cmd("sudo apt update")
    run_cmd("sudo apt install -y python3-dev python3-pip portaudio19-dev")

    if "orange_pi" in profile:
        print("Note: Orange Pi audio works best with USB microphones.")
    elif "raspberry_pi_5" in profile:
        print("Note: Raspberry Pi 5 performs best with NVMe storage.")


def install_python_packages():
    print("\nInstalling Python dependencies...")
    run_cmd("pip install --upgrade pip")
    run_cmd("pip install openai python-dotenv")


def main():
    print("\n=== OpenAI ARM Quickstart Kits Installer ===")

    board_name, profile = detect_board()
    print(f"\nDetected board: {board_name}")
    print(f"Using profile: {profile}")

    choice = input("\nProceed with recommended installation? (y/n): ").strip().lower()
    if choice != "y":
        print("\nInstallation cancelled.")
        return

    install_system_packages(profile)
    install_python_packages()

    print("\n✅ Installation complete!")
    print(f"✅ Loaded profile: {profile}")
    print("\nNext steps:")
    print("1. Clone the repo: git clone https://github.com/<YOUR-USERNAME>/<YOUR-REPO>")
    print("2. Create a .env file with your OpenAI API key.")
    print("3. Try running:  oaicli chat \"hello\"")
    print("\nYou're ready to build AI on ARM hardware!")


if __name__ == "__main__":
    main()
