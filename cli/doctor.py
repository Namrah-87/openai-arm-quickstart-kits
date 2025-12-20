# cli/doctor.py

import platform
import shutil
from openai_arm.client import test_api_key
from openai_arm.profile_loader import load_profile

def run_doctor():
    print("\n=== oaicli doctor ===")

    print(f"Python: {platform.python_version()}")
    print(f"Pip: {shutil.which('pip')}")
    print(f"API key valid: {test_api_key()}")

    board, profile = load_profile("auto", return_detected=True)
    print(f"Detected board: {board}")
    print(f"Profile: {profile}")

    print("\nDoctor check complete.")
