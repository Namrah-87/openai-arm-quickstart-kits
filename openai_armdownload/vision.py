from pathlib import Path
from .client import get_client

def describe_image(image_path: str, model="gpt-4o-mini"):
    client = get_client()
    img = Path(image_path)
    if not img.exists():
        raise FileNotFoundError(image_path)

    with img.open("rb") as f:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Describe the image in detail."},
                {"role": "user", "content": [
                    {"type": "input_image", "image": f}
                ]}
            ]
        )
    return response.choices[0].message.content

