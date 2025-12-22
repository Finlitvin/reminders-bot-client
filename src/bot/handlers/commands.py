from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters


from bot.utils.formatters import format_welcome_message
from bot.keyboards.keyboards import get_main_menu


async def start_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    user = update.effective_user

    text = format_welcome_message(user.first_name)
    reply_markup = get_main_menu()

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

    if text == "Список напоминаний":
        await update.message.reply_text("Управление напоминаниями:")


def get_handlers():
    return [
        CommandHandler("start", start_command),
        MessageHandler(filters.TEXT & ~filters.COMMAND, main_menu_handler),
    ]
