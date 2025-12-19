import argparse
from openai_arm.chat import simple_chat, streaming_chat
from openai_arm.audio import transcribe, text_to_speech
from openai_arm.profile_loader import load_profile


def main():
    parser = argparse.ArgumentParser(prog="oaicli", description="OpenAI ARM Toolkit CLI")

    sub = parser.add_subparsers(dest="command")

    # Chat
    chat_cmd = sub.add_parser("chat", help="Send a simple chat message")
    chat_cmd.add_argument("message", type=str)

    # Streaming chat
    stream_cmd = sub.add_parser("stream", help="Stream a chat response")
    stream_cmd.add_argument("message", type=str)

    # Transcribe
    stt_cmd = sub.add_parser("transcribe", help="Transcribe an audio file")
    stt_cmd.add_argument("audio_path", type=str)

    # Text to speech
    tts_cmd = sub.add_parser("speak", help="Convert text to speech")
    tts_cmd.add_argument("text", type=str)
    tts_cmd.add_argument("out_path", type=str)

    # Profile
    prof_cmd = sub.add_parser("profile", help="Show hardware profile")
    prof_cmd.add_argument("name", type=str)

    args = parser.parse_args()

    if args.command == "chat":
        print(simple_chat(args.message))

    elif args.command == "stream":
        for chunk in streaming_chat(args.message):
            print(chunk, end="", flush=True)
        print()

    elif args.command == "transcribe":
        print(transcribe(args.audio_path))

    elif args.command == "speak":
        print(text_to_speech(args.text, args.out_path))

    elif args.command == "profile":
        profile = load_profile(args.name)
        print(profile)

    else:
        parser.print_help()
