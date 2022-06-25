from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp
import requests
import json
from data.config import WEATHER_TOKEN


@dp.message_handler(Command('weather'))
async def show_shop(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    await message.answer("А где ты?",
                         reply_markup=keyboard)


async def make_request(longitude, latitude):
    r = requests.request(method='GET',
                         url=f'https://api.weather.yandex.ru/v2/forecast?lat={latitude}&lon={longitude}&extra=true',
                         headers={'X-Yandex-API-Key': WEATHER_TOKEN})
    openweather_dict = json.loads(r.content)
    return openweather_dict["fact"]


@dp.message_handler(content_types=["location"])
async def location(message):
    if message.location is not None:
        weather = await make_request(message.location.longitude, message.location.latitude)
        await message.answer(text=f'За окном {weather["temp"]} градусов. Скорость ветра {weather["wind_speed"]} м/с',
                             reply_markup=types.ReplyKeyboardRemove())
