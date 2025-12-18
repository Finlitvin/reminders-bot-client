from telegram.ext import ApplicationBuilder

from src.bot.settings.config import get_bot_settings


def setup_bot():
    settings = get_bot_settings()

    application = ApplicationBuilder().token(settings.telegram_token).build()

    return application


def run_bot():
    bot = setup_bot()
    bot.run_polling()
