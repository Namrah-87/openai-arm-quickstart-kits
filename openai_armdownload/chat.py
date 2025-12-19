from .client import get_client

def simple_chat(message: str, model: str = "gpt-4o-mini"):
    client = get_client()
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a concise, helpful assistant."},
            {"role": "user", "content": message},
        ],
    )
    return response.choices[0].message.content


def streaming_chat(message: str, model: str = "gpt-4o-mini"):
    client = get_client()
    stream = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a concise, helpful assistant."},
            {"role": "user", "content": message},
        ],
        stream=True,
    )
    for chunk in stream:
        delta = chunk.choices[0].delta
        if delta.content:
            yield delta.content

