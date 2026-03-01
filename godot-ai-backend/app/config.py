import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LOCAL_AUTH_TOKEN = os.getenv("LOCAL_AUTH_TOKEN")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

if not OPENAI_API_KEY:
    raise RuntimeError("Falta OPENAI_API_KEY en .env")
if not LOCAL_AUTH_TOKEN:
    raise RuntimeError("Falta LOCAL_AUTH_TOKEN en .env")
