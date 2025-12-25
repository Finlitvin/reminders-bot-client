from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler

from bot.utils.database import lists__
from bot.keyboards.lists import lists_keyboard
from bot.constants.messages import Messages
from bot.constants.callbacks import Callbacks


async def show_lists(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    keyboard = lists_keyboard(lists__)
    text = Messages.LISTS.value

    if update.message:
        await update.message.reply_text(
            text,
            reply_markup=keyboard,
        )
    elif update.callback_query:
        await update.callback_query.edit_message_text(
            text,
            reply_markup=keyboard,
        )


def get_handlers() -> list:
    return [
        CallbackQueryHandler(
            show_lists,
            pattern=Callbacks.BACK.value,
        )
    ]
