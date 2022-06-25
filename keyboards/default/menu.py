from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Kotletki')],
        [KeyboardButton(text='Macaroni'), KeyboardButton(text='Pureshka')]],
    resize_keyboard=True
)
