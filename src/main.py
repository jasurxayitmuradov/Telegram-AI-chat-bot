import asyncio
from aiogram import Bot, Dispatcher

from src.config import BOT_TOKEN
from src.handlers import start
from src.storage.db import init_db

async def main():
    await init_db() 

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
