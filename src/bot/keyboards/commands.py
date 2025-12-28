from bot.keyboards.builders import ReplyKeyboardBuilder
from bot.constants.buttons import Buttons


def main_menu_keyboard():
    return (
        ReplyKeyboardBuilder()
        .resize()
        .button(Buttons.LISTS.value)
        .button(Buttons.ADD.value)
        .button(Buttons.SETTINGS.value)
        .build()
    )
