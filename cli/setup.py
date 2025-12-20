# cli/setup.py

import os
from openai_arm.profile_loader import load_profile
from openai_arm.client import test_api_key
from openai_arm.audio import detect_audio_devices

def run_setup():
    print("\n=== OpenAI ARM Setup ===")

    # Detect hardware profile
    board, profile = load_profile("auto", return_detected=True)
    print(f"Detected board: {board}")
    print(f"Using profile: {profile}")

    # Check API key
    if not test_api_key():
        print("No valid API key found. Create a .env file with OPENAI_API_KEY=...")
    else:
        print("API key OK.")

    # Detect audio devices
    mics, speakers = detect_audio_devices()
    print(f"Microphones: {mics}")
    print(f"Speakers: {speakers}")

    print("\nSetup complete.")
