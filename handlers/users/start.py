import asyncio

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from .help import bot_help
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
    await asyncio.sleep(0.8)
    await bot_help(message)
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("menu", " Показать меню еды"),
            types.BotCommand("weather", "Узнать погоду")

        ]
    )




# @dp.message_handler(content_types=types.Location)
# async def geo(message):
#     await message.answer()
