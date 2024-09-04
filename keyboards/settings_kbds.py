from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class SettingsMenuCallbackFactory(CallbackData, prefix="settings_menu"):
    action: str


def get_settings_menu_keyboard_fab(need_notification: bool = True):
    builder_1 = InlineKeyboardBuilder()
    builder_2 = InlineKeyboardBuilder()
    builder_3 = InlineKeyboardBuilder()
    builder_all = InlineKeyboardBuilder()

    builder_1.button(text="Измен. имя", callback_data=SettingsMenuCallbackFactory(action="name"))
    builder_1.button(text="Измен. группу", callback_data=SettingsMenuCallbackFactory(action="group"))
    builder_1.adjust(2)

    if need_notification:
        builder_2.button(text="Выкл. рассылку",
                         callback_data=SettingsMenuCallbackFactory(action="notification_off"))
    else:
        builder_2.button(text="Вкл. рассылку",
                         callback_data=SettingsMenuCallbackFactory(action="notification_on"))
    builder_2.button(text="Измен. время", callback_data=SettingsMenuCallbackFactory(action="time"))
    builder_2.adjust(2)

    builder_3.button(text="Я староста", callback_data=SettingsMenuCallbackFactory(action="chef"))
    builder_3.button(text="Информация", callback_data=SettingsMenuCallbackFactory(action="info"))
    builder_3.adjust(2)

    builder_all.attach(builder_1)
    builder_all.attach(builder_2)
    builder_all.attach(builder_3)

    return builder_all.as_markup()
