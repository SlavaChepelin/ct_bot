import os
from dotenv import load_dotenv

import datetime

import asyncio
import logging

from aiogram import Bot, Dispatcher

from handlers import start, test, user, schedule, settings

load_dotenv()
token: str = os.getenv("TOKEN")

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=token)
    dp = Dispatcher()

    dp.include_routers(start.start_router,
                       user.user_router,
                       schedule.schedule_router,
                       settings.settings_router,
                       test.test_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    #thread = threading.Thread(target=looper)
    #thread.start()
    asyncio.run(main())
