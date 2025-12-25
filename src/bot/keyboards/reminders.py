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


def reminder_action_keyboard(reminder_id: int):
    return (
        InlineKeyboardBuilder()
        .buttons(
            [
                {
                    "text": "☑️",
                    "callback_data": f"{Callbacks.reminder_done(reminder_id)}",
                },
                {
                    "text": "🗑️",
                    "callback_data": (
                        f"{Callbacks.reminder_delete(reminder_id)}"
                    ),
                },
                {
                    "text": "✏️",
                    "callback_data": f"{Callbacks.reminder_edit(reminder_id)}",
                },
            ],
        )
        .button("⬅️", Callbacks.BACK.value)
        .build()
    )
