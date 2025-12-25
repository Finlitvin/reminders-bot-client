from bot.keyboards.builders import InlineKeyboardBuilder
from bot.constants.callbacks import Callbacks


def reminders_keyboard(reminders: list):
    builder = InlineKeyboardBuilder()

    for reminder in reminders:
        text = f"{reminder.get('tittle')}"

        builder.button(
            text,
            callback_data=Callbacks.reminder_select(reminder.get("id")),
        )

    builder.button("⬅️", Callbacks.BACK.value)

    return builder.build()


def reminder_action_keyboard():
    return (
        InlineKeyboardBuilder()
        .buttons(
            [
                {"text": "☑️", "callback_data": "reminder_done"},
                {"text": "🗑️", "callback_data": "reminder_delete"},
                {"text": "✏️", "callback_data": "reminder_edit"},
            ],
        )
        .button("⬅️", Callbacks.BACK.value)
        .build()
    )
