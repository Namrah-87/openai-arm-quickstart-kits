# cli/main.py

import sys

from openai_arm.chat import simple_chat, streaming_chat
from openai_arm.audio import transcribe, text_to_speech
from openai_arm.profile_loader import load_profile

from cli.setup import run_setup
from cli.doctor import run_doctor
from cli.benchmark import run_benchmark
from cli.update import run_update
from cli.record import run_record
from cli.play import run_play


USAGE = """
oaicli - OpenAI ARM Quickstart Kits CLI

Usage:
  oaicli chat "message"
  oaicli stream "message"
  oaicli transcribe <audio_file>
  oaicli speak "text" <output_audio_file>
  oaicli profile <profile_name|auto>

  oaicli setup
  oaicli doctor
  oaicli benchmark
  oaicli update
  oaicli record <output.wav> [duration_seconds]
  oaicli play <audio_file>
"""


def main():
    if len(sys.argv) < 2:
        print(USAGE)
        sys.exit(1)

    cmd = sys.argv[1]

    # Basic chat
    if cmd == "chat":
        if len(sys.argv) < 3:
            print("Usage: oaicli chat \"message\"")
            sys.exit(1)
        message = " ".join(sys.argv[2:])
        response = simple_chat(message)
        print(response)
        return

    # Streaming chat
    if cmd == "stream":
        if len(sys.argv) < 3:
            print("Usage: oaicli stream \"message\"")
            sys.exit(1)
        message = " ".join(sys.argv[2:])
        for chunk in streaming_chat(message):
            print(chunk, end="", flush=True)
        print()
        return

    # Speech-to-text
    if cmd == "transcribe":
        if len(sys.argv) < 3:
            print("Usage: oaicli transcribe <audio_file>")
            sys.exit(1)
        audio_file = sys.argv[2]
        text = transcribe(audio_file)
        print(text)
        return

    # Text-to-speech
    if cmd == "speak":
        if len(sys.argv) < 4:
            print("Usage: oaicli speak \"text\" <output_audio_file>")
            sys.exit(1)
        text = sys.argv[2]
        output_file = sys.argv[3]
        text_to_speech(text, output_file)
        print(f"Saved to {output_file}")
        return

    # Profiles
    if cmd == "profile":
        if len(sys.argv) < 3:
            print("Usage: oaicli profile <profile_name|auto>")
            sys.exit(1)
        profile_name = sys.argv[2]
        if profile_name == "auto":
            board, profile = load_profile("auto", return_detected=True)
            print(f"Detected board: {board}")
            print(f"Profile: {profile}")
        else:
            profile = load_profile(profile_name)
            print(profile)
        return

    # Setup wizard
    if cmd == "setup":
        run_setup()
        return

    # Diagnostics
    if cmd == "doctor":
        run_doctor()
        return

    # Benchmarks
    if cmd == "benchmark":
        run_benchmark()
        return

    # Update repo + deps
    if cmd == "update":
        run_update()
        return

    # Record audio
    if cmd == "record":
        if len(sys.argv) < 3:
            print("Usage: oaicli record <output.wav> [duration_seconds]")
            sys.exit(1)
        filename = sys.argv[2]
        duration = 5
        if len(sys.argv) >= 4:
            try:
                duration = int(sys.argv[3])
            except ValueError:
                print("Invalid duration, using default 5 seconds.")
        run_record(filename=filename, duration=duration)
        return

    # Play audio
    if cmd == "play":
        if len(sys.argv) < 3:
            print("Usage: oaicli play <audio_file>")
            sys.exit(1)
        filename = sys.argv[2]
        run_play(filename)
        return

    # Unknown command
    print(f"Unknown command: {cmd}")
    print(USAGE)
    sys.exit(1)


if __name__ == "__main__":
    main()
