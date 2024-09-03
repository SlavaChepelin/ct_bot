from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from scripts import db_users

basic_router = Router()


@basic_router.message(CommandStart())
async def start(message: Message):
    await db_users.add_user(message.from_user.id,
                            message.from_user.username,
                            message.from_user.first_name,
                            message.from_user.last_name)

    await message.answer("Мы рады что вы решили воспользоваться нашим ботом!")
    await message.answer("Подскажите, из какой вы группы?")
