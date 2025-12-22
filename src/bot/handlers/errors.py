import html
import json
import traceback

from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

from bot.settings.config import get_bot_settings


settings = get_bot_settings()


async def error_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    tb_list = traceback.format_exception(
        None, context.error, context.error.__traceback__
    )
    tb_string = "".join(tb_list)

    update_str = (
        update.to_dict() if isinstance(update, Update) else str(update)
    )

    html_update = html.escape(
        json.dumps(update_str, indent=2, ensure_ascii=False)
    )
    html_chat_data = html.escape(str(context.chat_data))
    html_user_data = html.escape(str(context.user_data))

    text = (
        "An exception was raised while handling an updatex"
        f"<pre>update = {html_update}"
        "</pre>\n\n"
        f"<pre>context.chat_data = {html_chat_data}</pre>\n\n"
        f"<pre>context.user_data = {html_user_data}</pre>\n\n"
        f"<pre>{html.escape(tb_string)}</pre>"
    )

    await context.bot.send_message(
        chat_id=settings.developer_chat_id,
        text=text,
        parse_mode=ParseMode.HTML,
    )

    if not update and not update.effective_user:
        return

    text = (
        "⚠️ Произошла ошибка при обработке вашего запроса. "
        "Попробуйте еще раз или обратитесь к администратору."
    )
    try:
        await update.effective_user.send_message(text)
    except Exception:
        pass
