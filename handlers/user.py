from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from keyboards.schedule_kbd import get_schedule_type_selection_keyboard_fab
from keyboards.settings_kbds import get_settings_menu_keyboard_fab

user_router = Router()


@user_router.message(F.text == "🗓️")
async def send_schedule_selection(message: Message):
    await message.answer("Выберите опцию:", reply_markup=get_schedule_type_selection_keyboard_fab())


@user_router.message(F.text == "⚙️")
async def send_settings_selection(message: Message):
    await message.answer("Выберите опцию:", reply_markup=get_settings_menu_keyboard_fab())
