from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram import types
from keyboards.inline.choice_buttons import choice


@dp.message_handler(Command('items'))
async def show_items(message: types.Message):
    await message.answer(text='вот наши товары.\n'
                              'если ничего не нужно - нажмите отмену', reply_markup=choice)
