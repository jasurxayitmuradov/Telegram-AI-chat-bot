import asyncio
from aiogram import Bot, Dispatcher

from src.config import BOT_TOKEN
from src.handlers import start

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
