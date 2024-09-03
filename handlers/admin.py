from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from scripts import db_schedule


admin_router = Router()
admin_router.message.filter()


@admin_router.message(Command("db"))
async def admin_start(message: Message):
    await db_schedule.add_schedule_change("M1", "", 1, "", "", "")
    await message.answer("База создана")
