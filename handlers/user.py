from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.user_kbds import ScheduleTypeSelectionCallbackFactory, get_schedule_type_selection_keyboard_fab, menu_kb


user_router = Router()


@user_router.message(F.text == "🗓️")
async def send_schedule_selection(message: Message):
    await message.answer("Выберите опцию:", reply_markup=get_schedule_type_selection_keyboard_fab())
