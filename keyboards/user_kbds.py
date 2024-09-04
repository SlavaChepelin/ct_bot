from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗓️"),
            KeyboardButton(text="⚙️")
        ]
    ], resize_keyboard=True
)

delete_kb = ReplyKeyboardRemove()
