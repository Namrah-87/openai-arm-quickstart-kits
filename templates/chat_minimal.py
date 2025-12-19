"""
Minimal text chat example.

Usage:
  python templates/chat_minimal.py "Your question here"
"""

import sys
from templates.config import client, DEFAULT_MODEL


def main():
    if len(sys.argv) < 2:
        print("Usage: python templates/chat_minimal.py \"Your question here\"")
        sys.exit(1)

    user_message = sys.argv[1]

    response = client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=[
            {"role": "system", "content": "You are a concise, helpful assistant."},
            {"role": "user", "content": user_message},
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
