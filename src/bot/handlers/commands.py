from telegram import Update
from telegram.ext import (
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)

from bot.handlers.lists import show_lists
from bot.keyboards.commands import main_menu_keyboard
from bot.constants.commands import Commands
from bot.constants.messages import Messages


async def start_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    user = update.effective_user

    text = Messages.start(user.first_name)
    reply_markup = main_menu_keyboard()

    if update.message:
        await update.message.reply_text(text, reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.edit_message_text(
            text, reply_markup=reply_markup
        )


async def handle_main_menu(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    text = update.message.text

    if text == Messages.LISTS.value:
        await show_lists(update, context)

    elif text == Messages.SETTINGS.value:
        pass


def get_handlers() -> list:
    return [
        CommandHandler(Commands.START.value, start_command),
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_main_menu),
    ]
