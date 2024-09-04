from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

import datetime

from keyboards.user_kbds import (ScheduleTypeSelectionCallbackFactory,
                                 ScheduleDayBackCallbackFactory,
                                 get_schedule_type_selection_keyboard_fab,
                                 get_schedule_day_back_keyboard_fab,
                                 menu_kb)

from scripts.forms import get_schedule
from scripts.db_users import get_user


user_router = Router()


@user_router.message(F.text == "🗓️")
async def send_schedule_selection(message: Message):
    await message.answer("Выберите опцию:", reply_markup=get_schedule_type_selection_keyboard_fab())


@user_router.callback_query(ScheduleDayBackCallbackFactory.filter())
async def send_schedule_selection(callback: CallbackQuery, callback_data: ScheduleDayBackCallbackFactory):
    await callback.message.edit_text("Выберите опцию:")
    await callback.message.edit_reply_markup(reply_markup=get_schedule_type_selection_keyboard_fab())


@user_router.callback_query(ScheduleTypeSelectionCallbackFactory.filter())
async def send_schedule(callback: CallbackQuery, callback_data: ScheduleTypeSelectionCallbackFactory):

    if callback_data.action == "today" or callback_data.action == "tomorrow":
        text = "Расписание\n\n"

        if callback_data.action == "today":
            date = datetime.date.today()
        else:
            date = datetime.date(2024, 9, 5)

        group_id: tuple = await get_user(callback.from_user.id)
        schedule_list = await get_schedule(group_id[4], str(date).replace("-", "."))

        print(group_id[4], date, schedule_list)

        for line in schedule_list:
            text += line + "\n"

    else:
        text = "Мне лень было это писать"

    await callback.message.edit_text(text)
    await callback.message.edit_reply_markup(reply_markup=get_schedule_day_back_keyboard_fab())
