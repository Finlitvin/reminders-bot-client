from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

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


def get_handlers() -> list:
    return [
        CommandHandler(Commands.START.value, start_command),
    ]
