from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from scripts import db_schedule


admin_router = Router()
admin_router.message.filter()


@admin_router.message(Command("dbplus"))
async def dbplus(message: Message):
    await db_schedule.add_schedule_plus(39, "2024.09.01", 2, "Матан", "пр", 2444, "Кохась" )
    
@admin_router.message(Command("dbminus"))
async def dbminus(message: Message):
    await db_schedule.add_schedule_minus(39, "2024.09.01", 2)

