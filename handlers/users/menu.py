from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from keyboards.default import menu
from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer('выберите из меню ниже', reply_markup=menu)


@dp.message_handler(text='Kotletki')
async def get_kotletki(message: types.Message):
    await message.answer('you choose the Kotletki')


@dp.message_handler(Text(equals=['Pureshka', 'Macaroni']))
async def get_food(message: types.Message):
    await message.answer(f'you choose {message.text}', reply_markup=types.ReplyKeyboardRemove())

