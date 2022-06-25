from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Вот что я умею: ",
            "/weather - сообщаю о погоде за окном",
            "/currency - делюсь курсом валют",
            "/start -  приветствую тебя",
            "/help - вывожу справку")
    
    await message.answer("\n".join(text))
