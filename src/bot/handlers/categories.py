from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler

from bot.utils.database import lists__, categories__
from bot.constants.callbacks import Callbacks
from bot.keyboards.categories import categories_keyboard
from bot.handlers.reminders import show_reminders


async def show_categories(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    list_id = int(update.callback_query.data.split("$")[1])
    context.user_data["list_id"] = list_id

    categories = categories__[list_id]
    if len(categories) == 1 and categories[0].get("name") == "DEFAULT":
        await show_reminders(update, context)
    else:
        text = f"{lists__[list_id].get('icon')} {lists__[list_id].get('name')}"
        await update.callback_query.edit_message_text(
            text, reply_markup=categories_keyboard(categories)
        )


def get_handlers() -> list:
    return [
        CallbackQueryHandler(
            show_categories,
            pattern=Callbacks.LIST_SELECT.pattern,
        )
    ]
