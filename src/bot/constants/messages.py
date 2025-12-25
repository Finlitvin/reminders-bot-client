from enum import Enum


class Messages(str, Enum):
    LISTS = "📋 Список напоминаний"
    SETTINGS = "⚙️ Настройки"
    START = "👋 Привет, {username}!"

    @classmethod
    def start(cls, username: str) -> str:
        return cls.START.value.format(username=username)
