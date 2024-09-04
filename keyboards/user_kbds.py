from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class ScheduleTypeSelectionCallbackFactory(CallbackData, prefix="schedule_type_selection"):
    action: int


class ScheduleDayBackCallbackFactory(CallbackData, prefix="schedule_day_back"):
    action: int


def get_schedule_type_selection_keyboard_fab():
    builder = InlineKeyboardBuilder()

    builder.button(text="Расписание на сегодня", callback_data=ScheduleTypeSelectionCallbackFactory(action=0))
    builder.button(text="Расписание на завтра", callback_data=ScheduleTypeSelectionCallbackFactory(action=1))
    builder.button(text="Настраиваемое расписание", callback_data=ScheduleTypeSelectionCallbackFactory(action=2))

    builder.adjust(1)

    return builder.as_markup()


menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗓️"),
            KeyboardButton(text="⚙️")
        ]
    ], resize_keyboard=True
)

delete_kb = ReplyKeyboardRemove()


