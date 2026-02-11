from openai import OpenAI
from src.config import GROQ_API_KEY

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

SYSTEM_PROMPTS = {
    "chat": "You are a helpful assistant.",
    "grammar": "You are an English grammar corrector. Only correct grammar and spelling. Keep meaning the same.",
    "summarize": "You summarize the user's text clearly and briefly.",
    "translate": "You translate between Uzbek and English. Preserve meaning.",
}

def build_messages(mode: str, history: list[dict], user_text: str) -> list[dict]:
    system = SYSTEM_PROMPTS.get(mode, SYSTEM_PROMPTS["chat"])
    msgs = [{"role": "system", "content": system}]
    msgs.extend(history)
    msgs.append({"role": "user", "content": user_text})
    return msgs 

def ask_llm(messages: list[dict]) -> str:
    resp = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=messages,
    temperature=0.4,
    max_tokens=350,
    )

    return resp.choices[0].message.content
