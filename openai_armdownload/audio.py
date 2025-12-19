from pathlib import Path
from .client import get_client

def transcribe(audio_path: str, model="gpt-4o-mini-transcribe"):
    client = get_client()
    audio_file = Path(audio_path)
    if not audio_file.exists():
        raise FileNotFoundError(audio_path)

    with audio_file.open("rb") as f:
        result = client.audio.transcriptions.create(
            model=model,
            file=f,
        )
    return result.text


def text_to_speech(text: str, out_path: str, model="gpt-4o-mini-tts"):
    client = get_client()
    out_file = Path(out_path)

    result = client.audio.speech.create(
        model=model,
        voice="alloy",
        input=text,
        format="mp3",
    )

    out_file.write_bytes(result)
    return str(out_file)

