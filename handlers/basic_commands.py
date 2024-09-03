from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from kbds.basic_kbds import (GroupSelectionCallbackFactory, ConsentToUpdatesCallbackFactory,
                             TimeSelectionCallbackFactory,
                             get_group_selection_keyboard_fab, get_consent_to_updates_keyboard_fab,
                             get_time_selection_keyboard_fab)

from scripts import db_users

basic_router = Router()


class AddInfo(StatesGroup):
    first_name = State()
    last_name = State()
    group_id = State()
    need_update = State()
    time_selection = State()


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
    await message.answer(f"В какой группе вы учитесь?", reply_markup=get_group_selection_keyboard_fab())

    await state.set_state(AddInfo.group_id)


@basic_router.callback_query(AddInfo.group_id,
                             GroupSelectionCallbackFactory.filter())
async def add_group_selection(callback: CallbackQuery,
                              callback_data: GroupSelectionCallbackFactory,
                              state: FSMContext):
    await state.update_data(group_id=callback_data.action)

    await callback.message.answer(f"Спасибо, записана группа M3{callback_data.action}.\n\n"
                                  f"Теперь скажите, хотите ли вы получать ежедневную рассылку?",
                                  reply_markup=get_consent_to_updates_keyboard_fab())

    await state.set_state(AddInfo.need_update)
    await callback.answer()


@basic_router.callback_query(AddInfo.need_update,
                             ConsentToUpdatesCallbackFactory.filter())
async def add_consent_to_updates(callback: CallbackQuery,
                                 callback_data: ConsentToUpdatesCallbackFactory,
                                 state: FSMContext):
    await state.update_data(need_update=callback_data.action)

    if callback_data.action:
        await callback.message.answer("Вы подписались на рассылку.\n"
                                      "Вы можете отказаться от неё в любой момент.\n\n"
                                      "Выберете время, в которое вам удобно получать расписание.",
                                      reply_markup=get_time_selection_keyboard_fab())
        await state.set_state(AddInfo.time_selection)

    else:
        await callback.message.answer("Вы отказались от рассылки.\n"
                                      "Вы можете подписаться на неё в любой момент.")
        await state.set_state(None)

    await callback.answer()


@basic_router.callback_query(AddInfo.time_selection, TimeSelectionCallbackFactory.filter())
async def add_time_selection(callback: CallbackQuery,
                             callback_data: TimeSelectionCallbackFactory,
                             state: FSMContext):
    await state.update_data(time_selection=callback_data.action)

    await callback.message.answer(f"Спасибо большое, вы выбрали получать уведомления в {callback_data.action}:00.")

    data: dict = await state.get_data()

    await db_users.update_user_group(callback.from_user.id, data["group_id"])
    await db_users.update_user_name(callback.from_user.id, data["first_name"], data["last_name"])
    await db_users.update_user_updates(callback.from_user.id, data["need_update"])
    await db_users.update_user_update_time(callback.from_user.id, data["time_selection"])

    await state.set_state(None)
    await callback.answer()



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