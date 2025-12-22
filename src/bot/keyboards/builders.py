from abc import ABC, abstractmethod

from telegram import (
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
)


class KeyboardBuilderInterface(ABC):
    """Общий интерфейс для всех клавиатурных билдеров"""

    @abstractmethod
    def button(self, text: str, **kwargs) -> "KeyboardBuilderInterface":
        """Добавить одну кнопку"""
        pass

    @abstractmethod
    def buttons(
        self, texts: list[str], **kwargs
    ) -> "KeyboardBuilderInterface":
        """Добавить несколько кнопок в строку"""
        pass

    @abstractmethod
    def build(self) -> InlineKeyboardMarkup | ReplyKeyboardMarkup:
        """Построить клавиатуру"""
        pass


class InlineKeyboardBuilder(KeyboardBuilderInterface):
    def __init__(self):
        self._rows = []

    def button(self, text: str, callback_data: str, **kwargs):
        self._rows.append(
            [{"text": text, "callback_data": callback_data, **kwargs}]
        )
        return self

    def buttons(self, texts: list[str], callback_prefix: str):
        row = [
            {"text": t, "callback_data": f"{callback_prefix}_{i}"}
            for i, t in enumerate(texts)
        ]
        self._rows.append(row)
        return self

    def build(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(self._rows)


class ReplyKeyboardBuilder(KeyboardBuilderInterface):
    def __init__(self):
        self._rows = []
        self._resize = True
        self._one_time = False

    def button(self, text: str):
        self._rows.append([{"text": text}])
        return self

    def buttons(self, texts: list[str]):
        self._rows.append([{"text": t} for t in texts])
        return self

    def resize(self):
        self._resize = True
        return self

    def build(self) -> ReplyKeyboardMarkup:
        return ReplyKeyboardMarkup(self._rows, resize_keyboard=self._resize)
