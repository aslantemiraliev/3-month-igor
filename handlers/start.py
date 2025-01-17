from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram import types
from aiogram.types import InlineKeyboardMarkup

start_router = Router()

kb = types.InlineKeyboardMarkup(inline_keyboard=[
    [types.InlineKeyboardButton(text='Review', callback_data='review')],
    [types.InlineKeyboardButton(text='Advertising', callback_data='advertising')],
    [types.InlineKeyboardButton(text='Catalog of dishes', callback_data='catalog of dishes')]
])


@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f'Привет {name}', reply_markup=kb)
