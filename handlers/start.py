from aiogram import Router, F
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message, CallbackQuery

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards.start_kbds import (GroupSelectionCallbackFactory, ConsentToUpdatesCallbackFactory,
                                  TimeSelectionCallbackFactory,
                                  get_group_selection_keyboard_fab, get_consent_to_updates_keyboard_fab,
                                  get_time_selection_keyboard_fab)

from scripts import db_users


start_router = Router()


class AddInfo(StatesGroup):
    first_name = State()
    last_name = State()
    group_id = State()
    need_update = State()
    time_selection = State()


@start_router.message(StateFilter(None), CommandStart())
async def start(message: Message, state: FSMContext) -> None:
    text_1 = "Здравствуйте, мы рады что вы решили воспользоваться нашим ботом для расписания занятий на КТ!\n\n"

    await db_users.add_user(message.from_user.id, message.from_user.username)
    is_filled = await db_users.is_filled(message.from_user.id)

    if is_filled:
        text_2 = "Вы уже ввели свои данные, хотите их поменять?"

    else:
        text_2 = "Для работы пожалуйста введите ваши данные.\nСначала напишите своё имя."

        await state.set_state(AddInfo.first_name)

    await message.answer(text_1 + text_2)


@start_router.message(AddInfo.first_name, F.text)
async def add_first_name(message: Message, state: FSMContext) -> None:
    await state.update_data(first_name=message.text)
    await message.answer(f"Приятно познакомиться, {message.text}!\n\n"
                         f"Теперь пожалуйста введите вашу фамилию.")

    await state.set_state(AddInfo.last_name)


@start_router.message(AddInfo.last_name, F.text)
async def add_last_name(message: Message, state: FSMContext) -> None:
    await state.update_data(last_name=message.text)
    await message.answer(f"В какой группе вы учитесь?", reply_markup=get_group_selection_keyboard_fab())

    await state.set_state(AddInfo.group_id)


@start_router.callback_query(AddInfo.group_id, GroupSelectionCallbackFactory.filter())
async def add_group_selection(callback: CallbackQuery,
                              callback_data: GroupSelectionCallbackFactory,
                              state: FSMContext) -> None:
    await state.update_data(group_id=callback_data.action)

    await callback.message.edit_text(f"Спасибо, записана группа M3{callback_data.action}.\n\n"
                                     f"Теперь скажите, хотите ли вы получать ежедневную рассылку?")
    await callback.message.edit_reply_markup(reply_markup=get_consent_to_updates_keyboard_fab())

    await state.set_state(AddInfo.need_update)
    await callback.answer()


@start_router.callback_query(AddInfo.need_update, ConsentToUpdatesCallbackFactory.filter())
async def add_consent_to_updates(callback: CallbackQuery,
                                 callback_data: ConsentToUpdatesCallbackFactory,
                                 state: FSMContext) -> None:
    await state.update_data(need_update=callback_data.action)

    if callback_data.action:
        await callback.message.edit_text("Вы подписались на рассылку.\n"
                                         "Вы можете отказаться от неё в любой момент.\n\n"
                                         "Выберете время, в которое вам удобно получать расписание.", )
        await callback.message.edit_reply_markup(reply_markup=get_time_selection_keyboard_fab())

        await state.set_state(AddInfo.time_selection)

    else:
        await callback.message.edit_text("Вы отказались от рассылки.\n"
                                         "Вы можете подписаться на неё в любой момент.")
        await state.set_state(None)

    await callback.answer()


@start_router.callback_query(AddInfo.time_selection, TimeSelectionCallbackFactory.filter())
async def add_time_selection(callback: CallbackQuery,
                             callback_data: TimeSelectionCallbackFactory,
                             state: FSMContext) -> None:
    await state.update_data(time_selection=callback_data.action)

    await callback.message.edit_text(f"Спасибо большое, вы выбрали получать уведомления в {callback_data.action}:00.")

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
