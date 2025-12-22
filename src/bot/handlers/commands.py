from telegram import Update
from telegram.ext import ContextTypes

from bot.utils.formatters import format_welcome_message


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    text = format_welcome_message(user.first_name)

    if update.message:
        await update.message.reply_text(text)
    elif update.callback_query:
        await update.callback_query.edit_message_text(text)
