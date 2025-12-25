from bot.keyboards.builders import InlineKeyboardBuilder
from bot.constants.callbacks import Callbacks


def categories_keyboard(categories: list):
    builder = InlineKeyboardBuilder()

    for category in categories:
        text = f"{category.get('icon')} {category.get('name')}"

        builder.button(
            text,
            callback_data=Callbacks.category_select(category.get("id")),
        )

    builder.button("⬅️", Callbacks.BACK.value)

    return builder.build()
