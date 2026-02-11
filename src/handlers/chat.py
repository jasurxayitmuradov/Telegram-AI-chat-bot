from aiogram import Router, types

from src.storage import repo
from src.services.llm import build_messages, ask_llm
import asyncio
from src.services.rate_limit import is_rate_limited
from src.services.logger import logger

router = Router()

@router.message()
async def chat_handler(message: types.Message):
    text = (message.text or "").strip()
    if not text:
        return

    user_id = message.from_user.id

    # 🔥 Rate limit
    if is_rate_limited(user_id):
        await message.answer("⏳ Juda tez yuboryapsiz. Iltimos, biroz sekinroq.")
        return

    mode = await repo.get_mode(user_id)
    history = await repo.get_history(user_id)

    messages = build_messages(mode, history, text)

    # 🔥 Typing indicator
    await message.chat.do("typing")

    try:
        answer = await asyncio.wait_for(
            asyncio.to_thread(ask_llm, messages),
            timeout=15
        )
    except asyncio.TimeoutError:
        logger.warning("Timeout for user_id=%s", user_id)
        await message.answer("⚠️ AI juda sekin javob berdi. Qayta urinib ko‘ring.")
        return
    except Exception as e:
        logger.exception("LLM error for user_id=%s: %s", user_id, e)
        await message.answer("⚠️ AI xatolik berdi. Keyinroq urinib ko‘ring.")
        return

    await repo.add_message(user_id, "user", text)
    await repo.add_message(user_id, "assistant", answer)

    await message.answer(answer)

