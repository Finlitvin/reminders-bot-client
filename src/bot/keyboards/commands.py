from bot.keyboards.builders import ReplyKeyboardBuilder
from bot.constants.messages import Messages


def main_menu_keyboard():
    return (
        ReplyKeyboardBuilder()
        .resize()
        .button(Messages.LISTS.value)
        .button(Messages.SETTINGS.value)
        .build()
    )
