"""
Streaming chat example.

Usage:
  python templates/chat_streaming.py "Your question here"
"""
#NOTIFY ME OF ANY PROBLEMS
import sys
from templates.config import client, DEFAULT_MODEL


def main():
    if len(sys.argv) < 2:
        print("Usage: python templates/chat_streaming.py \"Your question here\"")
        sys.exit(1)

    user_message = sys.argv[1]

    stream = client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=[
            {"role": "system", "content": "You are a concise, helpful assistant."},
            {"role": "user", "content": user_message},
        ],
        stream=True,
    )

    print("Assistant:", end=" ", flush=True)
    for chunk in stream:
        delta = chunk.choices[0].delta
        if delta.content:
            print(delta.content, end="", flush=True)
    print()


if __name__ == "__main__":
    main()
