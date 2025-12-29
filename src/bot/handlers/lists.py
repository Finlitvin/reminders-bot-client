from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler, MessageHandler

from bot.utils.database import lists__
from bot.keyboards.lists import lists_keyboard
from bot.constants.messages import Messages
from bot.constants.callbacks import Callbacks
from bot.handlers.filters.lists import SHOW_LIST_FILTER


async def show_lists(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    keyboard = lists_keyboard(lists__)
    text = Messages.SHOW_LISTS.value

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
        MessageHandler(SHOW_LIST_FILTER, show_lists),
        CallbackQueryHandler(
            show_lists,
            pattern=Callbacks.BACK.pattern,
        ),
    ]
