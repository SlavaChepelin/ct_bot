from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.filters import Command, StateFilter
from aiogram.types import Message

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from scripts import db_users

basic_router = Router()


class AddInfo(StatesGroup):
    first_name = State()
    last_name = State()
    group_id = State()
    need_update = State()
    update_time = State()


@basic_router.message(StateFilter(None), CommandStart())
async def start(message: Message, state: FSMContext):
    await db_users.add_user(message.from_user.id, message.from_user.username)

    await message.answer("Здравствуйте, "
                         "мы рады что вы решили воспользоваться нашим ботом для расписания занятий на КТ!\n\n"
                         "Для работы пожалуйста введите ваши данные.\n"
                         "Сначала напишите своё имя.")

    await state.set_state(AddInfo.first_name)


@basic_router.message(AddInfo.first_name, F.text)
async def add_first_name(message: Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await message.answer(f"Приятно познакомиться, {message.text}!\n\n"
                         f"Теперь пожалуйста введите вашу фамилию.")

    await state.set_state(AddInfo.last_name)


@basic_router.message(AddInfo.last_name, F.text)
async def add_last_name(message: Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await message.answer(f"В какой группе вы учитесь?")

    await state.set_state(AddInfo.need_update)




'''
@basic_router.message(Command("get_users"))
async def get_user_data(message: Message):
    result = await db_users.get_user(message.from_user.id)
    await message.answer(   str(result[0]) + " " + result[1])

@basic_router.message(Command("update_groups"))
async def update_group(message: Message):
    result = await db_users.get_user(message.from_user.id)
    await message.answer(str(result[0]) + " " + str(result[4]))
    await db_users.update_user_group(message.from_user.id,39)
    result = await db_users.get_user(message.from_user.id)
    await message.answer(str(result[0]) + " " + str(result[4]))
'''