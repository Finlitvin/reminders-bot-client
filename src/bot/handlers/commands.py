from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters


from bot.utils.formatters import format_welcome_message
from bot.keyboards.keyboards import main_menu_keyboard, reminder_list_keyboard
from bot.constants.commands import CommandsData
from bot.constants.messages import MessagesData

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
    }
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
        await update.message.reply_text(
            MessagesData.REMINDER_LIST.value,
            reply_markup=reminder_list_keyboard(reminder_list__)
        )

    elif text == MessagesData.SETTINGS.value:
        pass


def get_handlers():
    return [
        CommandHandler(CommandsData.START.value, start_command),
        MessageHandler(filters.TEXT & ~filters.COMMAND, main_menu_handler),
    ]
