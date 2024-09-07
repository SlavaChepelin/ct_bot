from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

import datetime


class GroupSelectionCallbackFactory(CallbackData, prefix="group_selection"):
    action: int


class ConsentToUpdatesCallbackFactory(CallbackData, prefix="consent_to_updates"):
    action: bool


class TimeSelectionCallbackFactory(CallbackData, prefix="time_selection"):
    action: int


def get_group_selection_keyboard_fab():
    builder_1 = InlineKeyboardBuilder()
    builder_2 = InlineKeyboardBuilder()
    builder_3 = InlineKeyboardBuilder()
    builder_all = InlineKeyboardBuilder()

    for i in range(32, 36):
        builder_1.button(text=f"M31{i}", callback_data=GroupSelectionCallbackFactory(action=(i + 100)))
    builder_1.adjust(4)

    for i in range(36, 40):
        builder_2.button(text=f"M31{i}", callback_data=GroupSelectionCallbackFactory(action=(i + 100)))
    builder_2.adjust(4)

    for i in range(41, 43):
        builder_3.button(text=f"M31{i}", callback_data=GroupSelectionCallbackFactory(action=(i + 100)))
    builder_3.adjust(2)

    builder_all.attach(builder_1)
    builder_all.attach(builder_2)
    builder_all.attach(builder_3)

    return builder_all.as_markup()


def get_consent_to_updates_keyboard_fab():
    builder = InlineKeyboardBuilder()

    builder.button(text="Да", callback_data=ConsentToUpdatesCallbackFactory(action=True))
    builder.button(text="Нет", callback_data=ConsentToUpdatesCallbackFactory(action=False))

    builder.adjust(2)

    return builder.as_markup()


def get_time_selection_keyboard_fab():
    builder_1 = InlineKeyboardBuilder()
    builder_2 = InlineKeyboardBuilder()
    builder_3 = InlineKeyboardBuilder()
    builder_4 = InlineKeyboardBuilder()
    builder_all = InlineKeyboardBuilder()

    builder_1.button(text="В вечер перед парами", callback_data=TimeSelectionCallbackFactory(action=0))
    builder_1.adjust(1)

    builder_2.button(text="18:00", callback_data=TimeSelectionCallbackFactory(action=18))
    builder_2.button(text="20:00", callback_data=TimeSelectionCallbackFactory(action=20))
    builder_2.button(text="22:00", callback_data=TimeSelectionCallbackFactory(action=22))
    builder_2.adjust(3)

    builder_3.button(text="На утро перед парами", callback_data=TimeSelectionCallbackFactory(action=0))
    builder_3.adjust(1)

    builder_4.button(text="7:00", callback_data=TimeSelectionCallbackFactory(action=7))
    builder_4.button(text="8:00", callback_data=TimeSelectionCallbackFactory(action=8))
    builder_4.button(text="9:00", callback_data=TimeSelectionCallbackFactory(action=9))
    builder_4.adjust(3)

    builder_all.attach(builder_1)
    builder_all.attach(builder_2)
    builder_all.attach(builder_3)
    builder_all.attach(builder_4)

    return builder_all.as_markup()
