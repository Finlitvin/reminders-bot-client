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
    reminders_keyboard,
)
from bot.constants.commands import CommandsData
from bot.constants.messages import MessagesData
from bot.constants.callbacks import CallbackData, PATTERNS


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
    [
        {
            "id": 0,
            "name": "DEFAULT",
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

reminders__ = [
    [
        {
            "id": 0,
            "tittle": "Закинуть стирку",
            "date": "12-07-25",
            "time": "14:30",
            "description": "Только цветное белье",
            "status": "done",
        },
        {
            "id": 1,
            "tittle": "Почистить обувь",
            "date": "12-07-25",
            "time": "14:30",
            "description": "",
            "status": "not_done",
        },
        {
            "id": 2,
            "tittle": "Купить крем для рук",
            "date": "12-07-25",
            "time": "",
            "description": "",
            "status": "not_done",
        },
    ],
    [
        {
            "id": 0,
            "tittle": "Закинуть стирку",
            "date": "12-07-25",
            "time": "14:30",
            "description": "Только цветное белье",
            "status": "done",
        },
        {
            "id": 1,
            "tittle": "Почистить обувь",
            "date": "12-07-25",
            "time": "14:30",
            "description": "",
            "status": "not_done",
        },
        {
            "id": 2,
            "tittle": "Купить крем для рук",
            "date": "12-07-25",
            "time": "",
            "description": "",
            "status": "not_done",
        },
    ],
    [
        {
            "id": 0,
            "tittle": "Закинуть стирку",
            "date": "12-07-25",
            "time": "14:30",
            "description": "Только цветное белье",
            "status": "done",
        },
        {
            "id": 1,
            "tittle": "Почистить обувь",
            "date": "12-07-25",
            "time": "14:30",
            "description": "",
            "status": "not_done",
        },
        {
            "id": 2,
            "tittle": "Купить крем для рук",
            "date": "12-07-25",
            "time": "",
            "description": "",
            "status": "not_done",
        },
    ],
    [
        {
            "id": 0,
            "tittle": "Закинуть стирку",
            "date": "12-07-25",
            "time": "14:30",
            "description": "Только цветное белье",
            "status": "done",
        },
        {
            "id": 1,
            "tittle": "Почистить обувь",
            "date": "12-07-25",
            "time": "14:30",
            "description": "",
            "status": "not_done",
        },
        {
            "id": 2,
            "tittle": "Купить крем для рук",
            "date": "12-07-25",
            "time": "",
            "description": "",
            "status": "not_done",
        },
    ],
    [
        {
            "id": 0,
            "tittle": "Закинуть стирку",
            "date": "12-07-25",
            "time": "14:30",
            "description": "Только цветное белье",
            "status": "done",
        },
        {
            "id": 1,
            "tittle": "Почистить обувь",
            "date": "12-07-25",
            "time": "14:30",
            "description": "",
            "status": "not_done",
        },
        {
            "id": 2,
            "tittle": "Купить крем для рук",
            "date": "12-07-25",
            "time": "",
            "description": "",
            "status": "not_done",
        },
    ]
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
        await show_reminder_list(update, context)

    elif text == MessagesData.SETTINGS.value:
        pass


async def show_reminder_list(
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


async def show_sections(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    list_id = int(
        update.callback_query.data.split(CallbackData.SPLIT_SYMBOL.value)[1]
    )

    sections = section_list__[list_id]
    if len(sections) == 1 and sections[0].get("name") == "DEFAULT":
        await show_reminders(update, context)
    else:
        text = (
            f"{reminder_list__[list_id].get('icon')}"
            f"{reminder_list__[list_id].get('name')}"
        )
        await update.callback_query.edit_message_text(
            text, reply_markup=section_list_keyboard(section_list__[list_id])
        )


async def show_reminders(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    section_id = int(
        update.callback_query.data.split(CallbackData.SPLIT_SYMBOL.value)[1]
    )

    await update.callback_query.edit_message_text(
        "Напоминания: ",
        reply_markup=reminders_keyboard(reminders__[section_id])
    )



def get_handlers():
    return [
        CommandHandler(CommandsData.START.value, start_command),
        MessageHandler(filters.TEXT & ~filters.COMMAND, main_menu_handler),
        CallbackQueryHandler(
            show_reminder_list, pattern=f"^{CallbackData.BACK.value}"
        ),
        CallbackQueryHandler(
            show_sections,
            pattern=PATTERNS["reminder_list"],
        ),
        CallbackQueryHandler(
            show_reminders,
            pattern=PATTERNS["section"],
        ),
    ]
