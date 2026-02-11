import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN topilmadi. .env ichini tekshiring.")
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY topilmadi. .env ichini tekshiring.")
