from aiogram import Router

from aiogram.types import Message, CallbackQuery

import datetime

from keyboards.schedule_kbd import (ScheduleDayBackCallbackFactory, ScheduleTypeSelectionCallbackFactory,
                                    get_schedule_day_back_keyboard_fab, get_schedule_type_selection_keyboard_fab)

from scripts.formatting import get_schedule
from scripts.db_users import get_user


schedule_router = Router()


@schedule_router.callback_query(ScheduleDayBackCallbackFactory.filter())
async def send_schedule_selection(callback: CallbackQuery, callback_data: ScheduleDayBackCallbackFactory):
    await callback.message.edit_text("Выберите опцию:")
    await callback.message.edit_reply_markup(reply_markup=get_schedule_type_selection_keyboard_fab())


@schedule_router.callback_query(ScheduleTypeSelectionCallbackFactory.filter())
async def send_schedule(callback: CallbackQuery, callback_data: ScheduleTypeSelectionCallbackFactory):
    if callback_data.action == "today" or callback_data.action == "tomorrow":
        text = "Расписание\n\n"
        date = datetime.date.today()

        if callback_data.action == "tomorrow":
            date = date + datetime.timedelta(days=1)

        group_id: tuple = await get_user(callback.from_user.id)
        schedule_list = await get_schedule(group_id[4], str(date).replace("-", "."))

        print(group_id[4], date, schedule_list)

        for line in schedule_list:
            text += line + "\n"

    else:
        text = "Мне лень было это писать"

    await callback.message.edit_text(text)
    await callback.message.edit_reply_markup(reply_markup=get_schedule_day_back_keyboard_fab())
