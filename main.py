from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values
import logging
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import choice
import asyncio

token = dotenv_values('.env')['TOKEN']
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command('start'))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Начать работу с ботом', callback_data='start')],
        [InlineKeyboardButton(text='Случайное имя', callback_data='random')],
        [InlineKeyboardButton(text='Информация о себе', callback_data='myinfo')]
    ])

    await message.answer(f'Привет {name}\n'
                         f'Мои комманды:', reply_markup=keyboard)


@dp.message(Command('random'))
async def random_handler(message: types.Message):
    name_list = choice(['Jim', 'Jessie', 'Aisuluu', 'Jasmina', 'Suga'])
    await message.answer(f'Случайное имя: {name_list}')


@dp.message(Command('myinfo'))
async def myinfo_handler(message: types.Message):
    id = message.from_user.id
    name = message.from_user.first_name
    nickname = message.from_user.username
    await message.answer(f'Ваше имя: {name}'
                         f'Ваш nickname:{nickname}'
                         f'Ваш id {id}')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
