from aiogram import types
from aiogram.types import Message, InlineKeyboardButton, \
    InlineKeyboardMarkup, ReplyKeyboardRemove


def MENU_ADM():
    buttons = [
        [
            types.InlineKeyboardButton(
                text="📄 админпанель",
                callback_data="menuAdm:adminpanel"
            )
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=buttons
    )
    return keyboard


def ADMIN_PANEL():
    buttons = [
        [
            types.InlineKeyboardButton(
                text='Добавить статью',
                callback_data="addArticleStart:start"
            ),
            types.InlineKeyboardButton(
                text='Добавить вопрос-ответ',
                callback_data="addDecisionStart:start"
            )
        ],
        [
            types.InlineKeyboardButton(
                text='Назад',
                callback_data="startAdm:back"
            )
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=buttons
    )
    return keyboard


def ADD_EXIT():
    buttons = [
        [
            types.InlineKeyboardButton(
                text='отменить добавление',
                callback_data="END:state"
            )
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=buttons
    )
    return keyboard


def ADD_ARTICLE():
    buttons = [
        [
            types.InlineKeyboardButton(
                text='добавить без фотографии',
                callback_data="addArticle:NonePhoto"
            ),
            types.InlineKeyboardButton(
                text='отменить добавление',
                callback_data="END:state"
            )
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=buttons
    )
    return keyboard


def CHECK_DECISION():
    buttons = [
        [
            types.InlineKeyboardButton(
                text='Сохранить',
                callback_data="save:decision"
            ),
            types.InlineKeyboardButton(
                text='Изменить',
                callback_data="change:decision"
            )
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=buttons
    )
    return keyboard

def CHECK_ARTICLE():
    buttons = [
        [
            types.InlineKeyboardButton(
                text='Сохранить',
                callback_data="save:article"
            ),
            types.InlineKeyboardButton(
                text='Изменить',
                callback_data="change:article"
            )
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=buttons
    )
    return keyboard

def CHANGE_DECISION():
    buttons = [
        [
            types.InlineKeyboardButton(
                text='Фотографию',
                callback_data="HotelRoom:photo"
            )
        ],
        [
            types.InlineKeyboardButton(
                text='Тип(имя)',
                callback_data="HotelRoom:name"
            ),
            types.InlineKeyboardButton(
                text='Описание',
                callback_data="HotelRoom:description"
            )
        ],
        [
            types.InlineKeyboardButton(
                text='Колличество',
                callback_data="HotelRoom:current_count"
            ),
            types.InlineKeyboardButton(
                text='Цену',
                callback_data="HotelRoom:price"
            )
        ],
        [
            types.InlineKeyboardButton(
                text='Создать заново',
                callback_data="HotelRoom:update"
            )
        ],
        [
            types.InlineKeyboardButton(
                text='Я передумал, сохраняем',
                callback_data="save:HotelRoom"
            )

        ],
    ]
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=buttons
    )
    return keyboard

def CHANGE_ARTICLE_MENU(val = 'default'):
    if val == 'default':
        buttons = [
            [
                types.InlineKeyboardButton(
                    text='Изменить фотографию',
                    callback_data="CHANGE_ARTICLE_photo:upd"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text='Текст статьи',
                    callback_data="CHANGE_ARTICLE_article:text"
                )
            ]
        ]
    else :
        buttons = [
        [
            types.InlineKeyboardButton(
                text='Добавить фотографию',
                callback_data="CHANGE_ARTICLE_photo:add"
            )
        ],
        [
            types.InlineKeyboardButton(
                text='Текст статьи',
                callback_data="CHANGE_ARTICLE_article:text"
            )
        ]
    ]

    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=buttons
    )
    return keyboard

def CHANGE_ARTICLE_EXIT():
    buttons = [
        [
            types.InlineKeyboardButton(
                text='отменить изменение',
                callback_data="CHANGE_EXIT:article"
            )
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=buttons
    )
    return keyboard