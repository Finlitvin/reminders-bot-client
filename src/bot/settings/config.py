from functools import lru_cache

from src.bot.settings.base import BaseBotSettings


class BotSettings(BaseBotSettings):
    telegram_token: str
    developer_chat_id: str


@lru_cache
def get_bot_settings() -> BotSettings:
    return BotSettings()
