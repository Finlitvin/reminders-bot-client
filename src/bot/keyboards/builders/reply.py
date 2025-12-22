from telegram import ReplyKeyboardMarkup

from bot.keyboards.builders.abc import KeyboardBuilder


class ReplyKeyboardBuilder(KeyboardBuilder):
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
