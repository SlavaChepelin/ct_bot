import os
from dotenv import load_dotenv

import asyncio
import logging

from aiogram import Bot, Dispatcher

from handlers import start, admin


load_dotenv()
token: str = os.getenv("TOKEN")

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=token)
    dp = Dispatcher()

    dp.include_routers(start.start_router,
                       admin.admin_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
