from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F
from bot_config import db

dish_router = Router()

)

class Dish(StatesGroup):
    name = State()
    price = State()
    description = State()
    category = State()
    porsion = State()


@dish_router.message(Command('dish_add'))
async def start_dish(message, state: FSMContext):
    await message.answer('what is dish name ?')
    await state.set_state(Dish.name)


@dish_router.message(Dish.name)
async def process_name(m: types.Message, state: FSMContext):
    await state.update_data(name=m.text)
    await m.answer("what is price ")
    await state.set_state(Dish.price)


@dish_router.message(Dish.price)
async def process_price(m: types.Message, state: FSMContext):
    await state.update_data(price=m.text)
    await m.answer("add description?")
    await state.set_state(Dish.description)


@dish_router.message(Dish.description)
async def process_description(m: types.Message, state: FSMContext):
    await state.update_data(description=m.text)
    await m.answer("what is the category?")
    await state.set_state(Dish.category)


@dish_router.message(Dish.category)
async def process_category(m,state):
    await state.update_data(cat=m.text)
    await m.answer("what is the porsion")
    await state.set_state(Dish.porsion)



@dish_router.message(Dish.porsion)
async def process_portion(m: types.Message, state: FSMContext):
    await state.update_data(portion=m.text)
    data = await state.get_data()
    await m.answer(
        f'name:{data["name"]}\nprice:{data["price"]}\ndescription:{data["description"]}\ncategory:{data["cat"]}\nporsion:{data["portion"]}')
    db.save_dish(data)
    await state.clear()
