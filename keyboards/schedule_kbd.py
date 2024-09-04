from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class ScheduleTypeSelectionCallbackFactory(CallbackData, prefix="schedule_type_selection"):
    action: str


class ScheduleDayBackCallbackFactory(CallbackData, prefix="schedule_day_back"):
    action: str


def get_schedule_type_selection_keyboard_fab():
    builder = InlineKeyboardBuilder()

    builder.button(text="Расписание на сегодня", callback_data=ScheduleTypeSelectionCallbackFactory(action="today"))
    builder.button(text="Расписание на завтра", callback_data=ScheduleTypeSelectionCallbackFactory(action="tomorrow"))
    builder.button(text="Настраиваемое расписание", callback_data=ScheduleTypeSelectionCallbackFactory(action="custom"))

    builder.adjust(1)

    return builder.as_markup()


def get_schedule_day_back_keyboard_fab():
    builder = InlineKeyboardBuilder()

    builder.button(text="Назад к выбору", callback_data=ScheduleDayBackCallbackFactory(action="back"))

    builder.adjust(1)

    return builder.as_markup()
