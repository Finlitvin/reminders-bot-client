from telegram import Update
from telegram.ext import (
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
)


from bot.utils.formatters import format_welcome_message
from bot.keyboards.keyboards import (
    main_menu_keyboard,
    reminder_list_keyboard,
    section_list_keyboard,
)
from bot.constants.commands import CommandsData
from bot.constants.messages import MessagesData
from bot.constants.callbacks import CallbackData

reminder_list__ = [
    {
        "id": 0,
        "name": "Входящие",
        "icon": "📥",
    },
    {
        "id": 1,
        "name": "Следующие действия",
        "icon": "⏭️",
    },
    {
        "id": 2,
        "name": "Проекты",
        "icon": "👨‍💻",
    },
    {
        "id": 3,
        "name": "Запланировано",
        "icon": "🗓️",
    },
    {
        "id": 4,
        "name": "Когда-нибудь",
        "icon": "🤷‍♂️",
    },
]

section_list__ = [
    [
        {
            "id": 0,
            "name": "DEFAULT",
            "icon": "",
        },
    ],
    [
        {
            "id": 1,
            "name": "Программирование",
            "icon": "",
        },
        {
            "id": 2,
            "name": "Виш-лист",
            "icon": "",
        },
    ],
    [
        {
            "id": 3,
            "name": "Разово",
            "icon": "",
        },
        {
            "id": 4,
            "name": "Здоровье",
            "icon": "",
        },
    ],
]


async def start_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    user = update.effective_user

    text = format_welcome_message(user.first_name)
    reply_markup = main_menu_keyboard()

    if update.message:
        await update.message.reply_text(text, reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.edit_message_text(
            text, reply_markup=reply_markup
        )


async def main_menu_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    text = update.message.text

    if text == MessagesData.REMINDER_LIST.value:
        await reminder_list_handler(update, context)

    elif text == MessagesData.SETTINGS.value:
        pass


async def reminder_list_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    if update.message:
        await update.message.reply_text(
            MessagesData.REMINDER_LIST.value,
            reply_markup=reminder_list_keyboard(reminder_list__),
        )
    elif update.callback_query:
        await update.callback_query.edit_message_text(
            MessagesData.REMINDER_LIST.value,
            reply_markup=reminder_list_keyboard(reminder_list__),
        )


async def sections_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    list_id = int(
        update.callback_query.data.split(CallbackData.SPLIT_SYMBOL.value)[1]
    )
    text = f"{reminder_list__[list_id].get('icon')} {reminder_list__[list_id].get('name')}"
    await update.callback_query.edit_message_text(
        text, reply_markup=section_list_keyboard(section_list__[list_id])
    )


def get_handlers():
    return [
        CommandHandler(CommandsData.START.value, start_command),
        MessageHandler(filters.TEXT & ~filters.COMMAND, main_menu_handler),
        CallbackQueryHandler(
            reminder_list_handler, pattern=f"^{CallbackData.BACK.value}"
        ),
        CallbackQueryHandler(
            sections_handler,
            pattern=f"^{CallbackData.split_symbol(CallbackData.REMINDER_LIST_SELECT.value)}",
        ),
    ]
