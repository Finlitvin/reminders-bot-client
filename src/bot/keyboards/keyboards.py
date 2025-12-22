from bot.keyboards.builders import ReplyKeyboardBuilder, InlineKeyboardBuilder
from bot.constants.callbacks import CallbackData
from bot.constants.messages import MessagesData


def main_menu_keyboard():
    return (
        ReplyKeyboardBuilder()
        .resize()
        .button(MessagesData.REMINDER_LIST.value)
        .button(MessagesData.SETTINGS.value)
        .build()
    )


def reminder_list_keyboard(reminder_list: list):
    inline_keyboard = InlineKeyboardBuilder()

    for reminder in reminder_list:
        text = f"{reminder.get("icon")} {reminder.get("name")}"

        inline_keyboard.button(
            text,
            callback_data=CallbackData.reminder_list_select(reminder.get("id"))
        )

    return inline_keyboard.build()
