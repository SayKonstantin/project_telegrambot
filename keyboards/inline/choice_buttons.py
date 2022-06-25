import logging

from aiogram import types
from callback_datas import buy_callback
from loader import dp, bot

choice = types.InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        types.InlineKeyboardButton(text='купить IPHONE',
                                   callback_data=buy_callback.new(item_name='iphone', quantity=1)),
        types.InlineKeyboardButton(text='купить MACBOOK', callback_data=buy_callback('buy:apple:5'))
    ],
    [
        types.InlineKeyboardButton(text='Отмена', callback_data=buy_callback('cancel'))
    ]
])


@dp.message_handler(buy_callback.filter(item_name='iphone'))
async def buying_iphone(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    quantity = callback_data.get('quantity')
    await call.message.answer(quantity)
