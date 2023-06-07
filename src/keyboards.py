from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

greet_kb = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(KeyboardButton('Привет! 👋'))