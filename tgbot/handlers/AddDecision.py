from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import types, Dispatcher

from ..misc.states import FSM_Admin_addDecision

from ..keyboards.admin_inline import ADMIN_PANEL
from ..keyboards.admin_inline import ADD_DECISION
from ..keyboards.reply import ADD_ROOM_CLOSE
from ..keyboards.admin_inline import CHECK_DECISION
from ..keyboards.admin_inline import CHANGE_DECISION


async def addDecisionStart(callback: types.CallbackQuery, state: FSMContext):
    current_filter = callback.data.split(":")[1]
    if current_filter == "decision":
        await callback.message.edit_text('На какой вопрос отвечаем?', reply_markup= ADD_DECISION())
        await callback.answer()
        await FSM_Admin_addDecision.question.set()

async def loadQuestion(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['question'] = message.text
    await FSM_Admin_addDecision.next()
    await message.answer('Введи ответ на вопрос', reply_markup=ADD_ROOM_CLOSE())
    # await callback.answer()

# async def add_name(message: Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['name'] = message.text
#     await FSM_Admin_addDecision.next()
#     await message.answer('Введи описание номера')

# async def add_description(message: Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['description'] = message.text
#     await FSM_Admin_addDecision.next()
#     await message.answer('Введи количество номеров данного типа')

# async def add_count(message: Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['count']=int(message.text)
#     await FSM_Admin_addDecision.next()
#     await message.answer('Введи цену номера')

async def addDecision(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['decision']= message.text

    async with state.proxy() as data:
        await message.answer("Теперь давай проверим, все ли верно", reply_markup= ReplyKeyboardRemove())
        await message.answer(f"Ожидаемый вопрос: \n{data['question']}\n\nОтвет: \n{data['decision']}", reply_markup= CHECK_DECISION())
        # await message.answer(text=f'{str(data)}', reply_markup= CHECK_ROOM())

async def CallbackSaveDecision(callback: types.CallbackQuery, state: FSMContext):
    current_TypesRoom = callback.data.split(":")[1]

    if current_TypesRoom == "decision":
        await state.finish()
        await callback.message.delete()
        await callback.message.answer('Вопрос и ответ успешно сохранены\n\nТы вернулся в панель администратра', \
            reply_markup= ADMIN_PANEL())
    await callback.answer()
    
async def CallbackChangeRoom(callback: types.CallbackQuery, state: FSMContext):
    current_TypesRoom = callback.data.split(":")[1]

    if current_TypesRoom == "photo":
        await callback.message.delete()
        await callback.message.answer('Номер успешно сохранен\n\nТы вернулся в панель администратра', \
            reply_markup= ADMIN_PANEL())
    await callback.answer()

def register_addDecision(dp: Dispatcher):
    dp.register_callback_query_handler(addDecisionStart, Text(startswith="addMain:"), state=None, is_admin=True)

    # dp.register_message_handler(retypeHotelroom, state=FSM_Admin_addDecision.retype)
    # dp.register_message_handler(retypeHotelroom, Text(startswith="addRoom:"), state=FSM_Admin_addDecision.retype)

    dp.register_message_handler(loadQuestion, state=FSM_Admin_addDecision.question)
    dp.register_message_handler(addDecision, state=FSM_Admin_addDecision.decision)
    dp.register_callback_query_handler(CallbackSaveDecision, Text(startswith="save:"), state=FSM_Admin_addDecision.decision)
    dp.register_callback_query_handler(CallbackChangeRoom, Text(startswith="addMain:"), state=FSM_Admin_addDecision.decision)