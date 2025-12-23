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
        text = f"{reminder.get('icon')} {reminder.get('name')}"

        inline_keyboard.button(
            text,
            callback_data=CallbackData.reminder_list_id(
                reminder.get("id")
            ),
        )

    return inline_keyboard.build()


def section_list_keyboard(section_list: list):
    inline_keyboard = InlineKeyboardBuilder()

    for section in section_list:
        text = f"{section.get('icon')} {section.get('name')}"

        inline_keyboard.button(
            text,
            callback_data=CallbackData.section_id(section.get("id")),
        )
    inline_keyboard.button("⬅️", CallbackData.BACK.value)

    return inline_keyboard.build()


def reminders_keyboard(reminders: list):
    inline_keyboard = InlineKeyboardBuilder()

    for reminder in reminders:
        text = f"{reminder.get('tittle')}"

        inline_keyboard.button(
            text,
            callback_data=CallbackData.reminder_id(reminder.get("id")),
        )
    inline_keyboard.button("⬅️", CallbackData.BACK.value)

    return inline_keyboard.build()
