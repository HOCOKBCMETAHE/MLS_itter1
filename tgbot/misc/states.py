from aiogram.dispatcher.filters.state import State, StatesGroup


# FSM ADMINS
class FSM_Admin_AddConferenceRoom(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


class FSM_Admin_addDecision(StatesGroup):
    question = State()
    decision = State()
    checksave = State()


class FSM_Admin_addArticle(StatesGroup):
    photo = State()
    article = State()
    checksave = State()
