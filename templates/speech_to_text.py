"""
Speech-to-text from an audio file.

Usage:
  python templates/speech_to_text.py path/to/audio.wav
"""

import sys
from pathlib import Path
from templates.config import client


def main():
    if len(sys.argv) < 2:
        print("Usage: python templates/speech_to_text.py path/to/audio.wav")
        sys.exit(1)

    audio_path = Path(sys.argv[1])
    if not audio_path.is_file():
        print(f"File not found: {audio_path}")
        sys.exit(1)

    with audio_path.open("rb") as f:
        transcription = client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=f,
        )

    print("Transcription:")
    print(transcription.text)


if __name__ == "__main__":
    main()
