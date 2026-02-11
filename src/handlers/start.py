from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.storage import repo

router = Router()

def menu_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="💬 Chat", callback_data="mode:chat")
    kb.button(text="✅ Grammar", callback_data="mode:grammar")
    kb.button(text="🧾 Summarize", callback_data="mode:summarize")
    kb.button(text="🌐 Translate", callback_data="mode:translate")
    kb.button(text="🗑 Reset memory", callback_data="mem:reset")
    kb.adjust(2, 2, 1)
    return kb.as_markup()

@router.message(CommandStart())
async def start_handler(message: types.Message):
    mode = await repo.get_mode(message.from_user.id)
    await message.answer(
        f"Salom! ✅\nHozirgi rejim: <b>{mode}</b>\n\nRejim tanlang 👇",
        reply_markup=menu_kb()
    )

@router.callback_query(F.data.startswith("mode:"))
async def set_mode_handler(cb: types.CallbackQuery):
    mode = cb.data.split(":", 1)[1]
    await repo.set_mode(cb.from_user.id, mode)
    await cb.answer(f"Mode: {mode} ✅")
    await cb.message.edit_text(
        f"✅ Rejim o‘rnatildi: <b>{mode}</b>\nEndi matn yuboring.",
        reply_markup=menu_kb()
    )

@router.callback_query(F.data == "mem:reset")
async def reset_memory_handler(cb: types.CallbackQuery):
    await repo.reset_history(cb.from_user.id)
    await cb.answer("Memory reset ✅")
    await cb.message.edit_text(
        "🗑 Memory tozalandi.\nRejim tanlang yoki matn yuboring.",
        reply_markup=menu_kb()
    )
