from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import types, Dispatcher

from ..misc.states import FSM_Admin_addArticle

from ..keyboards.admin_inline import ADMIN_PANEL
from ..keyboards.admin_inline import ADD_ARTICLE
from ..keyboards.admin_inline import ADD_EXIT
from ..keyboards.reply import ADD_CLOSE
from ..keyboards.admin_inline import CHECK_ARTICLE
from ..keyboards.admin_inline import CHANGE_ARTICLE_MENU
from ..keyboards.admin_inline import CHANGE_ARTICLE_EXIT


# adding an article about a product to the database
async def addArticleStart(callback: types.CallbackQuery, state: FSMContext):
    current_filter = callback.data.split(":")[1]
    if current_filter == "start":
        await callback.message.edit_text('Загрузи фото, если оно необходимо', reply_markup=ADD_ARTICLE())
        await callback.answer()
        await FSM_Admin_addArticle.photo.set()


# photo == true
async def loadPhoto(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['statusPhoto'] = 1
        data['statusChangePhoto'] = 0
        data['photo'] = message.photo[0].file_id
    await FSM_Admin_addArticle.next()
    await message.answer('Теперь добавим статью\n!уведомить \
                   [LIMIT]:4000', reply_markup=ADD_EXIT())


# photo == false
async def articleNonePhoto(callback: types.CallbackQuery, state: FSMContext):
    current_filter = callback.data.split(":")[1]
    if current_filter == "NonePhoto":
        async with state.proxy() as data:
            data['statusChangePhoto'] = 0
            data['statusPhoto'] = 0
        await FSM_Admin_addArticle.next()
        await callback.message.edit_text('Напиши статью\n!уведомить \
                    [LIMIT]:4000', reply_markup=ADD_EXIT())


# add article
async def addArticle(message: Message, state: FSMContext):

    async with state.proxy() as data:
        if data['statusChangePhoto'] == 1:
            data['photo'] = message.photo[0].file_id
        else:
            data['article'] = message.text

    async with state.proxy() as data:
        if data['statusPhoto'] == 0 and data['statusChangePhoto'] == 0:
            await message.answer("Теперь давай проверим, все ли верно", reply_markup=ReplyKeyboardRemove())
            await message.answer(f"{data['article']}",
                                 reply_markup=CHECK_ARTICLE())
        elif data['statusPhoto'] == 1 and data['statusChangePhoto'] == 0:
            await message.answer("Теперь давай проверим, все ли верно", reply_markup=ReplyKeyboardRemove())
            await message.answer_photo(str(data['photo']), f"{data['article']}",
                                       reply_markup=CHECK_ARTICLE())
        # elif data['statusPhoto'] == 1 and data['statusChange'] == 1:
            # await message.answer("Теперь давай проверим, все ли верно", reply_markup=ReplyKeyboardRemove())
            # await message.answer_photo(str(data['photo']), f"{data['article']}",
            #                            reply_markup=CHECK_ARTICLE())


# save an article to the database
async def CallbackSaveArticle(callback: types.CallbackQuery, state: FSMContext):
    current_TypesQuer = callback.data.split(":")[1]
    if current_TypesQuer == "article":
        await state.finish()
        await callback.message.delete()
        await callback.message.answer('Статья сохранена\n\nТы вернулся в панель администратра',
                                      reply_markup=ADMIN_PANEL())
    await callback.answer()


# change article
async def ChangeArticleMenu(callback: types.CallbackQuery, state: FSMContext):
    current_TypesQuer = callback.data.split(":")[1]
    async with state.proxy() as data:

        if current_TypesQuer == "article" and data['statusPhoto'] == 1:
            data['statusChangePhoto'] = 1
            await callback.message.answer('Что меняем?',
                                          reply_markup=CHANGE_ARTICLE_MENU())
            await FSM_Admin_addArticle.article()

        if current_TypesQuer == "article" and data['statusPhoto'] == 0:
            data['statusChangePhoto'] = 0
            await callback.message.answer('Что меняем?',
                                          reply_markup=CHANGE_ARTICLE_EXIT('photo'))
            await FSM_Admin_addArticle.article()
    await callback.answer()


# selecting the article modification mode
async def ChangeArticle(callback: types.CallbackQuery, state: FSMContext):
    current_TypesQuer = callback.data.split(":")[1]
    async with state.proxy() as data:
        if current_TypesQuer == "article" and data['statusPhoto'] == 1:
            await callback.message.answer('Что меняем?',
                                          reply_markup=CHANGE_ARTICLE_MENU())
        else:
            await callback.message.answer('Что меняем?',
                                          reply_markup=CHANGE_ARTICLE_EXIT('photo'))
    await callback.answer()


# registering a handler to add a article
def register_addArticle(dp: Dispatcher):
    dp.register_callback_query_handler(addArticleStart, Text(
        startswith="addArticleStart:"), state=None, is_admin=True)
    dp.register_message_handler(
        loadPhoto, content_types=['photo'], state=FSM_Admin_addArticle.photo)
    dp.register_message_handler(
        addArticle, state=FSM_Admin_addArticle.article)
    dp.register_callback_query_handler(articleNonePhoto, Text(startswith="addArticle:"),
                                       state=FSM_Admin_addArticle.photo)
    dp.register_callback_query_handler(CallbackSaveArticle, Text(startswith="save:"),
                                       state=FSM_Admin_addArticle.article)
    dp.register_callback_query_handler(ChangeArticleMenu, Text(startswith="change:"),
                                       state=FSM_Admin_addArticle.article)
    dp.register_callback_query_handler(ChangeArticle, Text(startswith="CHANGE_ARTICLE:"),
                                       state=FSM_Admin_addArticle.article)
