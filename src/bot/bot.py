from telegram.ext import ApplicationBuilder

from bot.handlers import get_all_handlers
from bot.handlers.errors import error_handler
from bot.settings.config import get_bot_settings


def setup_bot():
    settings = get_bot_settings()

    application = ApplicationBuilder().token(settings.telegram_token).build()

    application.add_error_handler(error_handler)
    application.add_handlers(get_all_handlers())

    return application


def run_bot():
    bot = setup_bot()
    bot.run_polling()
