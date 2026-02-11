from aiogram import Router, types

from src.storage import repo
from src.services.llm import build_messages, ask_llm

router = Router()

@router.message()
async def chat_handler(message: types.Message):
    text = (message.text or "").strip()
    if not text:
        return

    user_id = message.from_user.id
    mode = await repo.get_mode(user_id)

    history = await repo.get_history(user_id)
    messages = build_messages(mode, history, text)

    try:
        answer = ask_llm(messages)
    except Exception:
        await message.answer("⚠️ AI xatolik berdi. Keyinroq urinib ko‘ring.")
        return

    # history saqlash
    await repo.add_message(user_id, "user", text)
    await repo.add_message(user_id, "assistant", answer)

    await message.answer(answer)
