from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

def menu_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="💬 Chat", callback_data="menu:chat")
    kb.button(text="ℹ️ Help", callback_data="menu:help")
    kb.adjust(2)
    return kb.as_markup()

@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "Salom! Men Telegram botman ✅\nQuyidan tanlang:",
        reply_markup=menu_kb()
    )

@router.callback_query()
async def menu_handler(callback: types.CallbackQuery):
    data = callback.data or ""
    if data == "menu:chat":
        await callback.answer("Chat tanlandi ✅")
        await callback.message.answer("Menga istalgan xabar yozing (hozir echo).")
    elif data == "menu:help":
        await callback.answer("Help ✅")
        await callback.message.answer("Bu demo bot. Keyin AI qo‘shamiz.")
    else:
        await callback.answer()
