from enum import Enum


class Buttons(str, Enum):
    LISTS = "📋 Список напоминаний"
    SETTINGS = "⚙️ Настройки"
    ADD = "➕ Добавить напоминание"
