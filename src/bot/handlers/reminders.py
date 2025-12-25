from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler

from bot.utils.database import reminders__
from bot.keyboards.reminders import (
    reminders_keyboard,
    reminder_action_keyboard,
)
from bot.constants.callbacks import PATTERNS


async def show_reminders(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    category_id = int(update.callback_query.data.split("$")[1])

    keyboard = reminders_keyboard(reminders__[category_id])

    await update.callback_query.edit_message_text(
        "Напоминания: ",
        reply_markup=keyboard,
    )


async def show_reminder(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    reminder_id = int(update.callback_query.data.split("$")[1])
    reminder = reminders__[0][reminder_id]

    text = (
        f"{reminder.get('tittle')}\n"
        f"{reminder.get('description')}\n"
        f"Дата: {reminder.get('date')}\n"
        f"Время: {reminder.get('time')}\n"
        f"Статус: {reminder.get('status')}\n"
    )
    keyboard = reminder_action_keyboard(reminder_id)

    if update.message:
        await update.message.reply_text(
            text,
            reply_markup=keyboard,
        )
    elif update.callback_query:
        await update.callback_query.edit_message_text(
            text,
            reply_markup=keyboard,
        )


async def delete_reminder(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    reminder_id = int(update.callback_query.data.split("$")[1])
    print(reminder_id)


async def edit_reminder(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    reminder_id = int(update.callback_query.data.split("$")[1])
    print(reminder_id)


async def mark_reminder_done(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    reminder_id = int(update.callback_query.data.split("$")[1])
    status = reminders__[0][reminder_id]["status"]

    if status == "done":
        reminders__[0][reminder_id]["status"] = "not_done"
    else:
        reminders__[0][reminder_id]["status"] = "done"

    await show_reminder(update, context)


def get_handlers() -> list:
    return [
        CallbackQueryHandler(
            show_reminders,
            pattern=PATTERNS["category_select"],
        ),
        CallbackQueryHandler(
            show_reminder,
            pattern=PATTERNS["reminder_select"],
        ),
        CallbackQueryHandler(
            delete_reminder,
            pattern=PATTERNS["reminder_delete"],
        ),
        CallbackQueryHandler(
            edit_reminder,
            pattern=PATTERNS["reminder_edit"],
        ),
        CallbackQueryHandler(
            mark_reminder_done,
            pattern=PATTERNS["reminder_done"],
        ),
    ]
