from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from requests import get
import json
from loader import dp
from aiogram.utils.emoji import emojize


@dp.message_handler(Command('currency'))
async def get_courses(message: types.Message):
    r_eu = get('https://api.tinkoff.ru/v1/currency_rates?from=EUR&to=RUB').text
    r_usd = get('https://api.tinkoff.ru/v1/currency_rates?from=USD&to=RUB').text
    data_eu = json.loads(r_eu)
    data_usd = json.loads(r_usd)
    eu_sell = data_eu['payload']['rates'][5]['buy']
    eu_buy = data_eu['payload']['rates'][5]['sell']
    usd_sell = data_usd['payload']['rates'][5]['buy']
    usd_buy = data_usd['payload']['rates'][5]['sell']

    await message.answer(text='<b>Курсы валют Тинькофф</b>\n\n'
                              f'{emojize("💵")}\n'
                              f'{usd_buy} / {usd_sell}\n\n'
                              f'{emojize("💶")}\n'
                              f'{eu_buy} / {eu_sell}\n\n')
