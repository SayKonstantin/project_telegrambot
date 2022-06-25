from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states import Test


@dp.message_handler(Command('test'))
async def enter_test(message: types.Message):
    await message.answer('вы начали тестирование')
    await Test.Q1.set()


# await Test.first()

@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(asnwer1=answer)
    await message.answer('Вопрос № 2\n'
                         'blablabla')
    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get('answer1')
    answer2 = message.text

    await message.answer('спасибо за ваши ответы')
    await message.answer(f'Ответ 1 : {answer1}')
    await message.answer(f'Ответ 2 : {answer2}')


    # вариант 1
    await state.finish()

    # вариант 2
    #await state.reset_state(#with_data=False)
