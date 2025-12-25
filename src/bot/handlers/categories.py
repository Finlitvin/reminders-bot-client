from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler

from bot.utils.database import lists__, categories__
from bot.constants.callbacks import PATTERNS
from bot.keyboards.categories import categories_keyboard


async def show_categories(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    list_id = int(update.callback_query.data.split("$")[1])

    categories = categories__[list_id]
    if len(categories) == 1 and categories[0].get("name") == "DEFAULT":
        # await show_reminders(update, context)
        pass
    else:
        text = f"{lists__[list_id].get('icon')}{lists__[list_id].get('name')}"
        await update.callback_query.edit_message_text(
            text, reply_markup=categories_keyboard(categories__[list_id])
        )


def get_handlers() -> list:
    return [
        CallbackQueryHandler(
            show_categories,
            pattern=PATTERNS["list_select"],
        )
    ]
