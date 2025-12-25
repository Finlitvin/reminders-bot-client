from bot.keyboards.builders import InlineKeyboardBuilder
from bot.constants.callbacks import Callbacks


def lists_keyboard(lists: list):
    builder = InlineKeyboardBuilder()

    for lst in lists:
        text = f"{lst.get('icon')} {lst.get('name')}"

        builder.button(
            text,
            callback_data=Callbacks.list_select(lst.get("id")),
        )

    return builder.build()
