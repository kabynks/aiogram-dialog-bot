from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)
main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Получить цены'),
        ]

    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True,

)