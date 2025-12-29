from enum import Enum


class Messages(str, Enum):
    START = "👋 Привет, {username}!"
    SHOW_LISTS = "📋 Список напоминаний"

    @classmethod
    def start(cls, username: str) -> str:
        return cls.START.value.format(username=username)
