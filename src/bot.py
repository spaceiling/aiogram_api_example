import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text

from src.messages import MESSAGES
from src.stickers import STICKERS
import src.keyboards as kb

from dotenv import load_dotenv
import os

if os.getenv("GITHUB_ACTIONS"):
    bot_token = os.getenv("BOT_API_TOKEN")
else:
    load_dotenv()
    bot_token = os.getenv("BOT_API_TOKEN")


bot = Bot(token=bot_token)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(Command('start'), state='*')
async def start(message: types.Message):    
    await bot.send_sticker(message.chat.id, STICKERS['hello'])
    await bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! 👋 \n\n" + MESSAGES['start'], 
                           reply_markup=kb.greet_kb, parse_mode='Markdown')

@dp.message_handler(Text(equals='Привет! 👋'))
async def hello_button_click(message: types.Message):
    await bot.send_message(message.chat.id, f"{message.from_user.first_name}, {MESSAGES['finish_onboarding']}")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await bot.send_message(message.chat.id, f"{MESSAGES['help']}", reply_markup=None)

async def on_shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=on_shutdown)