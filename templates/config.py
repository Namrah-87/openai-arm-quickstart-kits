import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not set in environment or .env file")

client = OpenAI(api_key=api_key)

# Central place to change models
DEFAULT_MODEL = "gpt-4o-mini"
